# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.00x slower
- HPT reliability: 53.08%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 257 ms                                                                | 256 ms: 1.00x faster                                                  |
| html5lib       | 63.1 ms                                                               | 64.0 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg | 901 ms                                                                | 887 ms: 1.02x faster                                                  |
| asyncio_tcp      | 478 ms                                                                | 473 ms: 1.01x faster                                                  |
| async_tree_io    | 930 ms                                                                | 920 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl  | 1.80 sec                                                              | 1.79 sec: 1.01x faster                                                |
| async_generators | 437 ms                                                                | 439 ms: 1.01x slower                                                  |
| coroutines       | 23.1 ms                                                               | 23.8 ms: 1.03x slower                                                 |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_none, asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 186 ms: 1.00x faster                                                  |
| float          | 77.5 ms                                                               | 78.3 ms: 1.01x slower                                                 |
| nbody          | 84.1 ms                                                               | 89.8 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.81 ms                                                               | 3.77 ms: 1.01x faster                                                 |
| regex_v8       | 26.2 ms                                                               | 26.1 ms: 1.00x faster                                                 |
| regex_compile  | 128 ms                                                                | 129 ms: 1.01x slower                                                  |
| regex_dna      | 220 ms                                                                | 224 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 10.5 ms                                                               | 10.4 ms: 1.01x faster                                                 |
| tomli_loads          | 2.09 sec                                                              | 2.08 sec: 1.01x faster                                                |
| unpickle_pure_python | 213 us                                                                | 214 us: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (6): xml_etree_parse, xml_etree_process, xml_etree_generate, pickle_pure_python, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 7.11 ms                                                               | 7.07 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text    | 23.0 ms                                                               | 21.8 ms: 1.05x faster                                                 |
| genshi_xml     | 49.5 ms                                                               | 49.1 ms: 1.01x faster                                                 |
| mako           | 11.3 ms                                                               | 11.5 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text             | 23.0 ms                                                               | 21.8 ms: 1.05x faster                                                 |
| pathlib                 | 16.2 ms                                                               | 15.7 ms: 1.03x faster                                                 |
| crypto_pyaes            | 72.6 ms                                                               | 71.4 ms: 1.02x faster                                                 |
| deepcopy_reduce         | 2.72 us                                                               | 2.67 us: 1.02x faster                                                 |
| async_tree_io_tg        | 901 ms                                                                | 887 ms: 1.02x faster                                                  |
| pycparser               | 1.20 sec                                                              | 1.18 sec: 1.01x faster                                                |
| hexiom                  | 6.20 ms                                                               | 6.11 ms: 1.01x faster                                                 |
| sqlglot_parse           | 1.30 ms                                                               | 1.28 ms: 1.01x faster                                                 |
| asyncio_tcp             | 478 ms                                                                | 473 ms: 1.01x faster                                                  |
| telco                   | 8.42 ms                                                               | 8.32 ms: 1.01x faster                                                 |
| nqueens                 | 81.3 ms                                                               | 80.4 ms: 1.01x faster                                                 |
| regex_effbot            | 3.81 ms                                                               | 3.77 ms: 1.01x faster                                                 |
| spectral_norm           | 114 ms                                                                | 113 ms: 1.01x faster                                                  |
| async_tree_io           | 930 ms                                                                | 920 ms: 1.01x faster                                                  |
| json_dumps              | 10.5 ms                                                               | 10.4 ms: 1.01x faster                                                 |
| genshi_xml              | 49.5 ms                                                               | 49.1 ms: 1.01x faster                                                 |
| fannkuch                | 406 ms                                                                | 403 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.79 sec: 1.01x faster                                                |
| meteor_contest          | 107 ms                                                                | 106 ms: 1.01x faster                                                  |
| python_startup          | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| mdp                     | 2.52 sec                                                              | 2.50 sec: 1.01x faster                                                |
| sqlglot_transpile       | 1.58 ms                                                               | 1.57 ms: 1.01x faster                                                 |
| python_startup_no_site  | 7.11 ms                                                               | 7.07 ms: 1.01x faster                                                 |
| tomli_loads             | 2.09 sec                                                              | 2.08 sec: 1.01x faster                                                |
| sympy_sum               | 147 ms                                                                | 146 ms: 1.00x faster                                                  |
| thrift                  | 771 us                                                                | 767 us: 1.00x faster                                                  |
| sympy_integrate         | 19.5 ms                                                               | 19.4 ms: 1.00x faster                                                 |
| 2to3                    | 257 ms                                                                | 256 ms: 1.00x faster                                                  |
| regex_v8                | 26.2 ms                                                               | 26.1 ms: 1.00x faster                                                 |
| gc_traversal            | 3.72 ms                                                               | 3.71 ms: 1.00x faster                                                 |
| pidigits                | 187 ms                                                                | 186 ms: 1.00x faster                                                  |
| richards_super          | 51.7 ms                                                               | 51.9 ms: 1.00x slower                                                 |
| bench_thread_pool       | 780 us                                                                | 784 us: 1.00x slower                                                  |
| create_gc_cycles        | 1.74 ms                                                               | 1.75 ms: 1.00x slower                                                 |
| async_generators        | 437 ms                                                                | 439 ms: 1.01x slower                                                  |
| generators              | 27.7 ms                                                               | 27.8 ms: 1.01x slower                                                 |
| go                      | 118 ms                                                                | 119 ms: 1.01x slower                                                  |
| sqlglot_normalize       | 108 ms                                                                | 108 ms: 1.01x slower                                                  |
| regex_compile           | 128 ms                                                                | 129 ms: 1.01x slower                                                  |
| unpickle_pure_python    | 213 us                                                                | 214 us: 1.01x slower                                                  |
| scimark_sor             | 125 ms                                                                | 126 ms: 1.01x slower                                                  |
| logging_simple          | 5.51 us                                                               | 5.55 us: 1.01x slower                                                 |
| bpe_tokeniser           | 4.78 sec                                                              | 4.83 sec: 1.01x slower                                                |
| scimark_lu              | 113 ms                                                                | 114 ms: 1.01x slower                                                  |
| pprint_pformat          | 1.45 sec                                                              | 1.47 sec: 1.01x slower                                                |
| float                   | 77.5 ms                                                               | 78.3 ms: 1.01x slower                                                 |
| coverage                | 85.3 ms                                                               | 86.2 ms: 1.01x slower                                                 |
| raytrace                | 259 ms                                                                | 262 ms: 1.01x slower                                                  |
| html5lib                | 63.1 ms                                                               | 64.0 ms: 1.01x slower                                                 |
| logging_format          | 6.08 us                                                               | 6.18 us: 1.02x slower                                                 |
| deepcopy_memo           | 29.7 us                                                               | 30.1 us: 1.02x slower                                                 |
| pprint_safe_repr        | 704 ms                                                                | 716 ms: 1.02x slower                                                  |
| mako                    | 11.3 ms                                                               | 11.5 ms: 1.02x slower                                                 |
| regex_dna               | 220 ms                                                                | 224 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult | 4.71 ms                                                               | 4.83 ms: 1.03x slower                                                 |
| coroutines              | 23.1 ms                                                               | 23.8 ms: 1.03x slower                                                 |
| logging_silent          | 97.9 ns                                                               | 101 ns: 1.03x slower                                                  |
| scimark_fft             | 353 ms                                                                | 369 ms: 1.05x slower                                                  |
| nbody                   | 84.1 ms                                                               | 89.8 ms: 1.07x slower                                                 |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (30): async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, pylint, xml_etree_parse, async_tree_cpu_io_mixed_tg, richards, comprehensions, async_tree_none, deepcopy, tornado_http, deltablue, xml_etree_process, xml_etree_generate, pickle_pure_python, sympy_expand, pyflate, json_loads, json, docutils, sqlglot_optimize, bench_mp_pool, asyncio_websockets, chaos, scimark_monte_carlo, typing_runtime_protocols, async_tree_cpu_io_mixed, django_template, xml_etree_iterparse, sympy_str

# HPT report

- Reliability score: 53.08% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x