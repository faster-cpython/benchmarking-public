# Results vs. 3.10.4

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 584015a
- commit date: 2025-01-23
- overall geometric mean: 1.351x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                                                   |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                                 |
| html5lib       | 94.6 ms                                                      | 66.4 ms: 1.43x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 653 ms: 2.45x faster                                                                   |
| async_tree_none         | 692 ms                                                       | 288 ms: 2.40x faster                                                                   |
| async_tree_memoization  | 819 ms                                                       | 351 ms: 2.33x faster                                                                   |
| async_tree_cpu_io_mixed | 936 ms                                                       | 517 ms: 1.81x faster                                                                   |
| Geometric mean          | (ref)                                                        | 2.23x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.3 ms: 1.60x faster                                                                  |
| nbody          | 134 ms                                                       | 86.6 ms: 1.55x faster                                                                  |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.39x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 134 ms: 1.42x faster                                                                   |
| regex_v8       | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                                  |
| regex_dna      | 261 ms                                                       | 244 ms: 1.07x faster                                                                   |
| regex_effbot   | 3.09 ms                                                      | 3.12 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 208 us: 1.50x faster                                                                   |
| tomli_loads          | 2.92 sec                                                     | 2.05 sec: 1.43x faster                                                                 |
| pickle_pure_python   | 455 us                                                       | 323 us: 1.41x faster                                                                   |
| xml_etree_process    | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 11.7 ms: 1.24x faster                                                                  |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                                                  |
| xml_etree_parse      | 160 ms                                                       | 134 ms: 1.19x faster                                                                   |
| xml_etree_generate   | 92.3 ms                                                      | 84.1 ms: 1.10x faster                                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                                   |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.98 ms: 1.23x slower                                                                  |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 37.0 ms: 1.36x faster                                                                  |
| genshi_text     | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                                  |
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                                  |
| genshi_xml      | 63.3 ms                                                      | 52.3 ms: 1.21x faster                                                                  |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 168 us: 3.19x faster                                                                   |
| async_tree_io            | 1.60 sec                                                     | 653 ms: 2.45x faster                                                                   |
| async_tree_none          | 692 ms                                                       | 288 ms: 2.40x faster                                                                   |
| async_tree_memoization   | 819 ms                                                       | 351 ms: 2.33x faster                                                                   |
| deltablue                | 7.50 ms                                                      | 3.43 ms: 2.19x faster                                                                  |
| generators               | 57.3 ms                                                      | 28.2 ms: 2.03x faster                                                                  |
| go                       | 262 ms                                                       | 130 ms: 2.01x faster                                                                   |
| chaos                    | 109 ms                                                       | 58.8 ms: 1.85x faster                                                                  |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 517 ms: 1.81x faster                                                                   |
| raytrace                 | 489 ms                                                       | 272 ms: 1.80x faster                                                                   |
| scimark_lu               | 167 ms                                                       | 94.3 ms: 1.77x faster                                                                  |
| pylint                   | 566 ms                                                       | 322 ms: 1.76x faster                                                                   |
| logging_silent           | 167 ns                                                       | 97.4 ns: 1.72x faster                                                                  |
| scimark_monte_carlo      | 107 ms                                                       | 62.8 ms: 1.71x faster                                                                  |
| sqlglot_parse            | 2.24 ms                                                      | 1.33 ms: 1.69x faster                                                                  |
| pyflate                  | 733 ms                                                       | 438 ms: 1.67x faster                                                                   |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                                                   |
| spectral_norm            | 139 ms                                                       | 84.3 ms: 1.65x faster                                                                  |
| scimark_sor              | 180 ms                                                       | 110 ms: 1.64x faster                                                                   |
| crypto_pyaes             | 119 ms                                                       | 72.6 ms: 1.64x faster                                                                  |
| deepcopy_memo            | 49.8 us                                                      | 30.4 us: 1.64x faster                                                                  |
| float                    | 111 ms                                                       | 69.3 ms: 1.60x faster                                                                  |
| hexiom                   | 9.42 ms                                                      | 5.91 ms: 1.59x faster                                                                  |
| sqlglot_transpile        | 2.68 ms                                                      | 1.71 ms: 1.56x faster                                                                  |
| nbody                    | 134 ms                                                       | 86.6 ms: 1.55x faster                                                                  |
| comprehensions           | 26.7 us                                                      | 17.7 us: 1.50x faster                                                                  |
| unpickle_pure_python     | 312 us                                                       | 208 us: 1.50x faster                                                                   |
| coroutines               | 30.3 ms                                                      | 20.6 ms: 1.47x faster                                                                  |
| richards_super           | 90.6 ms                                                      | 62.3 ms: 1.45x faster                                                                  |
| html5lib                 | 94.6 ms                                                      | 66.4 ms: 1.43x faster                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.05 sec: 1.43x faster                                                                 |
| regex_compile            | 190 ms                                                       | 134 ms: 1.42x faster                                                                   |
| logging_simple           | 8.88 us                                                      | 6.28 us: 1.41x faster                                                                  |
| pickle_pure_python       | 455 us                                                       | 323 us: 1.41x faster                                                                   |
| logging_format           | 9.64 us                                                      | 6.86 us: 1.40x faster                                                                  |
| deepcopy_reduce          | 4.01 us                                                      | 2.90 us: 1.38x faster                                                                  |
| pprint_pformat           | 2.15 sec                                                     | 1.57 sec: 1.37x faster                                                                 |
| richards                 | 75.1 ms                                                      | 55.3 ms: 1.36x faster                                                                  |
| django_template          | 50.2 ms                                                      | 37.0 ms: 1.36x faster                                                                  |
| genshi_text              | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                                  |
| mako                     | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                                  |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                                                  |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                                 |
| pprint_safe_repr         | 1.05 sec                                                     | 782 ms: 1.34x faster                                                                   |
| thrift                   | 1.18 ms                                                      | 880 us: 1.34x faster                                                                   |
| sqlalchemy_declarative   | 190 ms                                                       | 143 ms: 1.33x faster                                                                   |
| fannkuch                 | 483 ms                                                       | 366 ms: 1.32x faster                                                                   |
| nqueens                  | 115 ms                                                       | 88.8 ms: 1.30x faster                                                                  |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.7 ms: 1.29x faster                                                                  |
| xml_etree_process        | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                                  |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                                   |
| sympy_str                | 360 ms                                                       | 288 ms: 1.25x faster                                                                   |
| json_dumps               | 14.5 ms                                                      | 11.7 ms: 1.24x faster                                                                  |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.24x faster                                                                   |
| mdp                      | 3.01 sec                                                     | 2.43 sec: 1.24x faster                                                                 |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                                                   |
| dulwich_log              | 81.1 ms                                                      | 65.7 ms: 1.23x faster                                                                  |
| sympy_expand             | 600 ms                                                       | 490 ms: 1.22x faster                                                                   |
| bench_thread_pool        | 1.14 ms                                                      | 933 us: 1.22x faster                                                                   |
| sqlglot_optimize         | 70.1 ms                                                      | 57.5 ms: 1.22x faster                                                                  |
| sympy_integrate          | 28.2 ms                                                      | 23.1 ms: 1.22x faster                                                                  |
| genshi_xml               | 63.3 ms                                                      | 52.3 ms: 1.21x faster                                                                  |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.20x faster                                                                  |
| xml_etree_parse          | 160 ms                                                       | 134 ms: 1.19x faster                                                                   |
| scimark_fft              | 361 ms                                                       | 305 ms: 1.19x faster                                                                   |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                                 |
| json                     | 5.86 ms                                                      | 5.34 ms: 1.10x faster                                                                  |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                                   |
| xml_etree_generate       | 92.3 ms                                                      | 84.1 ms: 1.10x faster                                                                  |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.66 ms: 1.09x faster                                                                  |
| regex_v8                 | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                                  |
| regex_dna                | 261 ms                                                       | 244 ms: 1.07x faster                                                                   |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                                   |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.06x faster                                                                   |
| async_generators         | 421 ms                                                       | 400 ms: 1.05x faster                                                                   |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                                   |
| regex_effbot             | 3.09 ms                                                      | 3.12 ms: 1.01x slower                                                                  |
| telco                    | 7.23 ms                                                      | 7.66 ms: 1.06x slower                                                                  |
| python_startup_no_site   | 7.33 ms                                                      | 8.98 ms: 1.23x slower                                                                  |
| coverage                 | 63.3 ms                                                      | 77.7 ms: 1.23x slower                                                                  |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                                  |
| create_gc_cycles         | 1.76 ms                                                      | 2.79 ms: 1.58x slower                                                                  |
| gc_traversal             | 3.42 ms                                                      | 6.41 ms: 1.88x slower                                                                  |
| bench_mp_pool            | 6.37 ms                                                      | 2.02 sec: 316.50x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250123-3.14.0a4+-584015a/bm-20250123-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.351x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.27x