# Results vs. 3.10.4

- fork: brandtbucher
- ref: hack_night
- machine: linux-x86_64
- commit hash: b856d47
- commit date: 2025-02-22
- overall geometric mean: 1.442x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                              |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                            |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                             |
| Geometric mean | (ref)                                                  | 1.34x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 626 ms: 2.82x faster                                              |
| async_tree_none         | 728 ms                                                 | 270 ms: 2.70x faster                                              |
| async_tree_memoization  | 870 ms                                                 | 329 ms: 2.65x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 501 ms: 2.03x faster                                              |
| Geometric mean          | (ref)                                                  | 2.53x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.5 ms: 1.66x faster                                             |
| nbody          | 154 ms                                                 | 94.0 ms: 1.63x faster                                             |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.41x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.50x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.10 ms: 1.17x faster                                             |
| regex_v8       | 27.8 ms                                                | 23.7 ms: 1.17x faster                                             |
| regex_dna      | 227 ms                                                 | 207 ms: 1.09x faster                                              |
| Geometric mean | (ref)                                                  | 1.23x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.69x faster                                            |
| unpickle_pure_python | 331 us                                                 | 202 us: 1.64x faster                                              |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                              |
| xml_etree_process    | 79.1 ms                                                | 55.9 ms: 1.42x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 78.6 ms: 1.26x faster                                             |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 95.3 ms: 1.21x faster                                             |
| json_dumps           | 14.2 ms                                                | 12.0 ms: 1.18x faster                                             |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                             |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                             |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                             |
| django_template | 48.2 ms                                                | 32.0 ms: 1.51x faster                                             |
| genshi_text     | 31.8 ms                                                | 22.1 ms: 1.44x faster                                             |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                             |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                              |
| generators               | 80.1 ms                                                | 28.0 ms: 2.86x faster                                             |
| async_tree_io            | 1.77 sec                                               | 626 ms: 2.82x faster                                              |
| async_tree_none          | 728 ms                                                 | 270 ms: 2.70x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 329 ms: 2.65x faster                                              |
| deltablue                | 7.91 ms                                                | 3.39 ms: 2.33x faster                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 501 ms: 2.03x faster                                              |
| pylint                   | 551 ms                                                 | 279 ms: 1.97x faster                                              |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                             |
| deepcopy_memo            | 58.5 us                                                | 31.0 us: 1.89x faster                                             |
| richards_super           | 94.7 ms                                                | 50.6 ms: 1.87x faster                                             |
| go                       | 240 ms                                                 | 130 ms: 1.85x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 69.5 ms: 1.84x faster                                             |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                              |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                              |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                              |
| richards                 | 79.3 ms                                                | 44.2 ms: 1.79x faster                                             |
| scimark_monte_carlo      | 118 ms                                                 | 66.2 ms: 1.79x faster                                             |
| logging_silent           | 190 ns                                                 | 109 ns: 1.75x faster                                              |
| spectral_norm            | 170 ms                                                 | 97.5 ms: 1.74x faster                                             |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.69x faster                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                             |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                             |
| float                    | 117 ms                                                 | 70.5 ms: 1.66x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 202 us: 1.64x faster                                              |
| nbody                    | 154 ms                                                 | 94.0 ms: 1.63x faster                                             |
| pyflate                  | 716 ms                                                 | 440 ms: 1.63x faster                                              |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                             |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                             |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                              |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                              |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.51x faster                                             |
| regex_compile            | 188 ms                                                 | 125 ms: 1.50x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.33 ms: 1.49x faster                                             |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                             |
| hexiom                   | 10.4 ms                                                | 6.97 ms: 1.49x faster                                             |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                              |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.49x faster                                             |
| logging_format           | 9.09 us                                                | 6.16 us: 1.48x faster                                             |
| genshi_text              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                             |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 55.9 ms: 1.42x faster                                             |
| thrift                   | 1.07 ms                                                | 768 us: 1.40x faster                                              |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                             |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                            |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                              |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                              |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                            |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.33x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 772 ms: 1.32x faster                                              |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                              |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                              |
| sqlglot_optimize         | 69.2 ms                                                | 53.6 ms: 1.29x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 20.2 ms: 1.28x faster                                             |
| dulwich_log              | 84.3 ms                                                | 66.1 ms: 1.28x faster                                             |
| xml_etree_generate       | 99.4 ms                                                | 78.6 ms: 1.26x faster                                             |
| sympy_str                | 346 ms                                                 | 276 ms: 1.25x faster                                              |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                             |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                            |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 95.3 ms: 1.21x faster                                             |
| sympy_expand             | 566 ms                                                 | 474 ms: 1.19x faster                                              |
| json_dumps               | 14.2 ms                                                | 12.0 ms: 1.18x faster                                             |
| nqueens                  | 106 ms                                                 | 89.9 ms: 1.18x faster                                             |
| regex_effbot             | 3.63 ms                                                | 3.10 ms: 1.17x faster                                             |
| regex_v8                 | 27.8 ms                                                | 23.7 ms: 1.17x faster                                             |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                             |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                            |
| bench_thread_pool        | 986 us                                                 | 891 us: 1.11x faster                                              |
| json                     | 5.69 ms                                                | 5.17 ms: 1.10x faster                                             |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                             |
| regex_dna                | 227 ms                                                 | 207 ms: 1.09x faster                                              |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                             |
| async_generators         | 444 ms                                                 | 410 ms: 1.08x faster                                              |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                              |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                              |
| telco                    | 7.27 ms                                                | 7.68 ms: 1.06x slower                                             |
| coverage                 | 79.4 ms                                                | 89.7 ms: 1.13x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                             |
| gc_traversal             | 3.62 ms                                                | 5.06 ms: 1.40x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                             |
| bench_mp_pool            | 24.0 ms                                                | 81.2 ms: 3.38x slower                                             |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                      |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250222-3.14.0a5-b856d47-JIT/bm-20250222-linux-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.442x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x