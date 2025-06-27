# Results vs. 3.12.0

- fork: faster-cpython
- ref: never_inline_decref
- machine: windows-amd64
- commit hash: 2ab3a06
- commit date: 2025-06-27
- overall geometric mean: 1.084x faster
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                                |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                              |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 393 ms: 1.96x faster                                                                |
| async_tree_io              | 731 ms                                                      | 399 ms: 1.83x faster                                                                |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                                |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.69x faster                                                                |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                                |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                                |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 326 ms: 1.50x faster                                                                |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 339 ms: 1.48x faster                                                                |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.9 ms: 1.29x faster                                                               |
| nbody          | 71.9 ms                                                     | 65.2 ms: 1.10x faster                                                               |
| pidigits       | 152 ms                                                      | 146 ms: 1.04x faster                                                                |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 81.8 ms: 1.07x faster                                                               |
| regex_dna      | 126 ms                                                      | 119 ms: 1.07x faster                                                                |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                               |
| regex_v8       | 14.2 ms                                                     | 13.7 ms: 1.04x faster                                                               |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 92.1 ms: 1.01x faster                                                               |
| unpickle_pure_python | 133 us                                                      | 135 us: 1.01x slower                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                               |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                               |
| xml_etree_process    | 37.7 ms                                                     | 39.4 ms: 1.05x slower                                                               |
| tomli_loads          | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                              |
| pickle_pure_python   | 195 us                                                      | 211 us: 1.08x slower                                                                |
| json_dumps           | 5.70 ms                                                     | 6.43 ms: 1.13x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                                        |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                               |
| python_startup         | 19.5 ms                                                     | 25.5 ms: 1.31x slower                                                               |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.76 ms: 1.05x faster                                                               |
| django_template | 22.9 ms                                                     | 23.6 ms: 1.03x slower                                                               |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.8 ms: 2.53x faster                                                               |
| async_tree_io_tg           | 771 ms                                                      | 393 ms: 1.96x faster                                                                |
| async_tree_io              | 731 ms                                                      | 399 ms: 1.83x faster                                                                |
| async_tree_memoization_tg  | 367 ms                                                      | 212 ms: 1.73x faster                                                                |
| mdp                        | 1.37 sec                                                    | 807 ms: 1.70x faster                                                                |
| async_tree_none            | 291 ms                                                      | 173 ms: 1.69x faster                                                                |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.67x faster                                                                |
| async_tree_memoization     | 339 ms                                                      | 209 ms: 1.62x faster                                                                |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 326 ms: 1.50x faster                                                                |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 339 ms: 1.48x faster                                                                |
| deepcopy                   | 238 us                                                      | 172 us: 1.39x faster                                                                |
| deepcopy_memo              | 23.7 us                                                     | 17.9 us: 1.32x faster                                                               |
| float                      | 56.8 ms                                                     | 43.9 ms: 1.29x faster                                                               |
| comprehensions             | 14.1 us                                                     | 11.1 us: 1.27x faster                                                               |
| go                         | 91.6 ms                                                     | 76.5 ms: 1.20x faster                                                               |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                               |
| deepcopy_reduce            | 2.09 us                                                     | 1.87 us: 1.12x faster                                                               |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                               |
| nbody                      | 71.9 ms                                                     | 65.2 ms: 1.10x faster                                                               |
| logging_silent             | 60.5 ns                                                     | 55.2 ns: 1.10x faster                                                               |
| raytrace                   | 192 ms                                                      | 177 ms: 1.09x faster                                                                |
| dulwich_log                | 44.3 ms                                                     | 41.1 ms: 1.08x faster                                                               |
| chaos                      | 43.3 ms                                                     | 40.4 ms: 1.07x faster                                                               |
| regex_compile              | 87.5 ms                                                     | 81.8 ms: 1.07x faster                                                               |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.0 ms: 1.07x faster                                                               |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.07x faster                                                                |
| richards                   | 28.4 ms                                                     | 26.8 ms: 1.06x faster                                                               |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                                               |
| mako                       | 7.09 ms                                                     | 6.76 ms: 1.05x faster                                                               |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                               |
| pidigits                   | 152 ms                                                      | 146 ms: 1.04x faster                                                                |
| sympy_sum                  | 91.5 ms                                                     | 87.8 ms: 1.04x faster                                                               |
| spectral_norm              | 66.9 ms                                                     | 64.3 ms: 1.04x faster                                                               |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                                               |
| regex_v8                   | 14.2 ms                                                     | 13.7 ms: 1.04x faster                                                               |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.04x faster                                                                |
| scimark_lu                 | 58.9 ms                                                     | 57.1 ms: 1.03x faster                                                               |
| scimark_sor                | 78.8 ms                                                     | 76.5 ms: 1.03x faster                                                               |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                              |
| logging_simple             | 6.28 us                                                     | 6.19 us: 1.01x faster                                                               |
| pprint_pformat             | 1.05 sec                                                    | 1.03 sec: 1.01x faster                                                              |
| crypto_pyaes               | 48.5 ms                                                     | 47.9 ms: 1.01x faster                                                               |
| xml_etree_parse            | 93.0 ms                                                     | 92.1 ms: 1.01x faster                                                               |
| meteor_contest             | 74.6 ms                                                     | 73.9 ms: 1.01x faster                                                               |
| pprint_safe_repr           | 513 ms                                                      | 509 ms: 1.01x faster                                                                |
| logging_format             | 6.72 us                                                     | 6.67 us: 1.01x faster                                                               |
| pycparser                  | 699 ms                                                      | 706 ms: 1.01x slower                                                                |
| unpickle_pure_python       | 133 us                                                      | 135 us: 1.01x slower                                                                |
| xml_etree_generate         | 55.8 ms                                                     | 56.5 ms: 1.01x slower                                                               |
| async_generators           | 239 ms                                                      | 243 ms: 1.01x slower                                                                |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                                |
| deltablue                  | 2.16 ms                                                     | 2.20 ms: 1.02x slower                                                               |
| hexiom                     | 4.10 ms                                                     | 4.18 ms: 1.02x slower                                                               |
| json                       | 3.05 ms                                                     | 3.11 ms: 1.02x slower                                                               |
| sympy_expand               | 284 ms                                                      | 290 ms: 1.02x slower                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.62 ms: 1.02x slower                                                               |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                               |
| django_template            | 22.9 ms                                                     | 23.6 ms: 1.03x slower                                                               |
| coroutines                 | 14.3 ms                                                     | 14.8 ms: 1.04x slower                                                               |
| xml_etree_process          | 37.7 ms                                                     | 39.4 ms: 1.05x slower                                                               |
| tomli_loads                | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                              |
| fannkuch                   | 247 ms                                                      | 261 ms: 1.06x slower                                                                |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.07x slower                                                                |
| pickle_pure_python         | 195 us                                                      | 211 us: 1.08x slower                                                                |
| json_dumps                 | 5.70 ms                                                     | 6.43 ms: 1.13x slower                                                               |
| telco                      | 4.13 ms                                                     | 4.73 ms: 1.15x slower                                                               |
| python_startup_no_site     | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                               |
| coverage                   | 40.8 ms                                                     | 52.3 ms: 1.28x slower                                                               |
| python_startup             | 19.5 ms                                                     | 25.5 ms: 1.31x slower                                                               |
| gc_traversal               | 1.52 ms                                                     | 2.18 ms: 1.43x slower                                                               |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                                               |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                                        |

Benchmark hidden because not significant (4): pyflate, scimark_fft, nqueens, xml_etree_iterparse
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250627-3.15.0a0-2ab3a06/bm-20250627-pythonperf1-amd64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.084x faster

# HPT report

- Reliability score: 99.79% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown