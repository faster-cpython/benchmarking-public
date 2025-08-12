# Results vs. 3.10.4

- fork: python
- ref: af15e1d13ea26575afbb
- machine: linux-x86_64
- commit hash: af15e1d
- commit date: 2025-08-09
- overall geometric mean: 1.340x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.9 ms: 1.41x faster                                                       |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 623 ms: 2.57x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 330 ms: 2.48x faster                                                        |
| async_tree_none         | 692 ms                                                       | 281 ms: 2.46x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 504 ms: 1.86x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 64.2 ms: 1.73x faster                                                       |
| nbody          | 134 ms                                                       | 99.6 ms: 1.35x faster                                                       |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 132 ms: 1.44x faster                                                        |
| regex_dna      | 261 ms                                                       | 226 ms: 1.15x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 24.2 ms: 1.12x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.60 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 193 us: 1.62x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.90 sec: 1.53x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.1 ms: 1.44x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 327 us: 1.39x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 55.8 ms: 1.36x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 139 ms: 1.16x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 80.8 ms: 1.14x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 97.9 ms: 1.13x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.81 ms: 1.20x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.72 ms: 1.51x faster                                                       |
| django_template | 50.2 ms                                                      | 34.7 ms: 1.45x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 56.9 ms: 1.11x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.35x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.15x faster                                                        |
| deltablue                | 7.50 ms                                                      | 2.89 ms: 2.60x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 623 ms: 2.57x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 330 ms: 2.48x faster                                                        |
| async_tree_none          | 692 ms                                                       | 281 ms: 2.46x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.28 sec: 2.35x faster                                                      |
| richards_super           | 90.6 ms                                                      | 40.2 ms: 2.25x faster                                                       |
| richards                 | 75.1 ms                                                      | 34.2 ms: 2.20x faster                                                       |
| go                       | 262 ms                                                       | 126 ms: 2.08x faster                                                        |
| generators               | 57.3 ms                                                      | 29.7 ms: 1.93x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 504 ms: 1.86x faster                                                        |
| chaos                    | 109 ms                                                       | 58.9 ms: 1.84x faster                                                       |
| logging_silent           | 167 ns                                                       | 91.9 ns: 1.82x faster                                                       |
| pyflate                  | 733 ms                                                       | 406 ms: 1.81x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 27.7 us: 1.80x faster                                                       |
| scimark_sor              | 180 ms                                                       | 101 ms: 1.78x faster                                                        |
| scimark_lu               | 167 ms                                                       | 93.9 ms: 1.78x faster                                                       |
| pylint                   | 566 ms                                                       | 320 ms: 1.77x faster                                                        |
| spectral_norm            | 139 ms                                                       | 78.8 ms: 1.77x faster                                                       |
| raytrace                 | 489 ms                                                       | 282 ms: 1.74x faster                                                        |
| float                    | 111 ms                                                       | 64.2 ms: 1.73x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 62.1 ms: 1.73x faster                                                       |
| deepcopy                 | 468 us                                                       | 272 us: 1.72x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 193 us: 1.62x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 76.9 ms: 1.55x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.10 ms: 1.54x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.90 sec: 1.53x faster                                                      |
| mako                     | 14.7 ms                                                      | 9.72 ms: 1.51x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.09 us: 1.46x faster                                                       |
| django_template          | 50.2 ms                                                      | 34.7 ms: 1.45x faster                                                       |
| regex_compile            | 190 ms                                                       | 132 ms: 1.44x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.1 ms: 1.44x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.70 us: 1.44x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.51 sec: 1.42x faster                                                      |
| html5lib                 | 94.6 ms                                                      | 66.9 ms: 1.41x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 749 ms: 1.40x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 327 us: 1.39x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.39x faster                                                      |
| thrift                   | 1.18 ms                                                      | 854 us: 1.38x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 59.4 ms: 1.37x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 55.8 ms: 1.36x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.95 us: 1.36x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                       |
| nbody                    | 134 ms                                                       | 99.6 ms: 1.35x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.5 ms: 1.34x faster                                                       |
| fannkuch                 | 483 ms                                                       | 371 ms: 1.30x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.7 ms: 1.28x faster                                                       |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.2 ms: 1.27x faster                                                       |
| nqueens                  | 115 ms                                                       | 92.3 ms: 1.25x faster                                                       |
| sympy_str                | 360 ms                                                       | 289 ms: 1.25x faster                                                        |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                                        |
| sympy_expand             | 600 ms                                                       | 497 ms: 1.21x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.20x faster                                                       |
| scimark_fft              | 361 ms                                                       | 302 ms: 1.20x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 139 ms: 1.16x faster                                                        |
| regex_dna                | 261 ms                                                       | 226 ms: 1.15x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 80.8 ms: 1.14x faster                                                       |
| meteor_contest           | 138 ms                                                       | 122 ms: 1.13x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.9 ms: 1.13x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 24.2 ms: 1.12x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 56.9 ms: 1.11x faster                                                       |
| json                     | 5.86 ms                                                      | 5.43 ms: 1.08x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.79 us: 1.07x faster                                                       |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.91 ms: 1.03x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 381 ms: 1.02x faster                                                        |
| async_generators         | 421 ms                                                       | 448 ms: 1.07x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.60 ms: 1.17x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.81 ms: 1.20x slower                                                       |
| coverage                 | 63.3 ms                                                      | 77.9 ms: 1.23x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.92 ms: 1.66x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.79 ms: 1.99x slower                                                       |
| telco                    | 7.23 ms                                                      | 158 ms: 21.85x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250809-3.15.0a0-af15e1d-JIT/bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.340x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.40x