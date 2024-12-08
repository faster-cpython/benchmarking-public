# Results vs. 3.13.0

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: linux-aarch64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.028x slower
- HPT reliability: 93.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.20 sec: 1.08x slower                                                   |
| html5lib       | 65.6 ms                                                  | 72.9 ms: 1.11x slower                                                    |
| sphinx         | 1.20 sec                                                 | 1.26 sec: 1.05x slower                                                   |
| Geometric mean | (ref)                                                    | 1.06x slower                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 535 ms: 1.24x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 956 ms: 1.22x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 547 ms: 1.21x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 946 ms: 1.20x faster                                                     |
| async_tree_none            | 504 ms                                                   | 423 ms: 1.19x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 423 ms: 1.15x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 714 ms: 1.12x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 719 ms: 1.10x faster                                                     |
| async_generators           | 500 ms                                                   | 528 ms: 1.05x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.12x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.10 ms: 1.24x faster                                                    |
| regex_compile  | 134 ms                                                   | 142 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 179 ms: 1.13x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.10x faster                                                     |
| xml_etree_generate  | 118 ms                                                   | 111 ms: 1.07x faster                                                     |
| pickle_pure_python  | 374 us                                                   | 408 us: 1.09x slower                                                     |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (5): xml_etree_process, tomli_loads, json_loads, json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.18 ms: 1.04x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 32.7 ms: 1.15x slower                                                    |
| django_template | 39.4 ms                                                  | 48.4 ms: 1.23x slower                                                    |
| genshi_xml      | 61.6 ms                                                  | 82.0 ms: 1.33x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.17x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 53.0 us                                                  | 40.1 us: 1.32x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 4.10 ms: 1.24x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 535 ms: 1.24x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 956 ms: 1.22x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 547 ms: 1.21x faster                                                     |
| deepcopy                   | 479 us                                                   | 396 us: 1.21x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 946 ms: 1.20x faster                                                     |
| async_tree_none            | 504 ms                                                   | 423 ms: 1.19x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 423 ms: 1.15x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 714 ms: 1.12x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.10x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 22.1 ms: 1.10x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.50 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 719 ms: 1.10x faster                                                     |
| xml_etree_generate         | 118 ms                                                   | 111 ms: 1.07x faster                                                     |
| k_core                     | 2.99 sec                                                 | 2.83 sec: 1.06x faster                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.23 ms: 1.05x faster                                                    |
| sqlalchemy_declarative     | 154 ms                                                   | 147 ms: 1.04x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.86 sec: 1.03x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.39 sec: 1.03x slower                                                   |
| richards                   | 54.5 ms                                                  | 56.7 ms: 1.04x slower                                                    |
| mdp                        | 3.45 sec                                                 | 3.59 sec: 1.04x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.18 ms: 1.04x slower                                                    |
| sphinx                     | 1.20 sec                                                 | 1.26 sec: 1.05x slower                                                   |
| pyflate                    | 582 ms                                                   | 610 ms: 1.05x slower                                                     |
| async_generators           | 500 ms                                                   | 528 ms: 1.05x slower                                                     |
| regex_compile              | 134 ms                                                   | 142 ms: 1.06x slower                                                     |
| sqlglot_optimize           | 65.2 ms                                                  | 69.7 ms: 1.07x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.13 ms: 1.07x slower                                                    |
| fannkuch                   | 478 ms                                                   | 512 ms: 1.07x slower                                                     |
| meteor_contest             | 117 ms                                                   | 125 ms: 1.07x slower                                                     |
| spectral_norm              | 143 ms                                                   | 154 ms: 1.08x slower                                                     |
| docutils                   | 2.96 sec                                                 | 3.20 sec: 1.08x slower                                                   |
| logging_silent             | 135 ns                                                   | 146 ns: 1.08x slower                                                     |
| sqlglot_transpile          | 1.84 ms                                                  | 2.00 ms: 1.09x slower                                                    |
| logging_simple             | 7.25 us                                                  | 7.90 us: 1.09x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 408 us: 1.09x slower                                                     |
| go                         | 164 ms                                                   | 180 ms: 1.09x slower                                                     |
| sympy_sum                  | 151 ms                                                   | 166 ms: 1.10x slower                                                     |
| logging_format             | 8.10 us                                                  | 8.89 us: 1.10x slower                                                    |
| sympy_expand               | 472 ms                                                   | 523 ms: 1.11x slower                                                     |
| sqlglot_normalize          | 131 ms                                                   | 145 ms: 1.11x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 94.2 ms: 1.11x slower                                                    |
| html5lib                   | 65.6 ms                                                  | 72.9 ms: 1.11x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 220 us: 1.12x slower                                                     |
| sympy_integrate            | 21.4 ms                                                  | 24.1 ms: 1.12x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.74 ms: 1.14x slower                                                    |
| sqlglot_parse              | 1.43 ms                                                  | 1.63 ms: 1.14x slower                                                    |
| genshi_text                | 28.6 ms                                                  | 32.7 ms: 1.15x slower                                                    |
| sympy_str                  | 265 ms                                                   | 304 ms: 1.15x slower                                                     |
| raytrace                   | 310 ms                                                   | 361 ms: 1.16x slower                                                     |
| chaos                      | 70.7 ms                                                  | 84.1 ms: 1.19x slower                                                    |
| comprehensions             | 20.8 us                                                  | 25.3 us: 1.21x slower                                                    |
| django_template            | 39.4 ms                                                  | 48.4 ms: 1.23x slower                                                    |
| generators                 | 40.3 ms                                                  | 50.5 ms: 1.25x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 9.35 ms: 1.27x slower                                                    |
| nqueens                    | 105 ms                                                   | 134 ms: 1.27x slower                                                     |
| pprint_safe_repr           | 962 ms                                                   | 1.27 sec: 1.32x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.63 sec: 1.33x slower                                                   |
| genshi_xml                 | 61.6 ms                                                  | 82.0 ms: 1.33x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 27.7 ms: 1.36x slower                                                    |
| many_optionals             | 626 us                                                   | 857 us: 1.37x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 1.46 sec: 180.46x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.09x slower                                                             |

Benchmark hidden because not significant (32): json, deepcopy_reduce, coverage, pylint, scimark_fft, xml_etree_process, richards_super, tomli_loads, json_loads, float, json_dumps, sqlite_synth, unpickle_pure_python, asyncio_websockets, scimark_sor, regex_v8, nbody, mako, regex_dna, djangocms, scimark_monte_carlo, pidigits, coroutines, shortest_path, connected_components, sqlalchemy_imperative, 2to3, bench_thread_pool, python_startup, thrift, deltablue, scimark_lu
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241207-3.14.0a2+-79b7cab-JIT/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: dulwich_log

- Geometric mean (including insignificant results): 1.028x slower

# HPT report

- Reliability score: 93.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x