# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a5
- machine: linux-aarch64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.00x slower
- HPT reliability: 64.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| chameleon      | 8.95 ms                                                      | 8.86 ms: 1.01x faster                                        |
| docutils       | 3.10 sec                                                     | 2.92 sec: 1.06x faster                                       |
| tornado_http   | 128 ms                                                       | 136 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.43 sec: 1.12x slower                                       |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 893 ms: 1.13x slower                                         |
| async_tree_memoization     | 645 ms                                                       | 737 ms: 1.14x slower                                         |
| async_tree_none            | 492 ms                                                       | 573 ms: 1.16x slower                                         |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 890 ms: 1.17x slower                                         |
| async_tree_io              | 1.22 sec                                                     | 1.44 sec: 1.17x slower                                       |
| async_tree_memoization_tg  | 604 ms                                                       | 731 ms: 1.21x slower                                         |
| async_tree_none_tg         | 476 ms                                                       | 577 ms: 1.21x slower                                         |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 103 ms: 1.10x faster                                         |
| float          | 91.4 ms                                                      | 93.1 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 251 ms: 1.03x faster                                         |
| regex_v8       | 31.1 ms                                                      | 30.4 ms: 1.02x faster                                        |
| regex_compile  | 128 ms                                                       | 126 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                        | 1.02x faster                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_list        | 6.52 us                                                      | 6.25 us: 1.04x faster                                        |
| pickle_pure_python   | 359 us                                                       | 349 us: 1.03x faster                                         |
| json_dumps           | 13.1 ms                                                      | 12.8 ms: 1.03x faster                                        |
| unpickle             | 19.8 us                                                      | 19.3 us: 1.02x faster                                        |
| pickle               | 13.4 us                                                      | 13.3 us: 1.01x faster                                        |
| pickle_list          | 5.27 us                                                      | 5.26 us: 1.00x faster                                        |
| tomli_loads          | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                       |
| xml_etree_iterparse  | 147 ms                                                       | 149 ms: 1.01x slower                                         |
| unpickle_pure_python | 251 us                                                       | 256 us: 1.02x slower                                         |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (5): xml_etree_process, pickle_dict, xml_etree_parse, json_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 12.2 ms: 1.06x faster                                        |
| python_startup_no_site | 8.60 ms                                                      | 10.5 ms: 1.22x slower                                        |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 40.5 ms: 1.04x faster                                        |
| mako            | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                 |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols   | 193 us                                                       | 133 us: 1.45x faster                                         |
| create_gc_cycles           | 2.33 ms                                                      | 1.99 ms: 1.17x faster                                        |
| gc_traversal               | 5.17 ms                                                      | 4.45 ms: 1.16x faster                                        |
| nbody                      | 114 ms                                                       | 103 ms: 1.10x faster                                         |
| richards                   | 55.9 ms                                                      | 51.8 ms: 1.08x faster                                        |
| python_startup             | 13.0 ms                                                      | 12.2 ms: 1.06x faster                                        |
| docutils                   | 3.10 sec                                                     | 2.92 sec: 1.06x faster                                       |
| richards_super             | 62.3 ms                                                      | 59.1 ms: 1.05x faster                                        |
| deepcopy_memo              | 50.8 us                                                      | 48.2 us: 1.05x faster                                        |
| django_template            | 42.3 ms                                                      | 40.5 ms: 1.04x faster                                        |
| asyncio_tcp                | 584 ms                                                       | 559 ms: 1.04x faster                                         |
| spectral_norm              | 141 ms                                                       | 135 ms: 1.04x faster                                         |
| unpickle_list              | 6.52 us                                                      | 6.25 us: 1.04x faster                                        |
| deepcopy                   | 448 us                                                       | 431 us: 1.04x faster                                         |
| pprint_pformat             | 1.93 sec                                                     | 1.86 sec: 1.04x faster                                       |
| thrift                     | 962 us                                                       | 929 us: 1.04x faster                                         |
| crypto_pyaes               | 82.0 ms                                                      | 79.2 ms: 1.03x faster                                        |
| pprint_safe_repr           | 933 ms                                                       | 903 ms: 1.03x faster                                         |
| generators                 | 37.1 ms                                                      | 35.9 ms: 1.03x faster                                        |
| comprehensions             | 20.5 us                                                      | 19.9 us: 1.03x faster                                        |
| regex_dna                  | 259 ms                                                       | 251 ms: 1.03x faster                                         |
| scimark_lu                 | 141 ms                                                       | 137 ms: 1.03x faster                                         |
| nqueens                    | 98.9 ms                                                      | 96.0 ms: 1.03x faster                                        |
| sympy_sum                  | 144 ms                                                       | 140 ms: 1.03x faster                                         |
| pickle_pure_python         | 359 us                                                       | 349 us: 1.03x faster                                         |
| json_dumps                 | 13.1 ms                                                      | 12.8 ms: 1.03x faster                                        |
| logging_silent             | 133 ns                                                       | 130 ns: 1.02x faster                                         |
| sqlglot_optimize           | 62.6 ms                                                      | 61.2 ms: 1.02x faster                                        |
| hexiom                     | 7.08 ms                                                      | 6.92 ms: 1.02x faster                                        |
| regex_v8                   | 31.1 ms                                                      | 30.4 ms: 1.02x faster                                        |
| deepcopy_reduce            | 4.04 us                                                      | 3.95 us: 1.02x faster                                        |
| unpickle                   | 19.8 us                                                      | 19.3 us: 1.02x faster                                        |
| sympy_integrate            | 20.9 ms                                                      | 20.4 ms: 1.02x faster                                        |
| sympy_str                  | 265 ms                                                       | 260 ms: 1.02x faster                                         |
| mako                       | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                        |
| regex_compile              | 128 ms                                                       | 126 ms: 1.02x faster                                         |
| sympy_expand               | 457 ms                                                       | 451 ms: 1.01x faster                                         |
| scimark_fft                | 445 ms                                                       | 441 ms: 1.01x faster                                         |
| chameleon                  | 8.95 ms                                                      | 8.86 ms: 1.01x faster                                        |
| pickle                     | 13.4 us                                                      | 13.3 us: 1.01x faster                                        |
| pickle_list                | 5.27 us                                                      | 5.26 us: 1.00x faster                                        |
| tomli_loads                | 2.57 sec                                                     | 2.59 sec: 1.01x slower                                       |
| asyncio_websockets         | 657 ms                                                       | 664 ms: 1.01x slower                                         |
| xml_etree_iterparse        | 147 ms                                                       | 149 ms: 1.01x slower                                         |
| fannkuch                   | 451 ms                                                       | 459 ms: 1.02x slower                                         |
| telco                      | 10.0 ms                                                      | 10.2 ms: 1.02x slower                                        |
| float                      | 91.4 ms                                                      | 93.1 ms: 1.02x slower                                        |
| unpickle_pure_python       | 251 us                                                       | 256 us: 1.02x slower                                         |
| dulwich_log                | 58.5 ms                                                      | 59.7 ms: 1.02x slower                                        |
| sqlglot_transpile          | 1.71 ms                                                      | 1.75 ms: 1.02x slower                                        |
| bench_thread_pool          | 1.26 ms                                                      | 1.29 ms: 1.02x slower                                        |
| deltablue                  | 3.88 ms                                                      | 4.00 ms: 1.03x slower                                        |
| coverage                   | 98.4 ms                                                      | 102 ms: 1.03x slower                                         |
| dask                       | 370 ms                                                       | 383 ms: 1.03x slower                                         |
| scimark_sor                | 159 ms                                                       | 165 ms: 1.03x slower                                         |
| gunicorn                   | 1.19 ms                                                      | 1.23 ms: 1.04x slower                                        |
| pycparser                  | 1.22 sec                                                     | 1.28 sec: 1.05x slower                                       |
| pathlib                    | 22.8 ms                                                      | 24.2 ms: 1.06x slower                                        |
| pyflate                    | 557 ms                                                       | 591 ms: 1.06x slower                                         |
| tornado_http               | 128 ms                                                       | 136 ms: 1.06x slower                                         |
| async_tree_io_tg           | 1.27 sec                                                     | 1.43 sec: 1.12x slower                                       |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 893 ms: 1.13x slower                                         |
| async_tree_memoization     | 645 ms                                                       | 737 ms: 1.14x slower                                         |
| async_tree_none            | 492 ms                                                       | 573 ms: 1.16x slower                                         |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 890 ms: 1.17x slower                                         |
| async_tree_io              | 1.22 sec                                                     | 1.44 sec: 1.17x slower                                       |
| mypy2                      | 767 ms                                                       | 917 ms: 1.20x slower                                         |
| async_tree_memoization_tg  | 604 ms                                                       | 731 ms: 1.21x slower                                         |
| async_tree_none_tg         | 476 ms                                                       | 577 ms: 1.21x slower                                         |
| python_startup_no_site     | 8.60 ms                                                      | 10.5 ms: 1.22x slower                                        |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                 |

Benchmark hidden because not significant (31): sqlglot_parse, sqlglot_normalize, chaos, regex_effbot, sqlite_synth, scimark_sparse_mat_mult, coroutines, pylint, xml_etree_process, logging_simple, aiohttp, html5lib, scimark_monte_carlo, async_generators, bench_mp_pool, raytrace, pickle_dict, mdp, xml_etree_parse, pidigits, logging_format, genshi_xml, json_loads, go, asyncio_tcp_ssl, 2to3, flaskblogging, json, genshi_text, meteor_contest, xml_etree_generate
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 64.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x