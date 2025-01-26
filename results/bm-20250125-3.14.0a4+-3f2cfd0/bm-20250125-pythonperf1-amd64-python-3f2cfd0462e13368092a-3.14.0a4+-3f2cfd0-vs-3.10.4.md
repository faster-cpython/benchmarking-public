# Results vs. 3.10.4

- fork: python
- ref: 3f2cfd0462e13368092a
- machine: windows-amd64
- commit hash: 3f2cfd0
- commit date: 2025-01-25
- overall geometric mean: 1.166x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 232 ms: 1.06x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.5 ms: 1.29x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 434 ms: 2.55x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 233 ms: 2.26x faster                                                        |
| async_tree_none         | 435 ms                                                      | 199 ms: 2.19x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 356 ms: 1.79x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.18x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 51.8 ms: 1.19x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| nbody          | 71.3 ms                                                     | 77.7 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 89.2 ms: 1.19x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                       |
| regex_dna      | 136 ms                                                      | 123 ms: 1.11x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.85 ms: 1.34x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.46 sec: 1.15x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 242 us: 1.12x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 165 us: 1.11x faster                                                        |
| xml_etree_parse      | 96.8 ms                                                     | 89.0 ms: 1.09x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 41.9 ms: 1.06x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.58 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.6 ms: 1.01x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.81 us: 1.04x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.2 us: 1.06x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 59.1 ms: 1.06x slower                                                       |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.07x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.07 us: 1.12x slower                                                       |
| pickle               | 6.85 us                                                     | 8.00 us: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.9 ms: 1.16x slower                                                       |
| python_startup         | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.13 ms: 1.27x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.7 ms: 1.18x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.2 ms: 1.13x faster                                                       |
| django_template | 28.9 ms                                                     | 26.4 ms: 1.10x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.04x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 434 ms: 2.55x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 233 ms: 2.26x faster                                                        |
| async_tree_none          | 435 ms                                                      | 199 ms: 2.19x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 356 ms: 1.79x faster                                                        |
| pylint                   | 350 ms                                                      | 201 ms: 1.74x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.41 ms: 1.74x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.42 sec: 1.49x faster                                                      |
| go                       | 139 ms                                                      | 93.4 ms: 1.49x faster                                                       |
| generators               | 32.4 ms                                                     | 22.0 ms: 1.47x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.1 ms: 1.43x faster                                                       |
| richards_super           | 52.2 ms                                                     | 37.2 ms: 1.41x faster                                                       |
| deepcopy                 | 255 us                                                      | 189 us: 1.35x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.85 ms: 1.34x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.6 us: 1.33x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 71.2 ns: 1.33x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 554 ms: 1.32x faster                                                        |
| raytrace                 | 273 ms                                                      | 207 ms: 1.32x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 921 us: 1.32x faster                                                        |
| comprehensions           | 16.5 us                                                     | 12.7 us: 1.30x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.14 ms: 1.30x faster                                                       |
| richards                 | 42.4 ms                                                     | 32.7 ms: 1.30x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.5 ms: 1.29x faster                                                       |
| pyflate                  | 409 ms                                                      | 318 ms: 1.28x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 49.2 ms: 1.27x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.13 ms: 1.27x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 70.3 ms: 1.22x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.76 ms: 1.21x faster                                                       |
| float                    | 61.7 ms                                                     | 51.8 ms: 1.19x faster                                                       |
| regex_compile            | 106 ms                                                      | 89.2 ms: 1.19x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 65.0 ms: 1.19x faster                                                       |
| thrift                   | 617 us                                                      | 520 us: 1.19x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 42.6 ms: 1.19x faster                                                       |
| pycparser                | 930 ms                                                      | 785 ms: 1.19x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 16.7 ms: 1.18x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                       |
| sympy_sum                | 107 ms                                                      | 91.0 ms: 1.18x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.7 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 834 us: 1.15x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.46 sec: 1.15x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 36.2 ms: 1.13x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                                       |
| scimark_sor              | 106 ms                                                      | 94.0 ms: 1.13x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.58 sec: 1.13x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 242 us: 1.12x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 165 us: 1.11x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.8 ms: 1.11x faster                                                       |
| regex_dna                | 136 ms                                                      | 123 ms: 1.11x faster                                                        |
| django_template          | 28.9 ms                                                     | 26.4 ms: 1.10x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 89.0 ms: 1.09x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.8 ms: 1.08x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.8 ms: 1.08x faster                                                       |
| sympy_str                | 194 ms                                                      | 180 ms: 1.08x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.13 sec: 1.08x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 41.9 ms: 1.06x faster                                                       |
| 2to3                     | 246 ms                                                      | 232 ms: 1.06x faster                                                        |
| unpickle                 | 9.09 us                                                     | 8.58 us: 1.06x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 563 ms: 1.05x faster                                                        |
| json                     | 3.14 ms                                                     | 3.05 ms: 1.03x faster                                                       |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 201 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.68 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.6 ms: 1.01x slower                                                       |
| logging_format           | 6.76 us                                                     | 6.87 us: 1.02x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 77.6 ms: 1.02x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| async_generators         | 222 ms                                                      | 227 ms: 1.02x slower                                                        |
| pathlib                  | 75.7 ms                                                     | 77.7 ms: 1.03x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.81 us: 1.04x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.45 us: 1.04x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.2 us: 1.06x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 59.1 ms: 1.06x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.07x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 42.3 ns: 1.07x slower                                                       |
| scimark_fft              | 187 ms                                                      | 203 ms: 1.08x slower                                                        |
| nbody                    | 71.3 ms                                                     | 77.7 ms: 1.09x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.07 us: 1.12x slower                                                       |
| fannkuch                 | 256 ms                                                      | 286 ms: 1.12x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 17.9 ms: 1.16x slower                                                       |
| pickle                   | 6.85 us                                                     | 8.00 us: 1.17x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.5 ms: 1.24x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.90 ms: 1.24x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.99 ms: 1.41x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 87.7 ms: 1.41x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.53x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (1): nqueens
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250125-3.14.0a4+-3f2cfd0/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.166x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown