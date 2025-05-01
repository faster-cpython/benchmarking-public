# Results vs. 3.10.4

- fork: sergey-miryanov
- ref: gh_132042_optimize_c
- machine: linux-x86_64
- commit hash: 04539cc
- commit date: 2025-05-01
- overall geometric mean: 1.441x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                              |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                            |
| html5lib       | 88.9 ms                                                | 62.6 ms: 1.42x faster                                                             |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 601 ms: 2.94x faster                                                              |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                              |
| async_tree_none         | 728 ms                                                 | 264 ms: 2.76x faster                                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 499 ms: 2.04x faster                                                              |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.3 ms: 1.69x faster                                                             |
| nbody          | 154 ms                                                 | 101 ms: 1.52x faster                                                              |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                              |
| regex_v8       | 27.8 ms                                                | 22.5 ms: 1.23x faster                                                             |
| regex_effbot   | 3.63 ms                                                | 3.14 ms: 1.16x faster                                                             |
| regex_dna      | 227 ms                                                 | 208 ms: 1.09x faster                                                              |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                            |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                              |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                              |
| xml_etree_process    | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                             |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                              |
| json_dumps           | 14.2 ms                                                | 12.0 ms: 1.18x faster                                                             |
| xml_etree_iterparse  | 115 ms                                                 | 99.5 ms: 1.16x faster                                                             |
| xml_etree_generate   | 99.4 ms                                                | 85.9 ms: 1.16x faster                                                             |
| json_loads           | 31.2 us                                                | 30.3 us: 1.03x faster                                                             |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.12x faster                                                             |
| python_startup_no_site | 5.93 ms                                                | 6.90 ms: 1.16x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                             |
| django_template | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                             |
| mako            | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                             |
| genshi_xml      | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.23x faster                                                              |
| async_tree_io            | 1.77 sec                                               | 601 ms: 2.94x faster                                                              |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                              |
| generators               | 80.1 ms                                                | 28.9 ms: 2.77x faster                                                             |
| async_tree_none          | 728 ms                                                 | 264 ms: 2.76x faster                                                              |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.31x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.43 ms: 2.30x faster                                                             |
| go                       | 240 ms                                                 | 112 ms: 2.14x faster                                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 499 ms: 2.04x faster                                                              |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                             |
| logging_silent           | 190 ns                                                 | 95.9 ns: 1.98x faster                                                             |
| pylint                   | 551 ms                                                 | 282 ms: 1.95x faster                                                              |
| chaos                    | 115 ms                                                 | 59.8 ms: 1.93x faster                                                             |
| richards_super           | 94.7 ms                                                | 50.1 ms: 1.89x faster                                                             |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                              |
| raytrace                 | 507 ms                                                 | 276 ms: 1.83x faster                                                              |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                              |
| richards                 | 79.3 ms                                                | 44.0 ms: 1.80x faster                                                             |
| scimark_monte_carlo      | 118 ms                                                 | 67.5 ms: 1.75x faster                                                             |
| crypto_pyaes             | 128 ms                                                 | 74.7 ms: 1.71x faster                                                             |
| float                    | 117 ms                                                 | 69.3 ms: 1.69x faster                                                             |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                             |
| hexiom                   | 10.4 ms                                                | 6.25 ms: 1.66x faster                                                             |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                              |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                            |
| pyflate                  | 716 ms                                                 | 456 ms: 1.57x faster                                                              |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                              |
| nbody                    | 154 ms                                                 | 101 ms: 1.52x faster                                                              |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                              |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                             |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.78 us: 1.50x faster                                                             |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                              |
| django_template          | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                             |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                                             |
| logging_format           | 9.09 us                                                | 6.28 us: 1.45x faster                                                             |
| html5lib                 | 88.9 ms                                                | 62.6 ms: 1.42x faster                                                             |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                             |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 60.1 ms: 1.40x faster                                                             |
| pprint_safe_repr         | 1.02 sec                                               | 732 ms: 1.39x faster                                                              |
| coroutines               | 35.1 ms                                                | 25.4 ms: 1.38x faster                                                             |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                              |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.3 ms: 1.35x faster                                                             |
| sympy_integrate          | 25.8 ms                                                | 19.2 ms: 1.35x faster                                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.82 ms: 1.34x faster                                                             |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                             |
| xml_etree_process        | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                             |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                              |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                                              |
| nqueens                  | 106 ms                                                 | 82.1 ms: 1.29x faster                                                             |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                              |
| scimark_fft              | 466 ms                                                 | 363 ms: 1.28x faster                                                              |
| fannkuch                 | 532 ms                                                 | 423 ms: 1.26x faster                                                              |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 22.5 ms: 1.23x faster                                                             |
| sympy_expand             | 566 ms                                                 | 459 ms: 1.23x faster                                                              |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                              |
| json_dumps               | 14.2 ms                                                | 12.0 ms: 1.18x faster                                                             |
| pathlib                  | 20.5 ms                                                | 17.4 ms: 1.18x faster                                                             |
| xml_etree_iterparse      | 115 ms                                                 | 99.5 ms: 1.16x faster                                                             |
| xml_etree_generate       | 99.4 ms                                                | 85.9 ms: 1.16x faster                                                             |
| regex_effbot             | 3.63 ms                                                | 3.14 ms: 1.16x faster                                                             |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                              |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.12x faster                                                             |
| bench_thread_pool        | 986 us                                                 | 891 us: 1.11x faster                                                              |
| regex_dna                | 227 ms                                                 | 208 ms: 1.09x faster                                                              |
| async_generators         | 444 ms                                                 | 409 ms: 1.09x faster                                                              |
| sqlite_synth             | 3.02 us                                                | 2.92 us: 1.04x faster                                                             |
| json                     | 5.69 ms                                                | 5.52 ms: 1.03x faster                                                             |
| json_loads               | 31.2 us                                                | 30.3 us: 1.03x faster                                                             |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                              |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                              |
| telco                    | 7.27 ms                                                | 7.85 ms: 1.08x slower                                                             |
| coverage                 | 79.4 ms                                                | 92.1 ms: 1.16x slower                                                             |
| python_startup_no_site   | 5.93 ms                                                | 6.90 ms: 1.16x slower                                                             |
| gc_traversal             | 3.62 ms                                                | 5.08 ms: 1.40x slower                                                             |
| create_gc_cycles         | 1.62 ms                                                | 2.50 ms: 1.54x slower                                                             |
| bench_mp_pool            | 24.0 ms                                                | 81.7 ms: 3.40x slower                                                             |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                                      |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250501-3.14.0a7+-04539cc/bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.441x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.28x