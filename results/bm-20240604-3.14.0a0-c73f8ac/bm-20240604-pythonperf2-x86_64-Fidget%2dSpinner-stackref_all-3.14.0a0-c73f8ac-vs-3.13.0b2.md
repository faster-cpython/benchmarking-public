# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: c73f8ac
- commit date: 2024-06-04
- overall geometric mean: 1.02x slower
- HPT reliability: 97.08%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 308 ms: 1.06x slower                                                          |
| docutils       | 2.98 sec                                                         | 3.14 sec: 1.05x slower                                                        |
| tornado_http   | 119 ms                                                           | 123 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                            | 1.03x slower                                                                  |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|-------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none         | 365 ms                                                           | 373 ms: 1.02x slower                                                          |
| async_tree_memoization  | 460 ms                                                           | 474 ms: 1.03x slower                                                          |
| async_tree_cpu_io_mixed | 604 ms                                                           | 623 ms: 1.03x slower                                                          |
| Geometric mean          | (ref)                                                            | 1.02x slower                                                                  |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 75.0 ms: 1.07x faster                                                         |
| nbody          | 87.8 ms                                                          | 84.3 ms: 1.04x faster                                                         |
| pidigits       | 254 ms                                                           | 251 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 141 ms: 1.02x faster                                                          |
| regex_dna      | 249 ms                                                           | 245 ms: 1.02x faster                                                          |
| regex_v8       | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                                         |
| regex_effbot   | 3.40 ms                                                          | 3.43 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|---------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads         | 2.40 sec                                                         | 2.10 sec: 1.15x faster                                                        |
| xml_etree_generate  | 85.7 ms                                                          | 81.5 ms: 1.05x faster                                                         |
| pickle_dict         | 32.8 us                                                          | 31.6 us: 1.04x faster                                                         |
| xml_etree_process   | 59.7 ms                                                          | 58.3 ms: 1.02x faster                                                         |
| xml_etree_iterparse | 103 ms                                                           | 100 ms: 1.02x faster                                                          |
| json_dumps          | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                         |
| pickle              | 10.6 us                                                          | 10.5 us: 1.01x faster                                                         |
| pickle_list         | 4.44 us                                                          | 4.42 us: 1.01x faster                                                         |
| pickle_pure_python  | 307 us                                                           | 326 us: 1.06x slower                                                          |
| Geometric mean      | (ref)                                                            | 1.02x faster                                                                  |

