# Results vs. 3.13.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-aarch64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.064x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 334 ms: 1.10x slower                                                     |
| docutils       | 2.89 sec                                                 | 3.39 sec: 1.17x slower                                                   |
| html5lib       | 66.4 ms                                                  | 70.9 ms: 1.07x slower                                                    |
| sphinx         | 1.17 sec                                                 | 1.34 sec: 1.15x slower                                                   |
| Geometric mean | (ref)                                                    | 1.12x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 579 ms: 1.12x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 598 ms: 1.09x faster                                                     |
| async_tree_none           | 497 ms                                                   | 471 ms: 1.05x faster                                                     |
| asyncio_websockets        | 659 ms                                                   | 673 ms: 1.02x slower                                                     |
| async_tree_none_tg        | 470 ms                                                   | 490 ms: 1.04x slower                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.21 sec: 1.09x slower                                                   |
| async_generators          | 489 ms                                                   | 538 ms: 1.10x slower                                                     |
| async_tree_io_tg          | 1.13 sec                                                 | 1.28 sec: 1.13x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (3): coroutines, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 97.9 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                  | 4.13 ms: 1.18x faster                                                    |
| regex_dna      | 253 ms                                                   | 246 ms: 1.03x faster                                                     |
| regex_compile  | 127 ms                                                   | 151 ms: 1.19x slower                                                     |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|--------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads        | 2.54 sec                                                 | 2.60 sec: 1.03x slower                                                   |
| json_dumps         | 13.6 ms                                                  | 14.6 ms: 1.07x slower                                                    |
| pickle_pure_python | 357 us                                                   | 410 us: 1.15x slower                                                     |
| Geometric mean     | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (6): xml_etree_parse, xml_etree_generate, json_loads, xml_etree_process, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.73 ms                                                  | 9.08 ms: 1.04x slower                                                    |
| python_startup         | 15.4 ms                                                  | 16.3 ms: 1.06x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.05x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 41.6 ms                                                  | 47.5 ms: 1.14x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 32.3 ms: 1.17x slower                                                    |
| genshi_xml      | 60.3 ms                                                  | 79.5 ms: 1.32x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.16x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot              | 4.89 ms                                                  | 4.13 ms: 1.18x faster                                                    |
| deepcopy_memo             | 50.4 us                                                  | 42.9 us: 1.17x faster                                                    |
| deepcopy                  | 447 us                                                   | 389 us: 1.15x faster                                                     |
| async_tree_memoization_tg | 649 ms                                                   | 579 ms: 1.12x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 598 ms: 1.09x faster                                                     |
| async_tree_none           | 497 ms                                                   | 471 ms: 1.05x faster                                                     |
| regex_dna                 | 253 ms                                                   | 246 ms: 1.03x faster                                                     |
| json                      | 5.73 ms                                                  | 5.60 ms: 1.02x faster                                                    |
| bpe_tokeniser             | 5.87 sec                                                 | 5.94 sec: 1.01x slower                                                   |
| asyncio_websockets        | 659 ms                                                   | 673 ms: 1.02x slower                                                     |
| tomli_loads               | 2.54 sec                                                 | 2.60 sec: 1.03x slower                                                   |
| richards                  | 53.6 ms                                                  | 55.1 ms: 1.03x slower                                                    |
| shortest_path             | 565 ms                                                   | 585 ms: 1.03x slower                                                     |
| python_startup_no_site    | 8.73 ms                                                  | 9.08 ms: 1.04x slower                                                    |
| logging_format            | 7.82 us                                                  | 8.14 us: 1.04x slower                                                    |
| async_tree_none_tg        | 470 ms                                                   | 490 ms: 1.04x slower                                                     |
| logging_simple            | 7.07 us                                                  | 7.41 us: 1.05x slower                                                    |
| float                     | 93.3 ms                                                  | 97.9 ms: 1.05x slower                                                    |
| connected_components      | 533 ms                                                   | 563 ms: 1.06x slower                                                     |
| python_startup            | 15.4 ms                                                  | 16.3 ms: 1.06x slower                                                    |
| html5lib                  | 66.4 ms                                                  | 70.9 ms: 1.07x slower                                                    |
| spectral_norm             | 143 ms                                                   | 152 ms: 1.07x slower                                                     |
| json_dumps                | 13.6 ms                                                  | 14.6 ms: 1.07x slower                                                    |
| bench_thread_pool         | 1.27 ms                                                  | 1.37 ms: 1.07x slower                                                    |
| mdp                       | 3.34 sec                                                 | 3.60 sec: 1.08x slower                                                   |
| sqlalchemy_declarative    | 150 ms                                                   | 163 ms: 1.08x slower                                                     |
| scimark_lu                | 139 ms                                                   | 151 ms: 1.08x slower                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.21 sec: 1.09x slower                                                   |
| meteor_contest            | 114 ms                                                   | 124 ms: 1.09x slower                                                     |
| crypto_pyaes              | 83.7 ms                                                  | 91.9 ms: 1.10x slower                                                    |
| async_generators          | 489 ms                                                   | 538 ms: 1.10x slower                                                     |
| 2to3                      | 304 ms                                                   | 334 ms: 1.10x slower                                                     |
| gc_traversal              | 5.77 ms                                                  | 6.36 ms: 1.10x slower                                                    |
| deltablue                 | 3.82 ms                                                  | 4.21 ms: 1.10x slower                                                    |
| fannkuch                  | 461 ms                                                   | 509 ms: 1.10x slower                                                     |
| scimark_monte_carlo       | 83.6 ms                                                  | 92.4 ms: 1.11x slower                                                    |
| scimark_sparse_mat_mult   | 6.51 ms                                                  | 7.28 ms: 1.12x slower                                                    |
| pyflate                   | 556 ms                                                   | 625 ms: 1.12x slower                                                     |
| create_gc_cycles          | 3.35 ms                                                  | 3.77 ms: 1.13x slower                                                    |
| sqlglot_normalize         | 127 ms                                                   | 143 ms: 1.13x slower                                                     |
| async_tree_io_tg          | 1.13 sec                                                 | 1.28 sec: 1.13x slower                                                   |
| sqlglot_optimize          | 62.2 ms                                                  | 70.8 ms: 1.14x slower                                                    |
| django_template           | 41.6 ms                                                  | 47.5 ms: 1.14x slower                                                    |
| sphinx                    | 1.17 sec                                                 | 1.34 sec: 1.15x slower                                                   |
| pickle_pure_python        | 357 us                                                   | 410 us: 1.15x slower                                                     |
| sympy_integrate           | 20.8 ms                                                  | 24.1 ms: 1.16x slower                                                    |
| genshi_text               | 27.7 ms                                                  | 32.3 ms: 1.17x slower                                                    |
| docutils                  | 2.89 sec                                                 | 3.39 sec: 1.17x slower                                                   |
| sympy_expand              | 457 ms                                                   | 536 ms: 1.17x slower                                                     |
| pycparser                 | 1.27 sec                                                 | 1.50 sec: 1.18x slower                                                   |
| sqlalchemy_imperative     | 15.1 ms                                                  | 17.8 ms: 1.18x slower                                                    |
| typing_runtime_protocols  | 193 us                                                   | 228 us: 1.18x slower                                                     |
| sqlglot_transpile         | 1.73 ms                                                  | 2.05 ms: 1.19x slower                                                    |
| regex_compile             | 127 ms                                                   | 151 ms: 1.19x slower                                                     |
| raytrace                  | 300 ms                                                   | 358 ms: 1.20x slower                                                     |
| sympy_str                 | 264 ms                                                   | 317 ms: 1.20x slower                                                     |
| sqlglot_parse             | 1.38 ms                                                  | 1.66 ms: 1.20x slower                                                    |
| go                        | 160 ms                                                   | 196 ms: 1.23x slower                                                     |
| chaos                     | 68.0 ms                                                  | 84.2 ms: 1.24x slower                                                    |
| k_core                    | 2.96 sec                                                 | 3.67 sec: 1.24x slower                                                   |
| comprehensions            | 20.4 us                                                  | 25.5 us: 1.25x slower                                                    |
| sympy_sum                 | 144 ms                                                   | 182 ms: 1.27x slower                                                     |
| nqueens                   | 100 ms                                                   | 129 ms: 1.29x slower                                                     |
| genshi_xml                | 60.3 ms                                                  | 79.5 ms: 1.32x slower                                                    |
| generators                | 37.6 ms                                                  | 49.8 ms: 1.32x slower                                                    |
| pprint_safe_repr          | 926 ms                                                   | 1.24 sec: 1.34x slower                                                   |
| pprint_pformat            | 1.90 sec                                                 | 2.62 sec: 1.38x slower                                                   |
| hexiom                    | 7.11 ms                                                  | 9.84 ms: 1.38x slower                                                    |
| bench_mp_pool             | 7.68 ms                                                  | 1.53 sec: 198.65x slower                                                 |
| Geometric mean            | (ref)                                                    | 1.15x slower                                                             |

Benchmark hidden because not significant (23): xml_etree_parse, regex_v8, telco, coverage, xml_etree_generate, pathlib, scimark_fft, coroutines, scimark_sor, pylint, deepcopy_reduce, richards_super, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, logging_silent, pidigits, nbody, json_loads, xml_etree_process, mako, thrift, unpickle_pure_python, xml_etree_iterparse
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (5) of results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: djangocms, dulwich_log, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.064x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.04x