# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: windows-amd64
- commit hash: f03f745
- commit date: 2024-10-29
- overall geometric mean: 1.104x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 247 ms: 1.13x slower                                                           |
| docutils       | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                                         |
| tornado_http   | 89.5 ms                                                     | 96.4 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 276 ms: 1.33x faster                                                           |
| async_tree_none_tg         | 285 ms                                                      | 224 ms: 1.27x faster                                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 407 ms: 1.23x faster                                                           |
| async_tree_io              | 731 ms                                                      | 592 ms: 1.23x faster                                                           |
| async_tree_none            | 291 ms                                                      | 237 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 402 ms: 1.22x faster                                                           |
| async_tree_io_tg           | 771 ms                                                      | 660 ms: 1.17x faster                                                           |
| async_tree_memoization     | 339 ms                                                      | 294 ms: 1.15x faster                                                           |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                           |
| float          | 56.8 ms                                                     | 61.5 ms: 1.08x slower                                                          |
| nbody          | 71.9 ms                                                     | 89.4 ms: 1.24x slower                                                          |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 114 ms: 1.11x faster                                                           |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                          |
| regex_v8       | 14.2 ms                                                     | 15.1 ms: 1.06x slower                                                          |
| regex_compile  | 87.5 ms                                                     | 99.9 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 96.0 ms: 1.03x slower                                                          |
| xml_etree_iterparse  | 65.2 ms                                                     | 69.9 ms: 1.07x slower                                                          |
| json_loads           | 13.9 us                                                     | 14.9 us: 1.07x slower                                                          |
| xml_etree_generate   | 55.8 ms                                                     | 63.6 ms: 1.14x slower                                                          |
| xml_etree_process    | 37.7 ms                                                     | 45.9 ms: 1.22x slower                                                          |
| json_dumps           | 5.70 ms                                                     | 7.13 ms: 1.25x slower                                                          |
| pickle_pure_python   | 195 us                                                      | 249 us: 1.28x slower                                                           |
| tomli_loads          | 1.37 sec                                                    | 1.77 sec: 1.29x slower                                                         |
| unpickle_pure_python | 133 us                                                      | 183 us: 1.38x slower                                                           |
| Geometric mean       | (ref)                                                       | 1.19x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.7 ms: 1.09x slower                                                          |
| python_startup         | 19.5 ms                                                     | 24.1 ms: 1.24x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 8.02 ms: 1.13x slower                                                          |
| django_template | 22.9 ms                                                     | 28.4 ms: 1.24x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.18x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 276 ms: 1.33x faster                                                           |
| async_tree_none_tg         | 285 ms                                                      | 224 ms: 1.27x faster                                                           |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 407 ms: 1.23x faster                                                           |
| async_tree_io              | 731 ms                                                      | 592 ms: 1.23x faster                                                           |
| async_tree_none            | 291 ms                                                      | 237 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 402 ms: 1.22x faster                                                           |
| async_tree_io_tg           | 771 ms                                                      | 660 ms: 1.17x faster                                                           |
| async_tree_memoization     | 339 ms                                                      | 294 ms: 1.15x faster                                                           |
| deepcopy                   | 238 us                                                      | 212 us: 1.12x faster                                                           |
| regex_dna                  | 126 ms                                                      | 114 ms: 1.11x faster                                                           |
| sqlite_synth               | 1.76 us                                                     | 1.66 us: 1.06x faster                                                          |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                           |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                          |
| pathlib                    | 80.5 ms                                                     | 79.7 ms: 1.01x faster                                                          |
| dulwich_log                | 44.3 ms                                                     | 44.7 ms: 1.01x slower                                                          |
| xml_etree_parse            | 93.0 ms                                                     | 96.0 ms: 1.03x slower                                                          |
| comprehensions             | 14.1 us                                                     | 14.6 us: 1.03x slower                                                          |
| deepcopy_reduce            | 2.09 us                                                     | 2.19 us: 1.05x slower                                                          |
| sympy_sum                  | 91.5 ms                                                     | 95.9 ms: 1.05x slower                                                          |
| deepcopy_memo              | 23.7 us                                                     | 24.9 us: 1.05x slower                                                          |
| coroutines                 | 14.3 ms                                                     | 15.1 ms: 1.06x slower                                                          |
| regex_v8                   | 14.2 ms                                                     | 15.1 ms: 1.06x slower                                                          |
| json                       | 3.05 ms                                                     | 3.24 ms: 1.06x slower                                                          |
| docutils                   | 1.66 sec                                                    | 1.77 sec: 1.07x slower                                                         |
| xml_etree_iterparse        | 65.2 ms                                                     | 69.9 ms: 1.07x slower                                                          |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                                          |
| tornado_http               | 89.5 ms                                                     | 96.4 ms: 1.08x slower                                                          |
| float                      | 56.8 ms                                                     | 61.5 ms: 1.08x slower                                                          |
| python_startup_no_site     | 16.2 ms                                                     | 17.7 ms: 1.09x slower                                                          |
| sympy_str                  | 175 ms                                                      | 191 ms: 1.09x slower                                                           |
| meteor_contest             | 74.6 ms                                                     | 81.5 ms: 1.09x slower                                                          |
| sympy_integrate            | 13.0 ms                                                     | 14.4 ms: 1.11x slower                                                          |
| generators                 | 22.5 ms                                                     | 25.2 ms: 1.12x slower                                                          |
| mako                       | 7.09 ms                                                     | 8.02 ms: 1.13x slower                                                          |
| logging_format             | 6.72 us                                                     | 7.61 us: 1.13x slower                                                          |
| 2to3                       | 218 ms                                                      | 247 ms: 1.13x slower                                                           |
| logging_simple             | 6.28 us                                                     | 7.15 us: 1.14x slower                                                          |
| xml_etree_generate         | 55.8 ms                                                     | 63.6 ms: 1.14x slower                                                          |
| async_generators           | 239 ms                                                      | 273 ms: 1.14x slower                                                           |
| regex_compile              | 87.5 ms                                                     | 99.9 ms: 1.14x slower                                                          |
| sqlglot_normalize          | 187 ms                                                      | 214 ms: 1.14x slower                                                           |
| raytrace                   | 192 ms                                                      | 220 ms: 1.15x slower                                                           |
| sympy_expand               | 284 ms                                                      | 329 ms: 1.16x slower                                                           |
| nqueens                    | 62.8 ms                                                     | 73.3 ms: 1.17x slower                                                          |
| sqlglot_optimize           | 34.5 ms                                                     | 40.3 ms: 1.17x slower                                                          |
| pycparser                  | 699 ms                                                      | 820 ms: 1.17x slower                                                           |
| logging_silent             | 60.5 ns                                                     | 71.3 ns: 1.18x slower                                                          |
| crypto_pyaes               | 48.5 ms                                                     | 57.4 ms: 1.18x slower                                                          |
| mdp                        | 1.37 sec                                                    | 1.64 sec: 1.19x slower                                                         |
| pprint_pformat             | 1.05 sec                                                    | 1.25 sec: 1.19x slower                                                         |
| pprint_safe_repr           | 513 ms                                                      | 614 ms: 1.20x slower                                                           |
| coverage                   | 40.8 ms                                                     | 48.8 ms: 1.20x slower                                                          |
| go                         | 91.6 ms                                                     | 110 ms: 1.20x slower                                                           |
| chaos                      | 43.3 ms                                                     | 52.0 ms: 1.20x slower                                                          |
| deltablue                  | 2.16 ms                                                     | 2.60 ms: 1.20x slower                                                          |
| spectral_norm              | 66.9 ms                                                     | 80.7 ms: 1.21x slower                                                          |
| bench_mp_pool              | 69.2 ms                                                     | 84.0 ms: 1.21x slower                                                          |
| pyflate                    | 295 ms                                                      | 358 ms: 1.21x slower                                                           |
| xml_etree_process          | 37.7 ms                                                     | 45.9 ms: 1.22x slower                                                          |
| sqlglot_transpile          | 1.02 ms                                                     | 1.25 ms: 1.22x slower                                                          |
| scimark_fft                | 184 ms                                                      | 226 ms: 1.22x slower                                                           |
| python_startup             | 19.5 ms                                                     | 24.1 ms: 1.24x slower                                                          |
| django_template            | 22.9 ms                                                     | 28.4 ms: 1.24x slower                                                          |
| nbody                      | 71.9 ms                                                     | 89.4 ms: 1.24x slower                                                          |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.18 ms: 1.25x slower                                                          |
| scimark_monte_carlo        | 43.7 ms                                                     | 54.7 ms: 1.25x slower                                                          |
| json_dumps                 | 5.70 ms                                                     | 7.13 ms: 1.25x slower                                                          |
| telco                      | 4.13 ms                                                     | 5.17 ms: 1.25x slower                                                          |
| hexiom                     | 4.10 ms                                                     | 5.14 ms: 1.25x slower                                                          |
| gc_traversal               | 1.52 ms                                                     | 1.92 ms: 1.26x slower                                                          |
| scimark_lu                 | 58.9 ms                                                     | 74.6 ms: 1.27x slower                                                          |
| sqlglot_parse              | 804 us                                                      | 1.02 ms: 1.27x slower                                                          |
| pickle_pure_python         | 195 us                                                      | 249 us: 1.28x slower                                                           |
| richards_super             | 32.1 ms                                                     | 41.4 ms: 1.29x slower                                                          |
| tomli_loads                | 1.37 sec                                                    | 1.77 sec: 1.29x slower                                                         |
| richards                   | 28.4 ms                                                     | 36.9 ms: 1.30x slower                                                          |
| scimark_sor                | 78.8 ms                                                     | 103 ms: 1.31x slower                                                           |
| typing_runtime_protocols   | 95.1 us                                                     | 126 us: 1.33x slower                                                           |
| fannkuch                   | 247 ms                                                      | 330 ms: 1.34x slower                                                           |
| unpickle_pure_python       | 133 us                                                      | 183 us: 1.38x slower                                                           |
| create_gc_cycles           | 752 us                                                      | 1.37 ms: 1.83x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.12x slower                                                                   |

Benchmark hidden because not significant (1): bench_thread_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241029-3.14.0a1+-f03f745/bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.104x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown