# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: linux-x86_64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.310x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 278 ms: 1.25x faster                                                         |
| docutils       | 3.30 sec                                               | 2.73 sec: 1.21x faster                                                       |
| html5lib       | 88.9 ms                                                | 65.5 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 669 ms: 2.64x faster                                                         |
| async_tree_none         | 728 ms                                                 | 285 ms: 2.56x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 357 ms: 2.44x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 555 ms: 1.83x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 78.0 ms: 1.50x faster                                                        |
| nbody          | 154 ms                                                 | 120 ms: 1.27x faster                                                         |
| pidigits       | 191 ms                                                 | 214 ms: 1.12x slower                                                         |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 147 ms: 1.28x faster                                                         |
| regex_dna      | 227 ms                                                 | 196 ms: 1.15x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.32 ms: 1.09x faster                                                        |
| regex_v8       | 27.8 ms                                                | 26.6 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 361 us: 1.34x faster                                                         |
| tomli_loads          | 3.14 sec                                               | 2.36 sec: 1.33x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 252 us: 1.31x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 67.5 ms: 1.17x faster                                                        |
| json_dumps           | 14.2 ms                                                | 13.2 ms: 1.08x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 95.6 ms: 1.04x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 163 ms: 1.03x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                 |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.12x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.21x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 36.4 ms: 1.32x faster                                                        |
| mako            | 16.3 ms                                                | 13.0 ms: 1.25x faster                                                        |
| genshi_text     | 31.8 ms                                                | 25.5 ms: 1.25x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 60.8 ms: 1.09x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.22x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 669 ms: 2.64x faster                                                         |
| async_tree_none          | 728 ms                                                 | 285 ms: 2.56x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 357 ms: 2.44x faster                                                         |
| generators               | 80.1 ms                                                | 34.7 ms: 2.31x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.94 ms: 2.01x faster                                                        |
| pylint                   | 551 ms                                                 | 292 ms: 1.89x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 555 ms: 1.83x faster                                                         |
| logging_silent           | 190 ns                                                 | 109 ns: 1.74x faster                                                         |
| chaos                    | 115 ms                                                 | 66.8 ms: 1.73x faster                                                        |
| go                       | 240 ms                                                 | 140 ms: 1.71x faster                                                         |
| raytrace                 | 507 ms                                                 | 296 ms: 1.71x faster                                                         |
| deepcopy                 | 479 us                                                 | 291 us: 1.64x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 71.9 ms: 1.64x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 35.6 us: 1.64x faster                                                        |
| richards_super           | 94.7 ms                                                | 57.7 ms: 1.64x faster                                                        |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 80.0 ms: 1.60x faster                                                        |
| comprehensions           | 28.8 us                                                | 18.2 us: 1.58x faster                                                        |
| richards                 | 79.3 ms                                                | 51.8 ms: 1.53x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.42 ms: 1.52x faster                                                        |
| scimark_sor              | 220 ms                                                 | 146 ms: 1.51x faster                                                         |
| float                    | 117 ms                                                 | 78.0 ms: 1.50x faster                                                        |
| pyflate                  | 716 ms                                                 | 480 ms: 1.49x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.75 ms: 1.47x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.54 ms: 1.42x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.94 us: 1.42x faster                                                        |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                         |
| hexiom                   | 10.4 ms                                                | 7.47 ms: 1.39x faster                                                        |
| coroutines               | 35.1 ms                                                | 25.7 ms: 1.36x faster                                                        |
| html5lib                 | 88.9 ms                                                | 65.5 ms: 1.36x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 361 us: 1.34x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 2.36 sec: 1.33x faster                                                       |
| django_template          | 48.2 ms                                                | 36.4 ms: 1.32x faster                                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.8 ms: 1.31x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 252 us: 1.31x faster                                                         |
| regex_compile            | 188 ms                                                 | 147 ms: 1.28x faster                                                         |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                        |
| nbody                    | 154 ms                                                 | 120 ms: 1.27x faster                                                         |
| thrift                   | 1.07 ms                                                | 847 us: 1.27x faster                                                         |
| scimark_fft              | 466 ms                                                 | 370 ms: 1.26x faster                                                         |
| 2to3                     | 348 ms                                                 | 278 ms: 1.25x faster                                                         |
| mako                     | 16.3 ms                                                | 13.0 ms: 1.25x faster                                                        |
| sympy_sum                | 196 ms                                                 | 157 ms: 1.25x faster                                                         |
| genshi_text              | 31.8 ms                                                | 25.5 ms: 1.25x faster                                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 138 ms: 1.25x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 68.1 ms: 1.24x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.28 sec: 1.23x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 21.1 ms: 1.23x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 117 ms: 1.22x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.73 sec: 1.21x faster                                                       |
| sympy_str                | 346 ms                                                 | 290 ms: 1.19x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 58.2 ms: 1.19x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 67.5 ms: 1.17x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.80 sec: 1.17x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 876 ms: 1.16x faster                                                         |
| logging_simple           | 8.30 us                                                | 7.16 us: 1.16x faster                                                        |
| regex_dna                | 227 ms                                                 | 196 ms: 1.15x faster                                                         |
| fannkuch                 | 532 ms                                                 | 461 ms: 1.15x faster                                                         |
| nqueens                  | 106 ms                                                 | 92.0 ms: 1.15x faster                                                        |
| logging_format           | 9.09 us                                                | 7.92 us: 1.15x faster                                                        |
| sympy_expand             | 566 ms                                                 | 498 ms: 1.14x faster                                                         |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.12x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.32 ms: 1.09x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 60.8 ms: 1.09x faster                                                        |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                        |
| json_dumps               | 14.2 ms                                                | 13.2 ms: 1.08x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 917 us: 1.08x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                                         |
| async_generators         | 444 ms                                                 | 417 ms: 1.06x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 26.6 ms: 1.05x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 95.6 ms: 1.04x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 163 ms: 1.03x faster                                                         |
| meteor_contest           | 120 ms                                                 | 117 ms: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                         |
| json                     | 5.69 ms                                                | 5.63 ms: 1.01x faster                                                        |
| coverage                 | 79.4 ms                                                | 79.1 ms: 1.00x faster                                                        |
| telco                    | 7.27 ms                                                | 7.90 ms: 1.09x slower                                                        |
| pidigits                 | 191 ms                                                 | 214 ms: 1.12x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.21x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.76 ms: 1.31x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.50 ms: 1.54x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 83.5 ms: 3.48x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                                 |

Benchmark hidden because not significant (2): json_loads, mdp
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250225-3.14.0a5+-da5ad58-CLANG/bm-20250225-linux-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.310x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.30x