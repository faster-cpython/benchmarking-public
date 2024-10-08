# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a2
- machine: linux-aarch64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.00x faster
- HPT reliability: 80.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 303 ms: 1.01x faster                                         |
| docutils       | 3.10 sec                                                     | 2.88 sec: 1.08x faster                                       |
| tornado_http   | 128 ms                                                       | 135 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmark hidden because not significant (2): chameleon, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 791 ms                                                       | 882 ms: 1.11x slower                                         |
| async_tree_memoization     | 645 ms                                                       | 736 ms: 1.14x slower                                         |
| async_tree_io_tg           | 1.27 sec                                                     | 1.47 sec: 1.16x slower                                       |
| async_tree_none            | 492 ms                                                       | 572 ms: 1.16x slower                                         |
| async_tree_io              | 1.22 sec                                                     | 1.44 sec: 1.18x slower                                       |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 907 ms: 1.19x slower                                         |
| async_tree_none_tg         | 476 ms                                                       | 590 ms: 1.24x slower                                         |
| async_tree_memoization_tg  | 604 ms                                                       | 763 ms: 1.26x slower                                         |
| Geometric mean             | (ref)                                                        | 1.18x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 105 ms: 1.09x faster                                         |
| float          | 91.4 ms                                                      | 90.6 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.61 ms: 1.08x faster                                        |
| regex_dna      | 259 ms                                                       | 246 ms: 1.05x faster                                         |
| regex_v8       | 31.1 ms                                                      | 30.0 ms: 1.03x faster                                        |
| regex_compile  | 128 ms                                                       | 129 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|---------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_list       | 6.52 us                                                      | 6.12 us: 1.07x faster                                        |
| json_dumps          | 13.1 ms                                                      | 12.4 ms: 1.06x faster                                        |
| unpickle            | 19.8 us                                                      | 18.7 us: 1.06x faster                                        |
| json_loads          | 32.1 us                                                      | 30.8 us: 1.04x faster                                        |
| pickle_pure_python  | 359 us                                                       | 346 us: 1.04x faster                                         |
| xml_etree_process   | 80.8 ms                                                      | 79.5 ms: 1.02x faster                                        |
| pickle_list         | 5.27 us                                                      | 5.19 us: 1.02x faster                                        |
| xml_etree_generate  | 114 ms                                                       | 113 ms: 1.01x faster                                         |
| xml_etree_iterparse | 147 ms                                                       | 149 ms: 1.02x slower                                         |
| Geometric mean      | (ref)                                                        | 1.02x faster                                                 |

