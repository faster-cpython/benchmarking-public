# Results vs. 3.10.4

- fork: brandtbucher
- ref: for_iter_dict_items
- machine: linux-x86_64
- commit hash: 66ef77e
- commit date: 2025-02-11
- overall geometric mean: 1.444x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.35x faster                                                        |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                      |
| html5lib       | 88.9 ms                                                | 61.5 ms: 1.45x faster                                                       |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 620 ms: 2.85x faster                                                        |
| async_tree_none         | 728 ms                                                 | 267 ms: 2.72x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 326 ms: 2.67x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.56x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.9 ms: 1.65x faster                                                       |
| nbody          | 154 ms                                                 | 97.4 ms: 1.58x faster                                                       |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.50x faster                                                        |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                       |
| regex_effbot   | 3.63 ms                                                | 3.20 ms: 1.13x faster                                                       |
| regex_dna      | 227 ms                                                 | 206 ms: 1.10x faster                                                        |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 198 us: 1.67x faster                                                        |
| pickle_pure_python   | 484 us                                                 | 314 us: 1.54x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 55.1 ms: 1.44x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 78.2 ms: 1.27x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 95.8 ms: 1.21x faster                                                       |
| json_dumps           | 14.2 ms                                                | 11.9 ms: 1.20x faster                                                       |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.97 ms: 1.64x faster                                                       |
| django_template | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                       |
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.48x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                        |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 620 ms: 2.85x faster                                                        |
| async_tree_none          | 728 ms                                                 | 267 ms: 2.72x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 326 ms: 2.67x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.43 ms: 2.31x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                                        |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                        |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 30.3 us: 1.93x faster                                                       |
| richards_super           | 94.7 ms                                                | 50.1 ms: 1.89x faster                                                       |
| go                       | 240 ms                                                 | 129 ms: 1.85x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 69.1 ms: 1.85x faster                                                       |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.84x faster                                                        |
| deepcopy                 | 479 us                                                 | 261 us: 1.83x faster                                                        |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 65.6 ms: 1.80x faster                                                       |
| richards                 | 79.3 ms                                                | 44.0 ms: 1.80x faster                                                       |
| spectral_norm            | 170 ms                                                 | 94.9 ms: 1.79x faster                                                       |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 198 us: 1.67x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                       |
| float                    | 117 ms                                                 | 70.9 ms: 1.65x faster                                                       |
| comprehensions           | 28.8 us                                                | 17.4 us: 1.65x faster                                                       |
| mako                     | 16.3 ms                                                | 9.97 ms: 1.64x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                       |
| nbody                    | 154 ms                                                 | 97.4 ms: 1.58x faster                                                       |
| pyflate                  | 716 ms                                                 | 462 ms: 1.55x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.55x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 314 us: 1.54x faster                                                        |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                        |
| django_template          | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                                       |
| regex_compile            | 188 ms                                                 | 125 ms: 1.50x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.93 ms: 1.50x faster                                                       |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                        |
| logging_format           | 9.09 us                                                | 6.10 us: 1.49x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.39 ms: 1.47x faster                                                       |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                                       |
| html5lib                 | 88.9 ms                                                | 61.5 ms: 1.45x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 55.1 ms: 1.44x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                                      |
| thrift                   | 1.07 ms                                                | 759 us: 1.41x faster                                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.37x faster                                                      |
| fannkuch                 | 532 ms                                                 | 394 ms: 1.35x faster                                                        |
| 2to3                     | 348 ms                                                 | 259 ms: 1.35x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 760 ms: 1.34x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                       |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 66.0 ms: 1.28x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 20.2 ms: 1.28x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 78.2 ms: 1.27x faster                                                       |
| sympy_sum                | 196 ms                                                 | 157 ms: 1.25x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 55.4 ms: 1.25x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                      |
| sympy_str                | 346 ms                                                 | 281 ms: 1.23x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 95.8 ms: 1.21x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.9 ms: 1.20x faster                                                       |
| nqueens                  | 106 ms                                                 | 90.0 ms: 1.18x faster                                                       |
| sympy_expand             | 566 ms                                                 | 482 ms: 1.17x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                       |
| regex_effbot             | 3.63 ms                                                | 3.20 ms: 1.13x faster                                                       |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 888 us: 1.11x faster                                                        |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                       |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                        |
| regex_dna                | 227 ms                                                 | 206 ms: 1.10x faster                                                        |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                       |
| async_generators         | 444 ms                                                 | 412 ms: 1.08x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                        |
| telco                    | 7.27 ms                                                | 7.61 ms: 1.05x slower                                                       |
| coverage                 | 79.4 ms                                                | 89.1 ms: 1.12x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                       |
| gc_traversal             | 3.62 ms                                                | 4.99 ms: 1.38x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                       |
| bench_mp_pool            | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250211-3.14.0a4+-66ef77e-JIT/bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.444x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.28x