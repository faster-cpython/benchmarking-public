# Results vs. 3.10.4

- fork: faster-cpython
- ref: account_for_escapes_
- machine: linux-x86_64
- commit hash: f62123f
- commit date: 2025-02-06
- overall geometric mean: 1.351x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                                                   |
| docutils       | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                                 |
| html5lib       | 94.6 ms                                                      | 67.8 ms: 1.40x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 661 ms: 2.42x faster                                                                   |
| async_tree_none         | 692 ms                                                       | 288 ms: 2.40x faster                                                                   |
| async_tree_memoization  | 819 ms                                                       | 354 ms: 2.32x faster                                                                   |
| async_tree_cpu_io_mixed | 936 ms                                                       | 523 ms: 1.79x faster                                                                   |
| Geometric mean          | (ref)                                                        | 2.21x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.6 ms: 1.55x faster                                                                  |
| nbody          | 134 ms                                                       | 91.4 ms: 1.47x faster                                                                  |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.41x faster                                                                   |
| regex_dna      | 261 ms                                                       | 244 ms: 1.07x faster                                                                   |
| regex_v8       | 27.2 ms                                                      | 26.6 ms: 1.02x faster                                                                  |
| regex_effbot   | 3.09 ms                                                      | 3.17 ms: 1.03x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 209 us: 1.49x faster                                                                   |
| tomli_loads          | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                                 |
| pickle_pure_python   | 455 us                                                       | 329 us: 1.38x faster                                                                   |
| xml_etree_process    | 75.9 ms                                                      | 59.7 ms: 1.27x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 11.8 ms: 1.23x faster                                                                  |
| xml_etree_parse      | 160 ms                                                       | 134 ms: 1.19x faster                                                                   |
| json_loads           | 30.3 us                                                      | 26.4 us: 1.15x faster                                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 96.5 ms: 1.15x faster                                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 83.9 ms: 1.10x faster                                                                  |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                                  |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 34.8 ms: 1.44x faster                                                                  |
| mako            | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                                  |
| genshi_text     | 31.4 ms                                                      | 24.4 ms: 1.29x faster                                                                  |
| genshi_xml      | 63.3 ms                                                      | 55.7 ms: 1.14x faster                                                                  |
| Geometric mean  | (ref)                                                        | 1.30x faster                                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 167 us: 3.21x faster                                                                   |
| async_tree_io            | 1.60 sec                                                     | 661 ms: 2.42x faster                                                                   |
| async_tree_none          | 692 ms                                                       | 288 ms: 2.40x faster                                                                   |
| async_tree_memoization   | 819 ms                                                       | 354 ms: 2.32x faster                                                                   |
| deltablue                | 7.50 ms                                                      | 3.34 ms: 2.25x faster                                                                  |
| go                       | 262 ms                                                       | 126 ms: 2.07x faster                                                                   |
| generators               | 57.3 ms                                                      | 28.7 ms: 2.00x faster                                                                  |
| pylint                   | 566 ms                                                       | 315 ms: 1.80x faster                                                                   |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 523 ms: 1.79x faster                                                                   |
| chaos                    | 109 ms                                                       | 60.8 ms: 1.79x faster                                                                  |
| raytrace                 | 489 ms                                                       | 275 ms: 1.78x faster                                                                   |
| scimark_monte_carlo      | 107 ms                                                       | 60.8 ms: 1.77x faster                                                                  |
| scimark_lu               | 167 ms                                                       | 95.1 ms: 1.76x faster                                                                  |
| richards_super           | 90.6 ms                                                      | 52.4 ms: 1.73x faster                                                                  |
| logging_silent           | 167 ns                                                       | 96.9 ns: 1.73x faster                                                                  |
| pyflate                  | 733 ms                                                       | 439 ms: 1.67x faster                                                                   |
| scimark_sor              | 180 ms                                                       | 108 ms: 1.67x faster                                                                   |
| spectral_norm            | 139 ms                                                       | 83.5 ms: 1.67x faster                                                                  |
| deepcopy_memo            | 49.8 us                                                      | 30.1 us: 1.65x faster                                                                  |
| deepcopy                 | 468 us                                                       | 283 us: 1.65x faster                                                                   |
| sqlglot_parse            | 2.24 ms                                                      | 1.36 ms: 1.65x faster                                                                  |
| richards                 | 75.1 ms                                                      | 46.2 ms: 1.63x faster                                                                  |
| crypto_pyaes             | 119 ms                                                       | 73.6 ms: 1.62x faster                                                                  |
| hexiom                   | 9.42 ms                                                      | 6.06 ms: 1.55x faster                                                                  |
| comprehensions           | 26.7 us                                                      | 17.2 us: 1.55x faster                                                                  |
| float                    | 111 ms                                                       | 71.6 ms: 1.55x faster                                                                  |
| sqlglot_transpile        | 2.68 ms                                                      | 1.74 ms: 1.54x faster                                                                  |
| unpickle_pure_python     | 312 us                                                       | 209 us: 1.49x faster                                                                   |
| nbody                    | 134 ms                                                       | 91.4 ms: 1.47x faster                                                                  |
| logging_simple           | 8.88 us                                                      | 6.15 us: 1.44x faster                                                                  |
| django_template          | 50.2 ms                                                      | 34.8 ms: 1.44x faster                                                                  |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.43x faster                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                                 |
| logging_format           | 9.64 us                                                      | 6.79 us: 1.42x faster                                                                  |
| regex_compile            | 190 ms                                                       | 135 ms: 1.41x faster                                                                   |
| html5lib                 | 94.6 ms                                                      | 67.8 ms: 1.40x faster                                                                  |
| pickle_pure_python       | 455 us                                                       | 329 us: 1.38x faster                                                                   |
| pathlib                  | 21.4 ms                                                      | 15.5 ms: 1.38x faster                                                                  |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                                 |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                                  |
| thrift                   | 1.18 ms                                                      | 865 us: 1.36x faster                                                                   |
| deepcopy_reduce          | 4.01 us                                                      | 2.96 us: 1.35x faster                                                                  |
| fannkuch                 | 483 ms                                                       | 359 ms: 1.34x faster                                                                   |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.33x faster                                                                 |
| pprint_safe_repr         | 1.05 sec                                                     | 787 ms: 1.33x faster                                                                   |
| sqlalchemy_declarative   | 190 ms                                                       | 143 ms: 1.33x faster                                                                   |
| genshi_text              | 31.4 ms                                                      | 24.4 ms: 1.29x faster                                                                  |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.7 ms: 1.29x faster                                                                  |
| nqueens                  | 115 ms                                                       | 89.8 ms: 1.28x faster                                                                  |
| xml_etree_process        | 75.9 ms                                                      | 59.7 ms: 1.27x faster                                                                  |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                                   |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                                   |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.24x faster                                                                   |
| 2to3                     | 350 ms                                                       | 284 ms: 1.23x faster                                                                   |
| json_dumps               | 14.5 ms                                                      | 11.8 ms: 1.23x faster                                                                  |
| bench_thread_pool        | 1.14 ms                                                      | 931 us: 1.23x faster                                                                   |
| sympy_expand             | 600 ms                                                       | 492 ms: 1.22x faster                                                                   |
| dulwich_log              | 81.1 ms                                                      | 66.5 ms: 1.22x faster                                                                  |
| sqlglot_optimize         | 70.1 ms                                                      | 57.7 ms: 1.22x faster                                                                  |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.22x faster                                                                  |
| mdp                      | 3.01 sec                                                     | 2.52 sec: 1.20x faster                                                                 |
| scimark_fft              | 361 ms                                                       | 303 ms: 1.19x faster                                                                   |
| xml_etree_parse          | 160 ms                                                       | 134 ms: 1.19x faster                                                                   |
| docutils                 | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                                 |
| json_loads               | 30.3 us                                                      | 26.4 us: 1.15x faster                                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 96.5 ms: 1.15x faster                                                                  |
| genshi_xml               | 63.3 ms                                                      | 55.7 ms: 1.14x faster                                                                  |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.49 ms: 1.13x faster                                                                  |
| meteor_contest           | 138 ms                                                       | 124 ms: 1.12x faster                                                                   |
| xml_etree_generate       | 92.3 ms                                                      | 83.9 ms: 1.10x faster                                                                  |
| regex_dna                | 261 ms                                                       | 244 ms: 1.07x faster                                                                   |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                                   |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.06x faster                                                                  |
| json                     | 5.86 ms                                                      | 5.52 ms: 1.06x faster                                                                  |
| async_generators         | 421 ms                                                       | 408 ms: 1.03x faster                                                                   |
| regex_v8                 | 27.2 ms                                                      | 26.6 ms: 1.02x faster                                                                  |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                                   |
| regex_effbot             | 3.09 ms                                                      | 3.17 ms: 1.03x slower                                                                  |
| telco                    | 7.23 ms                                                      | 8.01 ms: 1.11x slower                                                                  |
| coverage                 | 63.3 ms                                                      | 77.8 ms: 1.23x slower                                                                  |
| python_startup_no_site   | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                                  |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                                  |
| create_gc_cycles         | 1.76 ms                                                      | 2.79 ms: 1.58x slower                                                                  |
| gc_traversal             | 3.42 ms                                                      | 6.56 ms: 1.92x slower                                                                  |
| bench_mp_pool            | 6.37 ms                                                      | 1.08 sec: 169.87x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250206-3.14.0a4+-f62123f/bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-f62123f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.351x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.27x