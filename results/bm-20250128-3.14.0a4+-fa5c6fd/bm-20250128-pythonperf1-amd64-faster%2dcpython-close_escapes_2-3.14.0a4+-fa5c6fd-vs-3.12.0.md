# Results vs. 3.12.0

- fork: faster-cpython
- ref: close_escapes_2
- machine: windows-amd64
- commit hash: fa5c6fd
- commit date: 2025-01-28
- overall geometric mean: 1.002x slower
- HPT reliability: 97.85%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 231 ms: 1.06x slower                                                             |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                           |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 422 ms: 1.83x faster                                                             |
| async_tree_io              | 731 ms                                                      | 432 ms: 1.69x faster                                                             |
| async_tree_memoization_tg  | 367 ms                                                      | 221 ms: 1.66x faster                                                             |
| async_tree_none_tg         | 285 ms                                                      | 187 ms: 1.53x faster                                                             |
| async_tree_none            | 291 ms                                                      | 195 ms: 1.49x faster                                                             |
| async_tree_memoization     | 339 ms                                                      | 228 ms: 1.49x faster                                                             |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.45x faster                                                             |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 347 ms: 1.41x faster                                                             |
| Geometric mean             | (ref)                                                       | 1.56x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 51.9 ms: 1.09x faster                                                            |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                             |
| nbody          | 71.9 ms                                                     | 78.2 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                            |
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                             |
| regex_compile  | 87.5 ms                                                     | 89.3 ms: 1.02x slower                                                            |
| regex_v8       | 14.2 ms                                                     | 16.3 ms: 1.15x slower                                                            |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.0 ms: 1.06x faster                                                            |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.1 ms: 1.02x faster                                                            |
| xml_etree_generate   | 55.8 ms                                                     | 58.5 ms: 1.05x slower                                                            |
| tomli_loads          | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                           |
| xml_etree_process    | 37.7 ms                                                     | 41.4 ms: 1.10x slower                                                            |
| json_loads           | 13.9 us                                                     | 15.4 us: 1.11x slower                                                            |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.16x slower                                                             |
| json_dumps           | 5.70 ms                                                     | 6.77 ms: 1.19x slower                                                            |
| pickle_pure_python   | 195 us                                                      | 236 us: 1.21x slower                                                             |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.1 ms: 1.12x slower                                                            |
| python_startup         | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                            |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.77 ms: 1.05x faster                                                            |
| django_template | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                            |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 422 ms: 1.83x faster                                                             |
| async_tree_io              | 731 ms                                                      | 432 ms: 1.69x faster                                                             |
| async_tree_memoization_tg  | 367 ms                                                      | 221 ms: 1.66x faster                                                             |
| async_tree_none_tg         | 285 ms                                                      | 187 ms: 1.53x faster                                                             |
| async_tree_none            | 291 ms                                                      | 195 ms: 1.49x faster                                                             |
| async_tree_memoization     | 339 ms                                                      | 228 ms: 1.49x faster                                                             |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.45x faster                                                             |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 347 ms: 1.41x faster                                                             |
| deepcopy                   | 238 us                                                      | 185 us: 1.29x faster                                                             |
| deepcopy_memo              | 23.7 us                                                     | 20.8 us: 1.14x faster                                                            |
| deepcopy_reduce            | 2.09 us                                                     | 1.86 us: 1.12x faster                                                            |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                            |
| float                      | 56.8 ms                                                     | 51.9 ms: 1.09x faster                                                            |
| regex_effbot               | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                            |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                             |
| comprehensions             | 14.1 us                                                     | 13.0 us: 1.08x faster                                                            |
| generators                 | 22.5 ms                                                     | 21.0 ms: 1.07x faster                                                            |
| async_generators           | 239 ms                                                      | 226 ms: 1.06x faster                                                             |
| xml_etree_parse            | 93.0 ms                                                     | 88.0 ms: 1.06x faster                                                            |
| mako                       | 7.09 ms                                                     | 6.77 ms: 1.05x faster                                                            |
| sympy_sum                  | 91.5 ms                                                     | 88.0 ms: 1.04x faster                                                            |
| dulwich_log                | 44.3 ms                                                     | 42.7 ms: 1.04x faster                                                            |
| pathlib                    | 80.5 ms                                                     | 78.0 ms: 1.03x faster                                                            |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                             |
| bench_thread_pool          | 857 us                                                      | 836 us: 1.03x faster                                                             |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.1 ms: 1.02x faster                                                            |
| spectral_norm              | 66.9 ms                                                     | 66.2 ms: 1.01x faster                                                            |
| crypto_pyaes               | 48.5 ms                                                     | 48.6 ms: 1.00x slower                                                            |
| chaos                      | 43.3 ms                                                     | 43.5 ms: 1.00x slower                                                            |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                             |
| meteor_contest             | 74.6 ms                                                     | 75.4 ms: 1.01x slower                                                            |
| logging_format             | 6.72 us                                                     | 6.82 us: 1.02x slower                                                            |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                           |
| regex_compile              | 87.5 ms                                                     | 89.3 ms: 1.02x slower                                                            |
| logging_simple             | 6.28 us                                                     | 6.41 us: 1.02x slower                                                            |
| go                         | 91.6 ms                                                     | 93.6 ms: 1.02x slower                                                            |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                            |
| coroutines                 | 14.3 ms                                                     | 14.7 ms: 1.03x slower                                                            |
| scimark_fft                | 184 ms                                                      | 191 ms: 1.04x slower                                                             |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.05x slower                                                           |
| xml_etree_generate         | 55.8 ms                                                     | 58.5 ms: 1.05x slower                                                            |
| sympy_expand               | 284 ms                                                      | 299 ms: 1.05x slower                                                             |
| nqueens                    | 62.8 ms                                                     | 66.1 ms: 1.05x slower                                                            |
| pycparser                  | 699 ms                                                      | 737 ms: 1.05x slower                                                             |
| 2to3                       | 218 ms                                                      | 231 ms: 1.06x slower                                                             |
| tomli_loads                | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                           |
| sqlglot_optimize           | 34.5 ms                                                     | 36.6 ms: 1.06x slower                                                            |
| sqlglot_transpile          | 1.02 ms                                                     | 1.09 ms: 1.06x slower                                                            |
| sqlglot_normalize          | 187 ms                                                      | 200 ms: 1.07x slower                                                             |
| raytrace                   | 192 ms                                                      | 206 ms: 1.07x slower                                                             |
| pyflate                    | 295 ms                                                      | 316 ms: 1.07x slower                                                             |
| pprint_safe_repr           | 513 ms                                                      | 551 ms: 1.07x slower                                                             |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.76 ms: 1.08x slower                                                            |
| nbody                      | 71.9 ms                                                     | 78.2 ms: 1.09x slower                                                            |
| sqlglot_parse              | 804 us                                                      | 882 us: 1.10x slower                                                             |
| xml_etree_process          | 37.7 ms                                                     | 41.4 ms: 1.10x slower                                                            |
| mdp                        | 1.37 sec                                                    | 1.51 sec: 1.10x slower                                                           |
| json_loads                 | 13.9 us                                                     | 15.4 us: 1.11x slower                                                            |
| scimark_monte_carlo        | 43.7 ms                                                     | 48.8 ms: 1.12x slower                                                            |
| python_startup_no_site     | 16.2 ms                                                     | 18.1 ms: 1.12x slower                                                            |
| django_template            | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                            |
| regex_v8                   | 14.2 ms                                                     | 16.3 ms: 1.15x slower                                                            |
| deltablue                  | 2.16 ms                                                     | 2.48 ms: 1.15x slower                                                            |
| logging_silent             | 60.5 ns                                                     | 69.9 ns: 1.16x slower                                                            |
| telco                      | 4.13 ms                                                     | 4.79 ms: 1.16x slower                                                            |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.16x slower                                                             |
| richards_super             | 32.1 ms                                                     | 37.4 ms: 1.16x slower                                                            |
| hexiom                     | 4.10 ms                                                     | 4.79 ms: 1.17x slower                                                            |
| richards                   | 28.4 ms                                                     | 33.1 ms: 1.17x slower                                                            |
| fannkuch                   | 247 ms                                                      | 289 ms: 1.17x slower                                                             |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.17x slower                                                             |
| json_dumps                 | 5.70 ms                                                     | 6.77 ms: 1.19x slower                                                            |
| scimark_sor                | 78.8 ms                                                     | 94.7 ms: 1.20x slower                                                            |
| pickle_pure_python         | 195 us                                                      | 236 us: 1.21x slower                                                             |
| coverage                   | 40.8 ms                                                     | 49.3 ms: 1.21x slower                                                            |
| scimark_lu                 | 58.9 ms                                                     | 71.5 ms: 1.21x slower                                                            |
| python_startup             | 19.5 ms                                                     | 24.3 ms: 1.25x slower                                                            |
| bench_mp_pool              | 69.2 ms                                                     | 88.5 ms: 1.28x slower                                                            |
| gc_traversal               | 1.52 ms                                                     | 1.99 ms: 1.30x slower                                                            |
| create_gc_cycles           | 752 us                                                      | 1.21 ms: 1.61x slower                                                            |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): json
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250128-3.14.0a4+-fa5c6fd/bm-20250128-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 97.85% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown