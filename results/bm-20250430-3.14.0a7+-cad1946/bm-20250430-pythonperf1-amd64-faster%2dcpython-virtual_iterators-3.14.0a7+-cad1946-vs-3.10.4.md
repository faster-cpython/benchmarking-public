# Results vs. 3.10.4

- fork: faster-cpython
- ref: virtual_iterators
- machine: windows-amd64
- commit hash: cad1946
- commit date: 2025-04-30
- overall geometric mean: 1.282x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                               |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                             |
| html5lib       | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                                              |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 409 ms: 2.71x faster                                                               |
| async_tree_memoization  | 526 ms                                                      | 207 ms: 2.55x faster                                                               |
| async_tree_none         | 435 ms                                                      | 180 ms: 2.42x faster                                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 334 ms: 1.91x faster                                                               |
| Geometric mean          | (ref)                                                       | 2.38x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                              |
| nbody          | 71.3 ms                                                     | 63.7 ms: 1.12x faster                                                              |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.4 ms: 1.32x faster                                                              |
| regex_effbot   | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                                              |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                               |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                              |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 139 us: 1.32x faster                                                               |
| json_dumps           | 9.16 ms                                                     | 6.96 ms: 1.32x faster                                                              |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                               |
| tomli_loads          | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                             |
| xml_etree_process    | 44.5 ms                                                     | 39.7 ms: 1.12x faster                                                              |
| xml_etree_parse      | 96.8 ms                                                     | 88.7 ms: 1.09x faster                                                              |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                              |
| xml_etree_generate   | 55.5 ms                                                     | 56.4 ms: 1.02x slower                                                              |
| json_loads           | 14.0 us                                                     | 15.4 us: 1.10x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                              |
| python_startup_no_site | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.54 ms: 1.38x faster                                                              |
| genshi_text     | 19.8 ms                                                     | 14.7 ms: 1.35x faster                                                              |
| genshi_xml      | 41.0 ms                                                     | 33.5 ms: 1.22x faster                                                              |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                              |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 100 us: 3.35x faster                                                               |
| async_tree_io            | 1.11 sec                                                    | 409 ms: 2.71x faster                                                               |
| async_tree_memoization   | 526 ms                                                      | 207 ms: 2.55x faster                                                               |
| async_tree_none          | 435 ms                                                      | 180 ms: 2.42x faster                                                               |
| pathlib                  | 75.7 ms                                                     | 32.1 ms: 2.36x faster                                                              |
| mdp                      | 1.78 sec                                                    | 777 ms: 2.29x faster                                                               |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 334 ms: 1.91x faster                                                               |
| deltablue                | 4.19 ms                                                     | 2.20 ms: 1.90x faster                                                              |
| go                       | 139 ms                                                      | 77.3 ms: 1.80x faster                                                              |
| logging_silent           | 94.6 ns                                                     | 55.4 ns: 1.71x faster                                                              |
| generators               | 32.4 ms                                                     | 19.3 ms: 1.68x faster                                                              |
| richards_super           | 52.2 ms                                                     | 31.4 ms: 1.66x faster                                                              |
| deepcopy_memo            | 28.8 us                                                     | 18.2 us: 1.58x faster                                                              |
| chaos                    | 61.7 ms                                                     | 39.1 ms: 1.58x faster                                                              |
| raytrace                 | 273 ms                                                      | 176 ms: 1.56x faster                                                               |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.55x faster                                                              |
| richards                 | 42.4 ms                                                     | 27.5 ms: 1.54x faster                                                              |
| deepcopy                 | 255 us                                                      | 167 us: 1.52x faster                                                               |
| pyflate                  | 409 ms                                                      | 276 ms: 1.48x faster                                                               |
| hexiom                   | 5.74 ms                                                     | 3.95 ms: 1.45x faster                                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.5 ms: 1.41x faster                                                              |
| float                    | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                              |
| scimark_sor              | 106 ms                                                      | 75.7 ms: 1.40x faster                                                              |
| mako                     | 9.03 ms                                                     | 6.54 ms: 1.38x faster                                                              |
| scimark_lu               | 85.8 ms                                                     | 62.8 ms: 1.37x faster                                                              |
| spectral_norm            | 77.3 ms                                                     | 57.0 ms: 1.36x faster                                                              |
| genshi_text              | 19.8 ms                                                     | 14.7 ms: 1.35x faster                                                              |
| unpickle_pure_python     | 183 us                                                      | 139 us: 1.32x faster                                                               |
| regex_compile            | 106 ms                                                      | 80.4 ms: 1.32x faster                                                              |
| json_dumps               | 9.16 ms                                                     | 6.96 ms: 1.32x faster                                                              |
| html5lib                 | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                                              |
| crypto_pyaes             | 62.5 ms                                                     | 47.9 ms: 1.30x faster                                                              |
| pycparser                | 930 ms                                                      | 714 ms: 1.30x faster                                                               |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                               |
| genshi_xml               | 41.0 ms                                                     | 33.5 ms: 1.22x faster                                                              |
| pprint_pformat           | 1.22 sec                                                    | 1.00 sec: 1.21x faster                                                             |
| tomli_loads              | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                             |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                              |
| dulwich_log              | 50.5 ms                                                     | 42.0 ms: 1.20x faster                                                              |
| pprint_safe_repr         | 592 ms                                                      | 494 ms: 1.20x faster                                                               |
| deepcopy_reduce          | 2.20 us                                                     | 1.84 us: 1.20x faster                                                              |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                                              |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.18x faster                                                              |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                             |
| regex_effbot             | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                                              |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                               |
| nbody                    | 71.3 ms                                                     | 63.7 ms: 1.12x faster                                                              |
| xml_etree_process        | 44.5 ms                                                     | 39.7 ms: 1.12x faster                                                              |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                               |
| bench_thread_pool        | 958 us                                                      | 864 us: 1.11x faster                                                               |
| nqueens                  | 66.6 ms                                                     | 60.2 ms: 1.11x faster                                                              |
| xml_etree_parse          | 96.8 ms                                                     | 88.7 ms: 1.09x faster                                                              |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                              |
| meteor_contest           | 75.9 ms                                                     | 70.7 ms: 1.07x faster                                                              |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.61 ms: 1.04x faster                                                              |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                              |
| fannkuch                 | 256 ms                                                      | 251 ms: 1.02x faster                                                               |
| json                     | 3.14 ms                                                     | 3.08 ms: 1.02x faster                                                              |
| logging_format           | 6.76 us                                                     | 6.83 us: 1.01x slower                                                              |
| logging_simple           | 6.22 us                                                     | 6.30 us: 1.01x slower                                                              |
| xml_etree_generate       | 55.5 ms                                                     | 56.4 ms: 1.02x slower                                                              |
| async_generators         | 222 ms                                                      | 232 ms: 1.05x slower                                                               |
| json_loads               | 14.0 us                                                     | 15.4 us: 1.10x slower                                                              |
| telco                    | 3.94 ms                                                     | 4.61 ms: 1.17x slower                                                              |
| python_startup           | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                              |
| python_startup_no_site   | 15.5 ms                                                     | 19.7 ms: 1.27x slower                                                              |
| coverage                 | 39.0 ms                                                     | 51.2 ms: 1.31x slower                                                              |
| bench_mp_pool            | 62.0 ms                                                     | 90.2 ms: 1.45x slower                                                              |
| gc_traversal             | 1.41 ms                                                     | 2.08 ms: 1.48x slower                                                              |
| create_gc_cycles         | 800 us                                                      | 1.26 ms: 1.57x slower                                                              |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                                       |

Benchmark hidden because not significant (2): pidigits, scimark_fft
Ignored benchmarks (26) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250430-3.14.0a7+-cad1946/bm-20250430-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.282x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown