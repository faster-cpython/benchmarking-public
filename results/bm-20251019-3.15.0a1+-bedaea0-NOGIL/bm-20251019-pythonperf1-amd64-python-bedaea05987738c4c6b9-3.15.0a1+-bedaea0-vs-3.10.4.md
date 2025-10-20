# Results vs. 3.10.4

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.185x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                        |
| docutils       | 1.92 sec                                                    | 2.82 sec: 1.47x slower                                                      |
| html5lib       | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 344 ms: 3.22x faster                                                        |
| async_tree_none         | 435 ms                                                      | 169 ms: 2.58x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.56x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 324 ms: 1.97x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.54x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.2 ms: 1.34x faster                                                       |
| pidigits       | 149 ms                                                      | 136 ms: 1.09x faster                                                        |
| nbody          | 71.3 ms                                                     | 76.7 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 112 ms: 1.22x faster                                                        |
| regex_compile  | 106 ms                                                      | 89.8 ms: 1.18x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.97 ms: 1.53x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 223 us: 1.21x faster                                                        |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.9 ms: 1.08x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 92.8 ms: 1.04x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 43.2 ms: 1.03x faster                                                       |
| pickle_list          | 2.75 us                                                     | 3.03 us: 1.10x slower                                                       |
| unpickle             | 9.09 us                                                     | 10.1 us: 1.11x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 3.02 us: 1.11x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 61.9 ms: 1.12x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.9 us: 1.14x slower                                                       |
| pickle               | 6.85 us                                                     | 7.82 us: 1.14x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 20.3 us: 1.18x slower                                                       |
| tomli_loads          | 1.67 sec                                                    | 2.32 sec: 1.39x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                       |
| python_startup         | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 37.7 ms: 1.09x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.3 ms: 1.08x faster                                                       |
| mako            | 9.03 ms                                                     | 10.1 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.04x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 344 ms: 3.22x faster                                                        |
| typing_runtime_protocols | 336 us                                                      | 126 us: 2.67x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 28.8 ms: 2.63x faster                                                       |
| async_tree_none          | 435 ms                                                      | 169 ms: 2.58x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.56x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 324 ms: 1.97x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.35 ms: 1.78x faster                                                       |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.05 sec: 1.69x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 449 ms: 1.63x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 59.9 ns: 1.58x faster                                                       |
| go                       | 139 ms                                                      | 89.4 ms: 1.55x faster                                                       |
| generators               | 32.4 ms                                                     | 21.0 ms: 1.54x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.6 us: 1.54x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.97 ms: 1.53x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.5 us: 1.43x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.34 us: 1.42x faster                                                       |
| deepcopy                 | 255 us                                                      | 183 us: 1.39x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 63.0 ms: 1.36x faster                                                       |
| richards_super           | 52.2 ms                                                     | 38.5 ms: 1.36x faster                                                       |
| chaos                    | 61.7 ms                                                     | 45.6 ms: 1.35x faster                                                       |
| float                    | 61.7 ms                                                     | 46.2 ms: 1.34x faster                                                       |
| pyflate                  | 409 ms                                                      | 307 ms: 1.33x faster                                                        |
| pycparser                | 930 ms                                                      | 702 ms: 1.33x faster                                                        |
| raytrace                 | 273 ms                                                      | 208 ms: 1.32x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.39 ms: 1.31x faster                                                       |
| richards                 | 42.4 ms                                                     | 32.9 ms: 1.29x faster                                                       |
| scimark_sor              | 106 ms                                                      | 83.3 ms: 1.27x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.8 ms: 1.24x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                        |
| regex_dna                | 136 ms                                                      | 112 ms: 1.22x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 223 us: 1.21x faster                                                        |
| regex_compile            | 106 ms                                                      | 89.8 ms: 1.18x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.16x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.4 ms: 1.16x faster                                                       |
| sympy_sum                | 107 ms                                                      | 94.7 ms: 1.13x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.96 us: 1.12x faster                                                       |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 56.3 ms: 1.11x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.8 ms: 1.11x faster                                                       |
| django_template          | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 536 ms: 1.10x faster                                                        |
| thrift                   | 617 us                                                      | 563 us: 1.10x faster                                                        |
| pidigits                 | 149 ms                                                      | 136 ms: 1.09x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 70.8 ms: 1.09x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 37.7 ms: 1.09x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.9 ms: 1.08x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 36.7 ns: 1.08x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 18.3 ms: 1.08x faster                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.31 ms: 1.08x faster                                                       |
| sympy_str                | 194 ms                                                      | 185 ms: 1.05x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.05x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.8 ms: 1.04x faster                                                       |
| json                     | 3.14 ms                                                     | 3.03 ms: 1.03x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 43.2 ms: 1.03x faster                                                       |
| scimark_fft              | 187 ms                                                      | 187 ms: 1.00x faster                                                        |
| logging_format           | 6.76 us                                                     | 7.04 us: 1.04x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.53 us: 1.05x slower                                                       |
| bench_thread_pool        | 958 us                                                      | 1.02 ms: 1.06x slower                                                       |
| nqueens                  | 66.6 ms                                                     | 71.4 ms: 1.07x slower                                                       |
| nbody                    | 71.3 ms                                                     | 76.7 ms: 1.08x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.03 us: 1.10x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.00 ms: 1.10x slower                                                       |
| unpickle                 | 9.09 us                                                     | 10.1 us: 1.11x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 3.02 us: 1.11x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 61.9 ms: 1.12x slower                                                       |
| mako                     | 9.03 ms                                                     | 10.1 ms: 1.12x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 85.1 ms: 1.12x slower                                                       |
| async_generators         | 222 ms                                                      | 252 ms: 1.14x slower                                                        |
| json_loads               | 14.0 us                                                     | 15.9 us: 1.14x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.82 us: 1.14x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 20.3 us: 1.18x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 74.2 ms: 1.20x slower                                                       |
| fannkuch                 | 256 ms                                                      | 310 ms: 1.21x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                                       |
| telco                    | 3.94 ms                                                     | 5.02 ms: 1.27x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.03 ms: 1.29x slower                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.62 sec: 1.33x slower                                                      |
| tomli_loads              | 1.67 sec                                                    | 2.32 sec: 1.39x slower                                                      |
| docutils                 | 1.92 sec                                                    | 2.82 sec: 1.47x slower                                                      |
| coverage                 | 39.0 ms                                                     | 67.1 ms: 1.72x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                                |

Benchmark hidden because not significant (2): sympy_expand, asyncio_tcp_ssl
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251019-3.15.0a1+-bedaea0-NOGIL/bm-20251019-pythonperf1-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.185x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown