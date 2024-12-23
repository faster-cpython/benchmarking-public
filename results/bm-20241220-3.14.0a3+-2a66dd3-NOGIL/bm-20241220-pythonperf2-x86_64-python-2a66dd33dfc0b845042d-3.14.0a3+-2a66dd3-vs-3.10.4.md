# Results vs. 3.10.4

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-x86_64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.037x faster
- HPT reliability: 97.14%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.52x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 386 ms: 1.10x slower                                                         |
| docutils       | 3.41 sec                                                     | 3.12 sec: 1.09x faster                                                       |
| html5lib       | 94.6 ms                                                      | 93.1 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 783 ms: 2.04x faster                                                         |
| async_tree_none         | 692 ms                                                       | 360 ms: 1.92x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 445 ms: 1.84x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 610 ms: 1.54x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.82x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 247 ms: 1.10x faster                                                         |
| nbody          | 134 ms                                                       | 129 ms: 1.04x faster                                                         |
| float          | 111 ms                                                       | 108 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 173 ms: 1.10x faster                                                         |
| regex_dna      | 261 ms                                                       | 242 ms: 1.08x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.29 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 110 ms                                                       | 92.5 ms: 1.19x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 134 ms: 1.19x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.62 sec: 1.11x faster                                                       |
| json_loads           | 30.3 us                                                      | 27.6 us: 1.10x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 14.3 ms: 1.02x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 75.7 ms: 1.00x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 321 us: 1.03x slower                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 99.6 ms: 1.08x slower                                                        |
| pickle_pure_python   | 455 us                                                       | 506 us: 1.11x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 12.2 ms: 1.66x slower                                                        |
| python_startup         | 11.5 ms                                                      | 19.6 ms: 1.71x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.68x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 31.4 ms                                                      | 33.6 ms: 1.07x slower                                                        |
| django_template | 50.2 ms                                                      | 53.9 ms: 1.07x slower                                                        |
| genshi_xml      | 63.3 ms                                                      | 69.4 ms: 1.10x slower                                                        |
| mako            | 14.7 ms                                                      | 19.6 ms: 1.33x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.14x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 224 us: 2.39x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 783 ms: 2.04x faster                                                         |
| async_tree_none          | 692 ms                                                       | 360 ms: 1.92x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 445 ms: 1.84x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 610 ms: 1.54x faster                                                         |
| generators               | 57.3 ms                                                      | 38.6 ms: 1.49x faster                                                        |
| pylint                   | 566 ms                                                       | 386 ms: 1.47x faster                                                         |
| deepcopy                 | 468 us                                                       | 343 us: 1.37x faster                                                         |
| spectral_norm            | 139 ms                                                       | 102 ms: 1.36x faster                                                         |
| coroutines               | 30.3 ms                                                      | 23.1 ms: 1.31x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 39.4 us: 1.26x faster                                                        |
| scimark_lu               | 167 ms                                                       | 135 ms: 1.23x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 17.3 ms: 1.23x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 98.6 ms: 1.21x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 92.5 ms: 1.19x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 134 ms: 1.19x faster                                                         |
| richards_super           | 90.6 ms                                                      | 78.9 ms: 1.15x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.46 sec: 1.15x faster                                                       |
| chaos                    | 109 ms                                                       | 95.2 ms: 1.14x faster                                                        |
| pyflate                  | 733 ms                                                       | 646 ms: 1.13x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.67 us: 1.12x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.62 sec: 1.11x faster                                                       |
| json_loads               | 30.3 us                                                      | 27.6 us: 1.10x faster                                                        |
| pidigits                 | 271 ms                                                       | 247 ms: 1.10x faster                                                         |
| regex_compile            | 190 ms                                                       | 173 ms: 1.10x faster                                                         |
| docutils                 | 3.41 sec                                                     | 3.12 sec: 1.09x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.70 us: 1.08x faster                                                        |
| regex_dna                | 261 ms                                                       | 242 ms: 1.08x faster                                                         |
| go                       | 262 ms                                                       | 244 ms: 1.07x faster                                                         |
| json                     | 5.86 ms                                                      | 5.47 ms: 1.07x faster                                                        |
| thrift                   | 1.18 ms                                                      | 1.11 ms: 1.06x faster                                                        |
| scimark_fft              | 361 ms                                                       | 341 ms: 1.06x faster                                                         |
| richards                 | 75.1 ms                                                      | 71.3 ms: 1.05x faster                                                        |
| deltablue                | 7.50 ms                                                      | 7.15 ms: 1.05x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.88 sec: 1.04x faster                                                       |
| nbody                    | 134 ms                                                       | 129 ms: 1.04x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 78.4 ms: 1.03x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 378 ms: 1.03x faster                                                         |
| nqueens                  | 115 ms                                                       | 111 ms: 1.03x faster                                                         |
| logging_silent           | 167 ns                                                       | 162 ns: 1.03x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 26.4 ms: 1.03x faster                                                        |
| float                    | 111 ms                                                       | 108 ms: 1.02x faster                                                         |
| raytrace                 | 489 ms                                                       | 480 ms: 1.02x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 14.3 ms: 1.02x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 93.1 ms: 1.02x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 1.03 sec: 1.02x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 9.31 ms: 1.01x faster                                                        |
| logging_simple           | 8.88 us                                                      | 8.79 us: 1.01x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 107 ms: 1.00x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 75.7 ms: 1.00x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 2.17 sec: 1.01x slower                                                       |
| logging_format           | 9.64 us                                                      | 9.71 us: 1.01x slower                                                        |
| sqlglot_normalize        | 144 ms                                                       | 146 ms: 1.01x slower                                                         |
| comprehensions           | 26.7 us                                                      | 27.1 us: 1.02x slower                                                        |
| fannkuch                 | 483 ms                                                       | 497 ms: 1.03x slower                                                         |
| unpickle_pure_python     | 312 us                                                       | 321 us: 1.03x slower                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 72.5 ms: 1.03x slower                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 2.82 ms: 1.05x slower                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 2.37 ms: 1.06x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.29 ms: 1.07x slower                                                        |
| genshi_text              | 31.4 ms                                                      | 33.6 ms: 1.07x slower                                                        |
| sympy_integrate          | 28.2 ms                                                      | 30.2 ms: 1.07x slower                                                        |
| django_template          | 50.2 ms                                                      | 53.9 ms: 1.07x slower                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 204 ms: 1.08x slower                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 99.6 ms: 1.08x slower                                                        |
| scimark_sor              | 180 ms                                                       | 195 ms: 1.08x slower                                                         |
| genshi_xml               | 63.3 ms                                                      | 69.4 ms: 1.10x slower                                                        |
| 2to3                     | 350 ms                                                       | 386 ms: 1.10x slower                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.60 ms: 1.10x slower                                                        |
| pickle_pure_python       | 455 us                                                       | 506 us: 1.11x slower                                                         |
| sympy_str                | 360 ms                                                       | 403 ms: 1.12x slower                                                         |
| gc_traversal             | 3.42 ms                                                      | 3.87 ms: 1.13x slower                                                        |
| meteor_contest           | 138 ms                                                       | 158 ms: 1.14x slower                                                         |
| sympy_expand             | 600 ms                                                       | 734 ms: 1.22x slower                                                         |
| async_generators         | 421 ms                                                       | 515 ms: 1.22x slower                                                         |
| sympy_sum                | 193 ms                                                       | 240 ms: 1.25x slower                                                         |
| telco                    | 7.23 ms                                                      | 9.42 ms: 1.30x slower                                                        |
| mako                     | 14.7 ms                                                      | 19.6 ms: 1.33x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.55 ms: 1.36x slower                                                        |
| mypy2                    | 933 ms                                                       | 1.31 sec: 1.40x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.68 ms: 1.52x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 12.2 ms: 1.66x slower                                                        |
| coverage                 | 63.3 ms                                                      | 108 ms: 1.71x slower                                                         |
| python_startup           | 11.5 ms                                                      | 19.6 ms: 1.71x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 53.7 ms: 8.42x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241220-3.14.0a3+-2a66dd3-NOGIL/bm-20241220-pythonperf2-x86_64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 97.14% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.52x