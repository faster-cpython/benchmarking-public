# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: linux-aarch64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.00x faster
- HPT reliability: 59.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 303 ms: 1.01x faster                                         |
| docutils       | 2.91 sec                                                 | 2.88 sec: 1.01x faster                                       |
| html5lib       | 64.3 ms                                                  | 65.7 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_generators           | 496 ms                                                   | 480 ms: 1.03x faster                                         |
| asyncio_tcp                | 568 ms                                                   | 551 ms: 1.03x faster                                         |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                       |
| coroutines                 | 28.2 ms                                                  | 29.2 ms: 1.04x slower                                        |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 882 ms: 1.15x slower                                         |
| async_tree_none            | 493 ms                                                   | 572 ms: 1.16x slower                                         |
| async_tree_memoization_tg  | 649 ms                                                   | 763 ms: 1.17x slower                                         |
| async_tree_memoization     | 626 ms                                                   | 736 ms: 1.18x slower                                         |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 907 ms: 1.23x slower                                         |
| async_tree_none_tg         | 467 ms                                                   | 590 ms: 1.26x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.44 sec: 1.30x slower                                       |
| async_tree_io_tg           | 1.09 sec                                                 | 1.47 sec: 1.35x slower                                       |
| Geometric mean             | (ref)                                                    | 1.13x slower                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 105 ms: 1.09x faster                                         |
| float          | 94.4 ms                                                  | 90.6 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                    | 1.04x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 4.61 ms: 1.06x faster                                        |
| regex_v8       | 31.5 ms                                                  | 30.0 ms: 1.05x faster                                        |
| regex_compile  | 128 ms                                                   | 129 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                    | 1.02x faster                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_list       | 6.65 us                                                  | 6.12 us: 1.09x faster                                        |
| unpickle            | 20.2 us                                                  | 18.7 us: 1.08x faster                                        |
| json_dumps          | 13.4 ms                                                  | 12.4 ms: 1.08x faster                                        |
| pickle_pure_python  | 359 us                                                   | 346 us: 1.04x faster                                         |
| pickle_list         | 5.34 us                                                  | 5.19 us: 1.03x faster                                        |
| json_loads          | 31.4 us                                                  | 30.8 us: 1.02x faster                                        |
| pickle_dict         | 38.1 us                                                  | 37.5 us: 1.02x faster                                        |
| tomli_loads         | 2.53 sec                                                 | 2.57 sec: 1.02x slower                                       |
| xml_etree_iterparse | 147 ms                                                   | 149 ms: 1.02x slower                                         |
| xml_etree_parse     | 188 ms                                                   | 196 ms: 1.05x slower                                         |
| Geometric mean      | (ref)                                                    | 1.02x faster                                                 |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_process, xml_etree_generate, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 12.6 ms: 1.06x faster                                        |
| python_startup_no_site | 8.75 ms                                                  | 10.9 ms: 1.24x slower                                        |
| Geometric mean         | (ref)                                                    | 1.09x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 12.8 ms: 1.04x faster                                        |
| django_template | 42.3 ms                                                  | 40.9 ms: 1.03x faster                                        |
| genshi_text     | 27.7 ms                                                  | 27.9 ms: 1.01x slower                                        |
| genshi_xml      | 60.2 ms                                                  | 60.7 ms: 1.01x slower                                        |
| Geometric mean  | (ref)                                                    | 1.01x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols   | 192 us                                                   | 138 us: 1.39x faster                                         |
| mypy2                      | 1.18 sec                                                 | 892 ms: 1.33x faster                                         |
| create_gc_cycles           | 2.12 ms                                                  | 1.89 ms: 1.12x faster                                        |
| spectral_norm              | 141 ms                                                   | 129 ms: 1.10x faster                                         |
| nbody                      | 114 ms                                                   | 105 ms: 1.09x faster                                         |
| unpickle_list              | 6.65 us                                                  | 6.12 us: 1.09x faster                                        |
| unpickle                   | 20.2 us                                                  | 18.7 us: 1.08x faster                                        |
| json_dumps                 | 13.4 ms                                                  | 12.4 ms: 1.08x faster                                        |
| aiohttp                    | 1.19 ms                                                  | 1.11 ms: 1.07x faster                                        |
| crypto_pyaes               | 82.7 ms                                                  | 77.5 ms: 1.07x faster                                        |
| deepcopy_memo              | 51.0 us                                                  | 48.2 us: 1.06x faster                                        |
| bench_mp_pool              | 7.30 ms                                                  | 6.91 ms: 1.06x faster                                        |
| regex_effbot               | 4.87 ms                                                  | 4.61 ms: 1.06x faster                                        |
| python_startup             | 13.3 ms                                                  | 12.6 ms: 1.06x faster                                        |
| regex_v8                   | 31.5 ms                                                  | 30.0 ms: 1.05x faster                                        |
| scimark_fft                | 447 ms                                                   | 428 ms: 1.04x faster                                         |
| logging_silent             | 135 ns                                                   | 130 ns: 1.04x faster                                         |
| float                      | 94.4 ms                                                  | 90.6 ms: 1.04x faster                                        |
| deepcopy                   | 451 us                                                   | 433 us: 1.04x faster                                         |
| sqlglot_normalize          | 128 ms                                                   | 123 ms: 1.04x faster                                         |
| pickle_pure_python         | 359 us                                                   | 346 us: 1.04x faster                                         |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.34 ms: 1.04x faster                                        |
| mako                       | 13.3 ms                                                  | 12.8 ms: 1.04x faster                                        |
| deepcopy_reduce            | 4.07 us                                                  | 3.93 us: 1.04x faster                                        |
| comprehensions             | 20.4 us                                                  | 19.7 us: 1.04x faster                                        |
| django_template            | 42.3 ms                                                  | 40.9 ms: 1.03x faster                                        |
| scimark_monte_carlo        | 83.8 ms                                                  | 81.1 ms: 1.03x faster                                        |
| async_generators           | 496 ms                                                   | 480 ms: 1.03x faster                                         |
| asyncio_tcp                | 568 ms                                                   | 551 ms: 1.03x faster                                         |
| sqlglot_optimize           | 62.4 ms                                                  | 60.6 ms: 1.03x faster                                        |
| chaos                      | 68.8 ms                                                  | 66.9 ms: 1.03x faster                                        |
| pickle_list                | 5.34 us                                                  | 5.19 us: 1.03x faster                                        |
| sympy_integrate            | 21.0 ms                                                  | 20.4 ms: 1.03x faster                                        |
| richards                   | 53.5 ms                                                  | 52.2 ms: 1.03x faster                                        |
| sympy_sum                  | 143 ms                                                   | 140 ms: 1.03x faster                                         |
| thrift                     | 946 us                                                   | 923 us: 1.02x faster                                         |
| json                       | 5.61 ms                                                  | 5.49 ms: 1.02x faster                                        |
| gc_traversal               | 4.53 ms                                                  | 4.44 ms: 1.02x faster                                        |
| json_loads                 | 31.4 us                                                  | 30.8 us: 1.02x faster                                        |
| sqlite_synth               | 3.84 us                                                  | 3.77 us: 1.02x faster                                        |
| pickle_dict                | 38.1 us                                                  | 37.5 us: 1.02x faster                                        |
| go                         | 163 ms                                                   | 160 ms: 1.02x faster                                         |
| sympy_expand               | 455 ms                                                   | 448 ms: 1.01x faster                                         |
| hexiom                     | 7.13 ms                                                  | 7.03 ms: 1.01x faster                                        |
| sympy_str                  | 264 ms                                                   | 260 ms: 1.01x faster                                         |
| pprint_safe_repr           | 926 ms                                                   | 916 ms: 1.01x faster                                         |
| mdp                        | 3.36 sec                                                 | 3.33 sec: 1.01x faster                                       |
| sqlglot_parse              | 1.38 ms                                                  | 1.37 ms: 1.01x faster                                        |
| nqueens                    | 98.7 ms                                                  | 97.6 ms: 1.01x faster                                        |
| pprint_pformat             | 1.90 sec                                                 | 1.88 sec: 1.01x faster                                       |
| docutils                   | 2.91 sec                                                 | 2.88 sec: 1.01x faster                                       |
| 2to3                       | 306 ms                                                   | 303 ms: 1.01x faster                                         |
| regex_compile              | 128 ms                                                   | 129 ms: 1.01x slower                                         |
| genshi_text                | 27.7 ms                                                  | 27.9 ms: 1.01x slower                                        |
| scimark_lu                 | 139 ms                                                   | 141 ms: 1.01x slower                                         |
| genshi_xml                 | 60.2 ms                                                  | 60.7 ms: 1.01x slower                                        |
| logging_simple             | 7.04 us                                                  | 7.12 us: 1.01x slower                                        |
| coverage                   | 98.5 ms                                                  | 99.8 ms: 1.01x slower                                        |
| fannkuch                   | 452 ms                                                   | 458 ms: 1.01x slower                                         |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.21 sec: 1.01x slower                                       |
| pyflate                    | 556 ms                                                   | 565 ms: 1.02x slower                                         |
| tomli_loads                | 2.53 sec                                                 | 2.57 sec: 1.02x slower                                       |
| xml_etree_iterparse        | 147 ms                                                   | 149 ms: 1.02x slower                                         |
| scimark_sor                | 159 ms                                                   | 162 ms: 1.02x slower                                         |
| html5lib                   | 64.3 ms                                                  | 65.7 ms: 1.02x slower                                        |
| bench_thread_pool          | 1.28 ms                                                  | 1.31 ms: 1.02x slower                                        |
| coroutines                 | 28.2 ms                                                  | 29.2 ms: 1.04x slower                                        |
| deltablue                  | 3.85 ms                                                  | 4.00 ms: 1.04x slower                                        |
| generators                 | 37.8 ms                                                  | 39.5 ms: 1.04x slower                                        |
| xml_etree_parse            | 188 ms                                                   | 196 ms: 1.05x slower                                         |
| pathlib                    | 22.4 ms                                                  | 23.9 ms: 1.07x slower                                        |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 882 ms: 1.15x slower                                         |
| async_tree_none            | 493 ms                                                   | 572 ms: 1.16x slower                                         |
| async_tree_memoization_tg  | 649 ms                                                   | 763 ms: 1.17x slower                                         |
| async_tree_memoization     | 626 ms                                                   | 736 ms: 1.18x slower                                         |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 907 ms: 1.23x slower                                         |
| python_startup_no_site     | 8.75 ms                                                  | 10.9 ms: 1.24x slower                                        |
| async_tree_none_tg         | 467 ms                                                   | 590 ms: 1.26x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.44 sec: 1.30x slower                                       |
| async_tree_io_tg           | 1.09 sec                                                 | 1.47 sec: 1.35x slower                                       |
| Geometric mean             | (ref)                                                    | 1.00x faster                                                 |

Benchmark hidden because not significant (19): pylint, logging_format, sqlglot_transpile, gunicorn, unpickle_pure_python, chameleon, flaskblogging, xml_etree_process, telco, pycparser, xml_etree_generate, pickle, pidigits, regex_dna, asyncio_websockets, raytrace, richards_super, meteor_contest, tornado_http
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, dask, unpack_sequence
Ignored benchmarks (1) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e.json: dulwich_log

# HPT report

- Reliability score: 59.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.95x