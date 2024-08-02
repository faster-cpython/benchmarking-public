# Results vs. base

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.02x slower
- HPT reliability: 99.19%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 289 ms                                                                                                                | 306 ms: 1.06x slower                                                                                                      |
| chameleon      | 7.29 ms                                                                                                               | 8.00 ms: 1.10x slower                                                                                                     |
| docutils       | 2.99 sec                                                                                                              | 3.15 sec: 1.05x slower                                                                                                    |
| html5lib       | 74.3 ms                                                                                                               | 72.8 ms: 1.02x faster                                                                                                     |
| tornado_http   | 119 ms                                                                                                                | 124 ms: 1.05x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.05x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none | 366 ms                                                                                                                | 374 ms: 1.02x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 80.0 ms                                                                                                               | 73.6 ms: 1.09x faster                                                                                                     |
| nbody          | 87.9 ms                                                                                                               | 82.6 ms: 1.06x faster                                                                                                     |
| pidigits       | 253 ms                                                                                                                | 250 ms: 1.01x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.05x faster                                                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 246 ms                                                                                                                | 239 ms: 1.03x faster                                                                                                      |
| regex_effbot   | 3.70 ms                                                                                                               | 3.60 ms: 1.03x faster                                                                                                     |
| regex_compile  | 143 ms                                                                                                                | 141 ms: 1.01x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.35 sec                                                                                                              | 2.13 sec: 1.10x faster                                                                                                    |
| xml_etree_iterparse  | 105 ms                                                                                                                | 99.6 ms: 1.05x faster                                                                                                     |
| xml_etree_generate   | 84.6 ms                                                                                                               | 81.4 ms: 1.04x faster                                                                                                     |
| unpickle_pure_python | 222 us                                                                                                                | 214 us: 1.04x faster                                                                                                      |
| xml_etree_process    | 59.8 ms                                                                                                               | 58.3 ms: 1.03x faster                                                                                                     |
| json_dumps           | 10.7 ms                                                                                                               | 10.6 ms: 1.01x faster                                                                                                     |
| unpickle             | 14.7 us                                                                                                               | 14.8 us: 1.01x slower                                                                                                     |
| unpickle_list        | 4.77 us                                                                                                               | 4.88 us: 1.02x slower                                                                                                     |
| pickle_pure_python   | 313 us                                                                                                                | 321 us: 1.03x slower                                                                                                      |
| pickle               | 10.5 us                                                                                                               | 10.9 us: 1.04x slower                                                                                                     |
| pickle_dict          | 30.7 us                                                                                                               | 32.2 us: 1.05x slower                                                                                                     |
| pickle_list          | 4.44 us                                                                                                               | 4.68 us: 1.05x slower                                                                                                     |
| Geometric mean       | (ref)                                                                                                                 | 1.00x faster                                                                                                              |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                                                               | 13.4 ms: 1.05x slower                                                                                                     |
| python_startup_no_site | 8.82 ms                                                                                                               | 9.43 ms: 1.07x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                                 | 1.06x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.5 ms                                                                                                               | 9.11 ms: 1.15x faster                                                                                                     |
| django_template | 39.4 ms                                                                                                               | 43.4 ms: 1.10x slower                                                                                                     |
| genshi_text     | 25.4 ms                                                                                                               | 29.3 ms: 1.16x slower                                                                                                     |
| genshi_xml      | 55.9 ms                                                                                                               | 68.7 ms: 1.23x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                                 | 1.08x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                | results/bm-20240518-3.14.0a0-caf6064/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json | results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf2-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json |
|--------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| spectral_norm            | 96.4 ms                                                                                                               | 83.0 ms: 1.16x faster                                                                                                     |
| mako                     | 10.5 ms                                                                                                               | 9.11 ms: 1.15x faster                                                                                                     |
| richards                 | 51.6 ms                                                                                                               | 46.0 ms: 1.12x faster                                                                                                     |
| richards_super           | 59.2 ms                                                                                                               | 52.7 ms: 1.12x faster                                                                                                     |
| tomli_loads              | 2.35 sec                                                                                                              | 2.13 sec: 1.10x faster                                                                                                    |
| float                    | 80.0 ms                                                                                                               | 73.6 ms: 1.09x faster                                                                                                     |
| nbody                    | 87.9 ms                                                                                                               | 82.6 ms: 1.06x faster                                                                                                     |
| scimark_sor              | 138 ms                                                                                                                | 130 ms: 1.06x faster                                                                                                      |
| xml_etree_iterparse      | 105 ms                                                                                                                | 99.6 ms: 1.05x faster                                                                                                     |
| json                     | 5.42 ms                                                                                                               | 5.18 ms: 1.04x faster                                                                                                     |
| deepcopy_memo            | 38.2 us                                                                                                               | 36.6 us: 1.04x faster                                                                                                     |
| go                       | 170 ms                                                                                                                | 164 ms: 1.04x faster                                                                                                      |
| xml_etree_generate       | 84.6 ms                                                                                                               | 81.4 ms: 1.04x faster                                                                                                     |
| unpickle_pure_python     | 222 us                                                                                                                | 214 us: 1.04x faster                                                                                                      |
| create_gc_cycles         | 2.03 ms                                                                                                               | 1.96 ms: 1.03x faster                                                                                                     |
| regex_dna                | 246 ms                                                                                                                | 239 ms: 1.03x faster                                                                                                      |
| regex_effbot             | 3.70 ms                                                                                                               | 3.60 ms: 1.03x faster                                                                                                     |
| pyflate                  | 483 ms                                                                                                                | 470 ms: 1.03x faster                                                                                                      |
| xml_etree_process        | 59.8 ms                                                                                                               | 58.3 ms: 1.03x faster                                                                                                     |
| pprint_safe_repr         | 810 ms                                                                                                                | 790 ms: 1.02x faster                                                                                                      |
| fannkuch                 | 358 ms                                                                                                                | 350 ms: 1.02x faster                                                                                                      |
| crypto_pyaes             | 72.1 ms                                                                                                               | 70.6 ms: 1.02x faster                                                                                                     |
| html5lib                 | 74.3 ms                                                                                                               | 72.8 ms: 1.02x faster                                                                                                     |
| scimark_fft              | 295 ms                                                                                                                | 289 ms: 1.02x faster                                                                                                      |
| scimark_sparse_mat_mult  | 4.12 ms                                                                                                               | 4.06 ms: 1.02x faster                                                                                                     |
| pprint_pformat           | 1.66 sec                                                                                                              | 1.63 sec: 1.01x faster                                                                                                    |
| regex_compile            | 143 ms                                                                                                                | 141 ms: 1.01x faster                                                                                                      |
| sqlite_synth             | 2.84 us                                                                                                               | 2.81 us: 1.01x faster                                                                                                     |
| pidigits                 | 253 ms                                                                                                                | 250 ms: 1.01x faster                                                                                                      |
| json_dumps               | 10.7 ms                                                                                                               | 10.6 ms: 1.01x faster                                                                                                     |
| dulwich_log              | 67.9 ms                                                                                                               | 67.5 ms: 1.01x faster                                                                                                     |
| coroutines               | 21.3 ms                                                                                                               | 21.3 ms: 1.00x slower                                                                                                     |
| asyncio_tcp_ssl          | 1.58 sec                                                                                                              | 1.58 sec: 1.00x slower                                                                                                    |
| thrift                   | 904 us                                                                                                                | 910 us: 1.01x slower                                                                                                      |
| unpickle                 | 14.7 us                                                                                                               | 14.8 us: 1.01x slower                                                                                                     |
| gc_traversal             | 4.40 ms                                                                                                               | 4.45 ms: 1.01x slower                                                                                                     |
| sqlglot_parse            | 1.42 ms                                                                                                               | 1.44 ms: 1.01x slower                                                                                                     |
| scimark_monte_carlo      | 64.2 ms                                                                                                               | 65.4 ms: 1.02x slower                                                                                                     |
| async_tree_none          | 366 ms                                                                                                                | 374 ms: 1.02x slower                                                                                                      |
| telco                    | 170 ms                                                                                                                | 174 ms: 1.02x slower                                                                                                      |
| unpickle_list            | 4.77 us                                                                                                               | 4.88 us: 1.02x slower                                                                                                     |
| pickle_pure_python       | 313 us                                                                                                                | 321 us: 1.03x slower                                                                                                      |
| meteor_contest           | 130 ms                                                                                                                | 134 ms: 1.03x slower                                                                                                      |
| raytrace                 | 276 ms                                                                                                                | 284 ms: 1.03x slower                                                                                                      |
| sqlglot_transpile        | 1.80 ms                                                                                                               | 1.85 ms: 1.03x slower                                                                                                     |
| generators               | 33.7 ms                                                                                                               | 34.9 ms: 1.04x slower                                                                                                     |
| coverage                 | 77.7 ms                                                                                                               | 80.6 ms: 1.04x slower                                                                                                     |
| mdp                      | 2.50 sec                                                                                                              | 2.60 sec: 1.04x slower                                                                                                    |
| dask                     | 395 ms                                                                                                                | 411 ms: 1.04x slower                                                                                                      |
| pickle                   | 10.5 us                                                                                                               | 10.9 us: 1.04x slower                                                                                                     |
| comprehensions           | 17.1 us                                                                                                               | 17.9 us: 1.04x slower                                                                                                     |
| tornado_http             | 119 ms                                                                                                                | 124 ms: 1.05x slower                                                                                                      |
| python_startup           | 12.8 ms                                                                                                               | 13.4 ms: 1.05x slower                                                                                                     |
| pickle_dict              | 30.7 us                                                                                                               | 32.2 us: 1.05x slower                                                                                                     |
| flaskblogging            | 4.73 ms                                                                                                               | 4.96 ms: 1.05x slower                                                                                                     |
| docutils                 | 2.99 sec                                                                                                              | 3.15 sec: 1.05x slower                                                                                                    |
| pickle_list              | 4.44 us                                                                                                               | 4.68 us: 1.05x slower                                                                                                     |
| typing_runtime_protocols | 177 us                                                                                                                | 186 us: 1.05x slower                                                                                                      |
| sympy_expand             | 507 ms                                                                                                                | 535 ms: 1.05x slower                                                                                                      |
| hexiom                   | 6.33 ms                                                                                                               | 6.68 ms: 1.06x slower                                                                                                     |
| sympy_str                | 298 ms                                                                                                                | 315 ms: 1.06x slower                                                                                                      |
| nqueens                  | 92.2 ms                                                                                                               | 97.4 ms: 1.06x slower                                                                                                     |
| 2to3                     | 289 ms                                                                                                                | 306 ms: 1.06x slower                                                                                                      |
| sqlglot_normalize        | 123 ms                                                                                                                | 130 ms: 1.06x slower                                                                                                      |
| async_generators         | 373 ms                                                                                                                | 396 ms: 1.06x slower                                                                                                      |
| logging_simple           | 6.37 us                                                                                                               | 6.76 us: 1.06x slower                                                                                                     |
| deepcopy_reduce          | 3.44 us                                                                                                               | 3.67 us: 1.06x slower                                                                                                     |
| bench_mp_pool            | 4.53 ms                                                                                                               | 4.82 ms: 1.06x slower                                                                                                     |
| bench_thread_pool        | 902 us                                                                                                                | 963 us: 1.07x slower                                                                                                      |
| python_startup_no_site   | 8.82 ms                                                                                                               | 9.43 ms: 1.07x slower                                                                                                     |
| logging_format           | 6.97 us                                                                                                               | 7.47 us: 1.07x slower                                                                                                     |
| sqlglot_optimize         | 60.1 ms                                                                                                               | 64.4 ms: 1.07x slower                                                                                                     |
| logging_silent           | 97.6 ns                                                                                                               | 105 ns: 1.07x slower                                                                                                      |
| sympy_sum                | 155 ms                                                                                                                | 168 ms: 1.08x slower                                                                                                      |
| chameleon                | 7.29 ms                                                                                                               | 8.00 ms: 1.10x slower                                                                                                     |
| django_template          | 39.4 ms                                                                                                               | 43.4 ms: 1.10x slower                                                                                                     |
| deepcopy                 | 384 us                                                                                                                | 424 us: 1.10x slower                                                                                                      |
| chaos                    | 59.8 ms                                                                                                               | 66.1 ms: 1.11x slower                                                                                                     |
| sympy_integrate          | 23.5 ms                                                                                                               | 26.0 ms: 1.11x slower                                                                                                     |
| deltablue                | 3.41 ms                                                                                                               | 3.79 ms: 1.11x slower                                                                                                     |
| pylint                   | 343 ms                                                                                                                | 383 ms: 1.12x slower                                                                                                      |
| scimark_lu               | 99.2 ms                                                                                                               | 115 ms: 1.16x slower                                                                                                      |
| genshi_text              | 25.4 ms                                                                                                               | 29.3 ms: 1.16x slower                                                                                                     |
| genshi_xml               | 55.9 ms                                                                                                               | 68.7 ms: 1.23x slower                                                                                                     |
| Geometric mean           | (ref)                                                                                                                 | 1.02x slower                                                                                                              |

Benchmark hidden because not significant (14): asyncio_websockets, json_loads, pathlib, xml_etree_parse, asyncio_tcp, async_tree_io_tg, pycparser, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none_tg, regex_v8, async_tree_memoization_tg

# HPT report

- Reliability score: 99.19% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x