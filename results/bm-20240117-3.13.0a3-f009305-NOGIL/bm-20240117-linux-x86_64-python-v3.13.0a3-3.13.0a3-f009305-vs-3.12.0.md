# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.11x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 290 ms: 1.06x slower                                       |
| chameleon      | 7.41 ms                                                | 7.87 ms: 1.06x slower                                      |
| docutils       | 2.77 sec                                               | 2.95 sec: 1.07x slower                                     |
| Geometric mean | (ref)                                                  | 1.04x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 533 ms: 1.13x slower                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 838 ms: 1.16x slower                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 848 ms: 1.17x slower                                       |
| async_tree_none_tg         | 450 ms                                                 | 537 ms: 1.19x slower                                       |
| async_tree_memoization     | 578 ms                                                 | 704 ms: 1.22x slower                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 702 ms: 1.22x slower                                       |
| async_tree_io_tg           | 1.18 sec                                               | 1.50 sec: 1.27x slower                                     |
| async_tree_io              | 1.16 sec                                               | 1.49 sec: 1.29x slower                                     |
| Geometric mean             | (ref)                                                  | 1.20x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                       |
| float          | 84.7 ms                                                | 88.3 ms: 1.04x slower                                      |
| nbody          | 97.0 ms                                                | 105 ms: 1.09x slower                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 139 ms: 1.07x faster                                       |
| regex_effbot   | 3.61 ms                                                | 3.52 ms: 1.03x faster                                      |
| regex_v8       | 23.1 ms                                                | 23.7 ms: 1.03x slower                                      |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle               | 11.6 us                                                | 10.6 us: 1.10x faster                                      |
| pickle_dict          | 35.5 us                                                | 33.2 us: 1.07x faster                                      |
| unpickle_list        | 5.29 us                                                | 4.99 us: 1.06x faster                                      |
| pickle_list          | 5.08 us                                                | 4.87 us: 1.04x faster                                      |
| tomli_loads          | 2.33 sec                                               | 2.24 sec: 1.04x faster                                     |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                       |
| unpickle_pure_python | 230 us                                                 | 234 us: 1.02x slower                                       |
| json_loads           | 28.5 us                                                | 29.3 us: 1.03x slower                                      |
| xml_etree_generate   | 89.2 ms                                                | 94.2 ms: 1.06x slower                                      |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                      |
| xml_etree_process    | 61.7 ms                                                | 65.4 ms: 1.06x slower                                      |
| xml_etree_iterparse  | 107 ms                                                 | 114 ms: 1.06x slower                                       |
| xml_etree_parse      | 159 ms                                                 | 172 ms: 1.08x slower                                       |
| Geometric mean       | (ref)                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 12.1 ms: 1.26x slower                                      |
| python_startup_no_site | 6.94 ms                                                | 10.5 ms: 1.51x slower                                      |
| Geometric mean         | (ref)                                                  | 1.38x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.9 ms                                                | 12.0 ms: 1.01x slower                                      |
| django_template | 34.6 ms                                                | 37.3 ms: 1.08x slower                                      |
| Geometric mean  | (ref)                                                  | 1.04x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 124 us: 1.28x faster                                       |
| comprehensions             | 21.8 us                                                | 17.7 us: 1.23x faster                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.26 ms: 1.18x faster                                      |
| crypto_pyaes               | 81.9 ms                                                | 74.5 ms: 1.10x faster                                      |
| pickle                     | 11.6 us                                                | 10.6 us: 1.10x faster                                      |
| gc_traversal               | 3.79 ms                                                | 3.52 ms: 1.08x faster                                      |
| raytrace                   | 312 ms                                                 | 291 ms: 1.07x faster                                       |
| pickle_dict                | 35.5 us                                                | 33.2 us: 1.07x faster                                      |
| regex_compile              | 148 ms                                                 | 139 ms: 1.07x faster                                       |
| unpickle_list              | 5.29 us                                                | 4.99 us: 1.06x faster                                      |
| deltablue                  | 3.72 ms                                                | 3.56 ms: 1.05x faster                                      |
| pickle_list                | 5.08 us                                                | 4.87 us: 1.04x faster                                      |
| tomli_loads                | 2.33 sec                                               | 2.24 sec: 1.04x faster                                     |
| logging_format             | 7.23 us                                                | 6.96 us: 1.04x faster                                      |
| logging_simple             | 6.46 us                                                | 6.26 us: 1.03x faster                                      |
| pyflate                    | 482 ms                                                 | 469 ms: 1.03x faster                                       |
| chaos                      | 67.0 ms                                                | 65.2 ms: 1.03x faster                                      |
| regex_effbot               | 3.61 ms                                                | 3.52 ms: 1.03x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.5 ms: 1.02x faster                                      |
| deepcopy_reduce            | 3.35 us                                                | 3.27 us: 1.02x faster                                      |
| pathlib                    | 19.3 ms                                                | 18.9 ms: 1.02x faster                                      |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 74.0 ms: 1.02x faster                                      |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.01x faster                                       |
| deepcopy                   | 371 us                                                 | 368 us: 1.01x faster                                       |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                       |
| mako                       | 11.9 ms                                                | 12.0 ms: 1.01x slower                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.71 ms: 1.01x slower                                      |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                      |
| asyncio_websockets         | 551 ms                                                 | 560 ms: 1.02x slower                                       |
| unpickle_pure_python       | 230 us                                                 | 234 us: 1.02x slower                                       |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                      |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.02x slower                                       |
| nqueens                    | 83.3 ms                                                | 85.2 ms: 1.02x slower                                      |
| scimark_fft                | 382 ms                                                 | 391 ms: 1.02x slower                                       |
| pprint_safe_repr           | 776 ms                                                 | 796 ms: 1.03x slower                                       |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.03x slower                                       |
| regex_v8                   | 23.1 ms                                                | 23.7 ms: 1.03x slower                                      |
| meteor_contest             | 112 ms                                                 | 115 ms: 1.03x slower                                       |
| async_generators           | 463 ms                                                 | 476 ms: 1.03x slower                                       |
| json_loads                 | 28.5 us                                                | 29.3 us: 1.03x slower                                      |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                       |
| generators                 | 31.2 ms                                                | 32.3 ms: 1.03x slower                                      |
| hexiom                     | 6.41 ms                                                | 6.64 ms: 1.04x slower                                      |
| scimark_sor                | 129 ms                                                 | 134 ms: 1.04x slower                                       |
| asyncio_tcp                | 491 ms                                                 | 510 ms: 1.04x slower                                       |
| deepcopy_memo              | 40.7 us                                                | 42.4 us: 1.04x slower                                      |
| float                      | 84.7 ms                                                | 88.3 ms: 1.04x slower                                      |
| pprint_pformat             | 1.57 sec                                               | 1.64 sec: 1.04x slower                                     |
| sqlglot_optimize           | 54.8 ms                                                | 57.3 ms: 1.04x slower                                      |
| xml_etree_generate         | 89.2 ms                                                | 94.2 ms: 1.06x slower                                      |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                      |
| 2to3                       | 274 ms                                                 | 290 ms: 1.06x slower                                       |
| xml_etree_process          | 61.7 ms                                                | 65.4 ms: 1.06x slower                                      |
| chameleon                  | 7.41 ms                                                | 7.87 ms: 1.06x slower                                      |
| xml_etree_iterparse        | 107 ms                                                 | 114 ms: 1.06x slower                                       |
| logging_silent             | 104 ns                                                 | 111 ns: 1.06x slower                                       |
| docutils                   | 2.77 sec                                               | 2.95 sec: 1.07x slower                                     |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.90 sec: 1.07x slower                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.42 ms: 1.07x slower                                      |
| go                         | 139 ms                                                 | 149 ms: 1.07x slower                                       |
| gunicorn                   | 1.24 ms                                                | 1.33 ms: 1.07x slower                                      |
| aiohttp                    | 1.15 ms                                                | 1.23 ms: 1.07x slower                                      |
| sympy_integrate            | 21.4 ms                                                | 23.0 ms: 1.07x slower                                      |
| django_template            | 34.6 ms                                                | 37.3 ms: 1.08x slower                                      |
| xml_etree_parse            | 159 ms                                                 | 172 ms: 1.08x slower                                       |
| richards                   | 45.8 ms                                                | 49.6 ms: 1.08x slower                                      |
| nbody                      | 97.0 ms                                                | 105 ms: 1.09x slower                                       |
| richards_super             | 51.5 ms                                                | 56.0 ms: 1.09x slower                                      |
| pycparser                  | 1.18 sec                                               | 1.29 sec: 1.09x slower                                     |
| sqlite_synth               | 2.83 us                                                | 3.15 us: 1.11x slower                                      |
| mdp                        | 2.63 sec                                               | 2.93 sec: 1.11x slower                                     |
| async_tree_none            | 472 ms                                                 | 533 ms: 1.13x slower                                       |
| sympy_str                  | 300 ms                                                 | 342 ms: 1.14x slower                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 838 ms: 1.16x slower                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 848 ms: 1.17x slower                                       |
| async_tree_none_tg         | 450 ms                                                 | 537 ms: 1.19x slower                                       |
| async_tree_memoization     | 578 ms                                                 | 704 ms: 1.22x slower                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 702 ms: 1.22x slower                                       |
| python_startup             | 9.55 ms                                                | 12.1 ms: 1.26x slower                                      |
| async_tree_io_tg           | 1.18 sec                                               | 1.50 sec: 1.27x slower                                     |
| sympy_sum                  | 169 ms                                                 | 216 ms: 1.28x slower                                       |
| telco                      | 7.10 ms                                                | 9.10 ms: 1.28x slower                                      |
| async_tree_io              | 1.16 sec                                               | 1.49 sec: 1.29x slower                                     |
| sympy_expand               | 478 ms                                                 | 644 ms: 1.35x slower                                       |
| mypy2                      | 830 ms                                                 | 1.18 sec: 1.43x slower                                     |
| python_startup_no_site     | 6.94 ms                                                | 10.5 ms: 1.51x slower                                      |
| bench_thread_pool          | 842 us                                                 | 2.54 ms: 3.01x slower                                      |
| coverage                   | 72.7 ms                                                | 690 ms: 9.49x slower                                       |
| fannkuch                   | 417 ms                                                 | 4.97 sec: 11.92x slower                                    |
| Geometric mean             | (ref)                                                  | 1.11x slower                                               |

Benchmark hidden because not significant (4): unpickle, tornado_http, dulwich_log, sqlglot_parse
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240117-3.13.0a3-f009305-NOGIL/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.05x