# Results vs. 3.10.4

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: windows-amd64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.245x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.73 sec: 1.11x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.6 ms: 1.29x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 403 ms: 2.75x faster                                                        |
| async_tree_none         | 435 ms                                                      | 184 ms: 2.37x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 224 ms: 2.35x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 354 ms: 1.80x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 53.0 ms: 1.35x faster                                                       |
| float          | 61.7 ms                                                     | 45.9 ms: 1.34x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.4 ms: 1.32x faster                                                       |
| regex_dna      | 136 ms                                                      | 113 ms: 1.20x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 20.2 ms: 1.31x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 110 us: 1.66x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 6.41 ms: 1.43x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.20 sec: 1.40x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 85.9 ms: 1.13x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 58.8 ms: 1.11x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.5 ms: 1.10x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.24x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.3 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.13 ms: 1.76x faster                                                       |
| django_template | 28.9 ms                                                     | 27.1 ms: 1.06x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 46.2 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.95x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 403 ms: 2.75x faster                                                        |
| async_tree_none          | 435 ms                                                      | 184 ms: 2.37x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 224 ms: 2.35x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.84x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 354 ms: 1.80x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.13 ms: 1.76x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.8 us: 1.71x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 56.3 ns: 1.68x faster                                                       |
| pylint                   | 350 ms                                                      | 209 ms: 1.68x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 110 us: 1.66x faster                                                        |
| scimark_sor              | 106 ms                                                      | 63.9 ms: 1.66x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 54.7 ms: 1.57x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 49.4 ms: 1.56x faster                                                       |
| go                       | 139 ms                                                      | 89.9 ms: 1.55x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 40.8 ms: 1.53x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.4 ms: 1.53x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.3 ms: 1.49x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 844 us: 1.44x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.41 ms: 1.43x faster                                                       |
| pyflate                  | 409 ms                                                      | 288 ms: 1.42x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.20 sec: 1.40x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.38x faster                                                       |
| generators               | 32.4 ms                                                     | 23.6 ms: 1.37x faster                                                       |
| richards_super           | 52.2 ms                                                     | 38.4 ms: 1.36x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.09 ms: 1.35x faster                                                       |
| nbody                    | 71.3 ms                                                     | 53.0 ms: 1.35x faster                                                       |
| float                    | 61.7 ms                                                     | 45.9 ms: 1.34x faster                                                       |
| deepcopy                 | 255 us                                                      | 191 us: 1.34x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.05 ms: 1.33x faster                                                       |
| regex_compile            | 106 ms                                                      | 80.4 ms: 1.32x faster                                                       |
| scimark_fft              | 187 ms                                                      | 143 ms: 1.31x faster                                                        |
| pycparser                | 930 ms                                                      | 714 ms: 1.30x faster                                                        |
| raytrace                 | 273 ms                                                      | 212 ms: 1.29x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 39.6 ms: 1.29x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                        |
| richards                 | 42.4 ms                                                     | 33.7 ms: 1.26x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.0 ms: 1.23x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 996 ms: 1.22x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                       |
| thrift                   | 617 us                                                      | 512 us: 1.21x faster                                                        |
| regex_dna                | 136 ms                                                      | 113 ms: 1.20x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.20x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 497 ms: 1.19x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.19x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.86 us: 1.18x faster                                                       |
| sympy_sum                | 107 ms                                                      | 91.1 ms: 1.18x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 830 us: 1.15x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 5.06 ms: 1.14x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 85.9 ms: 1.13x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.6 ms: 1.12x faster                                                       |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.73 sec: 1.11x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 58.8 ms: 1.11x faster                                                       |
| sympy_str                | 194 ms                                                      | 177 ms: 1.10x faster                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 50.5 ms: 1.10x faster                                                       |
| json                     | 3.14 ms                                                     | 2.87 ms: 1.09x faster                                                       |
| django_template          | 28.9 ms                                                     | 27.1 ms: 1.06x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 18.7 ms: 1.06x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 37.8 ms: 1.05x faster                                                       |
| fannkuch                 | 256 ms                                                      | 246 ms: 1.04x faster                                                        |
| sympy_expand             | 314 ms                                                      | 303 ms: 1.04x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 74.1 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.88 us: 1.02x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 77.4 ms: 1.02x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.43 us: 1.03x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.05x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.27 ms: 1.08x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 46.2 ms: 1.13x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.3 ms: 1.13x slower                                                       |
| mypy2                    | 555 ms                                                      | 636 ms: 1.15x slower                                                        |
| async_generators         | 222 ms                                                      | 260 ms: 1.17x slower                                                        |
| coverage                 | 39.0 ms                                                     | 47.1 ms: 1.21x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 20.2 ms: 1.31x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 82.7 ms: 1.33x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.96 ms: 1.39x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.52x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                |

Benchmark hidden because not significant (2): nqueens, sqlglot_normalize
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.245x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown