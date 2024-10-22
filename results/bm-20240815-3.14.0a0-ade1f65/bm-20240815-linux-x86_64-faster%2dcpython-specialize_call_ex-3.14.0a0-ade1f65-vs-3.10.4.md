# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_call_ex
- machine: linux-x86_64
- commit hash: ade1f65
- commit date: 2024-08-15
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                                          |
| docutils       | 3.30 sec                                               | 2.72 sec: 1.21x faster                                                        |
| html5lib       | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                         |
| tornado_http   | 136 ms                                                 | 90.1 ms: 1.51x faster                                                         |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.23x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 425 ms: 2.05x faster                                                          |
| async_tree_io           | 1.77 sec                                               | 908 ms: 1.95x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 570 ms: 1.78x faster                                                          |
| Geometric mean          | (ref)                                                  | 1.99x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.9 ms: 1.77x faster                                                         |
| float          | 117 ms                                                 | 79.8 ms: 1.47x faster                                                         |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.38x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                                          |
| regex_v8       | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                         |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                  |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 306 us: 1.58x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                          |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                        |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 86.2 ms: 1.15x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                          |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                          |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 7.03 ms: 1.18x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                         |
| django_template | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                         |
| genshi_text     | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 50.5 ms: 1.31x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                          |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.25 ms: 2.44x faster                                                         |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.23x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 425 ms: 2.05x faster                                                          |
| chaos                    | 115 ms                                                 | 58.5 ms: 1.97x faster                                                         |
| raytrace                 | 507 ms                                                 | 259 ms: 1.95x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 908 ms: 1.95x faster                                                          |
| asyncio_tcp              | 922 ms                                                 | 479 ms: 1.93x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 30.9 us: 1.89x faster                                                         |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                                          |
| deepcopy                 | 479 us                                                 | 267 us: 1.79x faster                                                          |
| richards_super           | 94.7 ms                                                | 52.8 ms: 1.79x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 570 ms: 1.78x faster                                                          |
| nbody                    | 154 ms                                                 | 86.9 ms: 1.77x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 73.1 ms: 1.75x faster                                                         |
| pylint                   | 551 ms                                                 | 316 ms: 1.74x faster                                                          |
| scimark_monte_carlo      | 118 ms                                                 | 68.6 ms: 1.72x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                         |
| richards                 | 79.3 ms                                                | 46.4 ms: 1.71x faster                                                         |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                          |
| go                       | 240 ms                                                 | 142 ms: 1.69x faster                                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.69x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.17 ms: 1.68x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.62x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 306 us: 1.58x faster                                                          |
| spectral_norm            | 170 ms                                                 | 109 ms: 1.55x faster                                                          |
| pyflate                  | 716 ms                                                 | 462 ms: 1.55x faster                                                          |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                          |
| tornado_http             | 136 ms                                                 | 90.1 ms: 1.51x faster                                                         |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                        |
| logging_format           | 9.09 us                                                | 6.09 us: 1.49x faster                                                         |
| float                    | 117 ms                                                 | 79.8 ms: 1.47x faster                                                         |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                                        |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                                          |
| django_template          | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                         |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                         |
| genshi_text              | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                         |
| thrift                   | 1.07 ms                                                | 783 us: 1.37x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                                        |
| html5lib                 | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                         |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 754 ms: 1.35x faster                                                          |
| fannkuch                 | 532 ms                                                 | 396 ms: 1.34x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                         |
| nqueens                  | 106 ms                                                 | 79.2 ms: 1.34x faster                                                         |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                                          |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.33x faster                                                          |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 50.5 ms: 1.31x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.31x faster                                                         |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                          |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 53.8 ms: 1.29x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.07 ms: 1.28x faster                                                         |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                                          |
| bench_thread_pool        | 986 us                                                 | 785 us: 1.26x faster                                                          |
| scimark_fft              | 466 ms                                                 | 374 ms: 1.25x faster                                                          |
| sympy_expand             | 566 ms                                                 | 465 ms: 1.22x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.72 sec: 1.21x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 86.2 ms: 1.15x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                        |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                          |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                         |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                         |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                          |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                          |
| gc_traversal             | 3.62 ms                                                | 3.82 ms: 1.06x slower                                                         |
| coverage                 | 79.4 ms                                                | 84.7 ms: 1.07x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                         |
| telco                    | 7.27 ms                                                | 8.16 ms: 1.12x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.03 ms: 1.18x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                  |

Benchmark hidden because not significant (4): regex_effbot, bench_mp_pool, async_generators, asyncio_websockets
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240815-3.14.0a0-ade1f65/bm-20240815-linux-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-ade1f65.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.13x