# Results vs. base

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-aarch64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.00x slower
- HPT reliability: 86.27%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.10 sec                                                                | 3.12 sec: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_generators | 493 ms                                                                  | 487 ms: 1.01x faster                                                    |
| asyncio_tcp_ssl  | 2.19 sec                                                                | 2.21 sec: 1.01x slower                                                  |
| asyncio_tcp      | 562 ms                                                                  | 576 ms: 1.02x slower                                                    |
| Geometric mean   | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (10): asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_io_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 92.1 ms                                                                 | 92.7 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.3 ms                                                                 | 30.6 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python | 365 us                                                                  | 357 us: 1.02x faster                                                    |
| tomli_loads        | 2.55 sec                                                                | 2.53 sec: 1.01x faster                                                  |
| Geometric mean     | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (7): json_dumps, xml_etree_generate, unpickle_pure_python, xml_etree_process, json_loads, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                                 | 13.4 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.3 ms                                                                 | 13.4 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240802-arminc-aarch64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_reduce          | 3.48 us                                                                 | 3.38 us: 1.03x faster                                                   |
| regex_v8                 | 31.3 ms                                                                 | 30.6 ms: 1.02x faster                                                   |
| nqueens                  | 100 ms                                                                  | 97.8 ms: 1.02x faster                                                   |
| pickle_pure_python       | 365 us                                                                  | 357 us: 1.02x faster                                                    |
| scimark_monte_carlo      | 82.9 ms                                                                 | 81.5 ms: 1.02x faster                                                   |
| pprint_safe_repr         | 957 ms                                                                  | 941 ms: 1.02x faster                                                    |
| sqlglot_transpile        | 1.74 ms                                                                 | 1.72 ms: 1.01x faster                                                   |
| async_generators         | 493 ms                                                                  | 487 ms: 1.01x faster                                                    |
| bpe_tokeniser            | 5.91 sec                                                                | 5.84 sec: 1.01x faster                                                  |
| pprint_pformat           | 1.95 sec                                                                | 1.92 sec: 1.01x faster                                                  |
| mdp                      | 3.35 sec                                                                | 3.33 sec: 1.01x faster                                                  |
| tomli_loads              | 2.55 sec                                                                | 2.53 sec: 1.01x faster                                                  |
| crypto_pyaes             | 81.8 ms                                                                 | 82.1 ms: 1.00x slower                                                   |
| pyflate                  | 579 ms                                                                  | 582 ms: 1.00x slower                                                    |
| float                    | 92.1 ms                                                                 | 92.7 ms: 1.01x slower                                                   |
| mako                     | 13.3 ms                                                                 | 13.4 ms: 1.01x slower                                                   |
| docutils                 | 3.10 sec                                                                | 3.12 sec: 1.01x slower                                                  |
| pathlib                  | 21.1 ms                                                                 | 21.3 ms: 1.01x slower                                                   |
| fannkuch                 | 462 ms                                                                  | 467 ms: 1.01x slower                                                    |
| meteor_contest           | 111 ms                                                                  | 112 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl          | 2.19 sec                                                                | 2.21 sec: 1.01x slower                                                  |
| typing_runtime_protocols | 194 us                                                                  | 197 us: 1.02x slower                                                    |
| logging_simple           | 6.81 us                                                                 | 6.97 us: 1.02x slower                                                   |
| python_startup           | 13.0 ms                                                                 | 13.4 ms: 1.02x slower                                                   |
| asyncio_tcp              | 562 ms                                                                  | 576 ms: 1.02x slower                                                    |
| logging_format           | 7.54 us                                                                 | 7.73 us: 1.03x slower                                                   |
| create_gc_cycles         | 2.28 ms                                                                 | 2.37 ms: 1.04x slower                                                   |
| Geometric mean           | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (63): json_dumps, regex_effbot, xml_etree_generate, sqlglot_optimize, gc_traversal, asyncio_websockets, unpickle_pure_python, deltablue, bench_thread_pool, async_tree_cpu_io_mixed_tg, coverage, telco, sympy_integrate, spectral_norm, regex_dna, async_tree_none, scimark_sparse_mat_mult, async_tree_memoization_tg, go, pycparser, regex_compile, scimark_lu, scimark_fft, richards_super, logging_silent, async_tree_io, deepcopy, raytrace, genshi_text, generators, pidigits, hexiom, sympy_expand, scimark_sor, xml_etree_process, json, richards, comprehensions, 2to3, async_tree_none_tg, deepcopy_memo, dask, html5lib, sympy_str, sympy_sum, django_template, bench_mp_pool, python_startup_no_site, async_tree_cpu_io_mixed, json_loads, async_tree_memoization, sqlglot_normalize, tornado_http, async_tree_io_tg, chaos, pylint, thrift, nbody, coroutines, sqlglot_parse, xml_etree_parse, genshi_xml, xml_etree_iterparse

# HPT report

- Reliability score: 86.27% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x