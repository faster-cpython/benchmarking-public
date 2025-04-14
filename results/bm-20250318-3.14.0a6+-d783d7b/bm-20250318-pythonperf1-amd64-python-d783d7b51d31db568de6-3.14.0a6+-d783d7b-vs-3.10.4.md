# Results vs. 3.10.4

- fork: python
- ref: d783d7b51d31db568de6
- machine: windows-amd64
- commit hash: d783d7b
- commit date: 2025-03-18
- overall geometric mean: 1.209x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                      |
| html5lib       | 51.0 ms                                                     | 41.3 ms: 1.23x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 429 ms: 2.58x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 224 ms: 2.34x faster                                                        |
| async_tree_none         | 435 ms                                                      | 190 ms: 2.29x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 346 ms: 1.84x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.25x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.5 ms: 1.33x faster                                                       |
| nbody          | 71.3 ms                                                     | 67.0 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 89.0 ms: 1.19x faster                                                       |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.45 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.93 ms: 1.32x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 152 us: 1.21x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 228 us: 1.18x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.7 ms: 1.09x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 42.1 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 59.2 ms: 1.07x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.2 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.4 ms: 1.28x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.4 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.73 ms: 1.34x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.4 ms: 1.14x faster                                                       |
| django_template | 28.9 ms                                                     | 26.7 ms: 1.08x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 38.5 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.03x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 429 ms: 2.58x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 224 ms: 2.34x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.7 ms: 2.32x faster                                                       |
| async_tree_none          | 435 ms                                                      | 190 ms: 2.29x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.27 ms: 1.84x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 346 ms: 1.84x faster                                                        |
| pylint                   | 350 ms                                                      | 203 ms: 1.72x faster                                                        |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.66x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 58.9 ns: 1.61x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.3 ms: 1.57x faster                                                       |
| go                       | 139 ms                                                      | 90.4 ms: 1.54x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 19.1 us: 1.50x faster                                                       |
| richards                 | 42.4 ms                                                     | 29.3 ms: 1.45x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.4 ms: 1.42x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 60.9 ms: 1.41x faster                                                       |
| raytrace                 | 273 ms                                                      | 199 ms: 1.38x faster                                                        |
| deepcopy                 | 255 us                                                      | 187 us: 1.37x faster                                                        |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.37x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 57.2 ms: 1.35x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.73 ms: 1.34x faster                                                       |
| float                    | 61.7 ms                                                     | 46.5 ms: 1.33x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.93 ms: 1.32x faster                                                       |
| pyflate                  | 409 ms                                                      | 314 ms: 1.30x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.1 ms: 1.30x faster                                                       |
| scimark_sor              | 106 ms                                                      | 81.9 ms: 1.30x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.46 ms: 1.29x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 49.3 ms: 1.27x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 41.3 ms: 1.23x faster                                                       |
| pycparser                | 930 ms                                                      | 754 ms: 1.23x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 152 us: 1.21x faster                                                        |
| regex_compile            | 106 ms                                                      | 89.0 ms: 1.19x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 228 us: 1.18x faster                                                        |
| thrift                   | 617 us                                                      | 522 us: 1.18x faster                                                        |
| sympy_sum                | 107 ms                                                      | 91.0 ms: 1.18x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.18x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                      |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 43.5 ms: 1.16x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.65 us: 1.16x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.45 ms: 1.15x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.4 ms: 1.14x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.10 sec: 1.10x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 2.00 us: 1.10x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.62 sec: 1.10x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 878 us: 1.09x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 88.7 ms: 1.09x faster                                                       |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 545 ms: 1.09x faster                                                        |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                        |
| django_template          | 28.9 ms                                                     | 26.7 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.53 ms: 1.08x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 38.5 ms: 1.06x faster                                                       |
| nbody                    | 71.3 ms                                                     | 67.0 ms: 1.06x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 42.1 ms: 1.06x faster                                                       |
| json                     | 3.14 ms                                                     | 3.06 ms: 1.03x faster                                                       |
| sympy_expand             | 314 ms                                                      | 307 ms: 1.02x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 65.2 ms: 1.02x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                                       |
| scimark_fft              | 187 ms                                                      | 184 ms: 1.02x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 76.9 ms: 1.01x slower                                                       |
| async_generators         | 222 ms                                                      | 229 ms: 1.03x slower                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 59.2 ms: 1.07x slower                                                       |
| fannkuch                 | 256 ms                                                      | 273 ms: 1.07x slower                                                        |
| json_loads               | 14.0 us                                                     | 15.2 us: 1.08x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.36 us: 1.09x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.82 us: 1.10x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.4 ms: 1.24x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.96 ms: 1.26x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.4 ms: 1.28x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.4 ms: 1.32x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.8 ms: 1.43x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.06 ms: 1.46x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.56x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250318-3.14.0a6+-d783d7b/bm-20250318-pythonperf1-amd64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.209x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown