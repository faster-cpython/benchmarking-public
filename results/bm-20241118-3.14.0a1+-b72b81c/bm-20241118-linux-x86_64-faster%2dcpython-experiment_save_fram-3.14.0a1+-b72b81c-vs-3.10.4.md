# Results vs. 3.10.4

- fork: faster-cpython
- ref: experiment_save_fram
- machine: linux-x86_64
- commit hash: b72b81c
- commit date: 2024-11-18
- overall geometric mean: 1.399x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                             |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                           |
| html5lib       | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                            |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 331 ms: 2.20x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 416 ms: 2.09x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 848 ms: 2.09x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 580 ms: 1.75x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 96.7 ms: 1.59x faster                                                            |
| float          | 117 ms                                                 | 80.0 ms: 1.46x faster                                                            |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                             |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                            |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                                             |
| tomli_loads          | 3.14 sec                                               | 2.10 sec: 1.49x faster                                                           |
| pickle_pure_python   | 484 us                                                 | 326 us: 1.49x faster                                                             |
| xml_etree_process    | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                            |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                            |
| json_loads           | 31.2 us                                                | 27.1 us: 1.15x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 86.8 ms: 1.15x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                             |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.06x faster                                                             |
| Geometric mean       | (ref)                                                  | 1.27x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                            |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                            |
| genshi_text     | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 51.3 ms: 1.29x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.31x faster                                                             |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.42x faster                                                            |
| async_tree_none          | 728 ms                                                 | 331 ms: 2.20x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 416 ms: 2.09x faster                                                             |
| async_tree_io            | 1.77 sec                                               | 848 ms: 2.09x faster                                                             |
| go                       | 240 ms                                                 | 119 ms: 2.02x faster                                                             |
| deepcopy_memo            | 58.5 us                                                | 30.2 us: 1.94x faster                                                            |
| chaos                    | 115 ms                                                 | 61.6 ms: 1.87x faster                                                            |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                             |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                                             |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                                             |
| richards_super           | 94.7 ms                                                | 52.8 ms: 1.80x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 71.9 ms: 1.78x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 580 ms: 1.75x faster                                                             |
| pylint                   | 551 ms                                                 | 320 ms: 1.72x faster                                                             |
| djangocms                | 38.4 us                                                | 22.4 us: 1.72x faster                                                            |
| richards                 | 79.3 ms                                                | 46.4 ms: 1.71x faster                                                            |
| scimark_sor              | 220 ms                                                 | 130 ms: 1.69x faster                                                             |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 70.3 ms: 1.68x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.33 ms: 1.64x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                            |
| nbody                    | 154 ms                                                 | 96.7 ms: 1.59x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                                            |
| pyflate                  | 716 ms                                                 | 470 ms: 1.52x faster                                                             |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                                             |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                            |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                            |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.50x faster                                                             |
| tomli_loads              | 3.14 sec                                               | 2.10 sec: 1.49x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 326 us: 1.49x faster                                                             |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.49x faster                                                            |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                                            |
| float                    | 117 ms                                                 | 80.0 ms: 1.46x faster                                                            |
| spectral_norm            | 170 ms                                                 | 117 ms: 1.46x faster                                                             |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                             |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                           |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 724 ms: 1.41x faster                                                             |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                            |
| thrift                   | 1.07 ms                                                | 778 us: 1.38x faster                                                             |
| genshi_text              | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                            |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                             |
| html5lib                 | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                            |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.35x faster                                                             |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                                             |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                             |
| xml_etree_process        | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                            |
| fannkuch                 | 532 ms                                                 | 404 ms: 1.32x faster                                                             |
| nqueens                  | 106 ms                                                 | 81.6 ms: 1.30x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 65.3 ms: 1.29x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 53.7 ms: 1.29x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 51.3 ms: 1.29x faster                                                            |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                             |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.13 ms: 1.26x faster                                                            |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                             |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                            |
| scimark_fft              | 466 ms                                                 | 379 ms: 1.23x faster                                                             |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 852 us: 1.16x faster                                                             |
| json_loads               | 31.2 us                                                | 27.1 us: 1.15x faster                                                            |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 86.8 ms: 1.15x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                            |
| json                     | 5.69 ms                                                | 5.03 ms: 1.13x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                             |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.08x faster                                                             |
| mdp                      | 2.85 sec                                               | 2.67 sec: 1.07x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.06x faster                                                             |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                            |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                             |
| async_generators         | 444 ms                                                 | 434 ms: 1.02x faster                                                             |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                             |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                             |
| coverage                 | 79.4 ms                                                | 84.0 ms: 1.06x slower                                                            |
| telco                    | 7.27 ms                                                | 7.82 ms: 1.08x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 4.72 ms: 1.30x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.70 ms: 1.66x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 78.7 ms: 3.28x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                                     |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241118-3.14.0a1+-b72b81c/bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.399x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.26x