# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.02x faster
- HPT reliability: 99.11%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 270 ms: 1.01x faster                                       |
| chameleon      | 7.41 ms                                                | 6.87 ms: 1.08x faster                                      |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                     |
| tornado_http   | 103 ms                                                 | 96.8 ms: 1.06x faster                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 446 ms: 1.06x faster                                       |
| async_tree_none_tg         | 450 ms                                                 | 447 ms: 1.00x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 734 ms: 1.01x slower                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 586 ms: 1.02x slower                                       |
| async_tree_io_tg           | 1.18 sec                                               | 1.21 sec: 1.03x slower                                     |
| async_tree_io              | 1.16 sec                                               | 1.21 sec: 1.05x slower                                     |
| Geometric mean             | (ref)                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 89.5 ms: 1.08x faster                                      |
| float          | 84.7 ms                                                | 82.0 ms: 1.03x faster                                      |
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                       |
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                      |
| regex_dna      | 212 ms                                                 | 230 ms: 1.08x slower                                       |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.16 sec: 1.08x faster                                     |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                       |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                       |
| pickle_dict          | 35.5 us                                                | 33.8 us: 1.05x faster                                      |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                      |
| pickle_list          | 5.08 us                                                | 4.98 us: 1.02x faster                                      |
| xml_etree_generate   | 89.2 ms                                                | 87.4 ms: 1.02x faster                                      |
| unpickle_list        | 5.29 us                                                | 5.25 us: 1.01x faster                                      |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                      |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| xml_etree_parse      | 159 ms                                                 | 161 ms: 1.01x slower                                       |
| Geometric mean       | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (3): xml_etree_iterparse, unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 10.4 ms: 1.08x slower                                      |
| python_startup_no_site | 6.94 ms                                                | 8.92 ms: 1.29x slower                                      |
| Geometric mean         | (ref)                                                  | 1.18x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.3 ms: 1.06x faster                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 110 us: 1.44x faster                                       |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.34x faster                                      |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                       |
| deltablue                  | 3.72 ms                                                | 3.23 ms: 1.15x faster                                      |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                       |
| crypto_pyaes               | 81.9 ms                                                | 72.3 ms: 1.13x faster                                      |
| chaos                      | 67.0 ms                                                | 59.9 ms: 1.12x faster                                      |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                       |
| logging_format             | 7.23 us                                                | 6.53 us: 1.11x faster                                      |
| logging_simple             | 6.46 us                                                | 5.89 us: 1.10x faster                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 68.6 ms: 1.10x faster                                      |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                       |
| nbody                      | 97.0 ms                                                | 89.5 ms: 1.08x faster                                      |
| tomli_loads                | 2.33 sec                                               | 2.16 sec: 1.08x faster                                     |
| chameleon                  | 7.41 ms                                                | 6.87 ms: 1.08x faster                                      |
| deepcopy_reduce            | 3.35 us                                                | 3.11 us: 1.08x faster                                      |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                      |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                       |
| generators                 | 31.2 ms                                                | 29.2 ms: 1.07x faster                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                      |
| deepcopy_memo              | 40.7 us                                                | 38.4 us: 1.06x faster                                      |
| tornado_http               | 103 ms                                                 | 96.8 ms: 1.06x faster                                      |
| deepcopy                   | 371 us                                                 | 350 us: 1.06x faster                                       |
| async_tree_none            | 472 ms                                                 | 446 ms: 1.06x faster                                       |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.06x faster                                      |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                       |
| pickle_dict                | 35.5 us                                                | 33.8 us: 1.05x faster                                      |
| hexiom                     | 6.41 ms                                                | 6.10 ms: 1.05x faster                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                      |
| pathlib                    | 19.3 ms                                                | 18.5 ms: 1.05x faster                                      |
| scimark_fft                | 382 ms                                                 | 366 ms: 1.05x faster                                       |
| pprint_safe_repr           | 776 ms                                                 | 745 ms: 1.04x faster                                       |
| coroutines                 | 23.2 ms                                                | 22.3 ms: 1.04x faster                                      |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                       |
| fannkuch                   | 417 ms                                                 | 402 ms: 1.04x faster                                       |
| float                      | 84.7 ms                                                | 82.0 ms: 1.03x faster                                      |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                     |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.03x faster                                       |
| nqueens                    | 83.3 ms                                                | 80.7 ms: 1.03x faster                                      |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                      |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                       |
| dulwich_log                | 68.5 ms                                                | 66.8 ms: 1.03x faster                                      |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                       |
| pyflate                    | 482 ms                                                 | 471 ms: 1.02x faster                                       |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.02x faster                                     |
| mdp                        | 2.63 sec                                               | 2.58 sec: 1.02x faster                                     |
| async_generators           | 463 ms                                                 | 454 ms: 1.02x faster                                       |
| pickle_list                | 5.08 us                                                | 4.98 us: 1.02x faster                                      |
| xml_etree_generate         | 89.2 ms                                                | 87.4 ms: 1.02x faster                                      |
| 2to3                       | 274 ms                                                 | 270 ms: 1.01x faster                                       |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                       |
| bench_mp_pool              | 24.0 ms                                                | 23.8 ms: 1.01x faster                                      |
| unpickle_list              | 5.29 us                                                | 5.25 us: 1.01x faster                                      |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                      |
| async_tree_none_tg         | 450 ms                                                 | 447 ms: 1.00x faster                                       |
| gc_traversal               | 3.79 ms                                                | 3.78 ms: 1.00x faster                                      |
| go                         | 139 ms                                                 | 140 ms: 1.00x slower                                       |
| asyncio_tcp                | 491 ms                                                 | 493 ms: 1.00x slower                                       |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                       |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| xml_etree_parse            | 159 ms                                                 | 161 ms: 1.01x slower                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.10 ms: 1.01x slower                                      |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                     |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 734 ms: 1.01x slower                                       |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.01x slower                                       |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                      |
| aiohttp                    | 1.15 ms                                                | 1.17 ms: 1.02x slower                                      |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                       |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 586 ms: 1.02x slower                                       |
| asyncio_websockets         | 551 ms                                                 | 563 ms: 1.02x slower                                       |
| gunicorn                   | 1.24 ms                                                | 1.27 ms: 1.02x slower                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.51 ms: 1.02x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.02x slower                                     |
| json                       | 5.26 ms                                                | 5.39 ms: 1.03x slower                                      |
| async_tree_io_tg           | 1.18 sec                                               | 1.21 sec: 1.03x slower                                     |
| async_tree_io              | 1.16 sec                                               | 1.21 sec: 1.05x slower                                     |
| richards                   | 45.8 ms                                                | 48.9 ms: 1.07x slower                                      |
| richards_super             | 51.5 ms                                                | 55.1 ms: 1.07x slower                                      |
| python_startup             | 9.55 ms                                                | 10.4 ms: 1.08x slower                                      |
| regex_dna                  | 212 ms                                                 | 230 ms: 1.08x slower                                       |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                      |
| telco                      | 7.10 ms                                                | 8.55 ms: 1.20x slower                                      |
| python_startup_no_site     | 6.94 ms                                                | 8.92 ms: 1.29x slower                                      |
| coverage                   | 72.7 ms                                                | 95.8 ms: 1.32x slower                                      |
| Geometric mean             | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (9): async_tree_memoization, xml_etree_iterparse, async_tree_cpu_io_mixed, sqlglot_optimize, bench_thread_pool, unpickle, django_template, json_loads, mypy2
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (7) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.93x