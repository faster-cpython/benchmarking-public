# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: method_jit_bench
- machine: linux-x86_64
- commit hash: 2b1c0da
- commit date: 2025-03-14
- overall geometric mean: 1.292x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 3.30 sec                                               | 5.32 sec: 1.61x slower                                                       |
| html5lib       | 88.9 ms                                                | 128 ms: 1.44x slower                                                         |
| Geometric mean | (ref)                                                  | 1.52x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 1.20 sec: 1.47x faster                                                       |
| async_tree_none         | 728 ms                                                 | 519 ms: 1.40x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 647 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 989 ms: 1.03x faster                                                         |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 139 ms: 1.18x slower                                                         |
| nbody          | 154 ms                                                 | 193 ms: 1.26x slower                                                         |
| pidigits       | 191 ms                                                 | 378 ms: 1.98x slower                                                         |
| Geometric mean | (ref)                                                  | 1.43x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 265 ms: 1.41x slower                                                         |
| regex_v8       | 27.8 ms                                                | 48.8 ms: 1.76x slower                                                        |
| regex_effbot   | 3.63 ms                                                | 6.44 ms: 1.77x slower                                                        |
| regex_dna      | 227 ms                                                 | 436 ms: 1.92x slower                                                         |
| Geometric mean | (ref)                                                  | 1.70x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 430 us: 1.30x slower                                                         |
| tomli_loads          | 3.14 sec                                               | 4.20 sec: 1.34x slower                                                       |
| pickle_pure_python   | 484 us                                                 | 649 us: 1.34x slower                                                         |
| xml_etree_process    | 79.1 ms                                                | 116 ms: 1.47x slower                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 188 ms: 1.63x slower                                                         |
| json_dumps           | 14.2 ms                                                | 23.2 ms: 1.63x slower                                                        |
| xml_etree_parse      | 168 ms                                                 | 279 ms: 1.66x slower                                                         |
| xml_etree_generate   | 99.4 ms                                                | 168 ms: 1.69x slower                                                         |
| json_loads           | 31.2 us                                                | 60.1 us: 1.93x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.54x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 31.2 ms: 2.14x slower                                                        |
| python_startup_no_site | 5.93 ms                                                | 31.0 ms: 5.22x slower                                                        |
| Geometric mean         | (ref)                                                  | 3.34x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 64.4 ms: 1.34x slower                                                        |
| genshi_text     | 31.8 ms                                                | 44.3 ms: 1.39x slower                                                        |
| mako            | 16.3 ms                                                | 23.4 ms: 1.43x slower                                                        |
| genshi_xml      | 66.0 ms                                                | 98.8 ms: 1.50x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.41x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 327 us: 1.67x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.47x faster                                                       |
| async_tree_none          | 728 ms                                                 | 519 ms: 1.40x faster                                                         |
| generators               | 80.1 ms                                                | 57.8 ms: 1.39x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 647 ms: 1.34x faster                                                         |
| deltablue                | 7.91 ms                                                | 7.42 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 989 ms: 1.03x faster                                                         |
| go                       | 240 ms                                                 | 242 ms: 1.01x slower                                                         |
| chaos                    | 115 ms                                                 | 119 ms: 1.03x slower                                                         |
| logging_silent           | 190 ns                                                 | 197 ns: 1.04x slower                                                         |
| richards_super           | 94.7 ms                                                | 100 ms: 1.06x slower                                                         |
| scimark_sor              | 220 ms                                                 | 233 ms: 1.06x slower                                                         |
| deepcopy                 | 479 us                                                 | 524 us: 1.09x slower                                                         |
| raytrace                 | 507 ms                                                 | 562 ms: 1.11x slower                                                         |
| richards                 | 79.3 ms                                                | 88.7 ms: 1.12x slower                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 133 ms: 1.13x slower                                                         |
| hexiom                   | 10.4 ms                                                | 12.3 ms: 1.18x slower                                                        |
| float                    | 117 ms                                                 | 139 ms: 1.18x slower                                                         |
| comprehensions           | 28.8 us                                                | 34.1 us: 1.18x slower                                                        |
| crypto_pyaes             | 128 ms                                                 | 152 ms: 1.19x slower                                                         |
| spectral_norm            | 170 ms                                                 | 202 ms: 1.19x slower                                                         |
| pyflate                  | 716 ms                                                 | 875 ms: 1.22x slower                                                         |
| nbody                    | 154 ms                                                 | 193 ms: 1.26x slower                                                         |
| deepcopy_reduce          | 4.17 us                                                | 5.34 us: 1.28x slower                                                        |
| unpickle_pure_python     | 331 us                                                 | 430 us: 1.30x slower                                                         |
| scimark_lu               | 176 ms                                                 | 231 ms: 1.31x slower                                                         |
| logging_simple           | 8.30 us                                                | 11.0 us: 1.33x slower                                                        |
| tomli_loads              | 3.14 sec                                               | 4.20 sec: 1.34x slower                                                       |
| django_template          | 48.2 ms                                                | 64.4 ms: 1.34x slower                                                        |
| pickle_pure_python       | 484 us                                                 | 649 us: 1.34x slower                                                         |
| logging_format           | 9.09 us                                                | 12.2 us: 1.34x slower                                                        |
| coroutines               | 35.1 ms                                                | 47.8 ms: 1.36x slower                                                        |
| genshi_text              | 31.8 ms                                                | 44.3 ms: 1.39x slower                                                        |
| dulwich_log              | 84.3 ms                                                | 118 ms: 1.40x slower                                                         |
| regex_compile            | 188 ms                                                 | 265 ms: 1.41x slower                                                         |
| mako                     | 16.3 ms                                                | 23.4 ms: 1.43x slower                                                        |
| pprint_pformat           | 2.10 sec                                               | 3.01 sec: 1.43x slower                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 9.29 ms: 1.44x slower                                                        |
| html5lib                 | 88.9 ms                                                | 128 ms: 1.44x slower                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 33.6 ms: 1.44x slower                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 1.47 sec: 1.45x slower                                                       |
| thrift                   | 1.07 ms                                                | 1.55 ms: 1.45x slower                                                        |
| pycparser                | 1.58 sec                                               | 2.28 sec: 1.45x slower                                                       |
| xml_etree_process        | 79.1 ms                                                | 116 ms: 1.47x slower                                                         |
| scimark_fft              | 466 ms                                                 | 686 ms: 1.47x slower                                                         |
| genshi_xml               | 66.0 ms                                                | 98.8 ms: 1.50x slower                                                        |
| sympy_sum                | 196 ms                                                 | 301 ms: 1.53x slower                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 268 ms: 1.56x slower                                                         |
| sympy_integrate          | 25.8 ms                                                | 40.3 ms: 1.56x slower                                                        |
| fannkuch                 | 532 ms                                                 | 831 ms: 1.56x slower                                                         |
| sympy_str                | 346 ms                                                 | 542 ms: 1.57x slower                                                         |
| nqueens                  | 106 ms                                                 | 169 ms: 1.60x slower                                                         |
| docutils                 | 3.30 sec                                               | 5.32 sec: 1.61x slower                                                       |
| sympy_expand             | 566 ms                                                 | 916 ms: 1.62x slower                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 188 ms: 1.63x slower                                                         |
| json_dumps               | 14.2 ms                                                | 23.2 ms: 1.63x slower                                                        |
| pathlib                  | 20.5 ms                                                | 33.8 ms: 1.65x slower                                                        |
| xml_etree_parse          | 168 ms                                                 | 279 ms: 1.66x slower                                                         |
| xml_etree_generate       | 99.4 ms                                                | 168 ms: 1.69x slower                                                         |
| regex_v8                 | 27.8 ms                                                | 48.8 ms: 1.76x slower                                                        |
| regex_effbot             | 3.63 ms                                                | 6.44 ms: 1.77x slower                                                        |
| meteor_contest           | 120 ms                                                 | 212 ms: 1.77x slower                                                         |
| mdp                      | 2.85 sec                                               | 5.06 sec: 1.78x slower                                                       |
| async_generators         | 444 ms                                                 | 791 ms: 1.78x slower                                                         |
| sqlite_synth             | 3.02 us                                                | 5.55 us: 1.83x slower                                                        |
| json                     | 5.69 ms                                                | 10.5 ms: 1.85x slower                                                        |
| regex_dna                | 227 ms                                                 | 436 ms: 1.92x slower                                                         |
| json_loads               | 31.2 us                                                | 60.1 us: 1.93x slower                                                        |
| asyncio_websockets       | 559 ms                                                 | 1.08 sec: 1.94x slower                                                       |
| pidigits                 | 191 ms                                                 | 378 ms: 1.98x slower                                                         |
| python_startup           | 14.6 ms                                                | 31.2 ms: 2.14x slower                                                        |
| coverage                 | 79.4 ms                                                | 172 ms: 2.16x slower                                                         |
| telco                    | 7.27 ms                                                | 16.2 ms: 2.23x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 9.25 ms: 2.55x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 5.10 ms: 3.15x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 31.0 ms: 5.22x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 136 ms: 5.65x slower                                                         |
| bench_thread_pool        | 986 us                                                 | 30.2 ms: 30.67x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.49x slower                                                                 |

Benchmark hidden because not significant (2): deepcopy_memo, pylint
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250314-3.14.0a5+-2b1c0da-JIT/bm-20250314-linux-x86_64-Fidget%2dSpinner-method_jit_bench-3.14.0a5+-2b1c0da.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.292x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.37x
- 95% likely to have a slowdown of 1.34x
- 99% likely to have a slowdown of 1.30x

# Memory
- memory change: 1.30x