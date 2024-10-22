# Results vs. 3.13.0

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: linux-aarch64
- commit hash: 1ba3555
- commit date: 2024-09-30
- overall geometric mean: 1.00x slower
- HPT reliability: 71.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| tornado_http   | 131 ms                                                   | 126 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (4): 2to3, chameleon, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_generators          | 496 ms                                                   | 488 ms: 1.02x faster                                                     |
| async_tree_none_tg        | 467 ms                                                   | 460 ms: 1.02x faster                                                     |
| async_tree_none           | 493 ms                                                   | 486 ms: 1.02x faster                                                     |
| async_tree_memoization_tg | 649 ms                                                   | 645 ms: 1.01x faster                                                     |
| asyncio_websockets        | 656 ms                                                   | 662 ms: 1.01x slower                                                     |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_io_tg, asyncio_tcp, async_tree_cpu_io_mixed, asyncio_tcp_ssl, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 93.5 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.1 ms: 1.05x faster                                                    |
| regex_dna      | 246 ms                                                   | 252 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads         | 2.53 sec                                                 | 2.56 sec: 1.01x slower                                                   |
| xml_etree_iterparse | 147 ms                                                   | 150 ms: 1.02x slower                                                     |
| xml_etree_parse     | 188 ms                                                   | 200 ms: 1.06x slower                                                     |
| Geometric mean      | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (11): pickle_dict, xml_etree_process, pickle_list, unpickle_pure_python, json_dumps, unpickle_list, pickle, unpickle, xml_etree_generate, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 42.3 ms                                                  | 41.5 ms: 1.02x faster                                                    |
| mako            | 13.3 ms                                                  | 13.3 ms: 1.00x faster                                                    |
| Geometric mean  | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-arminc-aarch64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8                  | 31.5 ms                                                  | 30.1 ms: 1.05x faster                                                    |
| tornado_http              | 131 ms                                                   | 126 ms: 1.04x faster                                                     |
| deepcopy_memo             | 51.0 us                                                  | 50.0 us: 1.02x faster                                                    |
| django_template           | 42.3 ms                                                  | 41.5 ms: 1.02x faster                                                    |
| async_generators          | 496 ms                                                   | 488 ms: 1.02x faster                                                     |
| async_tree_none_tg        | 467 ms                                                   | 460 ms: 1.02x faster                                                     |
| async_tree_none           | 493 ms                                                   | 486 ms: 1.02x faster                                                     |
| hexiom                    | 7.13 ms                                                  | 7.05 ms: 1.01x faster                                                    |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.52 ms: 1.01x faster                                                    |
| float                     | 94.4 ms                                                  | 93.5 ms: 1.01x faster                                                    |
| scimark_fft               | 447 ms                                                   | 444 ms: 1.01x faster                                                     |
| async_tree_memoization_tg | 649 ms                                                   | 645 ms: 1.01x faster                                                     |
| mako                      | 13.3 ms                                                  | 13.3 ms: 1.00x faster                                                    |
| logging_simple            | 7.04 us                                                  | 7.02 us: 1.00x faster                                                    |
| sqlite_synth              | 3.84 us                                                  | 3.87 us: 1.01x slower                                                    |
| asyncio_websockets        | 656 ms                                                   | 662 ms: 1.01x slower                                                     |
| pyflate                   | 556 ms                                                   | 561 ms: 1.01x slower                                                     |
| pathlib                   | 22.4 ms                                                  | 22.7 ms: 1.01x slower                                                    |
| tomli_loads               | 2.53 sec                                                 | 2.56 sec: 1.01x slower                                                   |
| thrift                    | 946 us                                                   | 960 us: 1.02x slower                                                     |
| deepcopy_reduce           | 4.07 us                                                  | 4.13 us: 1.02x slower                                                    |
| json                      | 5.61 ms                                                  | 5.70 ms: 1.02x slower                                                    |
| xml_etree_iterparse       | 147 ms                                                   | 150 ms: 1.02x slower                                                     |
| regex_dna                 | 246 ms                                                   | 252 ms: 1.02x slower                                                     |
| unpack_sequence           | 57.2 ns                                                  | 59.3 ns: 1.04x slower                                                    |
| bench_mp_pool             | 7.30 ms                                                  | 7.65 ms: 1.05x slower                                                    |
| xml_etree_parse           | 188 ms                                                   | 200 ms: 1.06x slower                                                     |
| Geometric mean            | (ref)                                                    | 1.00x slower                                                             |

Benchmark hidden because not significant (75): async_tree_memoization, sqlglot_normalize, aiohttp, sympy_integrate, pickle_dict, xml_etree_process, async_tree_io, nqueens, async_tree_cpu_io_mixed_tg, pickle_list, chaos, sympy_sum, nbody, sqlglot_transpile, async_tree_io_tg, crypto_pyaes, unpickle_pure_python, docutils, sqlglot_parse, logging_format, json_dumps, mdp, scimark_monte_carlo, comprehensions, logging_silent, unpickle_list, pickle, unpickle, asyncio_tcp, 2to3, gc_traversal, mypy2, bench_thread_pool, fannkuch, async_tree_cpu_io_mixed, go, richards_super, meteor_contest, generators, deepcopy, pidigits, genshi_text, xml_etree_generate, raytrace, scimark_sor, coverage, deltablue, pprint_pformat, scimark_lu, python_startup_no_site, pycparser, dask, spectral_norm, bpe_tokeniser, asyncio_tcp_ssl, create_gc_cycles, pprint_safe_repr, sympy_expand, telco, richards, sympy_str, genshi_xml, flaskblogging, json_loads, python_startup, regex_compile, regex_effbot, typing_runtime_protocols, sqlglot_optimize, pylint, chameleon, coroutines, pickle_pure_python, gunicorn, html5lib

# HPT report

- Reliability score: 71.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x