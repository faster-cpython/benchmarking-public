# Results vs. 3.10.4

- fork: faster-cpython
- ref: account_for_escapes_
- machine: linux-x86_64
- commit hash: 17b3e16
- commit date: 2025-02-07
- overall geometric mean: 1.349x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                                                   |
| docutils       | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                                 |
| html5lib       | 94.6 ms                                                      | 66.7 ms: 1.42x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 654 ms: 2.44x faster                                                                   |
| async_tree_none         | 692 ms                                                       | 288 ms: 2.40x faster                                                                   |
| async_tree_memoization  | 819 ms                                                       | 353 ms: 2.32x faster                                                                   |
| async_tree_cpu_io_mixed | 936 ms                                                       | 522 ms: 1.79x faster                                                                   |
| Geometric mean          | (ref)                                                        | 2.22x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.2 ms: 1.58x faster                                                                  |
| nbody          | 134 ms                                                       | 91.6 ms: 1.46x faster                                                                  |
| pidigits       | 271 ms                                                       | 254 ms: 1.06x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 136 ms: 1.40x faster                                                                   |
| regex_dna      | 261 ms                                                       | 250 ms: 1.05x faster                                                                   |
| regex_v8       | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                                  |
| regex_effbot   | 3.09 ms                                                      | 3.19 ms: 1.03x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 206 us: 1.51x faster                                                                   |
| tomli_loads          | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                                                 |
| pickle_pure_python   | 455 us                                                       | 332 us: 1.37x faster                                                                   |
| xml_etree_process    | 75.9 ms                                                      | 58.8 ms: 1.29x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                                  |
| xml_etree_parse      | 160 ms                                                       | 135 ms: 1.19x faster                                                                   |
| xml_etree_iterparse  | 110 ms                                                       | 95.1 ms: 1.16x faster                                                                  |
| json_loads           | 30.3 us                                                      | 26.5 us: 1.14x faster                                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 82.3 ms: 1.12x faster                                                                  |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.99 ms: 1.23x slower                                                                  |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.9 ms: 1.40x faster                                                                  |
| mako            | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                                                  |
| genshi_text     | 31.4 ms                                                      | 24.4 ms: 1.29x faster                                                                  |
| genshi_xml      | 63.3 ms                                                      | 55.7 ms: 1.14x faster                                                                  |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 169 us: 3.17x faster                                                                   |
| async_tree_io            | 1.60 sec                                                     | 654 ms: 2.44x faster                                                                   |
| async_tree_none          | 692 ms                                                       | 288 ms: 2.40x faster                                                                   |
| async_tree_memoization   | 819 ms                                                       | 353 ms: 2.32x faster                                                                   |
| deltablue                | 7.50 ms                                                      | 3.37 ms: 2.23x faster                                                                  |
| go                       | 262 ms                                                       | 129 ms: 2.03x faster                                                                   |
| generators               | 57.3 ms                                                      | 30.2 ms: 1.90x faster                                                                  |
| chaos                    | 109 ms                                                       | 60.2 ms: 1.80x faster                                                                  |
| pylint                   | 566 ms                                                       | 315 ms: 1.80x faster                                                                   |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 522 ms: 1.79x faster                                                                   |
| scimark_lu               | 167 ms                                                       | 94.4 ms: 1.77x faster                                                                  |
| raytrace                 | 489 ms                                                       | 277 ms: 1.77x faster                                                                   |
| scimark_monte_carlo      | 107 ms                                                       | 61.5 ms: 1.75x faster                                                                  |
| logging_silent           | 167 ns                                                       | 96.9 ns: 1.73x faster                                                                  |
| richards_super           | 90.6 ms                                                      | 53.4 ms: 1.70x faster                                                                  |
| spectral_norm            | 139 ms                                                       | 82.5 ms: 1.69x faster                                                                  |
| deepcopy_memo            | 49.8 us                                                      | 29.7 us: 1.67x faster                                                                  |
| pyflate                  | 733 ms                                                       | 439 ms: 1.67x faster                                                                   |
| deepcopy                 | 468 us                                                       | 282 us: 1.66x faster                                                                   |
| scimark_sor              | 180 ms                                                       | 109 ms: 1.66x faster                                                                   |
| sqlglot_parse            | 2.24 ms                                                      | 1.36 ms: 1.65x faster                                                                  |
| richards                 | 75.1 ms                                                      | 46.7 ms: 1.61x faster                                                                  |
| crypto_pyaes             | 119 ms                                                       | 75.0 ms: 1.59x faster                                                                  |
| float                    | 111 ms                                                       | 70.2 ms: 1.58x faster                                                                  |
| comprehensions           | 26.7 us                                                      | 17.0 us: 1.57x faster                                                                  |
| sqlglot_transpile        | 2.68 ms                                                      | 1.74 ms: 1.54x faster                                                                  |
| hexiom                   | 9.42 ms                                                      | 6.16 ms: 1.53x faster                                                                  |
| unpickle_pure_python     | 312 us                                                       | 206 us: 1.51x faster                                                                   |
| nbody                    | 134 ms                                                       | 91.6 ms: 1.46x faster                                                                  |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.44x faster                                                                  |
| html5lib                 | 94.6 ms                                                      | 66.7 ms: 1.42x faster                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                                                 |
| regex_compile            | 190 ms                                                       | 136 ms: 1.40x faster                                                                   |
| django_template          | 50.2 ms                                                      | 35.9 ms: 1.40x faster                                                                  |
| pickle_pure_python       | 455 us                                                       | 332 us: 1.37x faster                                                                   |
| pathlib                  | 21.4 ms                                                      | 15.6 ms: 1.37x faster                                                                  |
| logging_simple           | 8.88 us                                                      | 6.50 us: 1.36x faster                                                                  |
| thrift                   | 1.18 ms                                                      | 863 us: 1.36x faster                                                                   |
| pprint_pformat           | 2.15 sec                                                     | 1.58 sec: 1.36x faster                                                                 |
| deepcopy_reduce          | 4.01 us                                                      | 2.96 us: 1.35x faster                                                                  |
| pprint_safe_repr         | 1.05 sec                                                     | 776 ms: 1.35x faster                                                                   |
| logging_format           | 9.64 us                                                      | 7.14 us: 1.35x faster                                                                  |
| mako                     | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                                                  |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                                 |
| fannkuch                 | 483 ms                                                       | 364 ms: 1.33x faster                                                                   |
| sqlalchemy_declarative   | 190 ms                                                       | 144 ms: 1.32x faster                                                                   |
| xml_etree_process        | 75.9 ms                                                      | 58.8 ms: 1.29x faster                                                                  |
| genshi_text              | 31.4 ms                                                      | 24.4 ms: 1.29x faster                                                                  |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.8 ms: 1.28x faster                                                                  |
| nqueens                  | 115 ms                                                       | 89.9 ms: 1.28x faster                                                                  |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                                   |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                                  |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                                   |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.24x faster                                                                   |
| bench_thread_pool        | 1.14 ms                                                      | 928 us: 1.23x faster                                                                   |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                                                   |
| dulwich_log              | 81.1 ms                                                      | 66.3 ms: 1.22x faster                                                                  |
| sqlglot_optimize         | 70.1 ms                                                      | 57.4 ms: 1.22x faster                                                                  |
| sympy_integrate          | 28.2 ms                                                      | 23.1 ms: 1.22x faster                                                                  |
| sympy_expand             | 600 ms                                                       | 495 ms: 1.21x faster                                                                   |
| mdp                      | 3.01 sec                                                     | 2.48 sec: 1.21x faster                                                                 |
| scimark_fft              | 361 ms                                                       | 303 ms: 1.19x faster                                                                   |
| docutils                 | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                                 |
| xml_etree_parse          | 160 ms                                                       | 135 ms: 1.19x faster                                                                   |
| xml_etree_iterparse      | 110 ms                                                       | 95.1 ms: 1.16x faster                                                                  |
| json_loads               | 30.3 us                                                      | 26.5 us: 1.14x faster                                                                  |
| genshi_xml               | 63.3 ms                                                      | 55.7 ms: 1.14x faster                                                                  |
| xml_etree_generate       | 92.3 ms                                                      | 82.3 ms: 1.12x faster                                                                  |
| meteor_contest           | 138 ms                                                       | 124 ms: 1.12x faster                                                                   |
| json                     | 5.86 ms                                                      | 5.46 ms: 1.07x faster                                                                  |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.73 ms: 1.07x faster                                                                  |
| pidigits                 | 271 ms                                                       | 254 ms: 1.06x faster                                                                   |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.06x faster                                                                  |
| regex_dna                | 261 ms                                                       | 250 ms: 1.05x faster                                                                   |
| async_generators         | 421 ms                                                       | 402 ms: 1.05x faster                                                                   |
| regex_v8                 | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                                  |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                                   |
| regex_effbot             | 3.09 ms                                                      | 3.19 ms: 1.03x slower                                                                  |
| telco                    | 7.23 ms                                                      | 8.04 ms: 1.11x slower                                                                  |
| python_startup_no_site   | 7.33 ms                                                      | 8.99 ms: 1.23x slower                                                                  |
| coverage                 | 63.3 ms                                                      | 78.3 ms: 1.24x slower                                                                  |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                                  |
| create_gc_cycles         | 1.76 ms                                                      | 2.76 ms: 1.56x slower                                                                  |
| gc_traversal             | 3.42 ms                                                      | 6.12 ms: 1.79x slower                                                                  |
| bench_mp_pool            | 6.37 ms                                                      | 1.03 sec: 161.72x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250207-3.14.0a4+-17b3e16/bm-20250207-pythonperf2-x86_64-faster%2dcpython-account_for_escapes_-3.14.0a4+-17b3e16.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.349x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.27x