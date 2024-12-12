# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_binary_op_swa
- machine: linux-x86_64
- commit hash: 18b60c7
- commit date: 2024-12-11
- overall geometric mean: 1.420x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                         |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                       |
| html5lib       | 88.9 ms                                                | 63.2 ms: 1.41x faster                                                        |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 625 ms: 2.83x faster                                                         |
| async_tree_none         | 728 ms                                                 | 272 ms: 2.68x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 343 ms: 2.53x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 502 ms: 2.02x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.50x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 93.8 ms: 1.64x faster                                                        |
| float          | 117 ms                                                 | 77.2 ms: 1.52x faster                                                        |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.19 ms: 1.14x faster                                                        |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                        |
| regex_dna      | 227 ms                                                 | 211 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 194 us: 1.70x faster                                                         |
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.51x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 54.6 ms: 1.45x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 81.2 ms: 1.22x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 95.0 ms: 1.21x faster                                                        |
| json_loads           | 31.2 us                                                | 25.9 us: 1.21x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.37x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.59x faster                                                        |
| django_template | 48.2 ms                                                | 33.9 ms: 1.42x faster                                                        |
| genshi_text     | 31.8 ms                                                | 23.9 ms: 1.33x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 56.3 ms: 1.17x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 625 ms: 2.83x faster                                                         |
| async_tree_none          | 728 ms                                                 | 272 ms: 2.68x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 343 ms: 2.53x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                        |
| generators               | 80.1 ms                                                | 36.3 ms: 2.21x faster                                                        |
| richards_super           | 94.7 ms                                                | 43.8 ms: 2.16x faster                                                        |
| richards                 | 79.3 ms                                                | 36.9 ms: 2.15x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 502 ms: 2.02x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.00x faster                                                        |
| pylint                   | 551 ms                                                 | 290 ms: 1.90x faster                                                         |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                         |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                         |
| chaos                    | 115 ms                                                 | 63.7 ms: 1.81x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 70.8 ms: 1.81x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 65.6 ms: 1.80x faster                                                        |
| deepcopy                 | 479 us                                                 | 267 us: 1.79x faster                                                         |
| go                       | 240 ms                                                 | 134 ms: 1.79x faster                                                         |
| raytrace                 | 507 ms                                                 | 291 ms: 1.74x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 194 us: 1.70x faster                                                         |
| djangocms                | 38.4 us                                                | 22.8 us: 1.69x faster                                                        |
| comprehensions           | 28.8 us                                                | 17.3 us: 1.66x faster                                                        |
| nbody                    | 154 ms                                                 | 93.8 ms: 1.64x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                       |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.59x faster                                                        |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.58x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                                        |
| pyflate                  | 716 ms                                                 | 462 ms: 1.55x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                        |
| float                    | 117 ms                                                 | 77.2 ms: 1.52x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.51x faster                                                         |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                                        |
| hexiom                   | 10.4 ms                                                | 7.07 ms: 1.47x faster                                                        |
| logging_format           | 9.09 us                                                | 6.19 us: 1.47x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.68 us: 1.46x faster                                                        |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 54.6 ms: 1.45x faster                                                        |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 712 ms: 1.43x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                       |
| django_template          | 48.2 ms                                                | 33.9 ms: 1.42x faster                                                        |
| html5lib                 | 88.9 ms                                                | 63.2 ms: 1.41x faster                                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                        |
| thrift                   | 1.07 ms                                                | 777 us: 1.38x faster                                                         |
| fannkuch                 | 532 ms                                                 | 386 ms: 1.38x faster                                                         |
| scimark_fft              | 466 ms                                                 | 343 ms: 1.36x faster                                                         |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                         |
| genshi_text              | 31.8 ms                                                | 23.9 ms: 1.33x faster                                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.33x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.29x faster                                                         |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.13 ms: 1.26x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                        |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 55.4 ms: 1.25x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 67.6 ms: 1.25x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.8 ms: 1.24x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 81.2 ms: 1.22x faster                                                        |
| sympy_str                | 346 ms                                                 | 283 ms: 1.22x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 95.0 ms: 1.21x faster                                                        |
| json_loads               | 31.2 us                                                | 25.9 us: 1.21x faster                                                        |
| sympy_expand             | 566 ms                                                 | 476 ms: 1.19x faster                                                         |
| json                     | 5.69 ms                                                | 4.80 ms: 1.19x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 56.3 ms: 1.17x faster                                                        |
| nqueens                  | 106 ms                                                 | 91.1 ms: 1.16x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.19 ms: 1.14x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 878 us: 1.12x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                       |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                                        |
| regex_dna                | 227 ms                                                 | 211 ms: 1.07x faster                                                         |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                         |
| async_generators         | 444 ms                                                 | 445 ms: 1.00x slower                                                         |
| telco                    | 7.27 ms                                                | 7.66 ms: 1.05x slower                                                        |
| coverage                 | 79.4 ms                                                | 84.3 ms: 1.06x slower                                                        |
| mypy2                    | 894 ms                                                 | 959 ms: 1.07x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.95 ms: 1.37x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 81.3 ms: 3.39x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                 |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241211-3.14.0a2+-18b60c7-JIT/bm-20241211-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18b60c7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.420x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.29x