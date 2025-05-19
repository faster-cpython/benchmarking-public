# Results vs. 3.10.4

- fork: faster-cpython
- ref: make_decref_a_call
- machine: windows-amd64
- commit hash: 4fee8de
- commit date: 2025-05-19
- overall geometric mean: 1.248x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                               |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                             |
| html5lib       | 51.0 ms                                                     | 38.1 ms: 1.34x faster                                                              |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 409 ms: 2.71x faster                                                               |
| async_tree_none         | 435 ms                                                      | 176 ms: 2.47x faster                                                               |
| async_tree_memoization  | 526 ms                                                      | 213 ms: 2.47x faster                                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 335 ms: 1.91x faster                                                               |
| Geometric mean          | (ref)                                                       | 2.37x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.1 ms: 1.43x faster                                                              |
| nbody          | 71.3 ms                                                     | 60.7 ms: 1.17x faster                                                              |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                               |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.0 ms: 1.29x faster                                                              |
| regex_dna      | 136 ms                                                      | 116 ms: 1.18x faster                                                               |
| regex_v8       | 15.4 ms                                                     | 13.6 ms: 1.14x faster                                                              |
| regex_effbot   | 1.66 ms                                                     | 1.50 ms: 1.10x faster                                                              |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.66 ms: 1.37x faster                                                              |
| unpickle_pure_python | 183 us                                                      | 137 us: 1.34x faster                                                               |
| pickle_pure_python   | 270 us                                                      | 213 us: 1.27x faster                                                               |
| tomli_loads          | 1.67 sec                                                    | 1.40 sec: 1.19x faster                                                             |
| xml_etree_process    | 44.5 ms                                                     | 42.3 ms: 1.05x faster                                                              |
| xml_etree_parse      | 96.8 ms                                                     | 94.2 ms: 1.03x faster                                                              |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.6 ms: 1.02x slower                                                              |
| xml_etree_generate   | 55.5 ms                                                     | 60.7 ms: 1.09x slower                                                              |
| json_loads           | 14.0 us                                                     | 15.6 us: 1.12x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                              |
| python_startup         | 20.6 ms                                                     | 24.9 ms: 1.21x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.21x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.49 ms: 1.39x faster                                                              |
| genshi_text     | 19.8 ms                                                     | 16.1 ms: 1.23x faster                                                              |
| django_template | 28.9 ms                                                     | 25.4 ms: 1.14x faster                                                              |
| genshi_xml      | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                              |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.92x faster                                                               |
| async_tree_io            | 1.11 sec                                                    | 409 ms: 2.71x faster                                                               |
| pathlib                  | 75.7 ms                                                     | 29.9 ms: 2.53x faster                                                              |
| async_tree_none          | 435 ms                                                      | 176 ms: 2.47x faster                                                               |
| async_tree_memoization   | 526 ms                                                      | 213 ms: 2.47x faster                                                               |
| mdp                      | 1.78 sec                                                    | 841 ms: 2.12x faster                                                               |
| deltablue                | 4.19 ms                                                     | 2.17 ms: 1.93x faster                                                              |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 335 ms: 1.91x faster                                                               |
| go                       | 139 ms                                                      | 78.6 ms: 1.77x faster                                                              |
| pylint                   | 350 ms                                                      | 203 ms: 1.73x faster                                                               |
| richards_super           | 52.2 ms                                                     | 31.4 ms: 1.67x faster                                                              |
| chaos                    | 61.7 ms                                                     | 39.0 ms: 1.58x faster                                                              |
| generators               | 32.4 ms                                                     | 20.9 ms: 1.55x faster                                                              |
| richards                 | 42.4 ms                                                     | 27.6 ms: 1.54x faster                                                              |
| raytrace                 | 273 ms                                                      | 182 ms: 1.50x faster                                                               |
| deepcopy_memo            | 28.8 us                                                     | 19.6 us: 1.47x faster                                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.5 ms: 1.45x faster                                                              |
| float                    | 61.7 ms                                                     | 43.1 ms: 1.43x faster                                                              |
| scimark_lu               | 85.8 ms                                                     | 60.7 ms: 1.41x faster                                                              |
| deepcopy                 | 255 us                                                      | 182 us: 1.41x faster                                                               |
| mako                     | 9.03 ms                                                     | 6.49 ms: 1.39x faster                                                              |
| hexiom                   | 5.74 ms                                                     | 4.14 ms: 1.39x faster                                                              |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                              |
| json_dumps               | 9.16 ms                                                     | 6.66 ms: 1.37x faster                                                              |
| pyflate                  | 409 ms                                                      | 301 ms: 1.36x faster                                                               |
| scimark_sor              | 106 ms                                                      | 78.6 ms: 1.35x faster                                                              |
| html5lib                 | 51.0 ms                                                     | 38.1 ms: 1.34x faster                                                              |
| unpickle_pure_python     | 183 us                                                      | 137 us: 1.34x faster                                                               |
| crypto_pyaes             | 62.5 ms                                                     | 47.6 ms: 1.31x faster                                                              |
| pycparser                | 930 ms                                                      | 717 ms: 1.30x faster                                                               |
| spectral_norm            | 77.3 ms                                                     | 59.6 ms: 1.30x faster                                                              |
| regex_compile            | 106 ms                                                      | 82.0 ms: 1.29x faster                                                              |
| pickle_pure_python       | 270 us                                                      | 213 us: 1.27x faster                                                               |
| dulwich_log              | 50.5 ms                                                     | 40.9 ms: 1.23x faster                                                              |
| genshi_text              | 19.8 ms                                                     | 16.1 ms: 1.23x faster                                                              |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.20x faster                                                              |
| tomli_loads              | 1.67 sec                                                    | 1.40 sec: 1.19x faster                                                             |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                              |
| sympy_sum                | 107 ms                                                      | 90.6 ms: 1.18x faster                                                              |
| thrift                   | 617 us                                                      | 524 us: 1.18x faster                                                               |
| regex_dna                | 136 ms                                                      | 116 ms: 1.18x faster                                                               |
| pprint_pformat           | 1.22 sec                                                    | 1.04 sec: 1.17x faster                                                             |
| nbody                    | 71.3 ms                                                     | 60.7 ms: 1.17x faster                                                              |
| pprint_safe_repr         | 592 ms                                                      | 510 ms: 1.16x faster                                                               |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                             |
| deepcopy_reduce          | 2.20 us                                                     | 1.93 us: 1.14x faster                                                              |
| django_template          | 28.9 ms                                                     | 25.4 ms: 1.14x faster                                                              |
| regex_v8                 | 15.4 ms                                                     | 13.6 ms: 1.14x faster                                                              |
| genshi_xml               | 41.0 ms                                                     | 36.6 ms: 1.12x faster                                                              |
| bench_thread_pool        | 958 us                                                      | 861 us: 1.11x faster                                                               |
| regex_effbot             | 1.66 ms                                                     | 1.50 ms: 1.10x faster                                                              |
| coroutines               | 16.0 ms                                                     | 14.6 ms: 1.09x faster                                                              |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                               |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                               |
| nqueens                  | 66.6 ms                                                     | 62.8 ms: 1.06x faster                                                              |
| xml_etree_process        | 44.5 ms                                                     | 42.3 ms: 1.05x faster                                                              |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.62 ms: 1.04x faster                                                              |
| xml_etree_parse          | 96.8 ms                                                     | 94.2 ms: 1.03x faster                                                              |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                                               |
| json                     | 3.14 ms                                                     | 3.08 ms: 1.02x faster                                                              |
| scimark_fft              | 187 ms                                                      | 186 ms: 1.01x faster                                                               |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                               |
| meteor_contest           | 75.9 ms                                                     | 77.4 ms: 1.02x slower                                                              |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.6 ms: 1.02x slower                                                              |
| logging_format           | 6.76 us                                                     | 7.03 us: 1.04x slower                                                              |
| logging_simple           | 6.22 us                                                     | 6.55 us: 1.05x slower                                                              |
| xml_etree_generate       | 55.5 ms                                                     | 60.7 ms: 1.09x slower                                                              |
| fannkuch                 | 256 ms                                                      | 280 ms: 1.09x slower                                                               |
| json_loads               | 14.0 us                                                     | 15.6 us: 1.12x slower                                                              |
| async_generators         | 222 ms                                                      | 252 ms: 1.14x slower                                                               |
| python_startup_no_site   | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                              |
| python_startup           | 20.6 ms                                                     | 24.9 ms: 1.21x slower                                                              |
| telco                    | 3.94 ms                                                     | 5.09 ms: 1.29x slower                                                              |
| coverage                 | 39.0 ms                                                     | 56.9 ms: 1.46x slower                                                              |
| gc_traversal             | 1.41 ms                                                     | 2.08 ms: 1.48x slower                                                              |
| bench_mp_pool            | 62.0 ms                                                     | 92.7 ms: 1.49x slower                                                              |
| create_gc_cycles         | 800 us                                                      | 1.29 ms: 1.62x slower                                                              |
| logging_silent           | 94.6 ns                                                     | 342 ns: 3.61x slower                                                               |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                                       |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250519-3.15.0a0-4fee8de/bm-20250519-pythonperf1-amd64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.248x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown