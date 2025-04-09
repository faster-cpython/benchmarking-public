# Results vs. 3.12.0

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: windows-amd64
- commit hash: 3514aa1
- commit date: 2025-04-09
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 394 ms: 1.96x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 409 ms: 1.79x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.69x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 203 ms: 1.67x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 178 ms: 1.63x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 336 ms: 1.49x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 42.2 ms: 1.35x faster                                                                |
| nbody          | 71.9 ms                                                     | 61.3 ms: 1.17x faster                                                                |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.5 ms: 1.11x faster                                                                |
| regex_effbot   | 1.62 ms                                                     | 1.45 ms: 1.11x faster                                                                |
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 90.0 ms: 1.03x faster                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 54.8 ms: 1.02x faster                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.4 ms: 1.01x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                               |
| unpickle_pure_python | 133 us                                                      | 132 us: 1.01x faster                                                                 |
| xml_etree_process    | 37.7 ms                                                     | 38.8 ms: 1.03x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 208 us: 1.07x slower                                                                 |
| json_loads           | 13.9 us                                                     | 14.9 us: 1.07x slower                                                                |
| json_dumps           | 5.70 ms                                                     | 6.73 ms: 1.18x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                                |
| python_startup         | 19.5 ms                                                     | 25.3 ms: 1.30x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.65 ms: 1.07x faster                                                                |
| django_template | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.4 ms: 2.83x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 394 ms: 1.96x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 409 ms: 1.79x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                                 |
| mdp                        | 1.37 sec                                                    | 782 ms: 1.75x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.69x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 203 ms: 1.67x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 178 ms: 1.63x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 336 ms: 1.49x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 329 ms: 1.49x faster                                                                 |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                                 |
| float                      | 56.8 ms                                                     | 42.2 ms: 1.35x faster                                                                |
| deepcopy_memo              | 23.7 us                                                     | 18.2 us: 1.30x faster                                                                |
| spectral_norm              | 66.9 ms                                                     | 53.7 ms: 1.25x faster                                                                |
| comprehensions             | 14.1 us                                                     | 11.5 us: 1.23x faster                                                                |
| go                         | 91.6 ms                                                     | 75.8 ms: 1.21x faster                                                                |
| generators                 | 22.5 ms                                                     | 19.0 ms: 1.19x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.77 us: 1.18x faster                                                                |
| nbody                      | 71.9 ms                                                     | 61.3 ms: 1.17x faster                                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.8 ms: 1.16x faster                                                                |
| chaos                      | 43.3 ms                                                     | 37.4 ms: 1.16x faster                                                                |
| logging_silent             | 60.5 ns                                                     | 54.2 ns: 1.12x faster                                                                |
| regex_compile              | 87.5 ms                                                     | 78.5 ms: 1.11x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.45 ms: 1.11x faster                                                                |
| raytrace                   | 192 ms                                                      | 173 ms: 1.11x faster                                                                 |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                                |
| dulwich_log                | 44.3 ms                                                     | 40.5 ms: 1.09x faster                                                                |
| scimark_fft                | 184 ms                                                      | 169 ms: 1.09x faster                                                                 |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                                 |
| scimark_sor                | 78.8 ms                                                     | 72.7 ms: 1.08x faster                                                                |
| mako                       | 7.09 ms                                                     | 6.65 ms: 1.07x faster                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.41 ms: 1.06x faster                                                                |
| richards                   | 28.4 ms                                                     | 26.7 ms: 1.06x faster                                                                |
| nqueens                    | 62.8 ms                                                     | 59.3 ms: 1.06x faster                                                                |
| async_generators           | 239 ms                                                      | 227 ms: 1.05x faster                                                                 |
| hexiom                     | 4.10 ms                                                     | 3.90 ms: 1.05x faster                                                                |
| sympy_sum                  | 91.5 ms                                                     | 87.2 ms: 1.05x faster                                                                |
| richards_super             | 32.1 ms                                                     | 30.6 ms: 1.05x faster                                                                |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.05x faster                                                                |
| pprint_safe_repr           | 513 ms                                                      | 493 ms: 1.04x faster                                                                 |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.04x faster                                                                 |
| crypto_pyaes               | 48.5 ms                                                     | 46.8 ms: 1.04x faster                                                                |
| scimark_lu                 | 58.9 ms                                                     | 56.8 ms: 1.04x faster                                                                |
| pprint_pformat             | 1.05 sec                                                    | 1.01 sec: 1.03x faster                                                               |
| xml_etree_parse            | 93.0 ms                                                     | 90.0 ms: 1.03x faster                                                                |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                                 |
| meteor_contest             | 74.6 ms                                                     | 72.5 ms: 1.03x faster                                                                |
| logging_simple             | 6.28 us                                                     | 6.12 us: 1.03x faster                                                                |
| deltablue                  | 2.16 ms                                                     | 2.11 ms: 1.03x faster                                                                |
| pyflate                    | 295 ms                                                      | 287 ms: 1.03x faster                                                                 |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.02x faster                                                                |
| xml_etree_generate         | 55.8 ms                                                     | 54.8 ms: 1.02x faster                                                                |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.4 ms: 1.01x faster                                                                |
| logging_format             | 6.72 us                                                     | 6.64 us: 1.01x faster                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                               |
| unpickle_pure_python       | 133 us                                                      | 132 us: 1.01x faster                                                                 |
| pycparser                  | 699 ms                                                      | 705 ms: 1.01x slower                                                                 |
| sympy_expand               | 284 ms                                                      | 289 ms: 1.02x slower                                                                 |
| fannkuch                   | 247 ms                                                      | 254 ms: 1.03x slower                                                                 |
| xml_etree_process          | 37.7 ms                                                     | 38.8 ms: 1.03x slower                                                                |
| json                       | 3.05 ms                                                     | 3.15 ms: 1.03x slower                                                                |
| django_template            | 22.9 ms                                                     | 23.9 ms: 1.04x slower                                                                |
| pickle_pure_python         | 195 us                                                      | 208 us: 1.07x slower                                                                 |
| json_loads                 | 13.9 us                                                     | 14.9 us: 1.07x slower                                                                |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.10x slower                                                                 |
| telco                      | 4.13 ms                                                     | 4.61 ms: 1.12x slower                                                                |
| json_dumps                 | 5.70 ms                                                     | 6.73 ms: 1.18x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                                |
| bench_mp_pool              | 69.2 ms                                                     | 86.8 ms: 1.25x slower                                                                |
| coverage                   | 40.8 ms                                                     | 51.3 ms: 1.26x slower                                                                |
| python_startup             | 19.5 ms                                                     | 25.3 ms: 1.30x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 2.10 ms: 1.38x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 1.23 ms: 1.63x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                                         |

Benchmark hidden because not significant (4): bench_thread_pool, docutils, 2to3, regex_v8
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250409-3.14.0a7+-3514aa1/bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-3514aa1.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown