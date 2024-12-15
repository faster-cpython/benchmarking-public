# Results vs. base

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.235x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x slower
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                                                                            | 353 ms: 1.38x slower                                                                                                    |
| docutils       | 2.59 sec                                                                                                          | 3.01 sec: 1.16x slower                                                                                                  |
| html5lib       | 64.1 ms                                                                                                           | 89.8 ms: 1.40x slower                                                                                                   |
| sphinx         | 1.02 sec                                                                                                          | 1.17 sec: 1.15x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.27x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                                                           | 26.8 ms: 1.16x slower                                                                                                   |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                                                            | 574 ms: 1.18x slower                                                                                                    |
| async_generators           | 417 ms                                                                                                            | 501 ms: 1.20x slower                                                                                                    |
| async_tree_io_tg           | 619 ms                                                                                                            | 748 ms: 1.21x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 500 ms                                                                                                            | 619 ms: 1.24x slower                                                                                                    |
| async_tree_io              | 627 ms                                                                                                            | 782 ms: 1.25x slower                                                                                                    |
| async_tree_none_tg         | 252 ms                                                                                                            | 330 ms: 1.31x slower                                                                                                    |
| async_tree_memoization_tg  | 314 ms                                                                                                            | 422 ms: 1.34x slower                                                                                                    |
| async_tree_none            | 271 ms                                                                                                            | 368 ms: 1.36x slower                                                                                                    |
| async_tree_memoization     | 339 ms                                                                                                            | 464 ms: 1.37x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.23x slower                                                                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                                                            | 191 ms: 1.02x slower                                                                                                    |
| nbody          | 95.5 ms                                                                                                           | 139 ms: 1.46x slower                                                                                                    |
| float          | 77.5 ms                                                                                                           | 129 ms: 1.66x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.35x slower                                                                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                                                                            | 224 ms: 1.01x slower                                                                                                    |
| regex_v8       | 25.0 ms                                                                                                           | 25.7 ms: 1.03x slower                                                                                                   |
| regex_effbot   | 3.31 ms                                                                                                           | 3.51 ms: 1.06x slower                                                                                                   |
| regex_compile  | 128 ms                                                                                                            | 170 ms: 1.33x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.10x slower                                                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 97.3 ms                                                                                                           | 96.5 ms: 1.01x faster                                                                                                   |
| xml_etree_parse      | 138 ms                                                                                                            | 148 ms: 1.08x slower                                                                                                    |
| json_loads           | 27.1 us                                                                                                           | 30.1 us: 1.11x slower                                                                                                   |
| xml_etree_generate   | 86.6 ms                                                                                                           | 96.9 ms: 1.12x slower                                                                                                   |
| json_dumps           | 11.6 ms                                                                                                           | 13.4 ms: 1.15x slower                                                                                                   |
| xml_etree_process    | 59.9 ms                                                                                                           | 75.0 ms: 1.25x slower                                                                                                   |
| tomli_loads          | 2.04 sec                                                                                                          | 2.62 sec: 1.29x slower                                                                                                  |
| unpickle_pure_python | 219 us                                                                                                            | 316 us: 1.44x slower                                                                                                    |
| pickle_pure_python   | 324 us                                                                                                            | 479 us: 1.48x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.20x slower                                                                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.9 ms                                                                                                           | 16.1 ms: 1.25x slower                                                                                                   |
| python_startup_no_site | 7.09 ms                                                                                                           | 9.81 ms: 1.38x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.32x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 49.8 ms                                                                                                           | 64.3 ms: 1.29x slower                                                                                                   |
| genshi_text     | 22.2 ms                                                                                                           | 30.5 ms: 1.37x slower                                                                                                   |
| django_template | 32.0 ms                                                                                                           | 47.1 ms: 1.47x slower                                                                                                   |
| mako            | 11.4 ms                                                                                                           | 18.0 ms: 1.57x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.42x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| gc_traversal               | 4.94 ms                                                                                                           | 3.65 ms: 1.35x faster                                                                                                   |
| create_gc_cycles           | 2.47 ms                                                                                                           | 2.31 ms: 1.07x faster                                                                                                   |
| xml_etree_iterparse        | 97.3 ms                                                                                                           | 96.5 ms: 1.01x faster                                                                                                   |
| regex_dna                  | 221 ms                                                                                                            | 224 ms: 1.01x slower                                                                                                    |
| pidigits                   | 186 ms                                                                                                            | 191 ms: 1.02x slower                                                                                                    |
| regex_v8                   | 25.0 ms                                                                                                           | 25.7 ms: 1.03x slower                                                                                                   |
| regex_effbot               | 3.31 ms                                                                                                           | 3.51 ms: 1.06x slower                                                                                                   |
| pathlib                    | 16.5 ms                                                                                                           | 17.5 ms: 1.06x slower                                                                                                   |
| json                       | 5.05 ms                                                                                                           | 5.44 ms: 1.08x slower                                                                                                   |
| xml_etree_parse            | 138 ms                                                                                                            | 148 ms: 1.08x slower                                                                                                    |
| k_core                     | 2.28 sec                                                                                                          | 2.48 sec: 1.09x slower                                                                                                  |
| json_loads                 | 27.1 us                                                                                                           | 30.1 us: 1.11x slower                                                                                                   |
| xml_etree_generate         | 86.6 ms                                                                                                           | 96.9 ms: 1.12x slower                                                                                                   |
| sphinx                     | 1.02 sec                                                                                                          | 1.17 sec: 1.15x slower                                                                                                  |
| spectral_norm              | 108 ms                                                                                                            | 124 ms: 1.15x slower                                                                                                    |
| json_dumps                 | 11.6 ms                                                                                                           | 13.4 ms: 1.15x slower                                                                                                   |
| coroutines                 | 23.2 ms                                                                                                           | 26.8 ms: 1.16x slower                                                                                                   |
| docutils                   | 2.59 sec                                                                                                          | 3.01 sec: 1.16x slower                                                                                                  |
| bpe_tokeniser              | 4.54 sec                                                                                                          | 5.26 sec: 1.16x slower                                                                                                  |
| telco                      | 7.85 ms                                                                                                           | 9.21 ms: 1.17x slower                                                                                                   |
| deepcopy                   | 268 us                                                                                                            | 316 us: 1.18x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                                                            | 574 ms: 1.18x slower                                                                                                    |
| mdp                        | 2.54 sec                                                                                                          | 3.05 sec: 1.20x slower                                                                                                  |
| scimark_fft                | 347 ms                                                                                                            | 416 ms: 1.20x slower                                                                                                    |
| async_generators           | 417 ms                                                                                                            | 501 ms: 1.20x slower                                                                                                    |
| many_optionals             | 956 us                                                                                                            | 1.15 ms: 1.20x slower                                                                                                   |
| connected_components       | 444 ms                                                                                                            | 535 ms: 1.21x slower                                                                                                    |
| shortest_path              | 480 ms                                                                                                            | 579 ms: 1.21x slower                                                                                                    |
| async_tree_io_tg           | 619 ms                                                                                                            | 748 ms: 1.21x slower                                                                                                    |
| meteor_contest             | 106 ms                                                                                                            | 130 ms: 1.22x slower                                                                                                    |
| nqueens                    | 80.0 ms                                                                                                           | 98.2 ms: 1.23x slower                                                                                                   |
| dulwich_log                | 64.7 ms                                                                                                           | 79.5 ms: 1.23x slower                                                                                                   |
| pycparser                  | 1.18 sec                                                                                                          | 1.45 sec: 1.23x slower                                                                                                  |
| deepcopy_reduce            | 2.81 us                                                                                                           | 3.46 us: 1.23x slower                                                                                                   |
| async_tree_cpu_io_mixed    | 500 ms                                                                                                            | 619 ms: 1.24x slower                                                                                                    |
| sqlglot_optimize           | 52.8 ms                                                                                                           | 65.5 ms: 1.24x slower                                                                                                   |
| sqlglot_normalize          | 104 ms                                                                                                            | 130 ms: 1.24x slower                                                                                                    |
| bench_mp_pool              | 81.5 ms                                                                                                           | 102 ms: 1.25x slower                                                                                                    |
| async_tree_io              | 627 ms                                                                                                            | 782 ms: 1.25x slower                                                                                                    |
| xml_etree_process          | 59.9 ms                                                                                                           | 75.0 ms: 1.25x slower                                                                                                   |
| python_startup             | 12.9 ms                                                                                                           | 16.1 ms: 1.25x slower                                                                                                   |
| scimark_sparse_mat_mult    | 4.87 ms                                                                                                           | 6.12 ms: 1.26x slower                                                                                                   |
| crypto_pyaes               | 72.8 ms                                                                                                           | 92.9 ms: 1.28x slower                                                                                                   |
| pylint                     | 277 ms                                                                                                            | 353 ms: 1.28x slower                                                                                                    |
| generators                 | 28.2 ms                                                                                                           | 36.2 ms: 1.28x slower                                                                                                   |
| tomli_loads                | 2.04 sec                                                                                                          | 2.62 sec: 1.29x slower                                                                                                  |
| typing_runtime_protocols   | 162 us                                                                                                            | 209 us: 1.29x slower                                                                                                    |
| genshi_xml                 | 49.8 ms                                                                                                           | 64.3 ms: 1.29x slower                                                                                                   |
| fannkuch                   | 401 ms                                                                                                            | 524 ms: 1.30x slower                                                                                                    |
| sympy_integrate            | 20.1 ms                                                                                                           | 26.2 ms: 1.31x slower                                                                                                   |
| async_tree_none_tg         | 252 ms                                                                                                            | 330 ms: 1.31x slower                                                                                                    |
| coverage                   | 83.2 ms                                                                                                           | 109 ms: 1.31x slower                                                                                                    |
| deepcopy_memo              | 31.0 us                                                                                                           | 40.6 us: 1.31x slower                                                                                                   |
| regex_compile              | 128 ms                                                                                                            | 170 ms: 1.33x slower                                                                                                    |
| subparsers                 | 20.9 ms                                                                                                           | 27.7 ms: 1.33x slower                                                                                                   |
| mypy2                      | 953 ms                                                                                                            | 1.28 sec: 1.34x slower                                                                                                  |
| async_tree_memoization_tg  | 314 ms                                                                                                            | 422 ms: 1.34x slower                                                                                                    |
| async_tree_none            | 271 ms                                                                                                            | 368 ms: 1.36x slower                                                                                                    |
| pprint_pformat             | 1.52 sec                                                                                                          | 2.07 sec: 1.36x slower                                                                                                  |
| pprint_safe_repr           | 734 ms                                                                                                            | 1000 ms: 1.36x slower                                                                                                   |
| async_tree_memoization     | 339 ms                                                                                                            | 464 ms: 1.37x slower                                                                                                    |
| genshi_text                | 22.2 ms                                                                                                           | 30.5 ms: 1.37x slower                                                                                                   |
| 2to3                       | 257 ms                                                                                                            | 353 ms: 1.38x slower                                                                                                    |
| python_startup_no_site     | 7.09 ms                                                                                                           | 9.81 ms: 1.38x slower                                                                                                   |
| sympy_str                  | 270 ms                                                                                                            | 376 ms: 1.39x slower                                                                                                    |
| html5lib                   | 64.1 ms                                                                                                           | 89.8 ms: 1.40x slower                                                                                                   |
| pyflate                    | 467 ms                                                                                                            | 655 ms: 1.40x slower                                                                                                    |
| thrift                     | 761 us                                                                                                            | 1.09 ms: 1.43x slower                                                                                                   |
| unpickle_pure_python       | 219 us                                                                                                            | 316 us: 1.44x slower                                                                                                    |
| nbody                      | 95.5 ms                                                                                                           | 139 ms: 1.46x slower                                                                                                    |
| django_template            | 32.0 ms                                                                                                           | 47.1 ms: 1.47x slower                                                                                                   |
| pickle_pure_python         | 324 us                                                                                                            | 479 us: 1.48x slower                                                                                                    |
| scimark_lu                 | 118 ms                                                                                                            | 176 ms: 1.49x slower                                                                                                    |
| sqlalchemy_declarative     | 127 ms                                                                                                            | 190 ms: 1.49x slower                                                                                                    |
| sympy_expand               | 457 ms                                                                                                            | 682 ms: 1.49x slower                                                                                                    |
| sqlalchemy_imperative      | 16.4 ms                                                                                                           | 24.5 ms: 1.49x slower                                                                                                   |
| comprehensions             | 17.0 us                                                                                                           | 25.7 us: 1.51x slower                                                                                                   |
| richards_super             | 52.4 ms                                                                                                           | 80.0 ms: 1.53x slower                                                                                                   |
| logging_simple             | 5.56 us                                                                                                           | 8.55 us: 1.54x slower                                                                                                   |
| logging_format             | 6.11 us                                                                                                           | 9.52 us: 1.56x slower                                                                                                   |
| mako                       | 11.4 ms                                                                                                           | 18.0 ms: 1.57x slower                                                                                                   |
| sympy_sum                  | 149 ms                                                                                                            | 235 ms: 1.58x slower                                                                                                    |
| hexiom                     | 6.23 ms                                                                                                           | 9.82 ms: 1.58x slower                                                                                                   |
| chaos                      | 61.4 ms                                                                                                           | 98.7 ms: 1.61x slower                                                                                                   |
| richards                   | 45.8 ms                                                                                                           | 74.0 ms: 1.62x slower                                                                                                   |
| float                      | 77.5 ms                                                                                                           | 129 ms: 1.66x slower                                                                                                    |
| scimark_monte_carlo        | 68.1 ms                                                                                                           | 113 ms: 1.66x slower                                                                                                    |
| logging_silent             | 106 ns                                                                                                            | 178 ns: 1.67x slower                                                                                                    |
| sqlglot_transpile          | 1.60 ms                                                                                                           | 2.76 ms: 1.72x slower                                                                                                   |
| scimark_sor                | 125 ms                                                                                                            | 226 ms: 1.80x slower                                                                                                    |
| raytrace                   | 272 ms                                                                                                            | 502 ms: 1.84x slower                                                                                                    |
| sqlglot_parse              | 1.29 ms                                                                                                           | 2.39 ms: 1.86x slower                                                                                                   |
| go                         | 120 ms                                                                                                            | 240 ms: 2.00x slower                                                                                                    |
| deltablue                  | 3.25 ms                                                                                                           | 7.57 ms: 2.33x slower                                                                                                   |
| bench_thread_pool          | 862 us                                                                                                            | 3.57 ms: 4.15x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.32x slower                                                                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, sqlite_synth
Ignored benchmarks (1) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: djangocms

- Geometric mean (including insignificant results): 1.235x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.25x
- 95% likely to have a slowdown of 1.24x
- 99% likely to have a slowdown of 1.23x

# Memory
- memory change: 1.18x