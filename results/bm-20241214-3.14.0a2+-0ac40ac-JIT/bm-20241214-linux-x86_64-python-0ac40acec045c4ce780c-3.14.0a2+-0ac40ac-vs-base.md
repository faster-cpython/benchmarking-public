# Results vs. base

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.001x faster
- HPT reliability: 63.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                                                                            | 259 ms: 1.01x slower                                                                                                  |
| docutils       | 2.59 sec                                                                                                          | 2.70 sec: 1.04x slower                                                                                                |
| html5lib       | 64.1 ms                                                                                                           | 65.3 ms: 1.02x slower                                                                                                 |
| sphinx         | 1.02 sec                                                                                                          | 1.06 sec: 1.04x slower                                                                                                |
| Geometric mean | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_none            | 271 ms                                                                                                            | 266 ms: 1.02x faster                                                                                                  |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                                                            | 478 ms: 1.01x faster                                                                                                  |
| async_tree_memoization     | 339 ms                                                                                                            | 336 ms: 1.01x faster                                                                                                  |
| async_tree_cpu_io_mixed    | 500 ms                                                                                                            | 496 ms: 1.01x faster                                                                                                  |
| asyncio_websockets         | 553 ms                                                                                                            | 556 ms: 1.01x slower                                                                                                  |
| async_generators           | 417 ms                                                                                                            | 446 ms: 1.07x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (5): async_tree_io, coroutines, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| nbody          | 95.5 ms                                                                                                           | 82.6 ms: 1.16x faster                                                                                                 |
| float          | 77.5 ms                                                                                                           | 73.3 ms: 1.06x faster                                                                                                 |
| pidigits       | 186 ms                                                                                                            | 186 ms: 1.00x faster                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.07x faster                                                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.31 ms                                                                                                           | 3.24 ms: 1.02x faster                                                                                                 |
| regex_v8       | 25.0 ms                                                                                                           | 24.7 ms: 1.01x faster                                                                                                 |
| regex_dna      | 221 ms                                                                                                            | 219 ms: 1.01x faster                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 219 us                                                                                                            | 193 us: 1.13x faster                                                                                                  |
| xml_etree_generate   | 86.6 ms                                                                                                           | 78.3 ms: 1.11x faster                                                                                                 |
| tomli_loads          | 2.04 sec                                                                                                          | 1.85 sec: 1.10x faster                                                                                                |
| xml_etree_process    | 59.9 ms                                                                                                           | 55.7 ms: 1.08x faster                                                                                                 |
| json_loads           | 27.1 us                                                                                                           | 26.0 us: 1.04x faster                                                                                                 |
| xml_etree_iterparse  | 97.3 ms                                                                                                           | 94.5 ms: 1.03x faster                                                                                                 |
| json_dumps           | 11.6 ms                                                                                                           | 11.4 ms: 1.02x faster                                                                                                 |
| pickle_pure_python   | 324 us                                                                                                            | 321 us: 1.01x faster                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.06x faster                                                                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                                                           | 12.8 ms: 1.01x faster                                                                                                 |
| python_startup_no_site | 7.09 ms                                                                                                           | 7.06 ms: 1.00x faster                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 11.4 ms                                                                                                           | 10.3 ms: 1.11x faster                                                                                                 |
| django_template | 32.0 ms                                                                                                           | 33.9 ms: 1.06x slower                                                                                                 |
| genshi_text     | 22.2 ms                                                                                                           | 23.8 ms: 1.07x slower                                                                                                 |
| genshi_xml      | 49.8 ms                                                                                                           | 58.6 ms: 1.18x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.05x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                  | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| nbody                      | 95.5 ms                                                                                                           | 82.6 ms: 1.16x faster                                                                                                 |
| unpickle_pure_python       | 219 us                                                                                                            | 193 us: 1.13x faster                                                                                                  |
| mako                       | 11.4 ms                                                                                                           | 10.3 ms: 1.11x faster                                                                                                 |
| scimark_fft                | 347 ms                                                                                                            | 313 ms: 1.11x faster                                                                                                  |
| xml_etree_generate         | 86.6 ms                                                                                                           | 78.3 ms: 1.11x faster                                                                                                 |
| tomli_loads                | 2.04 sec                                                                                                          | 1.85 sec: 1.10x faster                                                                                                |
| scimark_sor                | 125 ms                                                                                                            | 114 ms: 1.10x faster                                                                                                  |
| scimark_monte_carlo        | 68.1 ms                                                                                                           | 62.0 ms: 1.10x faster                                                                                                 |
| xml_etree_process          | 59.9 ms                                                                                                           | 55.7 ms: 1.08x faster                                                                                                 |
| crypto_pyaes               | 72.8 ms                                                                                                           | 68.0 ms: 1.07x faster                                                                                                 |
| float                      | 77.5 ms                                                                                                           | 73.3 ms: 1.06x faster                                                                                                 |
| spectral_norm              | 108 ms                                                                                                            | 103 ms: 1.05x faster                                                                                                  |
| json                       | 5.05 ms                                                                                                           | 4.81 ms: 1.05x faster                                                                                                 |
| fannkuch                   | 401 ms                                                                                                            | 385 ms: 1.04x faster                                                                                                  |
| deepcopy_memo              | 31.0 us                                                                                                           | 29.8 us: 1.04x faster                                                                                                 |
| json_loads                 | 27.1 us                                                                                                           | 26.0 us: 1.04x faster                                                                                                 |
| telco                      | 7.85 ms                                                                                                           | 7.59 ms: 1.04x faster                                                                                                 |
| pyflate                    | 467 ms                                                                                                            | 452 ms: 1.03x faster                                                                                                  |
| xml_etree_iterparse        | 97.3 ms                                                                                                           | 94.5 ms: 1.03x faster                                                                                                 |
| scimark_sparse_mat_mult    | 4.87 ms                                                                                                           | 4.74 ms: 1.03x faster                                                                                                 |
| json_dumps                 | 11.6 ms                                                                                                           | 11.4 ms: 1.02x faster                                                                                                 |
| bpe_tokeniser              | 4.54 sec                                                                                                          | 4.43 sec: 1.02x faster                                                                                                |
| richards                   | 45.8 ms                                                                                                           | 44.7 ms: 1.02x faster                                                                                                 |
| regex_effbot               | 3.31 ms                                                                                                           | 3.24 ms: 1.02x faster                                                                                                 |
| sqlite_synth               | 2.83 us                                                                                                           | 2.77 us: 1.02x faster                                                                                                 |
| richards_super             | 52.4 ms                                                                                                           | 51.4 ms: 1.02x faster                                                                                                 |
| deepcopy_reduce            | 2.81 us                                                                                                           | 2.76 us: 1.02x faster                                                                                                 |
| pprint_pformat             | 1.52 sec                                                                                                          | 1.50 sec: 1.02x faster                                                                                                |
| async_tree_none            | 271 ms                                                                                                            | 266 ms: 1.02x faster                                                                                                  |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                                                            | 478 ms: 1.01x faster                                                                                                  |
| connected_components       | 444 ms                                                                                                            | 438 ms: 1.01x faster                                                                                                  |
| regex_v8                   | 25.0 ms                                                                                                           | 24.7 ms: 1.01x faster                                                                                                 |
| regex_dna                  | 221 ms                                                                                                            | 219 ms: 1.01x faster                                                                                                  |
| async_tree_memoization     | 339 ms                                                                                                            | 336 ms: 1.01x faster                                                                                                  |
| pickle_pure_python         | 324 us                                                                                                            | 321 us: 1.01x faster                                                                                                  |
| async_tree_cpu_io_mixed    | 500 ms                                                                                                            | 496 ms: 1.01x faster                                                                                                  |
| sqlglot_parse              | 1.29 ms                                                                                                           | 1.28 ms: 1.01x faster                                                                                                 |
| python_startup             | 12.9 ms                                                                                                           | 12.8 ms: 1.01x faster                                                                                                 |
| python_startup_no_site     | 7.09 ms                                                                                                           | 7.06 ms: 1.00x faster                                                                                                 |
| bench_mp_pool              | 81.5 ms                                                                                                           | 81.2 ms: 1.00x faster                                                                                                 |
| pidigits                   | 186 ms                                                                                                            | 186 ms: 1.00x faster                                                                                                  |
| gc_traversal               | 4.94 ms                                                                                                           | 4.95 ms: 1.00x slower                                                                                                 |
| sqlglot_transpile          | 1.60 ms                                                                                                           | 1.61 ms: 1.01x slower                                                                                                 |
| asyncio_websockets         | 553 ms                                                                                                            | 556 ms: 1.01x slower                                                                                                  |
| comprehensions             | 17.0 us                                                                                                           | 17.1 us: 1.01x slower                                                                                                 |
| deepcopy                   | 268 us                                                                                                            | 270 us: 1.01x slower                                                                                                  |
| logging_silent             | 106 ns                                                                                                            | 107 ns: 1.01x slower                                                                                                  |
| thrift                     | 761 us                                                                                                            | 769 us: 1.01x slower                                                                                                  |
| coverage                   | 83.2 ms                                                                                                           | 84.1 ms: 1.01x slower                                                                                                 |
| 2to3                       | 257 ms                                                                                                            | 259 ms: 1.01x slower                                                                                                  |
| deltablue                  | 3.25 ms                                                                                                           | 3.29 ms: 1.01x slower                                                                                                 |
| meteor_contest             | 106 ms                                                                                                            | 108 ms: 1.01x slower                                                                                                  |
| sqlalchemy_declarative     | 127 ms                                                                                                            | 129 ms: 1.02x slower                                                                                                  |
| html5lib                   | 64.1 ms                                                                                                           | 65.3 ms: 1.02x slower                                                                                                 |
| sqlalchemy_imperative      | 16.4 ms                                                                                                           | 16.7 ms: 1.02x slower                                                                                                 |
| djangocms                  | 21.8 us                                                                                                           | 22.3 us: 1.02x slower                                                                                                 |
| typing_runtime_protocols   | 162 us                                                                                                            | 166 us: 1.02x slower                                                                                                  |
| pprint_safe_repr           | 734 ms                                                                                                            | 752 ms: 1.03x slower                                                                                                  |
| logging_format             | 6.11 us                                                                                                           | 6.27 us: 1.03x slower                                                                                                 |
| logging_simple             | 5.56 us                                                                                                           | 5.71 us: 1.03x slower                                                                                                 |
| bench_thread_pool          | 862 us                                                                                                            | 887 us: 1.03x slower                                                                                                  |
| many_optionals             | 956 us                                                                                                            | 985 us: 1.03x slower                                                                                                  |
| dulwich_log                | 64.7 ms                                                                                                           | 66.9 ms: 1.03x slower                                                                                                 |
| sympy_integrate            | 20.1 ms                                                                                                           | 20.8 ms: 1.03x slower                                                                                                 |
| sphinx                     | 1.02 sec                                                                                                          | 1.06 sec: 1.04x slower                                                                                                |
| sqlglot_optimize           | 52.8 ms                                                                                                           | 54.8 ms: 1.04x slower                                                                                                 |
| docutils                   | 2.59 sec                                                                                                          | 2.70 sec: 1.04x slower                                                                                                |
| raytrace                   | 272 ms                                                                                                            | 284 ms: 1.04x slower                                                                                                  |
| go                         | 120 ms                                                                                                            | 125 ms: 1.04x slower                                                                                                  |
| sqlglot_normalize          | 104 ms                                                                                                            | 109 ms: 1.05x slower                                                                                                  |
| sympy_expand               | 457 ms                                                                                                            | 478 ms: 1.05x slower                                                                                                  |
| sympy_sum                  | 149 ms                                                                                                            | 156 ms: 1.05x slower                                                                                                  |
| pylint                     | 277 ms                                                                                                            | 290 ms: 1.05x slower                                                                                                  |
| sympy_str                  | 270 ms                                                                                                            | 283 ms: 1.05x slower                                                                                                  |
| django_template            | 32.0 ms                                                                                                           | 33.9 ms: 1.06x slower                                                                                                 |
| mdp                        | 2.54 sec                                                                                                          | 2.69 sec: 1.06x slower                                                                                                |
| async_generators           | 417 ms                                                                                                            | 446 ms: 1.07x slower                                                                                                  |
| genshi_text                | 22.2 ms                                                                                                           | 23.8 ms: 1.07x slower                                                                                                 |
| nqueens                    | 80.0 ms                                                                                                           | 89.1 ms: 1.11x slower                                                                                                 |
| hexiom                     | 6.23 ms                                                                                                           | 7.03 ms: 1.13x slower                                                                                                 |
| genshi_xml                 | 49.8 ms                                                                                                           | 58.6 ms: 1.18x slower                                                                                                 |
| generators                 | 28.2 ms                                                                                                           | 34.6 ms: 1.22x slower                                                                                                 |
| Geometric mean             | (ref)                                                                                                             | 1.00x faster                                                                                                          |

Benchmark hidden because not significant (16): async_tree_io, scimark_lu, xml_etree_parse, coroutines, pathlib, create_gc_cycles, async_tree_none_tg, shortest_path, async_tree_memoization_tg, chaos, regex_compile, pycparser, k_core, subparsers, mypy2, async_tree_io_tg

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 63.50% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x