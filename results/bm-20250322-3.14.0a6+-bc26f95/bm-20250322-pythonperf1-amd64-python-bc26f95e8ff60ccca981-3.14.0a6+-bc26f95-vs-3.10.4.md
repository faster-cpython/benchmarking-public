# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: windows-amd64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.208x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 226 ms: 1.09x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                      |
| html5lib       | 51.0 ms                                                     | 41.0 ms: 1.24x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 430 ms: 2.58x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 220 ms: 2.39x faster                                                        |
| async_tree_none         | 435 ms                                                      | 189 ms: 2.30x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 338 ms: 1.89x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.27x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.4 ms: 1.33x faster                                                       |
| nbody          | 71.3 ms                                                     | 67.3 ms: 1.06x faster                                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 87.3 ms: 1.21x faster                                                       |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.0 ms: 1.11x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.92 ms: 1.32x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 150 us: 1.22x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 227 us: 1.19x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.51 sec: 1.11x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 89.7 ms: 1.08x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.42 us: 1.08x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 42.1 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.0 ms: 1.01x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.75 us: 1.01x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 58.6 ms: 1.05x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.0 us: 1.07x slower                                                       |
| pickle               | 6.85 us                                                     | 8.11 us: 1.18x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 20.8 us: 1.21x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.52 us: 1.28x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.3 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.84 ms: 1.32x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                       |
| django_template | 28.9 ms                                                     | 26.9 ms: 1.08x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 38.4 ms: 1.07x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.06x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 430 ms: 2.58x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 220 ms: 2.39x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.7 ms: 2.31x faster                                                       |
| async_tree_none          | 435 ms                                                      | 189 ms: 2.30x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 338 ms: 1.89x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.30 ms: 1.82x faster                                                       |
| pylint                   | 350 ms                                                      | 204 ms: 1.72x faster                                                        |
| generators               | 32.4 ms                                                     | 19.7 ms: 1.65x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 60.4 ns: 1.57x faster                                                       |
| go                       | 139 ms                                                      | 89.9 ms: 1.55x faster                                                       |
| richards_super           | 52.2 ms                                                     | 35.0 ms: 1.49x faster                                                       |
| chaos                    | 61.7 ms                                                     | 42.3 ms: 1.46x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.46 sec: 1.45x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 20.0 us: 1.44x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 61.2 ms: 1.40x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 526 ms: 1.39x faster                                                        |
| richards                 | 42.4 ms                                                     | 30.7 ms: 1.38x faster                                                       |
| deepcopy                 | 255 us                                                      | 186 us: 1.37x faster                                                        |
| raytrace                 | 273 ms                                                      | 200 ms: 1.37x faster                                                        |
| comprehensions           | 16.5 us                                                     | 12.2 us: 1.35x faster                                                       |
| float                    | 61.7 ms                                                     | 46.4 ms: 1.33x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.92 ms: 1.32x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.84 ms: 1.32x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 59.3 ms: 1.30x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.44 ms: 1.29x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.4 ms: 1.29x faster                                                       |
| scimark_sor              | 106 ms                                                      | 82.4 ms: 1.29x faster                                                       |
| pyflate                  | 409 ms                                                      | 318 ms: 1.29x faster                                                        |
| pycparser                | 930 ms                                                      | 745 ms: 1.25x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 41.0 ms: 1.24x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 50.3 ms: 1.24x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 150 us: 1.22x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                       |
| regex_compile            | 106 ms                                                      | 87.3 ms: 1.21x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.4 ms: 1.19x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 227 us: 1.19x faster                                                        |
| sympy_sum                | 107 ms                                                      | 90.7 ms: 1.18x faster                                                       |
| thrift                   | 617 us                                                      | 524 us: 1.18x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.15x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                      |
| mdp                      | 1.78 sec                                                    | 1.57 sec: 1.13x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.96 us: 1.12x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.51 sec: 1.11x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.0 ms: 1.11x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 871 us: 1.10x faster                                                        |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                        |
| 2to3                     | 246 ms                                                      | 226 ms: 1.09x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 89.7 ms: 1.08x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.42 us: 1.08x faster                                                       |
| django_template          | 28.9 ms                                                     | 26.9 ms: 1.08x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 554 ms: 1.07x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 38.4 ms: 1.07x faster                                                       |
| nbody                    | 71.3 ms                                                     | 67.3 ms: 1.06x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 42.1 ms: 1.06x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 37.7 ns: 1.05x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.62 ms: 1.04x faster                                                       |
| scimark_fft              | 187 ms                                                      | 181 ms: 1.03x faster                                                        |
| json                     | 3.14 ms                                                     | 3.03 ms: 1.03x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 64.5 ms: 1.03x faster                                                       |
| sympy_expand             | 314 ms                                                      | 309 ms: 1.02x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.0 ms: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| unpickle_list            | 2.71 us                                                     | 2.75 us: 1.01x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 78.3 ms: 1.03x slower                                                       |
| async_generators         | 222 ms                                                      | 230 ms: 1.04x slower                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 58.6 ms: 1.05x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.0 us: 1.07x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.22 us: 1.07x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.71 us: 1.08x slower                                                       |
| fannkuch                 | 256 ms                                                      | 282 ms: 1.10x slower                                                        |
| pickle                   | 6.85 us                                                     | 8.11 us: 1.18x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 20.8 us: 1.21x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.82 ms: 1.22x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                                       |
| coverage                 | 39.0 ms                                                     | 49.8 ms: 1.28x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.52 us: 1.28x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.3 ms: 1.31x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.8 ms: 1.43x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.08 ms: 1.47x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.56x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                                |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf1-amd64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.208x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown