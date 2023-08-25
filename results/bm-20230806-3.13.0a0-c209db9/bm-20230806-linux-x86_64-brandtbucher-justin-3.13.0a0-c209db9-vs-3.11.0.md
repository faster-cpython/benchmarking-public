
# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: c209db9
- commit date: 2023-08-06
- overall geometric mean: 1.00x faster
- HPT reliability: 99.33%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.75 sec: 1.05x slower                                        |
| tornado_http   | 96.3 ms                                                | 97.3 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                  | 1.03x slower                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 200 ms: 1.01x slower                                          |
| nbody          | 93.1 ms                                                | 102 ms: 1.09x slower                                          |
| float          | 77.2 ms                                                | 84.4 ms: 1.09x slower                                         |
| Geometric mean | (ref)                                                  | 1.06x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.39 ms: 1.18x faster                                         |
| regex_dna      | 204 ms                                                 | 200 ms: 1.02x faster                                          |
| regex_compile  | 138 ms                                                 | 150 ms: 1.09x slower                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.89 ms: 1.27x faster                                         |
| json_loads           | 26.5 us                                                | 25.4 us: 1.04x faster                                         |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                          |
| unpickle_pure_python | 228 us                                                 | 222 us: 1.03x faster                                          |
| pickle_pure_python   | 306 us                                                 | 300 us: 1.02x faster                                          |
| unpickle_list        | 4.91 us                                                | 4.96 us: 1.01x slower                                         |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                          |
| pickle_dict          | 31.1 us                                                | 31.8 us: 1.02x slower                                         |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                         |
| xml_etree_process    | 53.9 ms                                                | 59.0 ms: 1.10x slower                                         |
| unpickle             | 13.7 us                                                | 15.1 us: 1.11x slower                                         |
| pickle_list          | 4.11 us                                                | 4.57 us: 1.11x slower                                         |
| xml_etree_generate   | 76.2 ms                                                | 86.1 ms: 1.13x slower                                         |
| tomli_loads          | 2.22 sec                                               | 2.58 sec: 1.16x slower                                        |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.39 ms: 1.10x slower                                         |
| python_startup_no_site | 6.01 ms                                                | 6.88 ms: 1.15x slower                                         |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 12.1 ms: 1.20x slower                                         |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-linux-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 152 us: 3.19x faster                                          |
| generators               | 73.5 ms                                                | 29.1 ms: 2.52x faster                                         |
| asyncio_tcp              | 922 ms                                                 | 490 ms: 1.88x faster                                          |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                        |
| json_dumps               | 12.6 ms                                                | 9.89 ms: 1.27x faster                                         |
| mypy2                    | 420 ms                                                 | 350 ms: 1.20x faster                                          |
| regex_effbot             | 3.99 ms                                                | 3.39 ms: 1.18x faster                                         |
| coroutines               | 25.5 ms                                                | 22.4 ms: 1.14x faster                                         |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                        |
| deltablue                | 3.67 ms                                                | 3.42 ms: 1.07x faster                                         |
| async_tree_none          | 526 ms                                                 | 493 ms: 1.07x faster                                          |
| coverage                 | 100 ms                                                 | 93.8 ms: 1.07x faster                                         |
| sqlglot_parse            | 1.40 ms                                                | 1.32 ms: 1.06x faster                                         |
| raytrace                 | 297 ms                                                 | 280 ms: 1.06x faster                                          |
| chaos                    | 69.2 ms                                                | 65.5 ms: 1.06x faster                                         |
| async_tree_memoization   | 627 ms                                                 | 594 ms: 1.06x faster                                          |
| json_loads               | 26.5 us                                                | 25.4 us: 1.04x faster                                         |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                          |
| sqlglot_transpile        | 1.70 ms                                                | 1.65 ms: 1.03x faster                                         |
| unpickle_pure_python     | 228 us                                                 | 222 us: 1.03x faster                                          |
| pickle_pure_python       | 306 us                                                 | 300 us: 1.02x faster                                          |
| logging_format           | 6.68 us                                                | 6.56 us: 1.02x faster                                         |
| regex_dna                | 204 ms                                                 | 200 ms: 1.02x faster                                          |
| json                     | 4.94 ms                                                | 4.86 ms: 1.02x faster                                         |
| richards_super           | 56.8 ms                                                | 55.9 ms: 1.02x faster                                         |
| crypto_pyaes             | 74.7 ms                                                | 73.8 ms: 1.01x faster                                         |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 732 ms: 1.01x faster                                          |
| gc_traversal             | 4.02 ms                                                | 3.99 ms: 1.01x faster                                         |
| sqlglot_normalize        | 108 ms                                                 | 108 ms: 1.00x slower                                          |
| pycparser                | 1.18 sec                                               | 1.19 sec: 1.01x slower                                        |
| tornado_http             | 96.3 ms                                                | 97.3 ms: 1.01x slower                                         |
| unpickle_list            | 4.91 us                                                | 4.96 us: 1.01x slower                                         |
| scimark_monte_carlo      | 68.1 ms                                                | 68.9 ms: 1.01x slower                                         |
| pidigits                 | 198 ms                                                 | 200 ms: 1.01x slower                                          |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.01x slower                                         |
| xml_etree_iterparse      | 104 ms                                                 | 106 ms: 1.02x slower                                          |
| pickle_dict              | 31.1 us                                                | 31.8 us: 1.02x slower                                         |
| logging_silent           | 101 ns                                                 | 104 ns: 1.03x slower                                          |
| sqlglot_optimize         | 53.1 ms                                                | 54.6 ms: 1.03x slower                                         |
| pickle                   | 10.1 us                                                | 10.5 us: 1.04x slower                                         |
| pprint_pformat           | 1.46 sec                                               | 1.52 sec: 1.04x slower                                        |
| docutils                 | 2.63 sec                                               | 2.75 sec: 1.05x slower                                        |
| pathlib                  | 18.2 ms                                                | 19.1 ms: 1.05x slower                                         |
| go                       | 140 ms                                                 | 147 ms: 1.05x slower                                          |
| bench_thread_pool        | 819 us                                                 | 864 us: 1.05x slower                                          |
| dulwich_log              | 63.7 ms                                                | 67.2 ms: 1.05x slower                                         |
| scimark_sor              | 118 ms                                                 | 125 ms: 1.05x slower                                          |
| pprint_safe_repr         | 701 ms                                                 | 741 ms: 1.06x slower                                          |
| deepcopy                 | 342 us                                                 | 362 us: 1.06x slower                                          |
| richards                 | 45.7 ms                                                | 48.7 ms: 1.06x slower                                         |
| scimark_lu               | 110 ms                                                 | 118 ms: 1.07x slower                                          |
| meteor_contest           | 107 ms                                                 | 115 ms: 1.08x slower                                          |
| mdp                      | 2.62 sec                                               | 2.83 sec: 1.08x slower                                        |
| regex_compile            | 138 ms                                                 | 150 ms: 1.09x slower                                          |
| spectral_norm            | 100 ms                                                 | 109 ms: 1.09x slower                                          |
| deepcopy_reduce          | 2.94 us                                                | 3.20 us: 1.09x slower                                         |
| nbody                    | 93.1 ms                                                | 102 ms: 1.09x slower                                          |
| float                    | 77.2 ms                                                | 84.4 ms: 1.09x slower                                         |
| xml_etree_process        | 53.9 ms                                                | 59.0 ms: 1.10x slower                                         |
| python_startup           | 8.52 ms                                                | 9.39 ms: 1.10x slower                                         |
| unpickle                 | 13.7 us                                                | 15.1 us: 1.11x slower                                         |
| pickle_list              | 4.11 us                                                | 4.57 us: 1.11x slower                                         |
| sqlite_synth             | 2.52 us                                                | 2.80 us: 1.11x slower                                         |
| comprehensions           | 22.4 us                                                | 25.0 us: 1.11x slower                                         |
| xml_etree_generate       | 76.2 ms                                                | 86.1 ms: 1.13x slower                                         |
| deepcopy_memo            | 37.0 us                                                | 41.9 us: 1.13x slower                                         |
| python_startup_no_site   | 6.01 ms                                                | 6.88 ms: 1.15x slower                                         |
| unpack_sequence          | 43.1 ns                                                | 49.8 ns: 1.16x slower                                         |
| pyflate                  | 418 ms                                                 | 485 ms: 1.16x slower                                          |
| tomli_loads              | 2.22 sec                                               | 2.58 sec: 1.16x slower                                        |
| scimark_fft              | 328 ms                                                 | 385 ms: 1.17x slower                                          |
| nqueens                  | 83.4 ms                                                | 98.9 ms: 1.19x slower                                         |
| hexiom                   | 6.37 ms                                                | 7.61 ms: 1.19x slower                                         |
| mako                     | 10.1 ms                                                | 12.1 ms: 1.20x slower                                         |
| fannkuch                 | 388 ms                                                 | 468 ms: 1.21x slower                                          |
| telco                    | 6.58 ms                                                | 8.05 ms: 1.22x slower                                         |
| async_generators         | 368 ms                                                 | 466 ms: 1.26x slower                                          |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 5.70 ms: 1.27x slower                                         |
| dask                     | 360 ms                                                 | 532 ms: 1.48x slower                                          |
| Geometric mean           | (ref)                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (3): regex_v8, logging_simple, bench_mp_pool
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 99.33% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x
