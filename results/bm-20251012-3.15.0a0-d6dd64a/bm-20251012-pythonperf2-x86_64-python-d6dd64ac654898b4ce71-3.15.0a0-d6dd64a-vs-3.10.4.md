# Results vs. 3.10.4

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: linux-x86_64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.340x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 278 ms: 1.26x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.84 sec: 1.20x faster                                                      |
| html5lib       | 94.6 ms                                                      | 64.0 ms: 1.48x faster                                                       |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 618 ms: 2.59x faster                                                        |
| async_tree_none         | 692 ms                                                       | 273 ms: 2.54x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 328 ms: 2.49x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 501 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.35x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 68.9 ms: 1.61x faster                                                       |
| nbody          | 134 ms                                                       | 89.6 ms: 1.50x faster                                                       |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 131 ms: 1.45x faster                                                        |
| regex_dna      | 261 ms                                                       | 220 ms: 1.19x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 24.3 ms: 1.12x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.32 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 205 us: 1.52x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.99 sec: 1.47x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.1 ms: 1.44x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 329 us: 1.38x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 98.8 ms: 1.12x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 82.8 ms: 1.11x faster                                                       |
| unpickle             | 13.5 us                                                      | 14.8 us: 1.10x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 5.20 us: 1.12x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 35.1 us: 1.19x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.04 us: 1.22x slower                                                       |
| pickle               | 9.89 us                                                      | 12.7 us: 1.29x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.81 ms: 1.20x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.6 ms: 1.41x faster                                                       |
| mako            | 14.7 ms                                                      | 10.7 ms: 1.38x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.0 ms: 1.37x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 53.5 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.33x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 166 us: 3.23x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 618 ms: 2.59x faster                                                        |
| async_tree_none          | 692 ms                                                       | 273 ms: 2.54x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 328 ms: 2.49x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.27 sec: 2.37x faster                                                      |
| deltablue                | 7.50 ms                                                      | 3.17 ms: 2.36x faster                                                       |
| go                       | 262 ms                                                       | 117 ms: 2.25x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 370 ms: 2.11x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 25.3 us: 1.97x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| generators               | 57.3 ms                                                      | 30.2 ms: 1.90x faster                                                       |
| chaos                    | 109 ms                                                       | 57.8 ms: 1.88x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 501 ms: 1.87x faster                                                        |
| pyflate                  | 733 ms                                                       | 405 ms: 1.81x faster                                                        |
| richards_super           | 90.6 ms                                                      | 50.2 ms: 1.81x faster                                                       |
| logging_silent           | 167 ns                                                       | 94.1 ns: 1.78x faster                                                       |
| pylint                   | 566 ms                                                       | 318 ms: 1.78x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 61.0 ms: 1.76x faster                                                       |
| deepcopy                 | 468 us                                                       | 267 us: 1.75x faster                                                        |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.74x faster                                                        |
| scimark_lu               | 167 ms                                                       | 96.1 ms: 1.74x faster                                                       |
| raytrace                 | 489 ms                                                       | 283 ms: 1.73x faster                                                        |
| richards                 | 75.1 ms                                                      | 44.4 ms: 1.69x faster                                                       |
| comprehensions           | 26.7 us                                                      | 15.9 us: 1.68x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 5.77 ms: 1.63x faster                                                       |
| spectral_norm            | 139 ms                                                       | 85.4 ms: 1.63x faster                                                       |
| float                    | 111 ms                                                       | 68.9 ms: 1.61x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 75.5 ms: 1.58x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 205 us: 1.52x faster                                                        |
| logging_simple           | 8.88 us                                                      | 5.89 us: 1.51x faster                                                       |
| nbody                    | 134 ms                                                       | 89.6 ms: 1.50x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.51 us: 1.48x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 64.0 ms: 1.48x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.99 sec: 1.47x faster                                                      |
| regex_compile            | 190 ms                                                       | 131 ms: 1.45x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.1 ms: 1.44x faster                                                       |
| django_template          | 50.2 ms                                                      | 35.6 ms: 1.41x faster                                                       |
| thrift                   | 1.18 ms                                                      | 847 us: 1.39x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.4 ms: 1.38x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 329 us: 1.38x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.38x faster                                                      |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.38x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.56 sec: 1.38x faster                                                      |
| coroutines               | 30.3 ms                                                      | 22.1 ms: 1.37x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 23.0 ms: 1.37x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 59.3 ms: 1.37x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 769 ms: 1.37x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.96 us: 1.36x faster                                                       |
| fannkuch                 | 483 ms                                                       | 359 ms: 1.34x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 45.5 ns: 1.32x faster                                                       |
| scimark_fft              | 361 ms                                                       | 276 ms: 1.31x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 21.8 ms: 1.29x faster                                                       |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.29x faster                                                        |
| 2to3                     | 350 ms                                                       | 278 ms: 1.26x faster                                                        |
| sympy_str                | 360 ms                                                       | 286 ms: 1.26x faster                                                        |
| nqueens                  | 115 ms                                                       | 92.1 ms: 1.25x faster                                                       |
| sympy_expand             | 600 ms                                                       | 486 ms: 1.23x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 936 us: 1.22x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.84 sec: 1.20x faster                                                      |
| regex_dna                | 261 ms                                                       | 220 ms: 1.19x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 53.5 ms: 1.18x faster                                                       |
| meteor_contest           | 138 ms                                                       | 120 ms: 1.15x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.47 ms: 1.14x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 98.8 ms: 1.12x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 24.3 ms: 1.12x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 82.8 ms: 1.11x faster                                                       |
| json                     | 5.86 ms                                                      | 5.34 ms: 1.10x faster                                                       |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.85 us: 1.05x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                                        |
| async_generators         | 421 ms                                                       | 426 ms: 1.01x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.32 ms: 1.08x slower                                                       |
| unpickle                 | 13.5 us                                                      | 14.8 us: 1.10x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 5.20 us: 1.12x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 35.1 us: 1.19x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.81 ms: 1.20x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.04 us: 1.22x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.7 us: 1.29x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| coverage                 | 63.3 ms                                                      | 87.4 ms: 1.38x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.87 ms: 1.63x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.49 ms: 1.90x slower                                                       |
| telco                    | 7.23 ms                                                      | 154 ms: 21.37x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 1.98 sec: 310.38x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20251012-3.15.0a0-d6dd64a/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.340x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.39x