# Results vs. 3.13.0b2

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: linux-aarch64
- commit hash: 1ba3555
- commit date: 2024-09-30
- overall geometric mean: 1.00x faster
- HPT reliability: 91.04%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| chameleon      | 8.95 ms                                                      | 9.12 ms: 1.02x slower                                                    |
| docutils       | 3.10 sec                                                     | 2.89 sec: 1.07x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.08 sec: 1.17x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.10 sec: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 730 ms: 1.05x faster                                                     |
| async_tree_memoization     | 645 ms                                                       | 617 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 763 ms: 1.04x faster                                                     |
| async_tree_none_tg         | 476 ms                                                       | 460 ms: 1.04x faster                                                     |
| async_tree_none            | 492 ms                                                       | 486 ms: 1.01x faster                                                     |
| async_tree_memoization_tg  | 604 ms                                                       | 645 ms: 1.07x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 93.5 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x slower                                                             |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.1 ms: 1.03x faster                                                    |
| regex_dna      | 259 ms                                                       | 252 ms: 1.03x faster                                                     |
| regex_effbot   | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|---------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_process   | 80.8 ms                                                      | 79.3 ms: 1.02x faster                                                    |
| json_loads          | 32.1 us                                                      | 31.7 us: 1.01x faster                                                    |
| json_dumps          | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                    |
| unpickle            | 19.8 us                                                      | 20.1 us: 1.02x slower                                                    |
| unpickle_list       | 6.52 us                                                      | 6.63 us: 1.02x slower                                                    |
| xml_etree_iterparse | 147 ms                                                       | 150 ms: 1.02x slower                                                     |
| xml_etree_parse     | 191 ms                                                       | 200 ms: 1.04x slower                                                     |
| Geometric mean      | (ref)                                                        | 1.01x slower                                                             |

Benchmark hidden because not significant (7): xml_etree_generate, tomli_loads, pickle_dict, pickle, pickle_list, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.78 ms: 1.02x slower                                                    |
| python_startup         | 13.0 ms                                                      | 13.4 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.03x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 41.5 ms: 1.02x faster                                                    |
| mako            | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 27.7 ms: 1.01x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.08 sec: 1.17x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 4.52 ms: 1.14x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.10 sec: 1.12x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 2.13 ms: 1.09x faster                                                    |
| docutils                   | 3.10 sec                                                     | 2.89 sec: 1.07x faster                                                   |
| dask                       | 370 ms                                                       | 352 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 730 ms: 1.05x faster                                                     |
| async_tree_memoization     | 645 ms                                                       | 617 ms: 1.05x faster                                                     |
| richards                   | 55.9 ms                                                      | 53.8 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 763 ms: 1.04x faster                                                     |
| async_tree_none_tg         | 476 ms                                                       | 460 ms: 1.04x faster                                                     |
| richards_super             | 62.3 ms                                                      | 60.3 ms: 1.03x faster                                                    |
| asyncio_tcp                | 584 ms                                                       | 566 ms: 1.03x faster                                                     |
| regex_v8                   | 31.1 ms                                                      | 30.1 ms: 1.03x faster                                                    |
| regex_dna                  | 259 ms                                                       | 252 ms: 1.03x faster                                                     |
| logging_simple             | 7.21 us                                                      | 7.02 us: 1.03x faster                                                    |
| telco                      | 10.0 ms                                                      | 9.78 ms: 1.02x faster                                                    |
| django_template            | 42.3 ms                                                      | 41.5 ms: 1.02x faster                                                    |
| xml_etree_process          | 80.8 ms                                                      | 79.3 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.90 sec: 1.01x faster                                                   |
| deepcopy_memo              | 50.8 us                                                      | 50.0 us: 1.01x faster                                                    |
| json_loads                 | 32.1 us                                                      | 31.7 us: 1.01x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                                    |
| async_tree_none            | 492 ms                                                       | 486 ms: 1.01x faster                                                     |
| scimark_lu                 | 141 ms                                                       | 140 ms: 1.01x faster                                                     |
| nqueens                    | 98.9 ms                                                      | 97.8 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.19 sec: 1.01x faster                                                   |
| sqlite_synth               | 3.90 us                                                      | 3.87 us: 1.01x faster                                                    |
| mdp                        | 3.33 sec                                                     | 3.35 sec: 1.01x slower                                                   |
| pyflate                    | 557 ms                                                       | 561 ms: 1.01x slower                                                     |
| mako                       | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 27.7 ms: 1.01x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.27 ms: 1.01x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 83.5 ms: 1.01x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                    |
| bpe_tokeniser              | 5.83 sec                                                     | 5.92 sec: 1.02x slower                                                   |
| unpickle                   | 19.8 us                                                      | 20.1 us: 1.02x slower                                                    |
| unpickle_list              | 6.52 us                                                      | 6.63 us: 1.02x slower                                                    |
| chameleon                  | 8.95 ms                                                      | 9.12 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.78 ms: 1.02x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                       | 150 ms: 1.02x slower                                                     |
| float                      | 91.4 ms                                                      | 93.5 ms: 1.02x slower                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 4.13 us: 1.02x slower                                                    |
| python_startup             | 13.0 ms                                                      | 13.4 ms: 1.03x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.27 sec: 1.04x slower                                                   |
| xml_etree_parse            | 191 ms                                                       | 200 ms: 1.04x slower                                                     |
| async_tree_memoization_tg  | 604 ms                                                       | 645 ms: 1.07x slower                                                     |
| bench_mp_pool              | 7.03 ms                                                      | 7.65 ms: 1.09x slower                                                    |
| mypy2                      | 767 ms                                                       | 1.18 sec: 1.54x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                             |

Benchmark hidden because not significant (52): sqlglot_parse, sqlglot_normalize, tornado_http, coroutines, flaskblogging, comprehensions, sympy_sum, nbody, scimark_sparse_mat_mult, sympy_integrate, deltablue, logging_format, hexiom, pprint_safe_repr, xml_etree_generate, scimark_fft, tomli_loads, pathlib, sympy_expand, scimark_sor, thrift, aiohttp, meteor_contest, sympy_str, fannkuch, pidigits, async_generators, typing_runtime_protocols, 2to3, chaos, crypto_pyaes, spectral_norm, pickle_dict, coverage, html5lib, pickle, genshi_xml, sqlglot_optimize, raytrace, pickle_list, sqlglot_transpile, unpickle_pure_python, deepcopy, asyncio_websockets, go, logging_silent, json, regex_compile, pickle_pure_python, generators, pylint, gunicorn
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: dulwich_log
Ignored benchmarks (1) of results/bm-20240930-3.13.0rc2+-1ba3555/bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555.json: unpack_sequence

# HPT report

- Reliability score: 91.04% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x