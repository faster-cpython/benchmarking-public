# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: c41d531
- commit date: 2025-06-16
- overall geometric mean: 1.055x faster
- HPT reliability: 99.77%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                               |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 400 ms: 1.83x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.69x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 326 ms: 1.50x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.48x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.6 ms: 1.24x faster                                                                |
| nbody          | 71.9 ms                                                     | 65.7 ms: 1.09x faster                                                                |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.51 ms: 1.07x faster                                                                |
| regex_compile  | 87.5 ms                                                     | 82.2 ms: 1.07x faster                                                                |
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                                 |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                                |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.1 ms: 1.04x faster                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.7 ms: 1.02x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                               |
| xml_etree_generate   | 55.8 ms                                                     | 57.2 ms: 1.02x slower                                                                |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                                |
| unpickle_pure_python | 133 us                                                      | 139 us: 1.04x slower                                                                 |
| xml_etree_process    | 37.7 ms                                                     | 39.4 ms: 1.04x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 215 us: 1.10x slower                                                                 |
| json_dumps           | 5.70 ms                                                     | 6.29 ms: 1.10x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                                |
| python_startup         | 19.5 ms                                                     | 25.6 ms: 1.32x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.67 ms: 1.06x faster                                                                |
| django_template | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.3 ms: 2.49x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 398 ms: 1.94x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 400 ms: 1.83x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 211 ms: 1.74x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 172 ms: 1.69x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                                 |
| mdp                        | 1.37 sec                                                    | 826 ms: 1.66x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 326 ms: 1.50x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 340 ms: 1.48x faster                                                                 |
| deepcopy                   | 238 us                                                      | 172 us: 1.38x faster                                                                 |
| comprehensions             | 14.1 us                                                     | 11.2 us: 1.26x faster                                                                |
| deepcopy_memo              | 23.7 us                                                     | 19.0 us: 1.25x faster                                                                |
| float                      | 56.8 ms                                                     | 45.6 ms: 1.24x faster                                                                |
| go                         | 91.6 ms                                                     | 77.3 ms: 1.18x faster                                                                |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                                |
| spectral_norm              | 66.9 ms                                                     | 59.4 ms: 1.13x faster                                                                |
| sqlite_synth               | 1.76 us                                                     | 1.57 us: 1.12x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.88 us: 1.12x faster                                                                |
| chaos                      | 43.3 ms                                                     | 39.0 ms: 1.11x faster                                                                |
| nbody                      | 71.9 ms                                                     | 65.7 ms: 1.09x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.51 ms: 1.07x faster                                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.9 ms: 1.07x faster                                                                |
| regex_compile              | 87.5 ms                                                     | 82.2 ms: 1.07x faster                                                                |
| mako                       | 7.09 ms                                                     | 6.67 ms: 1.06x faster                                                                |
| dulwich_log                | 44.3 ms                                                     | 41.7 ms: 1.06x faster                                                                |
| pyflate                    | 295 ms                                                      | 280 ms: 1.05x faster                                                                 |
| xml_etree_parse            | 93.0 ms                                                     | 89.1 ms: 1.04x faster                                                                |
| sympy_sum                  | 91.5 ms                                                     | 87.7 ms: 1.04x faster                                                                |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                                 |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                                                |
| raytrace                   | 192 ms                                                      | 186 ms: 1.03x faster                                                                 |
| sympy_str                  | 175 ms                                                      | 170 ms: 1.03x faster                                                                 |
| scimark_fft                | 184 ms                                                      | 179 ms: 1.03x faster                                                                 |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                                 |
| crypto_pyaes               | 48.5 ms                                                     | 47.3 ms: 1.03x faster                                                                |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.7 ms: 1.02x faster                                                                |
| async_generators           | 239 ms                                                      | 234 ms: 1.02x faster                                                                 |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                               |
| richards                   | 28.4 ms                                                     | 27.9 ms: 1.02x faster                                                                |
| json                       | 3.05 ms                                                     | 3.00 ms: 1.02x faster                                                                |
| coroutines                 | 14.3 ms                                                     | 14.0 ms: 1.02x faster                                                                |
| richards_super             | 32.1 ms                                                     | 31.7 ms: 1.01x faster                                                                |
| meteor_contest             | 74.6 ms                                                     | 74.3 ms: 1.00x faster                                                                |
| scimark_sor                | 78.8 ms                                                     | 79.1 ms: 1.00x slower                                                                |
| scimark_lu                 | 58.9 ms                                                     | 59.3 ms: 1.01x slower                                                                |
| logging_format             | 6.72 us                                                     | 6.78 us: 1.01x slower                                                                |
| hexiom                     | 4.10 ms                                                     | 4.14 ms: 1.01x slower                                                                |
| sympy_expand               | 284 ms                                                      | 287 ms: 1.01x slower                                                                 |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                               |
| xml_etree_generate         | 55.8 ms                                                     | 57.2 ms: 1.02x slower                                                                |
| pycparser                  | 699 ms                                                      | 716 ms: 1.02x slower                                                                 |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                                |
| deltablue                  | 2.16 ms                                                     | 2.23 ms: 1.03x slower                                                                |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.66 ms: 1.04x slower                                                                |
| unpickle_pure_python       | 133 us                                                      | 139 us: 1.04x slower                                                                 |
| fannkuch                   | 247 ms                                                      | 257 ms: 1.04x slower                                                                 |
| xml_etree_process          | 37.7 ms                                                     | 39.4 ms: 1.04x slower                                                                |
| django_template            | 22.9 ms                                                     | 24.4 ms: 1.06x slower                                                                |
| pprint_safe_repr           | 513 ms                                                      | 553 ms: 1.08x slower                                                                 |
| pprint_pformat             | 1.05 sec                                                    | 1.13 sec: 1.08x slower                                                               |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.09x slower                                                                 |
| pickle_pure_python         | 195 us                                                      | 215 us: 1.10x slower                                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.29 ms: 1.10x slower                                                                |
| telco                      | 4.13 ms                                                     | 4.62 ms: 1.12x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 19.4 ms: 1.19x slower                                                                |
| python_startup             | 19.5 ms                                                     | 25.6 ms: 1.32x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 2.18 ms: 1.43x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                                                |
| logging_silent             | 60.5 ns                                                     | 317 ns: 5.24x slower                                                                 |
| coverage                   | 40.8 ms                                                     | 293 ms: 7.16x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                         |

Benchmark hidden because not significant (2): nqueens, logging_simple
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250616-3.15.0a0-c41d531/bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 99.77% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown