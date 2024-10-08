# Results vs. 3.10.4

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-x86_64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.12x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 442 ms: 1.26x slower                                                        |
| docutils       | 3.41 sec                                                     | 3.52 sec: 1.03x slower                                                      |
| html5lib       | 94.6 ms                                                      | 110 ms: 1.16x slower                                                        |
| tornado_http   | 157 ms                                                       | 170 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.13x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 964 ms: 1.66x faster                                                        |
| async_tree_none         | 692 ms                                                       | 428 ms: 1.62x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 533 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 688 ms: 1.36x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.54x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| float          | 111 ms                                                       | 143 ms: 1.29x slower                                                        |
| nbody          | 134 ms                                                       | 196 ms: 1.46x slower                                                        |
| Geometric mean | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 255 ms: 1.03x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 28.5 ms: 1.05x slower                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.59 ms: 1.16x slower                                                       |
| regex_compile  | 190 ms                                                       | 234 ms: 1.23x slower                                                        |
| Geometric mean | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 160 ms                                                       | 140 ms: 1.14x faster                                                        |
| json_loads           | 30.3 us                                                      | 30.1 us: 1.01x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 14.6 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 112 ms: 1.01x slower                                                        |
| tomli_loads          | 2.92 sec                                                     | 3.43 sec: 1.18x slower                                                      |
| xml_etree_generate   | 92.3 ms                                                      | 116 ms: 1.25x slower                                                        |
| xml_etree_process    | 75.9 ms                                                      | 95.7 ms: 1.26x slower                                                       |
| pickle_pure_python   | 455 us                                                       | 608 us: 1.34x slower                                                        |
| unpickle_pure_python | 312 us                                                       | 427 us: 1.37x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.13x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 17.3 ms: 1.51x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 11.9 ms: 1.63x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.57x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 63.3 ms                                                      | 84.2 ms: 1.33x slower                                                       |
| django_template | 50.2 ms                                                      | 68.4 ms: 1.36x slower                                                       |
| genshi_text     | 31.4 ms                                                      | 43.4 ms: 1.38x slower                                                       |
| mako            | 14.7 ms                                                      | 21.8 ms: 1.48x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.39x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 279 us: 1.92x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.77 sec: 1.75x faster                                                      |
| asyncio_tcp              | 779 ms                                                       | 452 ms: 1.73x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 964 ms: 1.66x faster                                                        |
| async_tree_none          | 692 ms                                                       | 428 ms: 1.62x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 533 ms: 1.54x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 688 ms: 1.36x faster                                                        |
| generators               | 57.3 ms                                                      | 42.4 ms: 1.35x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.95 ms: 1.29x faster                                                       |
| pylint                   | 566 ms                                                       | 440 ms: 1.29x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 2.90 ms: 1.18x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 140 ms: 1.14x faster                                                        |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 19.8 ms: 1.08x faster                                                       |
| deepcopy                 | 468 us                                                       | 450 us: 1.04x faster                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.70 ms: 1.04x faster                                                       |
| regex_dna                | 261 ms                                                       | 255 ms: 1.03x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                        |
| json_loads               | 30.3 us                                                      | 30.1 us: 1.01x faster                                                       |
| coroutines               | 30.3 ms                                                      | 30.5 ms: 1.01x slower                                                       |
| json_dumps               | 14.5 ms                                                      | 14.6 ms: 1.01x slower                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 112 ms: 1.01x slower                                                        |
| crypto_pyaes             | 119 ms                                                       | 122 ms: 1.02x slower                                                        |
| docutils                 | 3.41 sec                                                     | 3.52 sec: 1.03x slower                                                      |
| deepcopy_memo            | 49.8 us                                                      | 51.7 us: 1.04x slower                                                       |
| regex_v8                 | 27.2 ms                                                      | 28.5 ms: 1.05x slower                                                       |
| pycparser                | 1.67 sec                                                     | 1.76 sec: 1.05x slower                                                      |
| json                     | 5.86 ms                                                      | 6.19 ms: 1.06x slower                                                       |
| pyflate                  | 733 ms                                                       | 785 ms: 1.07x slower                                                        |
| mdp                      | 3.01 sec                                                     | 3.25 sec: 1.08x slower                                                      |
| tornado_http             | 157 ms                                                       | 170 ms: 1.08x slower                                                        |
| scimark_fft              | 361 ms                                                       | 394 ms: 1.09x slower                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.65 ms: 1.11x slower                                                       |
| richards_super           | 90.6 ms                                                      | 103 ms: 1.13x slower                                                        |
| nqueens                  | 115 ms                                                       | 130 ms: 1.14x slower                                                        |
| deltablue                | 7.50 ms                                                      | 8.55 ms: 1.14x slower                                                       |
| richards                 | 75.1 ms                                                      | 85.7 ms: 1.14x slower                                                       |
| comprehensions           | 26.7 us                                                      | 30.9 us: 1.16x slower                                                       |
| chaos                    | 109 ms                                                       | 126 ms: 1.16x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.59 ms: 1.16x slower                                                       |
| html5lib                 | 94.6 ms                                                      | 110 ms: 1.16x slower                                                        |
| sympy_integrate          | 28.2 ms                                                      | 32.9 ms: 1.17x slower                                                       |
| tomli_loads              | 2.92 sec                                                     | 3.43 sec: 1.18x slower                                                      |
| thrift                   | 1.18 ms                                                      | 1.39 ms: 1.18x slower                                                       |
| spectral_norm            | 139 ms                                                       | 165 ms: 1.18x slower                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 4.78 us: 1.19x slower                                                       |
| logging_silent           | 167 ns                                                       | 202 ns: 1.20x slower                                                        |
| async_generators         | 421 ms                                                       | 511 ms: 1.21x slower                                                        |
| fannkuch                 | 483 ms                                                       | 593 ms: 1.23x slower                                                        |
| regex_compile            | 190 ms                                                       | 234 ms: 1.23x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 116 ms: 1.25x slower                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 135 ms: 1.25x slower                                                        |
| meteor_contest           | 138 ms                                                       | 174 ms: 1.26x slower                                                        |
| xml_etree_process        | 75.9 ms                                                      | 95.7 ms: 1.26x slower                                                       |
| 2to3                     | 350 ms                                                       | 442 ms: 1.26x slower                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 3.42 ms: 1.28x slower                                                       |
| raytrace                 | 489 ms                                                       | 626 ms: 1.28x slower                                                        |
| sympy_str                | 360 ms                                                       | 462 ms: 1.28x slower                                                        |
| float                    | 111 ms                                                       | 143 ms: 1.29x slower                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 2.88 ms: 1.29x slower                                                       |
| hexiom                   | 9.42 ms                                                      | 12.2 ms: 1.29x slower                                                       |
| sqlglot_normalize        | 144 ms                                                       | 189 ms: 1.31x slower                                                        |
| genshi_xml               | 63.3 ms                                                      | 84.2 ms: 1.33x slower                                                       |
| logging_format           | 9.64 us                                                      | 12.9 us: 1.33x slower                                                       |
| pickle_pure_python       | 455 us                                                       | 608 us: 1.34x slower                                                        |
| go                       | 262 ms                                                       | 351 ms: 1.34x slower                                                        |
| logging_simple           | 8.88 us                                                      | 11.9 us: 1.34x slower                                                       |
| django_template          | 50.2 ms                                                      | 68.4 ms: 1.36x slower                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 95.9 ms: 1.37x slower                                                       |
| unpickle_pure_python     | 312 us                                                       | 427 us: 1.37x slower                                                        |
| genshi_text              | 31.4 ms                                                      | 43.4 ms: 1.38x slower                                                       |
| sympy_sum                | 193 ms                                                       | 266 ms: 1.38x slower                                                        |
| sympy_expand             | 600 ms                                                       | 837 ms: 1.40x slower                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 1.47 sec: 1.40x slower                                                      |
| pprint_pformat           | 2.15 sec                                                     | 3.04 sec: 1.41x slower                                                      |
| scimark_lu               | 167 ms                                                       | 238 ms: 1.42x slower                                                        |
| nbody                    | 134 ms                                                       | 196 ms: 1.46x slower                                                        |
| scimark_sor              | 180 ms                                                       | 266 ms: 1.48x slower                                                        |
| mako                     | 14.7 ms                                                      | 21.8 ms: 1.48x slower                                                       |
| telco                    | 7.23 ms                                                      | 10.7 ms: 1.48x slower                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 1.70 ms: 1.49x slower                                                       |
| python_startup           | 11.5 ms                                                      | 17.3 ms: 1.51x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 11.9 ms: 1.63x slower                                                       |
| coverage                 | 63.3 ms                                                      | 110 ms: 1.74x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.12x slower                                                                |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240817-3.14.0a0-79c542b-NOGIL/bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 1.31x