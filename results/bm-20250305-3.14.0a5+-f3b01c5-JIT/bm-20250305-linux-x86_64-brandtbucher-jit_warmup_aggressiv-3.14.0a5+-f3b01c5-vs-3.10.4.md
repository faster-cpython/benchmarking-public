# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_warmup_aggressiv
- machine: linux-x86_64
- commit hash: f3b01c5
- commit date: 2025-03-05
- overall geometric mean: 1.431x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 273 ms: 1.28x faster                                                         |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                       |
| html5lib       | 88.9 ms                                                | 62.5 ms: 1.42x faster                                                        |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 618 ms: 2.86x faster                                                         |
| async_tree_none         | 728 ms                                                 | 267 ms: 2.73x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 330 ms: 2.64x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.56x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.1 ms: 1.72x faster                                                        |
| float          | 117 ms                                                 | 69.7 ms: 1.68x faster                                                        |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.43x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.43x faster                                                         |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.34 ms: 1.09x faster                                                        |
| regex_dna      | 227 ms                                                 | 210 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 210 us: 1.57x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 56.1 ms: 1.41x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 79.4 ms: 1.25x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 99.6 ms: 1.16x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.15x faster                                                         |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.20x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.6 ms: 1.55x faster                                                        |
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                        |
| genshi_text     | 31.8 ms                                                | 21.6 ms: 1.47x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.27x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 618 ms: 2.86x faster                                                         |
| generators               | 80.1 ms                                                | 28.9 ms: 2.77x faster                                                        |
| async_tree_none          | 728 ms                                                 | 267 ms: 2.73x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 330 ms: 2.64x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.34 ms: 2.37x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.01x faster                                                        |
| go                       | 240 ms                                                 | 122 ms: 1.97x faster                                                         |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                                        |
| pylint                   | 551 ms                                                 | 289 ms: 1.90x faster                                                         |
| richards_super           | 94.7 ms                                                | 50.6 ms: 1.87x faster                                                        |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                         |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                         |
| richards                 | 79.3 ms                                                | 44.2 ms: 1.79x faster                                                        |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                                         |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.77x faster                                                         |
| nbody                    | 154 ms                                                 | 89.1 ms: 1.72x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 68.7 ms: 1.72x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 75.2 ms: 1.70x faster                                                        |
| float                    | 117 ms                                                 | 69.7 ms: 1.68x faster                                                        |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.67x faster                                                         |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.43 ms: 1.62x faster                                                        |
| pyflate                  | 716 ms                                                 | 447 ms: 1.60x faster                                                         |
| comprehensions           | 28.8 us                                                | 18.1 us: 1.59x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.57x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 210 us: 1.57x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                        |
| mako                     | 16.3 ms                                                | 10.6 ms: 1.55x faster                                                        |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                                         |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                        |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                        |
| scimark_fft              | 466 ms                                                 | 314 ms: 1.48x faster                                                         |
| genshi_text              | 31.8 ms                                                | 21.6 ms: 1.47x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.48 ms: 1.45x faster                                                        |
| regex_compile            | 188 ms                                                 | 132 ms: 1.43x faster                                                         |
| thrift                   | 1.07 ms                                                | 753 us: 1.42x faster                                                         |
| html5lib                 | 88.9 ms                                                | 62.5 ms: 1.42x faster                                                        |
| coroutines               | 35.1 ms                                                | 24.9 ms: 1.41x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 56.1 ms: 1.41x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 736 ms: 1.38x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.3 ms: 1.35x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 50.1 ms: 1.32x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                         |
| fannkuch                 | 532 ms                                                 | 412 ms: 1.29x faster                                                         |
| 2to3                     | 348 ms                                                 | 273 ms: 1.28x faster                                                         |
| nqueens                  | 106 ms                                                 | 82.9 ms: 1.28x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 67.3 ms: 1.25x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 79.4 ms: 1.25x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 55.3 ms: 1.25x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                        |
| sympy_str                | 346 ms                                                 | 278 ms: 1.24x faster                                                         |
| sympy_sum                | 196 ms                                                 | 158 ms: 1.24x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 20.8 ms: 1.24x faster                                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 140 ms: 1.23x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                        |
| sympy_expand             | 566 ms                                                 | 474 ms: 1.19x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 99.6 ms: 1.16x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.15x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                                       |
| python_startup           | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                        |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 890 us: 1.11x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.10x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.34 ms: 1.09x faster                                                        |
| async_generators         | 444 ms                                                 | 411 ms: 1.08x faster                                                         |
| regex_dna                | 227 ms                                                 | 210 ms: 1.08x faster                                                         |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                        |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                         |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.54 ms: 1.04x slower                                                        |
| coverage                 | 79.4 ms                                                | 84.4 ms: 1.06x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.20x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.73 ms: 1.30x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 87.3 ms: 3.64x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250305-3.14.0a5+-f3b01c5-JIT/bm-20250305-linux-x86_64-brandtbucher-jit_warmup_aggressiv-3.14.0a5+-f3b01c5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.431x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.33x