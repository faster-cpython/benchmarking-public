# Results vs. 3.10.4

- fork: faster-cpython
- ref: c_recursion_limit
- machine: windows-amd64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.245x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                               |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                             |
| html5lib       | 51.0 ms                                                     | 39.9 ms: 1.28x faster                                                              |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 411 ms: 2.70x faster                                                               |
| async_tree_memoization  | 526 ms                                                      | 224 ms: 2.35x faster                                                               |
| async_tree_none         | 435 ms                                                      | 188 ms: 2.32x faster                                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 344 ms: 1.85x faster                                                               |
| Geometric mean          | (ref)                                                       | 2.29x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.3 ms: 1.36x faster                                                              |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.1 ms: 1.25x faster                                                              |
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                               |
| regex_effbot   | 1.66 ms                                                     | 1.45 ms: 1.15x faster                                                              |
| regex_v8       | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                              |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.64 ms: 1.38x faster                                                              |
| unpickle_pure_python | 183 us                                                      | 145 us: 1.27x faster                                                               |
| pickle_pure_python   | 270 us                                                      | 219 us: 1.23x faster                                                               |
| tomli_loads          | 1.67 sec                                                    | 1.40 sec: 1.20x faster                                                             |
| xml_etree_process    | 44.5 ms                                                     | 40.5 ms: 1.10x faster                                                              |
| xml_etree_parse      | 96.8 ms                                                     | 91.1 ms: 1.06x faster                                                              |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.2 ms: 1.03x faster                                                              |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.02x slower                                                              |
| xml_etree_generate   | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                              |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                                              |
| python_startup         | 20.6 ms                                                     | 24.8 ms: 1.21x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.20x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.66 ms: 1.36x faster                                                              |
| genshi_text     | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                                              |
| genshi_xml      | 41.0 ms                                                     | 35.3 ms: 1.16x faster                                                              |
| django_template | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                              |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 107 us: 3.14x faster                                                               |
| async_tree_io            | 1.11 sec                                                    | 411 ms: 2.70x faster                                                               |
| pathlib                  | 75.7 ms                                                     | 29.1 ms: 2.60x faster                                                              |
| async_tree_memoization   | 526 ms                                                      | 224 ms: 2.35x faster                                                               |
| async_tree_none          | 435 ms                                                      | 188 ms: 2.32x faster                                                               |
| deltablue                | 4.19 ms                                                     | 2.14 ms: 1.95x faster                                                              |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 344 ms: 1.85x faster                                                               |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                               |
| generators               | 32.4 ms                                                     | 19.4 ms: 1.67x faster                                                              |
| go                       | 139 ms                                                      | 85.0 ms: 1.63x faster                                                              |
| logging_silent           | 94.6 ns                                                     | 58.8 ns: 1.61x faster                                                              |
| richards_super           | 52.2 ms                                                     | 33.6 ms: 1.55x faster                                                              |
| comprehensions           | 16.5 us                                                     | 11.0 us: 1.50x faster                                                              |
| chaos                    | 61.7 ms                                                     | 41.5 ms: 1.49x faster                                                              |
| deepcopy_memo            | 28.8 us                                                     | 19.7 us: 1.46x faster                                                              |
| richards                 | 42.4 ms                                                     | 29.2 ms: 1.45x faster                                                              |
| scimark_lu               | 85.8 ms                                                     | 60.3 ms: 1.42x faster                                                              |
| raytrace                 | 273 ms                                                      | 194 ms: 1.41x faster                                                               |
| sqlglot_parse            | 1.22 ms                                                     | 873 us: 1.39x faster                                                               |
| deepcopy                 | 255 us                                                      | 184 us: 1.39x faster                                                               |
| json_dumps               | 9.16 ms                                                     | 6.64 ms: 1.38x faster                                                              |
| sqlglot_transpile        | 1.48 ms                                                     | 1.08 ms: 1.37x faster                                                              |
| float                    | 61.7 ms                                                     | 45.3 ms: 1.36x faster                                                              |
| hexiom                   | 5.74 ms                                                     | 4.22 ms: 1.36x faster                                                              |
| mako                     | 9.03 ms                                                     | 6.66 ms: 1.36x faster                                                              |
| spectral_norm            | 77.3 ms                                                     | 57.6 ms: 1.34x faster                                                              |
| pyflate                  | 409 ms                                                      | 305 ms: 1.34x faster                                                               |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.0 ms: 1.30x faster                                                              |
| crypto_pyaes             | 62.5 ms                                                     | 48.5 ms: 1.29x faster                                                              |
| pycparser                | 930 ms                                                      | 726 ms: 1.28x faster                                                               |
| html5lib                 | 51.0 ms                                                     | 39.9 ms: 1.28x faster                                                              |
| scimark_sor              | 106 ms                                                      | 83.3 ms: 1.27x faster                                                              |
| unpickle_pure_python     | 183 us                                                      | 145 us: 1.27x faster                                                               |
| regex_compile            | 106 ms                                                      | 85.1 ms: 1.25x faster                                                              |
| mdp                      | 1.78 sec                                                    | 1.44 sec: 1.23x faster                                                             |
| pickle_pure_python       | 270 us                                                      | 219 us: 1.23x faster                                                               |
| dulwich_log              | 50.5 ms                                                     | 41.1 ms: 1.23x faster                                                              |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.22x faster                                                              |
| sympy_sum                | 107 ms                                                      | 88.2 ms: 1.21x faster                                                              |
| thrift                   | 617 us                                                      | 514 us: 1.20x faster                                                               |
| genshi_text              | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                                              |
| tomli_loads              | 1.67 sec                                                    | 1.40 sec: 1.20x faster                                                             |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                               |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                              |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                             |
| genshi_xml               | 41.0 ms                                                     | 35.3 ms: 1.16x faster                                                              |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.16x faster                                                              |
| deepcopy_reduce          | 2.20 us                                                     | 1.91 us: 1.15x faster                                                              |
| regex_effbot             | 1.66 ms                                                     | 1.45 ms: 1.15x faster                                                              |
| sqlglot_optimize         | 39.8 ms                                                     | 35.0 ms: 1.14x faster                                                              |
| django_template          | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                              |
| pprint_pformat           | 1.22 sec                                                    | 1.08 sec: 1.13x faster                                                             |
| sympy_str                | 194 ms                                                      | 173 ms: 1.12x faster                                                               |
| bench_thread_pool        | 958 us                                                      | 853 us: 1.12x faster                                                               |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                               |
| pprint_safe_repr         | 592 ms                                                      | 539 ms: 1.10x faster                                                               |
| xml_etree_process        | 44.5 ms                                                     | 40.5 ms: 1.10x faster                                                              |
| json                     | 3.14 ms                                                     | 2.91 ms: 1.08x faster                                                              |
| regex_v8                 | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                              |
| nqueens                  | 66.6 ms                                                     | 62.3 ms: 1.07x faster                                                              |
| sqlglot_normalize        | 205 ms                                                      | 193 ms: 1.06x faster                                                               |
| xml_etree_parse          | 96.8 ms                                                     | 91.1 ms: 1.06x faster                                                              |
| sympy_expand             | 314 ms                                                      | 296 ms: 1.06x faster                                                               |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.59 ms: 1.05x faster                                                              |
| scimark_fft              | 187 ms                                                      | 182 ms: 1.03x faster                                                               |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.2 ms: 1.03x faster                                                              |
| async_generators         | 222 ms                                                      | 218 ms: 1.02x faster                                                               |
| meteor_contest           | 75.9 ms                                                     | 76.4 ms: 1.01x slower                                                              |
| logging_format           | 6.76 us                                                     | 6.81 us: 1.01x slower                                                              |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                                               |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.02x slower                                                              |
| xml_etree_generate       | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                              |
| logging_simple           | 6.22 us                                                     | 6.35 us: 1.02x slower                                                              |
| fannkuch                 | 256 ms                                                      | 278 ms: 1.09x slower                                                               |
| coverage                 | 39.0 ms                                                     | 45.2 ms: 1.16x slower                                                              |
| telco                    | 3.94 ms                                                     | 4.71 ms: 1.20x slower                                                              |
| python_startup_no_site   | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                                              |
| python_startup           | 20.6 ms                                                     | 24.8 ms: 1.21x slower                                                              |
| bench_mp_pool            | 62.0 ms                                                     | 84.4 ms: 1.36x slower                                                              |
| gc_traversal             | 1.41 ms                                                     | 2.01 ms: 1.43x slower                                                              |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.53x slower                                                              |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                       |

Benchmark hidden because not significant (1): nbody
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250217-3.14.0a5+-21366c3/bm-20250217-pythonperf1-amd64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.245x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown