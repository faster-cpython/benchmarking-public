# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_10_10
- machine: linux-x86_64
- commit hash: 4d21167
- commit date: 2025-03-27
- overall geometric mean: 1.430x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 264 ms: 1.32x faster                                                 |
| docutils       | 3.30 sec                                               | 2.71 sec: 1.22x faster                                               |
| html5lib       | 88.9 ms                                                | 62.4 ms: 1.42x faster                                                |
| Geometric mean | (ref)                                                  | 1.32x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.87x faster                                                 |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.76x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.7 ms: 1.78x faster                                                |
| nbody          | 154 ms                                                 | 89.0 ms: 1.73x faster                                                |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.47x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                                 |
| regex_v8       | 27.8 ms                                                | 23.4 ms: 1.19x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.42 ms: 1.06x faster                                                |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.17x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.89 sec: 1.66x faster                                               |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.57x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 56.7 ms: 1.39x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 80.8 ms: 1.23x faster                                                |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.23x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                                |
| json_loads           | 31.2 us                                                | 30.2 us: 1.03x faster                                                |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 8.22 ms: 1.39x slower                                                |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                |
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 616 ms: 2.87x faster                                                 |
| generators               | 80.1 ms                                                | 28.8 ms: 2.78x faster                                                |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.76x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.04 ms: 2.60x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                |
| richards_super           | 94.7 ms                                                | 47.2 ms: 2.01x faster                                                |
| logging_silent           | 190 ns                                                 | 96.1 ns: 1.97x faster                                                |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                                 |
| richards                 | 79.3 ms                                                | 41.1 ms: 1.93x faster                                                |
| chaos                    | 115 ms                                                 | 60.3 ms: 1.92x faster                                                |
| go                       | 240 ms                                                 | 127 ms: 1.89x faster                                                 |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                 |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                 |
| deepcopy                 | 479 us                                                 | 261 us: 1.83x faster                                                 |
| spectral_norm            | 170 ms                                                 | 95.1 ms: 1.79x faster                                                |
| float                    | 117 ms                                                 | 65.7 ms: 1.78x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 68.2 ms: 1.73x faster                                                |
| nbody                    | 154 ms                                                 | 89.0 ms: 1.73x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 76.1 ms: 1.68x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.89 sec: 1.66x faster                                               |
| pyflate                  | 716 ms                                                 | 435 ms: 1.65x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.57x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                |
| comprehensions           | 28.8 us                                                | 19.0 us: 1.52x faster                                                |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                                |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                                 |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                |
| hexiom                   | 10.4 ms                                                | 7.03 ms: 1.48x faster                                                |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                |
| logging_format           | 9.09 us                                                | 6.16 us: 1.48x faster                                                |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                                 |
| coroutines               | 35.1 ms                                                | 24.2 ms: 1.45x faster                                                |
| html5lib                 | 88.9 ms                                                | 62.4 ms: 1.42x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 56.7 ms: 1.39x faster                                                |
| dulwich_log              | 84.3 ms                                                | 60.6 ms: 1.39x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.68 ms: 1.38x faster                                                |
| thrift                   | 1.07 ms                                                | 777 us: 1.38x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                               |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 771 ms: 1.32x faster                                                 |
| 2to3                     | 348 ms                                                 | 264 ms: 1.32x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.7 ms: 1.32x faster                                                |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 136 ms: 1.26x faster                                                 |
| fannkuch                 | 532 ms                                                 | 424 ms: 1.25x faster                                                 |
| sympy_str                | 346 ms                                                 | 278 ms: 1.24x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 80.8 ms: 1.23x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.23x faster                                                |
| nqueens                  | 106 ms                                                 | 86.4 ms: 1.22x faster                                                |
| docutils                 | 3.30 sec                                               | 2.71 sec: 1.22x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 23.4 ms: 1.19x faster                                                |
| sympy_expand             | 566 ms                                                 | 478 ms: 1.18x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                                |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.15x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.71 us: 1.11x faster                                                |
| bench_thread_pool        | 986 us                                                 | 888 us: 1.11x faster                                                 |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                 |
| json                     | 5.69 ms                                                | 5.34 ms: 1.07x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.42 ms: 1.06x faster                                                |
| async_generators         | 444 ms                                                 | 419 ms: 1.06x faster                                                 |
| json_loads               | 31.2 us                                                | 30.2 us: 1.03x faster                                                |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                 |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                 |
| coverage                 | 79.4 ms                                                | 86.3 ms: 1.09x slower                                                |
| telco                    | 7.27 ms                                                | 7.90 ms: 1.09x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.99 ms: 1.38x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 8.22 ms: 1.39x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.50 ms: 1.54x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 83.0 ms: 3.46x slower                                                |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                         |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250327-3.14.0a6+-4d21167-JIT/bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.430x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.30x