# Results vs. 3.10.4

- fork: python
- ref: a07cf4ce25205d836a6b
- machine: linux-x86_64
- commit hash: a07cf4c
- commit date: 2024-08-16
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                      |
| html5lib       | 94.6 ms                                                      | 73.5 ms: 1.29x faster                                                       |
| tornado_http   | 157 ms                                                       | 117 ms: 1.34x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 332 ms: 2.08x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 404 ms: 2.03x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 812 ms: 1.97x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 574 ms: 1.63x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.92x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 88.3 ms: 1.52x faster                                                       |
| float          | 111 ms                                                       | 81.6 ms: 1.36x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 141 ms: 1.35x faster                                                        |
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.64 ms: 1.18x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 317 us: 1.43x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 220 us: 1.42x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.22 sec: 1.32x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 59.1 ms: 1.28x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 84.2 ms: 1.10x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.43x faster                                                       |
| django_template | 50.2 ms                                                      | 39.4 ms: 1.27x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 55.3 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 176 us: 3.05x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.40 ms: 2.20x faster                                                       |
| async_tree_none          | 692 ms                                                       | 332 ms: 2.08x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.08x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 404 ms: 2.03x faster                                                        |
| generators               | 57.3 ms                                                      | 28.7 ms: 1.99x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 812 ms: 1.97x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| raytrace                 | 489 ms                                                       | 269 ms: 1.82x faster                                                        |
| scimark_lu               | 167 ms                                                       | 94.1 ms: 1.77x faster                                                       |
| chaos                    | 109 ms                                                       | 62.0 ms: 1.75x faster                                                       |
| logging_silent           | 167 ns                                                       | 96.5 ns: 1.73x faster                                                       |
| scimark_sor              | 180 ms                                                       | 109 ms: 1.66x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 72.4 ms: 1.65x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 30.3 us: 1.64x faster                                                       |
| pylint                   | 566 ms                                                       | 347 ms: 1.63x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 574 ms: 1.63x faster                                                        |
| richards_super           | 90.6 ms                                                      | 55.9 ms: 1.62x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 66.6 ms: 1.61x faster                                                       |
| go                       | 262 ms                                                       | 164 ms: 1.60x faster                                                        |
| deepcopy                 | 468 us                                                       | 293 us: 1.60x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.58x faster                                                       |
| richards                 | 75.1 ms                                                      | 49.3 ms: 1.52x faster                                                       |
| nbody                    | 134 ms                                                       | 88.3 ms: 1.52x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.6 us: 1.52x faster                                                       |
| pyflate                  | 733 ms                                                       | 485 ms: 1.51x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.30 ms: 1.50x faster                                                       |
| spectral_norm            | 139 ms                                                       | 96.0 ms: 1.45x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.2 ms: 1.43x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 317 us: 1.43x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.42x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.24 us: 1.42x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 220 us: 1.42x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.85 us: 1.41x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.66 ms: 1.37x faster                                                       |
| float                    | 111 ms                                                       | 81.6 ms: 1.36x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| thrift                   | 1.18 ms                                                      | 864 us: 1.36x faster                                                        |
| regex_compile            | 190 ms                                                       | 141 ms: 1.35x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.34x faster                                                      |
| fannkuch                 | 483 ms                                                       | 359 ms: 1.34x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.99 us: 1.34x faster                                                       |
| tornado_http             | 157 ms                                                       | 117 ms: 1.34x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.1 ms: 1.33x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 866 us: 1.32x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.22 sec: 1.32x faster                                                      |
| html5lib                 | 94.6 ms                                                      | 73.5 ms: 1.29x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 59.1 ms: 1.28x faster                                                       |
| nqueens                  | 115 ms                                                       | 89.9 ms: 1.28x faster                                                       |
| django_template          | 50.2 ms                                                      | 39.4 ms: 1.27x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 841 ms: 1.25x faster                                                        |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.25x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.73 sec: 1.24x faster                                                      |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.13 ms: 1.23x faster                                                       |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                        |
| scimark_fft              | 361 ms                                                       | 297 ms: 1.22x faster                                                        |
| sympy_str                | 360 ms                                                       | 296 ms: 1.21x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 23.3 ms: 1.21x faster                                                       |
| async_generators         | 421 ms                                                       | 353 ms: 1.19x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.53 sec: 1.19x faster                                                      |
| sympy_expand             | 600 ms                                                       | 505 ms: 1.19x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 123 ms: 1.17x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 60.1 ms: 1.17x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 55.3 ms: 1.14x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 84.2 ms: 1.10x faster                                                       |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                                        |
| json                     | 5.86 ms                                                      | 5.37 ms: 1.09x faster                                                       |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.95 ms: 1.10x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.07 ms: 1.12x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.64 ms: 1.18x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.05 ms: 1.23x slower                                                       |
| coverage                 | 63.3 ms                                                      | 85.5 ms: 1.35x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.68 ms: 1.37x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240816-3.14.0a0-a07cf4c/bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x