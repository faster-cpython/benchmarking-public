# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: method_jit_bench
- machine: linux-x86_64
- commit hash: d456718
- commit date: 2025-03-18
- overall geometric mean: 1.430x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 3.30 sec                                               | 2.63 sec: 1.25x faster                                                       |
| html5lib       | 88.9 ms                                                | 62.4 ms: 1.42x faster                                                        |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 612 ms: 2.89x faster                                                         |
| async_tree_none         | 728 ms                                                 | 257 ms: 2.83x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 316 ms: 2.76x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.2 ms: 1.69x faster                                                        |
| nbody          | 154 ms                                                 | 96.7 ms: 1.59x faster                                                        |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.40x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                                         |
| regex_v8       | 27.8 ms                                                | 23.1 ms: 1.20x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.18 ms: 1.14x faster                                                        |
| regex_dna      | 227 ms                                                 | 217 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                         |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 83.7 ms: 1.19x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                                        |
| json_loads           | 31.2 us                                                | 29.5 us: 1.06x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 8.29 ms: 1.40x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                        |
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                        |
| mako            | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.34x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 612 ms: 2.89x faster                                                         |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                                        |
| async_tree_none          | 728 ms                                                 | 257 ms: 2.83x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 316 ms: 2.76x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.63 ms: 2.18x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                         |
| go                       | 240 ms                                                 | 120 ms: 1.99x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                                        |
| logging_silent           | 190 ns                                                 | 96.8 ns: 1.96x faster                                                        |
| pylint                   | 551 ms                                                 | 282 ms: 1.96x faster                                                         |
| chaos                    | 115 ms                                                 | 59.9 ms: 1.93x faster                                                        |
| richards_super           | 94.7 ms                                                | 49.5 ms: 1.91x faster                                                        |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                         |
| richards                 | 79.3 ms                                                | 43.4 ms: 1.83x faster                                                        |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                                         |
| deepcopy                 | 479 us                                                 | 264 us: 1.82x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 67.4 ms: 1.75x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                        |
| spectral_norm            | 170 ms                                                 | 99.2 ms: 1.71x faster                                                        |
| float                    | 117 ms                                                 | 69.2 ms: 1.69x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 75.7 ms: 1.69x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                                        |
| pyflate                  | 716 ms                                                 | 446 ms: 1.60x faster                                                         |
| nbody                    | 154 ms                                                 | 96.7 ms: 1.59x faster                                                        |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.76 us: 1.51x faster                                                        |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                                         |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.63 us: 1.47x faster                                                        |
| coroutines               | 35.1 ms                                                | 24.0 ms: 1.46x faster                                                        |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                        |
| html5lib                 | 88.9 ms                                                | 62.4 ms: 1.42x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 59.2 ms: 1.42x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.40x faster                                                       |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                                         |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.39x faster                                                       |
| thrift                   | 1.07 ms                                                | 777 us: 1.38x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 739 ms: 1.38x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                        |
| scimark_fft              | 466 ms                                                 | 343 ms: 1.36x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.81 ms: 1.35x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                        |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                         |
| fannkuch                 | 532 ms                                                 | 413 ms: 1.29x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 20.2 ms: 1.28x faster                                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 135 ms: 1.27x faster                                                         |
| sympy_str                | 346 ms                                                 | 273 ms: 1.26x faster                                                         |
| nqueens                  | 106 ms                                                 | 83.8 ms: 1.26x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.63 sec: 1.25x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                        |
| sympy_expand             | 566 ms                                                 | 464 ms: 1.22x faster                                                         |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.21x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 23.1 ms: 1.20x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 83.7 ms: 1.19x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.18 ms: 1.14x faster                                                        |
| async_generators         | 444 ms                                                 | 393 ms: 1.13x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 875 us: 1.13x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                       |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                         |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                        |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                                        |
| json                     | 5.69 ms                                                | 5.35 ms: 1.06x faster                                                        |
| json_loads               | 31.2 us                                                | 29.5 us: 1.06x faster                                                        |
| regex_dna                | 227 ms                                                 | 217 ms: 1.05x faster                                                         |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.95 ms: 1.09x slower                                                        |
| coverage                 | 79.4 ms                                                | 93.3 ms: 1.17x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.83 ms: 1.33x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 8.29 ms: 1.40x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.50 ms: 1.54x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 85.8 ms: 3.57x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                 |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250318-3.14.0a6+-d456718-JIT/bm-20250318-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a6+-d456718.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.430x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.32x