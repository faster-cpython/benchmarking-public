# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-aarch64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.00x faster
- HPT reliability: 99.68%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| chameleon      | 8.95 ms                                                      | 9.16 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 91.9 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 250 ms: 1.03x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 129 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|---------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                                  |
| unpickle            | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| pickle_dict         | 37.6 us                                                      | 37.3 us: 1.01x faster                                                   |
| pickle_list         | 5.27 us                                                      | 5.24 us: 1.01x faster                                                   |
| json_dumps          | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| pickle              | 13.4 us                                                      | 13.6 us: 1.02x slower                                                   |
| xml_etree_iterparse | 147 ms                                                       | 153 ms: 1.05x slower                                                    |
| Geometric mean      | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (7): xml_etree_parse, xml_etree_generate, unpickle_pure_python, json_loads, xml_etree_process, pickle_pure_python, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 12.6 ms: 1.03x faster                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.41 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 41.6 ms: 1.02x faster                                                   |
| mako            | 13.2 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 27.9 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pathlib                  | 22.8 ms                                                      | 21.4 ms: 1.07x faster                                                   |
| richards                 | 55.9 ms                                                      | 53.7 ms: 1.04x faster                                                   |
| regex_dna                | 259 ms                                                       | 250 ms: 1.03x faster                                                    |
| python_startup           | 13.0 ms                                                      | 12.6 ms: 1.03x faster                                                   |
| richards_super           | 62.3 ms                                                      | 60.4 ms: 1.03x faster                                                   |
| scimark_lu               | 141 ms                                                       | 137 ms: 1.03x faster                                                    |
| python_startup_no_site   | 8.60 ms                                                      | 8.41 ms: 1.02x faster                                                   |
| asyncio_tcp              | 584 ms                                                       | 573 ms: 1.02x faster                                                    |
| regex_effbot             | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                   |
| sqlite_synth             | 3.90 us                                                      | 3.84 us: 1.02x faster                                                   |
| telco                    | 10.0 ms                                                      | 9.85 ms: 1.02x faster                                                   |
| django_template          | 42.3 ms                                                      | 41.6 ms: 1.02x faster                                                   |
| tomli_loads              | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                                  |
| scimark_monte_carlo      | 82.3 ms                                                      | 81.1 ms: 1.01x faster                                                   |
| unpickle                 | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| deepcopy_memo            | 50.8 us                                                      | 50.1 us: 1.01x faster                                                   |
| pprint_pformat           | 1.93 sec                                                     | 1.91 sec: 1.01x faster                                                  |
| pickle_dict              | 37.6 us                                                      | 37.3 us: 1.01x faster                                                   |
| pickle_list              | 5.27 us                                                      | 5.24 us: 1.01x faster                                                   |
| float                    | 91.4 ms                                                      | 91.9 ms: 1.00x slower                                                   |
| bench_thread_pool        | 1.26 ms                                                      | 1.27 ms: 1.01x slower                                                   |
| mako                     | 13.2 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| sympy_str                | 265 ms                                                       | 268 ms: 1.01x slower                                                    |
| sqlglot_transpile        | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                   |
| regex_compile            | 128 ms                                                       | 129 ms: 1.01x slower                                                    |
| json_dumps               | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| generators               | 37.1 ms                                                      | 37.6 ms: 1.01x slower                                                   |
| asyncio_websockets       | 657 ms                                                       | 666 ms: 1.01x slower                                                    |
| scimark_sparse_mat_mult  | 6.55 ms                                                      | 6.65 ms: 1.02x slower                                                   |
| genshi_text              | 27.4 ms                                                      | 27.9 ms: 1.02x slower                                                   |
| fannkuch                 | 451 ms                                                       | 460 ms: 1.02x slower                                                    |
| sympy_integrate          | 20.9 ms                                                      | 21.3 ms: 1.02x slower                                                   |
| pickle                   | 13.4 us                                                      | 13.6 us: 1.02x slower                                                   |
| chameleon                | 8.95 ms                                                      | 9.16 ms: 1.02x slower                                                   |
| typing_runtime_protocols | 193 us                                                       | 200 us: 1.03x slower                                                    |
| xml_etree_iterparse      | 147 ms                                                       | 153 ms: 1.05x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (62): async_tree_none_tg, async_tree_io, sqlglot_parse, logging_simple, sqlglot_normalize, meteor_contest, nqueens, async_generators, async_tree_cpu_io_mixed, nbody, async_tree_cpu_io_mixed_tg, comprehensions, async_tree_memoization_tg, sqlglot_optimize, async_tree_io_tg, regex_v8, logging_format, deepcopy, dask, xml_etree_parse, async_tree_none, chaos, coverage, xml_etree_generate, deepcopy_reduce, html5lib, spectral_norm, pprint_safe_repr, go, mdp, docutils, asyncio_tcp_ssl, bench_mp_pool, hexiom, coroutines, scimark_sor, pyflate, unpickle_pure_python, raytrace, crypto_pyaes, pidigits, scimark_fft, json_loads, async_tree_memoization, 2to3, pycparser, deltablue, sympy_sum, xml_etree_process, thrift, json, pickle_pure_python, sympy_expand, genshi_xml, flaskblogging, logging_silent, gc_traversal, unpickle_list, pylint, dulwich_log, tornado_http, create_gc_cycles
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 99.68% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x