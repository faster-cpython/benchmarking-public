# Results vs. base

- fork: PeterYang12
- ref: accelerate_DJBX33A
- machine: linux-aarch64
- commit hash: bf9cfa8
- commit date: 2024-08-24
- overall geometric mean: 1.00x slower
- HPT reliability: 94.66%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                                                | 1.14 sec: 1.02x faster                                                     |
| async_tree_cpu_io_mixed_tg | 719 ms                                                                  | 730 ms: 1.02x slower                                                       |
| async_tree_memoization     | 554 ms                                                                  | 563 ms: 1.02x slower                                                       |
| async_tree_none            | 420 ms                                                                  | 433 ms: 1.03x slower                                                       |
| asyncio_tcp_ssl            | 2.17 sec                                                                | 2.24 sec: 1.03x slower                                                     |
| asyncio_tcp                | 550 ms                                                                  | 573 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                                   | 1.01x slower                                                               |

Benchmark hidden because not significant (7): async_tree_memoization_tg, asyncio_websockets, async_tree_cpu_io_mixed, coroutines, async_generators, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 92.5 ms                                                                 | 91.2 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                               |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 30.7 ms                                                                 | 30.0 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                               |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|---------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse | 147 ms                                                                  | 146 ms: 1.01x faster                                                       |
| pickle_pure_python  | 356 us                                                                  | 365 us: 1.03x slower                                                       |
| Geometric mean      | (ref)                                                                   | 1.00x faster                                                               |

Benchmark hidden because not significant (7): xml_etree_generate, xml_etree_parse, json_loads, json_dumps, tomli_loads, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.77 ms                                                                 | 8.74 ms: 1.00x faster                                                      |
| Geometric mean         | (ref)                                                                   | 1.00x faster                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|-----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 42.2 ms                                                                 | 41.8 ms: 1.01x faster                                                      |
| genshi_text     | 27.2 ms                                                                 | 27.3 ms: 1.00x slower                                                      |
| Geometric mean  | (ref)                                                                   | 1.00x faster                                                               |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240825-arminc-aarch64-python-9b3749849eda4012261a-3.14.0a0-9b37498 | bm-20240824-arminc-aarch64-PeterYang12-accelerate_DJBX33A-3.14.0a0-bf9cfa8 |
|----------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pyflate                    | 574 ms                                                                  | 559 ms: 1.03x faster                                                       |
| create_gc_cycles           | 2.32 ms                                                                 | 2.26 ms: 1.03x faster                                                      |
| meteor_contest             | 113 ms                                                                  | 110 ms: 1.02x faster                                                       |
| regex_v8                   | 30.7 ms                                                                 | 30.0 ms: 1.02x faster                                                      |
| async_tree_io              | 1.16 sec                                                                | 1.14 sec: 1.02x faster                                                     |
| float                      | 92.5 ms                                                                 | 91.2 ms: 1.01x faster                                                      |
| sqlglot_transpile          | 1.74 ms                                                                 | 1.72 ms: 1.01x faster                                                      |
| xml_etree_iterparse        | 147 ms                                                                  | 146 ms: 1.01x faster                                                       |
| django_template            | 42.2 ms                                                                 | 41.8 ms: 1.01x faster                                                      |
| bpe_tokeniser              | 5.87 sec                                                                | 5.83 sec: 1.01x faster                                                     |
| python_startup_no_site     | 8.77 ms                                                                 | 8.74 ms: 1.00x faster                                                      |
| hexiom                     | 6.97 ms                                                                 | 6.97 ms: 1.00x faster                                                      |
| genshi_text                | 27.2 ms                                                                 | 27.3 ms: 1.00x slower                                                      |
| sqlglot_parse              | 1.39 ms                                                                 | 1.40 ms: 1.01x slower                                                      |
| pprint_pformat             | 1.86 sec                                                                | 1.88 sec: 1.01x slower                                                     |
| scimark_lu                 | 134 ms                                                                  | 136 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 915 ms                                                                  | 927 ms: 1.01x slower                                                       |
| scimark_monte_carlo        | 81.0 ms                                                                 | 82.0 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 719 ms                                                                  | 730 ms: 1.02x slower                                                       |
| async_tree_memoization     | 554 ms                                                                  | 563 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 6.37 ms                                                                 | 6.48 ms: 1.02x slower                                                      |
| deepcopy_memo              | 37.5 us                                                                 | 38.2 us: 1.02x slower                                                      |
| deepcopy_reduce            | 3.49 us                                                                 | 3.57 us: 1.02x slower                                                      |
| thrift                     | 918 us                                                                  | 939 us: 1.02x slower                                                       |
| pickle_pure_python         | 356 us                                                                  | 365 us: 1.03x slower                                                       |
| async_tree_none            | 420 ms                                                                  | 433 ms: 1.03x slower                                                       |
| asyncio_tcp_ssl            | 2.17 sec                                                                | 2.24 sec: 1.03x slower                                                     |
| telco                      | 9.64 ms                                                                 | 9.97 ms: 1.03x slower                                                      |
| asyncio_tcp                | 550 ms                                                                  | 573 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                                   | 1.00x slower                                                               |

Benchmark hidden because not significant (60): sqlglot_normalize, html5lib, xml_etree_generate, gc_traversal, richards, json, xml_etree_parse, pylint, regex_dna, pathlib, scimark_sor, sympy_sum, typing_runtime_protocols, json_loads, logging_silent, python_startup, json_dumps, async_tree_memoization_tg, crypto_pyaes, pidigits, sqlglot_optimize, mako, bench_mp_pool, docutils, regex_effbot, asyncio_websockets, sympy_integrate, tomli_loads, mdp, comprehensions, generators, spectral_norm, unpickle_pure_python, chaos, go, async_tree_cpu_io_mixed, deepcopy, nbody, genshi_xml, xml_etree_process, 2to3, richards_super, fannkuch, sympy_expand, bench_thread_pool, logging_format, raytrace, sympy_str, pycparser, nqueens, scimark_fft, coroutines, deltablue, async_generators, logging_simple, tornado_http, coverage, async_tree_none_tg, async_tree_io_tg, regex_compile

# HPT report

- Reliability score: 94.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x