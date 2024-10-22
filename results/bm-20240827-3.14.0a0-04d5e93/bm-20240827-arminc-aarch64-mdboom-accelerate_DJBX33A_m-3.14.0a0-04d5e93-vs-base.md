# Results vs. base

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: linux-aarch64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.00x faster
- HPT reliability: 99.70%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io   | 1.15 sec                                                                | 1.13 sec: 1.02x faster                                                  |
| asyncio_tcp_ssl | 2.20 sec                                                                | 2.25 sec: 1.02x slower                                                  |
| asyncio_tcp     | 560 ms                                                                  | 583 ms: 1.04x slower                                                    |
| Geometric mean  | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (10): async_generators, async_tree_cpu_io_mixed_tg, async_tree_io_tg, coroutines, async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.6 ms                                                                 | 92.6 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.85 ms                                                                 | 4.81 ms: 1.01x faster                                                   |
| regex_dna      | 245 ms                                                                  | 245 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|---------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse | 151 ms                                                                  | 146 ms: 1.04x faster                                                    |
| tomli_loads         | 2.64 sec                                                                | 2.55 sec: 1.04x faster                                                  |
| xml_etree_process   | 80.2 ms                                                                 | 77.5 ms: 1.03x faster                                                   |
| json_loads          | 32.5 us                                                                 | 32.2 us: 1.01x faster                                                   |
| Geometric mean      | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (5): unpickle_pure_python, xml_etree_parse, pickle_pure_python, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                 | 13.0 ms: 1.01x faster                                                   |
| python_startup_no_site | 8.75 ms                                                                 | 8.79 ms: 1.00x slower                                                   |
| Geometric mean         | (ref)                                                                   | 1.00x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 60.1 ms                                                                 | 59.1 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (3): django_template, genshi_text, mako

All benchmarks:
===============

| Benchmark                | bm-20240826-arminc-aarch64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|--------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse      | 151 ms                                                                  | 146 ms: 1.04x faster                                                    |
| tomli_loads              | 2.64 sec                                                                | 2.55 sec: 1.04x faster                                                  |
| xml_etree_process        | 80.2 ms                                                                 | 77.5 ms: 1.03x faster                                                   |
| deepcopy                 | 338 us                                                                  | 329 us: 1.03x faster                                                    |
| sqlglot_optimize         | 62.4 ms                                                                 | 61.0 ms: 1.02x faster                                                   |
| pprint_safe_repr         | 918 ms                                                                  | 898 ms: 1.02x faster                                                    |
| hexiom                   | 7.16 ms                                                                 | 7.00 ms: 1.02x faster                                                   |
| json                     | 5.71 ms                                                                 | 5.59 ms: 1.02x faster                                                   |
| sqlglot_transpile        | 1.74 ms                                                                 | 1.70 ms: 1.02x faster                                                   |
| deepcopy_reduce          | 3.52 us                                                                 | 3.45 us: 1.02x faster                                                   |
| scimark_monte_carlo      | 82.8 ms                                                                 | 81.2 ms: 1.02x faster                                                   |
| typing_runtime_protocols | 195 us                                                                  | 191 us: 1.02x faster                                                    |
| pprint_pformat           | 1.89 sec                                                                | 1.85 sec: 1.02x faster                                                  |
| go                       | 193 ms                                                                  | 190 ms: 1.02x faster                                                    |
| genshi_xml               | 60.1 ms                                                                 | 59.1 ms: 1.02x faster                                                   |
| async_tree_io            | 1.15 sec                                                                | 1.13 sec: 1.02x faster                                                  |
| sympy_expand             | 460 ms                                                                  | 453 ms: 1.01x faster                                                    |
| comprehensions           | 20.6 us                                                                 | 20.3 us: 1.01x faster                                                   |
| deepcopy_memo            | 38.0 us                                                                 | 37.6 us: 1.01x faster                                                   |
| json_loads               | 32.5 us                                                                 | 32.2 us: 1.01x faster                                                   |
| regex_effbot             | 4.85 ms                                                                 | 4.81 ms: 1.01x faster                                                   |
| bpe_tokeniser            | 5.87 sec                                                                | 5.83 sec: 1.01x faster                                                  |
| raytrace                 | 302 ms                                                                  | 300 ms: 1.01x faster                                                    |
| python_startup           | 13.1 ms                                                                 | 13.0 ms: 1.01x faster                                                   |
| mdp                      | 3.34 sec                                                                | 3.33 sec: 1.00x faster                                                  |
| regex_dna                | 245 ms                                                                  | 245 ms: 1.00x faster                                                    |
| python_startup_no_site   | 8.75 ms                                                                 | 8.79 ms: 1.00x slower                                                   |
| fannkuch                 | 464 ms                                                                  | 467 ms: 1.01x slower                                                    |
| float                    | 91.6 ms                                                                 | 92.6 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl          | 2.20 sec                                                                | 2.25 sec: 1.02x slower                                                  |
| pathlib                  | 20.8 ms                                                                 | 21.3 ms: 1.02x slower                                                   |
| pyflate                  | 563 ms                                                                  | 579 ms: 1.03x slower                                                    |
| gc_traversal             | 4.83 ms                                                                 | 4.98 ms: 1.03x slower                                                   |
| telco                    | 9.68 ms                                                                 | 10.0 ms: 1.04x slower                                                   |
| asyncio_tcp              | 560 ms                                                                  | 583 ms: 1.04x slower                                                    |
| Geometric mean           | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (54): html5lib, sqlglot_parse, django_template, bench_mp_pool, regex_compile, nqueens, regex_v8, tornado_http, coverage, sympy_sum, crypto_pyaes, genshi_text, sympy_integrate, docutils, richards, unpickle_pure_python, scimark_lu, pidigits, 2to3, chaos, async_generators, xml_etree_parse, bench_thread_pool, meteor_contest, sympy_str, scimark_sparse_mat_mult, scimark_sor, async_tree_cpu_io_mixed_tg, spectral_norm, logging_simple, pickle_pure_python, scimark_fft, logging_silent, async_tree_io_tg, richards_super, coroutines, xml_etree_generate, nbody, thrift, generators, pylint, deltablue, logging_format, async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed, pycparser, json_dumps, async_tree_memoization_tg, async_tree_memoization, sqlglot_normalize, create_gc_cycles, async_tree_none, mako

# HPT report

- Reliability score: 99.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x