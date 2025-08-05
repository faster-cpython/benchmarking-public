# Results vs. 3.10.4

- fork: python
- ref: d5fa437dfb50e2e47632
- machine: linux-x86_64
- commit hash: d5fa437
- commit date: 2025-07-26
- overall geometric mean: 1.114x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 324 ms: 1.08x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.13 sec: 1.09x faster                                                      |
| html5lib       | 94.6 ms                                                      | 75.4 ms: 1.25x faster                                                       |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 664 ms: 2.41x faster                                                        |
| async_tree_none         | 692 ms                                                       | 304 ms: 2.28x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 360 ms: 2.28x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 530 ms: 1.77x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.17x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| float          | 111 ms                                                       | 105 ms: 1.06x faster                                                        |
| nbody          | 134 ms                                                       | 184 ms: 1.37x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 159 ms: 1.19x faster                                                        |
| regex_dna      | 261 ms                                                       | 222 ms: 1.18x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 24.7 ms: 1.10x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.44 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                       |
| json_loads           | 30.3 us                                                      | 26.4 us: 1.15x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.12x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 410 us: 1.11x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 109 ms: 1.01x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 75.1 ms: 1.01x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 3.11 sec: 1.07x slower                                                      |
| xml_etree_generate   | 92.3 ms                                                      | 107 ms: 1.16x slower                                                        |
| unpickle_pure_python | 312 us                                                       | 387 us: 1.24x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.81 ms: 1.20x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.3 ms: 1.42x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 24.0 ms: 1.31x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 56.6 ms: 1.12x faster                                                       |
| mako            | 14.7 ms                                                      | 17.1 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.16x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 202 us: 2.66x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 664 ms: 2.41x faster                                                        |
| async_tree_none          | 692 ms                                                       | 304 ms: 2.28x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 360 ms: 2.28x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.47 sec: 2.05x faster                                                      |
| generators               | 57.3 ms                                                      | 30.4 ms: 1.89x faster                                                       |
| logging_silent           | 167 ns                                                       | 92.3 ns: 1.81x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 27.9 us: 1.79x faster                                                       |
| scimark_lu               | 167 ms                                                       | 93.9 ms: 1.78x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 530 ms: 1.77x faster                                                        |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.75x faster                                                        |
| chaos                    | 109 ms                                                       | 62.3 ms: 1.74x faster                                                       |
| pylint                   | 566 ms                                                       | 335 ms: 1.69x faster                                                        |
| deepcopy                 | 468 us                                                       | 283 us: 1.66x faster                                                        |
| richards_super           | 90.6 ms                                                      | 60.2 ms: 1.51x faster                                                       |
| raytrace                 | 489 ms                                                       | 325 ms: 1.51x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.17 us: 1.44x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.77 us: 1.42x faster                                                       |
| django_template          | 50.2 ms                                                      | 35.3 ms: 1.42x faster                                                       |
| richards                 | 75.1 ms                                                      | 54.0 ms: 1.39x faster                                                       |
| thrift                   | 1.18 ms                                                      | 849 us: 1.38x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.92 us: 1.37x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.2 ms: 1.36x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 61.8 ms: 1.31x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 24.0 ms: 1.31x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.9 ms: 1.27x faster                                                       |
| deltablue                | 7.50 ms                                                      | 5.96 ms: 1.26x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 75.4 ms: 1.25x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 89.5 ms: 1.20x faster                                                       |
| go                       | 262 ms                                                       | 219 ms: 1.19x faster                                                        |
| regex_compile            | 190 ms                                                       | 159 ms: 1.19x faster                                                        |
| sympy_sum                | 193 ms                                                       | 163 ms: 1.19x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.8 ms: 1.18x faster                                                       |
| regex_dna                | 261 ms                                                       | 222 ms: 1.18x faster                                                        |
| pyflate                  | 733 ms                                                       | 628 ms: 1.17x faster                                                        |
| json_loads               | 30.3 us                                                      | 26.4 us: 1.15x faster                                                       |
| sympy_str                | 360 ms                                                       | 316 ms: 1.14x faster                                                        |
| nqueens                  | 115 ms                                                       | 101 ms: 1.13x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 106 ms: 1.13x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 142 ms: 1.12x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.49 sec: 1.12x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 56.6 ms: 1.12x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 410 us: 1.11x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 24.7 ms: 1.10x faster                                                       |
| sympy_expand             | 600 ms                                                       | 549 ms: 1.09x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.13 sec: 1.09x faster                                                      |
| json                     | 5.86 ms                                                      | 5.42 ms: 1.08x faster                                                       |
| 2to3                     | 350 ms                                                       | 324 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| float                    | 111 ms                                                       | 105 ms: 1.06x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 381 ms: 1.02x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 109 ms: 1.01x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 75.1 ms: 1.01x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 2.26 sec: 1.05x slower                                                      |
| tomli_loads              | 2.92 sec                                                     | 3.11 sec: 1.07x slower                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 1.12 sec: 1.07x slower                                                      |
| async_generators         | 421 ms                                                       | 455 ms: 1.08x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.44 ms: 1.12x slower                                                       |
| hexiom                   | 9.42 ms                                                      | 10.7 ms: 1.13x slower                                                       |
| comprehensions           | 26.7 us                                                      | 30.3 us: 1.13x slower                                                       |
| meteor_contest           | 138 ms                                                       | 160 ms: 1.16x slower                                                        |
| mako                     | 14.7 ms                                                      | 17.1 ms: 1.16x slower                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 107 ms: 1.16x slower                                                        |
| spectral_norm            | 139 ms                                                       | 167 ms: 1.20x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.81 ms: 1.20x slower                                                       |
| unpickle_pure_python     | 312 us                                                       | 387 us: 1.24x slower                                                        |
| coverage                 | 63.3 ms                                                      | 79.5 ms: 1.26x slower                                                       |
| fannkuch                 | 483 ms                                                       | 618 ms: 1.28x slower                                                        |
| scimark_fft              | 361 ms                                                       | 465 ms: 1.29x slower                                                        |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.33x slower                                                       |
| nbody                    | 134 ms                                                       | 184 ms: 1.37x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.88 ms: 1.63x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 8.41 ms: 1.66x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.48 ms: 1.90x slower                                                       |
| telco                    | 7.23 ms                                                      | 158 ms: 21.89x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.12x faster                                                                |

Benchmark hidden because not significant (1): sqlite_synth
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250726-3.15.0a0-d5fa437-PYTHON_UOPS/bm-20250726-pythonperf2-x86_64-python-d5fa437dfb50e2e47632-3.15.0a0-d5fa437.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.114x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.39x