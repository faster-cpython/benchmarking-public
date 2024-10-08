# Results vs. 3.13.0b2

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-aarch64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.03x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 302 ms: 1.01x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.13 sec: 1.01x slower                                                  |
| tornado_http   | 128 ms                                                       | 121 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 400 ms: 1.19x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 549 ms: 1.17x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 533 ms: 1.13x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.08 sec: 1.13x faster                                                  |
| async_tree_none            | 492 ms                                                       | 438 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 726 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 706 ms: 1.08x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.13x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| float          | 91.4 ms                                                      | 93.1 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.7 ms: 1.01x faster                                                   |
| regex_compile  | 128 ms                                                       | 126 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|---------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate  | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| tomli_loads         | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                  |
| xml_etree_iterparse | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| json_loads          | 32.1 us                                                      | 32.8 us: 1.02x slower                                                   |
| json_dumps          | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| Geometric mean      | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.81 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 330 us: 1.36x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 37.5 us: 1.35x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 400 ms: 1.19x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.40 us: 1.19x faster                                                   |
| async_tree_memoization     | 645 ms                                                       | 549 ms: 1.17x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 533 ms: 1.13x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.08 sec: 1.13x faster                                                  |
| async_tree_none            | 492 ms                                                       | 438 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 726 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 706 ms: 1.08x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 4.79 ms: 1.08x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 21.1 ms: 1.08x faster                                                   |
| generators                 | 37.1 ms                                                      | 34.4 ms: 1.08x faster                                                   |
| richards                   | 55.9 ms                                                      | 51.9 ms: 1.08x faster                                                   |
| richards_super             | 62.3 ms                                                      | 58.4 ms: 1.07x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 134 ms: 1.06x faster                                                    |
| tornado_http               | 128 ms                                                       | 121 ms: 1.05x faster                                                    |
| logging_simple             | 7.21 us                                                      | 6.93 us: 1.04x faster                                                   |
| scimark_sor                | 159 ms                                                       | 154 ms: 1.03x faster                                                    |
| nbody                      | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| logging_silent             | 133 ns                                                       | 130 ns: 1.03x faster                                                    |
| deltablue                  | 3.88 ms                                                      | 3.77 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.37 ms: 1.03x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.4 ms: 1.02x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| regex_dna                  | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| logging_format             | 7.82 us                                                      | 7.69 us: 1.02x faster                                                   |
| hexiom                     | 7.08 ms                                                      | 6.98 ms: 1.01x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.7 ms: 1.01x faster                                                   |
| sqlglot_optimize           | 62.6 ms                                                      | 61.8 ms: 1.01x faster                                                   |
| regex_compile              | 128 ms                                                       | 126 ms: 1.01x faster                                                    |
| 2to3                       | 305 ms                                                       | 302 ms: 1.01x faster                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                  |
| bench_thread_pool          | 1.26 ms                                                      | 1.25 ms: 1.01x faster                                                   |
| spectral_norm              | 141 ms                                                       | 140 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.20 sec: 1.00x faster                                                  |
| pprint_pformat             | 1.93 sec                                                     | 1.92 sec: 1.00x faster                                                  |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.13 sec: 1.01x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 942 ms: 1.01x slower                                                    |
| sympy_str                  | 265 ms                                                       | 268 ms: 1.01x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                   |
| mako                       | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| sympy_expand               | 457 ms                                                       | 464 ms: 1.01x slower                                                    |
| mdp                        | 3.33 sec                                                     | 3.38 sec: 1.02x slower                                                  |
| float                      | 91.4 ms                                                      | 93.1 ms: 1.02x slower                                                   |
| fannkuch                   | 451 ms                                                       | 460 ms: 1.02x slower                                                    |
| json_loads                 | 32.1 us                                                      | 32.8 us: 1.02x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.81 ms: 1.02x slower                                                   |
| telco                      | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                   |
| pyflate                    | 557 ms                                                       | 577 ms: 1.04x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 201 us: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (34): create_gc_cycles, sqlglot_normalize, asyncio_tcp, async_generators, regex_effbot, xml_etree_parse, chaos, go, coverage, xml_etree_process, raytrace, pickle_pure_python, scimark_monte_carlo, thrift, bench_mp_pool, genshi_xml, scimark_fft, meteor_contest, pidigits, comprehensions, nqueens, crypto_pyaes, pycparser, unpickle_pure_python, bpe_tokeniser, html5lib, asyncio_websockets, genshi_text, sqlglot_parse, sympy_sum, sympy_integrate, django_template, json, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x