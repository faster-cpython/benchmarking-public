# Results vs. base

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.00x faster
- HPT reliability: 89.80%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 268 ms                                                                                                          | 280 ms: 1.04x slower                                                                                                |
| chameleon      | 6.97 ms                                                                                                         | 7.06 ms: 1.01x slower                                                                                               |
| docutils       | 2.78 sec                                                                                                        | 2.94 sec: 1.06x slower                                                                                              |
| html5lib       | 65.6 ms                                                                                                         | 66.0 ms: 1.01x slower                                                                                               |
| tornado_http   | 94.1 ms                                                                                                         | 96.6 ms: 1.03x slower                                                                                               |
| Geometric mean | (ref)                                                                                                           | 1.03x slower                                                                                                        |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| nbody          | 87.2 ms                                                                                                         | 80.4 ms: 1.08x faster                                                                                               |
| float          | 77.2 ms                                                                                                         | 71.9 ms: 1.07x faster                                                                                               |
| pidigits       | 189 ms                                                                                                          | 188 ms: 1.00x faster                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.05x faster                                                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 25.5 ms                                                                                                         | 24.0 ms: 1.06x faster                                                                                               |
| regex_dna      | 219 ms                                                                                                          | 209 ms: 1.05x faster                                                                                                |
| regex_effbot   | 3.55 ms                                                                                                         | 3.47 ms: 1.02x faster                                                                                               |
| regex_compile  | 134 ms                                                                                                          | 138 ms: 1.03x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.03x faster                                                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| unpickle             | 16.9 us                                                                                                         | 15.2 us: 1.11x faster                                                                                               |
| tomli_loads          | 2.11 sec                                                                                                        | 1.94 sec: 1.09x faster                                                                                              |
| xml_etree_iterparse  | 107 ms                                                                                                          | 102 ms: 1.05x faster                                                                                                |
| xml_etree_parse      | 158 ms                                                                                                          | 151 ms: 1.05x faster                                                                                                |
| xml_etree_generate   | 86.4 ms                                                                                                         | 82.4 ms: 1.05x faster                                                                                               |
| xml_etree_process    | 60.1 ms                                                                                                         | 58.1 ms: 1.04x faster                                                                                               |
| json_dumps           | 10.7 ms                                                                                                         | 10.4 ms: 1.03x faster                                                                                               |
| pickle_pure_python   | 305 us                                                                                                          | 300 us: 1.02x faster                                                                                                |
| unpickle_list        | 5.47 us                                                                                                         | 5.38 us: 1.02x faster                                                                                               |
| pickle               | 11.7 us                                                                                                         | 11.6 us: 1.01x faster                                                                                               |
| pickle_list          | 5.61 us                                                                                                         | 5.57 us: 1.01x faster                                                                                               |
| unpickle_pure_python | 220 us                                                                                                          | 222 us: 1.01x slower                                                                                                |
| Geometric mean       | (ref)                                                                                                           | 1.03x faster                                                                                                        |

Benchmark hidden because not significant (2): json_loads, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 10.4 ms                                                                                                         | 10.9 ms: 1.05x slower                                                                                               |
| python_startup_no_site | 7.10 ms                                                                                                         | 7.59 ms: 1.07x slower                                                                                               |
| Geometric mean         | (ref)                                                                                                           | 1.06x slower                                                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                                                                         | 9.62 ms: 1.16x faster                                                                                               |
| django_template | 34.3 ms                                                                                                         | 36.7 ms: 1.07x slower                                                                                               |
| genshi_text     | 23.0 ms                                                                                                         | 24.8 ms: 1.08x slower                                                                                               |
| genshi_xml      | 51.0 ms                                                                                                         | 58.0 ms: 1.14x slower                                                                                               |
| Geometric mean  | (ref)                                                                                                           | 1.03x slower                                                                                                        |

All benchmarks:
===============

