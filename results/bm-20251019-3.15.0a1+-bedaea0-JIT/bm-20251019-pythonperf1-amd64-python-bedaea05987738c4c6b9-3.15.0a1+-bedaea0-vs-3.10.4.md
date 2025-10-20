# Results vs. 3.10.4

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.348x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 217 ms: 1.13x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                      |
| html5lib       | 51.0 ms                                                     | 37.4 ms: 1.36x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 386 ms: 2.87x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 201 ms: 2.61x faster                                                        |
| async_tree_none         | 435 ms                                                      | 172 ms: 2.53x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.94x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.47x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 40.8 ms: 1.51x faster                                                       |
| nbody          | 71.3 ms                                                     | 54.6 ms: 1.31x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.26x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 77.6 ms: 1.37x faster                                                       |
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 13.4 ms: 1.16x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 104 us: 1.76x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 5.51 ms: 1.66x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.09 sec: 1.54x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 198 us: 1.36x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 35.6 ms: 1.25x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 84.9 ms: 1.14x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 49.5 ms: 1.12x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.1 ms: 1.08x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.60 us: 1.06x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.79 us: 1.03x slower                                                       |
| pickle               | 6.85 us                                                     | 7.34 us: 1.07x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 19.3 us: 1.12x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.18 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.16x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                       |
| python_startup         | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.32 ms: 1.70x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                       |
| django_template | 28.9 ms                                                     | 23.8 ms: 1.21x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 34.8 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.32x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.34x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 386 ms: 2.87x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 201 ms: 2.61x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 29.2 ms: 2.60x faster                                                       |
| async_tree_none          | 435 ms                                                      | 172 ms: 2.53x faster                                                        |
| mdp                      | 1.78 sec                                                    | 781 ms: 2.28x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.94x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.18 ms: 1.92x faster                                                       |
| go                       | 139 ms                                                      | 76.4 ms: 1.82x faster                                                       |
| pylint                   | 350 ms                                                      | 193 ms: 1.81x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 104 us: 1.76x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 16.9 us: 1.71x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.7 ms: 1.70x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.32 ms: 1.70x faster                                                       |
| generators               | 32.4 ms                                                     | 19.2 ms: 1.68x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 56.4 ns: 1.68x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.51 ms: 1.66x faster                                                       |
| pyflate                  | 409 ms                                                      | 252 ms: 1.62x faster                                                        |
| richards                 | 42.4 ms                                                     | 27.0 ms: 1.57x faster                                                       |
| deepcopy                 | 255 us                                                      | 163 us: 1.56x faster                                                        |
| comprehensions           | 16.5 us                                                     | 10.7 us: 1.55x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.09 sec: 1.54x faster                                                      |
| raytrace                 | 273 ms                                                      | 179 ms: 1.53x faster                                                        |
| float                    | 61.7 ms                                                     | 40.8 ms: 1.51x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.41 sec: 1.50x faster                                                      |
| chaos                    | 61.7 ms                                                     | 41.1 ms: 1.50x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 57.8 ms: 1.48x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 496 ms: 1.47x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 850 ms: 1.43x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 416 ms: 1.42x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.07 ms: 1.41x faster                                                       |
| scimark_fft              | 187 ms                                                      | 134 ms: 1.40x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 44.8 ms: 1.39x faster                                                       |
| pycparser                | 930 ms                                                      | 670 ms: 1.39x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.3 ms: 1.39x faster                                                       |
| scimark_sor              | 106 ms                                                      | 76.7 ms: 1.38x faster                                                       |
| regex_compile            | 106 ms                                                      | 77.6 ms: 1.37x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 37.4 ms: 1.36x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 198 us: 1.36x faster                                                        |
| nbody                    | 71.3 ms                                                     | 54.6 ms: 1.31x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 39.3 ms: 1.28x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.16 ms: 1.26x faster                                                       |
| sympy_sum                | 107 ms                                                      | 85.2 ms: 1.26x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.6 ms: 1.25x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.53 us: 1.25x faster                                                       |
| thrift                   | 617 us                                                      | 495 us: 1.25x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 63.0 ms: 1.23x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.23x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                       |
| django_template          | 28.9 ms                                                     | 23.8 ms: 1.21x faster                                                       |
| fannkuch                 | 256 ms                                                      | 211 ms: 1.21x faster                                                        |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.8 ms: 1.18x faster                                                       |
| sympy_str                | 194 ms                                                      | 166 ms: 1.17x faster                                                        |
| unpack_sequence          | 39.6 ns                                                     | 34.2 ns: 1.16x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.4 ms: 1.16x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 84.9 ms: 1.14x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 841 us: 1.14x faster                                                        |
| 2to3                     | 246 ms                                                      | 217 ms: 1.13x faster                                                        |
| coroutines               | 16.0 ms                                                     | 14.2 ms: 1.13x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 49.5 ms: 1.12x faster                                                       |
| json                     | 3.14 ms                                                     | 2.83 ms: 1.11x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 60.4 ms: 1.10x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                                       |
| sympy_expand             | 314 ms                                                      | 289 ms: 1.09x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.1 ms: 1.08x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 71.8 ms: 1.06x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.60 us: 1.06x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.58 us: 1.03x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| telco                    | 3.94 ms                                                     | 3.88 ms: 1.02x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.13 us: 1.01x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.79 us: 1.03x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.34 us: 1.07x slower                                                       |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                        |
| pickle_dict              | 17.2 us                                                     | 19.3 us: 1.12x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.18 us: 1.16x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                       |
| coverage                 | 39.0 ms                                                     | 51.3 ms: 1.32x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.5 ms: 1.43x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.09 ms: 1.48x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.56x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.31x faster                                                                |

Benchmark hidden because not significant (1): json_loads
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.348x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: unknown