Benchmark hidden because not significant (5): pickle_dict, tomli_loads, pickle, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 12.6 ms: 1.03x faster                                        |
| python_startup_no_site | 8.60 ms                                                      | 10.9 ms: 1.27x slower                                        |
| Geometric mean         | (ref)                                                        | 1.11x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 40.9 ms: 1.04x faster                                        |
| mako            | 13.2 ms                                                      | 12.8 ms: 1.02x faster                                        |
| genshi_text     | 27.4 ms                                                      | 27.9 ms: 1.02x slower                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols   | 193 us                                                       | 138 us: 1.40x faster                                         |
| create_gc_cycles           | 2.33 ms                                                      | 1.89 ms: 1.23x faster                                        |
| gc_traversal               | 5.17 ms                                                      | 4.44 ms: 1.17x faster                                        |
| spectral_norm              | 141 ms                                                       | 129 ms: 1.10x faster                                         |
| nbody                      | 114 ms                                                       | 105 ms: 1.09x faster                                         |
| regex_effbot               | 4.98 ms                                                      | 4.61 ms: 1.08x faster                                        |
| docutils                   | 3.10 sec                                                     | 2.88 sec: 1.08x faster                                       |
| richards                   | 55.9 ms                                                      | 52.2 ms: 1.07x faster                                        |
| unpickle_list              | 6.52 us                                                      | 6.12 us: 1.07x faster                                        |
| asyncio_tcp                | 584 ms                                                       | 551 ms: 1.06x faster                                         |
| aiohttp                    | 1.18 ms                                                      | 1.11 ms: 1.06x faster                                        |
| crypto_pyaes               | 82.0 ms                                                      | 77.5 ms: 1.06x faster                                        |
| json_dumps                 | 13.1 ms                                                      | 12.4 ms: 1.06x faster                                        |
| unpickle                   | 19.8 us                                                      | 18.7 us: 1.06x faster                                        |
| deepcopy_memo              | 50.8 us                                                      | 48.2 us: 1.05x faster                                        |
| regex_dna                  | 259 ms                                                       | 246 ms: 1.05x faster                                         |
| sqlglot_normalize          | 129 ms                                                       | 123 ms: 1.05x faster                                         |
| json_loads                 | 32.1 us                                                      | 30.8 us: 1.04x faster                                        |
| thrift                     | 962 us                                                       | 923 us: 1.04x faster                                         |
| comprehensions             | 20.5 us                                                      | 19.7 us: 1.04x faster                                        |
| sqlglot_parse              | 1.42 ms                                                      | 1.37 ms: 1.04x faster                                        |
| scimark_fft                | 445 ms                                                       | 428 ms: 1.04x faster                                         |
| sqlite_synth               | 3.90 us                                                      | 3.77 us: 1.04x faster                                        |
| pickle_pure_python         | 359 us                                                       | 346 us: 1.04x faster                                         |
| django_template            | 42.3 ms                                                      | 40.9 ms: 1.04x faster                                        |
| deepcopy                   | 448 us                                                       | 433 us: 1.03x faster                                         |
| regex_v8                   | 31.1 ms                                                      | 30.0 ms: 1.03x faster                                        |
| telco                      | 10.0 ms                                                      | 9.69 ms: 1.03x faster                                        |
| sqlglot_optimize           | 62.6 ms                                                      | 60.6 ms: 1.03x faster                                        |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.34 ms: 1.03x faster                                        |
| python_startup             | 13.0 ms                                                      | 12.6 ms: 1.03x faster                                        |
| deepcopy_reduce            | 4.04 us                                                      | 3.93 us: 1.03x faster                                        |
| json                       | 5.64 ms                                                      | 5.49 ms: 1.03x faster                                        |
| logging_silent             | 133 ns                                                       | 130 ns: 1.03x faster                                         |
| pprint_pformat             | 1.93 sec                                                     | 1.88 sec: 1.03x faster                                       |
| flaskblogging              | 4.70 ms                                                      | 4.57 ms: 1.03x faster                                        |
| richards_super             | 62.3 ms                                                      | 60.7 ms: 1.03x faster                                        |
| sympy_sum                  | 144 ms                                                       | 140 ms: 1.03x faster                                         |
| mako                       | 13.2 ms                                                      | 12.8 ms: 1.02x faster                                        |
| chaos                      | 68.3 ms                                                      | 66.9 ms: 1.02x faster                                        |
| sympy_expand               | 457 ms                                                       | 448 ms: 1.02x faster                                         |
| sympy_integrate            | 20.9 ms                                                      | 20.4 ms: 1.02x faster                                        |
| sympy_str                  | 265 ms                                                       | 260 ms: 1.02x faster                                         |
| pprint_safe_repr           | 933 ms                                                       | 916 ms: 1.02x faster                                         |
| bench_mp_pool              | 7.03 ms                                                      | 6.91 ms: 1.02x faster                                        |
| async_generators           | 488 ms                                                       | 480 ms: 1.02x faster                                         |
| xml_etree_process          | 80.8 ms                                                      | 79.5 ms: 1.02x faster                                        |
| pickle_list                | 5.27 us                                                      | 5.19 us: 1.02x faster                                        |
| scimark_monte_carlo        | 82.3 ms                                                      | 81.1 ms: 1.01x faster                                        |
| nqueens                    | 98.9 ms                                                      | 97.6 ms: 1.01x faster                                        |
| logging_format             | 7.82 us                                                      | 7.74 us: 1.01x faster                                        |
| float                      | 91.4 ms                                                      | 90.6 ms: 1.01x faster                                        |
| 2to3                       | 305 ms                                                       | 303 ms: 1.01x faster                                         |
| xml_etree_generate         | 114 ms                                                       | 113 ms: 1.01x faster                                         |
| regex_compile              | 128 ms                                                       | 129 ms: 1.01x slower                                         |
| fannkuch                   | 451 ms                                                       | 458 ms: 1.01x slower                                         |
| pyflate                    | 557 ms                                                       | 565 ms: 1.01x slower                                         |
| coverage                   | 98.4 ms                                                      | 99.8 ms: 1.01x slower                                        |
| dulwich_log                | 58.5 ms                                                      | 59.4 ms: 1.02x slower                                        |
| scimark_sor                | 159 ms                                                       | 162 ms: 1.02x slower                                         |
| genshi_text                | 27.4 ms                                                      | 27.9 ms: 1.02x slower                                        |
| xml_etree_iterparse        | 147 ms                                                       | 149 ms: 1.02x slower                                         |
| deltablue                  | 3.88 ms                                                      | 4.00 ms: 1.03x slower                                        |
| pycparser                  | 1.22 sec                                                     | 1.26 sec: 1.03x slower                                       |
| bench_thread_pool          | 1.26 ms                                                      | 1.31 ms: 1.04x slower                                        |
| pathlib                    | 22.8 ms                                                      | 23.9 ms: 1.05x slower                                        |
| tornado_http               | 128 ms                                                       | 135 ms: 1.06x slower                                         |
| generators                 | 37.1 ms                                                      | 39.5 ms: 1.06x slower                                        |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 882 ms: 1.11x slower                                         |
| async_tree_memoization     | 645 ms                                                       | 736 ms: 1.14x slower                                         |
| async_tree_io_tg           | 1.27 sec                                                     | 1.47 sec: 1.16x slower                                       |
| async_tree_none            | 492 ms                                                       | 572 ms: 1.16x slower                                         |
| mypy2                      | 767 ms                                                       | 892 ms: 1.16x slower                                         |
| async_tree_io              | 1.22 sec                                                     | 1.44 sec: 1.18x slower                                       |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 907 ms: 1.19x slower                                         |
| async_tree_none_tg         | 476 ms                                                       | 590 ms: 1.24x slower                                         |
| async_tree_memoization_tg  | 604 ms                                                       | 763 ms: 1.26x slower                                         |
| python_startup_no_site     | 8.60 ms                                                      | 10.9 ms: 1.27x slower                                        |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (22): logging_simple, hexiom, scimark_lu, html5lib, go, pickle_dict, pylint, pidigits, asyncio_tcp_ssl, mdp, asyncio_websockets, tomli_loads, chameleon, sqlglot_transpile, gunicorn, pickle, unpickle_pure_python, genshi_xml, raytrace, meteor_contest, coroutines, xml_etree_parse
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, dask

# HPT report

- Reliability score: 80.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.95x