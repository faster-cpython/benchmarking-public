# Results vs. 3.10.4

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-x86_64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.104x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 1.47x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 430 ms: 1.23x slower                                                         |
| docutils       | 3.41 sec                                                     | 3.40 sec: 1.00x faster                                                       |
| html5lib       | 94.6 ms                                                      | 103 ms: 1.09x slower                                                         |
| tornado_http   | 157 ms                                                       | 166 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 936 ms: 1.71x faster                                                         |
| async_tree_none         | 692 ms                                                       | 416 ms: 1.66x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 517 ms: 1.58x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 680 ms: 1.38x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.58x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 249 ms: 1.09x faster                                                         |
| float          | 111 ms                                                       | 145 ms: 1.31x slower                                                         |
| nbody          | 134 ms                                                       | 194 ms: 1.45x slower                                                         |
| Geometric mean | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.60 ms: 1.17x slower                                                        |
| regex_compile  | 190 ms                                                       | 226 ms: 1.19x slower                                                         |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 160 ms                                                       | 139 ms: 1.15x faster                                                         |
| json_loads           | 30.3 us                                                      | 28.8 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 109 ms: 1.01x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 15.1 ms: 1.04x slower                                                        |
| tomli_loads          | 2.92 sec                                                     | 3.41 sec: 1.17x slower                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 116 ms: 1.25x slower                                                         |
| xml_etree_process    | 75.9 ms                                                      | 95.3 ms: 1.26x slower                                                        |
| unpickle_pure_python | 312 us                                                       | 408 us: 1.31x slower                                                         |
| pickle_pure_python   | 455 us                                                       | 598 us: 1.32x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.12x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 11.8 ms: 1.62x slower                                                        |
| python_startup         | 11.5 ms                                                      | 19.3 ms: 1.68x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.65x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 63.3 ms                                                      | 81.0 ms: 1.28x slower                                                        |
| django_template | 50.2 ms                                                      | 67.2 ms: 1.34x slower                                                        |
| genshi_text     | 31.4 ms                                                      | 42.5 ms: 1.35x slower                                                        |
| mako            | 14.7 ms                                                      | 22.3 ms: 1.51x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.37x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 266 us: 2.02x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 936 ms: 1.71x faster                                                         |
| async_tree_none          | 692 ms                                                       | 416 ms: 1.66x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 517 ms: 1.58x faster                                                         |
| generators               | 57.3 ms                                                      | 40.8 ms: 1.41x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 680 ms: 1.38x faster                                                         |
| pylint                   | 566 ms                                                       | 432 ms: 1.31x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 139 ms: 1.15x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 19.4 ms: 1.10x faster                                                        |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                                         |
| pidigits                 | 271 ms                                                       | 249 ms: 1.09x faster                                                         |
| coroutines               | 30.3 ms                                                      | 28.0 ms: 1.08x faster                                                        |
| deepcopy                 | 468 us                                                       | 432 us: 1.08x faster                                                         |
| json_loads               | 30.3 us                                                      | 28.8 us: 1.05x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 381 ms: 1.02x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 48.8 us: 1.02x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 109 ms: 1.01x faster                                                         |
| docutils                 | 3.41 sec                                                     | 3.40 sec: 1.00x faster                                                       |
| json                     | 5.86 ms                                                      | 5.96 ms: 1.02x slower                                                        |
| crypto_pyaes             | 119 ms                                                       | 123 ms: 1.03x slower                                                         |
| pycparser                | 1.67 sec                                                     | 1.73 sec: 1.03x slower                                                       |
| json_dumps               | 14.5 ms                                                      | 15.1 ms: 1.04x slower                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 23.9 ms: 1.05x slower                                                        |
| tornado_http             | 157 ms                                                       | 166 ms: 1.06x slower                                                         |
| pyflate                  | 733 ms                                                       | 774 ms: 1.06x slower                                                         |
| gc_traversal             | 3.42 ms                                                      | 3.63 ms: 1.06x slower                                                        |
| mdp                      | 3.01 sec                                                     | 3.24 sec: 1.08x slower                                                       |
| richards                 | 75.1 ms                                                      | 81.0 ms: 1.08x slower                                                        |
| html5lib                 | 94.6 ms                                                      | 103 ms: 1.09x slower                                                         |
| dulwich_log              | 81.1 ms                                                      | 88.6 ms: 1.09x slower                                                        |
| deltablue                | 7.50 ms                                                      | 8.20 ms: 1.09x slower                                                        |
| logging_silent           | 167 ns                                                       | 183 ns: 1.09x slower                                                         |
| scimark_fft              | 361 ms                                                       | 397 ms: 1.10x slower                                                         |
| richards_super           | 90.6 ms                                                      | 99.9 ms: 1.10x slower                                                        |
| go                       | 262 ms                                                       | 291 ms: 1.11x slower                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.68 ms: 1.12x slower                                                        |
| comprehensions           | 26.7 us                                                      | 30.3 us: 1.14x slower                                                        |
| nqueens                  | 115 ms                                                       | 131 ms: 1.14x slower                                                         |
| chaos                    | 109 ms                                                       | 125 ms: 1.15x slower                                                         |
| sympy_integrate          | 28.2 ms                                                      | 32.8 ms: 1.16x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.60 ms: 1.17x slower                                                        |
| async_generators         | 421 ms                                                       | 492 ms: 1.17x slower                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 4.69 us: 1.17x slower                                                        |
| tomli_loads              | 2.92 sec                                                     | 3.41 sec: 1.17x slower                                                       |
| thrift                   | 1.18 ms                                                      | 1.39 ms: 1.18x slower                                                        |
| spectral_norm            | 139 ms                                                       | 166 ms: 1.19x slower                                                         |
| regex_compile            | 190 ms                                                       | 226 ms: 1.19x slower                                                         |
| sqlalchemy_declarative   | 190 ms                                                       | 226 ms: 1.19x slower                                                         |
| fannkuch                 | 483 ms                                                       | 590 ms: 1.22x slower                                                         |
| meteor_contest           | 138 ms                                                       | 169 ms: 1.22x slower                                                         |
| 2to3                     | 350 ms                                                       | 430 ms: 1.23x slower                                                         |
| hexiom                   | 9.42 ms                                                      | 11.7 ms: 1.24x slower                                                        |
| sympy_str                | 360 ms                                                       | 449 ms: 1.25x slower                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 134 ms: 1.25x slower                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 116 ms: 1.25x slower                                                         |
| xml_etree_process        | 75.9 ms                                                      | 95.3 ms: 1.26x slower                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 2.81 ms: 1.26x slower                                                        |
| raytrace                 | 489 ms                                                       | 616 ms: 1.26x slower                                                         |
| logging_format           | 9.64 us                                                      | 12.2 us: 1.26x slower                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 3.39 ms: 1.26x slower                                                        |
| logging_simple           | 8.88 us                                                      | 11.3 us: 1.27x slower                                                        |
| genshi_xml               | 63.3 ms                                                      | 81.0 ms: 1.28x slower                                                        |
| sqlglot_normalize        | 144 ms                                                       | 184 ms: 1.28x slower                                                         |
| float                    | 111 ms                                                       | 145 ms: 1.31x slower                                                         |
| scimark_lu               | 167 ms                                                       | 218 ms: 1.31x slower                                                         |
| unpickle_pure_python     | 312 us                                                       | 408 us: 1.31x slower                                                         |
| pickle_pure_python       | 455 us                                                       | 598 us: 1.32x slower                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 92.3 ms: 1.32x slower                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 1.39 sec: 1.33x slower                                                       |
| django_template          | 50.2 ms                                                      | 67.2 ms: 1.34x slower                                                        |
| sympy_expand             | 600 ms                                                       | 805 ms: 1.34x slower                                                         |
| pprint_pformat           | 2.15 sec                                                     | 2.89 sec: 1.34x slower                                                       |
| scimark_sor              | 180 ms                                                       | 242 ms: 1.35x slower                                                         |
| genshi_text              | 31.4 ms                                                      | 42.5 ms: 1.35x slower                                                        |
| sympy_sum                | 193 ms                                                       | 261 ms: 1.35x slower                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 1.57 ms: 1.37x slower                                                        |
| telco                    | 7.23 ms                                                      | 10.2 ms: 1.41x slower                                                        |
| nbody                    | 134 ms                                                       | 194 ms: 1.45x slower                                                         |
| create_gc_cycles         | 1.76 ms                                                      | 2.60 ms: 1.48x slower                                                        |
| mako                     | 14.7 ms                                                      | 22.3 ms: 1.51x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 11.8 ms: 1.62x slower                                                        |
| python_startup           | 11.5 ms                                                      | 19.3 ms: 1.68x slower                                                        |
| coverage                 | 63.3 ms                                                      | 108 ms: 1.71x slower                                                         |
| bench_mp_pool            | 6.37 ms                                                      | 52.2 ms: 8.19x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.15x slower                                                                 |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241026-3.14.0a1+-f6cc7c8-NOGIL/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.104x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 1.47x