| Benchmark                | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
| scimark_fft              | 377 ms                                                                                                          | 313 ms: 1.20x faster                                                                                                |
| mako                     | 11.2 ms                                                                                                         | 9.62 ms: 1.16x faster                                                                                               |
| scimark_sparse_mat_mult  | 5.11 ms                                                                                                         | 4.45 ms: 1.15x faster                                                                                               |
| richards                 | 48.0 ms                                                                                                         | 42.1 ms: 1.14x faster                                                                                               |
| richards_super           | 54.5 ms                                                                                                         | 48.0 ms: 1.14x faster                                                                                               |
| fannkuch                 | 402 ms                                                                                                          | 359 ms: 1.12x faster                                                                                                |
| unpickle                 | 16.9 us                                                                                                         | 15.2 us: 1.11x faster                                                                                               |
| spectral_norm            | 111 ms                                                                                                          | 101 ms: 1.10x faster                                                                                                |
| crypto_pyaes             | 73.4 ms                                                                                                         | 66.7 ms: 1.10x faster                                                                                               |
| pyflate                  | 480 ms                                                                                                          | 437 ms: 1.10x faster                                                                                                |
| tomli_loads              | 2.11 sec                                                                                                        | 1.94 sec: 1.09x faster                                                                                              |
| nbody                    | 87.2 ms                                                                                                         | 80.4 ms: 1.08x faster                                                                                               |
| scimark_monte_carlo      | 68.4 ms                                                                                                         | 63.1 ms: 1.08x faster                                                                                               |
| float                    | 77.2 ms                                                                                                         | 71.9 ms: 1.07x faster                                                                                               |
| regex_v8                 | 25.5 ms                                                                                                         | 24.0 ms: 1.06x faster                                                                                               |
| xml_etree_iterparse      | 107 ms                                                                                                          | 102 ms: 1.05x faster                                                                                                |
| xml_etree_parse          | 158 ms                                                                                                          | 151 ms: 1.05x faster                                                                                                |
| regex_dna                | 219 ms                                                                                                          | 209 ms: 1.05x faster                                                                                                |
| xml_etree_generate       | 86.4 ms                                                                                                         | 82.4 ms: 1.05x faster                                                                                               |
| pprint_pformat           | 1.54 sec                                                                                                        | 1.47 sec: 1.05x faster                                                                                              |
| pprint_safe_repr         | 751 ms                                                                                                          | 721 ms: 1.04x faster                                                                                                |
| deepcopy_memo            | 39.1 us                                                                                                         | 37.7 us: 1.04x faster                                                                                               |
| xml_etree_process        | 60.1 ms                                                                                                         | 58.1 ms: 1.04x faster                                                                                               |
| pycparser                | 1.19 sec                                                                                                        | 1.15 sec: 1.04x faster                                                                                              |
| sqlite_synth             | 2.95 us                                                                                                         | 2.86 us: 1.03x faster                                                                                               |
| json_dumps               | 10.7 ms                                                                                                         | 10.4 ms: 1.03x faster                                                                                               |
| regex_effbot             | 3.55 ms                                                                                                         | 3.47 ms: 1.02x faster                                                                                               |
| gc_traversal             | 3.90 ms                                                                                                         | 3.84 ms: 1.02x faster                                                                                               |
| pickle_pure_python       | 305 us                                                                                                          | 300 us: 1.02x faster                                                                                                |
| unpickle_list            | 5.47 us                                                                                                         | 5.38 us: 1.02x faster                                                                                               |
| json                     | 5.39 ms                                                                                                         | 5.32 ms: 1.01x faster                                                                                               |
| pickle                   | 11.7 us                                                                                                         | 11.6 us: 1.01x faster                                                                                               |
| telco                    | 173 ms                                                                                                          | 172 ms: 1.01x faster                                                                                                |
| pickle_list              | 5.61 us                                                                                                         | 5.57 us: 1.01x faster                                                                                               |
| logging_simple           | 5.72 us                                                                                                         | 5.69 us: 1.01x faster                                                                                               |
| pidigits                 | 189 ms                                                                                                          | 188 ms: 1.00x faster                                                                                                |
| create_gc_cycles         | 1.82 ms                                                                                                         | 1.82 ms: 1.00x slower                                                                                               |
| html5lib                 | 65.6 ms                                                                                                         | 66.0 ms: 1.01x slower                                                                                               |
| unpickle_pure_python     | 220 us                                                                                                          | 222 us: 1.01x slower                                                                                                |
| bench_mp_pool            | 23.8 ms                                                                                                         | 24.0 ms: 1.01x slower                                                                                               |
| sqlglot_transpile        | 1.61 ms                                                                                                         | 1.63 ms: 1.01x slower                                                                                               |
| meteor_contest           | 111 ms                                                                                                          | 112 ms: 1.01x slower                                                                                                |
| pathlib                  | 16.3 ms                                                                                                         | 16.5 ms: 1.01x slower                                                                                               |
| generators               | 29.7 ms                                                                                                         | 30.0 ms: 1.01x slower                                                                                               |
| asyncio_tcp_ssl          | 1.84 sec                                                                                                        | 1.86 sec: 1.01x slower                                                                                              |
| go                       | 145 ms                                                                                                          | 147 ms: 1.01x slower                                                                                                |
| chameleon                | 6.97 ms                                                                                                         | 7.06 ms: 1.01x slower                                                                                               |
| deepcopy                 | 361 us                                                                                                          | 366 us: 1.01x slower                                                                                                |
| deepcopy_reduce          | 3.26 us                                                                                                         | 3.31 us: 1.02x slower                                                                                               |
| thrift                   | 806 us                                                                                                          | 823 us: 1.02x slower                                                                                                |
| dask                     | 369 ms                                                                                                          | 378 ms: 1.02x slower                                                                                                |
| tornado_http             | 94.1 ms                                                                                                         | 96.6 ms: 1.03x slower                                                                                               |
| regex_compile            | 134 ms                                                                                                          | 138 ms: 1.03x slower                                                                                                |
| asyncio_tcp              | 506 ms                                                                                                          | 522 ms: 1.03x slower                                                                                                |
| flaskblogging            | 8.89 ms                                                                                                         | 9.18 ms: 1.03x slower                                                                                               |
| raytrace                 | 266 ms                                                                                                          | 275 ms: 1.03x slower                                                                                                |
| bench_thread_pool        | 832 us                                                                                                          | 860 us: 1.03x slower                                                                                                |
| coverage                 | 92.8 ms                                                                                                         | 95.9 ms: 1.03x slower                                                                                               |
| async_generators         | 447 ms                                                                                                          | 462 ms: 1.03x slower                                                                                                |
| typing_runtime_protocols | 167 us                                                                                                          | 173 us: 1.04x slower                                                                                                |
| 2to3                     | 268 ms                                                                                                          | 280 ms: 1.04x slower                                                                                                |
| sqlglot_optimize         | 54.7 ms                                                                                                         | 57.1 ms: 1.05x slower                                                                                               |
| sqlglot_normalize        | 109 ms                                                                                                          | 114 ms: 1.05x slower                                                                                                |
| dulwich_log              | 66.4 ms                                                                                                         | 69.5 ms: 1.05x slower                                                                                               |
| python_startup           | 10.4 ms                                                                                                         | 10.9 ms: 1.05x slower                                                                                               |
| scimark_sor              | 127 ms                                                                                                          | 133 ms: 1.05x slower                                                                                                |
| logging_silent           | 102 ns                                                                                                          | 108 ns: 1.06x slower                                                                                                |
| docutils                 | 2.78 sec                                                                                                        | 2.94 sec: 1.06x slower                                                                                              |
| hexiom                   | 6.30 ms                                                                                                         | 6.68 ms: 1.06x slower                                                                                               |
| python_startup_no_site   | 7.10 ms                                                                                                         | 7.59 ms: 1.07x slower                                                                                               |
| django_template          | 34.3 ms                                                                                                         | 36.7 ms: 1.07x slower                                                                                               |
| scimark_lu               | 117 ms                                                                                                          | 125 ms: 1.07x slower                                                                                                |
| sympy_str                | 278 ms                                                                                                          | 300 ms: 1.08x slower                                                                                                |
| genshi_text              | 23.0 ms                                                                                                         | 24.8 ms: 1.08x slower                                                                                               |
| sympy_expand             | 467 ms                                                                                                          | 508 ms: 1.09x slower                                                                                                |
| nqueens                  | 79.6 ms                                                                                                         | 87.3 ms: 1.10x slower                                                                                               |
| sympy_sum                | 155 ms                                                                                                          | 171 ms: 1.10x slower                                                                                                |
| pylint                   | 318 ms                                                                                                          | 352 ms: 1.11x slower                                                                                                |
| sympy_integrate          | 20.3 ms                                                                                                         | 22.5 ms: 1.11x slower                                                                                               |
| deltablue                | 3.29 ms                                                                                                         | 3.71 ms: 1.13x slower                                                                                               |
| genshi_xml               | 51.0 ms                                                                                                         | 58.0 ms: 1.14x slower                                                                                               |
| Geometric mean           | (ref)                                                                                                           | 1.00x faster                                                                                                        |

Benchmark hidden because not significant (17): comprehensions, chaos, sqlglot_parse, async_tree_io, mdp, json_loads, pickle_dict, asyncio_websockets, coroutines, logging_format, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg

# HPT report

- Reliability score: 89.80% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x