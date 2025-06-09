# Results vs. 3.10.4

- fork: python
- ref: v3.14.0b2
- machine: windows-amd64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.266x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                            |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                          |
| html5lib       | 51.0 ms                                                     | 38.0 ms: 1.34x faster                                           |
| Geometric mean | (ref)                                                       | 1.20x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 408 ms: 2.72x faster                                            |
| async_tree_memoization  | 526 ms                                                      | 210 ms: 2.51x faster                                            |
| async_tree_none         | 435 ms                                                      | 176 ms: 2.48x faster                                            |
| async_tree_cpu_io_mixed | 638 ms                                                      | 332 ms: 1.92x faster                                            |
| Geometric mean          | (ref)                                                       | 2.39x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                           |
| nbody          | 71.3 ms                                                     | 64.3 ms: 1.11x faster                                           |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                       | 1.16x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.8 ms: 1.30x faster                                           |
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                            |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                           |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                       | 1.13x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.38 ms: 1.44x faster                                           |
| unpickle_pure_python | 183 us                                                      | 136 us: 1.35x faster                                            |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                            |
| tomli_loads          | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                          |
| xml_etree_process    | 44.5 ms                                                     | 39.7 ms: 1.12x faster                                           |
| xml_etree_parse      | 96.8 ms                                                     | 90.4 ms: 1.07x faster                                           |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.2 ms: 1.01x faster                                           |
| xml_etree_generate   | 55.5 ms                                                     | 57.4 ms: 1.03x slower                                           |
| json_loads           | 14.0 us                                                     | 14.8 us: 1.06x slower                                           |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                           |
| python_startup_no_site | 15.5 ms                                                     | 20.1 ms: 1.30x slower                                           |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.71 ms: 1.35x faster                                           |
| genshi_text     | 19.8 ms                                                     | 15.2 ms: 1.30x faster                                           |
| genshi_xml      | 41.0 ms                                                     | 34.5 ms: 1.19x faster                                           |
| django_template | 28.9 ms                                                     | 25.0 ms: 1.16x faster                                           |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.98x faster                                            |
| async_tree_io            | 1.11 sec                                                    | 408 ms: 2.72x faster                                            |
| async_tree_memoization   | 526 ms                                                      | 210 ms: 2.51x faster                                            |
| async_tree_none          | 435 ms                                                      | 176 ms: 2.48x faster                                            |
| pathlib                  | 75.7 ms                                                     | 32.3 ms: 2.34x faster                                           |
| mdp                      | 1.78 sec                                                    | 820 ms: 2.17x faster                                            |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 332 ms: 1.92x faster                                            |
| deltablue                | 4.19 ms                                                     | 2.18 ms: 1.92x faster                                           |
| go                       | 139 ms                                                      | 78.2 ms: 1.78x faster                                           |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                            |
| richards_super           | 52.2 ms                                                     | 31.7 ms: 1.65x faster                                           |
| generators               | 32.4 ms                                                     | 19.9 ms: 1.63x faster                                           |
| chaos                    | 61.7 ms                                                     | 39.0 ms: 1.58x faster                                           |
| deepcopy_memo            | 28.8 us                                                     | 18.3 us: 1.57x faster                                           |
| richards                 | 42.4 ms                                                     | 27.8 ms: 1.53x faster                                           |
| deepcopy                 | 255 us                                                      | 172 us: 1.49x faster                                            |
| raytrace                 | 273 ms                                                      | 187 ms: 1.46x faster                                            |
| pyflate                  | 409 ms                                                      | 281 ms: 1.46x faster                                            |
| json_dumps               | 9.16 ms                                                     | 6.38 ms: 1.44x faster                                           |
| comprehensions           | 16.5 us                                                     | 11.5 us: 1.43x faster                                           |
| scimark_lu               | 85.8 ms                                                     | 60.1 ms: 1.43x faster                                           |
| float                    | 61.7 ms                                                     | 44.3 ms: 1.39x faster                                           |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.4 ms: 1.38x faster                                           |
| scimark_sor              | 106 ms                                                      | 77.5 ms: 1.37x faster                                           |
| hexiom                   | 5.74 ms                                                     | 4.19 ms: 1.37x faster                                           |
| unpickle_pure_python     | 183 us                                                      | 136 us: 1.35x faster                                            |
| mako                     | 9.03 ms                                                     | 6.71 ms: 1.35x faster                                           |
| html5lib                 | 51.0 ms                                                     | 38.0 ms: 1.34x faster                                           |
| crypto_pyaes             | 62.5 ms                                                     | 47.6 ms: 1.31x faster                                           |
| pycparser                | 930 ms                                                      | 716 ms: 1.30x faster                                            |
| genshi_text              | 19.8 ms                                                     | 15.2 ms: 1.30x faster                                           |
| regex_compile            | 106 ms                                                      | 81.8 ms: 1.30x faster                                           |
| spectral_norm            | 77.3 ms                                                     | 60.4 ms: 1.28x faster                                           |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                            |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                           |
| dulwich_log              | 50.5 ms                                                     | 41.8 ms: 1.21x faster                                           |
| sympy_sum                | 107 ms                                                      | 88.8 ms: 1.20x faster                                           |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.20x faster                                           |
| pprint_pformat           | 1.22 sec                                                    | 1.02 sec: 1.19x faster                                          |
| genshi_xml               | 41.0 ms                                                     | 34.5 ms: 1.19x faster                                           |
| deepcopy_reduce          | 2.20 us                                                     | 1.88 us: 1.17x faster                                           |
| tomli_loads              | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                          |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                          |
| pprint_safe_repr         | 592 ms                                                      | 507 ms: 1.17x faster                                            |
| django_template          | 28.9 ms                                                     | 25.0 ms: 1.16x faster                                           |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                           |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                            |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                            |
| xml_etree_process        | 44.5 ms                                                     | 39.7 ms: 1.12x faster                                           |
| nbody                    | 71.3 ms                                                     | 64.3 ms: 1.11x faster                                           |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                            |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                           |
| xml_etree_parse          | 96.8 ms                                                     | 90.4 ms: 1.07x faster                                           |
| nqueens                  | 66.6 ms                                                     | 62.5 ms: 1.07x faster                                           |
| sympy_expand             | 314 ms                                                      | 297 ms: 1.06x faster                                            |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.59 ms: 1.05x faster                                           |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.04x faster                                           |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                           |
| meteor_contest           | 75.9 ms                                                     | 74.1 ms: 1.02x faster                                           |
| scimark_fft              | 187 ms                                                      | 184 ms: 1.02x faster                                            |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.2 ms: 1.01x faster                                           |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                            |
| fannkuch                 | 256 ms                                                      | 259 ms: 1.01x slower                                            |
| logging_format           | 6.76 us                                                     | 6.98 us: 1.03x slower                                           |
| xml_etree_generate       | 55.5 ms                                                     | 57.4 ms: 1.03x slower                                           |
| logging_simple           | 6.22 us                                                     | 6.49 us: 1.04x slower                                           |
| json_loads               | 14.0 us                                                     | 14.8 us: 1.06x slower                                           |
| async_generators         | 222 ms                                                      | 236 ms: 1.07x slower                                            |
| telco                    | 3.94 ms                                                     | 4.61 ms: 1.17x slower                                           |
| python_startup           | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                           |
| coverage                 | 39.0 ms                                                     | 49.5 ms: 1.27x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 20.1 ms: 1.30x slower                                           |
| gc_traversal             | 1.41 ms                                                     | 2.11 ms: 1.50x slower                                           |
| create_gc_cycles         | 800 us                                                      | 1.31 ms: 1.63x slower                                           |
| logging_silent           | 94.6 ns                                                     | 325 ns: 3.43x slower                                            |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                    |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-pythonperf1-amd64-python-v3.14.0b2-3.14.0b2-12d3f88.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.266x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown