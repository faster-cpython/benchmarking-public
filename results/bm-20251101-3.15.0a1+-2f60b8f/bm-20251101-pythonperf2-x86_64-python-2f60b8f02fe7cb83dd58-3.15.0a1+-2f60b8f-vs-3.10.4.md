# Results vs. 3.10.4

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: linux-x86_64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.359x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 276 ms: 1.27x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.84 sec: 1.20x faster                                                       |
| html5lib       | 94.6 ms                                                      | 64.7 ms: 1.46x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 243 ms: 2.84x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 568 ms: 2.81x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 301 ms: 2.72x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 474 ms: 1.98x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.56x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 64.8 ms: 1.72x faster                                                        |
| nbody          | 134 ms                                                       | 89.7 ms: 1.50x faster                                                        |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.40x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 132 ms: 1.44x faster                                                         |
| regex_dna      | 261 ms                                                       | 222 ms: 1.18x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 23.8 ms: 1.14x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 206 us: 1.52x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 1.97 sec: 1.48x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 10.1 ms: 1.44x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 322 us: 1.41x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 57.4 ms: 1.32x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 86.2 ms: 1.28x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 81.1 ms: 1.14x faster                                                        |
| pickle_dict          | 29.5 us                                                      | 31.8 us: 1.08x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 5.04 us: 1.08x slower                                                        |
| unpickle             | 13.5 us                                                      | 14.8 us: 1.10x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.88 us: 1.19x slower                                                        |
| pickle               | 9.89 us                                                      | 12.3 us: 1.24x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.67 ms: 1.18x slower                                                        |
| python_startup         | 11.5 ms                                                      | 15.0 ms: 1.30x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 34.9 ms: 1.44x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 22.8 ms: 1.38x faster                                                        |
| mako            | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 53.2 ms: 1.19x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.34x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 167 us: 3.21x faster                                                         |
| async_tree_none          | 692 ms                                                       | 243 ms: 2.84x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 568 ms: 2.81x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 301 ms: 2.72x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.12 ms: 2.40x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.25 sec: 2.40x faster                                                       |
| go                       | 262 ms                                                       | 118 ms: 2.22x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 370 ms: 2.11x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 24.9 us: 2.00x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 474 ms: 1.98x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                       |
| chaos                    | 109 ms                                                       | 55.7 ms: 1.95x faster                                                        |
| generators               | 57.3 ms                                                      | 29.8 ms: 1.92x faster                                                        |
| raytrace                 | 489 ms                                                       | 268 ms: 1.83x faster                                                         |
| scimark_sor              | 180 ms                                                       | 98.6 ms: 1.83x faster                                                        |
| scimark_lu               | 167 ms                                                       | 91.6 ms: 1.82x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 59.1 ms: 1.82x faster                                                        |
| pyflate                  | 733 ms                                                       | 405 ms: 1.81x faster                                                         |
| richards_super           | 90.6 ms                                                      | 50.1 ms: 1.81x faster                                                        |
| logging_silent           | 167 ns                                                       | 93.0 ns: 1.80x faster                                                        |
| deepcopy                 | 468 us                                                       | 264 us: 1.77x faster                                                         |
| pylint                   | 566 ms                                                       | 323 ms: 1.75x faster                                                         |
| float                    | 111 ms                                                       | 64.8 ms: 1.72x faster                                                        |
| richards                 | 75.1 ms                                                      | 44.2 ms: 1.70x faster                                                        |
| spectral_norm            | 139 ms                                                       | 82.9 ms: 1.68x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 5.67 ms: 1.66x faster                                                        |
| comprehensions           | 26.7 us                                                      | 16.2 us: 1.65x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 74.9 ms: 1.59x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 206 us: 1.52x faster                                                         |
| logging_simple           | 8.88 us                                                      | 5.90 us: 1.50x faster                                                        |
| nbody                    | 134 ms                                                       | 89.7 ms: 1.50x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.49 us: 1.49x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 1.97 sec: 1.48x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 64.7 ms: 1.46x faster                                                        |
| regex_compile            | 190 ms                                                       | 132 ms: 1.44x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 14.8 ms: 1.44x faster                                                        |
| django_template          | 50.2 ms                                                      | 34.9 ms: 1.44x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.1 ms: 1.44x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 322 us: 1.41x faster                                                         |
| thrift                   | 1.18 ms                                                      | 841 us: 1.40x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 2.90 us: 1.38x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 22.8 ms: 1.38x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 59.0 ms: 1.38x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.57 sec: 1.37x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 771 ms: 1.36x faster                                                         |
| coroutines               | 30.3 ms                                                      | 22.4 ms: 1.35x faster                                                        |
| fannkuch                 | 483 ms                                                       | 358 ms: 1.35x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 57.4 ms: 1.32x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 45.3 ns: 1.32x faster                                                        |
| sympy_sum                | 193 ms                                                       | 149 ms: 1.30x faster                                                         |
| scimark_fft              | 361 ms                                                       | 281 ms: 1.29x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 21.9 ms: 1.28x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 86.2 ms: 1.28x faster                                                        |
| 2to3                     | 350 ms                                                       | 276 ms: 1.27x faster                                                         |
| sympy_str                | 360 ms                                                       | 287 ms: 1.26x faster                                                         |
| nqueens                  | 115 ms                                                       | 91.7 ms: 1.25x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 929 us: 1.23x faster                                                         |
| sympy_expand             | 600 ms                                                       | 490 ms: 1.22x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.84 sec: 1.20x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.20x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 53.2 ms: 1.19x faster                                                        |
| regex_dna                | 261 ms                                                       | 222 ms: 1.18x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| meteor_contest           | 138 ms                                                       | 119 ms: 1.16x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 23.8 ms: 1.14x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 81.1 ms: 1.14x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.49 ms: 1.13x faster                                                        |
| json                     | 5.86 ms                                                      | 5.34 ms: 1.10x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                        |
| async_generators         | 421 ms                                                       | 426 ms: 1.01x slower                                                         |
| asyncio_websockets       | 390 ms                                                       | 409 ms: 1.05x slower                                                         |
| pickle_dict              | 29.5 us                                                      | 31.8 us: 1.08x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.04 us: 1.08x slower                                                        |
| unpickle                 | 13.5 us                                                      | 14.8 us: 1.10x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.67 ms: 1.18x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.88 us: 1.19x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.3 us: 1.24x slower                                                        |
| coverage                 | 63.3 ms                                                      | 79.9 ms: 1.26x slower                                                        |
| python_startup           | 11.5 ms                                                      | 15.0 ms: 1.30x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.86 ms: 1.62x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.14 ms: 1.80x slower                                                        |
| telco                    | 7.23 ms                                                      | 152 ms: 21.05x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 2.57 sec: 402.78x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.25x faster                                                                 |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf2-x86_64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.359x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.39x