# Results vs. base

- fork: colesbury
- ref: gh_117376_pydecref_m
- machine: linux-aarch64
- commit hash: 4b27f3a
- commit date: 2024-08-13
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 517 ms                                                                  | 513 ms: 1.01x faster                                                       |
| docutils       | 4.11 sec                                                                | 4.09 sec: 1.01x faster                                                     |
| html5lib       | 121 ms                                                                  | 120 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|---------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp_ssl           | 2.59 sec                                                                | 2.43 sec: 1.06x faster                                                     |
| asyncio_tcp               | 684 ms                                                                  | 661 ms: 1.04x faster                                                       |
| coroutines                | 40.0 ms                                                                 | 39.1 ms: 1.02x faster                                                      |
| async_tree_memoization_tg | 695 ms                                                                  | 683 ms: 1.02x faster                                                       |
| async_tree_none_tg        | 565 ms                                                                  | 557 ms: 1.01x faster                                                       |
| async_tree_memoization    | 746 ms                                                                  | 739 ms: 1.01x faster                                                       |
| asyncio_websockets        | 675 ms                                                                  | 668 ms: 1.01x faster                                                       |
| async_tree_io             | 1.41 sec                                                                | 1.40 sec: 1.01x faster                                                     |
| async_tree_io_tg          | 1.35 sec                                                                | 1.34 sec: 1.01x faster                                                     |
| Geometric mean            | (ref)                                                                   | 1.02x faster                                                               |

Benchmark hidden because not significant (4): async_generators, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 286 ms                                                                  | 281 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                               |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 258 ms                                                                  | 254 ms: 1.02x faster                                                       |
| regex_effbot   | 4.41 ms                                                                 | 4.51 ms: 1.02x slower                                                      |
| regex_dna      | 249 ms                                                                  | 259 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark       | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse | 188 ms                                                                  | 183 ms: 1.03x faster                                                       |
| tomli_loads     | 4.23 sec                                                                | 4.20 sec: 1.01x faster                                                     |
| Geometric mean  | (ref)                                                                   | 1.01x faster                                                               |

Benchmark hidden because not significant (7): xml_etree_iterparse, xml_etree_process, unpickle_pure_python, xml_etree_generate, json_dumps, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 12.1 ms                                                                 | 11.9 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                                   | 1.02x faster                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-----------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 84.2 ms                                                                 | 82.2 ms: 1.02x faster                                                      |
| genshi_xml      | 106 ms                                                                  | 104 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                                   | 1.01x faster                                                               |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|---------------------------|:-----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp_ssl           | 2.59 sec                                                                | 2.43 sec: 1.06x faster                                                     |
| asyncio_tcp               | 684 ms                                                                  | 661 ms: 1.04x faster                                                       |
| logging_simple            | 14.8 us                                                                 | 14.4 us: 1.03x faster                                                      |
| sqlglot_parse             | 3.71 ms                                                                 | 3.59 ms: 1.03x faster                                                      |
| bench_mp_pool             | 7.13 ms                                                                 | 6.91 ms: 1.03x faster                                                      |
| logging_format            | 16.1 us                                                                 | 15.6 us: 1.03x faster                                                      |
| coverage                  | 136 ms                                                                  | 132 ms: 1.03x faster                                                       |
| xml_etree_parse           | 188 ms                                                                  | 183 ms: 1.03x faster                                                       |
| logging_silent            | 286 ns                                                                  | 279 ns: 1.03x faster                                                       |
| spectral_norm             | 233 ms                                                                  | 227 ms: 1.02x faster                                                       |
| django_template           | 84.2 ms                                                                 | 82.2 ms: 1.02x faster                                                      |
| coroutines                | 40.0 ms                                                                 | 39.1 ms: 1.02x faster                                                      |
| scimark_monte_carlo       | 177 ms                                                                  | 173 ms: 1.02x faster                                                       |
| python_startup_no_site    | 12.1 ms                                                                 | 11.9 ms: 1.02x faster                                                      |
| richards                  | 118 ms                                                                  | 116 ms: 1.02x faster                                                       |
| regex_compile             | 258 ms                                                                  | 254 ms: 1.02x faster                                                       |
| sqlglot_normalize         | 235 ms                                                                  | 230 ms: 1.02x faster                                                       |
| pathlib                   | 26.9 ms                                                                 | 26.4 ms: 1.02x faster                                                      |
| fannkuch                  | 751 ms                                                                  | 738 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult   | 8.95 ms                                                                 | 8.79 ms: 1.02x faster                                                      |
| raytrace                  | 816 ms                                                                  | 803 ms: 1.02x faster                                                       |
| async_tree_memoization_tg | 695 ms                                                                  | 683 ms: 1.02x faster                                                       |
| pprint_safe_repr          | 1.78 sec                                                                | 1.75 sec: 1.02x faster                                                     |
| nbody                     | 286 ms                                                                  | 281 ms: 1.02x faster                                                       |
| scimark_fft               | 580 ms                                                                  | 572 ms: 1.01x faster                                                       |
| async_tree_none_tg        | 565 ms                                                                  | 557 ms: 1.01x faster                                                       |
| pprint_pformat            | 3.66 sec                                                                | 3.61 sec: 1.01x faster                                                     |
| gc_traversal              | 3.48 ms                                                                 | 3.44 ms: 1.01x faster                                                      |
| pyflate                   | 1.02 sec                                                                | 1.01 sec: 1.01x faster                                                     |
| deepcopy_reduce           | 6.08 us                                                                 | 6.00 us: 1.01x faster                                                      |
| telco                     | 12.9 ms                                                                 | 12.8 ms: 1.01x faster                                                      |
| sympy_expand              | 964 ms                                                                  | 952 ms: 1.01x faster                                                       |
| genshi_xml                | 106 ms                                                                  | 104 ms: 1.01x faster                                                       |
| async_tree_memoization    | 746 ms                                                                  | 739 ms: 1.01x faster                                                       |
| sympy_str                 | 521 ms                                                                  | 516 ms: 1.01x faster                                                       |
| bench_thread_pool         | 2.13 ms                                                                 | 2.11 ms: 1.01x faster                                                      |
| asyncio_websockets        | 675 ms                                                                  | 668 ms: 1.01x faster                                                       |
| 2to3                      | 517 ms                                                                  | 513 ms: 1.01x faster                                                       |
| html5lib                  | 121 ms                                                                  | 120 ms: 1.01x faster                                                       |
| mdp                       | 4.36 sec                                                                | 4.32 sec: 1.01x faster                                                     |
| async_tree_io             | 1.41 sec                                                                | 1.40 sec: 1.01x faster                                                     |
| tomli_loads               | 4.23 sec                                                                | 4.20 sec: 1.01x faster                                                     |
| async_tree_io_tg          | 1.35 sec                                                                | 1.34 sec: 1.01x faster                                                     |
| docutils                  | 4.11 sec                                                                | 4.09 sec: 1.01x faster                                                     |
| pycparser                 | 2.05 sec                                                                | 2.06 sec: 1.01x slower                                                     |
| richards_super            | 139 ms                                                                  | 140 ms: 1.01x slower                                                       |
| scimark_lu                | 347 ms                                                                  | 353 ms: 1.02x slower                                                       |
| regex_effbot              | 4.41 ms                                                                 | 4.51 ms: 1.02x slower                                                      |
| regex_dna                 | 249 ms                                                                  | 259 ms: 1.04x slower                                                       |
| Geometric mean            | (ref)                                                                   | 1.01x faster                                                               |

Benchmark hidden because not significant (40): float, python_startup, sqlglot_optimize, xml_etree_iterparse, xml_etree_process, deltablue, tornado_http, generators, scimark_sor, hexiom, crypto_pyaes, pidigits, pylint, go, async_generators, deepcopy, async_tree_cpu_io_mixed_tg, chaos, sympy_integrate, meteor_contest, async_tree_cpu_io_mixed, nqueens, unpickle_pure_python, xml_etree_generate, sympy_sum, json_dumps, async_tree_none, create_gc_cycles, mako, pickle_pure_python, json_loads, bpe_tokeniser, deepcopy_memo, comprehensions, sqlglot_transpile, genshi_text, thrift, regex_v8, json, typing_runtime_protocols

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x