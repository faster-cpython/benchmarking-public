# Results vs. 3.13.0

- fork: python
- ref: c695e37a3f95c225ee08
- machine: linux-aarch64
- commit hash: c695e37
- commit date: 2024-11-13
- overall geometric mean: 1.099x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 398 ms: 1.31x slower                                                     |
| docutils       | 2.89 sec                                                 | 3.79 sec: 1.31x slower                                                   |
| html5lib       | 66.4 ms                                                  | 73.7 ms: 1.11x slower                                                    |
| sphinx         | 1.17 sec                                                 | 1.51 sec: 1.29x slower                                                   |
| Geometric mean | (ref)                                                    | 1.25x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 557 ms: 1.16x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 618 ms: 1.05x faster                                                     |
| async_tree_none           | 497 ms                                                   | 477 ms: 1.04x faster                                                     |
| async_tree_cpu_io_mixed   | 766 ms                                                   | 790 ms: 1.03x slower                                                     |
| asyncio_websockets        | 659 ms                                                   | 683 ms: 1.04x slower                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                                   |
| async_generators          | 489 ms                                                   | 529 ms: 1.08x slower                                                     |
| async_tree_io_tg          | 1.13 sec                                                 | 1.28 sec: 1.13x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed_tg, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 33.6 ms: 1.05x slower                                                    |
| regex_effbot   | 4.89 ms                                                  | 5.20 ms: 1.06x slower                                                    |
| regex_compile  | 127 ms                                                   | 180 ms: 1.42x slower                                                     |
| Geometric mean | (ref)                                                    | 1.13x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.54 sec                                                 | 2.63 sec: 1.04x slower                                                   |
| unpickle_pure_python | 251 us                                                   | 270 us: 1.08x slower                                                     |
| json_dumps           | 13.6 ms                                                  | 14.7 ms: 1.08x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 399 us: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (5): xml_etree_parse, xml_etree_generate, xml_etree_iterparse, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.73 ms                                                  | 9.03 ms: 1.03x slower                                                    |
| python_startup         | 15.4 ms                                                  | 16.1 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.04x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.7 ms                                                  | 33.6 ms: 1.21x slower                                                    |
| django_template | 41.6 ms                                                  | 52.5 ms: 1.26x slower                                                    |
| genshi_xml      | 60.3 ms                                                  | 84.6 ms: 1.40x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.21x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo             | 50.4 us                                                  | 40.8 us: 1.24x faster                                                    |
| async_tree_memoization_tg | 649 ms                                                   | 557 ms: 1.16x faster                                                     |
| deepcopy                  | 447 us                                                   | 399 us: 1.12x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 618 ms: 1.05x faster                                                     |
| async_tree_none           | 497 ms                                                   | 477 ms: 1.04x faster                                                     |
| async_tree_cpu_io_mixed   | 766 ms                                                   | 790 ms: 1.03x slower                                                     |
| shortest_path             | 565 ms                                                   | 584 ms: 1.03x slower                                                     |
| python_startup_no_site    | 8.73 ms                                                  | 9.03 ms: 1.03x slower                                                    |
| tomli_loads               | 2.54 sec                                                 | 2.63 sec: 1.04x slower                                                   |
| asyncio_websockets        | 659 ms                                                   | 683 ms: 1.04x slower                                                     |
| python_startup            | 15.4 ms                                                  | 16.1 ms: 1.05x slower                                                    |
| thrift                    | 968 us                                                   | 1.02 ms: 1.05x slower                                                    |
| spectral_norm             | 143 ms                                                   | 150 ms: 1.05x slower                                                     |
| regex_v8                  | 31.8 ms                                                  | 33.6 ms: 1.05x slower                                                    |
| regex_effbot              | 4.89 ms                                                  | 5.20 ms: 1.06x slower                                                    |
| connected_components      | 533 ms                                                   | 567 ms: 1.07x slower                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                                   |
| logging_format            | 7.82 us                                                  | 8.42 us: 1.08x slower                                                    |
| unpickle_pure_python      | 251 us                                                   | 270 us: 1.08x slower                                                     |
| json_dumps                | 13.6 ms                                                  | 14.7 ms: 1.08x slower                                                    |
| async_generators          | 489 ms                                                   | 529 ms: 1.08x slower                                                     |
| crypto_pyaes              | 83.7 ms                                                  | 90.8 ms: 1.08x slower                                                    |
| meteor_contest            | 114 ms                                                   | 124 ms: 1.09x slower                                                     |
| fannkuch                  | 461 ms                                                   | 502 ms: 1.09x slower                                                     |
| logging_simple            | 7.07 us                                                  | 7.73 us: 1.09x slower                                                    |
| mdp                       | 3.34 sec                                                 | 3.65 sec: 1.09x slower                                                   |
| pyflate                   | 556 ms                                                   | 609 ms: 1.10x slower                                                     |
| scimark_monte_carlo       | 83.6 ms                                                  | 91.6 ms: 1.10x slower                                                    |
| bench_thread_pool         | 1.27 ms                                                  | 1.41 ms: 1.10x slower                                                    |
| html5lib                  | 66.4 ms                                                  | 73.7 ms: 1.11x slower                                                    |
| gc_traversal              | 5.77 ms                                                  | 6.43 ms: 1.11x slower                                                    |
| pickle_pure_python        | 357 us                                                   | 399 us: 1.12x slower                                                     |
| scimark_sparse_mat_mult   | 6.51 ms                                                  | 7.30 ms: 1.12x slower                                                    |
| deltablue                 | 3.82 ms                                                  | 4.30 ms: 1.13x slower                                                    |
| scimark_lu                | 139 ms                                                   | 158 ms: 1.13x slower                                                     |
| async_tree_io_tg          | 1.13 sec                                                 | 1.28 sec: 1.13x slower                                                   |
| create_gc_cycles          | 3.35 ms                                                  | 3.83 ms: 1.14x slower                                                    |
| go                        | 160 ms                                                   | 185 ms: 1.16x slower                                                     |
| typing_runtime_protocols  | 193 us                                                   | 225 us: 1.17x slower                                                     |
| richards                  | 53.6 ms                                                  | 64.4 ms: 1.20x slower                                                    |
| genshi_text               | 27.7 ms                                                  | 33.6 ms: 1.21x slower                                                    |
| pycparser                 | 1.27 sec                                                 | 1.55 sec: 1.21x slower                                                   |
| nqueens                   | 100 ms                                                   | 123 ms: 1.23x slower                                                     |
| raytrace                  | 300 ms                                                   | 368 ms: 1.23x slower                                                     |
| richards_super            | 60.1 ms                                                  | 73.8 ms: 1.23x slower                                                    |
| comprehensions            | 20.4 us                                                  | 25.2 us: 1.24x slower                                                    |
| sqlglot_transpile         | 1.73 ms                                                  | 2.14 ms: 1.24x slower                                                    |
| sqlglot_parse             | 1.38 ms                                                  | 1.71 ms: 1.24x slower                                                    |
| django_template           | 41.6 ms                                                  | 52.5 ms: 1.26x slower                                                    |
| sqlalchemy_declarative    | 150 ms                                                   | 193 ms: 1.28x slower                                                     |
| chaos                     | 68.0 ms                                                  | 87.3 ms: 1.28x slower                                                    |
| sqlglot_normalize         | 127 ms                                                   | 164 ms: 1.29x slower                                                     |
| sphinx                    | 1.17 sec                                                 | 1.51 sec: 1.29x slower                                                   |
| sqlalchemy_imperative     | 15.1 ms                                                  | 19.7 ms: 1.30x slower                                                    |
| sympy_expand              | 457 ms                                                   | 596 ms: 1.31x slower                                                     |
| docutils                  | 2.89 sec                                                 | 3.79 sec: 1.31x slower                                                   |
| generators                | 37.6 ms                                                  | 49.3 ms: 1.31x slower                                                    |
| 2to3                      | 304 ms                                                   | 398 ms: 1.31x slower                                                     |
| sympy_str                 | 264 ms                                                   | 356 ms: 1.35x slower                                                     |
| pprint_safe_repr          | 926 ms                                                   | 1.26 sec: 1.36x slower                                                   |
| sqlglot_optimize          | 62.2 ms                                                  | 84.7 ms: 1.36x slower                                                    |
| genshi_xml                | 60.3 ms                                                  | 84.6 ms: 1.40x slower                                                    |
| pprint_pformat            | 1.90 sec                                                 | 2.66 sec: 1.40x slower                                                   |
| sympy_integrate           | 20.8 ms                                                  | 29.4 ms: 1.41x slower                                                    |
| regex_compile             | 127 ms                                                   | 180 ms: 1.42x slower                                                     |
| hexiom                    | 7.11 ms                                                  | 10.1 ms: 1.43x slower                                                    |
| pylint                    | 342 ms                                                   | 502 ms: 1.47x slower                                                     |
| sympy_sum                 | 144 ms                                                   | 212 ms: 1.48x slower                                                     |
| k_core                    | 2.96 sec                                                 | 4.59 sec: 1.55x slower                                                   |
| bench_mp_pool             | 7.68 ms                                                  | 2.37 sec: 308.68x slower                                                 |
| Geometric mean            | (ref)                                                    | 1.20x slower                                                             |

Benchmark hidden because not significant (22): scimark_sor, async_tree_none_tg, async_tree_cpu_io_mixed_tg, json, xml_etree_parse, mako, bpe_tokeniser, xml_etree_generate, pathlib, xml_etree_iterparse, nbody, float, regex_dna, scimark_fft, logging_silent, telco, coverage, xml_etree_process, deepcopy_reduce, pidigits, coroutines, json_loads
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (2) of results/bm-20241113-3.14.0a1+-c695e37-JIT/bm-20241113-arminc-aarch64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37.json: dulwich_log, sqlite_synth

- Geometric mean (including insignificant results): 1.099x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.08x