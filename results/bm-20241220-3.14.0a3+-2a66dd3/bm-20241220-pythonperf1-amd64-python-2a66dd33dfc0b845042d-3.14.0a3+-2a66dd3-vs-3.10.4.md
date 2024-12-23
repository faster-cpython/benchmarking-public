# Results vs. 3.10.4

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: windows-amd64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.185x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 226 ms: 1.09x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.9 ms: 1.25x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 412 ms: 2.69x faster                                                        |
| async_tree_none         | 435 ms                                                      | 186 ms: 2.34x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 229 ms: 2.30x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 354 ms: 1.80x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.3 ms: 1.12x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| nbody          | 71.3 ms                                                     | 82.0 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 88.7 ms: 1.20x faster                                                       |
| regex_dna      | 136 ms                                                      | 117 ms: 1.17x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.45 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 21.2 ms: 1.37x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.74 ms: 1.36x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 151 us: 1.21x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 228 us: 1.18x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.46 sec: 1.14x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 40.4 ms: 1.10x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 88.3 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.05x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 58.3 ms: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.4 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.78 ms: 1.33x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.7 ms: 1.18x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.0 ms: 1.17x faster                                                       |
| django_template | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.98x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 412 ms: 2.69x faster                                                        |
| async_tree_none          | 435 ms                                                      | 186 ms: 2.34x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 229 ms: 2.30x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.29 ms: 1.83x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 354 ms: 1.80x faster                                                        |
| pylint                   | 350 ms                                                      | 201 ms: 1.75x faster                                                        |
| go                       | 139 ms                                                      | 88.3 ms: 1.57x faster                                                       |
| generators               | 32.4 ms                                                     | 20.6 ms: 1.57x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 62.3 ns: 1.52x faster                                                       |
| richards_super           | 52.2 ms                                                     | 35.6 ms: 1.47x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.6 ms: 1.42x faster                                                       |
| raytrace                 | 273 ms                                                      | 196 ms: 1.40x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 20.8 us: 1.39x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 62.6 ms: 1.37x faster                                                       |
| deepcopy                 | 255 us                                                      | 187 us: 1.37x faster                                                        |
| richards                 | 42.4 ms                                                     | 31.2 ms: 1.36x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.74 ms: 1.36x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 903 us: 1.35x faster                                                        |
| comprehensions           | 16.5 us                                                     | 12.4 us: 1.33x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.78 ms: 1.33x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.32x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.9 ms: 1.30x faster                                                       |
| pyflate                  | 409 ms                                                      | 316 ms: 1.29x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.55 ms: 1.26x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.9 ms: 1.25x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 62.9 ms: 1.23x faster                                                       |
| pycparser                | 930 ms                                                      | 764 ms: 1.22x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 151 us: 1.21x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.6 ms: 1.20x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.1 ms: 1.20x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.20x faster                                                       |
| regex_compile            | 106 ms                                                      | 88.7 ms: 1.20x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.2 ms: 1.19x faster                                                       |
| scimark_sor              | 106 ms                                                      | 89.5 ms: 1.19x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.18x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.7 ms: 1.18x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 228 us: 1.18x faster                                                        |
| thrift                   | 617 us                                                      | 525 us: 1.18x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 35.0 ms: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.17x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.52 sec: 1.17x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 830 us: 1.15x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.91 us: 1.15x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.45 ms: 1.15x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.46 sec: 1.14x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.6 ms: 1.13x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.6 ms: 1.12x faster                                                       |
| float                    | 61.7 ms                                                     | 55.3 ms: 1.12x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 40.4 ms: 1.10x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.3 ms: 1.10x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.4 ms: 1.09x faster                                                       |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                        |
| 2to3                     | 246 ms                                                      | 226 ms: 1.09x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 558 ms: 1.06x faster                                                        |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.62 ms: 1.04x faster                                                       |
| sympy_expand             | 314 ms                                                      | 305 ms: 1.03x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.1 ms: 1.03x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 200 ms: 1.02x faster                                                        |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 66.3 ms: 1.00x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.81 us: 1.01x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 77.8 ms: 1.02x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.42 us: 1.03x slower                                                       |
| scimark_fft              | 187 ms                                                      | 194 ms: 1.04x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.05x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 58.3 ms: 1.05x slower                                                       |
| async_generators         | 222 ms                                                      | 235 ms: 1.06x slower                                                        |
| fannkuch                 | 256 ms                                                      | 282 ms: 1.10x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.4 ms: 1.14x slower                                                       |
| mypy2                    | 555 ms                                                      | 637 ms: 1.15x slower                                                        |
| nbody                    | 71.3 ms                                                     | 82.0 ms: 1.15x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.6 ms: 1.19x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.86 ms: 1.23x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 82.2 ms: 1.33x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 21.2 ms: 1.37x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.98 ms: 1.40x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.51x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.185x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown