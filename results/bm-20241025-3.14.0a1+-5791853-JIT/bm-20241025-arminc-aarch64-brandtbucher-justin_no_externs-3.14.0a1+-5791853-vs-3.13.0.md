# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-aarch64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.099x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 385 ms: 1.27x slower                                                        |
| docutils       | 2.89 sec                                                 | 3.66 sec: 1.27x slower                                                      |
| html5lib       | 66.4 ms                                                  | 71.5 ms: 1.08x slower                                                       |
| sphinx         | 1.17 sec                                                 | 1.46 sec: 1.25x slower                                                      |
| tornado_http   | 128 ms                                                   | 148 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                    | 1.20x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 535 ms: 1.21x faster                                                        |
| async_tree_memoization     | 651 ms                                                   | 595 ms: 1.09x faster                                                        |
| async_tree_none            | 497 ms                                                   | 465 ms: 1.07x faster                                                        |
| async_tree_none_tg         | 470 ms                                                   | 442 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 738 ms: 1.04x faster                                                        |
| asyncio_websockets         | 659 ms                                                   | 664 ms: 1.01x slower                                                        |
| async_generators           | 489 ms                                                   | 510 ms: 1.04x slower                                                        |
| async_tree_io              | 1.11 sec                                                 | 1.17 sec: 1.05x slower                                                      |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.10x slower                                                      |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                                |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 96.2 ms: 1.03x slower                                                       |
| nbody          | 114 ms                                                   | 119 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                    | 1.03x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.9 ms: 1.03x faster                                                       |
| regex_dna      | 253 ms                                                   | 251 ms: 1.01x faster                                                        |
| regex_effbot   | 4.89 ms                                                  | 4.94 ms: 1.01x slower                                                       |
| regex_compile  | 127 ms                                                   | 176 ms: 1.38x slower                                                        |
| Geometric mean | (ref)                                                    | 1.08x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 186 ms: 1.05x faster                                                        |
| xml_etree_generate   | 113 ms                                                   | 111 ms: 1.02x faster                                                        |
| tomli_loads          | 2.54 sec                                                 | 2.67 sec: 1.05x slower                                                      |
| unpickle_pure_python | 251 us                                                   | 268 us: 1.07x slower                                                        |
| pickle_pure_python   | 357 us                                                   | 387 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                    | 1.02x slower                                                                |

Benchmark hidden because not significant (4): xml_etree_iterparse, json_loads, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 14.6 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                    | 1.02x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.7 ms: 1.02x slower                                                       |
| genshi_text     | 27.7 ms                                                  | 34.6 ms: 1.25x slower                                                       |
| django_template | 41.6 ms                                                  | 52.3 ms: 1.26x slower                                                       |
| genshi_xml      | 60.3 ms                                                  | 84.5 ms: 1.40x slower                                                       |
| Geometric mean  | (ref)                                                    | 1.22x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 50.4 us                                                  | 39.0 us: 1.29x faster                                                       |
| async_tree_memoization_tg  | 649 ms                                                   | 535 ms: 1.21x faster                                                        |
| deepcopy                   | 447 us                                                   | 378 us: 1.18x faster                                                        |
| async_tree_memoization     | 651 ms                                                   | 595 ms: 1.09x faster                                                        |
| async_tree_none            | 497 ms                                                   | 465 ms: 1.07x faster                                                        |
| pathlib                    | 22.7 ms                                                  | 21.3 ms: 1.07x faster                                                       |
| async_tree_none_tg         | 470 ms                                                   | 442 ms: 1.06x faster                                                        |
| python_startup             | 15.4 ms                                                  | 14.6 ms: 1.06x faster                                                       |
| xml_etree_parse            | 197 ms                                                   | 186 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 738 ms: 1.04x faster                                                        |
| regex_v8                   | 31.8 ms                                                  | 30.9 ms: 1.03x faster                                                       |
| json                       | 5.73 ms                                                  | 5.61 ms: 1.02x faster                                                       |
| xml_etree_generate         | 113 ms                                                   | 111 ms: 1.02x faster                                                        |
| deepcopy_reduce            | 4.07 us                                                  | 4.01 us: 1.01x faster                                                       |
| regex_dna                  | 253 ms                                                   | 251 ms: 1.01x faster                                                        |
| thrift                     | 968 us                                                   | 963 us: 1.01x faster                                                        |
| asyncio_websockets         | 659 ms                                                   | 664 ms: 1.01x slower                                                        |
| scimark_fft                | 447 ms                                                   | 450 ms: 1.01x slower                                                        |
| regex_effbot               | 4.89 ms                                                  | 4.94 ms: 1.01x slower                                                       |
| mako                       | 13.4 ms                                                  | 13.7 ms: 1.02x slower                                                       |
| bpe_tokeniser              | 5.87 sec                                                 | 6.04 sec: 1.03x slower                                                      |
| float                      | 93.3 ms                                                  | 96.2 ms: 1.03x slower                                                       |
| nbody                      | 114 ms                                                   | 119 ms: 1.04x slower                                                        |
| async_generators           | 489 ms                                                   | 510 ms: 1.04x slower                                                        |
| mdp                        | 3.34 sec                                                 | 3.49 sec: 1.05x slower                                                      |
| async_tree_io              | 1.11 sec                                                 | 1.17 sec: 1.05x slower                                                      |
| tomli_loads                | 2.54 sec                                                 | 2.67 sec: 1.05x slower                                                      |
| logging_format             | 7.82 us                                                  | 8.26 us: 1.06x slower                                                       |
| logging_simple             | 7.07 us                                                  | 7.54 us: 1.07x slower                                                       |
| unpickle_pure_python       | 251 us                                                   | 268 us: 1.07x slower                                                        |
| bench_thread_pool          | 1.27 ms                                                  | 1.37 ms: 1.07x slower                                                       |
| html5lib                   | 66.4 ms                                                  | 71.5 ms: 1.08x slower                                                       |
| scimark_lu                 | 139 ms                                                   | 151 ms: 1.08x slower                                                        |
| pickle_pure_python         | 357 us                                                   | 387 us: 1.08x slower                                                        |
| gc_traversal               | 5.77 ms                                                  | 6.26 ms: 1.08x slower                                                       |
| scimark_monte_carlo        | 83.6 ms                                                  | 90.7 ms: 1.09x slower                                                       |
| create_gc_cycles           | 3.35 ms                                                  | 3.65 ms: 1.09x slower                                                       |
| spectral_norm              | 143 ms                                                   | 156 ms: 1.10x slower                                                        |
| meteor_contest             | 114 ms                                                   | 125 ms: 1.10x slower                                                        |
| crypto_pyaes               | 83.7 ms                                                  | 92.0 ms: 1.10x slower                                                       |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.10x slower                                                      |
| logging_silent             | 133 ns                                                   | 147 ns: 1.10x slower                                                        |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 7.20 ms: 1.11x slower                                                       |
| fannkuch                   | 461 ms                                                   | 510 ms: 1.11x slower                                                        |
| typing_runtime_protocols   | 193 us                                                   | 219 us: 1.13x slower                                                        |
| go                         | 160 ms                                                   | 185 ms: 1.16x slower                                                        |
| tornado_http               | 128 ms                                                   | 148 ms: 1.16x slower                                                        |
| pyflate                    | 556 ms                                                   | 645 ms: 1.16x slower                                                        |
| deltablue                  | 3.82 ms                                                  | 4.45 ms: 1.16x slower                                                       |
| raytrace                   | 300 ms                                                   | 351 ms: 1.17x slower                                                        |
| pycparser                  | 1.27 sec                                                 | 1.51 sec: 1.19x slower                                                      |
| richards_super             | 60.1 ms                                                  | 71.8 ms: 1.20x slower                                                       |
| sqlglot_normalize          | 127 ms                                                   | 156 ms: 1.23x slower                                                        |
| sphinx                     | 1.17 sec                                                 | 1.46 sec: 1.25x slower                                                      |
| genshi_text                | 27.7 ms                                                  | 34.6 ms: 1.25x slower                                                       |
| sqlalchemy_declarative     | 150 ms                                                   | 188 ms: 1.25x slower                                                        |
| comprehensions             | 20.4 us                                                  | 25.6 us: 1.25x slower                                                       |
| django_template            | 41.6 ms                                                  | 52.3 ms: 1.26x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                  | 1.73 ms: 1.26x slower                                                       |
| docutils                   | 2.89 sec                                                 | 3.66 sec: 1.27x slower                                                      |
| sqlalchemy_imperative      | 15.1 ms                                                  | 19.2 ms: 1.27x slower                                                       |
| 2to3                       | 304 ms                                                   | 385 ms: 1.27x slower                                                        |
| richards                   | 53.6 ms                                                  | 68.5 ms: 1.28x slower                                                       |
| sqlglot_transpile          | 1.73 ms                                                  | 2.21 ms: 1.28x slower                                                       |
| pylint                     | 342 ms                                                   | 437 ms: 1.28x slower                                                        |
| sympy_expand               | 457 ms                                                   | 590 ms: 1.29x slower                                                        |
| chaos                      | 68.0 ms                                                  | 88.3 ms: 1.30x slower                                                       |
| sqlglot_optimize           | 62.2 ms                                                  | 81.4 ms: 1.31x slower                                                       |
| nqueens                    | 100 ms                                                   | 132 ms: 1.32x slower                                                        |
| pprint_safe_repr           | 926 ms                                                   | 1.23 sec: 1.33x slower                                                      |
| sympy_str                  | 264 ms                                                   | 358 ms: 1.36x slower                                                        |
| pprint_pformat             | 1.90 sec                                                 | 2.61 sec: 1.37x slower                                                      |
| regex_compile              | 127 ms                                                   | 176 ms: 1.38x slower                                                        |
| genshi_xml                 | 60.3 ms                                                  | 84.5 ms: 1.40x slower                                                       |
| sympy_integrate            | 20.8 ms                                                  | 29.3 ms: 1.41x slower                                                       |
| hexiom                     | 7.11 ms                                                  | 10.5 ms: 1.48x slower                                                       |
| sympy_sum                  | 144 ms                                                   | 216 ms: 1.51x slower                                                        |
| generators                 | 37.6 ms                                                  | 58.3 ms: 1.55x slower                                                       |
| bench_mp_pool              | 7.68 ms                                                  | 1.27 sec: 165.72x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.17x slower                                                                |

Benchmark hidden because not significant (11): telco, async_tree_cpu_io_mixed, xml_etree_iterparse, coverage, json_loads, xml_etree_process, python_startup_no_site, pidigits, coroutines, scimark_sor, json_dumps
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path
Ignored benchmarks (1) of results/bm-20241025-3.14.0a1+-5791853-JIT/bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853.json: dulwich_log

- Geometric mean (including insignificant results): 1.099x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.08x