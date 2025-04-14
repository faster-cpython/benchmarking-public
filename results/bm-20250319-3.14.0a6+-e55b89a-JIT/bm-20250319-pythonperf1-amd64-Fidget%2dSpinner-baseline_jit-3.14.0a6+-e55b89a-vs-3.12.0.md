# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: baseline_jit
- machine: windows-amd64
- commit hash: e55b89a
- commit date: 2025-03-19
- overall geometric mean: 1.017x faster
- HPT reliability: 83.13%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 231 ms: 1.06x slower                                                          |
| docutils       | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 420 ms: 1.84x faster                                                          |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                          |
| async_tree_io              | 731 ms                                                      | 435 ms: 1.68x faster                                                          |
| async_tree_none_tg         | 285 ms                                                      | 179 ms: 1.59x faster                                                          |
| async_tree_none            | 291 ms                                                      | 193 ms: 1.51x faster                                                          |
| async_tree_memoization     | 339 ms                                                      | 227 ms: 1.49x faster                                                          |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                          |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 348 ms: 1.40x faster                                                          |
| Geometric mean             | (ref)                                                       | 1.58x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 57.9 ms: 1.24x faster                                                         |
| float          | 56.8 ms                                                     | 47.6 ms: 1.19x faster                                                         |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                         |
| regex_dna      | 126 ms                                                      | 117 ms: 1.08x faster                                                          |
| regex_v8       | 14.2 ms                                                     | 14.1 ms: 1.01x faster                                                         |
| regex_compile  | 87.5 ms                                                     | 88.3 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                        |
| xml_etree_parse      | 93.0 ms                                                     | 90.2 ms: 1.03x faster                                                         |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.6 ms: 1.03x faster                                                         |
| xml_etree_generate   | 55.8 ms                                                     | 59.7 ms: 1.07x slower                                                         |
| json_loads           | 13.9 us                                                     | 15.1 us: 1.09x slower                                                         |
| xml_etree_process    | 37.7 ms                                                     | 43.0 ms: 1.14x slower                                                         |
| pickle_pure_python   | 195 us                                                      | 228 us: 1.17x slower                                                          |
| unpickle_pure_python | 133 us                                                      | 157 us: 1.18x slower                                                          |
| json_dumps           | 5.70 ms                                                     | 7.01 ms: 1.23x slower                                                         |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.8 ms: 1.28x slower                                                         |
| python_startup         | 19.5 ms                                                     | 26.6 ms: 1.37x slower                                                         |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                         |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                                  |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.5 ms: 2.48x faster                                                         |
| async_tree_io_tg           | 771 ms                                                      | 420 ms: 1.84x faster                                                          |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                          |
| async_tree_io              | 731 ms                                                      | 435 ms: 1.68x faster                                                          |
| async_tree_none_tg         | 285 ms                                                      | 179 ms: 1.59x faster                                                          |
| async_tree_none            | 291 ms                                                      | 193 ms: 1.51x faster                                                          |
| async_tree_memoization     | 339 ms                                                      | 227 ms: 1.49x faster                                                          |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                          |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 348 ms: 1.40x faster                                                          |
| nbody                      | 71.9 ms                                                     | 57.9 ms: 1.24x faster                                                         |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.09 ms: 1.22x faster                                                         |
| float                      | 56.8 ms                                                     | 47.6 ms: 1.19x faster                                                         |
| scimark_fft                | 184 ms                                                      | 159 ms: 1.16x faster                                                          |
| deepcopy                   | 238 us                                                      | 211 us: 1.13x faster                                                          |
| spectral_norm              | 66.9 ms                                                     | 60.8 ms: 1.10x faster                                                         |
| regex_effbot               | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                         |
| generators                 | 22.5 ms                                                     | 20.8 ms: 1.09x faster                                                         |
| regex_dna                  | 126 ms                                                      | 117 ms: 1.08x faster                                                          |
| deepcopy_memo              | 23.7 us                                                     | 22.0 us: 1.08x faster                                                         |
| tomli_loads                | 1.37 sec                                                    | 1.28 sec: 1.07x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 90.2 ms: 1.03x faster                                                         |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                          |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.6 ms: 1.03x faster                                                         |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.02x faster                                                         |
| logging_silent             | 60.5 ns                                                     | 59.7 ns: 1.01x faster                                                         |
| sqlite_synth               | 1.76 us                                                     | 1.74 us: 1.01x faster                                                         |
| regex_v8                   | 14.2 ms                                                     | 14.1 ms: 1.01x faster                                                         |
| dulwich_log                | 44.3 ms                                                     | 44.0 ms: 1.01x faster                                                         |
| go                         | 91.6 ms                                                     | 92.3 ms: 1.01x slower                                                         |
| regex_compile              | 87.5 ms                                                     | 88.3 ms: 1.01x slower                                                         |
| sympy_sum                  | 91.5 ms                                                     | 92.4 ms: 1.01x slower                                                         |
| json                       | 3.05 ms                                                     | 3.10 ms: 1.02x slower                                                         |
| raytrace                   | 192 ms                                                      | 196 ms: 1.02x slower                                                          |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.6 ms: 1.02x slower                                                         |
| meteor_contest             | 74.6 ms                                                     | 76.3 ms: 1.02x slower                                                         |
| bench_thread_pool          | 857 us                                                      | 879 us: 1.03x slower                                                          |
| scimark_sor                | 78.8 ms                                                     | 81.3 ms: 1.03x slower                                                         |
| nqueens                    | 62.8 ms                                                     | 64.8 ms: 1.03x slower                                                         |
| sympy_str                  | 175 ms                                                      | 182 ms: 1.04x slower                                                          |
| scimark_lu                 | 58.9 ms                                                     | 61.2 ms: 1.04x slower                                                         |
| chaos                      | 43.3 ms                                                     | 45.2 ms: 1.04x slower                                                         |
| logging_simple             | 6.28 us                                                     | 6.55 us: 1.04x slower                                                         |
| docutils                   | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.6 ms: 1.05x slower                                                         |
| richards                   | 28.4 ms                                                     | 29.9 ms: 1.05x slower                                                         |
| 2to3                       | 218 ms                                                      | 231 ms: 1.06x slower                                                          |
| async_generators           | 239 ms                                                      | 254 ms: 1.06x slower                                                          |
| richards_super             | 32.1 ms                                                     | 34.1 ms: 1.06x slower                                                         |
| logging_format             | 6.72 us                                                     | 7.14 us: 1.06x slower                                                         |
| xml_etree_generate         | 55.8 ms                                                     | 59.7 ms: 1.07x slower                                                         |
| fannkuch                   | 247 ms                                                      | 265 ms: 1.07x slower                                                          |
| pyflate                    | 295 ms                                                      | 318 ms: 1.08x slower                                                          |
| pycparser                  | 699 ms                                                      | 758 ms: 1.09x slower                                                          |
| json_loads                 | 13.9 us                                                     | 15.1 us: 1.09x slower                                                         |
| pprint_pformat             | 1.05 sec                                                    | 1.14 sec: 1.09x slower                                                        |
| comprehensions             | 14.1 us                                                     | 15.5 us: 1.09x slower                                                         |
| deltablue                  | 2.16 ms                                                     | 2.37 ms: 1.10x slower                                                         |
| pprint_safe_repr           | 513 ms                                                      | 562 ms: 1.10x slower                                                          |
| sympy_expand               | 284 ms                                                      | 318 ms: 1.12x slower                                                          |
| django_template            | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                         |
| xml_etree_process          | 37.7 ms                                                     | 43.0 ms: 1.14x slower                                                         |
| mdp                        | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 55.9 ms: 1.15x slower                                                         |
| pickle_pure_python         | 195 us                                                      | 228 us: 1.17x slower                                                          |
| unpickle_pure_python       | 133 us                                                      | 157 us: 1.18x slower                                                          |
| coverage                   | 40.8 ms                                                     | 49.8 ms: 1.22x slower                                                         |
| telco                      | 4.13 ms                                                     | 5.05 ms: 1.22x slower                                                         |
| json_dumps                 | 5.70 ms                                                     | 7.01 ms: 1.23x slower                                                         |
| typing_runtime_protocols   | 95.1 us                                                     | 120 us: 1.26x slower                                                          |
| python_startup_no_site     | 16.2 ms                                                     | 20.8 ms: 1.28x slower                                                         |
| bench_mp_pool              | 69.2 ms                                                     | 89.4 ms: 1.29x slower                                                         |
| hexiom                     | 4.10 ms                                                     | 5.39 ms: 1.31x slower                                                         |
| gc_traversal               | 1.52 ms                                                     | 2.04 ms: 1.34x slower                                                         |
| python_startup             | 19.5 ms                                                     | 26.6 ms: 1.37x slower                                                         |
| create_gc_cycles           | 752 us                                                      | 1.27 ms: 1.69x slower                                                         |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                  |

Benchmark hidden because not significant (2): mako, deepcopy_reduce
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250319-3.14.0a6+-e55b89a-JIT/bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.017x faster

# HPT report

- Reliability score: 83.13% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown