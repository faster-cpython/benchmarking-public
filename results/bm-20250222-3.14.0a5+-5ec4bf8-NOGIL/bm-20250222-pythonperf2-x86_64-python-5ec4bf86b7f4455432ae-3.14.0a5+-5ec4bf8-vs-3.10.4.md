# Results vs. 3.10.4

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-x86_64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.209x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.53x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 329 ms: 1.06x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                                       |
| html5lib       | 94.6 ms                                                      | 74.1 ms: 1.28x faster                                                        |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 589 ms: 2.71x faster                                                         |
| async_tree_none         | 692 ms                                                       | 284 ms: 2.44x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 350 ms: 2.34x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 517 ms: 1.81x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.30x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 74.7 ms: 1.49x faster                                                        |
| pidigits       | 271 ms                                                       | 248 ms: 1.09x faster                                                         |
| nbody          | 134 ms                                                       | 129 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 160 ms: 1.18x faster                                                         |
| regex_dna      | 261 ms                                                       | 245 ms: 1.07x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.18 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 239 us: 1.30x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 365 us: 1.25x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 90.9 ms: 1.22x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.43 sec: 1.20x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 13.2 ms: 1.10x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 71.2 ms: 1.07x faster                                                        |
| json_loads           | 30.3 us                                                      | 28.7 us: 1.06x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 98.0 ms: 1.06x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 33.4 us: 1.13x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.77 us: 1.16x slower                                                        |
| unpickle             | 13.5 us                                                      | 15.9 us: 1.18x slower                                                        |
| pickle               | 9.89 us                                                      | 11.9 us: 1.21x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 5.63 us: 1.21x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                        |
| python_startup         | 11.5 ms                                                      | 19.1 ms: 1.66x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.63x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 45.6 ms: 1.10x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 29.8 ms: 1.05x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 64.3 ms: 1.02x slower                                                        |
| mako            | 14.7 ms                                                      | 17.6 ms: 1.20x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 589 ms: 2.71x faster                                                         |
| typing_runtime_protocols | 537 us                                                       | 219 us: 2.45x faster                                                         |
| async_tree_none          | 692 ms                                                       | 284 ms: 2.44x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 350 ms: 2.34x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.97 ms: 1.89x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 422 ms: 1.85x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 517 ms: 1.81x faster                                                         |
| generators               | 57.3 ms                                                      | 32.1 ms: 1.78x faster                                                        |
| go                       | 262 ms                                                       | 151 ms: 1.73x faster                                                         |
| logging_silent           | 167 ns                                                       | 100 ns: 1.67x faster                                                         |
| gc_traversal             | 3.42 ms                                                      | 2.05 ms: 1.67x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.88 sec: 1.65x faster                                                       |
| pylint                   | 566 ms                                                       | 348 ms: 1.63x faster                                                         |
| chaos                    | 109 ms                                                       | 69.5 ms: 1.56x faster                                                        |
| scimark_sor              | 180 ms                                                       | 117 ms: 1.54x faster                                                         |
| pyflate                  | 733 ms                                                       | 487 ms: 1.50x faster                                                         |
| float                    | 111 ms                                                       | 74.7 ms: 1.49x faster                                                        |
| coroutines               | 30.3 ms                                                      | 20.6 ms: 1.47x faster                                                        |
| raytrace                 | 489 ms                                                       | 334 ms: 1.47x faster                                                         |
| spectral_norm            | 139 ms                                                       | 96.3 ms: 1.44x faster                                                        |
| deepcopy                 | 468 us                                                       | 329 us: 1.42x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 35.2 us: 1.41x faster                                                        |
| scimark_lu               | 167 ms                                                       | 119 ms: 1.40x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                       |
| richards_super           | 90.6 ms                                                      | 66.8 ms: 1.36x faster                                                        |
| comprehensions           | 26.7 us                                                      | 19.7 us: 1.35x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.65 ms: 1.35x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 2.06 ms: 1.30x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 239 us: 1.30x faster                                                         |
| richards                 | 75.1 ms                                                      | 57.6 ms: 1.30x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 91.8 ms: 1.30x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 7.31 ms: 1.29x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 74.1 ms: 1.28x faster                                                        |
| logging_simple           | 8.88 us                                                      | 7.07 us: 1.26x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 365 us: 1.25x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 17.3 ms: 1.23x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.85 us: 1.23x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 90.9 ms: 1.22x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 88.5 ms: 1.21x faster                                                        |
| thrift                   | 1.18 ms                                                      | 975 us: 1.21x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.43 sec: 1.20x faster                                                       |
| regex_compile            | 190 ms                                                       | 160 ms: 1.18x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 69.8 ms: 1.16x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.58 us: 1.16x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 911 ms: 1.15x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.89 sec: 1.14x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.54 us: 1.13x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 20.3 ms: 1.12x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 129 ms: 1.11x faster                                                         |
| sympy_sum                | 193 ms                                                       | 174 ms: 1.11x faster                                                         |
| sqlalchemy_declarative   | 190 ms                                                       | 171 ms: 1.11x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 13.2 ms: 1.10x faster                                                        |
| django_template          | 50.2 ms                                                      | 45.6 ms: 1.10x faster                                                        |
| pidigits                 | 271 ms                                                       | 248 ms: 1.09x faster                                                         |
| sympy_str                | 360 ms                                                       | 335 ms: 1.07x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.81 sec: 1.07x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 71.2 ms: 1.07x faster                                                        |
| regex_dna                | 261 ms                                                       | 245 ms: 1.07x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 65.8 ms: 1.07x faster                                                        |
| 2to3                     | 350 ms                                                       | 329 ms: 1.06x faster                                                         |
| sympy_expand             | 600 ms                                                       | 565 ms: 1.06x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                                        |
| json_loads               | 30.3 us                                                      | 28.7 us: 1.06x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 29.8 ms: 1.05x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 26.9 ms: 1.05x faster                                                        |
| scimark_fft              | 361 ms                                                       | 347 ms: 1.04x faster                                                         |
| json                     | 5.86 ms                                                      | 5.66 ms: 1.04x faster                                                        |
| nbody                    | 134 ms                                                       | 129 ms: 1.04x faster                                                         |
| nqueens                  | 115 ms                                                       | 111 ms: 1.03x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 379 ms: 1.03x faster                                                         |
| fannkuch                 | 483 ms                                                       | 480 ms: 1.01x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 64.3 ms: 1.02x slower                                                        |
| unpack_sequence          | 59.9 ns                                                      | 61.4 ns: 1.03x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.18 ms: 1.03x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 98.0 ms: 1.06x slower                                                        |
| async_generators         | 421 ms                                                       | 466 ms: 1.11x slower                                                         |
| meteor_contest           | 138 ms                                                       | 153 ms: 1.11x slower                                                         |
| create_gc_cycles         | 1.76 ms                                                      | 1.96 ms: 1.11x slower                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.68 ms: 1.12x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 33.4 us: 1.13x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.77 us: 1.16x slower                                                        |
| unpickle                 | 13.5 us                                                      | 15.9 us: 1.18x slower                                                        |
| mako                     | 14.7 ms                                                      | 17.6 ms: 1.20x slower                                                        |
| pickle                   | 9.89 us                                                      | 11.9 us: 1.21x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.63 us: 1.21x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.44 ms: 1.26x slower                                                        |
| telco                    | 7.23 ms                                                      | 9.23 ms: 1.28x slower                                                        |
| coverage                 | 63.3 ms                                                      | 102 ms: 1.61x slower                                                         |
| python_startup_no_site   | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                        |
| python_startup           | 11.5 ms                                                      | 19.1 ms: 1.66x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 48.9 ms: 7.67x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.16x faster                                                                 |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (11) of results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.209x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.53x