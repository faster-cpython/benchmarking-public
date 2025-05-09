# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: outline
- machine: linux-x86_64
- commit hash: 69dad45
- commit date: 2025-05-08
- overall geometric mean: 1.418x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 265 ms: 1.31x faster                                                |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                              |
| html5lib       | 88.9 ms                                                | 61.7 ms: 1.44x faster                                               |
| Geometric mean | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 607 ms: 2.91x faster                                                |
| async_tree_none         | 728 ms                                                 | 264 ms: 2.75x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 319 ms: 2.72x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                                |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.4 ms: 1.69x faster                                               |
| nbody          | 154 ms                                                 | 99.3 ms: 1.55x faster                                               |
| pidigits       | 191 ms                                                 | 195 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.37x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.46x faster                                                |
| regex_v8       | 27.8 ms                                                | 22.4 ms: 1.24x faster                                               |
| regex_effbot   | 3.63 ms                                                | 2.95 ms: 1.23x faster                                               |
| regex_dna      | 227 ms                                                 | 195 ms: 1.16x faster                                                |
| Geometric mean | (ref)                                                  | 1.27x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.06 sec: 1.53x faster                                              |
| pickle_pure_python   | 484 us                                                 | 335 us: 1.45x faster                                                |
| unpickle_pure_python | 331 us                                                 | 234 us: 1.41x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 83.8 ms: 1.19x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.19x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                               |
| json_dumps           | 14.2 ms                                                | 12.1 ms: 1.17x faster                                               |
| json_loads           | 31.2 us                                                | 29.4 us: 1.06x faster                                               |
| Geometric mean       | (ref)                                                  | 1.27x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 6.96 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                               |
| django_template | 48.2 ms                                                | 32.9 ms: 1.46x faster                                               |
| mako            | 16.3 ms                                                | 11.7 ms: 1.40x faster                                               |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 175 us: 3.11x faster                                                |
| async_tree_io            | 1.77 sec                                               | 607 ms: 2.91x faster                                                |
| async_tree_none          | 728 ms                                                 | 264 ms: 2.75x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 319 ms: 2.72x faster                                                |
| generators               | 80.1 ms                                                | 30.3 ms: 2.65x faster                                               |
| deltablue                | 7.91 ms                                                | 3.55 ms: 2.23x faster                                               |
| mdp                      | 2.85 sec                                               | 1.29 sec: 2.21x faster                                              |
| richards_super           | 94.7 ms                                                | 43.8 ms: 2.16x faster                                               |
| richards                 | 79.3 ms                                                | 38.5 ms: 2.06x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                                |
| logging_silent           | 190 ns                                                 | 97.4 ns: 1.95x faster                                               |
| pylint                   | 551 ms                                                 | 285 ms: 1.93x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 30.8 us: 1.90x faster                                               |
| chaos                    | 115 ms                                                 | 61.1 ms: 1.89x faster                                               |
| deepcopy                 | 479 us                                                 | 260 us: 1.85x faster                                                |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                |
| raytrace                 | 507 ms                                                 | 282 ms: 1.80x faster                                                |
| go                       | 240 ms                                                 | 135 ms: 1.78x faster                                                |
| float                    | 117 ms                                                 | 69.4 ms: 1.69x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 71.6 ms: 1.65x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 80.0 ms: 1.60x faster                                               |
| pyflate                  | 716 ms                                                 | 462 ms: 1.55x faster                                                |
| nbody                    | 154 ms                                                 | 99.3 ms: 1.55x faster                                               |
| comprehensions           | 28.8 us                                                | 18.7 us: 1.54x faster                                               |
| tomli_loads              | 3.14 sec                                               | 2.06 sec: 1.53x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                               |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                               |
| hexiom                   | 10.4 ms                                                | 7.08 ms: 1.47x faster                                               |
| django_template          | 48.2 ms                                                | 32.9 ms: 1.46x faster                                               |
| regex_compile            | 188 ms                                                 | 130 ms: 1.46x faster                                                |
| pickle_pure_python       | 484 us                                                 | 335 us: 1.45x faster                                                |
| logging_simple           | 8.30 us                                                | 5.74 us: 1.45x faster                                               |
| html5lib                 | 88.9 ms                                                | 61.7 ms: 1.44x faster                                               |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.43x faster                                                |
| coroutines               | 35.1 ms                                                | 24.5 ms: 1.43x faster                                               |
| logging_format           | 9.09 us                                                | 6.41 us: 1.42x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 234 us: 1.41x faster                                                |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.40x faster                                               |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                              |
| dulwich_log              | 84.3 ms                                                | 62.5 ms: 1.35x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                               |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                               |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                |
| 2to3                     | 348 ms                                                 | 265 ms: 1.31x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.8 ms: 1.31x faster                                               |
| scimark_fft              | 466 ms                                                 | 362 ms: 1.29x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 135 ms: 1.28x faster                                                |
| nqueens                  | 106 ms                                                 | 83.7 ms: 1.26x faster                                               |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.69 sec: 1.25x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 820 ms: 1.24x faster                                                |
| regex_v8                 | 27.8 ms                                                | 22.4 ms: 1.24x faster                                               |
| regex_effbot             | 3.63 ms                                                | 2.95 ms: 1.23x faster                                               |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                              |
| fannkuch                 | 532 ms                                                 | 437 ms: 1.22x faster                                                |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 83.8 ms: 1.19x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.19x faster                                                |
| sympy_expand             | 566 ms                                                 | 481 ms: 1.18x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                               |
| json_dumps               | 14.2 ms                                                | 12.1 ms: 1.17x faster                                               |
| regex_dna                | 227 ms                                                 | 195 ms: 1.16x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.79 ms: 1.12x faster                                               |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                               |
| bench_thread_pool        | 986 us                                                 | 900 us: 1.10x faster                                                |
| json                     | 5.69 ms                                                | 5.26 ms: 1.08x faster                                               |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                               |
| json_loads               | 31.2 us                                                | 29.4 us: 1.06x faster                                               |
| async_generators         | 444 ms                                                 | 426 ms: 1.04x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                |
| pidigits                 | 191 ms                                                 | 195 ms: 1.02x slower                                                |
| coverage                 | 79.4 ms                                                | 88.0 ms: 1.11x slower                                               |
| telco                    | 7.27 ms                                                | 8.21 ms: 1.13x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 6.96 ms: 1.17x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.73 ms: 1.31x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.57 ms: 1.58x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 93.4 ms: 3.89x slower                                               |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                        |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250508-3.14.0a7+-69dad45-JIT/bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.418x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.32x