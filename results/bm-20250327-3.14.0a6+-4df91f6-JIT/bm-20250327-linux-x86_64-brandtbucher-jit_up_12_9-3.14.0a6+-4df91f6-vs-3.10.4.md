# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_12_9
- machine: linux-x86_64
- commit hash: 4df91f6
- commit date: 2025-03-27
- overall geometric mean: 1.435x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 265 ms: 1.31x faster                                                |
| docutils       | 3.30 sec                                               | 2.72 sec: 1.21x faster                                              |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                               |
| Geometric mean | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 622 ms: 2.84x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 317 ms: 2.75x faster                                                |
| async_tree_none         | 728 ms                                                 | 265 ms: 2.75x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 491 ms: 2.07x faster                                                |
| Geometric mean          | (ref)                                                  | 2.58x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.1 ms: 1.80x faster                                               |
| nbody          | 154 ms                                                 | 86.8 ms: 1.77x faster                                               |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.48x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                |
| regex_v8       | 27.8 ms                                                | 23.1 ms: 1.20x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.51 ms: 1.03x faster                                               |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.17x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.87 sec: 1.68x faster                                              |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.55x faster                                                |
| pickle_pure_python   | 484 us                                                 | 330 us: 1.47x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 57.1 ms: 1.38x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 81.0 ms: 1.23x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 97.5 ms: 1.18x faster                                               |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                               |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.19 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.0 ms: 1.50x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                               |
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                               |
| genshi_xml      | 66.0 ms                                                | 50.1 ms: 1.32x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.25x faster                                                |
| async_tree_io            | 1.77 sec                                               | 622 ms: 2.84x faster                                                |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 317 ms: 2.75x faster                                                |
| async_tree_none          | 728 ms                                                 | 265 ms: 2.75x faster                                                |
| deltablue                | 7.91 ms                                                | 3.06 ms: 2.59x faster                                               |
| richards_super           | 94.7 ms                                                | 41.9 ms: 2.26x faster                                               |
| richards                 | 79.3 ms                                                | 37.5 ms: 2.11x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 491 ms: 2.07x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.02x faster                                               |
| pylint                   | 551 ms                                                 | 281 ms: 1.96x faster                                                |
| chaos                    | 115 ms                                                 | 60.1 ms: 1.92x faster                                               |
| logging_silent           | 190 ns                                                 | 99.5 ns: 1.91x faster                                               |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                |
| go                       | 240 ms                                                 | 129 ms: 1.85x faster                                                |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                |
| float                    | 117 ms                                                 | 65.1 ms: 1.80x faster                                               |
| spectral_norm            | 170 ms                                                 | 95.5 ms: 1.78x faster                                               |
| nbody                    | 154 ms                                                 | 86.8 ms: 1.77x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 68.8 ms: 1.72x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.87 sec: 1.68x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 79.0 ms: 1.62x faster                                               |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.55x faster                                                |
| comprehensions           | 28.8 us                                                | 18.7 us: 1.53x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.83 ms: 1.52x faster                                               |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.50x faster                                               |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                               |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                               |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                               |
| pickle_pure_python       | 484 us                                                 | 330 us: 1.47x faster                                                |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                |
| logging_format           | 9.09 us                                                | 6.25 us: 1.45x faster                                               |
| coroutines               | 35.1 ms                                                | 24.6 ms: 1.43x faster                                               |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                               |
| dulwich_log              | 84.3 ms                                                | 60.7 ms: 1.39x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 57.1 ms: 1.38x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.68 ms: 1.38x faster                                               |
| thrift                   | 1.07 ms                                                | 781 us: 1.37x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.4 ms: 1.35x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                              |
| genshi_xml               | 66.0 ms                                                | 50.1 ms: 1.32x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 773 ms: 1.32x faster                                                |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                              |
| 2to3                     | 348 ms                                                 | 265 ms: 1.31x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 134 ms: 1.29x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                               |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.27x faster                                                |
| fannkuch                 | 532 ms                                                 | 422 ms: 1.26x faster                                                |
| sympy_str                | 346 ms                                                 | 276 ms: 1.25x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 81.0 ms: 1.23x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                               |
| nqueens                  | 106 ms                                                 | 87.1 ms: 1.21x faster                                               |
| docutils                 | 3.30 sec                                               | 2.72 sec: 1.21x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                |
| regex_v8                 | 27.8 ms                                                | 23.1 ms: 1.20x faster                                               |
| sympy_expand             | 566 ms                                                 | 474 ms: 1.19x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 97.5 ms: 1.18x faster                                               |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.13x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.70 us: 1.12x faster                                               |
| bench_thread_pool        | 986 us                                                 | 883 us: 1.12x faster                                                |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                               |
| async_generators         | 444 ms                                                 | 417 ms: 1.06x faster                                                |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.51 ms: 1.03x faster                                               |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                |
| coverage                 | 79.4 ms                                                | 85.0 ms: 1.07x slower                                               |
| telco                    | 7.27 ms                                                | 7.95 ms: 1.09x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.81 ms: 1.33x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.19 ms: 1.38x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 82.8 ms: 3.45x slower                                               |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                        |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250327-3.14.0a6+-4df91f6-JIT/bm-20250327-linux-x86_64-brandtbucher-jit_up_12_9-3.14.0a6+-4df91f6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.435x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.29x