Benchmark hidden because not significant (5): unpickle_pure_python, xml_etree_parse, unpickle, unpickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.7 ms: 1.04x slower                                                         |
| python_startup_no_site | 8.85 ms                                                          | 9.41 ms: 1.06x slower                                                         |
| Geometric mean         | (ref)                                                            | 1.05x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|-----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.27 ms: 1.12x faster                                                         |
| django_template | 39.0 ms                                                          | 43.0 ms: 1.10x slower                                                         |
| genshi_text     | 25.9 ms                                                          | 28.8 ms: 1.11x slower                                                         |
| genshi_xml      | 58.1 ms                                                          | 67.0 ms: 1.15x slower                                                         |
| Geometric mean  | (ref)                                                            | 1.06x slower                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf2-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|--------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| richards                 | 53.4 ms                                                          | 45.7 ms: 1.17x faster                                                         |
| spectral_norm            | 97.3 ms                                                          | 83.4 ms: 1.17x faster                                                         |
| richards_super           | 61.2 ms                                                          | 53.3 ms: 1.15x faster                                                         |
| tomli_loads              | 2.40 sec                                                         | 2.10 sec: 1.15x faster                                                        |
| mako                     | 10.4 ms                                                          | 9.27 ms: 1.12x faster                                                         |
| float                    | 80.2 ms                                                          | 75.0 ms: 1.07x faster                                                         |
| pyflate                  | 482 ms                                                           | 454 ms: 1.06x faster                                                          |
| scimark_fft              | 312 ms                                                           | 295 ms: 1.06x faster                                                          |
| xml_etree_generate       | 85.7 ms                                                          | 81.5 ms: 1.05x faster                                                         |
| gc_traversal             | 4.69 ms                                                          | 4.47 ms: 1.05x faster                                                         |
| create_gc_cycles         | 2.00 ms                                                          | 1.91 ms: 1.05x faster                                                         |
| nbody                    | 87.8 ms                                                          | 84.3 ms: 1.04x faster                                                         |
| pathlib                  | 17.1 ms                                                          | 16.5 ms: 1.04x faster                                                         |
| pickle_dict              | 32.8 us                                                          | 31.6 us: 1.04x faster                                                         |
| coverage                 | 83.5 ms                                                          | 80.3 ms: 1.04x faster                                                         |
| pprint_safe_repr         | 818 ms                                                           | 790 ms: 1.03x faster                                                          |
| xml_etree_process        | 59.7 ms                                                          | 58.3 ms: 1.02x faster                                                         |
| xml_etree_iterparse      | 103 ms                                                           | 100 ms: 1.02x faster                                                          |
| regex_compile            | 144 ms                                                           | 141 ms: 1.02x faster                                                          |
| scimark_sparse_mat_mult  | 4.28 ms                                                          | 4.20 ms: 1.02x faster                                                         |
| pprint_pformat           | 1.66 sec                                                         | 1.63 sec: 1.02x faster                                                        |
| regex_dna                | 249 ms                                                           | 245 ms: 1.02x faster                                                          |
| crypto_pyaes             | 73.6 ms                                                          | 72.4 ms: 1.02x faster                                                         |
| regex_v8                 | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                                         |
| telco                    | 8.40 ms                                                          | 8.27 ms: 1.02x faster                                                         |
| dulwich_log              | 67.3 ms                                                          | 66.3 ms: 1.01x faster                                                         |
| asyncio_websockets       | 395 ms                                                           | 390 ms: 1.01x faster                                                          |
| pidigits                 | 254 ms                                                           | 251 ms: 1.01x faster                                                          |
| go                       | 165 ms                                                           | 163 ms: 1.01x faster                                                          |
| json_dumps               | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                         |
| json                     | 5.35 ms                                                          | 5.31 ms: 1.01x faster                                                         |
| pickle                   | 10.6 us                                                          | 10.5 us: 1.01x faster                                                         |
| pickle_list              | 4.44 us                                                          | 4.42 us: 1.01x faster                                                         |
| sqlite_synth             | 2.80 us                                                          | 2.78 us: 1.01x faster                                                         |
| fannkuch                 | 353 ms                                                           | 355 ms: 1.01x slower                                                          |
| regex_effbot             | 3.40 ms                                                          | 3.43 ms: 1.01x slower                                                         |
| deepcopy_memo            | 37.3 us                                                          | 37.6 us: 1.01x slower                                                         |
| meteor_contest           | 128 ms                                                           | 129 ms: 1.01x slower                                                          |
| asyncio_tcp              | 378 ms                                                           | 381 ms: 1.01x slower                                                          |
| sqlglot_parse            | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                         |
| async_tree_none          | 365 ms                                                           | 373 ms: 1.02x slower                                                          |
| logging_simple           | 6.40 us                                                          | 6.55 us: 1.02x slower                                                         |
| generators               | 33.5 ms                                                          | 34.3 ms: 1.02x slower                                                         |
| tornado_http             | 119 ms                                                           | 123 ms: 1.03x slower                                                          |
| thrift                   | 880 us                                                           | 905 us: 1.03x slower                                                          |
| async_tree_memoization   | 460 ms                                                           | 474 ms: 1.03x slower                                                          |
| async_tree_cpu_io_mixed  | 604 ms                                                           | 623 ms: 1.03x slower                                                          |
| python_startup           | 13.2 ms                                                          | 13.7 ms: 1.04x slower                                                         |
| dask                     | 391 ms                                                           | 405 ms: 1.04x slower                                                          |
| sqlglot_transpile        | 1.76 ms                                                          | 1.84 ms: 1.04x slower                                                         |
| pycparser                | 1.22 sec                                                         | 1.27 sec: 1.04x slower                                                        |
| mdp                      | 2.46 sec                                                         | 2.59 sec: 1.05x slower                                                        |
| docutils                 | 2.98 sec                                                         | 3.14 sec: 1.05x slower                                                        |
| scimark_monte_carlo      | 65.5 ms                                                          | 69.1 ms: 1.05x slower                                                         |
| 2to3                     | 291 ms                                                           | 308 ms: 1.06x slower                                                          |
| bench_thread_pool        | 908 us                                                           | 959 us: 1.06x slower                                                          |
| pickle_pure_python       | 307 us                                                           | 326 us: 1.06x slower                                                          |
| python_startup_no_site   | 8.85 ms                                                          | 9.41 ms: 1.06x slower                                                         |
| sympy_str                | 295 ms                                                           | 316 ms: 1.07x slower                                                          |
| sympy_expand             | 501 ms                                                           | 538 ms: 1.07x slower                                                          |
| sqlglot_normalize        | 120 ms                                                           | 129 ms: 1.08x slower                                                          |
| sqlglot_optimize         | 59.5 ms                                                          | 64.2 ms: 1.08x slower                                                         |
| async_generators         | 363 ms                                                           | 392 ms: 1.08x slower                                                          |
| sympy_sum                | 155 ms                                                           | 168 ms: 1.08x slower                                                          |
| typing_runtime_protocols | 171 us                                                           | 185 us: 1.09x slower                                                          |
| comprehensions           | 17.0 us                                                          | 18.4 us: 1.09x slower                                                         |
| raytrace                 | 260 ms                                                           | 285 ms: 1.09x slower                                                          |
| hexiom                   | 6.35 ms                                                          | 6.96 ms: 1.09x slower                                                         |
| deepcopy_reduce          | 3.39 us                                                          | 3.73 us: 1.10x slower                                                         |
| django_template          | 39.0 ms                                                          | 43.0 ms: 1.10x slower                                                         |
| chaos                    | 59.6 ms                                                          | 66.0 ms: 1.11x slower                                                         |
| genshi_text              | 25.9 ms                                                          | 28.8 ms: 1.11x slower                                                         |
| sympy_integrate          | 23.2 ms                                                          | 25.8 ms: 1.11x slower                                                         |
| nqueens                  | 88.4 ms                                                          | 98.7 ms: 1.12x slower                                                         |
| pylint                   | 339 ms                                                           | 380 ms: 1.12x slower                                                          |
| deepcopy                 | 377 us                                                           | 423 us: 1.12x slower                                                          |
| scimark_sor              | 119 ms                                                           | 134 ms: 1.13x slower                                                          |
| logging_silent           | 96.3 ns                                                          | 109 ns: 1.13x slower                                                          |
| deltablue                | 3.37 ms                                                          | 3.82 ms: 1.13x slower                                                         |
| genshi_xml               | 58.1 ms                                                          | 67.0 ms: 1.15x slower                                                         |
| scimark_lu               | 97.5 ms                                                          | 122 ms: 1.26x slower                                                          |
| Geometric mean           | (ref)                                                            | 1.02x slower                                                                  |

Benchmark hidden because not significant (15): bench_mp_pool, async_tree_io_tg, html5lib, unpickle_pure_python, xml_etree_parse, coroutines, unpickle, asyncio_tcp_ssl, logging_format, unpickle_list, async_tree_none_tg, async_tree_io, json_loads, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, chameleon, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 97.08% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x