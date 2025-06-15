# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: 9b65402
- commit date: 2025-06-13
- overall geometric mean: 1.165x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                               |
| html5lib       | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                                |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 397 ms: 2.79x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.55x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 208 ms: 2.54x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.43x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.6 ms: 1.38x faster                                                                |
| nbody          | 71.3 ms                                                     | 61.8 ms: 1.15x faster                                                                |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.9 ms: 1.31x faster                                                                |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                                 |
| regex_v8       | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                                |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.31 ms: 1.45x faster                                                                |
| unpickle_pure_python | 183 us                                                      | 134 us: 1.37x faster                                                                 |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 39.3 ms: 1.13x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 90.2 ms: 1.07x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.1 ms: 1.01x faster                                                                |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.16x faster                                                                         |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                                |
| python_startup         | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.64 ms: 1.36x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                                |
| django_template | 28.9 ms                                                     | 23.7 ms: 1.22x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 34.1 ms: 1.20x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.25x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 397 ms: 2.79x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.55x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 208 ms: 2.54x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 32.4 ms: 2.33x faster                                                                |
| mdp                      | 1.78 sec                                                    | 805 ms: 2.21x faster                                                                 |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.22 ms: 1.89x faster                                                                |
| go                       | 139 ms                                                      | 76.1 ms: 1.83x faster                                                                |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                                 |
| richards_super           | 52.2 ms                                                     | 30.8 ms: 1.69x faster                                                                |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                                                |
| chaos                    | 61.7 ms                                                     | 38.7 ms: 1.60x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 18.2 us: 1.58x faster                                                                |
| richards                 | 42.4 ms                                                     | 26.9 ms: 1.58x faster                                                                |
| comprehensions           | 16.5 us                                                     | 10.8 us: 1.53x faster                                                                |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                                 |
| deepcopy                 | 255 us                                                      | 170 us: 1.50x faster                                                                 |
| pyflate                  | 409 ms                                                      | 280 ms: 1.46x faster                                                                 |
| scimark_lu               | 85.8 ms                                                     | 58.8 ms: 1.46x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 6.31 ms: 1.45x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.08 ms: 1.41x faster                                                                |
| float                    | 61.7 ms                                                     | 44.6 ms: 1.38x faster                                                                |
| scimark_sor              | 106 ms                                                      | 76.9 ms: 1.38x faster                                                                |
| unpickle_pure_python     | 183 us                                                      | 134 us: 1.37x faster                                                                 |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.9 ms: 1.37x faster                                                                |
| mako                     | 9.03 ms                                                     | 6.64 ms: 1.36x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 46.6 ms: 1.34x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                                |
| regex_compile            | 106 ms                                                      | 80.9 ms: 1.31x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                                |
| pycparser                | 930 ms                                                      | 715 ms: 1.30x faster                                                                 |
| spectral_norm            | 77.3 ms                                                     | 60.0 ms: 1.29x faster                                                                |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                                 |
| tomli_loads              | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                               |
| sympy_sum                | 107 ms                                                      | 87.2 ms: 1.23x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.23x faster                                                                |
| django_template          | 28.9 ms                                                     | 23.7 ms: 1.22x faster                                                                |
| dulwich_log              | 50.5 ms                                                     | 41.5 ms: 1.21x faster                                                                |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 34.1 ms: 1.20x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.18x faster                                                               |
| nbody                    | 71.3 ms                                                     | 61.8 ms: 1.15x faster                                                                |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                                                 |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                                |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                                 |
| xml_etree_process        | 44.5 ms                                                     | 39.3 ms: 1.13x faster                                                                |
| regex_v8                 | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                                |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                                 |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                               |
| nqueens                  | 66.6 ms                                                     | 60.6 ms: 1.10x faster                                                                |
| sympy_expand             | 314 ms                                                      | 289 ms: 1.09x faster                                                                 |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.51 ms: 1.08x faster                                                                |
| pprint_safe_repr         | 592 ms                                                      | 547 ms: 1.08x faster                                                                 |
| regex_effbot             | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                                |
| xml_etree_parse          | 96.8 ms                                                     | 90.2 ms: 1.07x faster                                                                |
| meteor_contest           | 75.9 ms                                                     | 71.6 ms: 1.06x faster                                                                |
| json                     | 3.14 ms                                                     | 2.98 ms: 1.05x faster                                                                |
| scimark_fft              | 187 ms                                                      | 182 ms: 1.03x faster                                                                 |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.1 ms: 1.01x faster                                                                |
| logging_simple           | 6.22 us                                                     | 6.29 us: 1.01x slower                                                                |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                                |
| async_generators         | 222 ms                                                      | 229 ms: 1.03x slower                                                                 |
| telco                    | 3.94 ms                                                     | 4.63 ms: 1.17x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                                |
| python_startup           | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 2.15 ms: 1.52x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.34 ms: 1.67x slower                                                                |
| logging_silent           | 94.6 ns                                                     | 316 ns: 3.34x slower                                                                 |
| coverage                 | 39.0 ms                                                     | 289 ms: 7.41x slower                                                                 |
| thrift                   | 617 us                                                      | 98.5 ms: 159.56x slower                                                              |
| Geometric mean           | (ref)                                                       | 1.14x faster                                                                         |

Benchmark hidden because not significant (4): pidigits, logging_format, xml_etree_generate, fannkuch
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250613-3.15.0a0-9b65402/bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.165x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown