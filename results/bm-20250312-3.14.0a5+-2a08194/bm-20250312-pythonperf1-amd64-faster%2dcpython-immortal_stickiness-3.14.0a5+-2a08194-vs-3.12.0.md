# Results vs. 3.12.0

- fork: faster-cpython
- ref: immortal_stickiness
- machine: windows-amd64
- commit hash: 2a08194
- commit date: 2025-03-12
- overall geometric mean: 1.040x faster
- HPT reliability: 53.83%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 229 ms: 1.05x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                               |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 420 ms: 1.84x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 424 ms: 1.73x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.62x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 222 ms: 1.53x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 191 ms: 1.53x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 342 ms: 1.43x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.60x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.4 ms: 1.25x faster                                                                |
| nbody          | 71.9 ms                                                     | 67.4 ms: 1.07x faster                                                                |
| pidigits       | 152 ms                                                      | 152 ms: 1.00x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.40 ms: 1.16x faster                                                                |
| regex_dna      | 126 ms                                                      | 111 ms: 1.14x faster                                                                 |
| regex_v8       | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                                                |
| regex_compile  | 87.5 ms                                                     | 86.5 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 90.9 ms: 1.02x faster                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.0 ms: 1.02x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                               |
| xml_etree_generate   | 55.8 ms                                                     | 59.2 ms: 1.06x slower                                                                |
| json_loads           | 13.9 us                                                     | 14.8 us: 1.07x slower                                                                |
| xml_etree_process    | 37.7 ms                                                     | 42.4 ms: 1.12x slower                                                                |
| unpickle_pure_python | 133 us                                                      | 150 us: 1.13x slower                                                                 |
| pickle_pure_python   | 195 us                                                      | 232 us: 1.19x slower                                                                 |
| json_dumps           | 5.70 ms                                                     | 7.02 ms: 1.23x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.5 ms: 1.26x slower                                                                |
| python_startup         | 19.5 ms                                                     | 26.4 ms: 1.36x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.96 ms: 1.02x faster                                                                |
| django_template | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.2 ms: 2.50x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 420 ms: 1.84x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 424 ms: 1.73x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.62x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 222 ms: 1.53x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 191 ms: 1.53x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 342 ms: 1.47x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 342 ms: 1.43x faster                                                                 |
| deepcopy                   | 238 us                                                      | 180 us: 1.33x faster                                                                 |
| float                      | 56.8 ms                                                     | 45.4 ms: 1.25x faster                                                                |
| deepcopy_memo              | 23.7 us                                                     | 19.3 us: 1.23x faster                                                                |
| comprehensions             | 14.1 us                                                     | 11.9 us: 1.19x faster                                                                |
| spectral_norm              | 66.9 ms                                                     | 56.6 ms: 1.18x faster                                                                |
| generators                 | 22.5 ms                                                     | 19.3 ms: 1.17x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.40 ms: 1.16x faster                                                                |
| regex_dna                  | 126 ms                                                      | 111 ms: 1.14x faster                                                                 |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.93 us: 1.08x faster                                                                |
| regex_v8                   | 14.2 ms                                                     | 13.2 ms: 1.08x faster                                                                |
| nbody                      | 71.9 ms                                                     | 67.4 ms: 1.07x faster                                                                |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.06x faster                                                                |
| async_generators           | 239 ms                                                      | 227 ms: 1.05x faster                                                                 |
| logging_silent             | 60.5 ns                                                     | 58.4 ns: 1.04x faster                                                                |
| dulwich_log                | 44.3 ms                                                     | 42.8 ms: 1.04x faster                                                                |
| scimark_fft                | 184 ms                                                      | 180 ms: 1.03x faster                                                                 |
| xml_etree_parse            | 93.0 ms                                                     | 90.9 ms: 1.02x faster                                                                |
| mako                       | 7.09 ms                                                     | 6.96 ms: 1.02x faster                                                                |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.0 ms: 1.02x faster                                                                |
| sympy_sum                  | 91.5 ms                                                     | 90.4 ms: 1.01x faster                                                                |
| scimark_lu                 | 58.9 ms                                                     | 58.2 ms: 1.01x faster                                                                |
| regex_compile              | 87.5 ms                                                     | 86.5 ms: 1.01x faster                                                                |
| go                         | 91.6 ms                                                     | 90.8 ms: 1.01x faster                                                                |
| pidigits                   | 152 ms                                                      | 152 ms: 1.00x faster                                                                 |
| scimark_monte_carlo        | 43.7 ms                                                     | 44.0 ms: 1.01x slower                                                                |
| sympy_str                  | 175 ms                                                      | 177 ms: 1.01x slower                                                                 |
| chaos                      | 43.3 ms                                                     | 44.1 ms: 1.02x slower                                                                |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                               |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.03x slower                                                                |
| raytrace                   | 192 ms                                                      | 200 ms: 1.04x slower                                                                 |
| deltablue                  | 2.16 ms                                                     | 2.25 ms: 1.04x slower                                                                |
| nqueens                    | 62.8 ms                                                     | 65.4 ms: 1.04x slower                                                                |
| logging_simple             | 6.28 us                                                     | 6.54 us: 1.04x slower                                                                |
| meteor_contest             | 74.6 ms                                                     | 77.9 ms: 1.04x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                               |
| crypto_pyaes               | 48.5 ms                                                     | 50.7 ms: 1.04x slower                                                                |
| richards_super             | 32.1 ms                                                     | 33.7 ms: 1.05x slower                                                                |
| 2to3                       | 218 ms                                                      | 229 ms: 1.05x slower                                                                 |
| pprint_pformat             | 1.05 sec                                                    | 1.10 sec: 1.05x slower                                                               |
| logging_format             | 6.72 us                                                     | 7.07 us: 1.05x slower                                                                |
| pprint_safe_repr           | 513 ms                                                      | 541 ms: 1.05x slower                                                                 |
| xml_etree_generate         | 55.8 ms                                                     | 59.2 ms: 1.06x slower                                                                |
| richards                   | 28.4 ms                                                     | 30.2 ms: 1.07x slower                                                                |
| sympy_expand               | 284 ms                                                      | 303 ms: 1.07x slower                                                                 |
| json_loads                 | 13.9 us                                                     | 14.8 us: 1.07x slower                                                                |
| pyflate                    | 295 ms                                                      | 314 ms: 1.07x slower                                                                 |
| hexiom                     | 4.10 ms                                                     | 4.39 ms: 1.07x slower                                                                |
| pycparser                  | 699 ms                                                      | 752 ms: 1.08x slower                                                                 |
| xml_etree_process          | 37.7 ms                                                     | 42.4 ms: 1.12x slower                                                                |
| unpickle_pure_python       | 133 us                                                      | 150 us: 1.13x slower                                                                 |
| django_template            | 22.9 ms                                                     | 25.9 ms: 1.13x slower                                                                |
| fannkuch                   | 247 ms                                                      | 282 ms: 1.14x slower                                                                 |
| mdp                        | 1.37 sec                                                    | 1.58 sec: 1.15x slower                                                               |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.17x slower                                                                 |
| telco                      | 4.13 ms                                                     | 4.90 ms: 1.19x slower                                                                |
| pickle_pure_python         | 195 us                                                      | 232 us: 1.19x slower                                                                 |
| coverage                   | 40.8 ms                                                     | 49.4 ms: 1.21x slower                                                                |
| json_dumps                 | 5.70 ms                                                     | 7.02 ms: 1.23x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 20.5 ms: 1.26x slower                                                                |
| bench_mp_pool              | 69.2 ms                                                     | 88.7 ms: 1.28x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 2.03 ms: 1.33x slower                                                                |
| python_startup             | 19.5 ms                                                     | 26.4 ms: 1.36x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 1.24 ms: 1.65x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                         |

Benchmark hidden because not significant (4): json, scimark_sparse_mat_mult, scimark_sor, bench_thread_pool
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250312-3.14.0a5+-2a08194/bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 53.83% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown