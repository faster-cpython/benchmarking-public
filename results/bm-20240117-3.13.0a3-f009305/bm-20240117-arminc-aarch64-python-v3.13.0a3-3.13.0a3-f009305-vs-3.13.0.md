# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: linux-aarch64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.007x faster
- HPT reliability: 78.51%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.86x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 305 ms: 1.00x slower                                         |
| chameleon      | 9.08 ms                                                  | 8.98 ms: 1.01x faster                                        |
| tornado_http   | 128 ms                                                   | 137 ms: 1.07x slower                                         |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_generators           | 489 ms                                                   | 480 ms: 1.02x faster                                         |
| coroutines                 | 28.5 ms                                                  | 29.4 ms: 1.03x slower                                        |
| async_tree_memoization_tg  | 649 ms                                                   | 736 ms: 1.13x slower                                         |
| async_tree_memoization     | 651 ms                                                   | 745 ms: 1.15x slower                                         |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 888 ms: 1.16x slower                                         |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 895 ms: 1.16x slower                                         |
| async_tree_none            | 497 ms                                                   | 582 ms: 1.17x slower                                         |
| async_tree_none_tg         | 470 ms                                                   | 574 ms: 1.22x slower                                         |
| async_tree_io_tg           | 1.13 sec                                                 | 1.44 sec: 1.27x slower                                       |
| async_tree_io              | 1.11 sec                                                 | 1.45 sec: 1.31x slower                                       |
| Geometric mean             | (ref)                                                    | 1.14x slower                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 104 ms: 1.10x faster                                         |
| float          | 93.3 ms                                                  | 91.0 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                    | 1.04x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.1 ms: 1.06x faster                                        |
| regex_effbot   | 4.89 ms                                                  | 4.65 ms: 1.05x faster                                        |
| regex_compile  | 127 ms                                                   | 125 ms: 1.02x faster                                         |
| regex_dna      | 253 ms                                                   | 255 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                    | 1.03x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.6 ms                                                  | 12.5 ms: 1.09x faster                                        |
| pickle_pure_python   | 357 us                                                   | 347 us: 1.03x faster                                         |
| json_loads           | 31.7 us                                                  | 31.1 us: 1.02x faster                                        |
| xml_etree_iterparse  | 149 ms                                                   | 152 ms: 1.02x slower                                         |
| unpickle_pure_python | 251 us                                                   | 256 us: 1.02x slower                                         |
| tomli_loads          | 2.54 sec                                                 | 2.59 sec: 1.02x slower                                       |
| xml_etree_parse      | 197 ms                                                   | 206 ms: 1.05x slower                                         |
| Geometric mean       | (ref)                                                    | 1.00x faster                                                 |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 12.1 ms: 1.28x faster                                        |
| python_startup_no_site | 8.73 ms                                                  | 10.3 ms: 1.18x slower                                        |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 12.9 ms: 1.04x faster                                        |
| django_template | 41.6 ms                                                  | 40.7 ms: 1.02x faster                                        |
| genshi_text     | 27.7 ms                                                  | 27.3 ms: 1.01x faster                                        |
| Geometric mean  | (ref)                                                    | 1.02x faster                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 1.91 ms: 1.76x faster                                        |
| typing_runtime_protocols   | 193 us                                                   | 135 us: 1.43x faster                                         |
| gc_traversal               | 5.77 ms                                                  | 4.36 ms: 1.32x faster                                        |
| mypy2                      | 1.15 sec                                                 | 899 ms: 1.28x faster                                         |
| python_startup             | 15.4 ms                                                  | 12.1 ms: 1.28x faster                                        |
| spectral_norm              | 143 ms                                                   | 129 ms: 1.11x faster                                         |
| nbody                      | 114 ms                                                   | 104 ms: 1.10x faster                                         |
| bench_mp_pool              | 7.68 ms                                                  | 6.98 ms: 1.10x faster                                        |
| json_dumps                 | 13.6 ms                                                  | 12.5 ms: 1.09x faster                                        |
| crypto_pyaes               | 83.7 ms                                                  | 77.3 ms: 1.08x faster                                        |
| regex_v8                   | 31.8 ms                                                  | 30.1 ms: 1.06x faster                                        |
| regex_effbot               | 4.89 ms                                                  | 4.65 ms: 1.05x faster                                        |
| thrift                     | 968 us                                                   | 925 us: 1.05x faster                                         |
| generators                 | 37.6 ms                                                  | 36.0 ms: 1.04x faster                                        |
| scimark_fft                | 447 ms                                                   | 430 ms: 1.04x faster                                         |
| nqueens                    | 100 ms                                                   | 96.4 ms: 1.04x faster                                        |
| mako                       | 13.4 ms                                                  | 12.9 ms: 1.04x faster                                        |
| sympy_sum                  | 144 ms                                                   | 139 ms: 1.03x faster                                         |
| comprehensions             | 20.4 us                                                  | 19.8 us: 1.03x faster                                        |
| sqlglot_normalize          | 127 ms                                                   | 123 ms: 1.03x faster                                         |
| pickle_pure_python         | 357 us                                                   | 347 us: 1.03x faster                                         |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.34 ms: 1.03x faster                                        |
| sqlglot_optimize           | 62.2 ms                                                  | 60.7 ms: 1.03x faster                                        |
| float                      | 93.3 ms                                                  | 91.0 ms: 1.03x faster                                        |
| json                       | 5.73 ms                                                  | 5.59 ms: 1.03x faster                                        |
| django_template            | 41.6 ms                                                  | 40.7 ms: 1.02x faster                                        |
| deepcopy_memo              | 50.4 us                                                  | 49.3 us: 1.02x faster                                        |
| sympy_expand               | 457 ms                                                   | 448 ms: 1.02x faster                                         |
| chaos                      | 68.0 ms                                                  | 66.7 ms: 1.02x faster                                        |
| sympy_str                  | 264 ms                                                   | 259 ms: 1.02x faster                                         |
| scimark_lu                 | 139 ms                                                   | 137 ms: 1.02x faster                                         |
| json_loads                 | 31.7 us                                                  | 31.1 us: 1.02x faster                                        |
| sympy_integrate            | 20.8 ms                                                  | 20.5 ms: 1.02x faster                                        |
| async_generators           | 489 ms                                                   | 480 ms: 1.02x faster                                         |
| regex_compile              | 127 ms                                                   | 125 ms: 1.02x faster                                         |
| genshi_text                | 27.7 ms                                                  | 27.3 ms: 1.01x faster                                        |
| raytrace                   | 300 ms                                                   | 296 ms: 1.01x faster                                         |
| fannkuch                   | 461 ms                                                   | 456 ms: 1.01x faster                                         |
| chameleon                  | 9.08 ms                                                  | 8.98 ms: 1.01x faster                                        |
| mdp                        | 3.34 sec                                                 | 3.32 sec: 1.00x faster                                       |
| 2to3                       | 304 ms                                                   | 305 ms: 1.00x slower                                         |
| go                         | 160 ms                                                   | 161 ms: 1.01x slower                                         |
| pprint_pformat             | 1.90 sec                                                 | 1.91 sec: 1.01x slower                                       |
| regex_dna                  | 253 ms                                                   | 255 ms: 1.01x slower                                         |
| pyflate                    | 556 ms                                                   | 562 ms: 1.01x slower                                         |
| pprint_safe_repr           | 926 ms                                                   | 936 ms: 1.01x slower                                         |
| logging_silent             | 133 ns                                                   | 134 ns: 1.01x slower                                         |
| richards_super             | 60.1 ms                                                  | 60.9 ms: 1.01x slower                                        |
| xml_etree_iterparse        | 149 ms                                                   | 152 ms: 1.02x slower                                         |
| scimark_sor                | 160 ms                                                   | 163 ms: 1.02x slower                                         |
| unpickle_pure_python       | 251 us                                                   | 256 us: 1.02x slower                                         |
| tomli_loads                | 2.54 sec                                                 | 2.59 sec: 1.02x slower                                       |
| logging_format             | 7.82 us                                                  | 8.00 us: 1.02x slower                                        |
| richards                   | 53.6 ms                                                  | 55.0 ms: 1.03x slower                                        |
| bench_thread_pool          | 1.27 ms                                                  | 1.31 ms: 1.03x slower                                        |
| logging_simple             | 7.07 us                                                  | 7.26 us: 1.03x slower                                        |
| coroutines                 | 28.5 ms                                                  | 29.4 ms: 1.03x slower                                        |
| coverage                   | 99.1 ms                                                  | 102 ms: 1.03x slower                                         |
| deltablue                  | 3.82 ms                                                  | 3.98 ms: 1.04x slower                                        |
| xml_etree_parse            | 197 ms                                                   | 206 ms: 1.05x slower                                         |
| pathlib                    | 22.7 ms                                                  | 24.1 ms: 1.06x slower                                        |
| tornado_http               | 128 ms                                                   | 137 ms: 1.07x slower                                         |
| async_tree_memoization_tg  | 649 ms                                                   | 736 ms: 1.13x slower                                         |
| async_tree_memoization     | 651 ms                                                   | 745 ms: 1.15x slower                                         |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 888 ms: 1.16x slower                                         |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 895 ms: 1.16x slower                                         |
| async_tree_none            | 497 ms                                                   | 582 ms: 1.17x slower                                         |
| python_startup_no_site     | 8.73 ms                                                  | 10.3 ms: 1.18x slower                                        |
| async_tree_none_tg         | 470 ms                                                   | 574 ms: 1.22x slower                                         |
| async_tree_io_tg           | 1.13 sec                                                 | 1.44 sec: 1.27x slower                                       |
| async_tree_io              | 1.11 sec                                                 | 1.45 sec: 1.31x slower                                       |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (17): pylint, sqlglot_transpile, sqlglot_parse, deepcopy_reduce, deepcopy, telco, pycparser, xml_etree_process, pidigits, html5lib, asyncio_websockets, scimark_monte_carlo, meteor_contest, hexiom, docutils, xml_etree_generate, genshi_xml
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-arminc-aarch64-python-v3.13.0a3-3.13.0a3-f009305.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dulwich_log, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.007x faster
# HPT report

- Reliability score: 78.51% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.86x