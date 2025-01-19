# Results vs. 3.10.4

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: windows-amd64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.146x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 237 ms: 1.04x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                      |
| html5lib       | 51.0 ms                                                     | 41.1 ms: 1.24x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 432 ms: 2.56x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 236 ms: 2.23x faster                                                        |
| async_tree_none         | 435 ms                                                      | 196 ms: 2.22x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 356 ms: 1.79x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.18x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 53.1 ms: 1.16x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| nbody          | 71.3 ms                                                     | 80.9 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 117 ms: 1.17x faster                                                        |
| regex_compile  | 106 ms                                                      | 93.6 ms: 1.13x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.53 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 7.00 ms: 1.31x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 240 us: 1.13x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.49 sec: 1.12x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 164 us: 1.12x faster                                                        |
| xml_etree_parse      | 96.8 ms                                                     | 88.8 ms: 1.09x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.47 us: 1.07x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 45.3 ms: 1.02x slower                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 66.2 ms: 1.02x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.77 us: 1.02x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.0 us: 1.05x slower                                                       |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.06x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.06 us: 1.11x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 63.3 ms: 1.14x slower                                                       |
| pickle               | 6.85 us                                                     | 7.91 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                       |
| python_startup         | 20.6 ms                                                     | 24.2 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.26 ms: 1.24x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.0 ms: 1.17x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.5 ms: 1.13x faster                                                       |
| django_template | 28.9 ms                                                     | 27.3 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 117 us: 2.87x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 432 ms: 2.56x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 236 ms: 2.23x faster                                                        |
| async_tree_none          | 435 ms                                                      | 196 ms: 2.22x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 356 ms: 1.79x faster                                                        |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.58 ms: 1.63x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.43 sec: 1.48x faster                                                      |
| go                       | 139 ms                                                      | 96.0 ms: 1.45x faster                                                       |
| chaos                    | 61.7 ms                                                     | 44.1 ms: 1.40x faster                                                       |
| richards_super           | 52.2 ms                                                     | 37.8 ms: 1.38x faster                                                       |
| generators               | 32.4 ms                                                     | 23.5 ms: 1.38x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 556 ms: 1.32x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 7.00 ms: 1.31x faster                                                       |
| deepcopy                 | 255 us                                                      | 196 us: 1.31x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 946 us: 1.28x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 22.5 us: 1.28x faster                                                       |
| richards                 | 42.4 ms                                                     | 33.3 ms: 1.27x faster                                                       |
| raytrace                 | 273 ms                                                      | 215 ms: 1.27x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.16 ms: 1.27x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 75.3 ns: 1.26x faster                                                       |
| comprehensions           | 16.5 us                                                     | 13.1 us: 1.26x faster                                                       |
| pyflate                  | 409 ms                                                      | 326 ms: 1.26x faster                                                        |
| mako                     | 9.03 ms                                                     | 7.26 ms: 1.24x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 69.0 ms: 1.24x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 41.1 ms: 1.24x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 50.7 ms: 1.23x faster                                                       |
| pycparser                | 930 ms                                                      | 764 ms: 1.22x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 64.1 ms: 1.21x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 91.2 ms: 1.17x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.0 ms: 1.17x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.92 ms: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.17x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 43.4 ms: 1.16x faster                                                       |
| float                    | 61.7 ms                                                     | 53.1 ms: 1.16x faster                                                       |
| thrift                   | 617 us                                                      | 538 us: 1.15x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.9 ms: 1.15x faster                                                       |
| regex_compile            | 106 ms                                                      | 93.6 ms: 1.13x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.5 ms: 1.13x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 240 us: 1.13x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 852 us: 1.12x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.49 sec: 1.12x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 164 us: 1.12x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.8 ms: 1.11x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 88.8 ms: 1.09x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.53 ms: 1.09x faster                                                       |
| scimark_sor              | 106 ms                                                      | 98.3 ms: 1.08x faster                                                       |
| sympy_str                | 194 ms                                                      | 181 ms: 1.08x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.65 sec: 1.08x faster                                                      |
| unpickle                 | 9.09 us                                                     | 8.47 us: 1.07x faster                                                       |
| django_template          | 28.9 ms                                                     | 27.3 ms: 1.06x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 37.6 ms: 1.06x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.15 sec: 1.06x faster                                                      |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                       |
| 2to3                     | 246 ms                                                      | 237 ms: 1.04x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 573 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.66 ms: 1.02x faster                                                       |
| sympy_expand             | 314 ms                                                      | 309 ms: 1.02x faster                                                        |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 204 ms: 1.01x faster                                                        |
| coroutines               | 16.0 ms                                                     | 16.2 ms: 1.01x slower                                                       |
| xml_etree_process        | 44.5 ms                                                     | 45.3 ms: 1.02x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 66.2 ms: 1.02x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.77 us: 1.02x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 77.9 ms: 1.03x slower                                                       |
| nqueens                  | 66.6 ms                                                     | 68.7 ms: 1.03x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 78.1 ms: 1.03x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 41.4 ns: 1.04x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.0 us: 1.05x slower                                                       |
| scimark_fft              | 187 ms                                                      | 197 ms: 1.05x slower                                                        |
| logging_format           | 6.76 us                                                     | 7.12 us: 1.05x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.06x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.61 us: 1.06x slower                                                       |
| async_generators         | 222 ms                                                      | 237 ms: 1.07x slower                                                        |
| pickle_list              | 2.75 us                                                     | 3.06 us: 1.11x slower                                                       |
| fannkuch                 | 256 ms                                                      | 288 ms: 1.13x slower                                                        |
| nbody                    | 71.3 ms                                                     | 80.9 ms: 1.13x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 63.3 ms: 1.14x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.91 us: 1.15x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.2 ms: 1.17x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.84 ms: 1.23x slower                                                       |
| coverage                 | 39.0 ms                                                     | 49.7 ms: 1.27x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.97 ms: 1.40x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.2 ms: 1.42x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.20 ms: 1.50x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250118-3.14.0a4+-61b35f7/bm-20250118-pythonperf1-amd64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.146x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown