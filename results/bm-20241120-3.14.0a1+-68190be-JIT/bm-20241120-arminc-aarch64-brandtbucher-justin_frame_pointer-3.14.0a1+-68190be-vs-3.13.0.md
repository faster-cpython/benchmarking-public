# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-aarch64
- commit hash: 68190be
- commit date: 2024-11-20
- overall geometric mean: 1.090x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 362 ms: 1.19x slower                                                           |
| docutils       | 2.89 sec                                                 | 3.54 sec: 1.22x slower                                                         |
| html5lib       | 66.4 ms                                                  | 80.6 ms: 1.21x slower                                                          |
| sphinx         | 1.17 sec                                                 | 1.45 sec: 1.24x slower                                                         |
| Geometric mean | (ref)                                                    | 1.22x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 541 ms: 1.20x faster                                                           |
| async_tree_io_tg           | 1.13 sec                                                 | 975 ms: 1.16x faster                                                           |
| async_tree_memoization     | 651 ms                                                   | 574 ms: 1.13x faster                                                           |
| async_tree_io              | 1.11 sec                                                 | 1.01 sec: 1.09x faster                                                         |
| async_tree_none            | 497 ms                                                   | 462 ms: 1.08x faster                                                           |
| async_tree_none_tg         | 470 ms                                                   | 437 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 727 ms: 1.06x faster                                                           |
| asyncio_websockets         | 659 ms                                                   | 675 ms: 1.02x slower                                                           |
| async_generators           | 489 ms                                                   | 547 ms: 1.12x slower                                                           |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 234 ms                                                   | 244 ms: 1.04x slower                                                           |
| nbody          | 114 ms                                                   | 135 ms: 1.18x slower                                                           |
| float          | 93.3 ms                                                  | 111 ms: 1.19x slower                                                           |
| Geometric mean | (ref)                                                    | 1.14x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                  | 4.15 ms: 1.18x faster                                                          |
| regex_dna      | 253 ms                                                   | 265 ms: 1.05x slower                                                           |
| regex_compile  | 127 ms                                                   | 172 ms: 1.35x slower                                                           |
| Geometric mean | (ref)                                                    | 1.05x slower                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_generate   | 113 ms                                                   | 122 ms: 1.08x slower                                                           |
| xml_etree_process    | 80.5 ms                                                  | 86.8 ms: 1.08x slower                                                          |
| json_dumps           | 13.6 ms                                                  | 14.8 ms: 1.09x slower                                                          |
| tomli_loads          | 2.54 sec                                                 | 2.86 sec: 1.13x slower                                                         |
| pickle_pure_python   | 357 us                                                   | 412 us: 1.15x slower                                                           |
| xml_etree_iterparse  | 149 ms                                                   | 175 ms: 1.17x slower                                                           |
| unpickle_pure_python | 251 us                                                   | 294 us: 1.17x slower                                                           |
| Geometric mean       | (ref)                                                    | 1.10x slower                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 15.8 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                    | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 14.0 ms: 1.05x slower                                                          |
| django_template | 41.6 ms                                                  | 50.1 ms: 1.20x slower                                                          |
| genshi_text     | 27.7 ms                                                  | 34.8 ms: 1.26x slower                                                          |
| genshi_xml      | 60.3 ms                                                  | 84.0 ms: 1.39x slower                                                          |
| Geometric mean  | (ref)                                                    | 1.22x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------------:|
| gc_traversal               | 5.77 ms                                                  | 2.88 ms: 2.01x faster                                                          |
| create_gc_cycles           | 3.35 ms                                                  | 2.40 ms: 1.39x faster                                                          |
| async_tree_memoization_tg  | 649 ms                                                   | 541 ms: 1.20x faster                                                           |
| regex_effbot               | 4.89 ms                                                  | 4.15 ms: 1.18x faster                                                          |
| async_tree_io_tg           | 1.13 sec                                                 | 975 ms: 1.16x faster                                                           |
| deepcopy_memo              | 50.4 us                                                  | 44.3 us: 1.14x faster                                                          |
| async_tree_memoization     | 651 ms                                                   | 574 ms: 1.13x faster                                                           |
| async_tree_io              | 1.11 sec                                                 | 1.01 sec: 1.09x faster                                                         |
| deepcopy                   | 447 us                                                   | 413 us: 1.08x faster                                                           |
| async_tree_none            | 497 ms                                                   | 462 ms: 1.08x faster                                                           |
| async_tree_none_tg         | 470 ms                                                   | 437 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 727 ms: 1.06x faster                                                           |
| pathlib                    | 22.7 ms                                                  | 22.1 ms: 1.03x faster                                                          |
| k_core                     | 2.96 sec                                                 | 3.02 sec: 1.02x slower                                                         |
| telco                      | 9.74 ms                                                  | 9.97 ms: 1.02x slower                                                          |
| python_startup             | 15.4 ms                                                  | 15.8 ms: 1.02x slower                                                          |
| asyncio_websockets         | 659 ms                                                   | 675 ms: 1.02x slower                                                           |
| sqlalchemy_declarative     | 150 ms                                                   | 156 ms: 1.04x slower                                                           |
| pidigits                   | 234 ms                                                   | 244 ms: 1.04x slower                                                           |
| scimark_fft                | 447 ms                                                   | 467 ms: 1.05x slower                                                           |
| regex_dna                  | 253 ms                                                   | 265 ms: 1.05x slower                                                           |
| mako                       | 13.4 ms                                                  | 14.0 ms: 1.05x slower                                                          |
| thrift                     | 968 us                                                   | 1.02 ms: 1.06x slower                                                          |
| deepcopy_reduce            | 4.07 us                                                  | 4.33 us: 1.06x slower                                                          |
| xml_etree_generate         | 113 ms                                                   | 122 ms: 1.08x slower                                                           |
| connected_components       | 533 ms                                                   | 573 ms: 1.08x slower                                                           |
| shortest_path              | 565 ms                                                   | 609 ms: 1.08x slower                                                           |
| xml_etree_process          | 80.5 ms                                                  | 86.8 ms: 1.08x slower                                                          |
| json_dumps                 | 13.6 ms                                                  | 14.8 ms: 1.09x slower                                                          |
| pylint                     | 342 ms                                                   | 375 ms: 1.10x slower                                                           |
| logging_format             | 7.82 us                                                  | 8.62 us: 1.10x slower                                                          |
| bpe_tokeniser              | 5.87 sec                                                 | 6.51 sec: 1.11x slower                                                         |
| bench_thread_pool          | 1.27 ms                                                  | 1.42 ms: 1.11x slower                                                          |
| async_generators           | 489 ms                                                   | 547 ms: 1.12x slower                                                           |
| logging_simple             | 7.07 us                                                  | 7.93 us: 1.12x slower                                                          |
| mdp                        | 3.34 sec                                                 | 3.75 sec: 1.12x slower                                                         |
| tomli_loads                | 2.54 sec                                                 | 2.86 sec: 1.13x slower                                                         |
| crypto_pyaes               | 83.7 ms                                                  | 94.4 ms: 1.13x slower                                                          |
| scimark_sor                | 160 ms                                                   | 183 ms: 1.14x slower                                                           |
| meteor_contest             | 114 ms                                                   | 130 ms: 1.15x slower                                                           |
| pickle_pure_python         | 357 us                                                   | 412 us: 1.15x slower                                                           |
| spectral_norm              | 143 ms                                                   | 166 ms: 1.17x slower                                                           |
| xml_etree_iterparse        | 149 ms                                                   | 175 ms: 1.17x slower                                                           |
| unpickle_pure_python       | 251 us                                                   | 294 us: 1.17x slower                                                           |
| scimark_monte_carlo        | 83.6 ms                                                  | 98.2 ms: 1.17x slower                                                          |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 7.70 ms: 1.18x slower                                                          |
| nbody                      | 114 ms                                                   | 135 ms: 1.18x slower                                                           |
| float                      | 93.3 ms                                                  | 111 ms: 1.19x slower                                                           |
| sqlalchemy_imperative      | 15.1 ms                                                  | 18.0 ms: 1.19x slower                                                          |
| scimark_lu                 | 139 ms                                                   | 166 ms: 1.19x slower                                                           |
| 2to3                       | 304 ms                                                   | 362 ms: 1.19x slower                                                           |
| fannkuch                   | 461 ms                                                   | 551 ms: 1.20x slower                                                           |
| richards_super             | 60.1 ms                                                  | 72.1 ms: 1.20x slower                                                          |
| django_template            | 41.6 ms                                                  | 50.1 ms: 1.20x slower                                                          |
| sqlglot_optimize           | 62.2 ms                                                  | 75.3 ms: 1.21x slower                                                          |
| pycparser                  | 1.27 sec                                                 | 1.55 sec: 1.21x slower                                                         |
| html5lib                   | 66.4 ms                                                  | 80.6 ms: 1.21x slower                                                          |
| richards                   | 53.6 ms                                                  | 65.6 ms: 1.22x slower                                                          |
| docutils                   | 2.89 sec                                                 | 3.54 sec: 1.22x slower                                                         |
| sympy_integrate            | 20.8 ms                                                  | 25.6 ms: 1.23x slower                                                          |
| logging_silent             | 133 ns                                                   | 164 ns: 1.23x slower                                                           |
| typing_runtime_protocols   | 193 us                                                   | 239 us: 1.24x slower                                                           |
| pyflate                    | 556 ms                                                   | 689 ms: 1.24x slower                                                           |
| sphinx                     | 1.17 sec                                                 | 1.45 sec: 1.24x slower                                                         |
| sqlglot_normalize          | 127 ms                                                   | 158 ms: 1.25x slower                                                           |
| sympy_sum                  | 144 ms                                                   | 179 ms: 1.25x slower                                                           |
| sqlglot_transpile          | 1.73 ms                                                  | 2.17 ms: 1.25x slower                                                          |
| genshi_text                | 27.7 ms                                                  | 34.8 ms: 1.26x slower                                                          |
| go                         | 160 ms                                                   | 203 ms: 1.27x slower                                                           |
| sympy_str                  | 264 ms                                                   | 345 ms: 1.31x slower                                                           |
| sqlglot_parse              | 1.38 ms                                                  | 1.81 ms: 1.32x slower                                                          |
| sympy_expand               | 457 ms                                                   | 608 ms: 1.33x slower                                                           |
| raytrace                   | 300 ms                                                   | 405 ms: 1.35x slower                                                           |
| regex_compile              | 127 ms                                                   | 172 ms: 1.35x slower                                                           |
| comprehensions             | 20.4 us                                                  | 27.8 us: 1.36x slower                                                          |
| pprint_pformat             | 1.90 sec                                                 | 2.60 sec: 1.37x slower                                                         |
| nqueens                    | 100 ms                                                   | 137 ms: 1.37x slower                                                           |
| chaos                      | 68.0 ms                                                  | 93.9 ms: 1.38x slower                                                          |
| pprint_safe_repr           | 926 ms                                                   | 1.29 sec: 1.39x slower                                                         |
| genshi_xml                 | 60.3 ms                                                  | 84.0 ms: 1.39x slower                                                          |
| deltablue                  | 3.82 ms                                                  | 5.47 ms: 1.43x slower                                                          |
| generators                 | 37.6 ms                                                  | 58.2 ms: 1.55x slower                                                          |
| hexiom                     | 7.11 ms                                                  | 11.6 ms: 1.63x slower                                                          |
| bench_mp_pool              | 7.68 ms                                                  | 1.60 sec: 208.26x slower                                                       |
| Geometric mean             | (ref)                                                    | 1.18x slower                                                                   |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, xml_etree_parse, python_startup_no_site, json, regex_v8, json_loads, coverage, coroutines
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (5) of results/bm-20241120-3.14.0a1+-68190be-JIT/bm-20241120-arminc-aarch64-brandtbucher-justin_frame_pointer-3.14.0a1+-68190be.json: djangocms, dulwich_log, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.090x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.03x