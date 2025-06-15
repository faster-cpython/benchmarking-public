# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: 9b65402
- commit date: 2025-06-13
- overall geometric mean: 1.066x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.02x faster                                                               |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.45x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.68x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.6 ms: 1.27x faster                                                                |
| nbody          | 71.9 ms                                                     | 61.8 ms: 1.16x faster                                                                |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 80.9 ms: 1.08x faster                                                                |
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                                 |
| regex_effbot   | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                                |
| regex_v8       | 14.2 ms                                                     | 13.9 ms: 1.03x faster                                                                |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|---------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse     | 93.0 ms                                                     | 90.2 ms: 1.03x faster                                                                |
| xml_etree_iterparse | 65.2 ms                                                     | 64.1 ms: 1.02x faster                                                                |
| tomli_loads         | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                               |
| json_loads          | 13.9 us                                                     | 14.3 us: 1.03x slower                                                                |
| xml_etree_process   | 37.7 ms                                                     | 39.3 ms: 1.04x slower                                                                |
| pickle_pure_python  | 195 us                                                      | 212 us: 1.09x slower                                                                 |
| json_dumps          | 5.70 ms                                                     | 6.31 ms: 1.11x slower                                                                |
| Geometric mean      | (ref)                                                       | 1.02x slower                                                                         |

Benchmark hidden because not significant (2): xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                                |
| python_startup         | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.64 ms: 1.07x faster                                                                |
| django_template | 22.9 ms                                                     | 23.7 ms: 1.03x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.02x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.4 ms: 2.48x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 391 ms: 1.97x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 397 ms: 1.84x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.71x faster                                                                 |
| mdp                        | 1.37 sec                                                    | 805 ms: 1.70x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 170 ms: 1.68x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 208 ms: 1.63x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 330 ms: 1.48x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 345 ms: 1.45x faster                                                                 |
| deepcopy                   | 238 us                                                      | 170 us: 1.40x faster                                                                 |
| comprehensions             | 14.1 us                                                     | 10.8 us: 1.31x faster                                                                |
| deepcopy_memo              | 23.7 us                                                     | 18.2 us: 1.30x faster                                                                |
| float                      | 56.8 ms                                                     | 44.6 ms: 1.27x faster                                                                |
| go                         | 91.6 ms                                                     | 76.1 ms: 1.20x faster                                                                |
| nbody                      | 71.9 ms                                                     | 61.8 ms: 1.16x faster                                                                |
| generators                 | 22.5 ms                                                     | 19.5 ms: 1.16x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.85 us: 1.13x faster                                                                |
| chaos                      | 43.3 ms                                                     | 38.7 ms: 1.12x faster                                                                |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                                |
| spectral_norm              | 66.9 ms                                                     | 60.0 ms: 1.12x faster                                                                |
| regex_compile              | 87.5 ms                                                     | 80.9 ms: 1.08x faster                                                                |
| mako                       | 7.09 ms                                                     | 6.64 ms: 1.07x faster                                                                |
| raytrace                   | 192 ms                                                      | 180 ms: 1.07x faster                                                                 |
| dulwich_log                | 44.3 ms                                                     | 41.5 ms: 1.07x faster                                                                |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                                 |
| regex_effbot               | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                                |
| richards                   | 28.4 ms                                                     | 26.9 ms: 1.05x faster                                                                |
| pyflate                    | 295 ms                                                      | 280 ms: 1.05x faster                                                                 |
| sympy_sum                  | 91.5 ms                                                     | 87.2 ms: 1.05x faster                                                                |
| async_generators           | 239 ms                                                      | 229 ms: 1.05x faster                                                                 |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.9 ms: 1.04x faster                                                                |
| meteor_contest             | 74.6 ms                                                     | 71.6 ms: 1.04x faster                                                                |
| richards_super             | 32.1 ms                                                     | 30.8 ms: 1.04x faster                                                                |
| crypto_pyaes               | 48.5 ms                                                     | 46.6 ms: 1.04x faster                                                                |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.04x faster                                                                |
| sympy_str                  | 175 ms                                                      | 169 ms: 1.04x faster                                                                 |
| nqueens                    | 62.8 ms                                                     | 60.6 ms: 1.04x faster                                                                |
| xml_etree_parse            | 93.0 ms                                                     | 90.2 ms: 1.03x faster                                                                |
| regex_v8                   | 14.2 ms                                                     | 13.9 ms: 1.03x faster                                                                |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.03x faster                                                                |
| scimark_sor                | 78.8 ms                                                     | 76.9 ms: 1.02x faster                                                                |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                                 |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.02x faster                                                               |
| json                       | 3.05 ms                                                     | 2.98 ms: 1.02x faster                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.51 ms: 1.02x faster                                                                |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.1 ms: 1.02x faster                                                                |
| scimark_fft                | 184 ms                                                      | 182 ms: 1.02x faster                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                               |
| hexiom                     | 4.10 ms                                                     | 4.08 ms: 1.00x faster                                                                |
| logging_format             | 6.72 us                                                     | 6.77 us: 1.01x slower                                                                |
| sympy_expand               | 284 ms                                                      | 289 ms: 1.02x slower                                                                 |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                                 |
| pycparser                  | 699 ms                                                      | 715 ms: 1.02x slower                                                                 |
| deltablue                  | 2.16 ms                                                     | 2.22 ms: 1.03x slower                                                                |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                                |
| django_template            | 22.9 ms                                                     | 23.7 ms: 1.03x slower                                                                |
| xml_etree_process          | 37.7 ms                                                     | 39.3 ms: 1.04x slower                                                                |
| fannkuch                   | 247 ms                                                      | 257 ms: 1.04x slower                                                                 |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                               |
| pprint_safe_repr           | 513 ms                                                      | 547 ms: 1.07x slower                                                                 |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.09x slower                                                                 |
| pickle_pure_python         | 195 us                                                      | 212 us: 1.09x slower                                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.31 ms: 1.11x slower                                                                |
| telco                      | 4.13 ms                                                     | 4.63 ms: 1.12x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 19.2 ms: 1.18x slower                                                                |
| python_startup             | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 2.15 ms: 1.41x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 1.34 ms: 1.78x slower                                                                |
| logging_silent             | 60.5 ns                                                     | 316 ns: 5.23x slower                                                                 |
| coverage                   | 40.8 ms                                                     | 289 ms: 7.08x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                         |

Benchmark hidden because not significant (4): xml_etree_generate, scimark_lu, logging_simple, unpickle_pure_python
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250613-3.15.0a0-9b65402/bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.066x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown