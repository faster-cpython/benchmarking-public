# Results vs. 3.10.4

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.314x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 216 ms: 1.14x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.58 sec: 1.21x faster                                                      |
| html5lib       | 51.0 ms                                                     | 37.2 ms: 1.37x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 387 ms: 2.87x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 202 ms: 2.61x faster                                                        |
| async_tree_none         | 435 ms                                                      | 173 ms: 2.51x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.94x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.46x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                                       |
| nbody          | 71.3 ms                                                     | 62.9 ms: 1.13x faster                                                       |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.8 ms: 1.35x faster                                                       |
| regex_dna      | 136 ms                                                      | 122 ms: 1.12x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.44 ms: 1.69x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 133 us: 1.38x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 206 us: 1.31x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.32 sec: 1.27x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.0 ms: 1.14x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 86.3 ms: 1.12x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.54 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.6 ms: 1.05x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.89 us: 1.07x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 19.3 us: 1.12x slower                                                       |
| pickle               | 6.85 us                                                     | 7.76 us: 1.13x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.20 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                       |
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.63 ms: 1.36x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                       |
| django_template | 28.9 ms                                                     | 23.0 ms: 1.25x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 33.4 ms: 1.23x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.29x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.22x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 387 ms: 2.87x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 28.5 ms: 2.65x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 202 ms: 2.61x faster                                                        |
| async_tree_none          | 435 ms                                                      | 173 ms: 2.51x faster                                                        |
| mdp                      | 1.78 sec                                                    | 813 ms: 2.19x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.94x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.16 ms: 1.94x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 387 ms: 1.89x faster                                                        |
| go                       | 139 ms                                                      | 75.7 ms: 1.84x faster                                                       |
| pylint                   | 350 ms                                                      | 193 ms: 1.82x faster                                                        |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.3 ns: 1.71x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.9 us: 1.70x faster                                                       |
| generators               | 32.4 ms                                                     | 19.2 ms: 1.69x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.44 ms: 1.69x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.25 sec: 1.68x faster                                                      |
| richards                 | 42.4 ms                                                     | 26.6 ms: 1.60x faster                                                       |
| chaos                    | 61.7 ms                                                     | 38.9 ms: 1.59x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 54.6 ms: 1.57x faster                                                       |
| deepcopy                 | 255 us                                                      | 163 us: 1.56x faster                                                        |
| raytrace                 | 273 ms                                                      | 177 ms: 1.54x faster                                                        |
| comprehensions           | 16.5 us                                                     | 10.8 us: 1.53x faster                                                       |
| pyflate                  | 409 ms                                                      | 276 ms: 1.48x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.7 ms: 1.44x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.99 ms: 1.44x faster                                                       |
| scimark_sor              | 106 ms                                                      | 75.9 ms: 1.40x faster                                                       |
| float                    | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 133 us: 1.38x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 37.2 ms: 1.37x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.63 ms: 1.36x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 46.4 ms: 1.35x faster                                                       |
| regex_compile            | 106 ms                                                      | 78.8 ms: 1.35x faster                                                       |
| pycparser                | 930 ms                                                      | 693 ms: 1.34x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 206 us: 1.31x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 39.0 ms: 1.29x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.32 sec: 1.27x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 61.1 ms: 1.27x faster                                                       |
| sympy_sum                | 107 ms                                                      | 84.7 ms: 1.26x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.1 ms: 1.26x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.75 us: 1.26x faster                                                       |
| django_template          | 28.9 ms                                                     | 23.0 ms: 1.25x faster                                                       |
| thrift                   | 617 us                                                      | 494 us: 1.25x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.54 us: 1.24x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 33.4 ms: 1.23x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 995 ms: 1.23x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 489 ms: 1.21x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.58 sec: 1.21x faster                                                      |
| sympy_str                | 194 ms                                                      | 165 ms: 1.18x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 824 us: 1.16x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 39.0 ms: 1.14x faster                                                       |
| 2to3                     | 246 ms                                                      | 216 ms: 1.14x faster                                                        |
| sympy_expand             | 314 ms                                                      | 276 ms: 1.14x faster                                                        |
| nbody                    | 71.3 ms                                                     | 62.9 ms: 1.13x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 86.3 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.44 ms: 1.12x faster                                                       |
| regex_dna                | 136 ms                                                      | 122 ms: 1.12x faster                                                        |
| scimark_fft              | 187 ms                                                      | 168 ms: 1.12x faster                                                        |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.0 ms: 1.10x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 60.5 ms: 1.10x faster                                                       |
| json                     | 3.14 ms                                                     | 2.89 ms: 1.08x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 70.7 ms: 1.07x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.54 us: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.56 ms: 1.06x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.39 us: 1.06x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.6 ms: 1.05x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.91 us: 1.05x faster                                                       |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| fannkuch                 | 256 ms                                                      | 258 ms: 1.01x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 40.2 ns: 1.01x slower                                                       |
| async_generators         | 222 ms                                                      | 234 ms: 1.05x slower                                                        |
| unpickle_list            | 2.71 us                                                     | 2.89 us: 1.07x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.23 ms: 1.07x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 19.3 us: 1.12x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.76 us: 1.13x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.20 us: 1.16x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.4 ms: 1.24x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.4 ms: 1.42x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.06 ms: 1.46x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.27 ms: 1.59x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.28x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_generate
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.314x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown