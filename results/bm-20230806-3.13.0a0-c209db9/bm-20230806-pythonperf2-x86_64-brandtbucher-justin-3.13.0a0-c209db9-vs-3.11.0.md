
# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: c209db9
- commit date: 2023-08-06
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.86 sec                                                     | 3.03 sec: 1.06x slower                                              |
| tornado_http   | 122 ms                                                       | 123 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                        | 1.04x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 260 ms: 1.03x slower                                                |
| nbody          | 90.7 ms                                                      | 94.7 ms: 1.04x slower                                               |
| float          | 74.2 ms                                                      | 85.3 ms: 1.15x slower                                               |
| Geometric mean | (ref)                                                        | 1.07x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 160 ms: 1.01x slower                                                |
| regex_effbot   | 3.50 ms                                                      | 3.55 ms: 1.02x slower                                               |
| regex_v8       | 23.9 ms                                                      | 24.4 ms: 1.02x slower                                               |
| regex_dna      | 227 ms                                                       | 244 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                        | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.5 ms: 1.27x faster                                               |
| json_loads           | 28.7 us                                                      | 25.7 us: 1.12x faster                                               |
| xml_etree_parse      | 158 ms                                                       | 149 ms: 1.06x faster                                                |
| unpickle_pure_python | 241 us                                                       | 237 us: 1.01x faster                                                |
| pickle_pure_python   | 319 us                                                       | 324 us: 1.02x slower                                                |
| unpickle_list        | 4.53 us                                                      | 4.68 us: 1.03x slower                                               |
| xml_etree_iterparse  | 104 ms                                                       | 109 ms: 1.04x slower                                                |
| pickle_dict          | 30.8 us                                                      | 32.3 us: 1.05x slower                                               |
| pickle               | 9.64 us                                                      | 10.2 us: 1.06x slower                                               |
| xml_etree_process    | 56.5 ms                                                      | 61.8 ms: 1.09x slower                                               |
| unpickle             | 13.4 us                                                      | 14.7 us: 1.09x slower                                               |
| xml_etree_generate   | 80.5 ms                                                      | 89.2 ms: 1.11x slower                                               |
| pickle_list          | 3.83 us                                                      | 4.45 us: 1.16x slower                                               |
| tomli_loads          | 2.26 sec                                                     | 2.68 sec: 1.18x slower                                              |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                               |
| python_startup_no_site | 7.76 ms                                                      | 8.68 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                        | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|-----------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 11.0 ms                                                      | 11.5 ms: 1.05x slower                                               |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 523 us                                                       | 160 us: 3.26x faster                                                |
| asyncio_tcp              | 753 ms                                                       | 369 ms: 2.04x faster                                                |
| asyncio_tcp_ssl          | 3.08 sec                                                     | 1.58 sec: 1.95x faster                                              |
| generators               | 56.0 ms                                                      | 37.6 ms: 1.49x faster                                               |
| json_dumps               | 13.4 ms                                                      | 10.5 ms: 1.27x faster                                               |
| chaos                    | 80.9 ms                                                      | 67.4 ms: 1.20x faster                                               |
| mypy2                    | 451 ms                                                       | 385 ms: 1.17x faster                                                |
| coroutines               | 27.6 ms                                                      | 23.9 ms: 1.15x faster                                               |
| json_loads               | 28.7 us                                                      | 25.7 us: 1.12x faster                                               |
| json                     | 5.65 ms                                                      | 5.20 ms: 1.09x faster                                               |
| scimark_lu               | 115 ms                                                       | 106 ms: 1.08x faster                                                |
| async_tree_none          | 519 ms                                                       | 481 ms: 1.08x faster                                                |
| async_tree_memoization   | 630 ms                                                       | 585 ms: 1.08x faster                                                |
| raytrace                 | 317 ms                                                       | 294 ms: 1.08x faster                                                |
| crypto_pyaes             | 83.4 ms                                                      | 77.6 ms: 1.07x faster                                               |
| async_tree_io            | 1.17 sec                                                     | 1.10 sec: 1.07x faster                                              |
| xml_etree_parse          | 158 ms                                                       | 149 ms: 1.06x faster                                                |
| logging_format           | 8.11 us                                                      | 7.66 us: 1.06x faster                                               |
| sqlglot_normalize        | 126 ms                                                       | 122 ms: 1.04x faster                                                |
| sqlglot_parse            | 1.53 ms                                                      | 1.49 ms: 1.03x faster                                               |
| deltablue                | 4.00 ms                                                      | 3.89 ms: 1.03x faster                                               |
| async_tree_cpu_io_mixed  | 749 ms                                                       | 731 ms: 1.02x faster                                                |
| logging_simple           | 7.19 us                                                      | 7.04 us: 1.02x faster                                               |
| deepcopy                 | 399 us                                                       | 392 us: 1.02x faster                                                |
| richards_super           | 61.0 ms                                                      | 60.2 ms: 1.01x faster                                               |
| unpickle_pure_python     | 241 us                                                       | 237 us: 1.01x faster                                                |
| create_gc_cycles         | 1.61 ms                                                      | 1.59 ms: 1.01x faster                                               |
| sqlglot_transpile        | 1.92 ms                                                      | 1.90 ms: 1.01x faster                                               |
| logging_silent           | 101 ns                                                       | 100 ns: 1.01x faster                                                |
| mdp                      | 2.75 sec                                                     | 2.74 sec: 1.00x faster                                              |
| regex_compile            | 158 ms                                                       | 160 ms: 1.01x slower                                                |
| dulwich_log              | 68.4 ms                                                      | 69.4 ms: 1.01x slower                                               |
| regex_effbot             | 3.50 ms                                                      | 3.55 ms: 1.02x slower                                               |
| tornado_http             | 122 ms                                                       | 123 ms: 1.02x slower                                                |
| pickle_pure_python       | 319 us                                                       | 324 us: 1.02x slower                                                |
| regex_v8                 | 23.9 ms                                                      | 24.4 ms: 1.02x slower                                               |
| gc_traversal             | 3.85 ms                                                      | 3.95 ms: 1.03x slower                                               |
| pycparser                | 1.32 sec                                                     | 1.37 sec: 1.03x slower                                              |
| unpickle_list            | 4.53 us                                                      | 4.68 us: 1.03x slower                                               |
| pidigits                 | 251 ms                                                       | 260 ms: 1.03x slower                                                |
| sqlglot_optimize         | 59.8 ms                                                      | 61.8 ms: 1.03x slower                                               |
| scimark_monte_carlo      | 68.2 ms                                                      | 70.6 ms: 1.03x slower                                               |
| xml_etree_iterparse      | 104 ms                                                       | 109 ms: 1.04x slower                                                |
| nbody                    | 90.7 ms                                                      | 94.7 ms: 1.04x slower                                               |
| mako                     | 11.0 ms                                                      | 11.5 ms: 1.05x slower                                               |
| pickle_dict              | 30.8 us                                                      | 32.3 us: 1.05x slower                                               |
| pathlib                  | 19.1 ms                                                      | 20.1 ms: 1.06x slower                                               |
| docutils                 | 2.86 sec                                                     | 3.03 sec: 1.06x slower                                              |
| pickle                   | 9.64 us                                                      | 10.2 us: 1.06x slower                                               |
| nqueens                  | 103 ms                                                       | 109 ms: 1.06x slower                                                |
| coverage                 | 84.8 ms                                                      | 90.3 ms: 1.06x slower                                               |
| deepcopy_memo            | 38.8 us                                                      | 41.6 us: 1.07x slower                                               |
| regex_dna                | 227 ms                                                       | 244 ms: 1.08x slower                                                |
| python_startup           | 10.8 ms                                                      | 11.6 ms: 1.08x slower                                               |
| pprint_pformat           | 1.63 sec                                                     | 1.77 sec: 1.08x slower                                              |
| xml_etree_process        | 56.5 ms                                                      | 61.8 ms: 1.09x slower                                               |
| unpickle                 | 13.4 us                                                      | 14.7 us: 1.09x slower                                               |
| meteor_contest           | 131 ms                                                       | 143 ms: 1.10x slower                                                |
| fannkuch                 | 429 ms                                                       | 471 ms: 1.10x slower                                                |
| pprint_safe_repr         | 784 ms                                                       | 861 ms: 1.10x slower                                                |
| spectral_norm            | 93.3 ms                                                      | 103 ms: 1.10x slower                                                |
| comprehensions           | 24.6 us                                                      | 27.2 us: 1.11x slower                                               |
| xml_etree_generate       | 80.5 ms                                                      | 89.2 ms: 1.11x slower                                               |
| sqlite_synth             | 2.50 us                                                      | 2.78 us: 1.11x slower                                               |
| python_startup_no_site   | 7.76 ms                                                      | 8.68 ms: 1.12x slower                                               |
| hexiom                   | 7.13 ms                                                      | 8.05 ms: 1.13x slower                                               |
| go                       | 164 ms                                                       | 186 ms: 1.13x slower                                                |
| richards                 | 48.3 ms                                                      | 55.0 ms: 1.14x slower                                               |
| float                    | 74.2 ms                                                      | 85.3 ms: 1.15x slower                                               |
| pickle_list              | 3.83 us                                                      | 4.45 us: 1.16x slower                                               |
| telco                    | 6.86 ms                                                      | 8.04 ms: 1.17x slower                                               |
| tomli_loads              | 2.26 sec                                                     | 2.68 sec: 1.18x slower                                              |
| scimark_fft              | 285 ms                                                       | 339 ms: 1.19x slower                                                |
| pyflate                  | 449 ms                                                       | 537 ms: 1.20x slower                                                |
| unpack_sequence          | 45.6 ns                                                      | 56.4 ns: 1.23x slower                                               |
| async_generators         | 316 ms                                                       | 411 ms: 1.30x slower                                                |
| scimark_sor              | 111 ms                                                       | 150 ms: 1.35x slower                                                |
| scimark_sparse_mat_mult  | 4.05 ms                                                      | 5.65 ms: 1.40x slower                                               |
| dask                     | 410 ms                                                       | 597 ms: 1.46x slower                                                |
| Geometric mean           | (ref)                                                        | 1.00x slower                                                        |

Benchmark hidden because not significant (3): bench_thread_pool, deepcopy_reduce, bench_mp_pool
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
