# Results vs. 3.10.4

- fork: python
- ref: 85bc489b649fe261f962
- machine: windows-amd64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.297x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.2 ms: 1.34x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 404 ms: 2.75x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 203 ms: 2.59x faster                                                        |
| async_tree_none         | 435 ms                                                      | 179 ms: 2.44x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 328 ms: 1.95x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.41x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.2 ms: 1.46x faster                                                       |
| nbody          | 71.3 ms                                                     | 62.6 ms: 1.14x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.4 ms: 1.34x faster                                                       |
| regex_dna      | 136 ms                                                      | 118 ms: 1.15x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.49 ms: 1.41x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 134 us: 1.37x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 207 us: 1.30x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.33 sec: 1.26x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.53 us: 1.07x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.77 us: 1.02x slower                                                       |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 21.0 us: 1.22x slower                                                       |
| pickle               | 6.85 us                                                     | 8.57 us: 1.25x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.59 us: 1.30x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.6 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.47 ms: 1.40x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 33.1 ms: 1.24x faster                                                       |
| django_template | 28.9 ms                                                     | 25.0 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.23x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 404 ms: 2.75x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 203 ms: 2.59x faster                                                        |
| async_tree_none          | 435 ms                                                      | 179 ms: 2.44x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.0 ms: 2.37x faster                                                       |
| mdp                      | 1.78 sec                                                    | 793 ms: 2.25x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.13 ms: 1.96x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 328 ms: 1.95x faster                                                        |
| go                       | 139 ms                                                      | 76.3 ms: 1.82x faster                                                       |
| pylint                   | 350 ms                                                      | 196 ms: 1.79x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 55.0 ns: 1.72x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.9 ms: 1.69x faster                                                       |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                       |
| chaos                    | 61.7 ms                                                     | 38.7 ms: 1.60x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.1 us: 1.59x faster                                                       |
| raytrace                 | 273 ms                                                      | 173 ms: 1.58x faster                                                        |
| richards                 | 42.4 ms                                                     | 27.2 ms: 1.56x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.2 ms: 1.50x faster                                                       |
| deepcopy                 | 255 us                                                      | 171 us: 1.49x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 57.5 ms: 1.49x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.3 us: 1.46x faster                                                       |
| float                    | 61.7 ms                                                     | 42.2 ms: 1.46x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.45 sec: 1.46x faster                                                      |
| pyflate                  | 409 ms                                                      | 282 ms: 1.45x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 3.96 ms: 1.45x faster                                                       |
| scimark_sor              | 106 ms                                                      | 73.8 ms: 1.44x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 515 ms: 1.42x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.49 ms: 1.41x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.47 ms: 1.40x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 55.5 ms: 1.39x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 134 us: 1.37x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 46.0 ms: 1.36x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.2 ms: 1.34x faster                                                       |
| regex_compile            | 106 ms                                                      | 79.4 ms: 1.34x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                       |
| pycparser                | 930 ms                                                      | 709 ms: 1.31x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 207 us: 1.30x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.33 sec: 1.26x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 33.1 ms: 1.24x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.79 us: 1.23x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 487 ms: 1.22x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.01 sec: 1.21x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.8 ms: 1.21x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.9 ms: 1.20x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.19x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                      |
| django_template          | 28.9 ms                                                     | 25.0 ms: 1.16x faster                                                       |
| regex_dna                | 136 ms                                                      | 118 ms: 1.15x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.45 ms: 1.14x faster                                                       |
| sympy_str                | 194 ms                                                      | 170 ms: 1.14x faster                                                        |
| nbody                    | 71.3 ms                                                     | 62.6 ms: 1.14x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.1 ms: 1.14x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 850 us: 1.13x faster                                                        |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.44 ms: 1.12x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 60.5 ms: 1.10x faster                                                       |
| scimark_fft              | 187 ms                                                      | 171 ms: 1.10x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.3 ms: 1.08x faster                                                       |
| sympy_expand             | 314 ms                                                      | 291 ms: 1.08x faster                                                        |
| unpack_sequence          | 39.6 ns                                                     | 36.7 ns: 1.08x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.53 us: 1.07x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 73.7 ms: 1.03x faster                                                       |
| fannkuch                 | 256 ms                                                      | 250 ms: 1.02x faster                                                        |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| async_generators         | 222 ms                                                      | 224 ms: 1.01x slower                                                        |
| unpickle_list            | 2.71 us                                                     | 2.77 us: 1.02x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.62 ms: 1.17x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 21.0 us: 1.22x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.6 ms: 1.25x slower                                                       |
| pickle                   | 6.85 us                                                     | 8.57 us: 1.25x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.59 us: 1.30x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.6 ms: 1.33x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.3 ms: 1.42x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.04 ms: 1.45x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.24 ms: 1.56x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                                |

Benchmark hidden because not significant (4): xml_etree_generate, logging_format, logging_simple, json
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250405-3.14.0a6+-85bc489/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.297x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown