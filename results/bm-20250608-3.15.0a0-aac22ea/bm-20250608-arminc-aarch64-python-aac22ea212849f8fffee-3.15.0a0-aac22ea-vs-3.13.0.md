# Results vs. 3.13.0

- fork: python
- ref: aac22ea212849f8fffee
- machine: linux-aarch64
- commit hash: aac22ea
- commit date: 2025-06-08
- overall geometric mean: 1.026x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 300 ms: 1.04x faster                                                    |
| docutils       | 2.96 sec                                                 | 2.91 sec: 1.02x faster                                                  |
| html5lib       | 65.6 ms                                                  | 61.1 ms: 1.07x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.15 sec: 1.05x faster                                                  |
| Geometric mean | (ref)                                                    | 1.05x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 463 ms: 1.43x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 468 ms: 1.42x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 870 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 374 ms: 1.30x faster                                                    |
| async_tree_none            | 504 ms                                                   | 392 ms: 1.28x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 911 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 651 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 661 ms: 1.19x faster                                                    |
| async_generators           | 500 ms                                                   | 451 ms: 1.11x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.3 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 27.6 ms: 1.18x faster                                                   |
| regex_dna      | 263 ms                                                   | 232 ms: 1.13x faster                                                    |
| regex_compile  | 134 ms                                                   | 122 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                    | 1.18x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.12x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| tomli_loads         | 2.67 sec                                                 | 2.47 sec: 1.08x faster                                                  |
| xml_etree_generate  | 118 ms                                                   | 112 ms: 1.06x faster                                                    |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (5): json_dumps, xml_etree_process, json_loads, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.3 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.67 sec: 2.06x faster                                                  |
| deepcopy                   | 479 us                                                   | 325 us: 1.47x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 463 ms: 1.43x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 468 ms: 1.42x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 37.6 us: 1.41x faster                                                   |
| regex_effbot               | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                   |
| async_tree_io              | 1.14 sec                                                 | 870 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 374 ms: 1.30x faster                                                    |
| go                         | 164 ms                                                   | 127 ms: 1.29x faster                                                    |
| async_tree_none            | 504 ms                                                   | 392 ms: 1.28x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 911 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 651 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 661 ms: 1.19x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.58 us: 1.19x faster                                                   |
| regex_v8                   | 32.5 ms                                                  | 27.6 ms: 1.18x faster                                                   |
| regex_dna                  | 263 ms                                                   | 232 ms: 1.13x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.27 ms: 1.13x faster                                                   |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.12x faster                                                    |
| scimark_sor                | 164 ms                                                   | 146 ms: 1.12x faster                                                    |
| async_generators           | 500 ms                                                   | 451 ms: 1.11x faster                                                    |
| float                      | 95.8 ms                                                  | 86.3 ms: 1.11x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| regex_compile              | 134 ms                                                   | 122 ms: 1.10x faster                                                    |
| pylint                     | 345 ms                                                   | 315 ms: 1.10x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.53 sec: 1.09x faster                                                  |
| spectral_norm              | 143 ms                                                   | 132 ms: 1.09x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.5 ms: 1.08x faster                                                   |
| scimark_monte_carlo        | 87.8 ms                                                  | 81.2 ms: 1.08x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.47 sec: 1.08x faster                                                  |
| html5lib                   | 65.6 ms                                                  | 61.1 ms: 1.07x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.79 sec: 1.07x faster                                                  |
| pyflate                    | 582 ms                                                   | 545 ms: 1.07x faster                                                    |
| scimark_fft                | 463 ms                                                   | 434 ms: 1.07x faster                                                    |
| sympy_integrate            | 21.4 ms                                                  | 20.2 ms: 1.06x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 112 ms: 1.06x faster                                                    |
| richards                   | 54.5 ms                                                  | 51.6 ms: 1.06x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.28 sec: 1.05x faster                                                  |
| nqueens                    | 105 ms                                                   | 99.7 ms: 1.05x faster                                                   |
| python_startup             | 16.0 ms                                                  | 15.3 ms: 1.05x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.15 sec: 1.05x faster                                                  |
| hexiom                     | 7.34 ms                                                  | 7.01 ms: 1.05x faster                                                   |
| richards_super             | 60.8 ms                                                  | 58.2 ms: 1.05x faster                                                   |
| 2to3                       | 313 ms                                                   | 300 ms: 1.04x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.93 us: 1.04x faster                                                   |
| chaos                      | 70.7 ms                                                  | 68.1 ms: 1.04x faster                                                   |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.03x faster                                                    |
| docutils                   | 2.96 sec                                                 | 2.91 sec: 1.02x faster                                                  |
| pprint_pformat             | 1.99 sec                                                 | 2.03 sec: 1.02x slower                                                  |
| shortest_path              | 565 ms                                                   | 580 ms: 1.03x slower                                                    |
| connected_components       | 547 ms                                                   | 562 ms: 1.03x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 999 ms: 1.04x slower                                                    |
| logging_format             | 8.10 us                                                  | 8.46 us: 1.04x slower                                                   |
| raytrace                   | 310 ms                                                   | 326 ms: 1.05x slower                                                    |
| logging_simple             | 7.25 us                                                  | 7.84 us: 1.08x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.72 ms: 1.10x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.82 ms: 1.15x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 28.1 ms: 1.38x slower                                                   |
| many_optionals             | 626 us                                                   | 883 us: 1.41x slower                                                    |
| logging_silent             | 135 ns                                                   | 618 ns: 4.59x slower                                                    |
| coverage                   | 106 ms                                                   | 569 ms: 5.38x slower                                                    |
| thrift                     | 1.01 ms                                                  | 197 ms: 194.55x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (26): generators, json, comprehensions, sympy_sum, json_dumps, xml_etree_process, python_startup_no_site, pidigits, json_loads, genshi_text, fannkuch, mako, deltablue, typing_runtime_protocols, sympy_expand, asyncio_websockets, crypto_pyaes, unpickle_pure_python, sympy_str, coroutines, django_template, genshi_xml, nbody, scimark_sparse_mat_mult, scimark_lu, pickle_pure_python
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250608-3.15.0a0-aac22ea/bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.026x slower

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x