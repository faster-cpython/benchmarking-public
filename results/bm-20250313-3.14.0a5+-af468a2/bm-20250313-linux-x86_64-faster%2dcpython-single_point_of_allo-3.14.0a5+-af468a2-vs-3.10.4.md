# Results vs. 3.10.4

- fork: faster-cpython
- ref: single_point_of_allo
- machine: linux-x86_64
- commit hash: af468a2
- commit date: 2025-03-13
- overall geometric mean: 1.365x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.28x faster                                                             |
| docutils       | 3.30 sec                                               | 2.71 sec: 1.21x faster                                                           |
| html5lib       | 88.9 ms                                                | 63.2 ms: 1.41x faster                                                            |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 617 ms: 2.87x faster                                                             |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 336 ms: 2.59x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 499 ms: 2.04x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 75.7 ms: 1.55x faster                                                            |
| nbody          | 154 ms                                                 | 124 ms: 1.24x faster                                                             |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.41x faster                                                             |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.53 ms: 1.03x faster                                                            |
| regex_dna      | 227 ms                                                 | 227 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                             |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                                             |
| tomli_loads          | 3.14 sec                                               | 2.13 sec: 1.47x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 60.5 ms: 1.31x faster                                                            |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                                             |
| xml_etree_generate   | 99.4 ms                                                | 87.5 ms: 1.14x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 103 ms: 1.12x faster                                                             |
| json_loads           | 31.2 us                                                | 32.6 us: 1.05x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.25x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.3 ms: 1.10x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 8.30 ms: 1.40x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.48x faster                                                            |
| django_template | 48.2 ms                                                | 33.6 ms: 1.43x faster                                                            |
| genshi_text     | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 52.5 ms: 1.26x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 183 us: 2.97x faster                                                             |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 617 ms: 2.87x faster                                                             |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 336 ms: 2.59x faster                                                             |
| deltablue                | 7.91 ms                                                | 3.21 ms: 2.46x faster                                                            |
| go                       | 240 ms                                                 | 117 ms: 2.06x faster                                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 499 ms: 2.04x faster                                                             |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                            |
| pylint                   | 551 ms                                                 | 289 ms: 1.91x faster                                                             |
| richards_super           | 94.7 ms                                                | 50.3 ms: 1.88x faster                                                            |
| richards                 | 79.3 ms                                                | 43.8 ms: 1.81x faster                                                            |
| chaos                    | 115 ms                                                 | 65.3 ms: 1.77x faster                                                            |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                                             |
| deepcopy                 | 479 us                                                 | 272 us: 1.76x faster                                                             |
| raytrace                 | 507 ms                                                 | 298 ms: 1.70x faster                                                             |
| crypto_pyaes             | 128 ms                                                 | 75.3 ms: 1.70x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                                            |
| comprehensions           | 28.8 us                                                | 17.5 us: 1.64x faster                                                            |
| scimark_sor              | 220 ms                                                 | 136 ms: 1.61x faster                                                             |
| scimark_monte_carlo      | 118 ms                                                 | 76.0 ms: 1.56x faster                                                            |
| float                    | 117 ms                                                 | 75.7 ms: 1.55x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                             |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                            |
| pyflate                  | 716 ms                                                 | 479 ms: 1.50x faster                                                             |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                                             |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.48x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.13 sec: 1.47x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.76 us: 1.44x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.91 us: 1.43x faster                                                            |
| django_template          | 48.2 ms                                                | 33.6 ms: 1.43x faster                                                            |
| regex_compile            | 188 ms                                                 | 134 ms: 1.41x faster                                                             |
| html5lib                 | 88.9 ms                                                | 63.2 ms: 1.41x faster                                                            |
| logging_format           | 9.09 us                                                | 6.51 us: 1.40x faster                                                            |
| genshi_text              | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                            |
| scimark_lu               | 176 ms                                                 | 128 ms: 1.38x faster                                                             |
| dulwich_log              | 84.3 ms                                                | 61.4 ms: 1.37x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 757 ms: 1.34x faster                                                             |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                           |
| spectral_norm            | 170 ms                                                 | 127 ms: 1.34x faster                                                             |
| xml_etree_process        | 79.1 ms                                                | 60.5 ms: 1.31x faster                                                            |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.9 ms: 1.31x faster                                                            |
| thrift                   | 1.07 ms                                                | 828 us: 1.29x faster                                                             |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.29x faster                                                           |
| 2to3                     | 348 ms                                                 | 271 ms: 1.28x faster                                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 136 ms: 1.27x faster                                                             |
| genshi_xml               | 66.0 ms                                                | 52.5 ms: 1.26x faster                                                            |
| sympy_sum                | 196 ms                                                 | 157 ms: 1.25x faster                                                             |
| sympy_integrate          | 25.8 ms                                                | 20.6 ms: 1.25x faster                                                            |
| nbody                    | 154 ms                                                 | 124 ms: 1.24x faster                                                             |
| docutils                 | 3.30 sec                                               | 2.71 sec: 1.21x faster                                                           |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                            |
| sympy_str                | 346 ms                                                 | 293 ms: 1.18x faster                                                             |
| nqueens                  | 106 ms                                                 | 89.7 ms: 1.18x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                                             |
| pathlib                  | 20.5 ms                                                | 17.6 ms: 1.16x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                            |
| fannkuch                 | 532 ms                                                 | 467 ms: 1.14x faster                                                             |
| xml_etree_generate       | 99.4 ms                                                | 87.5 ms: 1.14x faster                                                            |
| sympy_expand             | 566 ms                                                 | 501 ms: 1.13x faster                                                             |
| xml_etree_iterparse      | 115 ms                                                 | 103 ms: 1.12x faster                                                             |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                           |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                             |
| scimark_fft              | 466 ms                                                 | 423 ms: 1.10x faster                                                             |
| python_startup           | 14.6 ms                                                | 13.3 ms: 1.10x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 906 us: 1.09x faster                                                             |
| sqlite_synth             | 3.02 us                                                | 2.93 us: 1.03x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.53 ms: 1.03x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.40 ms: 1.01x faster                                                            |
| regex_dna                | 227 ms                                                 | 227 ms: 1.00x slower                                                             |
| json                     | 5.69 ms                                                | 5.77 ms: 1.01x slower                                                            |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                                             |
| json_loads               | 31.2 us                                                | 32.6 us: 1.05x slower                                                            |
| coverage                 | 79.4 ms                                                | 85.4 ms: 1.07x slower                                                            |
| telco                    | 7.27 ms                                                | 8.13 ms: 1.12x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 4.75 ms: 1.31x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 8.30 ms: 1.40x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 84.9 ms: 3.53x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                                     |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250313-3.14.0a5+-af468a2/bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.365x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.27x