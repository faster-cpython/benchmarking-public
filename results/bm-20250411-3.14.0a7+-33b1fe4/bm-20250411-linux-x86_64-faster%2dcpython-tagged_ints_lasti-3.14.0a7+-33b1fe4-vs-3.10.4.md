# Results vs. 3.10.4

- fork: faster-cpython
- ref: tagged_ints_lasti
- machine: linux-x86_64
- commit hash: 33b1fe4
- commit date: 2025-04-11
- overall geometric mean: 1.461x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 251 ms: 1.39x faster                                                          |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                        |
| html5lib       | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                         |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 612 ms: 2.89x faster                                                          |
| async_tree_none         | 728 ms                                                 | 258 ms: 2.83x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 309 ms: 2.81x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 478 ms: 2.12x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.64x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 68.7 ms: 1.70x faster                                                         |
| nbody          | 154 ms                                                 | 94.6 ms: 1.62x faster                                                         |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.41x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                          |
| regex_v8       | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.26 ms: 1.11x faster                                                         |
| regex_dna      | 227 ms                                                 | 210 ms: 1.08x faster                                                          |
| Geometric mean | (ref)                                                  | 1.21x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                        |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                         |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                          |
| xml_etree_generate   | 99.4 ms                                                | 84.6 ms: 1.17x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 98.6 ms: 1.17x faster                                                         |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 8.19 ms: 1.38x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.8 ms: 1.53x faster                                                         |
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                         |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 48.5 ms: 1.36x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.33x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 612 ms: 2.89x faster                                                          |
| async_tree_none          | 728 ms                                                 | 258 ms: 2.83x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 309 ms: 2.81x faster                                                          |
| generators               | 80.1 ms                                                | 30.5 ms: 2.63x faster                                                         |
| mdp                      | 2.85 sec                                               | 1.21 sec: 2.36x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.41 ms: 2.32x faster                                                         |
| go                       | 240 ms                                                 | 112 ms: 2.15x faster                                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 478 ms: 2.12x faster                                                          |
| chaos                    | 115 ms                                                 | 55.7 ms: 2.07x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 28.5 us: 2.05x faster                                                         |
| logging_silent           | 190 ns                                                 | 94.9 ns: 2.00x faster                                                         |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                          |
| richards_super           | 94.7 ms                                                | 49.4 ms: 1.92x faster                                                         |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                          |
| deepcopy                 | 479 us                                                 | 250 us: 1.91x faster                                                          |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                          |
| richards                 | 79.3 ms                                                | 43.2 ms: 1.83x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 66.0 ms: 1.79x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 73.2 ms: 1.75x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                         |
| float                    | 117 ms                                                 | 68.7 ms: 1.70x faster                                                         |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                          |
| hexiom                   | 10.4 ms                                                | 6.27 ms: 1.66x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                        |
| nbody                    | 154 ms                                                 | 94.6 ms: 1.62x faster                                                         |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                         |
| genshi_text              | 31.8 ms                                                | 20.8 ms: 1.53x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                          |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.53 us: 1.50x faster                                                         |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                          |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                         |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                        |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                         |
| html5lib                 | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                         |
| coroutines               | 35.1 ms                                                | 24.6 ms: 1.43x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 59.4 ms: 1.42x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 717 ms: 1.42x faster                                                          |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                         |
| 2to3                     | 348 ms                                                 | 251 ms: 1.39x faster                                                          |
| sympy_integrate          | 25.8 ms                                                | 18.9 ms: 1.37x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.36x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 48.5 ms: 1.36x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                         |
| scimark_fft              | 466 ms                                                 | 348 ms: 1.34x faster                                                          |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.85 ms: 1.33x faster                                                         |
| nqueens                  | 106 ms                                                 | 80.2 ms: 1.32x faster                                                         |
| sympy_str                | 346 ms                                                 | 265 ms: 1.31x faster                                                          |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.30x faster                                                          |
| fannkuch                 | 532 ms                                                 | 413 ms: 1.29x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                        |
| sympy_expand             | 566 ms                                                 | 448 ms: 1.26x faster                                                          |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                          |
| pathlib                  | 20.5 ms                                                | 17.2 ms: 1.19x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 84.6 ms: 1.17x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 98.6 ms: 1.17x faster                                                         |
| async_generators         | 444 ms                                                 | 393 ms: 1.13x faster                                                          |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                          |
| bench_thread_pool        | 986 us                                                 | 887 us: 1.11x faster                                                          |
| regex_effbot             | 3.63 ms                                                | 3.26 ms: 1.11x faster                                                         |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                         |
| regex_dna                | 227 ms                                                 | 210 ms: 1.08x faster                                                          |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                         |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                                         |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                          |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                          |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                                         |
| coverage                 | 79.4 ms                                                | 87.5 ms: 1.10x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 4.78 ms: 1.32x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 8.19 ms: 1.38x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                         |
| bench_mp_pool            | 24.0 ms                                                | 81.5 ms: 3.39x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                  |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250411-3.14.0a7+-33b1fe4/bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.461x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.27x