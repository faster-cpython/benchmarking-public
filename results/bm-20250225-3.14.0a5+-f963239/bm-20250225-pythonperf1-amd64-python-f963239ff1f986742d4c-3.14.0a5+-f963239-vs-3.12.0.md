# Results vs. 3.12.0

- fork: python
- ref: f963239ff1f986742d4c
- machine: windows-amd64
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.029x faster
- HPT reliability: 82.57%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 410 ms: 1.88x faster                                                        |
| async_tree_io              | 731 ms                                                      | 423 ms: 1.73x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 176 ms: 1.62x faster                                                        |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 339 ms: 1.44x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.61x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 47.8 ms: 1.19x faster                                                       |
| nbody          | 71.9 ms                                                     | 74.1 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                       |
| regex_dna      | 126 ms                                                      | 112 ms: 1.12x faster                                                        |
| regex_v8       | 14.2 ms                                                     | 13.5 ms: 1.05x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 88.2 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 63.7 ms: 1.02x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 91.2 ms: 1.02x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 58.7 ms: 1.05x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.06x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 41.5 ms: 1.10x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.17x slower                                                        |
| pickle_pure_python   | 195 us                                                      | 237 us: 1.21x slower                                                        |
| json_dumps           | 5.70 ms                                                     | 7.05 ms: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.8 ms: 1.22x slower                                                       |
| python_startup         | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.86 ms: 1.03x faster                                                       |
| django_template | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.1 ms: 2.51x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 410 ms: 1.88x faster                                                        |
| async_tree_io              | 731 ms                                                      | 423 ms: 1.73x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 176 ms: 1.62x faster                                                        |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.51x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 343 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 339 ms: 1.44x faster                                                        |
| deepcopy                   | 238 us                                                      | 190 us: 1.25x faster                                                        |
| comprehensions             | 14.1 us                                                     | 11.3 us: 1.25x faster                                                       |
| float                      | 56.8 ms                                                     | 47.8 ms: 1.19x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.3 ms: 1.17x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.42 ms: 1.14x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.0 us: 1.13x faster                                                       |
| regex_dna                  | 126 ms                                                      | 112 ms: 1.12x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 61.5 ms: 1.09x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 1.94 us: 1.08x faster                                                       |
| async_generators           | 239 ms                                                      | 226 ms: 1.06x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.06x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.5 ms: 1.05x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.86 ms: 1.03x faster                                                       |
| go                         | 91.6 ms                                                     | 88.6 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.7 ms: 1.02x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 43.4 ms: 1.02x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 91.2 ms: 1.02x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 90.5 ms: 1.01x faster                                                       |
| raytrace                   | 192 ms                                                      | 191 ms: 1.01x faster                                                        |
| sympy_str                  | 175 ms                                                      | 176 ms: 1.01x slower                                                        |
| chaos                      | 43.3 ms                                                     | 43.6 ms: 1.01x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 88.2 ms: 1.01x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 63.6 ms: 1.01x slower                                                       |
| json                       | 3.05 ms                                                     | 3.14 ms: 1.03x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 76.9 ms: 1.03x slower                                                       |
| nbody                      | 71.9 ms                                                     | 74.1 ms: 1.03x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 50.0 ms: 1.03x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.53 us: 1.04x slower                                                       |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                        |
| scimark_fft                | 184 ms                                                      | 192 ms: 1.04x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                       |
| logging_format             | 6.72 us                                                     | 7.03 us: 1.05x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 58.7 ms: 1.05x slower                                                       |
| pycparser                  | 699 ms                                                      | 738 ms: 1.06x slower                                                        |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.06x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.29 ms: 1.06x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.72 ms: 1.06x slower                                                       |
| sympy_expand               | 284 ms                                                      | 302 ms: 1.06x slower                                                        |
| hexiom                     | 4.10 ms                                                     | 4.38 ms: 1.07x slower                                                       |
| pyflate                    | 295 ms                                                      | 315 ms: 1.07x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.1 ms: 1.08x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.13 sec: 1.08x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 65.2 ns: 1.08x slower                                                       |
| richards                   | 28.4 ms                                                     | 30.7 ms: 1.08x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 558 ms: 1.09x slower                                                        |
| django_template            | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                       |
| richards_super             | 32.1 ms                                                     | 35.1 ms: 1.10x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 41.5 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.12x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 66.9 ms: 1.14x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.8 ms: 1.15x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 91.0 ms: 1.16x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.17x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.89 ms: 1.19x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.64 sec: 1.19x slower                                                      |
| fannkuch                   | 247 ms                                                      | 296 ms: 1.20x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 237 us: 1.21x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 19.8 ms: 1.22x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 7.05 ms: 1.24x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 88.7 ms: 1.28x slower                                                       |
| python_startup             | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.06 ms: 1.35x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.66x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (2): pidigits, bench_thread_pool
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250225-3.14.0a5+-f963239/bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.029x faster

# HPT report

- Reliability score: 82.57% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown