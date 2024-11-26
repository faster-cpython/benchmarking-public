# Results vs. 3.13.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: linux-aarch64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.097x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 385 ms: 1.27x slower                                                     |
| docutils       | 2.89 sec                                                 | 3.64 sec: 1.26x slower                                                   |
| html5lib       | 66.4 ms                                                  | 72.4 ms: 1.09x slower                                                    |
| sphinx         | 1.17 sec                                                 | 1.47 sec: 1.26x slower                                                   |
| tornado_http   | 128 ms                                                   | 148 ms: 1.16x slower                                                     |
| Geometric mean | (ref)                                                    | 1.20x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 543 ms: 1.19x faster                                                     |
| async_tree_memoization     | 651 ms                                                   | 607 ms: 1.07x faster                                                     |
| async_tree_none_tg         | 470 ms                                                   | 449 ms: 1.05x faster                                                     |
| async_tree_none            | 497 ms                                                   | 475 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 748 ms: 1.03x faster                                                     |
| async_generators           | 489 ms                                                   | 511 ms: 1.04x slower                                                     |
| async_tree_io              | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.11x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 96.8 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                    |
| regex_compile  | 127 ms                                                   | 177 ms: 1.39x slower                                                     |
| Geometric mean | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 187 ms: 1.05x faster                                                     |
| xml_etree_iterparse  | 149 ms                                                   | 153 ms: 1.03x slower                                                     |
| tomli_loads          | 2.54 sec                                                 | 2.62 sec: 1.03x slower                                                   |
| json_dumps           | 13.6 ms                                                  | 14.4 ms: 1.06x slower                                                    |
| unpickle_pure_python | 251 us                                                   | 272 us: 1.09x slower                                                     |
| pickle_pure_python   | 357 us                                                   | 390 us: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (3): xml_etree_generate, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 14.5 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.2 ms: 1.02x faster                                                    |
| genshi_text     | 27.7 ms                                                  | 34.9 ms: 1.26x slower                                                    |
| django_template | 41.6 ms                                                  | 53.3 ms: 1.28x slower                                                    |
| genshi_xml      | 60.3 ms                                                  | 85.7 ms: 1.42x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.23x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 50.4 us                                                  | 39.0 us: 1.29x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 543 ms: 1.19x faster                                                     |
| deepcopy                   | 447 us                                                   | 382 us: 1.17x faster                                                     |
| async_tree_memoization     | 651 ms                                                   | 607 ms: 1.07x faster                                                     |
| python_startup             | 15.4 ms                                                  | 14.5 ms: 1.06x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 187 ms: 1.05x faster                                                     |
| async_tree_none_tg         | 470 ms                                                   | 449 ms: 1.05x faster                                                     |
| async_tree_none            | 497 ms                                                   | 475 ms: 1.05x faster                                                     |
| pathlib                    | 22.7 ms                                                  | 21.9 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 748 ms: 1.03x faster                                                     |
| regex_v8                   | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                    |
| scimark_sor                | 160 ms                                                   | 156 ms: 1.02x faster                                                     |
| mako                       | 13.4 ms                                                  | 13.2 ms: 1.02x faster                                                    |
| scimark_fft                | 447 ms                                                   | 453 ms: 1.01x slower                                                     |
| bpe_tokeniser              | 5.87 sec                                                 | 5.97 sec: 1.02x slower                                                   |
| coverage                   | 99.1 ms                                                  | 101 ms: 1.02x slower                                                     |
| xml_etree_iterparse        | 149 ms                                                   | 153 ms: 1.03x slower                                                     |
| tomli_loads                | 2.54 sec                                                 | 2.62 sec: 1.03x slower                                                   |
| float                      | 93.3 ms                                                  | 96.8 ms: 1.04x slower                                                    |
| async_generators           | 489 ms                                                   | 511 ms: 1.04x slower                                                     |
| mdp                        | 3.34 sec                                                 | 3.49 sec: 1.05x slower                                                   |
| logging_format             | 7.82 us                                                  | 8.22 us: 1.05x slower                                                    |
| json_dumps                 | 13.6 ms                                                  | 14.4 ms: 1.06x slower                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 89.1 ms: 1.07x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                                   |
| bench_thread_pool          | 1.27 ms                                                  | 1.36 ms: 1.07x slower                                                    |
| crypto_pyaes               | 83.7 ms                                                  | 90.0 ms: 1.08x slower                                                    |
| create_gc_cycles           | 3.35 ms                                                  | 3.61 ms: 1.08x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 151 ms: 1.08x slower                                                     |
| logging_simple             | 7.07 us                                                  | 7.68 us: 1.09x slower                                                    |
| meteor_contest             | 114 ms                                                   | 123 ms: 1.09x slower                                                     |
| unpickle_pure_python       | 251 us                                                   | 272 us: 1.09x slower                                                     |
| spectral_norm              | 143 ms                                                   | 155 ms: 1.09x slower                                                     |
| html5lib                   | 66.4 ms                                                  | 72.4 ms: 1.09x slower                                                    |
| pickle_pure_python         | 357 us                                                   | 390 us: 1.09x slower                                                     |
| gc_traversal               | 5.77 ms                                                  | 6.34 ms: 1.10x slower                                                    |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 7.18 ms: 1.10x slower                                                    |
| typing_runtime_protocols   | 193 us                                                   | 214 us: 1.11x slower                                                     |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.11x slower                                                   |
| fannkuch                   | 461 ms                                                   | 519 ms: 1.13x slower                                                     |
| richards_super             | 60.1 ms                                                  | 68.5 ms: 1.14x slower                                                    |
| pyflate                    | 556 ms                                                   | 638 ms: 1.15x slower                                                     |
| tornado_http               | 128 ms                                                   | 148 ms: 1.16x slower                                                     |
| go                         | 160 ms                                                   | 185 ms: 1.16x slower                                                     |
| raytrace                   | 300 ms                                                   | 351 ms: 1.17x slower                                                     |
| richards                   | 53.6 ms                                                  | 63.2 ms: 1.18x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 4.53 ms: 1.19x slower                                                    |
| pycparser                  | 1.27 sec                                                 | 1.53 sec: 1.20x slower                                                   |
| comprehensions             | 20.4 us                                                  | 25.0 us: 1.23x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.70 ms: 1.24x slower                                                    |
| sqlglot_normalize          | 127 ms                                                   | 157 ms: 1.24x slower                                                     |
| chaos                      | 68.0 ms                                                  | 85.0 ms: 1.25x slower                                                    |
| docutils                   | 2.89 sec                                                 | 3.64 sec: 1.26x slower                                                   |
| sphinx                     | 1.17 sec                                                 | 1.47 sec: 1.26x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 34.9 ms: 1.26x slower                                                    |
| nqueens                    | 100 ms                                                   | 127 ms: 1.26x slower                                                     |
| sqlglot_transpile          | 1.73 ms                                                  | 2.19 ms: 1.26x slower                                                    |
| 2to3                       | 304 ms                                                   | 385 ms: 1.27x slower                                                     |
| django_template            | 41.6 ms                                                  | 53.3 ms: 1.28x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.20 sec: 1.30x slower                                                   |
| sympy_expand               | 457 ms                                                   | 595 ms: 1.30x slower                                                     |
| pprint_pformat             | 1.90 sec                                                 | 2.51 sec: 1.32x slower                                                   |
| sqlglot_optimize           | 62.2 ms                                                  | 83.1 ms: 1.34x slower                                                    |
| sympy_str                  | 264 ms                                                   | 361 ms: 1.37x slower                                                     |
| pylint                     | 342 ms                                                   | 472 ms: 1.38x slower                                                     |
| regex_compile              | 127 ms                                                   | 177 ms: 1.39x slower                                                     |
| genshi_xml                 | 60.3 ms                                                  | 85.7 ms: 1.42x slower                                                    |
| sympy_integrate            | 20.8 ms                                                  | 30.2 ms: 1.45x slower                                                    |
| hexiom                     | 7.11 ms                                                  | 10.4 ms: 1.46x slower                                                    |
| sympy_sum                  | 144 ms                                                   | 219 ms: 1.53x slower                                                     |
| generators                 | 37.6 ms                                                  | 58.8 ms: 1.56x slower                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 2.71 sec: 353.15x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.18x slower                                                             |

Benchmark hidden because not significant (16): telco, thrift, nbody, xml_etree_generate, python_startup_no_site, async_tree_cpu_io_mixed, deepcopy_reduce, regex_dna, logging_silent, json_loads, xml_etree_process, asyncio_websockets, pidigits, json, regex_effbot, coroutines
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: dulwich_log

- Geometric mean (including insignificant results): 1.097x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.08x