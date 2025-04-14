# Results vs. 3.10.4

- fork: faster-cpython
- ref: account_for_escapes_
- machine: linux-x86_64
- commit hash: 534b694
- commit date: 2025-02-10
- overall geometric mean: 1.351x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                                                   |
| docutils       | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                                 |
| html5lib       | 94.6 ms                                                      | 68.0 ms: 1.39x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 649 ms: 2.46x faster                                                                   |
| async_tree_none         | 692 ms                                                       | 290 ms: 2.38x faster                                                                   |
| async_tree_memoization  | 819 ms                                                       | 354 ms: 2.31x faster                                                                   |
| async_tree_cpu_io_mixed | 936 ms                                                       | 521 ms: 1.80x faster                                                                   |
| Geometric mean          | (ref)                                                        | 2.22x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.3 ms: 1.58x faster                                                                  |
| nbody          | 134 ms                                                       | 90.8 ms: 1.48x faster                                                                  |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.41x faster                                                                   |
| regex_dna      | 261 ms                                                       | 242 ms: 1.08x faster                                                                   |
| regex_v8       | 27.2 ms                                                      | 26.6 ms: 1.02x faster                                                                  |
| regex_effbot   | 3.09 ms                                                      | 3.15 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 212 us: 1.47x faster                                                                   |
| tomli_loads          | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                                                 |
| pickle_pure_python   | 455 us                                                       | 330 us: 1.38x faster                                                                   |
| xml_etree_process    | 75.9 ms                                                      | 60.0 ms: 1.27x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 11.7 ms: 1.24x faster                                                                  |
| xml_etree_parse      | 160 ms                                                       | 134 ms: 1.19x faster                                                                   |
| xml_etree_iterparse  | 110 ms                                                       | 94.8 ms: 1.17x faster                                                                  |
| json_loads           | 30.3 us                                                      | 26.7 us: 1.14x faster                                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 83.7 ms: 1.10x faster                                                                  |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                                                  |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.8 ms: 1.40x faster                                                                  |
| mako            | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                                                  |
| genshi_text     | 31.4 ms                                                      | 23.9 ms: 1.32x faster                                                                  |
| genshi_xml      | 63.3 ms                                                      | 55.4 ms: 1.14x faster                                                                  |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 169 us: 3.17x faster                                                                   |
| async_tree_io            | 1.60 sec                                                     | 649 ms: 2.46x faster                                                                   |
| async_tree_none          | 692 ms                                                       | 290 ms: 2.38x faster                                                                   |
| async_tree_memoization   | 819 ms                                                       | 354 ms: 2.31x faster                                                                   |
| deltablue                | 7.50 ms                                                      | 3.35 ms: 2.24x faster                                                                  |
| go                       | 262 ms                                                       | 127 ms: 2.06x faster                                                                   |
| generators               | 57.3 ms                                                      | 29.3 ms: 1.96x faster                                                                  |
| chaos                    | 109 ms                                                       | 60.0 ms: 1.81x faster                                                                  |
| pylint                   | 566 ms                                                       | 313 ms: 1.81x faster                                                                   |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 521 ms: 1.80x faster                                                                   |
| raytrace                 | 489 ms                                                       | 275 ms: 1.78x faster                                                                   |
| scimark_lu               | 167 ms                                                       | 94.5 ms: 1.77x faster                                                                  |
| richards_super           | 90.6 ms                                                      | 51.9 ms: 1.75x faster                                                                  |
| logging_silent           | 167 ns                                                       | 96.9 ns: 1.73x faster                                                                  |
| pyflate                  | 733 ms                                                       | 426 ms: 1.72x faster                                                                   |
| deepcopy_memo            | 49.8 us                                                      | 29.1 us: 1.71x faster                                                                  |
| scimark_monte_carlo      | 107 ms                                                       | 63.3 ms: 1.70x faster                                                                  |
| scimark_sor              | 180 ms                                                       | 108 ms: 1.68x faster                                                                   |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                                                   |
| spectral_norm            | 139 ms                                                       | 83.7 ms: 1.66x faster                                                                  |
| richards                 | 75.1 ms                                                      | 45.4 ms: 1.65x faster                                                                  |
| sqlglot_parse            | 2.24 ms                                                      | 1.36 ms: 1.64x faster                                                                  |
| crypto_pyaes             | 119 ms                                                       | 73.9 ms: 1.61x faster                                                                  |
| float                    | 111 ms                                                       | 70.3 ms: 1.58x faster                                                                  |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                                                  |
| sqlglot_transpile        | 2.68 ms                                                      | 1.75 ms: 1.53x faster                                                                  |
| hexiom                   | 9.42 ms                                                      | 6.16 ms: 1.53x faster                                                                  |
| nbody                    | 134 ms                                                       | 90.8 ms: 1.48x faster                                                                  |
| unpickle_pure_python     | 312 us                                                       | 212 us: 1.47x faster                                                                   |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.43x faster                                                                  |
| logging_simple           | 8.88 us                                                      | 6.26 us: 1.42x faster                                                                  |
| regex_compile            | 190 ms                                                       | 135 ms: 1.41x faster                                                                   |
| django_template          | 50.2 ms                                                      | 35.8 ms: 1.40x faster                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                                                 |
| thrift                   | 1.18 ms                                                      | 841 us: 1.40x faster                                                                   |
| html5lib                 | 94.6 ms                                                      | 68.0 ms: 1.39x faster                                                                  |
| logging_format           | 9.64 us                                                      | 6.93 us: 1.39x faster                                                                  |
| pickle_pure_python       | 455 us                                                       | 330 us: 1.38x faster                                                                   |
| deepcopy_reduce          | 4.01 us                                                      | 2.92 us: 1.37x faster                                                                  |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                                 |
| pprint_safe_repr         | 1.05 sec                                                     | 780 ms: 1.35x faster                                                                   |
| pprint_pformat           | 2.15 sec                                                     | 1.60 sec: 1.34x faster                                                                 |
| mako                     | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                                                  |
| sqlalchemy_declarative   | 190 ms                                                       | 142 ms: 1.33x faster                                                                   |
| fannkuch                 | 483 ms                                                       | 365 ms: 1.32x faster                                                                   |
| genshi_text              | 31.4 ms                                                      | 23.9 ms: 1.32x faster                                                                  |
| pathlib                  | 21.4 ms                                                      | 16.3 ms: 1.31x faster                                                                  |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.7 ms: 1.28x faster                                                                  |
| nqueens                  | 115 ms                                                       | 89.6 ms: 1.28x faster                                                                  |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                                   |
| xml_etree_process        | 75.9 ms                                                      | 60.0 ms: 1.27x faster                                                                  |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                                   |
| json_dumps               | 14.5 ms                                                      | 11.7 ms: 1.24x faster                                                                  |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.24x faster                                                                   |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                                                   |
| sqlglot_optimize         | 70.1 ms                                                      | 57.3 ms: 1.22x faster                                                                  |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.22x faster                                                                  |
| sympy_expand             | 600 ms                                                       | 494 ms: 1.21x faster                                                                   |
| dulwich_log              | 81.1 ms                                                      | 67.0 ms: 1.21x faster                                                                  |
| bench_thread_pool        | 1.14 ms                                                      | 946 us: 1.21x faster                                                                   |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                                                 |
| xml_etree_parse          | 160 ms                                                       | 134 ms: 1.19x faster                                                                   |
| docutils                 | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                                 |
| scimark_fft              | 361 ms                                                       | 306 ms: 1.18x faster                                                                   |
| xml_etree_iterparse      | 110 ms                                                       | 94.8 ms: 1.17x faster                                                                  |
| genshi_xml               | 63.3 ms                                                      | 55.4 ms: 1.14x faster                                                                  |
| json_loads               | 30.3 us                                                      | 26.7 us: 1.14x faster                                                                  |
| meteor_contest           | 138 ms                                                       | 123 ms: 1.12x faster                                                                   |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.56 ms: 1.11x faster                                                                  |
| xml_etree_generate       | 92.3 ms                                                      | 83.7 ms: 1.10x faster                                                                  |
| json                     | 5.86 ms                                                      | 5.43 ms: 1.08x faster                                                                  |
| regex_dna                | 261 ms                                                       | 242 ms: 1.08x faster                                                                   |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                                                  |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                                   |
| regex_v8                 | 27.2 ms                                                      | 26.6 ms: 1.02x faster                                                                  |
| async_generators         | 421 ms                                                       | 413 ms: 1.02x faster                                                                   |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                                   |
| regex_effbot             | 3.09 ms                                                      | 3.15 ms: 1.02x slower                                                                  |
| telco                    | 7.23 ms                                                      | 7.76 ms: 1.07x slower                                                                  |
| python_startup_no_site   | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                                                  |
| coverage                 | 63.3 ms                                                      | 78.8 ms: 1.25x slower                                                                  |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                                  |
| create_gc_cycles         | 1.76 ms                                                      | 2.77 ms: 1.57x slower                                                                  |
| gc_traversal             | 3.42 ms                                                      | 6.35 ms: 1.86x slower                                                                  |
| bench_mp_pool            | 6.37 ms                                                      | 1.32 sec: 207.52x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250210-3.14.0a4+-534b694/bm-20250210-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-534b694.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.351x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.27x