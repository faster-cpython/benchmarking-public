# Results vs. 3.10.4

- fork: faster-cpython
- ref: immortal_stickiness
- machine: windows-amd64
- commit hash: 2a08194
- commit date: 2025-03-12
- overall geometric mean: 1.217x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 229 ms: 1.07x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                               |
| html5lib       | 51.0 ms                                                     | 40.7 ms: 1.25x faster                                                                |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 424 ms: 2.62x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 222 ms: 2.37x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 191 ms: 2.28x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 342 ms: 1.87x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.27x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.4 ms: 1.36x faster                                                                |
| nbody          | 71.3 ms                                                     | 67.4 ms: 1.06x faster                                                                |
| pidigits       | 149 ms                                                      | 152 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 111 ms: 1.23x faster                                                                 |
| regex_compile  | 106 ms                                                      | 86.5 ms: 1.23x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.40 ms: 1.18x faster                                                                |
| regex_v8       | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                                                |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 7.02 ms: 1.31x faster                                                                |
| unpickle_pure_python | 183 us                                                      | 150 us: 1.22x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                               |
| pickle_pure_python   | 270 us                                                      | 232 us: 1.16x faster                                                                 |
| xml_etree_parse      | 96.8 ms                                                     | 90.9 ms: 1.06x faster                                                                |
| xml_etree_process    | 44.5 ms                                                     | 42.4 ms: 1.05x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.0 ms: 1.01x faster                                                                |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.06x slower                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 59.2 ms: 1.07x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.4 ms: 1.28x slower                                                                |
| python_startup_no_site | 15.5 ms                                                     | 20.5 ms: 1.32x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.96 ms: 1.30x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 17.4 ms: 1.14x faster                                                                |
| django_template | 28.9 ms                                                     | 25.9 ms: 1.12x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 39.1 ms: 1.05x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.02x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 424 ms: 2.62x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 222 ms: 2.37x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 32.2 ms: 2.35x faster                                                                |
| async_tree_none          | 435 ms                                                      | 191 ms: 2.28x faster                                                                 |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 342 ms: 1.87x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.25 ms: 1.86x faster                                                                |
| pylint                   | 350 ms                                                      | 203 ms: 1.73x faster                                                                 |
| generators               | 32.4 ms                                                     | 19.3 ms: 1.68x faster                                                                |
| logging_silent           | 94.6 ns                                                     | 58.4 ns: 1.62x faster                                                                |
| richards_super           | 52.2 ms                                                     | 33.7 ms: 1.55x faster                                                                |
| go                       | 139 ms                                                      | 90.8 ms: 1.53x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 19.3 us: 1.49x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 58.2 ms: 1.47x faster                                                                |
| deepcopy                 | 255 us                                                      | 180 us: 1.42x faster                                                                 |
| richards                 | 42.4 ms                                                     | 30.2 ms: 1.40x faster                                                                |
| chaos                    | 61.7 ms                                                     | 44.1 ms: 1.40x faster                                                                |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                                |
| raytrace                 | 273 ms                                                      | 200 ms: 1.37x faster                                                                 |
| spectral_norm            | 77.3 ms                                                     | 56.6 ms: 1.37x faster                                                                |
| float                    | 61.7 ms                                                     | 45.4 ms: 1.36x faster                                                                |
| scimark_sor              | 106 ms                                                      | 79.0 ms: 1.34x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.39 ms: 1.31x faster                                                                |
| json_dumps               | 9.16 ms                                                     | 7.02 ms: 1.31x faster                                                                |
| pyflate                  | 409 ms                                                      | 314 ms: 1.30x faster                                                                 |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.0 ms: 1.30x faster                                                                |
| mako                     | 9.03 ms                                                     | 6.96 ms: 1.30x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 40.7 ms: 1.25x faster                                                                |
| pycparser                | 930 ms                                                      | 752 ms: 1.24x faster                                                                 |
| crypto_pyaes             | 62.5 ms                                                     | 50.7 ms: 1.23x faster                                                                |
| regex_dna                | 136 ms                                                      | 111 ms: 1.23x faster                                                                 |
| regex_compile            | 106 ms                                                      | 86.5 ms: 1.23x faster                                                                |
| unpickle_pure_python     | 183 us                                                      | 150 us: 1.22x faster                                                                 |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                                |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.18x faster                                                                |
| regex_effbot             | 1.66 ms                                                     | 1.40 ms: 1.18x faster                                                                |
| sympy_sum                | 107 ms                                                      | 90.4 ms: 1.18x faster                                                                |
| dulwich_log              | 50.5 ms                                                     | 42.8 ms: 1.18x faster                                                                |
| regex_v8                 | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                                               |
| pickle_pure_python       | 270 us                                                      | 232 us: 1.16x faster                                                                 |
| thrift                   | 617 us                                                      | 533 us: 1.16x faster                                                                 |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                                |
| deepcopy_reduce          | 2.20 us                                                     | 1.93 us: 1.14x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 17.4 ms: 1.14x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.13x faster                                                               |
| mdp                      | 1.78 sec                                                    | 1.58 sec: 1.12x faster                                                               |
| django_template          | 28.9 ms                                                     | 25.9 ms: 1.12x faster                                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.10 sec: 1.11x faster                                                               |
| bench_thread_pool        | 958 us                                                      | 868 us: 1.10x faster                                                                 |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                                 |
| pprint_safe_repr         | 592 ms                                                      | 541 ms: 1.09x faster                                                                 |
| 2to3                     | 246 ms                                                      | 229 ms: 1.07x faster                                                                 |
| xml_etree_parse          | 96.8 ms                                                     | 90.9 ms: 1.06x faster                                                                |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.56 ms: 1.06x faster                                                                |
| nbody                    | 71.3 ms                                                     | 67.4 ms: 1.06x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 39.1 ms: 1.05x faster                                                                |
| xml_etree_process        | 44.5 ms                                                     | 42.4 ms: 1.05x faster                                                                |
| scimark_fft              | 187 ms                                                      | 180 ms: 1.04x faster                                                                 |
| sympy_expand             | 314 ms                                                      | 303 ms: 1.04x faster                                                                 |
| json                     | 3.14 ms                                                     | 3.05 ms: 1.03x faster                                                                |
| nqueens                  | 66.6 ms                                                     | 65.4 ms: 1.02x faster                                                                |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.0 ms: 1.01x faster                                                                |
| pidigits                 | 149 ms                                                      | 152 ms: 1.02x slower                                                                 |
| meteor_contest           | 75.9 ms                                                     | 77.9 ms: 1.03x slower                                                                |
| async_generators         | 222 ms                                                      | 227 ms: 1.03x slower                                                                 |
| logging_format           | 6.76 us                                                     | 7.07 us: 1.05x slower                                                                |
| logging_simple           | 6.22 us                                                     | 6.54 us: 1.05x slower                                                                |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.06x slower                                                                |
| xml_etree_generate       | 55.5 ms                                                     | 59.2 ms: 1.07x slower                                                                |
| fannkuch                 | 256 ms                                                      | 282 ms: 1.10x slower                                                                 |
| telco                    | 3.94 ms                                                     | 4.90 ms: 1.24x slower                                                                |
| coverage                 | 39.0 ms                                                     | 49.4 ms: 1.27x slower                                                                |
| python_startup           | 20.6 ms                                                     | 26.4 ms: 1.28x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 20.5 ms: 1.32x slower                                                                |
| bench_mp_pool            | 62.0 ms                                                     | 88.7 ms: 1.43x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 2.03 ms: 1.44x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.24 ms: 1.55x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                                         |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250312-3.14.0a5+-2a08194/bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.217x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown