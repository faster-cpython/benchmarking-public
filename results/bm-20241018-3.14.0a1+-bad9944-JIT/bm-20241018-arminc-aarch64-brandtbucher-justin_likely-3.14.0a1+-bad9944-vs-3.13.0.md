# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_likely
- machine: linux-aarch64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.096x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 382 ms: 1.26x slower                                                    |
| docutils       | 2.89 sec                                                 | 3.58 sec: 1.24x slower                                                  |
| html5lib       | 66.4 ms                                                  | 71.9 ms: 1.08x slower                                                   |
| sphinx         | 1.17 sec                                                 | 1.47 sec: 1.26x slower                                                  |
| tornado_http   | 128 ms                                                   | 147 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                    | 1.19x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 536 ms: 1.21x faster                                                    |
| async_tree_none            | 497 ms                                                   | 457 ms: 1.09x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 600 ms: 1.08x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 446 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 742 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 755 ms: 1.02x faster                                                    |
| coroutines                 | 28.5 ms                                                  | 28.9 ms: 1.01x slower                                                   |
| async_generators           | 489 ms                                                   | 515 ms: 1.05x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.10x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 97.8 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                   |
| regex_effbot   | 4.89 ms                                                  | 4.96 ms: 1.01x slower                                                   |
| regex_compile  | 127 ms                                                   | 179 ms: 1.41x slower                                                    |
| Geometric mean | (ref)                                                    | 1.09x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 113 ms                                                   | 112 ms: 1.02x faster                                                    |
| tomli_loads          | 2.54 sec                                                 | 2.66 sec: 1.05x slower                                                  |
| json_dumps           | 13.6 ms                                                  | 14.6 ms: 1.07x slower                                                   |
| unpickle_pure_python | 251 us                                                   | 270 us: 1.08x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 392 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, json_loads, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 14.5 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.6 ms: 1.01x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 34.1 ms: 1.23x slower                                                   |
| django_template | 41.6 ms                                                  | 52.6 ms: 1.26x slower                                                   |
| genshi_xml      | 60.3 ms                                                  | 83.9 ms: 1.39x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.22x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.4 us                                                  | 39.3 us: 1.28x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 536 ms: 1.21x faster                                                    |
| deepcopy                   | 447 us                                                   | 380 us: 1.18x faster                                                    |
| async_tree_none            | 497 ms                                                   | 457 ms: 1.09x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 600 ms: 1.08x faster                                                    |
| python_startup             | 15.4 ms                                                  | 14.5 ms: 1.06x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 446 ms: 1.05x faster                                                    |
| pathlib                    | 22.7 ms                                                  | 21.8 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 742 ms: 1.04x faster                                                    |
| scimark_sor                | 160 ms                                                   | 154 ms: 1.03x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 3.98 us: 1.02x faster                                                   |
| xml_etree_generate         | 113 ms                                                   | 112 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 755 ms: 1.02x faster                                                    |
| telco                      | 9.74 ms                                                  | 9.64 ms: 1.01x faster                                                   |
| coroutines                 | 28.5 ms                                                  | 28.9 ms: 1.01x slower                                                   |
| mako                       | 13.4 ms                                                  | 13.6 ms: 1.01x slower                                                   |
| regex_effbot               | 4.89 ms                                                  | 4.96 ms: 1.01x slower                                                   |
| bpe_tokeniser              | 5.87 sec                                                 | 5.96 sec: 1.01x slower                                                  |
| scimark_fft                | 447 ms                                                   | 455 ms: 1.02x slower                                                    |
| logging_format             | 7.82 us                                                  | 8.12 us: 1.04x slower                                                   |
| float                      | 93.3 ms                                                  | 97.8 ms: 1.05x slower                                                   |
| mdp                        | 3.34 sec                                                 | 3.50 sec: 1.05x slower                                                  |
| tomli_loads                | 2.54 sec                                                 | 2.66 sec: 1.05x slower                                                  |
| async_generators           | 489 ms                                                   | 515 ms: 1.05x slower                                                    |
| logging_simple             | 7.07 us                                                  | 7.49 us: 1.06x slower                                                   |
| scimark_monte_carlo        | 83.6 ms                                                  | 88.7 ms: 1.06x slower                                                   |
| scimark_lu                 | 139 ms                                                   | 148 ms: 1.06x slower                                                    |
| crypto_pyaes               | 83.7 ms                                                  | 89.2 ms: 1.07x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                                  |
| json_dumps                 | 13.6 ms                                                  | 14.6 ms: 1.07x slower                                                   |
| unpickle_pure_python       | 251 us                                                   | 270 us: 1.08x slower                                                    |
| spectral_norm              | 143 ms                                                   | 154 ms: 1.08x slower                                                    |
| gc_traversal               | 5.77 ms                                                  | 6.24 ms: 1.08x slower                                                   |
| html5lib                   | 66.4 ms                                                  | 71.9 ms: 1.08x slower                                                   |
| bench_thread_pool          | 1.27 ms                                                  | 1.38 ms: 1.08x slower                                                   |
| meteor_contest             | 114 ms                                                   | 124 ms: 1.09x slower                                                    |
| pickle_pure_python         | 357 us                                                   | 392 us: 1.10x slower                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.10x slower                                                  |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 7.23 ms: 1.11x slower                                                   |
| fannkuch                   | 461 ms                                                   | 512 ms: 1.11x slower                                                    |
| create_gc_cycles           | 3.35 ms                                                  | 3.73 ms: 1.11x slower                                                   |
| typing_runtime_protocols   | 193 us                                                   | 219 us: 1.13x slower                                                    |
| tornado_http               | 128 ms                                                   | 147 ms: 1.15x slower                                                    |
| pyflate                    | 556 ms                                                   | 642 ms: 1.15x slower                                                    |
| go                         | 160 ms                                                   | 187 ms: 1.17x slower                                                    |
| raytrace                   | 300 ms                                                   | 352 ms: 1.18x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 4.50 ms: 1.18x slower                                                   |
| pycparser                  | 1.27 sec                                                 | 1.52 sec: 1.19x slower                                                  |
| richards_super             | 60.1 ms                                                  | 72.2 ms: 1.20x slower                                                   |
| richards                   | 53.6 ms                                                  | 64.6 ms: 1.21x slower                                                   |
| comprehensions             | 20.4 us                                                  | 24.8 us: 1.22x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 34.1 ms: 1.23x slower                                                   |
| docutils                   | 2.89 sec                                                 | 3.58 sec: 1.24x slower                                                  |
| nqueens                    | 100 ms                                                   | 124 ms: 1.24x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.71 ms: 1.24x slower                                                   |
| sqlglot_normalize          | 127 ms                                                   | 159 ms: 1.25x slower                                                    |
| sphinx                     | 1.17 sec                                                 | 1.47 sec: 1.26x slower                                                  |
| 2to3                       | 304 ms                                                   | 382 ms: 1.26x slower                                                    |
| chaos                      | 68.0 ms                                                  | 85.7 ms: 1.26x slower                                                   |
| django_template            | 41.6 ms                                                  | 52.6 ms: 1.26x slower                                                   |
| sympy_expand               | 457 ms                                                   | 589 ms: 1.29x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 2.25 ms: 1.30x slower                                                   |
| pprint_safe_repr           | 926 ms                                                   | 1.23 sec: 1.33x slower                                                  |
| sqlglot_optimize           | 62.2 ms                                                  | 83.1 ms: 1.34x slower                                                   |
| sympy_str                  | 264 ms                                                   | 356 ms: 1.35x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 2.62 sec: 1.38x slower                                                  |
| genshi_xml                 | 60.3 ms                                                  | 83.9 ms: 1.39x slower                                                   |
| sympy_integrate            | 20.8 ms                                                  | 29.3 ms: 1.41x slower                                                   |
| regex_compile              | 127 ms                                                   | 179 ms: 1.41x slower                                                    |
| pylint                     | 342 ms                                                   | 492 ms: 1.44x slower                                                    |
| hexiom                     | 7.11 ms                                                  | 10.3 ms: 1.45x slower                                                   |
| sympy_sum                  | 144 ms                                                   | 214 ms: 1.49x slower                                                    |
| generators                 | 37.6 ms                                                  | 59.1 ms: 1.57x slower                                                   |
| bench_mp_pool              | 7.68 ms                                                  | 2.25 sec: 292.95x slower                                                |
| Geometric mean             | (ref)                                                    | 1.18x slower                                                            |

Benchmark hidden because not significant (13): xml_etree_parse, json, coverage, logging_silent, json_loads, python_startup_no_site, xml_etree_iterparse, regex_dna, nbody, pidigits, asyncio_websockets, thrift, xml_etree_process
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-arminc-aarch64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.096x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.08x