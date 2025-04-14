# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.443x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                   |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                 |
| html5lib       | 88.9 ms                                                | 62.8 ms: 1.42x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 613 ms: 2.89x faster                                                   |
| async_tree_none         | 728 ms                                                 | 258 ms: 2.82x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 482 ms: 2.11x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.9 ms: 1.63x faster                                                  |
| nbody          | 154 ms                                                 | 99.0 ms: 1.55x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                                   |
| regex_v8       | 27.8 ms                                                | 23.6 ms: 1.17x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.10 ms: 1.17x faster                                                  |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 59.1 ms: 1.34x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 85.6 ms: 1.16x faster                                                  |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                  |
| unpickle_list        | 5.20 us                                                | 5.30 us: 1.02x slower                                                  |
| pickle_list          | 5.08 us                                                | 5.38 us: 1.06x slower                                                  |
| pickle_dict          | 29.6 us                                                | 34.3 us: 1.16x slower                                                  |
| pickle               | 10.7 us                                                | 13.0 us: 1.22x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 8.17 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.3 ms: 1.54x faster                                                  |
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                  |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.33x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 613 ms: 2.89x faster                                                   |
| async_tree_none          | 728 ms                                                 | 258 ms: 2.82x faster                                                   |
| generators               | 80.1 ms                                                | 28.7 ms: 2.79x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.09 ms: 2.56x faster                                                  |
| go                       | 240 ms                                                 | 113 ms: 2.13x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 482 ms: 2.11x faster                                                   |
| logging_silent           | 190 ns                                                 | 93.7 ns: 2.03x faster                                                  |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.98x faster                                                  |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 476 ms: 1.94x faster                                                   |
| raytrace                 | 507 ms                                                 | 266 ms: 1.91x faster                                                   |
| richards_super           | 94.7 ms                                                | 49.9 ms: 1.90x faster                                                  |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                   |
| deepcopy                 | 479 us                                                 | 260 us: 1.85x faster                                                   |
| richards                 | 79.3 ms                                                | 43.9 ms: 1.81x faster                                                  |
| spectral_norm            | 170 ms                                                 | 96.4 ms: 1.76x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 67.5 ms: 1.75x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 75.7 ms: 1.69x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.21 ms: 1.68x faster                                                  |
| float                    | 117 ms                                                 | 71.9 ms: 1.63x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                 |
| pyflate                  | 716 ms                                                 | 447 ms: 1.60x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                  |
| nbody                    | 154 ms                                                 | 99.0 ms: 1.55x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                                   |
| django_template          | 48.2 ms                                                | 31.3 ms: 1.54x faster                                                  |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.53 us: 1.50x faster                                                  |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                  |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 58.3 ms: 1.45x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                 |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                  |
| html5lib                 | 88.9 ms                                                | 62.8 ms: 1.42x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.41x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.40x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.39x faster                                                   |
| thrift                   | 1.07 ms                                                | 775 us: 1.38x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.75 ms: 1.36x faster                                                  |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.1 ms: 1.34x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                  |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                   |
| scimark_fft              | 466 ms                                                 | 352 ms: 1.32x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                   |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                 |
| nqueens                  | 106 ms                                                 | 83.6 ms: 1.27x faster                                                  |
| fannkuch                 | 532 ms                                                 | 422 ms: 1.26x faster                                                   |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| unpack_sequence          | 60.0 ns                                                | 50.9 ns: 1.18x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 23.6 ms: 1.17x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.10 ms: 1.17x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 85.6 ms: 1.16x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 869 us: 1.13x faster                                                   |
| async_generators         | 444 ms                                                 | 395 ms: 1.12x faster                                                   |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                  |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                  |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                   |
| json                     | 5.69 ms                                                | 5.37 ms: 1.06x faster                                                  |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| unpickle_list            | 5.20 us                                                | 5.30 us: 1.02x slower                                                  |
| pickle_list              | 5.08 us                                                | 5.38 us: 1.06x slower                                                  |
| telco                    | 7.27 ms                                                | 7.94 ms: 1.09x slower                                                  |
| coverage                 | 79.4 ms                                                | 91.6 ms: 1.15x slower                                                  |
| pickle_dict              | 29.6 us                                                | 34.3 us: 1.16x slower                                                  |
| pickle                   | 10.7 us                                                | 13.0 us: 1.22x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.82 ms: 1.33x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.17 ms: 1.38x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 82.8 ms: 3.45x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                           |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.443x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x