# Results vs. 3.12.0

- fork: faster-cpython
- ref: immortal_stickiness
- machine: windows-amd64
- commit hash: 490cf8d
- commit date: 2025-03-12
- overall geometric mean: 1.046x faster
- HPT reliability: 66.50%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 226 ms: 1.04x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                               |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 420 ms: 1.83x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 426 ms: 1.72x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 189 ms: 1.54x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 343 ms: 1.43x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.60x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 45.3 ms: 1.25x faster                                                                |
| nbody          | 71.9 ms                                                     | 69.2 ms: 1.04x faster                                                                |
| pidigits       | 152 ms                                                      | 152 ms: 1.00x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.40 ms: 1.16x faster                                                                |
| regex_dna      | 126 ms                                                      | 112 ms: 1.13x faster                                                                 |
| regex_v8       | 14.2 ms                                                     | 13.1 ms: 1.08x faster                                                                |
| regex_compile  | 87.5 ms                                                     | 85.9 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 91.7 ms: 1.01x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                               |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.05x slower                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 58.9 ms: 1.05x slower                                                                |
| unpickle_pure_python | 133 us                                                      | 146 us: 1.09x slower                                                                 |
| xml_etree_process    | 37.7 ms                                                     | 42.1 ms: 1.12x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 224 us: 1.15x slower                                                                 |
| json_dumps           | 5.70 ms                                                     | 6.90 ms: 1.21x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.4 ms: 1.26x slower                                                                |
| python_startup         | 19.5 ms                                                     | 26.3 ms: 1.35x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.83 ms: 1.04x faster                                                                |
| django_template | 22.9 ms                                                     | 26.0 ms: 1.13x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.0 ms: 2.52x faster                                                                |
| async_tree_io_tg           | 771 ms                                                      | 420 ms: 1.83x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 426 ms: 1.72x faster                                                                 |
| async_tree_memoization_tg  | 367 ms                                                      | 217 ms: 1.69x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 177 ms: 1.61x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 220 ms: 1.54x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 189 ms: 1.54x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 343 ms: 1.43x faster                                                                 |
| deepcopy                   | 238 us                                                      | 181 us: 1.31x faster                                                                 |
| float                      | 56.8 ms                                                     | 45.3 ms: 1.25x faster                                                                |
| comprehensions             | 14.1 us                                                     | 11.8 us: 1.20x faster                                                                |
| deepcopy_memo              | 23.7 us                                                     | 19.8 us: 1.19x faster                                                                |
| spectral_norm              | 66.9 ms                                                     | 56.0 ms: 1.19x faster                                                                |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.40 ms: 1.16x faster                                                                |
| regex_dna                  | 126 ms                                                      | 112 ms: 1.13x faster                                                                 |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.91 us: 1.10x faster                                                                |
| regex_v8                   | 14.2 ms                                                     | 13.1 ms: 1.08x faster                                                                |
| coroutines                 | 14.3 ms                                                     | 13.4 ms: 1.06x faster                                                                |
| async_generators           | 239 ms                                                      | 228 ms: 1.05x faster                                                                 |
| dulwich_log                | 44.3 ms                                                     | 42.6 ms: 1.04x faster                                                                |
| nbody                      | 71.9 ms                                                     | 69.2 ms: 1.04x faster                                                                |
| scimark_fft                | 184 ms                                                      | 178 ms: 1.04x faster                                                                 |
| mako                       | 7.09 ms                                                     | 6.83 ms: 1.04x faster                                                                |
| sympy_sum                  | 91.5 ms                                                     | 88.7 ms: 1.03x faster                                                                |
| logging_silent             | 60.5 ns                                                     | 58.8 ns: 1.03x faster                                                                |
| go                         | 91.6 ms                                                     | 89.1 ms: 1.03x faster                                                                |
| regex_compile              | 87.5 ms                                                     | 85.9 ms: 1.02x faster                                                                |
| xml_etree_parse            | 93.0 ms                                                     | 91.7 ms: 1.01x faster                                                                |
| scimark_sor                | 78.8 ms                                                     | 77.7 ms: 1.01x faster                                                                |
| scimark_monte_carlo        | 43.7 ms                                                     | 43.3 ms: 1.01x faster                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.55 ms: 1.00x faster                                                                |
| pidigits                   | 152 ms                                                      | 152 ms: 1.00x faster                                                                 |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                               |
| pprint_pformat             | 1.05 sec                                                    | 1.06 sec: 1.01x slower                                                               |
| pprint_safe_repr           | 513 ms                                                      | 518 ms: 1.01x slower                                                                 |
| nqueens                    | 62.8 ms                                                     | 63.9 ms: 1.02x slower                                                                |
| richards                   | 28.4 ms                                                     | 28.9 ms: 1.02x slower                                                                |
| richards_super             | 32.1 ms                                                     | 32.8 ms: 1.02x slower                                                                |
| sympy_integrate            | 13.0 ms                                                     | 13.3 ms: 1.02x slower                                                                |
| scimark_lu                 | 58.9 ms                                                     | 60.4 ms: 1.03x slower                                                                |
| logging_simple             | 6.28 us                                                     | 6.47 us: 1.03x slower                                                                |
| crypto_pyaes               | 48.5 ms                                                     | 50.2 ms: 1.03x slower                                                                |
| deltablue                  | 2.16 ms                                                     | 2.24 ms: 1.04x slower                                                                |
| 2to3                       | 218 ms                                                      | 226 ms: 1.04x slower                                                                 |
| logging_format             | 6.72 us                                                     | 6.97 us: 1.04x slower                                                                |
| raytrace                   | 192 ms                                                      | 200 ms: 1.04x slower                                                                 |
| meteor_contest             | 74.6 ms                                                     | 78.3 ms: 1.05x slower                                                                |
| hexiom                     | 4.10 ms                                                     | 4.31 ms: 1.05x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                               |
| pyflate                    | 295 ms                                                      | 310 ms: 1.05x slower                                                                 |
| sympy_expand               | 284 ms                                                      | 299 ms: 1.05x slower                                                                 |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.05x slower                                                                |
| xml_etree_generate         | 55.8 ms                                                     | 58.9 ms: 1.05x slower                                                                |
| pycparser                  | 699 ms                                                      | 742 ms: 1.06x slower                                                                 |
| unpickle_pure_python       | 133 us                                                      | 146 us: 1.09x slower                                                                 |
| xml_etree_process          | 37.7 ms                                                     | 42.1 ms: 1.12x slower                                                                |
| fannkuch                   | 247 ms                                                      | 276 ms: 1.12x slower                                                                 |
| django_template            | 22.9 ms                                                     | 26.0 ms: 1.13x slower                                                                |
| pickle_pure_python         | 195 us                                                      | 224 us: 1.15x slower                                                                 |
| mdp                        | 1.37 sec                                                    | 1.60 sec: 1.16x slower                                                               |
| telco                      | 4.13 ms                                                     | 4.85 ms: 1.17x slower                                                                |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.19x slower                                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.90 ms: 1.21x slower                                                                |
| coverage                   | 40.8 ms                                                     | 49.5 ms: 1.21x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 20.4 ms: 1.26x slower                                                                |
| bench_mp_pool              | 69.2 ms                                                     | 88.3 ms: 1.28x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 2.03 ms: 1.33x slower                                                                |
| python_startup             | 19.5 ms                                                     | 26.3 ms: 1.35x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 1.24 ms: 1.64x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                         |

Benchmark hidden because not significant (5): xml_etree_iterparse, sympy_str, chaos, json, bench_thread_pool
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250312-3.14.0a5+-490cf8d/bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 66.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown