# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-aarch64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.104x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 390 ms: 1.28x slower                                                        |
| docutils       | 2.89 sec                                                 | 3.62 sec: 1.25x slower                                                      |
| html5lib       | 66.4 ms                                                  | 71.6 ms: 1.08x slower                                                       |
| sphinx         | 1.17 sec                                                 | 1.45 sec: 1.24x slower                                                      |
| tornado_http   | 128 ms                                                   | 148 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                    | 1.20x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 544 ms: 1.19x faster                                                        |
| async_tree_memoization     | 651 ms                                                   | 608 ms: 1.07x faster                                                        |
| async_tree_none            | 497 ms                                                   | 469 ms: 1.06x faster                                                        |
| async_tree_none_tg         | 470 ms                                                   | 448 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 742 ms: 1.04x faster                                                        |
| asyncio_websockets         | 659 ms                                                   | 665 ms: 1.01x slower                                                        |
| async_generators           | 489 ms                                                   | 513 ms: 1.05x slower                                                        |
| async_tree_io              | 1.11 sec                                                 | 1.17 sec: 1.06x slower                                                      |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.11x slower                                                      |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 117 ms: 1.02x slower                                                        |
| float          | 93.3 ms                                                  | 95.9 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                    | 1.02x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.7 ms: 1.04x faster                                                       |
| regex_dna      | 253 ms                                                   | 251 ms: 1.01x faster                                                        |
| regex_compile  | 127 ms                                                   | 177 ms: 1.39x slower                                                        |
| Geometric mean | (ref)                                                    | 1.08x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 31.7 us                                                  | 31.8 us: 1.01x slower                                                       |
| json_dumps           | 13.6 ms                                                  | 14.2 ms: 1.05x slower                                                       |
| tomli_loads          | 2.54 sec                                                 | 2.71 sec: 1.07x slower                                                      |
| unpickle_pure_python | 251 us                                                   | 268 us: 1.07x slower                                                        |
| pickle_pure_python   | 357 us                                                   | 394 us: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                    | 1.03x slower                                                                |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_generate, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 14.6 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.3 ms: 1.00x faster                                                       |
| genshi_text     | 27.7 ms                                                  | 34.0 ms: 1.23x slower                                                       |
| django_template | 41.6 ms                                                  | 53.3 ms: 1.28x slower                                                       |
| genshi_xml      | 60.3 ms                                                  | 84.8 ms: 1.41x slower                                                       |
| Geometric mean  | (ref)                                                    | 1.22x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 50.4 us                                                  | 39.6 us: 1.27x faster                                                       |
| async_tree_memoization_tg  | 649 ms                                                   | 544 ms: 1.19x faster                                                        |
| deepcopy                   | 447 us                                                   | 386 us: 1.16x faster                                                        |
| async_tree_memoization     | 651 ms                                                   | 608 ms: 1.07x faster                                                        |
| async_tree_none            | 497 ms                                                   | 469 ms: 1.06x faster                                                        |
| python_startup             | 15.4 ms                                                  | 14.6 ms: 1.05x faster                                                       |
| pathlib                    | 22.7 ms                                                  | 21.6 ms: 1.05x faster                                                       |
| async_tree_none_tg         | 470 ms                                                   | 448 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 742 ms: 1.04x faster                                                        |
| regex_v8                   | 31.8 ms                                                  | 30.7 ms: 1.04x faster                                                       |
| telco                      | 9.74 ms                                                  | 9.55 ms: 1.02x faster                                                       |
| regex_dna                  | 253 ms                                                   | 251 ms: 1.01x faster                                                        |
| thrift                     | 968 us                                                   | 965 us: 1.00x faster                                                        |
| mako                       | 13.4 ms                                                  | 13.3 ms: 1.00x faster                                                       |
| json_loads                 | 31.7 us                                                  | 31.8 us: 1.01x slower                                                       |
| asyncio_websockets         | 659 ms                                                   | 665 ms: 1.01x slower                                                        |
| nbody                      | 114 ms                                                   | 117 ms: 1.02x slower                                                        |
| scimark_fft                | 447 ms                                                   | 459 ms: 1.03x slower                                                        |
| float                      | 93.3 ms                                                  | 95.9 ms: 1.03x slower                                                       |
| logging_format             | 7.82 us                                                  | 8.04 us: 1.03x slower                                                       |
| bpe_tokeniser              | 5.87 sec                                                 | 6.06 sec: 1.03x slower                                                      |
| json_dumps                 | 13.6 ms                                                  | 14.2 ms: 1.05x slower                                                       |
| async_generators           | 489 ms                                                   | 513 ms: 1.05x slower                                                        |
| logging_simple             | 7.07 us                                                  | 7.42 us: 1.05x slower                                                       |
| mdp                        | 3.34 sec                                                 | 3.53 sec: 1.06x slower                                                      |
| async_tree_io              | 1.11 sec                                                 | 1.17 sec: 1.06x slower                                                      |
| gc_traversal               | 5.77 ms                                                  | 6.12 ms: 1.06x slower                                                       |
| bench_thread_pool          | 1.27 ms                                                  | 1.36 ms: 1.07x slower                                                       |
| tomli_loads                | 2.54 sec                                                 | 2.71 sec: 1.07x slower                                                      |
| unpickle_pure_python       | 251 us                                                   | 268 us: 1.07x slower                                                        |
| html5lib                   | 66.4 ms                                                  | 71.6 ms: 1.08x slower                                                       |
| create_gc_cycles           | 3.35 ms                                                  | 3.64 ms: 1.09x slower                                                       |
| crypto_pyaes               | 83.7 ms                                                  | 91.2 ms: 1.09x slower                                                       |
| scimark_lu                 | 139 ms                                                   | 152 ms: 1.09x slower                                                        |
| meteor_contest             | 114 ms                                                   | 125 ms: 1.10x slower                                                        |
| pickle_pure_python         | 357 us                                                   | 394 us: 1.10x slower                                                        |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.11x slower                                                      |
| typing_runtime_protocols   | 193 us                                                   | 215 us: 1.11x slower                                                        |
| logging_silent             | 133 ns                                                   | 149 ns: 1.12x slower                                                        |
| spectral_norm              | 143 ms                                                   | 161 ms: 1.13x slower                                                        |
| scimark_monte_carlo        | 83.6 ms                                                  | 94.3 ms: 1.13x slower                                                       |
| fannkuch                   | 461 ms                                                   | 522 ms: 1.13x slower                                                        |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 7.42 ms: 1.14x slower                                                       |
| tornado_http               | 128 ms                                                   | 148 ms: 1.16x slower                                                        |
| pyflate                    | 556 ms                                                   | 652 ms: 1.17x slower                                                        |
| deltablue                  | 3.82 ms                                                  | 4.51 ms: 1.18x slower                                                       |
| go                         | 160 ms                                                   | 189 ms: 1.18x slower                                                        |
| pycparser                  | 1.27 sec                                                 | 1.51 sec: 1.19x slower                                                      |
| raytrace                   | 300 ms                                                   | 357 ms: 1.19x slower                                                        |
| sqlalchemy_imperative      | 15.1 ms                                                  | 18.4 ms: 1.21x slower                                                       |
| genshi_text                | 27.7 ms                                                  | 34.0 ms: 1.23x slower                                                       |
| sqlglot_normalize          | 127 ms                                                   | 157 ms: 1.24x slower                                                        |
| richards_super             | 60.1 ms                                                  | 74.4 ms: 1.24x slower                                                       |
| sqlalchemy_declarative     | 150 ms                                                   | 187 ms: 1.24x slower                                                        |
| sphinx                     | 1.17 sec                                                 | 1.45 sec: 1.24x slower                                                      |
| comprehensions             | 20.4 us                                                  | 25.5 us: 1.25x slower                                                       |
| docutils                   | 2.89 sec                                                 | 3.62 sec: 1.25x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                  | 1.75 ms: 1.27x slower                                                       |
| sqlglot_transpile          | 1.73 ms                                                  | 2.21 ms: 1.28x slower                                                       |
| django_template            | 41.6 ms                                                  | 53.3 ms: 1.28x slower                                                       |
| 2to3                       | 304 ms                                                   | 390 ms: 1.28x slower                                                        |
| nqueens                    | 100 ms                                                   | 130 ms: 1.30x slower                                                        |
| sympy_expand               | 457 ms                                                   | 597 ms: 1.31x slower                                                        |
| pylint                     | 342 ms                                                   | 450 ms: 1.32x slower                                                        |
| sqlglot_optimize           | 62.2 ms                                                  | 82.0 ms: 1.32x slower                                                       |
| chaos                      | 68.0 ms                                                  | 89.8 ms: 1.32x slower                                                       |
| richards                   | 53.6 ms                                                  | 71.9 ms: 1.34x slower                                                       |
| pprint_safe_repr           | 926 ms                                                   | 1.26 sec: 1.36x slower                                                      |
| sympy_str                  | 264 ms                                                   | 359 ms: 1.36x slower                                                        |
| pprint_pformat             | 1.90 sec                                                 | 2.62 sec: 1.38x slower                                                      |
| regex_compile              | 127 ms                                                   | 177 ms: 1.39x slower                                                        |
| genshi_xml                 | 60.3 ms                                                  | 84.8 ms: 1.41x slower                                                       |
| sympy_integrate            | 20.8 ms                                                  | 29.6 ms: 1.42x slower                                                       |
| hexiom                     | 7.11 ms                                                  | 10.4 ms: 1.47x slower                                                       |
| sympy_sum                  | 144 ms                                                   | 216 ms: 1.51x slower                                                        |
| generators                 | 37.6 ms                                                  | 59.1 ms: 1.57x slower                                                       |
| bench_mp_pool              | 7.68 ms                                                  | 1.51 sec: 196.24x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.18x slower                                                                |

Benchmark hidden because not significant (13): xml_etree_parse, async_tree_cpu_io_mixed, json, deepcopy_reduce, xml_etree_generate, coverage, scimark_sor, python_startup_no_site, pidigits, xml_etree_iterparse, regex_effbot, coroutines, xml_etree_process
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path
Ignored benchmarks (1) of results/bm-20241025-3.14.0a1+-64b198a-JIT/bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a.json: dulwich_log

- Geometric mean (including insignificant results): 1.104x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.08x