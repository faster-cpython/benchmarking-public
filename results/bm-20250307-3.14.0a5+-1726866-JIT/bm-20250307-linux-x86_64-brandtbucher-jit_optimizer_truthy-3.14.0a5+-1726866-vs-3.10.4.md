# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_optimizer_truthy
- machine: linux-x86_64
- commit hash: 1726866
- commit date: 2025-03-07
- overall geometric mean: 1.448x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                         |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                       |
| html5lib       | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                        |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 610 ms: 2.90x faster                                                         |
| async_tree_none         | 728 ms                                                 | 264 ms: 2.76x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 330 ms: 2.64x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.58x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.2 ms: 1.74x faster                                                        |
| float          | 117 ms                                                 | 69.8 ms: 1.68x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.44x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                                         |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.39 ms: 1.07x faster                                                        |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                  | 1.16x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.87 sec: 1.68x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 202 us: 1.63x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 79.4 ms: 1.25x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 99.4 ms: 1.16x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.15x faster                                                         |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.5 ms: 1.55x faster                                                        |
| django_template | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                        |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 610 ms: 2.90x faster                                                         |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                        |
| async_tree_none          | 728 ms                                                 | 264 ms: 2.76x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 330 ms: 2.64x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.43x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                         |
| go                       | 240 ms                                                 | 117 ms: 2.05x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.01x faster                                                        |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                         |
| chaos                    | 115 ms                                                 | 59.2 ms: 1.95x faster                                                        |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                         |
| richards_super           | 94.7 ms                                                | 50.7 ms: 1.87x faster                                                        |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                         |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                         |
| richards                 | 79.3 ms                                                | 44.3 ms: 1.79x faster                                                        |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                                         |
| spectral_norm            | 170 ms                                                 | 95.7 ms: 1.78x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 67.8 ms: 1.74x faster                                                        |
| nbody                    | 154 ms                                                 | 88.2 ms: 1.74x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 74.7 ms: 1.71x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.69x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.87 sec: 1.68x faster                                                       |
| float                    | 117 ms                                                 | 69.8 ms: 1.68x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 202 us: 1.63x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.37 ms: 1.63x faster                                                        |
| comprehensions           | 28.8 us                                                | 17.7 us: 1.63x faster                                                        |
| pyflate                  | 716 ms                                                 | 443 ms: 1.62x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.61x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.61 us: 1.60x faster                                                        |
| mako                     | 16.3 ms                                                | 10.5 ms: 1.55x faster                                                        |
| django_template          | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                        |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                         |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                                        |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                        |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                                         |
| scimark_fft              | 466 ms                                                 | 317 ms: 1.47x faster                                                         |
| html5lib                 | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.55 ms: 1.42x faster                                                        |
| thrift                   | 1.07 ms                                                | 755 us: 1.42x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.40x faster                                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 747 ms: 1.36x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.35x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.35x faster                                                       |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.33x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                        |
| fannkuch                 | 532 ms                                                 | 402 ms: 1.32x faster                                                         |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                         |
| nqueens                  | 106 ms                                                 | 81.5 ms: 1.30x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 53.5 ms: 1.29x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                                        |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 67.3 ms: 1.25x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 79.4 ms: 1.25x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                        |
| sympy_expand             | 566 ms                                                 | 467 ms: 1.21x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 99.4 ms: 1.16x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.15x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.14x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 876 us: 1.13x faster                                                         |
| python_startup           | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                        |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                                        |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                         |
| async_generators         | 444 ms                                                 | 408 ms: 1.09x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.39 ms: 1.07x faster                                                        |
| json                     | 5.69 ms                                                | 5.34 ms: 1.07x faster                                                        |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                                        |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                         |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                         |
| coverage                 | 79.4 ms                                                | 83.8 ms: 1.06x slower                                                        |
| telco                    | 7.27 ms                                                | 7.68 ms: 1.06x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.60 ms: 1.27x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.43 ms: 1.50x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 81.8 ms: 3.41x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250307-3.14.0a5+-1726866-JIT/bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.448x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x