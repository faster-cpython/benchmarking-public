# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.342x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.0 ms: 1.35x faster                                                       |
| tornado_http   | 157 ms                                                       | 116 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 317 ms: 2.18x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 395 ms: 2.07x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 816 ms: 1.96x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 569 ms: 1.65x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.95x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 86.4 ms: 1.55x faster                                                       |
| float          | 111 ms                                                       | 80.1 ms: 1.39x faster                                                       |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 141 ms: 1.35x faster                                                        |
| regex_dna      | 261 ms                                                       | 238 ms: 1.10x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.9 ms: 1.01x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 312 us: 1.46x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 214 us: 1.46x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.34x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 59.7 ms: 1.27x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.21x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.55 sec: 1.14x faster                                                      |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.09x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 147 ms: 1.09x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 85.1 ms: 1.08x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.23x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.09 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                       |
| django_template | 50.2 ms                                                      | 39.6 ms: 1.27x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 26.0 ms: 1.21x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 55.5 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.25x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.12x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.41 ms: 2.20x faster                                                       |
| async_tree_none          | 692 ms                                                       | 317 ms: 2.18x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 367 ms: 2.12x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 395 ms: 2.07x faster                                                        |
| generators               | 57.3 ms                                                      | 28.6 ms: 2.01x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 816 ms: 1.96x faster                                                        |
| go                       | 262 ms                                                       | 135 ms: 1.94x faster                                                        |
| raytrace                 | 489 ms                                                       | 273 ms: 1.79x faster                                                        |
| chaos                    | 109 ms                                                       | 61.8 ms: 1.76x faster                                                       |
| scimark_lu               | 167 ms                                                       | 95.4 ms: 1.75x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 29.0 us: 1.72x faster                                                       |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                                        |
| logging_silent           | 167 ns                                                       | 100 ns: 1.67x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 569 ms: 1.65x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 65.9 ms: 1.63x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 73.4 ms: 1.62x faster                                                       |
| pylint                   | 566 ms                                                       | 350 ms: 1.62x faster                                                        |
| richards_super           | 90.6 ms                                                      | 56.3 ms: 1.61x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                       |
| nbody                    | 134 ms                                                       | 86.4 ms: 1.55x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                                       |
| scimark_sor              | 180 ms                                                       | 119 ms: 1.52x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.78 ms: 1.51x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.26 ms: 1.50x faster                                                       |
| richards                 | 75.1 ms                                                      | 50.2 ms: 1.50x faster                                                       |
| pyflate                  | 733 ms                                                       | 497 ms: 1.48x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 312 us: 1.46x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 214 us: 1.46x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.37 ms: 1.46x faster                                                       |
| spectral_norm            | 139 ms                                                       | 95.4 ms: 1.46x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.68 us: 1.44x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.23 us: 1.43x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.20 sec: 1.39x faster                                                      |
| deepcopy_reduce          | 4.01 us                                                      | 2.88 us: 1.39x faster                                                       |
| float                    | 111 ms                                                       | 80.1 ms: 1.39x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.0 ms: 1.35x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                                       |
| tornado_http             | 157 ms                                                       | 116 ms: 1.35x faster                                                        |
| regex_compile            | 190 ms                                                       | 141 ms: 1.35x faster                                                        |
| thrift                   | 1.18 ms                                                      | 874 us: 1.35x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.34x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 853 us: 1.34x faster                                                        |
| fannkuch                 | 483 ms                                                       | 362 ms: 1.33x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 792 ms: 1.33x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                                      |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.27x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 59.7 ms: 1.27x faster                                                       |
| nqueens                  | 115 ms                                                       | 90.4 ms: 1.27x faster                                                       |
| django_template          | 50.2 ms                                                      | 39.6 ms: 1.27x faster                                                       |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                                        |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.11 ms: 1.24x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 22.9 ms: 1.23x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.21x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 26.0 ms: 1.21x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                                      |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.21x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 58.3 ms: 1.20x faster                                                       |
| sympy_expand             | 600 ms                                                       | 499 ms: 1.20x faster                                                        |
| scimark_fft              | 361 ms                                                       | 303 ms: 1.19x faster                                                        |
| async_generators         | 421 ms                                                       | 355 ms: 1.19x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| tomli_loads              | 2.92 sec                                                     | 2.55 sec: 1.14x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 55.5 ms: 1.14x faster                                                       |
| json                     | 5.86 ms                                                      | 5.31 ms: 1.10x faster                                                       |
| regex_dna                | 261 ms                                                       | 238 ms: 1.10x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.09x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 147 ms: 1.09x faster                                                        |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 85.1 ms: 1.08x faster                                                       |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.9 ms: 1.01x faster                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.00 ms: 1.13x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.27 ms: 1.14x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.09 ms: 1.24x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.44 ms: 1.30x slower                                                       |
| coverage                 | 63.3 ms                                                      | 85.2 ms: 1.35x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.36x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-15b187e/bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.342x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.13x