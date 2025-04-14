# Results vs. 3.10.4

- fork: faster-cpython
- ref: c_recursion_limit
- machine: linux-x86_64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.452x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                          |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                        |
| html5lib       | 88.9 ms                                                | 61.2 ms: 1.45x faster                                                         |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 621 ms: 2.85x faster                                                          |
| async_tree_none         | 728 ms                                                 | 265 ms: 2.74x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 323 ms: 2.69x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.57x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.9 ms: 1.65x faster                                                         |
| nbody          | 154 ms                                                 | 93.6 ms: 1.64x faster                                                         |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                  | 1.41x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                          |
| regex_effbot   | 3.63 ms                                                | 3.15 ms: 1.15x faster                                                         |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                         |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                        |
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 58.8 ms: 1.35x faster                                                         |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                          |
| xml_etree_iterparse  | 115 ms                                                 | 97.4 ms: 1.19x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 84.5 ms: 1.18x faster                                                         |
| json_loads           | 31.2 us                                                | 30.4 us: 1.03x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.0 ms: 1.51x faster                                                         |
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                         |
| genshi_text     | 31.8 ms                                                | 21.6 ms: 1.47x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 158 us: 3.45x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 621 ms: 2.85x faster                                                          |
| generators               | 80.1 ms                                                | 28.4 ms: 2.82x faster                                                         |
| async_tree_none          | 728 ms                                                 | 265 ms: 2.74x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 323 ms: 2.69x faster                                                          |
| deltablue                | 7.91 ms                                                | 3.15 ms: 2.51x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                          |
| go                       | 240 ms                                                 | 115 ms: 2.08x faster                                                          |
| pylint                   | 551 ms                                                 | 274 ms: 2.01x faster                                                          |
| chaos                    | 115 ms                                                 | 57.7 ms: 2.00x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.95x faster                                                         |
| richards_super           | 94.7 ms                                                | 49.8 ms: 1.90x faster                                                         |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                                          |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                          |
| logging_silent           | 190 ns                                                 | 103 ns: 1.85x faster                                                          |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                          |
| richards                 | 79.3 ms                                                | 43.6 ms: 1.82x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 66.5 ms: 1.78x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 72.6 ms: 1.76x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                                         |
| spectral_norm            | 170 ms                                                 | 96.9 ms: 1.75x faster                                                         |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.73x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.15 ms: 1.69x faster                                                         |
| float                    | 117 ms                                                 | 70.9 ms: 1.65x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.56 ms: 1.65x faster                                                         |
| nbody                    | 154 ms                                                 | 93.6 ms: 1.64x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                        |
| pyflate                  | 716 ms                                                 | 455 ms: 1.57x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                          |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                                         |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.51x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.49 us: 1.51x faster                                                         |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                          |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.51x faster                                                         |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                         |
| logging_format           | 9.09 us                                                | 6.07 us: 1.50x faster                                                         |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                         |
| genshi_text              | 31.8 ms                                                | 21.6 ms: 1.47x faster                                                         |
| html5lib                 | 88.9 ms                                                | 61.2 ms: 1.45x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.42x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 719 ms: 1.41x faster                                                          |
| thrift                   | 1.07 ms                                                | 767 us: 1.40x faster                                                          |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                        |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                          |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.37x faster                                                          |
| scimark_fft              | 466 ms                                                 | 342 ms: 1.36x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 58.8 ms: 1.35x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.34x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.83 ms: 1.34x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                         |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                          |
| sqlglot_optimize         | 69.2 ms                                                | 52.3 ms: 1.32x faster                                                         |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                          |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 64.3 ms: 1.31x faster                                                         |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                                          |
| nqueens                  | 106 ms                                                 | 81.7 ms: 1.30x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                        |
| sympy_expand             | 566 ms                                                 | 453 ms: 1.25x faster                                                          |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                         |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 97.4 ms: 1.19x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 84.5 ms: 1.18x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.15 ms: 1.15x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                                        |
| async_generators         | 444 ms                                                 | 389 ms: 1.14x faster                                                          |
| bench_thread_pool        | 986 us                                                 | 866 us: 1.14x faster                                                          |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.13x faster                                                          |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                                         |
| json                     | 5.69 ms                                                | 5.38 ms: 1.06x faster                                                         |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                          |
| json_loads               | 31.2 us                                                | 30.4 us: 1.03x faster                                                         |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                          |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                          |
| telco                    | 7.27 ms                                                | 7.75 ms: 1.07x slower                                                         |
| coverage                 | 79.4 ms                                                | 90.8 ms: 1.14x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 4.93 ms: 1.36x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                         |
| bench_mp_pool            | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                  |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250217-3.14.0a5+-21366c3/bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.452x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.26x