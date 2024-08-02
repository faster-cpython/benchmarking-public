# Results vs. 3.13.0b2

- fork: colesbury
- ref: gh_100240_freelist
- machine: linux-aarch64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.02x faster
- HPT reliability: 99.27%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 302 ms: 1.01x faster                                                     |
| html5lib       | 66.1 ms                                                      | 66.6 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 406 ms: 1.17x faster                                                     |
| async_tree_memoization     | 645 ms                                                       | 550 ms: 1.17x faster                                                     |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.15x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.08 sec: 1.13x faster                                                   |
| async_tree_memoization_tg  | 604 ms                                                       | 536 ms: 1.13x faster                                                     |
| async_tree_none            | 492 ms                                                       | 439 ms: 1.12x faster                                                     |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 724 ms: 1.09x faster                                                     |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 705 ms: 1.08x faster                                                     |
| Geometric mean             | (ref)                                                        | 1.13x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 112 ms: 1.02x faster                                                     |
| float          | 91.4 ms                                                      | 93.0 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                        | 1.00x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 250 ms: 1.03x faster                                                     |
| regex_effbot   | 4.98 ms                                                      | 4.87 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|---------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate  | 114 ms                                                       | 111 ms: 1.02x faster                                                     |
| tomli_loads         | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                   |
| json_loads          | 32.1 us                                                      | 32.3 us: 1.01x slower                                                    |
| json_dumps          | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                    |
| xml_etree_iterparse | 147 ms                                                       | 152 ms: 1.03x slower                                                     |
| Geometric mean      | (ref)                                                        | 1.00x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_process, pickle_pure_python, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                    |
| python_startup_no_site | 8.60 ms                                                      | 8.76 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 27.8 ms: 1.01x slower                                                    |
| mako           | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x slower                                                             |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 331 us: 1.36x faster                                                     |
| deepcopy_memo              | 50.8 us                                                      | 38.5 us: 1.32x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 406 ms: 1.17x faster                                                     |
| async_tree_memoization     | 645 ms                                                       | 550 ms: 1.17x faster                                                     |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.15x faster                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 3.51 us: 1.15x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.08 sec: 1.13x faster                                                   |
| async_tree_memoization_tg  | 604 ms                                                       | 536 ms: 1.13x faster                                                     |
| async_tree_none            | 492 ms                                                       | 439 ms: 1.12x faster                                                     |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 724 ms: 1.09x faster                                                     |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 705 ms: 1.08x faster                                                     |
| pathlib                    | 22.8 ms                                                      | 21.2 ms: 1.08x faster                                                    |
| richards                   | 55.9 ms                                                      | 52.8 ms: 1.06x faster                                                    |
| richards_super             | 62.3 ms                                                      | 59.0 ms: 1.06x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 4.93 ms: 1.05x faster                                                    |
| asyncio_tcp                | 584 ms                                                       | 560 ms: 1.04x faster                                                     |
| scimark_lu                 | 141 ms                                                       | 136 ms: 1.04x faster                                                     |
| regex_dna                  | 259 ms                                                       | 250 ms: 1.03x faster                                                     |
| regex_effbot               | 4.98 ms                                                      | 4.87 ms: 1.02x faster                                                    |
| nbody                      | 114 ms                                                       | 112 ms: 1.02x faster                                                     |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.41 ms: 1.02x faster                                                    |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.02x faster                                                     |
| bench_thread_pool          | 1.26 ms                                                      | 1.23 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.17 sec: 1.02x faster                                                   |
| pprint_pformat             | 1.93 sec                                                     | 1.90 sec: 1.01x faster                                                   |
| 2to3                       | 305 ms                                                       | 302 ms: 1.01x faster                                                     |
| scimark_fft                | 445 ms                                                       | 441 ms: 1.01x faster                                                     |
| tomli_loads                | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                   |
| mdp                        | 3.33 sec                                                     | 3.31 sec: 1.01x faster                                                   |
| json_loads                 | 32.1 us                                                      | 32.3 us: 1.01x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 66.6 ms: 1.01x slower                                                    |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 27.8 ms: 1.01x slower                                                    |
| mako                       | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                    |
| coverage                   | 98.4 ms                                                      | 100.0 ms: 1.02x slower                                                   |
| float                      | 91.4 ms                                                      | 93.0 ms: 1.02x slower                                                    |
| generators                 | 37.1 ms                                                      | 37.8 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.76 ms: 1.02x slower                                                    |
| fannkuch                   | 451 ms                                                       | 461 ms: 1.02x slower                                                     |
| typing_runtime_protocols   | 193 us                                                       | 200 us: 1.03x slower                                                     |
| xml_etree_iterparse        | 147 ms                                                       | 152 ms: 1.03x slower                                                     |
| nqueens                    | 98.9 ms                                                      | 103 ms: 1.04x slower                                                     |
| dulwich_log                | 58.5 ms                                                      | 61.2 ms: 1.05x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                             |

Benchmark hidden because not significant (46): tornado_http, logging_simple, create_gc_cycles, sqlglot_parse, meteor_contest, xml_etree_process, deltablue, telco, logging_format, pylint, docutils, coroutines, hexiom, spectral_norm, chaos, crypto_pyaes, bench_mp_pool, async_generators, scimark_sor, pprint_safe_repr, go, sympy_expand, pidigits, bpe_tokeniser, sqlglot_normalize, genshi_xml, pickle_pure_python, logging_silent, scimark_monte_carlo, regex_v8, raytrace, unpickle_pure_python, thrift, sympy_str, pyflate, sqlglot_transpile, pycparser, sympy_integrate, asyncio_websockets, comprehensions, json, regex_compile, django_template, sqlglot_optimize, sympy_sum, xml_etree_parse
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.27% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x