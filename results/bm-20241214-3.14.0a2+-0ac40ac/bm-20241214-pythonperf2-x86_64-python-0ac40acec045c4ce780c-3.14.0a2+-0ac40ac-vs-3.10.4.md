# Results vs. 3.10.4

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.329x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                       |
| html5lib       | 94.6 ms                                                      | 70.8 ms: 1.34x faster                                                        |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 654 ms: 2.44x faster                                                         |
| async_tree_none         | 692 ms                                                       | 295 ms: 2.34x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 360 ms: 2.27x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 524 ms: 1.79x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.20x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 77.9 ms: 1.43x faster                                                        |
| nbody          | 134 ms                                                       | 97.3 ms: 1.38x faster                                                        |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.38x faster                                                         |
| regex_dna      | 261 ms                                                       | 248 ms: 1.05x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.24 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 218 us: 1.43x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 331 us: 1.38x faster                                                         |
| json_loads           | 30.3 us                                                      | 23.9 us: 1.27x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.27x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 60.6 ms: 1.25x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.39 sec: 1.22x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 97.0 ms: 1.14x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 84.9 ms: 1.09x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.05 ms: 1.24x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.4 ms: 1.38x faster                                                        |
| mako            | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 24.5 ms: 1.28x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 54.9 ms: 1.15x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 176 us: 3.05x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 654 ms: 2.44x faster                                                         |
| async_tree_none          | 692 ms                                                       | 295 ms: 2.34x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 360 ms: 2.27x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.50 ms: 2.14x faster                                                        |
| generators               | 57.3 ms                                                      | 28.6 ms: 2.01x faster                                                        |
| go                       | 262 ms                                                       | 133 ms: 1.96x faster                                                         |
| raytrace                 | 489 ms                                                       | 269 ms: 1.82x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 524 ms: 1.79x faster                                                         |
| pylint                   | 566 ms                                                       | 317 ms: 1.78x faster                                                         |
| chaos                    | 109 ms                                                       | 62.0 ms: 1.75x faster                                                        |
| scimark_lu               | 167 ms                                                       | 95.7 ms: 1.74x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 63.3 ms: 1.70x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.6 us: 1.68x faster                                                        |
| scimark_sor              | 180 ms                                                       | 108 ms: 1.67x faster                                                         |
| logging_silent           | 167 ns                                                       | 101 ns: 1.66x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.35 ms: 1.65x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 72.3 ms: 1.65x faster                                                        |
| deepcopy                 | 468 us                                                       | 285 us: 1.64x faster                                                         |
| richards_super           | 90.6 ms                                                      | 56.9 ms: 1.59x faster                                                        |
| spectral_norm            | 139 ms                                                       | 87.7 ms: 1.59x faster                                                        |
| pyflate                  | 733 ms                                                       | 473 ms: 1.55x faster                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 1.75 ms: 1.53x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.21 ms: 1.52x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.7 us: 1.51x faster                                                        |
| richards                 | 75.1 ms                                                      | 50.6 ms: 1.48x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.0 ms: 1.45x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 218 us: 1.43x faster                                                         |
| float                    | 111 ms                                                       | 77.9 ms: 1.43x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.37 us: 1.39x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.20 sec: 1.39x faster                                                       |
| nbody                    | 134 ms                                                       | 97.3 ms: 1.38x faster                                                        |
| django_template          | 50.2 ms                                                      | 36.4 ms: 1.38x faster                                                        |
| regex_compile            | 190 ms                                                       | 138 ms: 1.38x faster                                                         |
| logging_format           | 9.64 us                                                      | 7.00 us: 1.38x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 331 us: 1.38x faster                                                         |
| fannkuch                 | 483 ms                                                       | 353 ms: 1.37x faster                                                         |
| thrift                   | 1.18 ms                                                      | 862 us: 1.36x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 2.95 us: 1.36x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 140 ms: 1.35x faster                                                         |
| mako                     | 14.7 ms                                                      | 11.0 ms: 1.34x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.34x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 70.8 ms: 1.34x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 807 ms: 1.30x faster                                                         |
| nqueens                  | 115 ms                                                       | 88.6 ms: 1.30x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.5 ms: 1.28x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.7 ms: 1.28x faster                                                        |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.27x faster                                                         |
| json_loads               | 30.3 us                                                      | 23.9 us: 1.27x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.27x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 114 ms: 1.26x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 60.6 ms: 1.25x faster                                                        |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                                         |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                         |
| scimark_fft              | 361 ms                                                       | 295 ms: 1.22x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.46 sec: 1.22x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.39 sec: 1.22x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 938 us: 1.22x faster                                                         |
| sympy_expand             | 600 ms                                                       | 493 ms: 1.22x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 57.7 ms: 1.22x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.3 ms: 1.21x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 67.5 ms: 1.20x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                                         |
| json                     | 5.86 ms                                                      | 5.07 ms: 1.16x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 54.9 ms: 1.15x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.44 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.0 ms: 1.14x faster                                                        |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 84.9 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                        |
| regex_dna                | 261 ms                                                       | 248 ms: 1.05x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                        |
| async_generators         | 421 ms                                                       | 431 ms: 1.02x slower                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.24 ms: 1.05x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.74 ms: 1.07x slower                                                        |
| mypy2                    | 933 ms                                                       | 1.03 sec: 1.10x slower                                                       |
| coverage                 | 63.3 ms                                                      | 77.3 ms: 1.22x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.05 ms: 1.24x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.75 ms: 1.56x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.59 ms: 1.93x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.21 sec: 189.26x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.25x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-pythonperf2-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.329x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.28x