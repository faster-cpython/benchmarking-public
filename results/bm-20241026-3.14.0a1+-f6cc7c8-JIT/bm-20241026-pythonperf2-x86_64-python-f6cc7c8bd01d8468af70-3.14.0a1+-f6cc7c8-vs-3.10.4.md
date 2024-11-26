# Results vs. 3.10.4

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-x86_64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.279x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 317 ms: 1.10x faster                                                         |
| docutils       | 3.41 sec                                                     | 3.20 sec: 1.07x faster                                                       |
| html5lib       | 94.6 ms                                                      | 70.7 ms: 1.34x faster                                                        |
| tornado_http   | 157 ms                                                       | 122 ms: 1.29x faster                                                         |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 334 ms: 2.07x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 402 ms: 2.04x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 838 ms: 1.91x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 573 ms: 1.63x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.90x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 83.8 ms: 1.60x faster                                                        |
| float          | 111 ms                                                       | 80.0 ms: 1.39x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 147 ms: 1.30x faster                                                         |
| regex_dna      | 261 ms                                                       | 240 ms: 1.09x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.1 ms: 1.08x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.60 ms: 1.17x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 221 us: 1.41x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 336 us: 1.35x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 57.7 ms: 1.32x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 80.9 ms: 1.14x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                         |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 15.8 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.49 ms: 1.55x faster                                                        |
| django_template | 50.2 ms                                                      | 44.4 ms: 1.13x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 30.2 ms: 1.04x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 67.9 ms: 1.07x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.14x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 187 us: 2.87x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.30 ms: 2.27x faster                                                        |
| async_tree_none          | 692 ms                                                       | 334 ms: 2.07x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 402 ms: 2.04x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 838 ms: 1.91x faster                                                         |
| richards_super           | 90.6 ms                                                      | 49.3 ms: 1.84x faster                                                        |
| logging_silent           | 167 ns                                                       | 94.2 ns: 1.78x faster                                                        |
| scimark_lu               | 167 ms                                                       | 96.0 ms: 1.74x faster                                                        |
| richards                 | 75.1 ms                                                      | 43.7 ms: 1.72x faster                                                        |
| go                       | 262 ms                                                       | 153 ms: 1.71x faster                                                         |
| scimark_sor              | 180 ms                                                       | 105 ms: 1.71x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 573 ms: 1.63x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 73.0 ms: 1.63x faster                                                        |
| pyflate                  | 733 ms                                                       | 450 ms: 1.63x faster                                                         |
| nbody                    | 134 ms                                                       | 83.8 ms: 1.60x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 31.2 us: 1.60x faster                                                        |
| raytrace                 | 489 ms                                                       | 310 ms: 1.58x faster                                                         |
| chaos                    | 109 ms                                                       | 69.2 ms: 1.57x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.49 ms: 1.55x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 69.7 ms: 1.54x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.50 ms: 1.50x faster                                                        |
| spectral_norm            | 139 ms                                                       | 93.6 ms: 1.49x faster                                                        |
| generators               | 57.3 ms                                                      | 38.8 ms: 1.48x faster                                                        |
| deepcopy                 | 468 us                                                       | 319 us: 1.47x faster                                                         |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.42x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 221 us: 1.41x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                       |
| float                    | 111 ms                                                       | 80.0 ms: 1.39x faster                                                        |
| comprehensions           | 26.7 us                                                      | 19.4 us: 1.38x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.97 ms: 1.36x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 336 us: 1.35x faster                                                         |
| logging_format           | 9.64 us                                                      | 7.13 us: 1.35x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.57 us: 1.35x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.35x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 70.7 ms: 1.34x faster                                                        |
| pylint                   | 566 ms                                                       | 423 ms: 1.34x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 795 ms: 1.32x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 57.7 ms: 1.32x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 7.18 ms: 1.31x faster                                                        |
| fannkuch                 | 483 ms                                                       | 372 ms: 1.30x faster                                                         |
| regex_compile            | 190 ms                                                       | 147 ms: 1.30x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.30 sec: 1.29x faster                                                       |
| thrift                   | 1.18 ms                                                      | 914 us: 1.29x faster                                                         |
| tornado_http             | 157 ms                                                       | 122 ms: 1.29x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 63.2 ms: 1.28x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.14 us: 1.28x faster                                                        |
| scimark_fft              | 361 ms                                                       | 290 ms: 1.25x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.4 ms: 1.23x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.20 ms: 1.21x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 954 us: 1.20x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.62 sec: 1.15x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 80.9 ms: 1.14x faster                                                        |
| json                     | 5.86 ms                                                      | 5.15 ms: 1.14x faster                                                        |
| django_template          | 50.2 ms                                                      | 44.4 ms: 1.13x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 168 ms: 1.13x faster                                                         |
| sympy_expand             | 600 ms                                                       | 535 ms: 1.12x faster                                                         |
| sympy_str                | 360 ms                                                       | 323 ms: 1.11x faster                                                         |
| async_generators         | 421 ms                                                       | 379 ms: 1.11x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                         |
| 2to3                     | 350 ms                                                       | 317 ms: 1.10x faster                                                         |
| nqueens                  | 115 ms                                                       | 104 ms: 1.10x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                         |
| sympy_sum                | 193 ms                                                       | 176 ms: 1.09x faster                                                         |
| regex_dna                | 261 ms                                                       | 240 ms: 1.09x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 25.1 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| docutils                 | 3.41 sec                                                     | 3.20 sec: 1.07x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 30.2 ms: 1.04x faster                                                        |
| meteor_contest           | 138 ms                                                       | 134 ms: 1.04x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 27.3 ms: 1.03x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 68.9 ms: 1.02x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 67.9 ms: 1.07x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.81 ms: 1.08x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.60 ms: 1.17x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                        |
| coverage                 | 63.3 ms                                                      | 82.1 ms: 1.30x slower                                                        |
| python_startup           | 11.5 ms                                                      | 15.8 ms: 1.38x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 5.52 ms: 1.62x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.87 ms: 1.63x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 2.79 sec: 438.18x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.19x faster                                                                 |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241026-3.14.0a1+-f6cc7c8-JIT/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.279x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.33x