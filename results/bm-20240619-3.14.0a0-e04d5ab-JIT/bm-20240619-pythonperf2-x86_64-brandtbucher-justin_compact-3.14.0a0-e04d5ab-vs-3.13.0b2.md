# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_compact
- machine: linux-x86_64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.00x slower
- HPT reliability: 94.51%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 307 ms: 1.05x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.13 sec: 1.05x slower                                                      |
| html5lib       | 74.7 ms                                                          | 73.9 ms: 1.01x faster                                                       |
| tornado_http   | 119 ms                                                           | 123 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                            | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg        | 900 ms                                                           | 872 ms: 1.03x faster                                                        |
| async_tree_memoization  | 460 ms                                                           | 476 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed | 604 ms                                                           | 628 ms: 1.04x slower                                                        |
| async_tree_none         | 365 ms                                                           | 380 ms: 1.04x slower                                                        |
| async_tree_io           | 873 ms                                                           | 913 ms: 1.05x slower                                                        |
| Geometric mean          | (ref)                                                            | 1.02x slower                                                                |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 74.6 ms: 1.07x faster                                                       |
| nbody          | 87.8 ms                                                          | 84.7 ms: 1.04x faster                                                       |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 137 ms: 1.05x faster                                                        |
| regex_dna      | 249 ms                                                           | 242 ms: 1.03x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.8 ms: 1.01x faster                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.48 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.15 sec: 1.12x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 82.4 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 99.7 ms: 1.03x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 58.3 ms: 1.02x faster                                                       |
| pickle_dict          | 32.8 us                                                          | 32.1 us: 1.02x faster                                                       |
| unpickle             | 15.7 us                                                          | 15.5 us: 1.01x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 222 us: 1.01x faster                                                        |
| xml_etree_parse      | 144 ms                                                           | 142 ms: 1.01x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                       |
| json_loads           | 25.0 us                                                          | 25.2 us: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 312 us: 1.02x slower                                                        |
| pickle               | 10.6 us                                                          | 10.8 us: 1.02x slower                                                       |
| pickle_list          | 4.44 us                                                          | 4.53 us: 1.02x slower                                                       |
| unpickle_list        | 4.70 us                                                          | 4.91 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.8 ms: 1.05x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.47 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.24 ms: 1.12x faster                                                       |
| django_template | 39.0 ms                                                          | 40.9 ms: 1.05x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 27.6 ms: 1.07x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 64.9 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|--------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo            | 37.3 us                                                          | 28.3 us: 1.32x faster                                                       |
| deepcopy                 | 377 us                                                           | 308 us: 1.23x faster                                                        |
| spectral_norm            | 97.3 ms                                                          | 81.9 ms: 1.19x faster                                                       |
| richards                 | 53.4 ms                                                          | 45.8 ms: 1.17x faster                                                       |
| richards_super           | 61.2 ms                                                          | 53.1 ms: 1.15x faster                                                       |
| mako                     | 10.4 ms                                                          | 9.24 ms: 1.12x faster                                                       |
| tomli_loads              | 2.40 sec                                                         | 2.15 sec: 1.12x faster                                                      |
| deepcopy_reduce          | 3.39 us                                                          | 3.08 us: 1.10x faster                                                       |
| pyflate                  | 482 ms                                                           | 447 ms: 1.08x faster                                                        |
| scimark_sparse_mat_mult  | 4.28 ms                                                          | 3.98 ms: 1.08x faster                                                       |
| float                    | 80.2 ms                                                          | 74.6 ms: 1.07x faster                                                       |
| pathlib                  | 17.1 ms                                                          | 16.1 ms: 1.06x faster                                                       |
| scimark_fft              | 312 ms                                                           | 294 ms: 1.06x faster                                                        |
| gc_traversal             | 4.69 ms                                                          | 4.47 ms: 1.05x faster                                                       |
| regex_compile            | 144 ms                                                           | 137 ms: 1.05x faster                                                        |
| crypto_pyaes             | 73.6 ms                                                          | 70.2 ms: 1.05x faster                                                       |
| create_gc_cycles         | 2.00 ms                                                          | 1.91 ms: 1.05x faster                                                       |
| telco                    | 8.40 ms                                                          | 8.06 ms: 1.04x faster                                                       |
| xml_etree_generate       | 85.7 ms                                                          | 82.4 ms: 1.04x faster                                                       |
| nbody                    | 87.8 ms                                                          | 84.7 ms: 1.04x faster                                                       |
| async_tree_io_tg         | 900 ms                                                           | 872 ms: 1.03x faster                                                        |
| fannkuch                 | 353 ms                                                           | 342 ms: 1.03x faster                                                        |
| pprint_safe_repr         | 818 ms                                                           | 795 ms: 1.03x faster                                                        |
| regex_dna                | 249 ms                                                           | 242 ms: 1.03x faster                                                        |
| xml_etree_iterparse      | 103 ms                                                           | 99.7 ms: 1.03x faster                                                       |
| xml_etree_process        | 59.7 ms                                                          | 58.3 ms: 1.02x faster                                                       |
| pickle_dict              | 32.8 us                                                          | 32.1 us: 1.02x faster                                                       |
| pprint_pformat           | 1.66 sec                                                         | 1.62 sec: 1.02x faster                                                      |
| go                       | 165 ms                                                           | 162 ms: 1.02x faster                                                        |
| dulwich_log              | 67.3 ms                                                          | 66.3 ms: 1.01x faster                                                       |
| unpickle                 | 15.7 us                                                          | 15.5 us: 1.01x faster                                                       |
| asyncio_websockets       | 395 ms                                                           | 390 ms: 1.01x faster                                                        |
| pidigits                 | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| unpickle_pure_python     | 224 us                                                           | 222 us: 1.01x faster                                                        |
| xml_etree_parse          | 144 ms                                                           | 142 ms: 1.01x faster                                                        |
| json_dumps               | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                       |
| html5lib                 | 74.7 ms                                                          | 73.9 ms: 1.01x faster                                                       |
| regex_v8                 | 26.0 ms                                                          | 25.8 ms: 1.01x faster                                                       |
| coroutines               | 22.0 ms                                                          | 21.9 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl          | 1.58 sec                                                         | 1.58 sec: 1.00x slower                                                      |
| json_loads               | 25.0 us                                                          | 25.2 us: 1.01x slower                                                       |
| scimark_monte_carlo      | 65.5 ms                                                          | 66.4 ms: 1.01x slower                                                       |
| generators               | 33.5 ms                                                          | 34.0 ms: 1.02x slower                                                       |
| pickle_pure_python       | 307 us                                                           | 312 us: 1.02x slower                                                        |
| pickle                   | 10.6 us                                                          | 10.8 us: 1.02x slower                                                       |
| meteor_contest           | 128 ms                                                           | 131 ms: 1.02x slower                                                        |
| sqlglot_parse            | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                       |
| bpe_tokeniser            | 5.14 sec                                                         | 5.23 sec: 1.02x slower                                                      |
| thrift                   | 880 us                                                           | 896 us: 1.02x slower                                                        |
| pickle_list              | 4.44 us                                                          | 4.53 us: 1.02x slower                                                       |
| coverage                 | 83.5 ms                                                          | 85.2 ms: 1.02x slower                                                       |
| regex_effbot             | 3.40 ms                                                          | 3.48 ms: 1.02x slower                                                       |
| sqlglot_transpile        | 1.76 ms                                                          | 1.81 ms: 1.03x slower                                                       |
| json                     | 5.35 ms                                                          | 5.51 ms: 1.03x slower                                                       |
| tornado_http             | 119 ms                                                           | 123 ms: 1.03x slower                                                        |
| dask                     | 391 ms                                                           | 404 ms: 1.04x slower                                                        |
| pycparser                | 1.22 sec                                                         | 1.27 sec: 1.04x slower                                                      |
| async_tree_memoization   | 460 ms                                                           | 476 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed  | 604 ms                                                           | 628 ms: 1.04x slower                                                        |
| async_tree_none          | 365 ms                                                           | 380 ms: 1.04x slower                                                        |
| unpickle_list            | 4.70 us                                                          | 4.91 us: 1.05x slower                                                       |
| async_tree_io            | 873 ms                                                           | 913 ms: 1.05x slower                                                        |
| python_startup           | 13.2 ms                                                          | 13.8 ms: 1.05x slower                                                       |
| django_template          | 39.0 ms                                                          | 40.9 ms: 1.05x slower                                                       |
| docutils                 | 2.98 sec                                                         | 3.13 sec: 1.05x slower                                                      |
| hexiom                   | 6.35 ms                                                          | 6.68 ms: 1.05x slower                                                       |
| 2to3                     | 291 ms                                                           | 307 ms: 1.05x slower                                                        |
| mdp                      | 2.46 sec                                                         | 2.60 sec: 1.06x slower                                                      |
| sympy_expand             | 501 ms                                                           | 529 ms: 1.06x slower                                                        |
| sympy_str                | 295 ms                                                           | 314 ms: 1.06x slower                                                        |
| logging_silent           | 96.3 ns                                                          | 102 ns: 1.06x slower                                                        |
| async_generators         | 363 ms                                                           | 386 ms: 1.06x slower                                                        |
| genshi_text              | 25.9 ms                                                          | 27.6 ms: 1.07x slower                                                       |
| sympy_sum                | 155 ms                                                           | 165 ms: 1.07x slower                                                        |
| comprehensions           | 17.0 us                                                          | 18.1 us: 1.07x slower                                                       |
| sqlglot_optimize         | 59.5 ms                                                          | 63.7 ms: 1.07x slower                                                       |
| python_startup_no_site   | 8.85 ms                                                          | 9.47 ms: 1.07x slower                                                       |
| scimark_sor              | 119 ms                                                           | 127 ms: 1.07x slower                                                        |
| bench_thread_pool        | 908 us                                                           | 983 us: 1.08x slower                                                        |
| nqueens                  | 88.4 ms                                                          | 96.1 ms: 1.09x slower                                                       |
| typing_runtime_protocols | 171 us                                                           | 186 us: 1.09x slower                                                        |
| deltablue                | 3.37 ms                                                          | 3.69 ms: 1.09x slower                                                       |
| sqlglot_normalize        | 120 ms                                                           | 132 ms: 1.10x slower                                                        |
| chaos                    | 59.6 ms                                                          | 65.9 ms: 1.10x slower                                                       |
| sympy_integrate          | 23.2 ms                                                          | 25.7 ms: 1.11x slower                                                       |
| pylint                   | 339 ms                                                           | 379 ms: 1.12x slower                                                        |
| genshi_xml               | 58.1 ms                                                          | 64.9 ms: 1.12x slower                                                       |
| raytrace                 | 260 ms                                                           | 296 ms: 1.14x slower                                                        |
| scimark_lu               | 97.5 ms                                                          | 122 ms: 1.25x slower                                                        |
| Geometric mean           | (ref)                                                            | 1.00x slower                                                                |

Benchmark hidden because not significant (8): bench_mp_pool, logging_simple, logging_format, sqlite_synth, asyncio_tcp, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 94.51% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x