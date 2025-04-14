# Results vs. 3.12.0

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: windows-amd64
- commit hash: 8aa20f2
- commit date: 2025-04-09
- overall geometric mean: 1.107x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 217 ms: 1.01x faster                                                                 |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                               |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 393 ms: 1.96x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 406 ms: 1.80x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 203 ms: 1.67x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 177 ms: 1.65x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 336 ms: 1.49x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 41.9 ms: 1.36x faster                                                                |
| nbody          | 71.9 ms                                                     | 61.8 ms: 1.16x faster                                                                |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.2 ms: 1.10x faster                                                                |
| regex_effbot   | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                                |
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                                 |
| regex_v8       | 14.2 ms                                                     | 13.8 ms: 1.03x faster                                                                |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.5 ms: 1.04x faster                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                               |
| unpickle_pure_python | 133 us                                                      | 131 us: 1.01x faster                                                                 |
| xml_etree_process    | 37.7 ms                                                     | 39.3 ms: 1.04x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 207 us: 1.06x slower                                                                 |
| json_loads           | 13.9 us                                                     | 15.2 us: 1.09x slower                                                                |
| json_dumps           | 5.70 ms                                                     | 6.81 ms: 1.20x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                         |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                                |
| python_startup         | 19.5 ms                                                     | 25.0 ms: 1.28x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.50 ms: 1.09x faster                                                                |
| django_template | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 28.5 ms: 2.83x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 393 ms: 1.96x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 406 ms: 1.80x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 207 ms: 1.77x faster                                                                 |
| mdp                        | 1.37 sec                                                    | 797 ms: 1.72x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 168 ms: 1.70x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 203 ms: 1.67x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 177 ms: 1.65x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 336 ms: 1.49x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                                 |
| deepcopy                   | 238 us                                                      | 171 us: 1.39x faster                                                                 |
| float                      | 56.8 ms                                                     | 41.9 ms: 1.36x faster                                                                |
| deepcopy_memo              | 23.7 us                                                     | 17.8 us: 1.33x faster                                                                |
| comprehensions             | 14.1 us                                                     | 11.3 us: 1.25x faster                                                                |
| go                         | 91.6 ms                                                     | 75.5 ms: 1.21x faster                                                                |
| generators                 | 22.5 ms                                                     | 18.8 ms: 1.20x faster                                                                |
| nbody                      | 71.9 ms                                                     | 61.8 ms: 1.16x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.81 us: 1.16x faster                                                                |
| spectral_norm              | 66.9 ms                                                     | 58.0 ms: 1.15x faster                                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.1 ms: 1.15x faster                                                                |
| chaos                      | 43.3 ms                                                     | 37.8 ms: 1.15x faster                                                                |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                                |
| logging_silent             | 60.5 ns                                                     | 54.5 ns: 1.11x faster                                                                |
| raytrace                   | 192 ms                                                      | 174 ms: 1.11x faster                                                                 |
| regex_compile              | 87.5 ms                                                     | 79.2 ms: 1.10x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                                |
| mako                       | 7.09 ms                                                     | 6.50 ms: 1.09x faster                                                                |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                                 |
| dulwich_log                | 44.3 ms                                                     | 41.0 ms: 1.08x faster                                                                |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                                                |
| scimark_sor                | 78.8 ms                                                     | 73.8 ms: 1.07x faster                                                                |
| richards                   | 28.4 ms                                                     | 26.7 ms: 1.06x faster                                                                |
| async_generators           | 239 ms                                                      | 226 ms: 1.06x faster                                                                 |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                                                |
| pprint_safe_repr           | 513 ms                                                      | 490 ms: 1.05x faster                                                                 |
| logging_simple             | 6.28 us                                                     | 6.01 us: 1.04x faster                                                                |
| xml_etree_parse            | 93.0 ms                                                     | 89.5 ms: 1.04x faster                                                                |
| nqueens                    | 62.8 ms                                                     | 60.6 ms: 1.04x faster                                                                |
| pprint_pformat             | 1.05 sec                                                    | 1.01 sec: 1.04x faster                                                               |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.0 ms: 1.03x faster                                                                |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.03x faster                                                                |
| scimark_fft                | 184 ms                                                      | 179 ms: 1.03x faster                                                                 |
| meteor_contest             | 74.6 ms                                                     | 72.3 ms: 1.03x faster                                                                |
| logging_format             | 6.72 us                                                     | 6.51 us: 1.03x faster                                                                |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                                 |
| sympy_sum                  | 91.5 ms                                                     | 88.8 ms: 1.03x faster                                                                |
| regex_v8                   | 14.2 ms                                                     | 13.8 ms: 1.03x faster                                                                |
| hexiom                     | 4.10 ms                                                     | 3.98 ms: 1.03x faster                                                                |
| scimark_lu                 | 58.9 ms                                                     | 57.4 ms: 1.03x faster                                                                |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.03x faster                                                                 |
| deltablue                  | 2.16 ms                                                     | 2.11 ms: 1.03x faster                                                                |
| pyflate                    | 295 ms                                                      | 288 ms: 1.02x faster                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.34 sec: 1.02x faster                                                               |
| crypto_pyaes               | 48.5 ms                                                     | 47.6 ms: 1.02x faster                                                                |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                               |
| unpickle_pure_python       | 133 us                                                      | 131 us: 1.01x faster                                                                 |
| 2to3                       | 218 ms                                                      | 217 ms: 1.01x faster                                                                 |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.55 ms: 1.00x faster                                                                |
| fannkuch                   | 247 ms                                                      | 248 ms: 1.01x slower                                                                 |
| sympy_expand               | 284 ms                                                      | 291 ms: 1.02x slower                                                                 |
| json                       | 3.05 ms                                                     | 3.16 ms: 1.04x slower                                                                |
| xml_etree_process          | 37.7 ms                                                     | 39.3 ms: 1.04x slower                                                                |
| django_template            | 22.9 ms                                                     | 24.0 ms: 1.05x slower                                                                |
| pickle_pure_python         | 195 us                                                      | 207 us: 1.06x slower                                                                 |
| json_loads                 | 13.9 us                                                     | 15.2 us: 1.09x slower                                                                |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.12x slower                                                                 |
| telco                      | 4.13 ms                                                     | 4.64 ms: 1.12x slower                                                                |
| json_dumps                 | 5.70 ms                                                     | 6.81 ms: 1.20x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 19.5 ms: 1.20x slower                                                                |
| coverage                   | 40.8 ms                                                     | 49.8 ms: 1.22x slower                                                                |
| bench_mp_pool              | 69.2 ms                                                     | 86.4 ms: 1.25x slower                                                                |
| python_startup             | 19.5 ms                                                     | 25.0 ms: 1.28x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 2.10 ms: 1.38x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 1.23 ms: 1.64x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                                         |

Benchmark hidden because not significant (3): bench_thread_pool, xml_etree_generate, pycparser
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250409-3.14.0a7+-8aa20f2/bm-20250409-pythonperf1-amd64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.107x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown