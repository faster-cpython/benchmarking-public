# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-aarch64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.132x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 401 ms: 1.32x slower                                                        |
| docutils       | 2.89 sec                                                 | 3.74 sec: 1.29x slower                                                      |
| html5lib       | 66.4 ms                                                  | 73.0 ms: 1.10x slower                                                       |
| sphinx         | 1.17 sec                                                 | 1.49 sec: 1.28x slower                                                      |
| tornado_http   | 128 ms                                                   | 152 ms: 1.19x slower                                                        |
| Geometric mean | (ref)                                                    | 1.23x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 542 ms: 1.20x faster                                                        |
| async_tree_memoization     | 651 ms                                                   | 606 ms: 1.07x faster                                                        |
| async_tree_none            | 497 ms                                                   | 473 ms: 1.05x faster                                                        |
| async_tree_none_tg         | 470 ms                                                   | 450 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 742 ms: 1.04x faster                                                        |
| async_generators           | 489 ms                                                   | 505 ms: 1.03x slower                                                        |
| async_tree_io              | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                                      |
| async_tree_io_tg           | 1.13 sec                                                 | 1.26 sec: 1.11x slower                                                      |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                                |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 98.7 ms: 1.06x slower                                                       |
| nbody          | 114 ms                                                   | 132 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                    | 1.07x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.9 ms: 1.03x faster                                                       |
| regex_dna      | 253 ms                                                   | 251 ms: 1.01x faster                                                        |
| regex_compile  | 127 ms                                                   | 183 ms: 1.44x slower                                                        |
| Geometric mean | (ref)                                                    | 1.09x slower                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 189 ms: 1.04x faster                                                        |
| xml_etree_iterparse  | 149 ms                                                   | 151 ms: 1.01x slower                                                        |
| xml_etree_generate   | 113 ms                                                   | 117 ms: 1.03x slower                                                        |
| json_dumps           | 13.6 ms                                                  | 14.2 ms: 1.05x slower                                                       |
| xml_etree_process    | 80.5 ms                                                  | 86.3 ms: 1.07x slower                                                       |
| unpickle_pure_python | 251 us                                                   | 275 us: 1.10x slower                                                        |
| pickle_pure_python   | 357 us                                                   | 411 us: 1.15x slower                                                        |
| tomli_loads          | 2.54 sec                                                 | 2.93 sec: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                    | 1.06x slower                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 14.6 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 14.2 ms: 1.06x slower                                                       |
| genshi_text     | 27.7 ms                                                  | 35.2 ms: 1.27x slower                                                       |
| django_template | 41.6 ms                                                  | 55.3 ms: 1.33x slower                                                       |
| genshi_xml      | 60.3 ms                                                  | 86.4 ms: 1.43x slower                                                       |
| Geometric mean  | (ref)                                                    | 1.27x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 542 ms: 1.20x faster                                                        |
| deepcopy_memo              | 50.4 us                                                  | 42.3 us: 1.19x faster                                                       |
| deepcopy                   | 447 us                                                   | 392 us: 1.14x faster                                                        |
| async_tree_memoization     | 651 ms                                                   | 606 ms: 1.07x faster                                                        |
| python_startup             | 15.4 ms                                                  | 14.6 ms: 1.06x faster                                                       |
| async_tree_none            | 497 ms                                                   | 473 ms: 1.05x faster                                                        |
| async_tree_none_tg         | 470 ms                                                   | 450 ms: 1.05x faster                                                        |
| xml_etree_parse            | 197 ms                                                   | 189 ms: 1.04x faster                                                        |
| pathlib                    | 22.7 ms                                                  | 21.9 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 742 ms: 1.04x faster                                                        |
| regex_v8                   | 31.8 ms                                                  | 30.9 ms: 1.03x faster                                                       |
| regex_dna                  | 253 ms                                                   | 251 ms: 1.01x faster                                                        |
| xml_etree_iterparse        | 149 ms                                                   | 151 ms: 1.01x slower                                                        |
| telco                      | 9.74 ms                                                  | 10.0 ms: 1.03x slower                                                       |
| deepcopy_reduce            | 4.07 us                                                  | 4.19 us: 1.03x slower                                                       |
| async_generators           | 489 ms                                                   | 505 ms: 1.03x slower                                                        |
| xml_etree_generate         | 113 ms                                                   | 117 ms: 1.03x slower                                                        |
| scimark_sor                | 160 ms                                                   | 166 ms: 1.04x slower                                                        |
| json_dumps                 | 13.6 ms                                                  | 14.2 ms: 1.05x slower                                                       |
| float                      | 93.3 ms                                                  | 98.7 ms: 1.06x slower                                                       |
| mako                       | 13.4 ms                                                  | 14.2 ms: 1.06x slower                                                       |
| mdp                        | 3.34 sec                                                 | 3.55 sec: 1.06x slower                                                      |
| logging_format             | 7.82 us                                                  | 8.34 us: 1.07x slower                                                       |
| gc_traversal               | 5.77 ms                                                  | 6.16 ms: 1.07x slower                                                       |
| bpe_tokeniser              | 5.87 sec                                                 | 6.29 sec: 1.07x slower                                                      |
| xml_etree_process          | 80.5 ms                                                  | 86.3 ms: 1.07x slower                                                       |
| bench_thread_pool          | 1.27 ms                                                  | 1.37 ms: 1.07x slower                                                       |
| scimark_fft                | 447 ms                                                   | 481 ms: 1.08x slower                                                        |
| logging_simple             | 7.07 us                                                  | 7.63 us: 1.08x slower                                                       |
| async_tree_io              | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                                      |
| create_gc_cycles           | 3.35 ms                                                  | 3.67 ms: 1.09x slower                                                       |
| unpickle_pure_python       | 251 us                                                   | 275 us: 1.10x slower                                                        |
| html5lib                   | 66.4 ms                                                  | 73.0 ms: 1.10x slower                                                       |
| async_tree_io_tg           | 1.13 sec                                                 | 1.26 sec: 1.11x slower                                                      |
| scimark_lu                 | 139 ms                                                   | 158 ms: 1.13x slower                                                        |
| typing_runtime_protocols   | 193 us                                                   | 221 us: 1.14x slower                                                        |
| pickle_pure_python         | 357 us                                                   | 411 us: 1.15x slower                                                        |
| nbody                      | 114 ms                                                   | 132 ms: 1.15x slower                                                        |
| logging_silent             | 133 ns                                                   | 153 ns: 1.15x slower                                                        |
| tomli_loads                | 2.54 sec                                                 | 2.93 sec: 1.15x slower                                                      |
| meteor_contest             | 114 ms                                                   | 133 ms: 1.17x slower                                                        |
| spectral_norm              | 143 ms                                                   | 167 ms: 1.17x slower                                                        |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 7.70 ms: 1.18x slower                                                       |
| crypto_pyaes               | 83.7 ms                                                  | 99.1 ms: 1.18x slower                                                       |
| tornado_http               | 128 ms                                                   | 152 ms: 1.19x slower                                                        |
| fannkuch                   | 461 ms                                                   | 547 ms: 1.19x slower                                                        |
| scimark_monte_carlo        | 83.6 ms                                                  | 101 ms: 1.21x slower                                                        |
| raytrace                   | 300 ms                                                   | 368 ms: 1.23x slower                                                        |
| pycparser                  | 1.27 sec                                                 | 1.58 sec: 1.24x slower                                                      |
| deltablue                  | 3.82 ms                                                  | 4.83 ms: 1.26x slower                                                       |
| go                         | 160 ms                                                   | 203 ms: 1.27x slower                                                        |
| sqlalchemy_imperative      | 15.1 ms                                                  | 19.2 ms: 1.27x slower                                                       |
| genshi_text                | 27.7 ms                                                  | 35.2 ms: 1.27x slower                                                       |
| sphinx                     | 1.17 sec                                                 | 1.49 sec: 1.28x slower                                                      |
| pylint                     | 342 ms                                                   | 438 ms: 1.28x slower                                                        |
| sqlalchemy_declarative     | 150 ms                                                   | 193 ms: 1.29x slower                                                        |
| sqlglot_normalize          | 127 ms                                                   | 163 ms: 1.29x slower                                                        |
| docutils                   | 2.89 sec                                                 | 3.74 sec: 1.29x slower                                                      |
| pyflate                    | 556 ms                                                   | 725 ms: 1.30x slower                                                        |
| sympy_expand               | 457 ms                                                   | 603 ms: 1.32x slower                                                        |
| 2to3                       | 304 ms                                                   | 401 ms: 1.32x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                  | 1.82 ms: 1.32x slower                                                       |
| django_template            | 41.6 ms                                                  | 55.3 ms: 1.33x slower                                                       |
| comprehensions             | 20.4 us                                                  | 27.3 us: 1.34x slower                                                       |
| richards_super             | 60.1 ms                                                  | 80.8 ms: 1.34x slower                                                       |
| sqlglot_transpile          | 1.73 ms                                                  | 2.33 ms: 1.35x slower                                                       |
| sqlglot_optimize           | 62.2 ms                                                  | 86.1 ms: 1.38x slower                                                       |
| nqueens                    | 100 ms                                                   | 139 ms: 1.39x slower                                                        |
| sympy_str                  | 264 ms                                                   | 370 ms: 1.40x slower                                                        |
| chaos                      | 68.0 ms                                                  | 95.6 ms: 1.41x slower                                                       |
| genshi_xml                 | 60.3 ms                                                  | 86.4 ms: 1.43x slower                                                       |
| regex_compile              | 127 ms                                                   | 183 ms: 1.44x slower                                                        |
| sympy_integrate            | 20.8 ms                                                  | 30.3 ms: 1.45x slower                                                       |
| generators                 | 37.6 ms                                                  | 55.2 ms: 1.47x slower                                                       |
| pprint_safe_repr           | 926 ms                                                   | 1.37 sec: 1.48x slower                                                      |
| richards                   | 53.6 ms                                                  | 79.8 ms: 1.49x slower                                                       |
| pprint_pformat             | 1.90 sec                                                 | 2.85 sec: 1.51x slower                                                      |
| sympy_sum                  | 144 ms                                                   | 222 ms: 1.55x slower                                                        |
| hexiom                     | 7.11 ms                                                  | 11.5 ms: 1.62x slower                                                       |
| bench_mp_pool              | 7.68 ms                                                  | 2.46 sec: 320.08x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.22x slower                                                                |

Benchmark hidden because not significant (10): coverage, json, async_tree_cpu_io_mixed, thrift, pidigits, coroutines, json_loads, python_startup_no_site, asyncio_websockets, regex_effbot
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path
Ignored benchmarks (1) of results/bm-20241024-3.14.0a1+-9698931-JIT/bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931.json: dulwich_log

- Geometric mean (including insignificant results): 1.132x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 1.09x