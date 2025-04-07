# Results vs. 3.10.4

- fork: python
- ref: 85bc489b649fe261f962
- machine: windows-amd64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.294x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 408 ms: 2.72x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 204 ms: 2.58x faster                                                        |
| async_tree_none         | 435 ms                                                      | 179 ms: 2.43x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.39x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.3 ms: 1.42x faster                                                       |
| nbody          | 71.3 ms                                                     | 57.0 ms: 1.25x faster                                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.6 ms: 1.32x faster                                                       |
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 119 us: 1.54x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.19 sec: 1.40x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 6.76 ms: 1.36x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 208 us: 1.30x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.9 ms: 1.21x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 51.4 ms: 1.08x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 92.1 ms: 1.05x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.70 us: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.2 ms: 1.03x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.78 us: 1.03x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.2 us: 1.08x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 19.5 us: 1.13x slower                                                       |
| pickle               | 6.85 us                                                     | 8.18 us: 1.19x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.39 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.3 ms: 1.28x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.5 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.67 ms: 1.59x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.3 ms: 1.16x faster                                                       |
| django_template | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.29x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.01x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 408 ms: 2.72x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 204 ms: 2.58x faster                                                        |
| async_tree_none          | 435 ms                                                      | 179 ms: 2.43x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.3 ms: 2.34x faster                                                       |
| mdp                      | 1.78 sec                                                    | 797 ms: 2.23x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.16 ms: 1.94x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                        |
| go                       | 139 ms                                                      | 80.3 ms: 1.73x faster                                                       |
| pylint                   | 350 ms                                                      | 203 ms: 1.73x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 55.0 ns: 1.72x faster                                                       |
| generators               | 32.4 ms                                                     | 19.2 ms: 1.68x faster                                                       |
| richards_super           | 52.2 ms                                                     | 31.5 ms: 1.66x faster                                                       |
| raytrace                 | 273 ms                                                      | 171 ms: 1.60x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.67 ms: 1.59x faster                                                       |
| chaos                    | 61.7 ms                                                     | 39.0 ms: 1.58x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.4 us: 1.57x faster                                                       |
| pyflate                  | 409 ms                                                      | 262 ms: 1.56x faster                                                        |
| richards                 | 42.4 ms                                                     | 27.4 ms: 1.55x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 119 us: 1.54x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 58.3 ms: 1.47x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.46 sec: 1.45x faster                                                      |
| deepcopy                 | 255 us                                                      | 177 us: 1.45x faster                                                        |
| scimark_sor              | 106 ms                                                      | 74.2 ms: 1.43x faster                                                       |
| float                    | 61.7 ms                                                     | 43.3 ms: 1.42x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 517 ms: 1.42x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.5 ms: 1.41x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.19 sec: 1.40x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.12 ms: 1.39x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.0 us: 1.38x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 56.5 ms: 1.37x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 45.8 ms: 1.37x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.76 ms: 1.36x faster                                                       |
| regex_compile            | 106 ms                                                      | 80.6 ms: 1.32x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                                       |
| pycparser                | 930 ms                                                      | 715 ms: 1.30x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 208 us: 1.30x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.29x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 963 ms: 1.27x faster                                                        |
| nbody                    | 71.3 ms                                                     | 57.0 ms: 1.25x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 482 ms: 1.23x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 36.9 ms: 1.21x faster                                                       |
| scimark_fft              | 187 ms                                                      | 157 ms: 1.20x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.9 ms: 1.19x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.7 ms: 1.18x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.32 ms: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.1 ms: 1.17x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 35.3 ms: 1.16x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.2 ms: 1.12x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 855 us: 1.12x faster                                                        |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                                        |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 60.8 ms: 1.10x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.08x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 51.4 ms: 1.08x faster                                                       |
| fannkuch                 | 256 ms                                                      | 238 ms: 1.07x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 92.1 ms: 1.05x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 37.9 ns: 1.05x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.70 us: 1.04x faster                                                       |
| sympy_expand             | 314 ms                                                      | 305 ms: 1.03x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.2 ms: 1.03x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 74.5 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| unpickle_list            | 2.71 us                                                     | 2.78 us: 1.03x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.2 us: 1.08x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.35 ms: 1.10x slower                                                       |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                        |
| pickle_dict              | 17.2 us                                                     | 19.5 us: 1.13x slower                                                       |
| pickle                   | 6.85 us                                                     | 8.18 us: 1.19x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.39 us: 1.23x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.3 ms: 1.28x slower                                                       |
| coverage                 | 39.0 ms                                                     | 51.1 ms: 1.31x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.5 ms: 1.32x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.3 ms: 1.42x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.09 ms: 1.48x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.24 ms: 1.55x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                                |

Benchmark hidden because not significant (3): logging_format, logging_simple, json
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250405-3.14.0a6+-85bc489-JIT/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.294x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown