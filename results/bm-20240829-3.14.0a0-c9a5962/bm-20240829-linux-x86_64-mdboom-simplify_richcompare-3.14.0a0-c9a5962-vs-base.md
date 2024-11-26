# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.006x faster
- HPT reliability: 99.66%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 257 ms                                                                | 253 ms: 1.02x faster                                                  |
| docutils       | 2.66 sec                                                              | 2.64 sec: 1.01x faster                                                |
| html5lib       | 63.1 ms                                                               | 63.8 ms: 1.01x slower                                                 |
| tornado_http   | 90.1 ms                                                               | 89.5 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp_ssl  | 1.80 sec                                                              | 1.79 sec: 1.01x faster                                                |
| async_tree_io    | 930 ms                                                                | 926 ms: 1.00x faster                                                  |
| coroutines       | 23.1 ms                                                               | 23.2 ms: 1.00x slower                                                 |
| async_generators | 437 ms                                                                | 439 ms: 1.01x slower                                                  |
| asyncio_tcp      | 478 ms                                                                | 486 ms: 1.02x slower                                                  |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_none, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 77.5 ms                                                               | 76.5 ms: 1.01x faster                                                 |
| nbody          | 84.1 ms                                                               | 85.3 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.81 ms                                                               | 3.54 ms: 1.08x faster                                                 |
| regex_v8       | 26.2 ms                                                               | 24.3 ms: 1.08x faster                                                 |
| regex_dna      | 220 ms                                                                | 218 ms: 1.01x faster                                                  |
| regex_compile  | 128 ms                                                                | 129 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads         | 2.09 sec                                                              | 2.05 sec: 1.02x faster                                                |
| json_dumps          | 10.5 ms                                                               | 10.4 ms: 1.01x faster                                                 |
| xml_etree_generate  | 84.6 ms                                                               | 85.2 ms: 1.01x slower                                                 |
| xml_etree_iterparse | 104 ms                                                                | 104 ms: 1.01x slower                                                  |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (5): unpickle_pure_python, pickle_pure_python, json_loads, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 7.11 ms                                                               | 7.04 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text    | 23.0 ms                                                               | 21.5 ms: 1.07x faster                                                 |
| genshi_xml     | 49.5 ms                                                               | 48.2 ms: 1.03x faster                                                 |
| mako           | 11.3 ms                                                               | 11.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot             | 3.81 ms                                                               | 3.54 ms: 1.08x faster                                                 |
| regex_v8                 | 26.2 ms                                                               | 24.3 ms: 1.08x faster                                                 |
| genshi_text              | 23.0 ms                                                               | 21.5 ms: 1.07x faster                                                 |
| pycparser                | 1.20 sec                                                              | 1.13 sec: 1.06x faster                                                |
| gc_traversal             | 3.72 ms                                                               | 3.54 ms: 1.05x faster                                                 |
| pyflate                  | 474 ms                                                                | 461 ms: 1.03x faster                                                  |
| genshi_xml               | 49.5 ms                                                               | 48.2 ms: 1.03x faster                                                 |
| deepcopy_reduce          | 2.72 us                                                               | 2.66 us: 1.02x faster                                                 |
| tomli_loads              | 2.09 sec                                                              | 2.05 sec: 1.02x faster                                                |
| nqueens                  | 81.3 ms                                                               | 79.8 ms: 1.02x faster                                                 |
| sqlglot_parse            | 1.30 ms                                                               | 1.28 ms: 1.02x faster                                                 |
| 2to3                     | 257 ms                                                                | 253 ms: 1.02x faster                                                  |
| scimark_sor              | 125 ms                                                                | 124 ms: 1.01x faster                                                  |
| float                    | 77.5 ms                                                               | 76.5 ms: 1.01x faster                                                 |
| spectral_norm            | 114 ms                                                                | 112 ms: 1.01x faster                                                  |
| json_dumps               | 10.5 ms                                                               | 10.4 ms: 1.01x faster                                                 |
| pathlib                  | 16.2 ms                                                               | 16.0 ms: 1.01x faster                                                 |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| thrift                   | 771 us                                                                | 762 us: 1.01x faster                                                  |
| fannkuch                 | 406 ms                                                                | 402 ms: 1.01x faster                                                  |
| meteor_contest           | 107 ms                                                                | 106 ms: 1.01x faster                                                  |
| python_startup_no_site   | 7.11 ms                                                               | 7.04 ms: 1.01x faster                                                 |
| telco                    | 8.42 ms                                                               | 8.34 ms: 1.01x faster                                                 |
| regex_dna                | 220 ms                                                                | 218 ms: 1.01x faster                                                  |
| pprint_pformat           | 1.45 sec                                                              | 1.44 sec: 1.01x faster                                                |
| sqlglot_transpile        | 1.58 ms                                                               | 1.57 ms: 1.01x faster                                                 |
| docutils                 | 2.66 sec                                                              | 2.64 sec: 1.01x faster                                                |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.79 sec: 1.01x faster                                                |
| mdp                      | 2.52 sec                                                              | 2.50 sec: 1.01x faster                                                |
| create_gc_cycles         | 1.74 ms                                                               | 1.73 ms: 1.01x faster                                                 |
| sympy_expand             | 455 ms                                                                | 452 ms: 1.01x faster                                                  |
| tornado_http             | 90.1 ms                                                               | 89.5 ms: 1.01x faster                                                 |
| chaos                    | 58.4 ms                                                               | 58.2 ms: 1.00x faster                                                 |
| async_tree_io            | 930 ms                                                                | 926 ms: 1.00x faster                                                  |
| sqlglot_optimize         | 53.6 ms                                                               | 53.5 ms: 1.00x faster                                                 |
| sympy_integrate          | 19.5 ms                                                               | 19.5 ms: 1.00x faster                                                 |
| bench_thread_pool        | 780 us                                                                | 783 us: 1.00x slower                                                  |
| coroutines               | 23.1 ms                                                               | 23.2 ms: 1.00x slower                                                 |
| sqlglot_normalize        | 108 ms                                                                | 108 ms: 1.01x slower                                                  |
| async_generators         | 437 ms                                                                | 439 ms: 1.01x slower                                                  |
| xml_etree_generate       | 84.6 ms                                                               | 85.2 ms: 1.01x slower                                                 |
| regex_compile            | 128 ms                                                                | 129 ms: 1.01x slower                                                  |
| xml_etree_iterparse      | 104 ms                                                                | 104 ms: 1.01x slower                                                  |
| raytrace                 | 259 ms                                                                | 261 ms: 1.01x slower                                                  |
| html5lib                 | 63.1 ms                                                               | 63.8 ms: 1.01x slower                                                 |
| scimark_sparse_mat_mult  | 4.71 ms                                                               | 4.77 ms: 1.01x slower                                                 |
| logging_simple           | 5.51 us                                                               | 5.58 us: 1.01x slower                                                 |
| nbody                    | 84.1 ms                                                               | 85.3 ms: 1.01x slower                                                 |
| mako                     | 11.3 ms                                                               | 11.4 ms: 1.02x slower                                                 |
| typing_runtime_protocols | 158 us                                                                | 161 us: 1.02x slower                                                  |
| asyncio_tcp              | 478 ms                                                                | 486 ms: 1.02x slower                                                  |
| logging_silent           | 97.9 ns                                                               | 100 ns: 1.02x slower                                                  |
| scimark_fft              | 353 ms                                                                | 363 ms: 1.03x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (36): async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, richards, go, pprint_safe_repr, pylint, deepcopy, comprehensions, scimark_monte_carlo, sympy_str, richards_super, json, deepcopy_memo, hexiom, unpickle_pure_python, django_template, sympy_sum, pidigits, pickle_pure_python, bench_mp_pool, json_loads, xml_etree_process, async_tree_none, generators, scimark_lu, asyncio_websockets, async_tree_cpu_io_mixed_tg, logging_format, bpe_tokeniser, crypto_pyaes, xml_etree_parse, deltablue, coverage, async_tree_cpu_io_mixed

- Geometric mean (including insignificant results): 1.006x faster
# HPT report

- Reliability score: 99.66% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x