# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_stackref_macros
- machine: windows-amd64
- commit hash: 17b97c6
- commit date: 2025-02-27
- overall geometric mean: 1.034x faster
- HPT reliability: 75.75%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                               |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 412 ms: 1.87x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 420 ms: 1.74x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 180 ms: 1.58x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.53x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 223 ms: 1.52x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 341 ms: 1.44x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.60x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.8 ms: 1.21x faster                                                                |
| nbody          | 71.9 ms                                                     | 65.5 ms: 1.10x faster                                                                |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.41 ms: 1.15x faster                                                                |
| regex_dna      | 126 ms                                                      | 112 ms: 1.13x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                         |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.8 ms: 1.04x faster                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.3 ms: 1.03x faster                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 57.6 ms: 1.03x slower                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                               |
| json_loads           | 13.9 us                                                     | 15.0 us: 1.08x slower                                                                |
| xml_etree_process    | 37.7 ms                                                     | 41.1 ms: 1.09x slower                                                                |
| unpickle_pure_python | 133 us                                                      | 151 us: 1.13x slower                                                                 |
| pickle_pure_python   | 195 us                                                      | 230 us: 1.18x slower                                                                 |
| json_dumps           | 5.70 ms                                                     | 6.87 ms: 1.21x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                                |
| python_startup         | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 26.2 ms: 1.14x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                                         |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.1 ms: 2.50x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 412 ms: 1.87x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 420 ms: 1.74x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 180 ms: 1.58x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 190 ms: 1.53x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 223 ms: 1.52x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 344 ms: 1.46x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 341 ms: 1.44x faster                                                                 |
| deepcopy                   | 238 us                                                      | 184 us: 1.29x faster                                                                 |
| deepcopy_memo              | 23.7 us                                                     | 19.1 us: 1.24x faster                                                                |
| float                      | 56.8 ms                                                     | 46.8 ms: 1.21x faster                                                                |
| spectral_norm              | 66.9 ms                                                     | 56.7 ms: 1.18x faster                                                                |
| comprehensions             | 14.1 us                                                     | 12.1 us: 1.17x faster                                                                |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.41 ms: 1.15x faster                                                                |
| regex_dna                  | 126 ms                                                      | 112 ms: 1.13x faster                                                                 |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                                |
| nbody                      | 71.9 ms                                                     | 65.5 ms: 1.10x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.95 us: 1.08x faster                                                                |
| async_generators           | 239 ms                                                      | 229 ms: 1.05x faster                                                                 |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.46 ms: 1.04x faster                                                                |
| xml_etree_parse            | 93.0 ms                                                     | 89.8 ms: 1.04x faster                                                                |
| coroutines                 | 14.3 ms                                                     | 13.8 ms: 1.03x faster                                                                |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.3 ms: 1.03x faster                                                                |
| go                         | 91.6 ms                                                     | 89.3 ms: 1.03x faster                                                                |
| dulwich_log                | 44.3 ms                                                     | 43.4 ms: 1.02x faster                                                                |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                                 |
| logging_silent             | 60.5 ns                                                     | 59.7 ns: 1.01x faster                                                                |
| sympy_sum                  | 91.5 ms                                                     | 90.5 ms: 1.01x faster                                                                |
| json                       | 3.05 ms                                                     | 3.02 ms: 1.01x faster                                                                |
| scimark_fft                | 184 ms                                                      | 184 ms: 1.00x faster                                                                 |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.0 ms: 1.01x slower                                                                |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                                 |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                               |
| scimark_lu                 | 58.9 ms                                                     | 59.9 ms: 1.02x slower                                                                |
| chaos                      | 43.3 ms                                                     | 44.1 ms: 1.02x slower                                                                |
| scimark_sor                | 78.8 ms                                                     | 80.5 ms: 1.02x slower                                                                |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                                |
| meteor_contest             | 74.6 ms                                                     | 76.9 ms: 1.03x slower                                                                |
| xml_etree_generate         | 55.8 ms                                                     | 57.6 ms: 1.03x slower                                                                |
| logging_format             | 6.72 us                                                     | 6.95 us: 1.03x slower                                                                |
| nqueens                    | 62.8 ms                                                     | 65.0 ms: 1.04x slower                                                                |
| logging_simple             | 6.28 us                                                     | 6.50 us: 1.04x slower                                                                |
| pyflate                    | 295 ms                                                      | 306 ms: 1.04x slower                                                                 |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                               |
| sqlglot_normalize          | 187 ms                                                      | 196 ms: 1.05x slower                                                                 |
| sqlglot_optimize           | 34.5 ms                                                     | 36.2 ms: 1.05x slower                                                                |
| pprint_pformat             | 1.05 sec                                                    | 1.10 sec: 1.05x slower                                                               |
| crypto_pyaes               | 48.5 ms                                                     | 51.3 ms: 1.06x slower                                                                |
| raytrace                   | 192 ms                                                      | 204 ms: 1.06x slower                                                                 |
| richards_super             | 32.1 ms                                                     | 34.1 ms: 1.06x slower                                                                |
| pprint_safe_repr           | 513 ms                                                      | 546 ms: 1.06x slower                                                                 |
| richards                   | 28.4 ms                                                     | 30.2 ms: 1.06x slower                                                                |
| pycparser                  | 699 ms                                                      | 744 ms: 1.07x slower                                                                 |
| deltablue                  | 2.16 ms                                                     | 2.31 ms: 1.07x slower                                                                |
| hexiom                     | 4.10 ms                                                     | 4.38 ms: 1.07x slower                                                                |
| sympy_expand               | 284 ms                                                      | 305 ms: 1.08x slower                                                                 |
| json_loads                 | 13.9 us                                                     | 15.0 us: 1.08x slower                                                                |
| xml_etree_process          | 37.7 ms                                                     | 41.1 ms: 1.09x slower                                                                |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.09x slower                                                               |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.10x slower                                                                |
| fannkuch                   | 247 ms                                                      | 273 ms: 1.11x slower                                                                 |
| unpickle_pure_python       | 133 us                                                      | 151 us: 1.13x slower                                                                 |
| sqlglot_parse              | 804 us                                                      | 910 us: 1.13x slower                                                                 |
| django_template            | 22.9 ms                                                     | 26.2 ms: 1.14x slower                                                                |
| typing_runtime_protocols   | 95.1 us                                                     | 109 us: 1.14x slower                                                                 |
| coverage                   | 40.8 ms                                                     | 47.6 ms: 1.17x slower                                                                |
| pickle_pure_python         | 195 us                                                      | 230 us: 1.18x slower                                                                 |
| telco                      | 4.13 ms                                                     | 4.88 ms: 1.18x slower                                                                |
| json_dumps                 | 5.70 ms                                                     | 6.87 ms: 1.21x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 19.7 ms: 1.21x slower                                                                |
| bench_mp_pool              | 69.2 ms                                                     | 86.6 ms: 1.25x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 1.99 ms: 1.31x slower                                                                |
| python_startup             | 19.5 ms                                                     | 26.1 ms: 1.34x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 1.23 ms: 1.64x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                         |

Benchmark hidden because not significant (4): regex_compile, mako, regex_v8, bench_thread_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250227-3.14.0a5+-17b97c6/bm-20250227-pythonperf1-amd64-faster%2dcpython-use_stackref_macros-3.14.0a5+-17b97c6.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 75.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown