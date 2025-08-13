# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: 6a85f95
- commit date: 2025-08-13
- overall geometric mean: 1.354x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 217 ms: 1.13x faster                                                               |
| docutils       | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                             |
| html5lib       | 51.0 ms                                                     | 37.8 ms: 1.35x faster                                                              |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 379 ms: 2.92x faster                                                               |
| async_tree_memoization  | 526 ms                                                      | 199 ms: 2.65x faster                                                               |
| async_tree_none         | 435 ms                                                      | 172 ms: 2.53x faster                                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.94x faster                                                               |
| Geometric mean          | (ref)                                                       | 2.48x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 43.5 ms: 1.64x faster                                                              |
| float          | 61.7 ms                                                     | 43.0 ms: 1.44x faster                                                              |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                               |
| Geometric mean | (ref)                                                       | 1.34x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.8 ms: 1.36x faster                                                              |
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                               |
| regex_v8       | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                              |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                              |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 104 us: 1.76x faster                                                               |
| json_dumps           | 9.16 ms                                                     | 5.40 ms: 1.70x faster                                                              |
| tomli_loads          | 1.67 sec                                                    | 1.07 sec: 1.56x faster                                                             |
| pickle_pure_python   | 270 us                                                      | 201 us: 1.34x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 34.7 ms: 1.28x faster                                                              |
| xml_etree_parse      | 96.8 ms                                                     | 86.7 ms: 1.12x faster                                                              |
| xml_etree_generate   | 55.5 ms                                                     | 50.1 ms: 1.11x faster                                                              |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                              |
| json_loads           | 14.0 us                                                     | 13.9 us: 1.01x faster                                                              |
| Geometric mean       | (ref)                                                       | 1.29x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                              |
| python_startup_no_site | 15.5 ms                                                     | 19.0 ms: 1.22x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.38 ms: 1.68x faster                                                              |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                              |
| genshi_xml      | 41.0 ms                                                     | 33.9 ms: 1.21x faster                                                              |
| django_template | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                              |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.33x faster                                                               |
| async_tree_io            | 1.11 sec                                                    | 379 ms: 2.92x faster                                                               |
| async_tree_memoization   | 526 ms                                                      | 199 ms: 2.65x faster                                                               |
| pathlib                  | 75.7 ms                                                     | 28.6 ms: 2.65x faster                                                              |
| async_tree_none          | 435 ms                                                      | 172 ms: 2.53x faster                                                               |
| mdp                      | 1.78 sec                                                    | 773 ms: 2.30x faster                                                               |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.94x faster                                                               |
| deltablue                | 4.19 ms                                                     | 2.26 ms: 1.85x faster                                                              |
| pylint                   | 350 ms                                                      | 192 ms: 1.83x faster                                                               |
| go                       | 139 ms                                                      | 76.1 ms: 1.83x faster                                                              |
| logging_silent           | 94.6 ns                                                     | 53.9 ns: 1.76x faster                                                              |
| unpickle_pure_python     | 183 us                                                      | 104 us: 1.76x faster                                                               |
| richards_super           | 52.2 ms                                                     | 30.4 ms: 1.72x faster                                                              |
| json_dumps               | 9.16 ms                                                     | 5.40 ms: 1.70x faster                                                              |
| mako                     | 9.03 ms                                                     | 5.38 ms: 1.68x faster                                                              |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.66x faster                                                              |
| nbody                    | 71.3 ms                                                     | 43.5 ms: 1.64x faster                                                              |
| deepcopy_memo            | 28.8 us                                                     | 17.9 us: 1.61x faster                                                              |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.60x faster                                                              |
| pyflate                  | 409 ms                                                      | 257 ms: 1.59x faster                                                               |
| richards                 | 42.4 ms                                                     | 26.9 ms: 1.58x faster                                                              |
| raytrace                 | 273 ms                                                      | 176 ms: 1.56x faster                                                               |
| tomli_loads              | 1.67 sec                                                    | 1.07 sec: 1.56x faster                                                             |
| chaos                    | 61.7 ms                                                     | 39.8 ms: 1.55x faster                                                              |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                               |
| scimark_lu               | 85.8 ms                                                     | 57.4 ms: 1.49x faster                                                              |
| crypto_pyaes             | 62.5 ms                                                     | 43.5 ms: 1.44x faster                                                              |
| float                    | 61.7 ms                                                     | 43.0 ms: 1.44x faster                                                              |
| hexiom                   | 5.74 ms                                                     | 4.05 ms: 1.42x faster                                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.6 ms: 1.41x faster                                                              |
| scimark_sor              | 106 ms                                                      | 75.4 ms: 1.41x faster                                                              |
| pprint_pformat           | 1.22 sec                                                    | 867 ms: 1.41x faster                                                               |
| pycparser                | 930 ms                                                      | 666 ms: 1.40x faster                                                               |
| pprint_safe_repr         | 592 ms                                                      | 430 ms: 1.38x faster                                                               |
| regex_compile            | 106 ms                                                      | 77.8 ms: 1.36x faster                                                              |
| html5lib                 | 51.0 ms                                                     | 37.8 ms: 1.35x faster                                                              |
| pickle_pure_python       | 270 us                                                      | 201 us: 1.34x faster                                                               |
| dulwich_log              | 50.5 ms                                                     | 38.5 ms: 1.31x faster                                                              |
| scimark_fft              | 187 ms                                                      | 145 ms: 1.29x faster                                                               |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                              |
| xml_etree_process        | 44.5 ms                                                     | 34.7 ms: 1.28x faster                                                              |
| fannkuch                 | 256 ms                                                      | 200 ms: 1.28x faster                                                               |
| spectral_norm            | 77.3 ms                                                     | 60.9 ms: 1.27x faster                                                              |
| thrift                   | 617 us                                                      | 490 us: 1.26x faster                                                               |
| sqlite_synth             | 1.91 us                                                     | 1.52 us: 1.25x faster                                                              |
| sympy_sum                | 107 ms                                                      | 85.9 ms: 1.25x faster                                                              |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.23x faster                                                              |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.22x faster                                                              |
| genshi_xml               | 41.0 ms                                                     | 33.9 ms: 1.21x faster                                                              |
| django_template          | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                              |
| docutils                 | 1.92 sec                                                    | 1.60 sec: 1.20x faster                                                             |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                               |
| regex_v8                 | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                              |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.31 ms: 1.18x faster                                                              |
| sympy_str                | 194 ms                                                      | 166 ms: 1.17x faster                                                               |
| nqueens                  | 66.6 ms                                                     | 58.6 ms: 1.14x faster                                                              |
| 2to3                     | 246 ms                                                      | 217 ms: 1.13x faster                                                               |
| xml_etree_parse          | 96.8 ms                                                     | 86.7 ms: 1.12x faster                                                              |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                              |
| xml_etree_generate       | 55.5 ms                                                     | 50.1 ms: 1.11x faster                                                              |
| meteor_contest           | 75.9 ms                                                     | 69.0 ms: 1.10x faster                                                              |
| sympy_expand             | 314 ms                                                      | 288 ms: 1.09x faster                                                               |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.07x faster                                                              |
| json                     | 3.14 ms                                                     | 2.96 ms: 1.06x faster                                                              |
| logging_simple           | 6.22 us                                                     | 5.98 us: 1.04x faster                                                              |
| logging_format           | 6.76 us                                                     | 6.52 us: 1.04x faster                                                              |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                               |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                              |
| json_loads               | 14.0 us                                                     | 13.9 us: 1.01x faster                                                              |
| telco                    | 3.94 ms                                                     | 4.24 ms: 1.08x slower                                                              |
| async_generators         | 222 ms                                                      | 246 ms: 1.11x slower                                                               |
| python_startup           | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                              |
| python_startup_no_site   | 15.5 ms                                                     | 19.0 ms: 1.22x slower                                                              |
| coverage                 | 39.0 ms                                                     | 49.2 ms: 1.26x slower                                                              |
| gc_traversal             | 1.41 ms                                                     | 2.07 ms: 1.47x slower                                                              |
| create_gc_cycles         | 800 us                                                      | 1.27 ms: 1.59x slower                                                              |
| Geometric mean           | (ref)                                                       | 1.35x faster                                                                       |
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250813-3.15.0a0-6a85f95-JIT/bm-20250813-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.354x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: unknown