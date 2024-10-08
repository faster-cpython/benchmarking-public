# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_call_ex
- machine: linux-x86_64
- commit hash: 852115b
- commit date: 2024-08-19
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 289 ms: 1.21x faster                                                                |
| docutils       | 3.41 sec                                                     | 2.99 sec: 1.14x faster                                                              |
| html5lib       | 94.6 ms                                                      | 75.4 ms: 1.26x faster                                                               |
| tornado_http   | 157 ms                                                       | 118 ms: 1.33x faster                                                                |
| Geometric mean | (ref)                                                        | 1.23x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 333 ms: 2.07x faster                                                                |
| async_tree_memoization  | 819 ms                                                       | 403 ms: 2.03x faster                                                                |
| async_tree_io           | 1.60 sec                                                     | 798 ms: 2.00x faster                                                                |
| async_tree_cpu_io_mixed | 936 ms                                                       | 574 ms: 1.63x faster                                                                |
| Geometric mean          | (ref)                                                        | 1.93x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.4 ms: 1.57x faster                                                               |
| float          | 111 ms                                                       | 80.1 ms: 1.39x faster                                                               |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                                |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.35x faster                                                                |
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                                                |
| regex_v8       | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                               |
| regex_effbot   | 3.09 ms                                                      | 3.66 ms: 1.19x slower                                                               |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 213 us: 1.46x faster                                                                |
| pickle_pure_python   | 455 us                                                       | 317 us: 1.44x faster                                                                |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.38x faster                                                               |
| xml_etree_process    | 75.9 ms                                                      | 58.7 ms: 1.29x faster                                                               |
| tomli_loads          | 2.92 sec                                                     | 2.28 sec: 1.28x faster                                                              |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                               |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                                |
| xml_etree_generate   | 92.3 ms                                                      | 84.2 ms: 1.10x faster                                                               |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.08x faster                                                                |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                               |
| python_startup_no_site | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                               |
| django_template | 50.2 ms                                                      | 39.6 ms: 1.27x faster                                                               |
| genshi_text     | 31.4 ms                                                      | 25.7 ms: 1.22x faster                                                               |
| genshi_xml      | 63.3 ms                                                      | 55.1 ms: 1.15x faster                                                               |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 180 us: 2.98x faster                                                                |
| deltablue                | 7.50 ms                                                      | 3.41 ms: 2.20x faster                                                               |
| async_tree_none          | 692 ms                                                       | 333 ms: 2.07x faster                                                                |
| asyncio_tcp              | 779 ms                                                       | 376 ms: 2.07x faster                                                                |
| async_tree_memoization   | 819 ms                                                       | 403 ms: 2.03x faster                                                                |
| async_tree_io            | 1.60 sec                                                     | 798 ms: 2.00x faster                                                                |
| generators               | 57.3 ms                                                      | 29.1 ms: 1.97x faster                                                               |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                              |
| raytrace                 | 489 ms                                                       | 263 ms: 1.86x faster                                                                |
| chaos                    | 109 ms                                                       | 61.8 ms: 1.76x faster                                                               |
| scimark_lu               | 167 ms                                                       | 95.8 ms: 1.74x faster                                                               |
| logging_silent           | 167 ns                                                       | 97.4 ns: 1.72x faster                                                               |
| deepcopy_memo            | 49.8 us                                                      | 29.6 us: 1.68x faster                                                               |
| scimark_monte_carlo      | 107 ms                                                       | 64.7 ms: 1.66x faster                                                               |
| deepcopy                 | 468 us                                                       | 284 us: 1.65x faster                                                                |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 574 ms: 1.63x faster                                                                |
| crypto_pyaes             | 119 ms                                                       | 73.3 ms: 1.62x faster                                                               |
| pylint                   | 566 ms                                                       | 349 ms: 1.62x faster                                                                |
| go                       | 262 ms                                                       | 163 ms: 1.60x faster                                                                |
| richards_super           | 90.6 ms                                                      | 57.1 ms: 1.59x faster                                                               |
| nbody                    | 134 ms                                                       | 85.4 ms: 1.57x faster                                                               |
| sqlglot_parse            | 2.24 ms                                                      | 1.43 ms: 1.56x faster                                                               |
| scimark_sor              | 180 ms                                                       | 116 ms: 1.55x faster                                                                |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.55x faster                                                               |
| hexiom                   | 9.42 ms                                                      | 6.23 ms: 1.51x faster                                                               |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                                               |
| richards                 | 75.1 ms                                                      | 50.6 ms: 1.48x faster                                                               |
| pyflate                  | 733 ms                                                       | 496 ms: 1.48x faster                                                                |
| unpickle_pure_python     | 312 us                                                       | 213 us: 1.46x faster                                                                |
| spectral_norm            | 139 ms                                                       | 95.6 ms: 1.45x faster                                                               |
| pickle_pure_python       | 455 us                                                       | 317 us: 1.44x faster                                                                |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                               |
| deepcopy_reduce          | 4.01 us                                                      | 2.87 us: 1.40x faster                                                               |
| coroutines               | 30.3 ms                                                      | 21.8 ms: 1.39x faster                                                               |
| float                    | 111 ms                                                       | 80.1 ms: 1.39x faster                                                               |
| bench_mp_pool            | 6.37 ms                                                      | 4.61 ms: 1.38x faster                                                               |
| logging_simple           | 8.88 us                                                      | 6.43 us: 1.38x faster                                                               |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.38x faster                                                               |
| logging_format           | 9.64 us                                                      | 7.09 us: 1.36x faster                                                               |
| regex_compile            | 190 ms                                                       | 140 ms: 1.35x faster                                                                |
| fannkuch                 | 483 ms                                                       | 358 ms: 1.35x faster                                                                |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                              |
| pathlib                  | 21.4 ms                                                      | 16.1 ms: 1.33x faster                                                               |
| tornado_http             | 157 ms                                                       | 118 ms: 1.33x faster                                                                |
| thrift                   | 1.18 ms                                                      | 888 us: 1.32x faster                                                                |
| bench_thread_pool        | 1.14 ms                                                      | 869 us: 1.31x faster                                                                |
| xml_etree_process        | 75.9 ms                                                      | 58.7 ms: 1.29x faster                                                               |
| tomli_loads              | 2.92 sec                                                     | 2.28 sec: 1.28x faster                                                              |
| pprint_pformat           | 2.15 sec                                                     | 1.69 sec: 1.28x faster                                                              |
| pprint_safe_repr         | 1.05 sec                                                     | 827 ms: 1.27x faster                                                                |
| django_template          | 50.2 ms                                                      | 39.6 ms: 1.27x faster                                                               |
| nqueens                  | 115 ms                                                       | 90.9 ms: 1.26x faster                                                               |
| html5lib                 | 94.6 ms                                                      | 75.4 ms: 1.26x faster                                                               |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.24x faster                                                                |
| genshi_text              | 31.4 ms                                                      | 25.7 ms: 1.22x faster                                                               |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                               |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.21x faster                                                                |
| sympy_str                | 360 ms                                                       | 297 ms: 1.21x faster                                                                |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.21x faster                                                               |
| 2to3                     | 350 ms                                                       | 289 ms: 1.21x faster                                                                |
| mdp                      | 3.01 sec                                                     | 2.51 sec: 1.20x faster                                                              |
| sqlglot_optimize         | 70.1 ms                                                      | 58.7 ms: 1.19x faster                                                               |
| sympy_expand             | 600 ms                                                       | 503 ms: 1.19x faster                                                                |
| scimark_fft              | 361 ms                                                       | 305 ms: 1.18x faster                                                                |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.30 ms: 1.18x faster                                                               |
| genshi_xml               | 63.3 ms                                                      | 55.1 ms: 1.15x faster                                                               |
| docutils                 | 3.41 sec                                                     | 2.99 sec: 1.14x faster                                                              |
| async_generators         | 421 ms                                                       | 368 ms: 1.14x faster                                                                |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                                |
| meteor_contest           | 138 ms                                                       | 125 ms: 1.10x faster                                                                |
| xml_etree_generate       | 92.3 ms                                                      | 84.2 ms: 1.10x faster                                                               |
| json                     | 5.86 ms                                                      | 5.37 ms: 1.09x faster                                                               |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                                                |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.08x faster                                                                |
| regex_v8                 | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                               |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                                |
| telco                    | 7.23 ms                                                      | 8.01 ms: 1.11x slower                                                               |
| create_gc_cycles         | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                               |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                               |
| regex_effbot             | 3.09 ms                                                      | 3.66 ms: 1.19x slower                                                               |
| python_startup_no_site   | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                               |
| coverage                 | 63.3 ms                                                      | 80.3 ms: 1.27x slower                                                               |
| gc_traversal             | 3.42 ms                                                      | 4.44 ms: 1.30x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                        |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240819-3.14.0a0-852115b/bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.13x