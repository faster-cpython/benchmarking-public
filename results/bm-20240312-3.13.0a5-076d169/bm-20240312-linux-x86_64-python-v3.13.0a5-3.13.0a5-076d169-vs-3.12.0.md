# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a5
- machine: linux-x86_64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.03x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 270 ms: 1.02x faster                                       |
| chameleon      | 7.41 ms                                                | 6.83 ms: 1.09x faster                                      |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                     |
| tornado_http   | 103 ms                                                 | 98.6 ms: 1.04x faster                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 449 ms: 1.05x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 745 ms: 1.03x slower                                       |
| async_tree_none_tg         | 450 ms                                                 | 463 ms: 1.03x slower                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 595 ms: 1.04x slower                                       |
| async_tree_io_tg           | 1.18 sec                                               | 1.24 sec: 1.05x slower                                     |
| async_tree_io              | 1.16 sec                                               | 1.22 sec: 1.05x slower                                     |
| Geometric mean             | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 93.6 ms: 1.04x faster                                      |
| float          | 84.7 ms                                                | 82.6 ms: 1.03x faster                                      |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.12x faster                                       |
| regex_effbot   | 3.61 ms                                                | 3.54 ms: 1.02x faster                                      |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                       |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.16 sec: 1.08x faster                                     |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                       |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                       |
| unpickle             | 15.9 us                                                | 15.1 us: 1.05x faster                                      |
| unpickle_list        | 5.29 us                                                | 5.05 us: 1.05x faster                                      |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                      |
| json_loads           | 28.5 us                                                | 27.7 us: 1.03x faster                                      |
| xml_etree_generate   | 89.2 ms                                                | 87.3 ms: 1.02x faster                                      |
| pickle_list          | 5.08 us                                                | 5.01 us: 1.01x faster                                      |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                      |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 10.4 ms: 1.09x slower                                      |
| python_startup_no_site | 6.94 ms                                                | 8.99 ms: 1.30x slower                                      |
| Geometric mean         | (ref)                                                  | 1.19x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                      |
| django_template | 34.6 ms                                                | 33.8 ms: 1.02x faster                                      |
| Geometric mean  | (ref)                                                  | 1.04x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 112 us: 1.41x faster                                       |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                      |
| raytrace                   | 312 ms                                                 | 263 ms: 1.19x faster                                       |
| deltablue                  | 3.72 ms                                                | 3.23 ms: 1.15x faster                                      |
| crypto_pyaes               | 81.9 ms                                                | 73.0 ms: 1.12x faster                                      |
| regex_compile              | 148 ms                                                 | 133 ms: 1.12x faster                                       |
| logging_format             | 7.23 us                                                | 6.53 us: 1.11x faster                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 67.9 ms: 1.11x faster                                      |
| logging_simple             | 6.46 us                                                | 5.85 us: 1.10x faster                                      |
| sympy_sum                  | 169 ms                                                 | 153 ms: 1.10x faster                                       |
| deepcopy_reduce            | 3.35 us                                                | 3.04 us: 1.10x faster                                      |
| chaos                      | 67.0 ms                                                | 60.9 ms: 1.10x faster                                      |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                       |
| chameleon                  | 7.41 ms                                                | 6.83 ms: 1.09x faster                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.68 ms: 1.08x faster                                      |
| tomli_loads                | 2.33 sec                                               | 2.16 sec: 1.08x faster                                     |
| deepcopy                   | 371 us                                                 | 346 us: 1.07x faster                                       |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                      |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                      |
| deepcopy_memo              | 40.7 us                                                | 38.1 us: 1.07x faster                                      |
| spectral_norm              | 115 ms                                                 | 108 ms: 1.06x faster                                       |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                       |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                      |
| scimark_fft                | 382 ms                                                 | 362 ms: 1.06x faster                                       |
| coroutines                 | 23.2 ms                                                | 22.0 ms: 1.05x faster                                      |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                      |
| unpickle                   | 15.9 us                                                | 15.1 us: 1.05x faster                                      |
| async_tree_none            | 472 ms                                                 | 449 ms: 1.05x faster                                       |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                       |
| logging_silent             | 104 ns                                                 | 99.5 ns: 1.05x faster                                      |
| unpickle_list              | 5.29 us                                                | 5.05 us: 1.05x faster                                      |
| hexiom                     | 6.41 ms                                                | 6.13 ms: 1.05x faster                                      |
| pathlib                    | 19.3 ms                                                | 18.5 ms: 1.04x faster                                      |
| fannkuch                   | 417 ms                                                 | 400 ms: 1.04x faster                                       |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                       |
| tornado_http               | 103 ms                                                 | 98.6 ms: 1.04x faster                                      |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                     |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                     |
| nbody                      | 97.0 ms                                                | 93.6 ms: 1.04x faster                                      |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                       |
| xml_etree_process          | 61.7 ms                                                | 59.8 ms: 1.03x faster                                      |
| nqueens                    | 83.3 ms                                                | 80.7 ms: 1.03x faster                                      |
| async_generators           | 463 ms                                                 | 449 ms: 1.03x faster                                       |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                       |
| pyflate                    | 482 ms                                                 | 469 ms: 1.03x faster                                       |
| json_loads                 | 28.5 us                                                | 27.7 us: 1.03x faster                                      |
| float                      | 84.7 ms                                                | 82.6 ms: 1.03x faster                                      |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                       |
| pprint_safe_repr           | 776 ms                                                 | 757 ms: 1.03x faster                                       |
| django_template            | 34.6 ms                                                | 33.8 ms: 1.02x faster                                      |
| json                       | 5.26 ms                                                | 5.15 ms: 1.02x faster                                      |
| xml_etree_generate         | 89.2 ms                                                | 87.3 ms: 1.02x faster                                      |
| regex_effbot               | 3.61 ms                                                | 3.54 ms: 1.02x faster                                      |
| dulwich_log                | 68.5 ms                                                | 67.3 ms: 1.02x faster                                      |
| sqlglot_optimize           | 54.8 ms                                                | 53.9 ms: 1.02x faster                                      |
| 2to3                       | 274 ms                                                 | 270 ms: 1.02x faster                                       |
| pickle_list                | 5.08 us                                                | 5.01 us: 1.01x faster                                      |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                     |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.01x faster                                      |
| go                         | 139 ms                                                 | 139 ms: 1.01x faster                                       |
| gc_traversal               | 3.79 ms                                                | 3.78 ms: 1.00x faster                                      |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                      |
| richards_super             | 51.5 ms                                                | 51.9 ms: 1.01x slower                                      |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                       |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                       |
| sqlite_synth               | 2.83 us                                                | 2.89 us: 1.02x slower                                      |
| asyncio_websockets         | 551 ms                                                 | 563 ms: 1.02x slower                                       |
| create_gc_cycles           | 1.48 ms                                                | 1.52 ms: 1.03x slower                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 745 ms: 1.03x slower                                       |
| asyncio_tcp                | 491 ms                                                 | 504 ms: 1.03x slower                                       |
| async_tree_none_tg         | 450 ms                                                 | 463 ms: 1.03x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.03x slower                                     |
| aiohttp                    | 1.15 ms                                                | 1.19 ms: 1.03x slower                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 595 ms: 1.04x slower                                       |
| json_dumps                 | 10.4 ms                                                | 10.8 ms: 1.04x slower                                      |
| gunicorn                   | 1.24 ms                                                | 1.29 ms: 1.04x slower                                      |
| async_tree_io_tg           | 1.18 sec                                               | 1.24 sec: 1.05x slower                                     |
| async_tree_io              | 1.16 sec                                               | 1.22 sec: 1.05x slower                                     |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                      |
| python_startup             | 9.55 ms                                                | 10.4 ms: 1.09x slower                                      |
| telco                      | 7.10 ms                                                | 8.60 ms: 1.21x slower                                      |
| python_startup_no_site     | 6.94 ms                                                | 8.99 ms: 1.30x slower                                      |
| coverage                   | 72.7 ms                                                | 95.6 ms: 1.32x slower                                      |
| Geometric mean             | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (10): dask, xml_etree_iterparse, bench_thread_pool, xml_etree_parse, richards, async_tree_cpu_io_mixed, pycparser, async_tree_memoization, pickle_dict, mypy2
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (7) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.94x