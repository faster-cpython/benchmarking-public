# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: linux-aarch64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.067x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 360 ms: 1.19x slower                                         |
| chameleon      | 9.08 ms                                                  | 9.18 ms: 1.01x slower                                        |
| docutils       | 2.89 sec                                                 | 3.52 sec: 1.22x slower                                       |
| html5lib       | 66.4 ms                                                  | 71.7 ms: 1.08x slower                                        |
| tornado_http   | 128 ms                                                   | 139 ms: 1.08x slower                                         |
| Geometric mean | (ref)                                                    | 1.11x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 620 ms: 1.05x faster                                         |
| coroutines                 | 28.5 ms                                                  | 28.8 ms: 1.01x slower                                        |
| async_tree_none            | 497 ms                                                   | 508 ms: 1.02x slower                                         |
| async_tree_memoization     | 651 ms                                                   | 671 ms: 1.03x slower                                         |
| async_tree_none_tg         | 470 ms                                                   | 485 ms: 1.03x slower                                         |
| async_generators           | 489 ms                                                   | 508 ms: 1.04x slower                                         |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 806 ms: 1.05x slower                                         |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 818 ms: 1.07x slower                                         |
| async_tree_io_tg           | 1.13 sec                                                 | 1.23 sec: 1.09x slower                                       |
| async_tree_io              | 1.11 sec                                                 | 1.25 sec: 1.13x slower                                       |
| Geometric mean             | (ref)                                                    | 1.04x slower                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 88.7 ms: 1.05x faster                                        |
| Geometric mean | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.4 ms: 1.05x faster                                        |
| regex_dna      | 253 ms                                                   | 247 ms: 1.02x faster                                         |
| regex_compile  | 127 ms                                                   | 175 ms: 1.37x slower                                         |
| Geometric mean | (ref)                                                    | 1.06x slower                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 188 ms: 1.04x faster                                         |
| xml_etree_iterparse  | 149 ms                                                   | 148 ms: 1.01x faster                                         |
| json_loads           | 31.7 us                                                  | 32.1 us: 1.02x slower                                        |
| tomli_loads          | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                       |
| unpickle_pure_python | 251 us                                                   | 278 us: 1.11x slower                                         |
| pickle_pure_python   | 357 us                                                   | 398 us: 1.12x slower                                         |
| Geometric mean       | (ref)                                                    | 1.02x slower                                                 |

Benchmark hidden because not significant (3): json_dumps, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.73 ms                                                  | 10.9 ms: 1.25x slower                                        |
| Geometric mean         | (ref)                                                    | 1.11x slower                                                 |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.0 ms: 1.03x faster                                        |
| django_template | 41.6 ms                                                  | 49.6 ms: 1.19x slower                                        |
| genshi_text     | 27.7 ms                                                  | 35.4 ms: 1.28x slower                                        |
| genshi_xml      | 60.3 ms                                                  | 83.4 ms: 1.38x slower                                        |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.38 ms: 1.41x faster                                        |
| mypy2                      | 1.15 sec                                                 | 929 ms: 1.24x faster                                         |
| gc_traversal               | 5.77 ms                                                  | 5.08 ms: 1.14x faster                                        |
| float                      | 93.3 ms                                                  | 88.7 ms: 1.05x faster                                        |
| regex_v8                   | 31.8 ms                                                  | 30.4 ms: 1.05x faster                                        |
| async_tree_memoization_tg  | 649 ms                                                   | 620 ms: 1.05x faster                                         |
| xml_etree_parse            | 197 ms                                                   | 188 ms: 1.04x faster                                         |
| mako                       | 13.4 ms                                                  | 13.0 ms: 1.03x faster                                        |
| regex_dna                  | 253 ms                                                   | 247 ms: 1.02x faster                                         |
| deepcopy_memo              | 50.4 us                                                  | 49.7 us: 1.01x faster                                        |
| coverage                   | 99.1 ms                                                  | 98.1 ms: 1.01x faster                                        |
| xml_etree_iterparse        | 149 ms                                                   | 148 ms: 1.01x faster                                         |
| chameleon                  | 9.08 ms                                                  | 9.18 ms: 1.01x slower                                        |
| coroutines                 | 28.5 ms                                                  | 28.8 ms: 1.01x slower                                        |
| json_loads                 | 31.7 us                                                  | 32.1 us: 1.02x slower                                        |
| bpe_tokeniser              | 5.87 sec                                                 | 5.97 sec: 1.02x slower                                       |
| pathlib                    | 22.7 ms                                                  | 23.2 ms: 1.02x slower                                        |
| async_tree_none            | 497 ms                                                   | 508 ms: 1.02x slower                                         |
| scimark_fft                | 447 ms                                                   | 459 ms: 1.03x slower                                         |
| logging_format             | 7.82 us                                                  | 8.05 us: 1.03x slower                                        |
| mdp                        | 3.34 sec                                                 | 3.44 sec: 1.03x slower                                       |
| async_tree_memoization     | 651 ms                                                   | 671 ms: 1.03x slower                                         |
| async_tree_none_tg         | 470 ms                                                   | 485 ms: 1.03x slower                                         |
| bench_thread_pool          | 1.27 ms                                                  | 1.32 ms: 1.03x slower                                        |
| logging_simple             | 7.07 us                                                  | 7.31 us: 1.03x slower                                        |
| meteor_contest             | 114 ms                                                   | 118 ms: 1.04x slower                                         |
| tomli_loads                | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                       |
| async_generators           | 489 ms                                                   | 508 ms: 1.04x slower                                         |
| telco                      | 9.74 ms                                                  | 10.1 ms: 1.04x slower                                        |
| spectral_norm              | 143 ms                                                   | 149 ms: 1.04x slower                                         |
| richards                   | 53.6 ms                                                  | 56.2 ms: 1.05x slower                                        |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 806 ms: 1.05x slower                                         |
| generators                 | 37.6 ms                                                  | 39.6 ms: 1.05x slower                                        |
| richards_super             | 60.1 ms                                                  | 63.4 ms: 1.05x slower                                        |
| logging_silent             | 133 ns                                                   | 141 ns: 1.06x slower                                         |
| pycparser                  | 1.27 sec                                                 | 1.35 sec: 1.06x slower                                       |
| crypto_pyaes               | 83.7 ms                                                  | 89.1 ms: 1.06x slower                                        |
| scimark_monte_carlo        | 83.6 ms                                                  | 89.0 ms: 1.06x slower                                        |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.94 ms: 1.07x slower                                        |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 818 ms: 1.07x slower                                         |
| typing_runtime_protocols   | 193 us                                                   | 207 us: 1.07x slower                                         |
| pyflate                    | 556 ms                                                   | 596 ms: 1.07x slower                                         |
| raytrace                   | 300 ms                                                   | 321 ms: 1.07x slower                                         |
| bench_mp_pool              | 7.68 ms                                                  | 8.24 ms: 1.07x slower                                        |
| html5lib                   | 66.4 ms                                                  | 71.7 ms: 1.08x slower                                        |
| tornado_http               | 128 ms                                                   | 139 ms: 1.08x slower                                         |
| async_tree_io_tg           | 1.13 sec                                                 | 1.23 sec: 1.09x slower                                       |
| scimark_sor                | 160 ms                                                   | 174 ms: 1.09x slower                                         |
| unpickle_pure_python       | 251 us                                                   | 278 us: 1.11x slower                                         |
| pickle_pure_python         | 357 us                                                   | 398 us: 1.12x slower                                         |
| deepcopy                   | 447 us                                                   | 502 us: 1.12x slower                                         |
| sqlglot_optimize           | 62.2 ms                                                  | 69.8 ms: 1.12x slower                                        |
| go                         | 160 ms                                                   | 180 ms: 1.12x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.25 sec: 1.13x slower                                       |
| comprehensions             | 20.4 us                                                  | 23.2 us: 1.14x slower                                        |
| sqlglot_normalize          | 127 ms                                                   | 144 ms: 1.14x slower                                         |
| sqlglot_parse              | 1.38 ms                                                  | 1.58 ms: 1.15x slower                                        |
| deepcopy_reduce            | 4.07 us                                                  | 4.68 us: 1.15x slower                                        |
| sqlglot_transpile          | 1.73 ms                                                  | 2.00 ms: 1.16x slower                                        |
| nqueens                    | 100 ms                                                   | 117 ms: 1.17x slower                                         |
| sympy_expand               | 457 ms                                                   | 538 ms: 1.18x slower                                         |
| 2to3                       | 304 ms                                                   | 360 ms: 1.19x slower                                         |
| django_template            | 41.6 ms                                                  | 49.6 ms: 1.19x slower                                        |
| pprint_safe_repr           | 926 ms                                                   | 1.11 sec: 1.20x slower                                       |
| deltablue                  | 3.82 ms                                                  | 4.58 ms: 1.20x slower                                        |
| pylint                     | 342 ms                                                   | 414 ms: 1.21x slower                                         |
| sympy_str                  | 264 ms                                                   | 321 ms: 1.22x slower                                         |
| pprint_pformat             | 1.90 sec                                                 | 2.31 sec: 1.22x slower                                       |
| docutils                   | 2.89 sec                                                 | 3.52 sec: 1.22x slower                                       |
| sympy_integrate            | 20.8 ms                                                  | 25.5 ms: 1.23x slower                                        |
| python_startup_no_site     | 8.73 ms                                                  | 10.9 ms: 1.25x slower                                        |
| hexiom                     | 7.11 ms                                                  | 8.89 ms: 1.25x slower                                        |
| sympy_sum                  | 144 ms                                                   | 183 ms: 1.27x slower                                         |
| genshi_text                | 27.7 ms                                                  | 35.4 ms: 1.28x slower                                        |
| chaos                      | 68.0 ms                                                  | 87.1 ms: 1.28x slower                                        |
| scimark_lu                 | 139 ms                                                   | 183 ms: 1.31x slower                                         |
| regex_compile              | 127 ms                                                   | 175 ms: 1.37x slower                                         |
| genshi_xml                 | 60.3 ms                                                  | 83.4 ms: 1.38x slower                                        |
| Geometric mean             | (ref)                                                    | 1.07x slower                                                 |

Benchmark hidden because not significant (11): json_dumps, python_startup, regex_effbot, xml_etree_process, thrift, asyncio_websockets, json, pidigits, xml_etree_generate, fannkuch, nbody
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.067x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 0.99x