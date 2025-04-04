# Results vs. 3.10.4

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: linux-x86_64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.466x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 249 ms: 1.40x faster                                                   |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                 |
| html5lib       | 88.9 ms                                                | 60.8 ms: 1.46x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 613 ms: 2.88x faster                                                   |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.78x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 480 ms: 2.12x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 91.3 ms: 1.68x faster                                                  |
| float          | 117 ms                                                 | 70.2 ms: 1.67x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.42x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 124 ms: 1.51x faster                                                   |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.35 ms: 1.08x faster                                                  |
| regex_dna      | 227 ms                                                 | 214 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.53x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 83.8 ms: 1.19x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.9 ms: 1.17x faster                                                  |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 8.17 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.0 ms: 1.51x faster                                                  |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                  |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 48.7 ms: 1.36x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.29x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 613 ms: 2.88x faster                                                   |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.78x faster                                                   |
| generators               | 80.1 ms                                                | 29.9 ms: 2.67x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.31 ms: 2.39x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                                 |
| go                       | 240 ms                                                 | 111 ms: 2.16x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 480 ms: 2.12x faster                                                   |
| chaos                    | 115 ms                                                 | 56.5 ms: 2.04x faster                                                  |
| logging_silent           | 190 ns                                                 | 94.4 ns: 2.01x faster                                                  |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 1.99x faster                                                  |
| raytrace                 | 507 ms                                                 | 258 ms: 1.97x faster                                                   |
| richards_super           | 94.7 ms                                                | 49.3 ms: 1.92x faster                                                  |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.92x faster                                                   |
| deepcopy                 | 479 us                                                 | 253 us: 1.89x faster                                                   |
| richards                 | 79.3 ms                                                | 43.0 ms: 1.84x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 66.2 ms: 1.79x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 73.0 ms: 1.75x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.14 ms: 1.69x faster                                                  |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                   |
| nbody                    | 154 ms                                                 | 91.3 ms: 1.68x faster                                                  |
| float                    | 117 ms                                                 | 70.2 ms: 1.67x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                 |
| pyflate                  | 716 ms                                                 | 445 ms: 1.61x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.53x faster                                                   |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                   |
| regex_compile            | 188 ms                                                 | 124 ms: 1.51x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.76 us: 1.51x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                  |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.51x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                  |
| logging_format           | 9.09 us                                                | 6.12 us: 1.49x faster                                                  |
| html5lib                 | 88.9 ms                                                | 60.8 ms: 1.46x faster                                                  |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.43x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 59.5 ms: 1.42x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 724 ms: 1.41x faster                                                   |
| 2to3                     | 348 ms                                                 | 249 ms: 1.40x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.64 ms: 1.39x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                  |
| scimark_fft              | 466 ms                                                 | 340 ms: 1.37x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 48.7 ms: 1.36x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                  |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.31x faster                                                   |
| nqueens                  | 106 ms                                                 | 81.7 ms: 1.29x faster                                                  |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                   |
| fannkuch                 | 532 ms                                                 | 413 ms: 1.29x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                  |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 83.8 ms: 1.19x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 98.9 ms: 1.17x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                  |
| async_generators         | 444 ms                                                 | 391 ms: 1.13x faster                                                   |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 877 us: 1.13x faster                                                   |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.35 ms: 1.08x faster                                                  |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                  |
| regex_dna                | 227 ms                                                 | 214 ms: 1.06x faster                                                   |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| coverage                 | 79.4 ms                                                | 84.4 ms: 1.06x slower                                                  |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.17 ms: 1.38x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 5.02 ms: 1.39x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                           |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-275056a/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.466x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.27x