# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: windows-amd64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.230x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 229 ms: 1.08x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.75 sec: 1.10x faster                                                      |
| html5lib       | 51.0 ms                                                     | 41.2 ms: 1.24x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 417 ms: 2.66x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 221 ms: 2.38x faster                                                        |
| async_tree_none         | 435 ms                                                      | 188 ms: 2.32x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 336 ms: 1.90x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 48.3 ms: 1.28x faster                                                       |
| nbody          | 71.3 ms                                                     | 59.7 ms: 1.19x faster                                                       |
| pidigits       | 149 ms                                                      | 149 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.5 ms: 1.23x faster                                                       |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 123 us: 1.49x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.23 sec: 1.36x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 7.04 ms: 1.30x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 217 us: 1.24x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 38.3 ms: 1.16x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.0 ms: 1.09x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.60 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.4 ms: 1.04x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 54.2 ms: 1.02x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.89 us: 1.06x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.1 us: 1.08x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 19.8 us: 1.16x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.38 us: 1.23x slower                                                       |
| pickle               | 6.85 us                                                     | 8.49 us: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.88 ms: 1.54x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.4 ms: 1.14x faster                                                       |
| django_template | 28.9 ms                                                     | 26.6 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.93x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 417 ms: 2.66x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 221 ms: 2.38x faster                                                        |
| async_tree_none          | 435 ms                                                      | 188 ms: 2.32x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 33.1 ms: 2.29x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 336 ms: 1.90x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.41 ms: 1.74x faster                                                       |
| pylint                   | 350 ms                                                      | 207 ms: 1.69x faster                                                        |
| generators               | 32.4 ms                                                     | 20.1 ms: 1.61x faster                                                       |
| go                       | 139 ms                                                      | 89.2 ms: 1.56x faster                                                       |
| richards_super           | 52.2 ms                                                     | 33.9 ms: 1.54x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.88 ms: 1.54x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 61.8 ns: 1.53x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 123 us: 1.49x faster                                                        |
| pyflate                  | 409 ms                                                      | 276 ms: 1.48x faster                                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.45 sec: 1.46x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.0 us: 1.44x faster                                                       |
| richards                 | 42.4 ms                                                     | 29.8 ms: 1.42x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 60.5 ms: 1.42x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 518 ms: 1.41x faster                                                        |
| chaos                    | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                       |
| raytrace                 | 273 ms                                                      | 199 ms: 1.37x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.23 sec: 1.36x faster                                                      |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                        |
| scimark_sor              | 106 ms                                                      | 80.6 ms: 1.32x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.9 ms: 1.30x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 7.04 ms: 1.30x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 60.2 ms: 1.28x faster                                                       |
| float                    | 61.7 ms                                                     | 48.3 ms: 1.28x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 49.5 ms: 1.26x faster                                                       |
| pycparser                | 930 ms                                                      | 746 ms: 1.25x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 217 us: 1.24x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.54 us: 1.24x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 41.2 ms: 1.24x faster                                                       |
| regex_compile            | 106 ms                                                      | 86.5 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.27 ms: 1.20x faster                                                       |
| nbody                    | 71.3 ms                                                     | 59.7 ms: 1.19x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.82 ms: 1.19x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.18x faster                                                      |
| scimark_fft              | 187 ms                                                      | 158 ms: 1.18x faster                                                        |
| thrift                   | 617 us                                                      | 525 us: 1.17x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.04 sec: 1.17x faster                                                      |
| sympy_sum                | 107 ms                                                      | 91.8 ms: 1.17x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 38.3 ms: 1.16x faster                                                       |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.9 ms: 1.15x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.4 ms: 1.14x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 520 ms: 1.14x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.8 ms: 1.12x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.75 sec: 1.10x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 875 us: 1.09x faster                                                        |
| unpack_sequence          | 39.6 ns                                                     | 36.4 ns: 1.09x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 89.0 ms: 1.09x faster                                                       |
| django_template          | 28.9 ms                                                     | 26.6 ms: 1.08x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.04 us: 1.08x faster                                                       |
| 2to3                     | 246 ms                                                      | 229 ms: 1.08x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 62.3 ms: 1.07x faster                                                       |
| sympy_str                | 194 ms                                                      | 182 ms: 1.07x faster                                                        |
| unpickle                 | 9.09 us                                                     | 8.60 us: 1.06x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.4 ms: 1.04x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 54.2 ms: 1.02x faster                                                       |
| json                     | 3.14 ms                                                     | 3.08 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 149 ms: 1.00x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 76.3 ms: 1.01x slower                                                       |
| sympy_expand             | 314 ms                                                      | 322 ms: 1.02x slower                                                        |
| logging_format           | 6.76 us                                                     | 7.18 us: 1.06x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.61 us: 1.06x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.89 us: 1.06x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.1 us: 1.08x slower                                                       |
| async_generators         | 222 ms                                                      | 249 ms: 1.12x slower                                                        |
| pickle_dict              | 17.2 us                                                     | 19.8 us: 1.16x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.63 ms: 1.17x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.38 us: 1.23x slower                                                       |
| pickle                   | 6.85 us                                                     | 8.49 us: 1.24x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                       |
| coverage                 | 39.0 ms                                                     | 50.4 ms: 1.29x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.7 ms: 1.43x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.04 ms: 1.45x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.24 ms: 1.55x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (2): fannkuch, genshi_xml
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.230x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown