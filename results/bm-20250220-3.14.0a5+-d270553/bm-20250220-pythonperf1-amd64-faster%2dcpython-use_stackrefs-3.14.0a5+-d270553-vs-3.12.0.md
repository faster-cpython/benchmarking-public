# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: windows-amd64
- commit hash: d270553
- commit date: 2025-02-20
- overall geometric mean: 1.024x slower
- HPT reliability: 99.75%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 231 ms: 1.06x slower                                                           |
| docutils       | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                         |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 444 ms: 1.74x faster                                                           |
| async_tree_io              | 731 ms                                                      | 444 ms: 1.65x faster                                                           |
| async_tree_memoization_tg  | 367 ms                                                      | 228 ms: 1.61x faster                                                           |
| async_tree_none_tg         | 285 ms                                                      | 186 ms: 1.53x faster                                                           |
| async_tree_none            | 291 ms                                                      | 199 ms: 1.47x faster                                                           |
| async_tree_memoization     | 339 ms                                                      | 234 ms: 1.45x faster                                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 350 ms: 1.44x faster                                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 355 ms: 1.38x faster                                                           |
| Geometric mean             | (ref)                                                       | 1.53x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 51.5 ms: 1.10x faster                                                          |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                           |
| nbody          | 71.9 ms                                                     | 78.4 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.49 ms: 1.09x faster                                                          |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                           |
| regex_compile  | 87.5 ms                                                     | 92.9 ms: 1.06x slower                                                          |
| regex_v8       | 14.2 ms                                                     | 15.2 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 91.2 ms: 1.02x faster                                                          |
| xml_etree_iterparse  | 65.2 ms                                                     | 65.7 ms: 1.01x slower                                                          |
| json_loads           | 13.9 us                                                     | 15.1 us: 1.08x slower                                                          |
| xml_etree_generate   | 55.8 ms                                                     | 61.2 ms: 1.10x slower                                                          |
| xml_etree_process    | 37.7 ms                                                     | 44.2 ms: 1.17x slower                                                          |
| tomli_loads          | 1.37 sec                                                    | 1.62 sec: 1.19x slower                                                         |
| json_dumps           | 5.70 ms                                                     | 7.11 ms: 1.25x slower                                                          |
| pickle_pure_python   | 195 us                                                      | 244 us: 1.25x slower                                                           |
| unpickle_pure_python | 133 us                                                      | 170 us: 1.27x slower                                                           |
| Geometric mean       | (ref)                                                       | 1.14x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.1 ms: 1.18x slower                                                          |
| python_startup         | 19.5 ms                                                     | 25.2 ms: 1.29x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 8.26 ms: 1.17x slower                                                          |
| django_template | 22.9 ms                                                     | 27.3 ms: 1.19x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.18x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 30.0 ms: 2.68x faster                                                          |
| async_tree_io_tg           | 771 ms                                                      | 444 ms: 1.74x faster                                                           |
| async_tree_io              | 731 ms                                                      | 444 ms: 1.65x faster                                                           |
| async_tree_memoization_tg  | 367 ms                                                      | 228 ms: 1.61x faster                                                           |
| async_tree_none_tg         | 285 ms                                                      | 186 ms: 1.53x faster                                                           |
| async_tree_none            | 291 ms                                                      | 199 ms: 1.47x faster                                                           |
| async_tree_memoization     | 339 ms                                                      | 234 ms: 1.45x faster                                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 350 ms: 1.44x faster                                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 355 ms: 1.38x faster                                                           |
| deepcopy                   | 238 us                                                      | 198 us: 1.20x faster                                                           |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.16x faster                                                          |
| float                      | 56.8 ms                                                     | 51.5 ms: 1.10x faster                                                          |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                          |
| regex_effbot               | 1.62 ms                                                     | 1.49 ms: 1.09x faster                                                          |
| comprehensions             | 14.1 us                                                     | 13.0 us: 1.09x faster                                                          |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                           |
| deepcopy_memo              | 23.7 us                                                     | 22.4 us: 1.06x faster                                                          |
| dulwich_log                | 44.3 ms                                                     | 42.1 ms: 1.05x faster                                                          |
| xml_etree_parse            | 93.0 ms                                                     | 91.2 ms: 1.02x faster                                                          |
| async_generators           | 239 ms                                                      | 236 ms: 1.01x faster                                                           |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                           |
| spectral_norm              | 66.9 ms                                                     | 66.7 ms: 1.00x faster                                                          |
| xml_etree_iterparse        | 65.2 ms                                                     | 65.7 ms: 1.01x slower                                                          |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                                          |
| json                       | 3.05 ms                                                     | 3.08 ms: 1.01x slower                                                          |
| sympy_sum                  | 91.5 ms                                                     | 92.8 ms: 1.01x slower                                                          |
| raytrace                   | 192 ms                                                      | 197 ms: 1.02x slower                                                           |
| docutils                   | 1.66 sec                                                    | 1.71 sec: 1.03x slower                                                         |
| go                         | 91.6 ms                                                     | 94.8 ms: 1.04x slower                                                          |
| sympy_str                  | 175 ms                                                      | 182 ms: 1.04x slower                                                           |
| meteor_contest             | 74.6 ms                                                     | 78.7 ms: 1.05x slower                                                          |
| chaos                      | 43.3 ms                                                     | 45.9 ms: 1.06x slower                                                          |
| 2to3                       | 218 ms                                                      | 231 ms: 1.06x slower                                                           |
| regex_compile              | 87.5 ms                                                     | 92.9 ms: 1.06x slower                                                          |
| sympy_integrate            | 13.0 ms                                                     | 13.8 ms: 1.06x slower                                                          |
| regex_v8                   | 14.2 ms                                                     | 15.2 ms: 1.07x slower                                                          |
| sqlglot_optimize           | 34.5 ms                                                     | 37.2 ms: 1.08x slower                                                          |
| json_loads                 | 13.9 us                                                     | 15.1 us: 1.08x slower                                                          |
| sqlglot_normalize          | 187 ms                                                      | 203 ms: 1.08x slower                                                           |
| nbody                      | 71.9 ms                                                     | 78.4 ms: 1.09x slower                                                          |
| xml_etree_generate         | 55.8 ms                                                     | 61.2 ms: 1.10x slower                                                          |
| sympy_expand               | 284 ms                                                      | 311 ms: 1.10x slower                                                           |
| deltablue                  | 2.16 ms                                                     | 2.39 ms: 1.10x slower                                                          |
| logging_format             | 6.72 us                                                     | 7.43 us: 1.11x slower                                                          |
| logging_simple             | 6.28 us                                                     | 6.95 us: 1.11x slower                                                          |
| pycparser                  | 699 ms                                                      | 786 ms: 1.13x slower                                                           |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.91 ms: 1.14x slower                                                          |
| scimark_fft                | 184 ms                                                      | 210 ms: 1.14x slower                                                           |
| nqueens                    | 62.8 ms                                                     | 71.8 ms: 1.14x slower                                                          |
| sqlglot_transpile          | 1.02 ms                                                     | 1.17 ms: 1.15x slower                                                          |
| logging_silent             | 60.5 ns                                                     | 69.6 ns: 1.15x slower                                                          |
| pprint_pformat             | 1.05 sec                                                    | 1.20 sec: 1.15x slower                                                         |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.5 ms: 1.15x slower                                                          |
| hexiom                     | 4.10 ms                                                     | 4.75 ms: 1.16x slower                                                          |
| pprint_safe_repr           | 513 ms                                                      | 596 ms: 1.16x slower                                                           |
| mako                       | 7.09 ms                                                     | 8.26 ms: 1.17x slower                                                          |
| pyflate                    | 295 ms                                                      | 344 ms: 1.17x slower                                                           |
| crypto_pyaes               | 48.5 ms                                                     | 56.6 ms: 1.17x slower                                                          |
| xml_etree_process          | 37.7 ms                                                     | 44.2 ms: 1.17x slower                                                          |
| richards_super             | 32.1 ms                                                     | 37.8 ms: 1.18x slower                                                          |
| richards                   | 28.4 ms                                                     | 33.4 ms: 1.18x slower                                                          |
| python_startup_no_site     | 16.2 ms                                                     | 19.1 ms: 1.18x slower                                                          |
| mdp                        | 1.37 sec                                                    | 1.62 sec: 1.18x slower                                                         |
| coverage                   | 40.8 ms                                                     | 48.3 ms: 1.18x slower                                                          |
| scimark_sor                | 78.8 ms                                                     | 93.3 ms: 1.18x slower                                                          |
| tomli_loads                | 1.37 sec                                                    | 1.62 sec: 1.19x slower                                                         |
| sqlglot_parse              | 804 us                                                      | 954 us: 1.19x slower                                                           |
| django_template            | 22.9 ms                                                     | 27.3 ms: 1.19x slower                                                          |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.21x slower                                                           |
| telco                      | 4.13 ms                                                     | 5.01 ms: 1.21x slower                                                          |
| bench_mp_pool              | 69.2 ms                                                     | 85.5 ms: 1.24x slower                                                          |
| json_dumps                 | 5.70 ms                                                     | 7.11 ms: 1.25x slower                                                          |
| pickle_pure_python         | 195 us                                                      | 244 us: 1.25x slower                                                           |
| scimark_lu                 | 58.9 ms                                                     | 73.9 ms: 1.26x slower                                                          |
| unpickle_pure_python       | 133 us                                                      | 170 us: 1.27x slower                                                           |
| fannkuch                   | 247 ms                                                      | 317 ms: 1.29x slower                                                           |
| python_startup             | 19.5 ms                                                     | 25.2 ms: 1.29x slower                                                          |
| gc_traversal               | 1.52 ms                                                     | 2.02 ms: 1.32x slower                                                          |
| create_gc_cycles           | 752 us                                                      | 1.26 ms: 1.68x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                   |

Benchmark hidden because not significant (2): deepcopy_reduce, bench_thread_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250220-3.14.0a5+-d270553/bm-20250220-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.024x slower

# HPT report

- Reliability score: 99.75% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown