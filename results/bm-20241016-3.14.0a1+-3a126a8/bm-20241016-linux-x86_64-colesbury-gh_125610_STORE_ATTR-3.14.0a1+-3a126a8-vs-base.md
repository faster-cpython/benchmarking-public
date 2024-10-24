# Results vs. base

- fork: colesbury
- ref: gh_125610_STORE_ATTR
- machine: linux-x86_64
- commit hash: 3a126a8
- commit date: 2024-10-16
- overall geometric mean: 1.00x slower
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 254 ms: 1.00x slower                                                      |
| html5lib       | 61.9 ms                                                                | 63.0 ms: 1.02x slower                                                     |
| tornado_http   | 89.8 ms                                                                | 90.2 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_generators | 431 ms                                                                 | 434 ms: 1.01x slower                                                      |
| coroutines       | 23.2 ms                                                                | 23.6 ms: 1.02x slower                                                     |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (9): async_tree_memoization_tg, async_tree_io, async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                                | 89.3 ms: 1.02x faster                                                     |
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x slower                                                      |
| float          | 78.1 ms                                                                | 78.7 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                                | 24.6 ms: 1.02x faster                                                     |
| regex_compile  | 128 ms                                                                 | 129 ms: 1.00x slower                                                      |
| regex_effbot   | 3.49 ms                                                                | 3.61 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                                 | 217 us: 1.00x slower                                                      |
| json_loads           | 26.8 us                                                                | 27.0 us: 1.01x slower                                                     |
| json_dumps           | 11.2 ms                                                                | 11.5 ms: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (6): xml_etree_generate, tomli_loads, xml_etree_iterparse, xml_etree_process, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.03 ms                                                                | 7.04 ms: 1.00x slower                                                     |
| python_startup         | 11.8 ms                                                                | 11.8 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako           | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                                     |
| genshi_text    | 22.3 ms                                                                | 22.9 ms: 1.02x slower                                                     |
| genshi_xml     | 50.1 ms                                                                | 51.3 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20241016-linux-x86_64-python-760872efecb95017db8e-3.14.0a1+-760872e | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8                 | 25.1 ms                                                                | 24.6 ms: 1.02x faster                                                     |
| logging_format           | 6.16 us                                                                | 6.05 us: 1.02x faster                                                     |
| comprehensions           | 16.9 us                                                                | 16.6 us: 1.02x faster                                                     |
| nbody                    | 90.7 ms                                                                | 89.3 ms: 1.02x faster                                                     |
| bpe_tokeniser            | 4.86 sec                                                               | 4.78 sec: 1.02x faster                                                    |
| scimark_sparse_mat_mult  | 4.87 ms                                                                | 4.80 ms: 1.01x faster                                                     |
| richards_super           | 52.7 ms                                                                | 52.2 ms: 1.01x faster                                                     |
| telco                    | 7.92 ms                                                                | 7.86 ms: 1.01x faster                                                     |
| coverage                 | 84.4 ms                                                                | 83.8 ms: 1.01x faster                                                     |
| scimark_fft              | 366 ms                                                                 | 363 ms: 1.01x faster                                                      |
| richards                 | 46.5 ms                                                                | 46.1 ms: 1.01x faster                                                     |
| meteor_contest           | 108 ms                                                                 | 107 ms: 1.01x faster                                                      |
| hexiom                   | 6.26 ms                                                                | 6.23 ms: 1.01x faster                                                     |
| scimark_lu               | 115 ms                                                                 | 114 ms: 1.00x faster                                                      |
| sqlglot_normalize        | 106 ms                                                                 | 106 ms: 1.00x faster                                                      |
| gc_traversal             | 4.38 ms                                                                | 4.37 ms: 1.00x faster                                                     |
| sqlglot_optimize         | 53.2 ms                                                                | 53.1 ms: 1.00x faster                                                     |
| create_gc_cycles         | 2.66 ms                                                                | 2.66 ms: 1.00x faster                                                     |
| 2to3                     | 254 ms                                                                 | 254 ms: 1.00x slower                                                      |
| pidigits                 | 187 ms                                                                 | 187 ms: 1.00x slower                                                      |
| python_startup_no_site   | 7.03 ms                                                                | 7.04 ms: 1.00x slower                                                     |
| bench_thread_pool        | 836 us                                                                 | 838 us: 1.00x slower                                                      |
| sympy_integrate          | 19.8 ms                                                                | 19.8 ms: 1.00x slower                                                     |
| fannkuch                 | 404 ms                                                                 | 406 ms: 1.00x slower                                                      |
| python_startup           | 11.8 ms                                                                | 11.8 ms: 1.00x slower                                                     |
| regex_compile            | 128 ms                                                                 | 129 ms: 1.00x slower                                                      |
| unpickle_pure_python     | 216 us                                                                 | 217 us: 1.00x slower                                                      |
| json_loads               | 26.8 us                                                                | 27.0 us: 1.01x slower                                                     |
| tornado_http             | 89.8 ms                                                                | 90.2 ms: 1.01x slower                                                     |
| pprint_safe_repr         | 726 ms                                                                 | 730 ms: 1.01x slower                                                      |
| typing_runtime_protocols | 159 us                                                                 | 160 us: 1.01x slower                                                      |
| pprint_pformat           | 1.48 sec                                                               | 1.49 sec: 1.01x slower                                                    |
| chaos                    | 59.6 ms                                                                | 59.9 ms: 1.01x slower                                                     |
| sympy_sum                | 146 ms                                                                 | 147 ms: 1.01x slower                                                      |
| mako                     | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                                     |
| async_generators         | 431 ms                                                                 | 434 ms: 1.01x slower                                                      |
| float                    | 78.1 ms                                                                | 78.7 ms: 1.01x slower                                                     |
| sqlglot_transpile        | 1.58 ms                                                                | 1.59 ms: 1.01x slower                                                     |
| bench_mp_pool            | 77.9 ms                                                                | 78.5 ms: 1.01x slower                                                     |
| dulwich_log              | 63.0 ms                                                                | 63.6 ms: 1.01x slower                                                     |
| sqlglot_parse            | 1.28 ms                                                                | 1.29 ms: 1.01x slower                                                     |
| raytrace                 | 264 ms                                                                 | 266 ms: 1.01x slower                                                      |
| go                       | 118 ms                                                                 | 120 ms: 1.01x slower                                                      |
| json                     | 5.04 ms                                                                | 5.10 ms: 1.01x slower                                                     |
| crypto_pyaes             | 71.5 ms                                                                | 72.4 ms: 1.01x slower                                                     |
| pathlib                  | 15.9 ms                                                                | 16.1 ms: 1.01x slower                                                     |
| generators               | 27.2 ms                                                                | 27.7 ms: 1.02x slower                                                     |
| html5lib                 | 61.9 ms                                                                | 63.0 ms: 1.02x slower                                                     |
| coroutines               | 23.2 ms                                                                | 23.6 ms: 1.02x slower                                                     |
| thrift                   | 765 us                                                                 | 782 us: 1.02x slower                                                      |
| genshi_text              | 22.3 ms                                                                | 22.9 ms: 1.02x slower                                                     |
| genshi_xml               | 50.1 ms                                                                | 51.3 ms: 1.02x slower                                                     |
| json_dumps               | 11.2 ms                                                                | 11.5 ms: 1.03x slower                                                     |
| nqueens                  | 80.3 ms                                                                | 82.7 ms: 1.03x slower                                                     |
| regex_effbot             | 3.49 ms                                                                | 3.61 ms: 1.03x slower                                                     |
| spectral_norm            | 112 ms                                                                 | 115 ms: 1.03x slower                                                      |
| pyflate                  | 453 ms                                                                 | 480 ms: 1.06x slower                                                      |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (32): logging_silent, django_template, deltablue, async_tree_memoization_tg, deepcopy_memo, pycparser, deepcopy, xml_etree_generate, mdp, tomli_loads, xml_etree_iterparse, deepcopy_reduce, logging_simple, async_tree_io, xml_etree_process, async_tree_none_tg, scimark_sor, asyncio_websockets, docutils, pylint, pickle_pure_python, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, sympy_expand, regex_dna, sphinx, async_tree_io_tg, scimark_monte_carlo, sympy_str, async_tree_none, async_tree_memoization, xml_etree_parse

# HPT report

- Reliability score: 99.93% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x