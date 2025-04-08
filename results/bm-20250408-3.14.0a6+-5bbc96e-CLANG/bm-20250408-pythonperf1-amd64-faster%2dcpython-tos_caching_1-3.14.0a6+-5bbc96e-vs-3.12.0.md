# Results vs. 3.12.0

- fork: faster-cpython
- ref: tos_caching_1
- machine: windows-amd64
- commit hash: 5bbc96e
- commit date: 2025-04-08
- overall geometric mean: 1.292x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 198 ms: 1.10x faster                                                           |
| docutils       | 1.66 sec                                                    | 1.53 sec: 1.09x faster                                                         |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 350 ms: 2.20x faster                                                           |
| async_tree_io              | 731 ms                                                      | 343 ms: 2.13x faster                                                           |
| async_tree_none            | 291 ms                                                      | 153 ms: 1.90x faster                                                           |
| async_tree_none_tg         | 285 ms                                                      | 152 ms: 1.88x faster                                                           |
| async_tree_memoization_tg  | 367 ms                                                      | 197 ms: 1.87x faster                                                           |
| async_tree_memoization     | 339 ms                                                      | 183 ms: 1.85x faster                                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 317 ms: 1.58x faster                                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 311 ms: 1.57x faster                                                           |
| Geometric mean             | (ref)                                                       | 1.86x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 35.9 ms: 1.58x faster                                                          |
| nbody          | 71.9 ms                                                     | 52.8 ms: 1.36x faster                                                          |
| pidigits       | 152 ms                                                      | 144 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                       | 1.31x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 67.5 ms: 1.30x faster                                                          |
| regex_v8       | 14.2 ms                                                     | 12.3 ms: 1.16x faster                                                          |
| regex_effbot   | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                          |
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 981 ms: 1.39x faster                                                           |
| unpickle_pure_python | 133 us                                                      | 104 us: 1.28x faster                                                           |
| pickle_pure_python   | 195 us                                                      | 165 us: 1.18x faster                                                           |
| xml_etree_process    | 37.7 ms                                                     | 32.8 ms: 1.15x faster                                                          |
| xml_etree_generate   | 55.8 ms                                                     | 48.8 ms: 1.14x faster                                                          |
| xml_etree_iterparse  | 65.2 ms                                                     | 61.0 ms: 1.07x faster                                                          |
| xml_etree_parse      | 93.0 ms                                                     | 89.6 ms: 1.04x faster                                                          |
| json_dumps           | 5.70 ms                                                     | 5.58 ms: 1.02x faster                                                          |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.7 ms: 1.27x slower                                                          |
| python_startup         | 19.5 ms                                                     | 26.8 ms: 1.37x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.76 ms: 1.23x faster                                                          |
| django_template | 22.9 ms                                                     | 18.8 ms: 1.22x faster                                                          |
| Geometric mean  | (ref)                                                       | 1.23x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.7 ms: 2.62x faster                                                          |
| async_tree_io_tg           | 771 ms                                                      | 350 ms: 2.20x faster                                                           |
| async_tree_io              | 731 ms                                                      | 343 ms: 2.13x faster                                                           |
| mdp                        | 1.37 sec                                                    | 671 ms: 2.05x faster                                                           |
| async_tree_none            | 291 ms                                                      | 153 ms: 1.90x faster                                                           |
| async_tree_none_tg         | 285 ms                                                      | 152 ms: 1.88x faster                                                           |
| async_tree_memoization_tg  | 367 ms                                                      | 197 ms: 1.87x faster                                                           |
| async_tree_memoization     | 339 ms                                                      | 183 ms: 1.85x faster                                                           |
| deepcopy_memo              | 23.7 us                                                     | 13.3 us: 1.78x faster                                                          |
| deepcopy                   | 238 us                                                      | 135 us: 1.77x faster                                                           |
| comprehensions             | 14.1 us                                                     | 8.19 us: 1.72x faster                                                          |
| go                         | 91.6 ms                                                     | 54.8 ms: 1.67x faster                                                          |
| scimark_sor                | 78.8 ms                                                     | 47.2 ms: 1.67x faster                                                          |
| scimark_monte_carlo        | 43.7 ms                                                     | 27.5 ms: 1.59x faster                                                          |
| generators                 | 22.5 ms                                                     | 14.2 ms: 1.59x faster                                                          |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 317 ms: 1.58x faster                                                           |
| float                      | 56.8 ms                                                     | 35.9 ms: 1.58x faster                                                          |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 311 ms: 1.57x faster                                                           |
| spectral_norm              | 66.9 ms                                                     | 44.9 ms: 1.49x faster                                                          |
| deepcopy_reduce            | 2.09 us                                                     | 1.43 us: 1.47x faster                                                          |
| chaos                      | 43.3 ms                                                     | 29.5 ms: 1.47x faster                                                          |
| deltablue                  | 2.16 ms                                                     | 1.48 ms: 1.46x faster                                                          |
| hexiom                     | 4.10 ms                                                     | 2.81 ms: 1.46x faster                                                          |
| raytrace                   | 192 ms                                                      | 134 ms: 1.44x faster                                                           |
| logging_silent             | 60.5 ns                                                     | 42.4 ns: 1.43x faster                                                          |
| tomli_loads                | 1.37 sec                                                    | 981 ms: 1.39x faster                                                           |
| richards                   | 28.4 ms                                                     | 20.8 ms: 1.37x faster                                                          |
| richards_super             | 32.1 ms                                                     | 23.5 ms: 1.36x faster                                                          |
| nbody                      | 71.9 ms                                                     | 52.8 ms: 1.36x faster                                                          |
| nqueens                    | 62.8 ms                                                     | 46.2 ms: 1.36x faster                                                          |
| scimark_fft                | 184 ms                                                      | 139 ms: 1.33x faster                                                           |
| async_generators           | 239 ms                                                      | 181 ms: 1.32x faster                                                           |
| pyflate                    | 295 ms                                                      | 224 ms: 1.32x faster                                                           |
| coroutines                 | 14.3 ms                                                     | 10.9 ms: 1.31x faster                                                          |
| scimark_lu                 | 58.9 ms                                                     | 45.4 ms: 1.30x faster                                                          |
| regex_compile              | 87.5 ms                                                     | 67.5 ms: 1.30x faster                                                          |
| pprint_safe_repr           | 513 ms                                                      | 399 ms: 1.29x faster                                                           |
| crypto_pyaes               | 48.5 ms                                                     | 37.8 ms: 1.28x faster                                                          |
| pprint_pformat             | 1.05 sec                                                    | 815 ms: 1.28x faster                                                           |
| unpickle_pure_python       | 133 us                                                      | 104 us: 1.28x faster                                                           |
| fannkuch                   | 247 ms                                                      | 200 ms: 1.23x faster                                                           |
| mako                       | 7.09 ms                                                     | 5.76 ms: 1.23x faster                                                          |
| django_template            | 22.9 ms                                                     | 18.8 ms: 1.22x faster                                                          |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.13 ms: 1.20x faster                                                          |
| sqlite_synth               | 1.76 us                                                     | 1.48 us: 1.19x faster                                                          |
| logging_simple             | 6.28 us                                                     | 5.29 us: 1.19x faster                                                          |
| pickle_pure_python         | 195 us                                                      | 165 us: 1.18x faster                                                           |
| logging_format             | 6.72 us                                                     | 5.70 us: 1.18x faster                                                          |
| sympy_str                  | 175 ms                                                      | 149 ms: 1.18x faster                                                           |
| sympy_sum                  | 91.5 ms                                                     | 78.2 ms: 1.17x faster                                                          |
| regex_v8                   | 14.2 ms                                                     | 12.3 ms: 1.16x faster                                                          |
| sympy_integrate            | 13.0 ms                                                     | 11.2 ms: 1.16x faster                                                          |
| xml_etree_process          | 37.7 ms                                                     | 32.8 ms: 1.15x faster                                                          |
| xml_etree_generate         | 55.8 ms                                                     | 48.8 ms: 1.14x faster                                                          |
| pycparser                  | 699 ms                                                      | 622 ms: 1.12x faster                                                           |
| meteor_contest             | 74.6 ms                                                     | 66.4 ms: 1.12x faster                                                          |
| sympy_expand               | 284 ms                                                      | 257 ms: 1.11x faster                                                           |
| dulwich_log                | 44.3 ms                                                     | 40.1 ms: 1.10x faster                                                          |
| 2to3                       | 218 ms                                                      | 198 ms: 1.10x faster                                                           |
| regex_effbot               | 1.62 ms                                                     | 1.47 ms: 1.10x faster                                                          |
| typing_runtime_protocols   | 95.1 us                                                     | 86.9 us: 1.09x faster                                                          |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                           |
| docutils                   | 1.66 sec                                                    | 1.53 sec: 1.09x faster                                                         |
| xml_etree_iterparse        | 65.2 ms                                                     | 61.0 ms: 1.07x faster                                                          |
| json                       | 3.05 ms                                                     | 2.88 ms: 1.06x faster                                                          |
| pidigits                   | 152 ms                                                      | 144 ms: 1.05x faster                                                           |
| xml_etree_parse            | 93.0 ms                                                     | 89.6 ms: 1.04x faster                                                          |
| coverage                   | 40.8 ms                                                     | 39.5 ms: 1.03x faster                                                          |
| bench_thread_pool          | 857 us                                                      | 834 us: 1.03x faster                                                           |
| json_dumps                 | 5.70 ms                                                     | 5.58 ms: 1.02x faster                                                          |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                          |
| telco                      | 4.13 ms                                                     | 4.22 ms: 1.02x slower                                                          |
| python_startup_no_site     | 16.2 ms                                                     | 20.7 ms: 1.27x slower                                                          |
| bench_mp_pool              | 69.2 ms                                                     | 88.3 ms: 1.28x slower                                                          |
| python_startup             | 19.5 ms                                                     | 26.8 ms: 1.37x slower                                                          |
| create_gc_cycles           | 752 us                                                      | 1.35 ms: 1.80x slower                                                          |
| gc_traversal               | 1.52 ms                                                     | 2.77 ms: 1.82x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.28x faster                                                                   |
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250408-3.14.0a6+-5bbc96e-CLANG/bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.292x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: unknown