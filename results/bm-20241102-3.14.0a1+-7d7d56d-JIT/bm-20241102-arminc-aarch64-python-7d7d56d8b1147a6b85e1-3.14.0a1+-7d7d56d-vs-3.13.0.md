# Results vs. 3.13.0

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: linux-aarch64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.099x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 405 ms: 1.33x slower                                                     |
| docutils       | 2.89 sec                                                 | 3.74 sec: 1.29x slower                                                   |
| html5lib       | 66.4 ms                                                  | 76.8 ms: 1.16x slower                                                    |
| sphinx         | 1.17 sec                                                 | 1.53 sec: 1.31x slower                                                   |
| tornado_http   | 128 ms                                                   | 150 ms: 1.18x slower                                                     |
| Geometric mean | (ref)                                                    | 1.25x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 552 ms: 1.18x faster                                                     |
| async_tree_none           | 497 ms                                                   | 475 ms: 1.05x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 630 ms: 1.03x faster                                                     |
| asyncio_websockets        | 659 ms                                                   | 677 ms: 1.03x slower                                                     |
| async_tree_io             | 1.11 sec                                                 | 1.19 sec: 1.08x slower                                                   |
| async_generators          | 489 ms                                                   | 537 ms: 1.10x slower                                                     |
| async_tree_io_tg          | 1.13 sec                                                 | 1.28 sec: 1.13x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 234 ms                                                   | 249 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 32.3 ms: 1.01x slower                                                    |
| regex_effbot   | 4.89 ms                                                  | 5.09 ms: 1.04x slower                                                    |
| regex_compile  | 127 ms                                                   | 177 ms: 1.39x slower                                                     |
| Geometric mean | (ref)                                                    | 1.10x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate   | 113 ms                                                   | 110 ms: 1.04x faster                                                     |
| tomli_loads          | 2.54 sec                                                 | 2.63 sec: 1.04x slower                                                   |
| json_dumps           | 13.6 ms                                                  | 14.5 ms: 1.07x slower                                                    |
| unpickle_pure_python | 251 us                                                   | 279 us: 1.11x slower                                                     |
| pickle_pure_python   | 357 us                                                   | 403 us: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.73 ms                                                  | 9.12 ms: 1.04x slower                                                    |
| python_startup         | 15.4 ms                                                  | 16.2 ms: 1.05x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.05x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 27.7 ms                                                  | 33.5 ms: 1.21x slower                                                    |
| django_template | 41.6 ms                                                  | 51.9 ms: 1.25x slower                                                    |
| genshi_xml      | 60.3 ms                                                  | 81.5 ms: 1.35x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.20x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo             | 50.4 us                                                  | 42.1 us: 1.20x faster                                                    |
| async_tree_memoization_tg | 649 ms                                                   | 552 ms: 1.18x faster                                                     |
| deepcopy                  | 447 us                                                   | 395 us: 1.13x faster                                                     |
| async_tree_none           | 497 ms                                                   | 475 ms: 1.05x faster                                                     |
| xml_etree_generate        | 113 ms                                                   | 110 ms: 1.04x faster                                                     |
| async_tree_memoization    | 651 ms                                                   | 630 ms: 1.03x faster                                                     |
| bpe_tokeniser             | 5.87 sec                                                 | 5.93 sec: 1.01x slower                                                   |
| regex_v8                  | 31.8 ms                                                  | 32.3 ms: 1.01x slower                                                    |
| shortest_path             | 565 ms                                                   | 576 ms: 1.02x slower                                                     |
| asyncio_websockets        | 659 ms                                                   | 677 ms: 1.03x slower                                                     |
| connected_components      | 533 ms                                                   | 549 ms: 1.03x slower                                                     |
| tomli_loads               | 2.54 sec                                                 | 2.63 sec: 1.04x slower                                                   |
| regex_effbot              | 4.89 ms                                                  | 5.09 ms: 1.04x slower                                                    |
| scimark_monte_carlo       | 83.6 ms                                                  | 87.2 ms: 1.04x slower                                                    |
| python_startup_no_site    | 8.73 ms                                                  | 9.12 ms: 1.04x slower                                                    |
| python_startup            | 15.4 ms                                                  | 16.2 ms: 1.05x slower                                                    |
| pidigits                  | 234 ms                                                   | 249 ms: 1.06x slower                                                     |
| json_dumps                | 13.6 ms                                                  | 14.5 ms: 1.07x slower                                                    |
| telco                     | 9.74 ms                                                  | 10.4 ms: 1.07x slower                                                    |
| mdp                       | 3.34 sec                                                 | 3.59 sec: 1.07x slower                                                   |
| async_tree_io             | 1.11 sec                                                 | 1.19 sec: 1.08x slower                                                   |
| spectral_norm             | 143 ms                                                   | 154 ms: 1.08x slower                                                     |
| logging_format            | 7.82 us                                                  | 8.45 us: 1.08x slower                                                    |
| bench_thread_pool         | 1.27 ms                                                  | 1.39 ms: 1.09x slower                                                    |
| scimark_lu                | 139 ms                                                   | 152 ms: 1.09x slower                                                     |
| fannkuch                  | 461 ms                                                   | 505 ms: 1.09x slower                                                     |
| async_generators          | 489 ms                                                   | 537 ms: 1.10x slower                                                     |
| unpickle_pure_python      | 251 us                                                   | 279 us: 1.11x slower                                                     |
| crypto_pyaes              | 83.7 ms                                                  | 93.6 ms: 1.12x slower                                                    |
| deltablue                 | 3.82 ms                                                  | 4.28 ms: 1.12x slower                                                    |
| meteor_contest            | 114 ms                                                   | 127 ms: 1.12x slower                                                     |
| logging_simple            | 7.07 us                                                  | 7.95 us: 1.12x slower                                                    |
| scimark_sparse_mat_mult   | 6.51 ms                                                  | 7.33 ms: 1.13x slower                                                    |
| pyflate                   | 556 ms                                                   | 627 ms: 1.13x slower                                                     |
| pickle_pure_python        | 357 us                                                   | 403 us: 1.13x slower                                                     |
| async_tree_io_tg          | 1.13 sec                                                 | 1.28 sec: 1.13x slower                                                   |
| create_gc_cycles          | 3.35 ms                                                  | 3.85 ms: 1.15x slower                                                    |
| html5lib                  | 66.4 ms                                                  | 76.8 ms: 1.16x slower                                                    |
| gc_traversal              | 5.77 ms                                                  | 6.72 ms: 1.16x slower                                                    |
| go                        | 160 ms                                                   | 187 ms: 1.17x slower                                                     |
| tornado_http              | 128 ms                                                   | 150 ms: 1.18x slower                                                     |
| typing_runtime_protocols  | 193 us                                                   | 228 us: 1.18x slower                                                     |
| pycparser                 | 1.27 sec                                                 | 1.51 sec: 1.18x slower                                                   |
| richards                  | 53.6 ms                                                  | 63.6 ms: 1.19x slower                                                    |
| richards_super            | 60.1 ms                                                  | 71.2 ms: 1.19x slower                                                    |
| genshi_text               | 27.7 ms                                                  | 33.5 ms: 1.21x slower                                                    |
| raytrace                  | 300 ms                                                   | 362 ms: 1.21x slower                                                     |
| sqlglot_parse             | 1.38 ms                                                  | 1.70 ms: 1.24x slower                                                    |
| chaos                     | 68.0 ms                                                  | 84.3 ms: 1.24x slower                                                    |
| sqlglot_normalize         | 127 ms                                                   | 157 ms: 1.24x slower                                                     |
| django_template           | 41.6 ms                                                  | 51.9 ms: 1.25x slower                                                    |
| comprehensions            | 20.4 us                                                  | 25.6 us: 1.25x slower                                                    |
| nqueens                   | 100 ms                                                   | 126 ms: 1.26x slower                                                     |
| sqlglot_transpile         | 1.73 ms                                                  | 2.22 ms: 1.28x slower                                                    |
| docutils                  | 2.89 sec                                                 | 3.74 sec: 1.29x slower                                                   |
| sqlalchemy_imperative     | 15.1 ms                                                  | 19.6 ms: 1.29x slower                                                    |
| generators                | 37.6 ms                                                  | 49.2 ms: 1.31x slower                                                    |
| sphinx                    | 1.17 sec                                                 | 1.53 sec: 1.31x slower                                                   |
| sqlalchemy_declarative    | 150 ms                                                   | 200 ms: 1.33x slower                                                     |
| 2to3                      | 304 ms                                                   | 405 ms: 1.33x slower                                                     |
| sympy_expand              | 457 ms                                                   | 613 ms: 1.34x slower                                                     |
| pprint_safe_repr          | 926 ms                                                   | 1.25 sec: 1.35x slower                                                   |
| genshi_xml                | 60.3 ms                                                  | 81.5 ms: 1.35x slower                                                    |
| sqlglot_optimize          | 62.2 ms                                                  | 85.3 ms: 1.37x slower                                                    |
| pprint_pformat            | 1.90 sec                                                 | 2.62 sec: 1.38x slower                                                   |
| regex_compile             | 127 ms                                                   | 177 ms: 1.39x slower                                                     |
| sympy_str                 | 264 ms                                                   | 368 ms: 1.39x slower                                                     |
| hexiom                    | 7.11 ms                                                  | 9.97 ms: 1.40x slower                                                    |
| pylint                    | 342 ms                                                   | 497 ms: 1.45x slower                                                     |
| sympy_integrate           | 20.8 ms                                                  | 31.6 ms: 1.52x slower                                                    |
| k_core                    | 2.96 sec                                                 | 4.55 sec: 1.54x slower                                                   |
| sympy_sum                 | 144 ms                                                   | 225 ms: 1.57x slower                                                     |
| bench_mp_pool             | 7.68 ms                                                  | 1.63 sec: 212.32x slower                                                 |
| Geometric mean            | (ref)                                                    | 1.19x slower                                                             |

Benchmark hidden because not significant (20): async_tree_none_tg, xml_etree_parse, json, regex_dna, xml_etree_iterparse, scimark_fft, nbody, deepcopy_reduce, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, coverage, xml_etree_process, mako, scimark_sor, float, pathlib, json_loads, logging_silent, thrift, coroutines
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2
Ignored benchmarks (2) of results/bm-20241102-3.14.0a1+-7d7d56d-JIT/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: dulwich_log, sqlite_synth

- Geometric mean (including insignificant results): 1.099x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.07x