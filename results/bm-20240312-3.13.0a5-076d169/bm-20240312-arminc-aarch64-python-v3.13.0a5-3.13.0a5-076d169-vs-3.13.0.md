# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a5
- machine: linux-aarch64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.007x faster
- HPT reliability: 81.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.88x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 306 ms: 1.01x slower                                         |
| chameleon      | 9.08 ms                                                  | 8.86 ms: 1.02x faster                                        |
| docutils       | 2.89 sec                                                 | 2.92 sec: 1.01x slower                                       |
| tornado_http   | 128 ms                                                   | 136 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| coroutines                 | 28.5 ms                                                  | 28.8 ms: 1.01x slower                                        |
| async_tree_memoization_tg  | 649 ms                                                   | 731 ms: 1.13x slower                                         |
| async_tree_memoization     | 651 ms                                                   | 737 ms: 1.13x slower                                         |
| async_tree_none            | 497 ms                                                   | 573 ms: 1.15x slower                                         |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 890 ms: 1.16x slower                                         |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 893 ms: 1.16x slower                                         |
| async_tree_none_tg         | 470 ms                                                   | 577 ms: 1.23x slower                                         |
| async_tree_io_tg           | 1.13 sec                                                 | 1.43 sec: 1.26x slower                                       |
| async_tree_io              | 1.11 sec                                                 | 1.44 sec: 1.30x slower                                       |
| Geometric mean             | (ref)                                                    | 1.14x slower                                                 |

Benchmark hidden because not significant (2): async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 103 ms: 1.11x faster                                         |
| Geometric mean | (ref)                                                    | 1.03x faster                                                 |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.4 ms: 1.05x faster                                        |
| Geometric mean | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (3): regex_dna, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.6 ms                                                  | 12.8 ms: 1.06x faster                                        |
| pickle_pure_python   | 357 us                                                   | 349 us: 1.02x faster                                         |
| json_loads           | 31.7 us                                                  | 32.2 us: 1.02x slower                                        |
| tomli_loads          | 2.54 sec                                                 | 2.59 sec: 1.02x slower                                       |
| unpickle_pure_python | 251 us                                                   | 256 us: 1.02x slower                                         |
| Geometric mean       | (ref)                                                    | 1.00x faster                                                 |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 12.2 ms: 1.26x faster                                        |
| python_startup_no_site | 8.73 ms                                                  | 10.5 ms: 1.20x slower                                        |
| Geometric mean         | (ref)                                                    | 1.02x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 12.9 ms: 1.03x faster                                        |
| django_template | 41.6 ms                                                  | 40.5 ms: 1.03x faster                                        |
| Geometric mean  | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 1.99 ms: 1.68x faster                                        |
| typing_runtime_protocols   | 193 us                                                   | 133 us: 1.45x faster                                         |
| gc_traversal               | 5.77 ms                                                  | 4.45 ms: 1.30x faster                                        |
| python_startup             | 15.4 ms                                                  | 12.2 ms: 1.26x faster                                        |
| mypy2                      | 1.15 sec                                                 | 917 ms: 1.26x faster                                         |
| nbody                      | 114 ms                                                   | 103 ms: 1.11x faster                                         |
| bench_mp_pool              | 7.68 ms                                                  | 7.02 ms: 1.09x faster                                        |
| json_dumps                 | 13.6 ms                                                  | 12.8 ms: 1.06x faster                                        |
| crypto_pyaes               | 83.7 ms                                                  | 79.2 ms: 1.06x faster                                        |
| spectral_norm              | 143 ms                                                   | 135 ms: 1.05x faster                                         |
| generators                 | 37.6 ms                                                  | 35.9 ms: 1.05x faster                                        |
| regex_v8                   | 31.8 ms                                                  | 30.4 ms: 1.05x faster                                        |
| deepcopy_memo              | 50.4 us                                                  | 48.2 us: 1.04x faster                                        |
| thrift                     | 968 us                                                   | 929 us: 1.04x faster                                         |
| nqueens                    | 100 ms                                                   | 96.0 ms: 1.04x faster                                        |
| deepcopy                   | 447 us                                                   | 431 us: 1.04x faster                                         |
| richards                   | 53.6 ms                                                  | 51.8 ms: 1.04x faster                                        |
| mako                       | 13.4 ms                                                  | 12.9 ms: 1.03x faster                                        |
| deepcopy_reduce            | 4.07 us                                                  | 3.95 us: 1.03x faster                                        |
| sympy_sum                  | 144 ms                                                   | 140 ms: 1.03x faster                                         |
| django_template            | 41.6 ms                                                  | 40.5 ms: 1.03x faster                                        |
| hexiom                     | 7.11 ms                                                  | 6.92 ms: 1.03x faster                                        |
| pprint_safe_repr           | 926 ms                                                   | 903 ms: 1.03x faster                                         |
| chameleon                  | 9.08 ms                                                  | 8.86 ms: 1.02x faster                                        |
| comprehensions             | 20.4 us                                                  | 19.9 us: 1.02x faster                                        |
| pickle_pure_python         | 357 us                                                   | 349 us: 1.02x faster                                         |
| pprint_pformat             | 1.90 sec                                                 | 1.86 sec: 1.02x faster                                       |
| logging_silent             | 133 ns                                                   | 130 ns: 1.02x faster                                         |
| sympy_integrate            | 20.8 ms                                                  | 20.4 ms: 1.02x faster                                        |
| richards_super             | 60.1 ms                                                  | 59.1 ms: 1.02x faster                                        |
| scimark_monte_carlo        | 83.6 ms                                                  | 82.1 ms: 1.02x faster                                        |
| sqlglot_optimize           | 62.2 ms                                                  | 61.2 ms: 1.02x faster                                        |
| scimark_lu                 | 139 ms                                                   | 137 ms: 1.02x faster                                         |
| sympy_str                  | 264 ms                                                   | 260 ms: 1.02x faster                                         |
| scimark_fft                | 447 ms                                                   | 441 ms: 1.01x faster                                         |
| sympy_expand               | 457 ms                                                   | 451 ms: 1.01x faster                                         |
| raytrace                   | 300 ms                                                   | 296 ms: 1.01x faster                                         |
| mdp                        | 3.34 sec                                                 | 3.32 sec: 1.00x faster                                       |
| docutils                   | 2.89 sec                                                 | 2.92 sec: 1.01x slower                                       |
| go                         | 160 ms                                                   | 161 ms: 1.01x slower                                         |
| 2to3                       | 304 ms                                                   | 306 ms: 1.01x slower                                         |
| bench_thread_pool          | 1.27 ms                                                  | 1.29 ms: 1.01x slower                                        |
| coroutines                 | 28.5 ms                                                  | 28.8 ms: 1.01x slower                                        |
| logging_simple             | 7.07 us                                                  | 7.18 us: 1.02x slower                                        |
| json_loads                 | 31.7 us                                                  | 32.2 us: 1.02x slower                                        |
| tomli_loads                | 2.54 sec                                                 | 2.59 sec: 1.02x slower                                       |
| unpickle_pure_python       | 251 us                                                   | 256 us: 1.02x slower                                         |
| coverage                   | 99.1 ms                                                  | 102 ms: 1.03x slower                                         |
| scimark_sor                | 160 ms                                                   | 165 ms: 1.03x slower                                         |
| telco                      | 9.74 ms                                                  | 10.2 ms: 1.05x slower                                        |
| deltablue                  | 3.82 ms                                                  | 4.00 ms: 1.05x slower                                        |
| pyflate                    | 556 ms                                                   | 591 ms: 1.06x slower                                         |
| tornado_http               | 128 ms                                                   | 136 ms: 1.06x slower                                         |
| pathlib                    | 22.7 ms                                                  | 24.2 ms: 1.06x slower                                        |
| async_tree_memoization_tg  | 649 ms                                                   | 731 ms: 1.13x slower                                         |
| async_tree_memoization     | 651 ms                                                   | 737 ms: 1.13x slower                                         |
| async_tree_none            | 497 ms                                                   | 573 ms: 1.15x slower                                         |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 890 ms: 1.16x slower                                         |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 893 ms: 1.16x slower                                         |
| python_startup_no_site     | 8.73 ms                                                  | 10.5 ms: 1.20x slower                                        |
| async_tree_none_tg         | 470 ms                                                   | 577 ms: 1.23x slower                                         |
| async_tree_io_tg           | 1.13 sec                                                 | 1.43 sec: 1.26x slower                                       |
| async_tree_io              | 1.11 sec                                                 | 1.44 sec: 1.30x slower                                       |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (25): xml_etree_parse, pylint, regex_dna, sqlglot_normalize, regex_compile, html5lib, chaos, xml_etree_iterparse, fannkuch, async_generators, json, sqlglot_parse, float, xml_etree_process, scimark_sparse_mat_mult, logging_format, genshi_text, pidigits, genshi_xml, pycparser, asyncio_websockets, regex_effbot, sqlglot_transpile, meteor_contest, xml_etree_generate
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, dulwich_log, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.007x faster
# HPT report

- Reliability score: 81.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.88x