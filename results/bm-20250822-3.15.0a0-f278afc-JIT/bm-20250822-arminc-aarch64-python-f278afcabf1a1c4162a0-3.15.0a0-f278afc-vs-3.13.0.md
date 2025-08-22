# Results vs. 3.13.0

- fork: python
- ref: f278afcabf1a1c4162a0
- machine: linux-aarch64
- commit hash: f278afc
- commit date: 2025-08-22
- overall geometric mean: 1.022x faster
- HPT reliability: 99.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.03 sec: 1.02x slower                                                  |
| html5lib       | 65.6 ms                                                  | 61.1 ms: 1.07x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                  |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 471 ms: 1.41x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 481 ms: 1.38x faster                                                    |
| async_tree_none            | 504 ms                                                   | 381 ms: 1.32x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 900 ms: 1.29x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 880 ms: 1.29x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 382 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 654 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 660 ms: 1.20x faster                                                    |
| async_generators           | 500 ms                                                   | 481 ms: 1.04x faster                                                    |
| coroutines                 | 29.4 ms                                                  | 31.5 ms: 1.07x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 81.3 ms: 1.18x faster                                                   |
| nbody          | 118 ms                                                   | 127 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.78 ms: 1.35x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 27.0 ms: 1.20x faster                                                   |
| regex_dna      | 263 ms                                                   | 223 ms: 1.18x faster                                                    |
| regex_compile  | 134 ms                                                   | 121 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                    | 1.21x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps          | 14.2 ms                                                  | 12.1 ms: 1.18x faster                                                   |
| tomli_loads         | 2.67 sec                                                 | 2.31 sec: 1.16x faster                                                  |
| xml_etree_parse     | 203 ms                                                   | 183 ms: 1.11x faster                                                    |
| xml_etree_generate  | 118 ms                                                   | 107 ms: 1.10x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 147 ms: 1.08x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 76.7 ms: 1.07x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.08x faster                                                            |

Benchmark hidden because not significant (3): unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.59 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.05x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 12.8 ms: 1.09x faster                                                   |
| genshi_text    | 28.6 ms                                                  | 26.8 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.65 sec: 2.09x faster                                                  |
| deepcopy_memo              | 53.0 us                                                  | 35.9 us: 1.48x faster                                                   |
| deepcopy                   | 479 us                                                   | 330 us: 1.45x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 471 ms: 1.41x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 481 ms: 1.38x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.78 ms: 1.35x faster                                                   |
| async_tree_none            | 504 ms                                                   | 381 ms: 1.32x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 900 ms: 1.29x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 880 ms: 1.29x faster                                                    |
| richards                   | 54.5 ms                                                  | 43.0 ms: 1.27x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 382 ms: 1.27x faster                                                    |
| spectral_norm              | 143 ms                                                   | 115 ms: 1.25x faster                                                    |
| richards_super             | 60.8 ms                                                  | 49.5 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 654 ms: 1.22x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 27.0 ms: 1.20x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 660 ms: 1.20x faster                                                    |
| float                      | 95.8 ms                                                  | 81.3 ms: 1.18x faster                                                   |
| regex_dna                  | 263 ms                                                   | 223 ms: 1.18x faster                                                    |
| json_dumps                 | 14.2 ms                                                  | 12.1 ms: 1.18x faster                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 3.63 us: 1.17x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.31 sec: 1.16x faster                                                  |
| scimark_sor                | 164 ms                                                   | 143 ms: 1.15x faster                                                    |
| scimark_fft                | 463 ms                                                   | 409 ms: 1.13x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.33 sec: 1.13x faster                                                  |
| xml_etree_parse            | 203 ms                                                   | 183 ms: 1.11x faster                                                    |
| regex_compile              | 134 ms                                                   | 121 ms: 1.10x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.0 ms: 1.10x faster                                                   |
| logging_format             | 8.10 us                                                  | 7.34 us: 1.10x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 107 ms: 1.10x faster                                                    |
| go                         | 164 ms                                                   | 150 ms: 1.10x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.9 ms: 1.09x faster                                                   |
| logging_simple             | 7.25 us                                                  | 6.65 us: 1.09x faster                                                   |
| pyflate                    | 582 ms                                                   | 535 ms: 1.09x faster                                                    |
| mako                       | 14.0 ms                                                  | 12.8 ms: 1.09x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 147 ms: 1.08x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.79 us: 1.08x faster                                                   |
| html5lib                   | 65.6 ms                                                  | 61.1 ms: 1.07x faster                                                   |
| scimark_monte_carlo        | 87.8 ms                                                  | 81.9 ms: 1.07x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 76.7 ms: 1.07x faster                                                   |
| python_startup             | 16.0 ms                                                  | 15.0 ms: 1.07x faster                                                   |
| pylint                     | 345 ms                                                   | 323 ms: 1.07x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 26.8 ms: 1.06x faster                                                   |
| thrift                     | 1.01 ms                                                  | 952 us: 1.06x faster                                                    |
| meteor_contest             | 117 ms                                                   | 111 ms: 1.06x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                                  |
| logging_silent             | 135 ns                                                   | 128 ns: 1.05x faster                                                    |
| fannkuch                   | 478 ms                                                   | 457 ms: 1.05x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                  |
| deltablue                  | 3.97 ms                                                  | 3.80 ms: 1.04x faster                                                   |
| async_generators           | 500 ms                                                   | 481 ms: 1.04x faster                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 8.59 ms: 1.02x faster                                                   |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| docutils                   | 2.96 sec                                                 | 3.03 sec: 1.02x slower                                                  |
| connected_components       | 547 ms                                                   | 570 ms: 1.04x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 207 us: 1.05x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 89.3 ms: 1.05x slower                                                   |
| shortest_path              | 565 ms                                                   | 596 ms: 1.05x slower                                                    |
| sympy_str                  | 265 ms                                                   | 279 ms: 1.05x slower                                                    |
| raytrace                   | 310 ms                                                   | 329 ms: 1.06x slower                                                    |
| comprehensions             | 20.8 us                                                  | 22.2 us: 1.06x slower                                                   |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.10 ms: 1.07x slower                                                   |
| coroutines                 | 29.4 ms                                                  | 31.5 ms: 1.07x slower                                                   |
| nbody                      | 118 ms                                                   | 127 ms: 1.08x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.81 ms: 1.12x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.81 ms: 1.15x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.11 sec: 1.15x slower                                                  |
| pprint_pformat             | 1.99 sec                                                 | 2.30 sec: 1.16x slower                                                  |
| many_optionals             | 626 us                                                   | 966 us: 1.54x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 47.1 ms: 2.32x slower                                                   |
| telco                      | 10.5 ms                                                  | 163 ms: 15.54x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (18): unpickle_pure_python, nqueens, scimark_lu, coverage, chaos, json, hexiom, sympy_integrate, asyncio_websockets, 2to3, sympy_sum, json_loads, pycparser, pidigits, genshi_xml, django_template, sympy_expand, pickle_pure_python
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250822-3.15.0a0-f278afc-JIT/bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.022x faster

# HPT report

- Reliability score: 99.73% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x