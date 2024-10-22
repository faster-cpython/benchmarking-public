# Results vs. 3.10.4

- fork: faster-cpython
- ref: spill_before_escapin
- machine: linux-x86_64
- commit hash: e5d0e67
- commit date: 2024-09-17
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 310 ms: 1.13x faster                                                                  |
| docutils       | 3.41 sec                                                     | 3.17 sec: 1.08x faster                                                                |
| html5lib       | 94.6 ms                                                      | 72.0 ms: 1.31x faster                                                                 |
| tornado_http   | 157 ms                                                       | 122 ms: 1.28x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 325 ms: 2.13x faster                                                                  |
| async_tree_memoization  | 819 ms                                                       | 406 ms: 2.02x faster                                                                  |
| async_tree_io           | 1.60 sec                                                     | 814 ms: 1.96x faster                                                                  |
| async_tree_cpu_io_mixed | 936 ms                                                       | 579 ms: 1.62x faster                                                                  |
| Geometric mean          | (ref)                                                        | 1.92x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 78.2 ms: 1.72x faster                                                                 |
| float          | 111 ms                                                       | 76.7 ms: 1.45x faster                                                                 |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.39x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 148 ms: 1.29x faster                                                                  |
| regex_dna      | 261 ms                                                       | 252 ms: 1.03x faster                                                                  |
| regex_v8       | 27.2 ms                                                      | 26.2 ms: 1.03x faster                                                                 |
| regex_effbot   | 3.09 ms                                                      | 3.58 ms: 1.16x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 215 us: 1.45x faster                                                                  |
| pickle_pure_python   | 455 us                                                       | 325 us: 1.40x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 10.5 ms: 1.39x faster                                                                 |
| tomli_loads          | 2.92 sec                                                     | 2.13 sec: 1.37x faster                                                                |
| xml_etree_process    | 75.9 ms                                                      | 55.8 ms: 1.36x faster                                                                 |
| json_loads           | 30.3 us                                                      | 23.9 us: 1.27x faster                                                                 |
| xml_etree_generate   | 92.3 ms                                                      | 80.7 ms: 1.14x faster                                                                 |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.13x faster                                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 97.8 ms: 1.13x faster                                                                 |
| pickle               | 9.89 us                                                      | 10.6 us: 1.07x slower                                                                 |
| pickle_dict          | 29.5 us                                                      | 31.9 us: 1.08x slower                                                                 |
| pickle_list          | 4.12 us                                                      | 4.52 us: 1.10x slower                                                                 |
| unpickle             | 13.5 us                                                      | 14.9 us: 1.10x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.15x faster                                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                                 |
| python_startup_no_site | 7.33 ms                                                      | 8.99 ms: 1.23x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.23 ms: 1.59x faster                                                                 |
| django_template | 50.2 ms                                                      | 43.6 ms: 1.15x faster                                                                 |
| genshi_text     | 31.4 ms                                                      | 29.9 ms: 1.05x faster                                                                 |
| genshi_xml      | 63.3 ms                                                      | 65.0 ms: 1.03x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.17x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 184 us: 2.92x faster                                                                  |
| deltablue                | 7.50 ms                                                      | 3.19 ms: 2.35x faster                                                                 |
| async_tree_none          | 692 ms                                                       | 325 ms: 2.13x faster                                                                  |
| asyncio_tcp              | 779 ms                                                       | 376 ms: 2.07x faster                                                                  |
| async_tree_memoization   | 819 ms                                                       | 406 ms: 2.02x faster                                                                  |
| async_tree_io            | 1.60 sec                                                     | 814 ms: 1.96x faster                                                                  |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                                |
| richards_super           | 90.6 ms                                                      | 49.7 ms: 1.82x faster                                                                 |
| deepcopy_memo            | 49.8 us                                                      | 28.3 us: 1.76x faster                                                                 |
| richards                 | 75.1 ms                                                      | 42.8 ms: 1.76x faster                                                                 |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.75x faster                                                                  |
| scimark_lu               | 167 ms                                                       | 96.3 ms: 1.73x faster                                                                 |
| spectral_norm            | 139 ms                                                       | 80.4 ms: 1.73x faster                                                                 |
| crypto_pyaes             | 119 ms                                                       | 68.8 ms: 1.73x faster                                                                 |
| go                       | 262 ms                                                       | 151 ms: 1.73x faster                                                                  |
| nbody                    | 134 ms                                                       | 78.2 ms: 1.72x faster                                                                 |
| logging_silent           | 167 ns                                                       | 102 ns: 1.64x faster                                                                  |
| chaos                    | 109 ms                                                       | 66.4 ms: 1.64x faster                                                                 |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 579 ms: 1.62x faster                                                                  |
| mako                     | 14.7 ms                                                      | 9.23 ms: 1.59x faster                                                                 |
| scimark_monte_carlo      | 107 ms                                                       | 67.7 ms: 1.59x faster                                                                 |
| deepcopy                 | 468 us                                                       | 300 us: 1.56x faster                                                                  |
| pyflate                  | 733 ms                                                       | 476 ms: 1.54x faster                                                                  |
| generators               | 57.3 ms                                                      | 37.3 ms: 1.53x faster                                                                 |
| sqlglot_parse            | 2.24 ms                                                      | 1.49 ms: 1.50x faster                                                                 |
| raytrace                 | 489 ms                                                       | 328 ms: 1.49x faster                                                                  |
| comprehensions           | 26.7 us                                                      | 18.2 us: 1.47x faster                                                                 |
| unpickle_pure_python     | 312 us                                                       | 215 us: 1.45x faster                                                                  |
| float                    | 111 ms                                                       | 76.7 ms: 1.45x faster                                                                 |
| coroutines               | 30.3 ms                                                      | 21.6 ms: 1.40x faster                                                                 |
| pickle_pure_python       | 455 us                                                       | 325 us: 1.40x faster                                                                  |
| json_dumps               | 14.5 ms                                                      | 10.5 ms: 1.39x faster                                                                 |
| sqlglot_transpile        | 2.68 ms                                                      | 1.94 ms: 1.38x faster                                                                 |
| pylint                   | 566 ms                                                       | 411 ms: 1.38x faster                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.13 sec: 1.37x faster                                                                |
| xml_etree_process        | 75.9 ms                                                      | 55.8 ms: 1.36x faster                                                                 |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                                                 |
| fannkuch                 | 483 ms                                                       | 357 ms: 1.35x faster                                                                  |
| hexiom                   | 9.42 ms                                                      | 6.99 ms: 1.35x faster                                                                 |
| logging_simple           | 8.88 us                                                      | 6.60 us: 1.34x faster                                                                 |
| deepcopy_reduce          | 4.01 us                                                      | 2.99 us: 1.34x faster                                                                 |
| logging_format           | 9.64 us                                                      | 7.21 us: 1.34x faster                                                                 |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                                |
| thrift                   | 1.18 ms                                                      | 892 us: 1.32x faster                                                                  |
| pprint_safe_repr         | 1.05 sec                                                     | 797 ms: 1.32x faster                                                                  |
| html5lib                 | 94.6 ms                                                      | 72.0 ms: 1.31x faster                                                                 |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                                                |
| regex_compile            | 190 ms                                                       | 148 ms: 1.29x faster                                                                  |
| tornado_http             | 157 ms                                                       | 122 ms: 1.28x faster                                                                  |
| json_loads               | 30.3 us                                                      | 23.9 us: 1.27x faster                                                                 |
| scimark_fft              | 361 ms                                                       | 288 ms: 1.26x faster                                                                  |
| dulwich_log              | 81.1 ms                                                      | 65.0 ms: 1.25x faster                                                                 |
| bench_thread_pool        | 1.14 ms                                                      | 924 us: 1.24x faster                                                                  |
| bench_mp_pool            | 6.37 ms                                                      | 5.19 ms: 1.23x faster                                                                 |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.20 ms: 1.21x faster                                                                 |
| mdp                      | 3.01 sec                                                     | 2.55 sec: 1.18x faster                                                                |
| django_template          | 50.2 ms                                                      | 43.6 ms: 1.15x faster                                                                 |
| sympy_str                | 360 ms                                                       | 313 ms: 1.15x faster                                                                  |
| xml_etree_generate       | 92.3 ms                                                      | 80.7 ms: 1.14x faster                                                                 |
| sympy_expand             | 600 ms                                                       | 525 ms: 1.14x faster                                                                  |
| nqueens                  | 115 ms                                                       | 101 ms: 1.14x faster                                                                  |
| sympy_sum                | 193 ms                                                       | 170 ms: 1.13x faster                                                                  |
| sqlglot_normalize        | 144 ms                                                       | 127 ms: 1.13x faster                                                                  |
| xml_etree_parse          | 160 ms                                                       | 142 ms: 1.13x faster                                                                  |
| 2to3                     | 350 ms                                                       | 310 ms: 1.13x faster                                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 97.8 ms: 1.13x faster                                                                 |
| json                     | 5.86 ms                                                      | 5.22 ms: 1.12x faster                                                                 |
| sqlite_synth             | 2.99 us                                                      | 2.70 us: 1.11x faster                                                                 |
| async_generators         | 421 ms                                                       | 386 ms: 1.09x faster                                                                  |
| sqlglot_optimize         | 70.1 ms                                                      | 64.5 ms: 1.09x faster                                                                 |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                                  |
| docutils                 | 3.41 sec                                                     | 3.17 sec: 1.08x faster                                                                |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.07x faster                                                                  |
| sympy_integrate          | 28.2 ms                                                      | 26.7 ms: 1.05x faster                                                                 |
| genshi_text              | 31.4 ms                                                      | 29.9 ms: 1.05x faster                                                                 |
| regex_dna                | 261 ms                                                       | 252 ms: 1.03x faster                                                                  |
| regex_v8                 | 27.2 ms                                                      | 26.2 ms: 1.03x faster                                                                 |
| asyncio_websockets       | 390 ms                                                       | 393 ms: 1.01x slower                                                                  |
| genshi_xml               | 63.3 ms                                                      | 65.0 ms: 1.03x slower                                                                 |
| pickle                   | 9.89 us                                                      | 10.6 us: 1.07x slower                                                                 |
| create_gc_cycles         | 1.76 ms                                                      | 1.89 ms: 1.07x slower                                                                 |
| pickle_dict              | 29.5 us                                                      | 31.9 us: 1.08x slower                                                                 |
| pickle_list              | 4.12 us                                                      | 4.52 us: 1.10x slower                                                                 |
| unpickle                 | 13.5 us                                                      | 14.9 us: 1.10x slower                                                                 |
| telco                    | 7.23 ms                                                      | 8.01 ms: 1.11x slower                                                                 |
| regex_effbot             | 3.09 ms                                                      | 3.58 ms: 1.16x slower                                                                 |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                                 |
| python_startup_no_site   | 7.33 ms                                                      | 8.99 ms: 1.23x slower                                                                 |
| gc_traversal             | 3.42 ms                                                      | 4.36 ms: 1.28x slower                                                                 |
| coverage                 | 63.3 ms                                                      | 81.2 ms: 1.28x slower                                                                 |
| unpack_sequence          | 59.9 ns                                                      | 88.0 ns: 1.47x slower                                                                 |
| Geometric mean           | (ref)                                                        | 1.29x faster                                                                          |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240917-3.14.0a0-e5d0e67-JIT/bm-20240917-pythonperf2-x86_64-faster%2dcpython-spill_before_escapin-3.14.0a0-e5d0e67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.22x