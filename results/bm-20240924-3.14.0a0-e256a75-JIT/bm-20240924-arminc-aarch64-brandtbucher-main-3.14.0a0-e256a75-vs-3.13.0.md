# Results vs. 3.13.0

- fork: brandtbucher
- ref: main
- machine: linux-aarch64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.083x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 380 ms: 1.25x slower                                          |
| docutils       | 2.89 sec                                                 | 4.02 sec: 1.39x slower                                        |
| html5lib       | 66.4 ms                                                  | 72.5 ms: 1.09x slower                                         |
| tornado_http   | 128 ms                                                   | 150 ms: 1.18x slower                                          |
| Geometric mean | (ref)                                                    | 1.22x slower                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 568 ms: 1.14x faster                                          |
| async_tree_none            | 497 ms                                                   | 445 ms: 1.12x faster                                          |
| async_tree_memoization     | 651 ms                                                   | 588 ms: 1.11x faster                                          |
| async_tree_none_tg         | 470 ms                                                   | 432 ms: 1.09x faster                                          |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 737 ms: 1.04x faster                                          |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 754 ms: 1.02x faster                                          |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                        |
| async_generators           | 489 ms                                                   | 507 ms: 1.04x slower                                          |
| async_tree_io_tg           | 1.13 sec                                                 | 1.19 sec: 1.06x slower                                        |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                  |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 88.5 ms: 1.05x faster                                         |
| Geometric mean | (ref)                                                    | 1.02x faster                                                  |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.5 ms: 1.04x faster                                         |
| regex_dna      | 253 ms                                                   | 255 ms: 1.01x slower                                          |
| regex_effbot   | 4.89 ms                                                  | 4.96 ms: 1.01x slower                                         |
| regex_compile  | 127 ms                                                   | 197 ms: 1.55x slower                                          |
| Geometric mean | (ref)                                                    | 1.11x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:--------------------------------------------------------:|:-------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 187 ms: 1.05x faster                                          |
| xml_etree_generate   | 113 ms                                                   | 110 ms: 1.03x faster                                          |
| xml_etree_iterparse  | 149 ms                                                   | 148 ms: 1.01x faster                                          |
| tomli_loads          | 2.54 sec                                                 | 2.63 sec: 1.03x slower                                        |
| unpickle_pure_python | 251 us                                                   | 266 us: 1.06x slower                                          |
| pickle_pure_python   | 357 us                                                   | 399 us: 1.12x slower                                          |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                  |

Benchmark hidden because not significant (3): json_dumps, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.1 ms: 1.18x faster                                         |
| Geometric mean | (ref)                                                    | 1.09x faster                                                  |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:--------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                         |
| django_template | 41.6 ms                                                  | 51.0 ms: 1.22x slower                                         |
| genshi_text     | 27.7 ms                                                  | 34.6 ms: 1.25x slower                                         |
| genshi_xml      | 60.3 ms                                                  | 80.5 ms: 1.33x slower                                         |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.33 ms: 1.43x faster                                         |
| deepcopy_memo              | 50.4 us                                                  | 37.5 us: 1.34x faster                                         |
| python_startup             | 15.4 ms                                                  | 13.1 ms: 1.18x faster                                         |
| async_tree_memoization_tg  | 649 ms                                                   | 568 ms: 1.14x faster                                          |
| gc_traversal               | 5.77 ms                                                  | 5.12 ms: 1.13x faster                                         |
| deepcopy                   | 447 us                                                   | 398 us: 1.12x faster                                          |
| async_tree_none            | 497 ms                                                   | 445 ms: 1.12x faster                                          |
| async_tree_memoization     | 651 ms                                                   | 588 ms: 1.11x faster                                          |
| async_tree_none_tg         | 470 ms                                                   | 432 ms: 1.09x faster                                          |
| scimark_sor                | 160 ms                                                   | 151 ms: 1.06x faster                                          |
| float                      | 93.3 ms                                                  | 88.5 ms: 1.05x faster                                         |
| xml_etree_parse            | 197 ms                                                   | 187 ms: 1.05x faster                                          |
| bench_mp_pool              | 7.68 ms                                                  | 7.35 ms: 1.05x faster                                         |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 737 ms: 1.04x faster                                          |
| deepcopy_reduce            | 4.07 us                                                  | 3.90 us: 1.04x faster                                         |
| regex_v8                   | 31.8 ms                                                  | 30.5 ms: 1.04x faster                                         |
| pathlib                    | 22.7 ms                                                  | 21.8 ms: 1.04x faster                                         |
| xml_etree_generate         | 113 ms                                                   | 110 ms: 1.03x faster                                          |
| mako                       | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                         |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 754 ms: 1.02x faster                                          |
| thrift                     | 968 us                                                   | 953 us: 1.02x faster                                          |
| xml_etree_iterparse        | 149 ms                                                   | 148 ms: 1.01x faster                                          |
| bpe_tokeniser              | 5.87 sec                                                 | 5.91 sec: 1.01x slower                                        |
| regex_dna                  | 253 ms                                                   | 255 ms: 1.01x slower                                          |
| regex_effbot               | 4.89 ms                                                  | 4.96 ms: 1.01x slower                                         |
| logging_silent             | 133 ns                                                   | 136 ns: 1.03x slower                                          |
| spectral_norm              | 143 ms                                                   | 146 ms: 1.03x slower                                          |
| scimark_fft                | 447 ms                                                   | 459 ms: 1.03x slower                                          |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                        |
| tomli_loads                | 2.54 sec                                                 | 2.63 sec: 1.03x slower                                        |
| async_generators           | 489 ms                                                   | 507 ms: 1.04x slower                                          |
| coverage                   | 99.1 ms                                                  | 103 ms: 1.04x slower                                          |
| logging_format             | 7.82 us                                                  | 8.16 us: 1.04x slower                                         |
| mdp                        | 3.34 sec                                                 | 3.49 sec: 1.05x slower                                        |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.86 ms: 1.05x slower                                         |
| async_tree_io_tg           | 1.13 sec                                                 | 1.19 sec: 1.06x slower                                        |
| logging_simple             | 7.07 us                                                  | 7.49 us: 1.06x slower                                         |
| unpickle_pure_python       | 251 us                                                   | 266 us: 1.06x slower                                          |
| bench_thread_pool          | 1.27 ms                                                  | 1.36 ms: 1.07x slower                                         |
| scimark_lu                 | 139 ms                                                   | 149 ms: 1.07x slower                                          |
| crypto_pyaes               | 83.7 ms                                                  | 89.9 ms: 1.07x slower                                         |
| meteor_contest             | 114 ms                                                   | 124 ms: 1.09x slower                                          |
| html5lib                   | 66.4 ms                                                  | 72.5 ms: 1.09x slower                                         |
| telco                      | 9.74 ms                                                  | 10.7 ms: 1.10x slower                                         |
| fannkuch                   | 461 ms                                                   | 510 ms: 1.11x slower                                          |
| typing_runtime_protocols   | 193 us                                                   | 215 us: 1.11x slower                                          |
| scimark_monte_carlo        | 83.6 ms                                                  | 93.0 ms: 1.11x slower                                         |
| pickle_pure_python         | 357 us                                                   | 399 us: 1.12x slower                                          |
| pyflate                    | 556 ms                                                   | 628 ms: 1.13x slower                                          |
| deltablue                  | 3.82 ms                                                  | 4.36 ms: 1.14x slower                                         |
| raytrace                   | 300 ms                                                   | 347 ms: 1.16x slower                                          |
| go                         | 160 ms                                                   | 186 ms: 1.17x slower                                          |
| tornado_http               | 128 ms                                                   | 150 ms: 1.18x slower                                          |
| pycparser                  | 1.27 sec                                                 | 1.51 sec: 1.18x slower                                        |
| comprehensions             | 20.4 us                                                  | 24.3 us: 1.19x slower                                         |
| sqlglot_normalize          | 127 ms                                                   | 154 ms: 1.21x slower                                          |
| django_template            | 41.6 ms                                                  | 51.0 ms: 1.22x slower                                         |
| richards                   | 53.6 ms                                                  | 66.6 ms: 1.24x slower                                         |
| genshi_text                | 27.7 ms                                                  | 34.6 ms: 1.25x slower                                         |
| 2to3                       | 304 ms                                                   | 380 ms: 1.25x slower                                          |
| sqlglot_parse              | 1.38 ms                                                  | 1.75 ms: 1.27x slower                                         |
| nqueens                    | 100 ms                                                   | 127 ms: 1.27x slower                                          |
| richards_super             | 60.1 ms                                                  | 76.3 ms: 1.27x slower                                         |
| sqlglot_optimize           | 62.2 ms                                                  | 79.1 ms: 1.27x slower                                         |
| sqlglot_transpile          | 1.73 ms                                                  | 2.21 ms: 1.28x slower                                         |
| genshi_xml                 | 60.3 ms                                                  | 80.5 ms: 1.33x slower                                         |
| chaos                      | 68.0 ms                                                  | 90.8 ms: 1.34x slower                                         |
| sympy_expand               | 457 ms                                                   | 613 ms: 1.34x slower                                          |
| pprint_safe_repr           | 926 ms                                                   | 1.26 sec: 1.36x slower                                        |
| sympy_integrate            | 20.8 ms                                                  | 28.4 ms: 1.36x slower                                         |
| pprint_pformat             | 1.90 sec                                                 | 2.61 sec: 1.38x slower                                        |
| sympy_str                  | 264 ms                                                   | 366 ms: 1.39x slower                                          |
| docutils                   | 2.89 sec                                                 | 4.02 sec: 1.39x slower                                        |
| pylint                     | 342 ms                                                   | 476 ms: 1.39x slower                                          |
| hexiom                     | 7.11 ms                                                  | 10.2 ms: 1.44x slower                                         |
| sympy_sum                  | 144 ms                                                   | 209 ms: 1.46x slower                                          |
| generators                 | 37.6 ms                                                  | 56.5 ms: 1.50x slower                                         |
| regex_compile              | 127 ms                                                   | 197 ms: 1.55x slower                                          |
| Geometric mean             | (ref)                                                    | 1.09x slower                                                  |

Benchmark hidden because not significant (9): json_dumps, json, python_startup_no_site, coroutines, nbody, pidigits, json_loads, asyncio_websockets, xml_etree_process
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.083x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 0.99x