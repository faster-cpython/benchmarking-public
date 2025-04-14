# Results vs. 3.10.4

- fork: faster-cpython
- ref: account_for_escapes_
- machine: linux-x86_64
- commit hash: de9adc3
- commit date: 2025-02-06
- overall geometric mean: 1.345x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.22x faster                                                                   |
| docutils       | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                                 |
| html5lib       | 94.6 ms                                                      | 67.6 ms: 1.40x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 658 ms: 2.43x faster                                                                   |
| async_tree_none         | 692 ms                                                       | 290 ms: 2.39x faster                                                                   |
| async_tree_memoization  | 819 ms                                                       | 353 ms: 2.32x faster                                                                   |
| async_tree_cpu_io_mixed | 936 ms                                                       | 523 ms: 1.79x faster                                                                   |
| Geometric mean          | (ref)                                                        | 2.22x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.3 ms: 1.58x faster                                                                  |
| nbody          | 134 ms                                                       | 90.8 ms: 1.48x faster                                                                  |
| pidigits       | 271 ms                                                       | 254 ms: 1.06x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.41x faster                                                                   |
| regex_dna      | 261 ms                                                       | 231 ms: 1.13x faster                                                                   |
| regex_v8       | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                                  |
| regex_effbot   | 3.09 ms                                                      | 3.11 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 211 us: 1.48x faster                                                                   |
| tomli_loads          | 2.92 sec                                                     | 2.09 sec: 1.39x faster                                                                 |
| pickle_pure_python   | 455 us                                                       | 329 us: 1.38x faster                                                                   |
| xml_etree_process    | 75.9 ms                                                      | 60.2 ms: 1.26x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 11.8 ms: 1.24x faster                                                                  |
| xml_etree_parse      | 160 ms                                                       | 139 ms: 1.15x faster                                                                   |
| json_loads           | 30.3 us                                                      | 26.5 us: 1.14x faster                                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 98.7 ms: 1.12x faster                                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 83.9 ms: 1.10x faster                                                                  |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                                  |
| python_startup         | 11.5 ms                                                      | 16.2 ms: 1.40x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.9 ms: 1.40x faster                                                                  |
| mako            | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                                  |
| genshi_text     | 31.4 ms                                                      | 24.7 ms: 1.27x faster                                                                  |
| genshi_xml      | 63.3 ms                                                      | 57.9 ms: 1.09x faster                                                                  |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.16x faster                                                                   |
| async_tree_io            | 1.60 sec                                                     | 658 ms: 2.43x faster                                                                   |
| async_tree_none          | 692 ms                                                       | 290 ms: 2.39x faster                                                                   |
| async_tree_memoization   | 819 ms                                                       | 353 ms: 2.32x faster                                                                   |
| deltablue                | 7.50 ms                                                      | 3.33 ms: 2.25x faster                                                                  |
| go                       | 262 ms                                                       | 127 ms: 2.05x faster                                                                   |
| generators               | 57.3 ms                                                      | 29.2 ms: 1.96x faster                                                                  |
| chaos                    | 109 ms                                                       | 60.0 ms: 1.81x faster                                                                  |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 523 ms: 1.79x faster                                                                   |
| pylint                   | 566 ms                                                       | 317 ms: 1.78x faster                                                                   |
| scimark_lu               | 167 ms                                                       | 94.1 ms: 1.77x faster                                                                  |
| raytrace                 | 489 ms                                                       | 277 ms: 1.77x faster                                                                   |
| logging_silent           | 167 ns                                                       | 96.9 ns: 1.73x faster                                                                  |
| richards_super           | 90.6 ms                                                      | 52.9 ms: 1.71x faster                                                                  |
| spectral_norm            | 139 ms                                                       | 83.1 ms: 1.67x faster                                                                  |
| pyflate                  | 733 ms                                                       | 439 ms: 1.67x faster                                                                   |
| sqlglot_parse            | 2.24 ms                                                      | 1.35 ms: 1.65x faster                                                                  |
| scimark_monte_carlo      | 107 ms                                                       | 65.4 ms: 1.64x faster                                                                  |
| deepcopy_memo            | 49.8 us                                                      | 30.5 us: 1.63x faster                                                                  |
| scimark_sor              | 180 ms                                                       | 111 ms: 1.63x faster                                                                   |
| deepcopy                 | 468 us                                                       | 288 us: 1.62x faster                                                                   |
| richards                 | 75.1 ms                                                      | 47.0 ms: 1.60x faster                                                                  |
| crypto_pyaes             | 119 ms                                                       | 75.4 ms: 1.58x faster                                                                  |
| float                    | 111 ms                                                       | 70.3 ms: 1.58x faster                                                                  |
| comprehensions           | 26.7 us                                                      | 17.2 us: 1.55x faster                                                                  |
| sqlglot_transpile        | 2.68 ms                                                      | 1.74 ms: 1.54x faster                                                                  |
| hexiom                   | 9.42 ms                                                      | 6.16 ms: 1.53x faster                                                                  |
| nbody                    | 134 ms                                                       | 90.8 ms: 1.48x faster                                                                  |
| unpickle_pure_python     | 312 us                                                       | 211 us: 1.48x faster                                                                   |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.44x faster                                                                  |
| logging_simple           | 8.88 us                                                      | 6.20 us: 1.43x faster                                                                  |
| regex_compile            | 190 ms                                                       | 135 ms: 1.41x faster                                                                   |
| logging_format           | 9.64 us                                                      | 6.87 us: 1.40x faster                                                                  |
| html5lib                 | 94.6 ms                                                      | 67.6 ms: 1.40x faster                                                                  |
| django_template          | 50.2 ms                                                      | 35.9 ms: 1.40x faster                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.09 sec: 1.39x faster                                                                 |
| pickle_pure_python       | 455 us                                                       | 329 us: 1.38x faster                                                                   |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                                  |
| deepcopy_reduce          | 4.01 us                                                      | 2.95 us: 1.36x faster                                                                  |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.36x faster                                                                  |
| thrift                   | 1.18 ms                                                      | 870 us: 1.35x faster                                                                   |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                                 |
| pprint_safe_repr         | 1.05 sec                                                     | 792 ms: 1.32x faster                                                                   |
| sqlalchemy_declarative   | 190 ms                                                       | 143 ms: 1.32x faster                                                                   |
| fannkuch                 | 483 ms                                                       | 366 ms: 1.32x faster                                                                   |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.32x faster                                                                 |
| nqueens                  | 115 ms                                                       | 88.9 ms: 1.29x faster                                                                  |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.8 ms: 1.28x faster                                                                  |
| genshi_text              | 31.4 ms                                                      | 24.7 ms: 1.27x faster                                                                  |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                                   |
| xml_etree_process        | 75.9 ms                                                      | 60.2 ms: 1.26x faster                                                                  |
| json_dumps               | 14.5 ms                                                      | 11.8 ms: 1.24x faster                                                                  |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                                   |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.24x faster                                                                   |
| mdp                      | 3.01 sec                                                     | 2.46 sec: 1.22x faster                                                                 |
| 2to3                     | 350 ms                                                       | 286 ms: 1.22x faster                                                                   |
| sqlglot_optimize         | 70.1 ms                                                      | 57.5 ms: 1.22x faster                                                                  |
| sympy_integrate          | 28.2 ms                                                      | 23.1 ms: 1.22x faster                                                                  |
| dulwich_log              | 81.1 ms                                                      | 67.0 ms: 1.21x faster                                                                  |
| sympy_expand             | 600 ms                                                       | 497 ms: 1.21x faster                                                                   |
| bench_thread_pool        | 1.14 ms                                                      | 957 us: 1.19x faster                                                                   |
| docutils                 | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                                 |
| xml_etree_parse          | 160 ms                                                       | 139 ms: 1.15x faster                                                                   |
| scimark_fft              | 361 ms                                                       | 313 ms: 1.15x faster                                                                   |
| json_loads               | 30.3 us                                                      | 26.5 us: 1.14x faster                                                                  |
| regex_dna                | 261 ms                                                       | 231 ms: 1.13x faster                                                                   |
| xml_etree_iterparse      | 110 ms                                                       | 98.7 ms: 1.12x faster                                                                  |
| meteor_contest           | 138 ms                                                       | 124 ms: 1.12x faster                                                                   |
| xml_etree_generate       | 92.3 ms                                                      | 83.9 ms: 1.10x faster                                                                  |
| genshi_xml               | 63.3 ms                                                      | 57.9 ms: 1.09x faster                                                                  |
| regex_v8                 | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                                  |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                                                  |
| json                     | 5.86 ms                                                      | 5.49 ms: 1.07x faster                                                                  |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.76 ms: 1.07x faster                                                                  |
| pidigits                 | 271 ms                                                       | 254 ms: 1.06x faster                                                                   |
| async_generators         | 421 ms                                                       | 405 ms: 1.04x faster                                                                   |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                                   |
| regex_effbot             | 3.09 ms                                                      | 3.11 ms: 1.01x slower                                                                  |
| telco                    | 7.23 ms                                                      | 8.11 ms: 1.12x slower                                                                  |
| coverage                 | 63.3 ms                                                      | 77.5 ms: 1.22x slower                                                                  |
| python_startup_no_site   | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                                  |
| python_startup           | 11.5 ms                                                      | 16.2 ms: 1.40x slower                                                                  |
| create_gc_cycles         | 1.76 ms                                                      | 2.76 ms: 1.56x slower                                                                  |
| gc_traversal             | 3.42 ms                                                      | 6.38 ms: 1.87x slower                                                                  |
| bench_mp_pool            | 6.37 ms                                                      | 1.64 sec: 256.59x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250206-3.14.0a4+-de9adc3/bm-20250206-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-de9adc3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.345x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.27x