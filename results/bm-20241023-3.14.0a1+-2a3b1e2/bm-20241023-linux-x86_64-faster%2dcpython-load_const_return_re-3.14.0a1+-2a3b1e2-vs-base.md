# Results vs. base

- fork: faster-cpython
- ref: load_const_return_re
- machine: linux-x86_64
- commit hash: 2a3b1e2
- commit date: 2024-10-23
- overall geometric mean: 1.00x faster
- HPT reliability: 60.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 254 ms: 1.00x slower                                                             |
| docutils       | 2.64 sec                                                               | 2.66 sec: 1.01x slower                                                           |
| tornado_http   | 90.1 ms                                                                | 91.4 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| coroutines         | 23.4 ms                                                                | 23.3 ms: 1.01x faster                                                            |
| async_generators   | 430 ms                                                                 | 427 ms: 1.01x faster                                                             |
| asyncio_websockets | 557 ms                                                                 | 553 ms: 1.01x faster                                                             |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 192 ms                                                                 | 187 ms: 1.02x faster                                                             |
| float          | 79.7 ms                                                                | 80.3 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                                | 3.60 ms: 1.03x faster                                                            |
| regex_dna      | 217 ms                                                                 | 214 ms: 1.01x faster                                                             |
| regex_compile  | 130 ms                                                                 | 131 ms: 1.01x slower                                                             |
| regex_v8       | 24.5 ms                                                                | 25.3 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                                 | 156 ms: 1.02x faster                                                             |
| json_dumps           | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                                            |
| tomli_loads          | 2.13 sec                                                               | 2.12 sec: 1.01x faster                                                           |
| unpickle_pure_python | 219 us                                                                 | 217 us: 1.01x faster                                                             |
| xml_etree_generate   | 86.7 ms                                                                | 87.1 ms: 1.01x slower                                                            |
| xml_etree_process    | 59.8 ms                                                                | 60.1 ms: 1.01x slower                                                            |
| pickle_pure_python   | 309 us                                                                 | 315 us: 1.02x slower                                                             |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (2): json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 11.7 ms                                                                | 11.8 ms: 1.01x slower                                                            |
| python_startup_no_site | 6.99 ms                                                                | 7.05 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.6 ms                                                                | 11.4 ms: 1.02x faster                                                            |
| django_template | 35.1 ms                                                                | 34.8 ms: 1.01x faster                                                            |
| genshi_xml      | 51.8 ms                                                                | 52.5 ms: 1.01x slower                                                            |
| genshi_text     | 22.8 ms                                                                | 23.8 ms: 1.05x slower                                                            |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                     |

All benchmarks:
===============

| Benchmark              | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| logging_silent         | 102 ns                                                                 | 98.3 ns: 1.03x faster                                                            |
| regex_effbot           | 3.73 ms                                                                | 3.60 ms: 1.03x faster                                                            |
| spectral_norm          | 118 ms                                                                 | 114 ms: 1.03x faster                                                             |
| mako                   | 11.6 ms                                                                | 11.4 ms: 1.02x faster                                                            |
| pycparser              | 1.17 sec                                                               | 1.14 sec: 1.02x faster                                                           |
| pidigits               | 192 ms                                                                 | 187 ms: 1.02x faster                                                             |
| generators             | 27.4 ms                                                                | 26.8 ms: 1.02x faster                                                            |
| xml_etree_parse        | 159 ms                                                                 | 156 ms: 1.02x faster                                                             |
| bpe_tokeniser          | 4.85 sec                                                               | 4.77 sec: 1.02x faster                                                           |
| crypto_pyaes           | 72.9 ms                                                                | 71.8 ms: 1.02x faster                                                            |
| pathlib                | 16.1 ms                                                                | 15.8 ms: 1.01x faster                                                            |
| comprehensions         | 16.8 us                                                                | 16.6 us: 1.01x faster                                                            |
| json_dumps             | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                                            |
| coverage               | 85.4 ms                                                                | 84.4 ms: 1.01x faster                                                            |
| django_template        | 35.1 ms                                                                | 34.8 ms: 1.01x faster                                                            |
| regex_dna              | 217 ms                                                                 | 214 ms: 1.01x faster                                                             |
| sympy_str              | 270 ms                                                                 | 267 ms: 1.01x faster                                                             |
| scimark_fft            | 369 ms                                                                 | 365 ms: 1.01x faster                                                             |
| nqueens                | 81.2 ms                                                                | 80.6 ms: 1.01x faster                                                            |
| coroutines             | 23.4 ms                                                                | 23.3 ms: 1.01x faster                                                            |
| sympy_sum              | 148 ms                                                                 | 147 ms: 1.01x faster                                                             |
| async_generators       | 430 ms                                                                 | 427 ms: 1.01x faster                                                             |
| tomli_loads            | 2.13 sec                                                               | 2.12 sec: 1.01x faster                                                           |
| unpickle_pure_python   | 219 us                                                                 | 217 us: 1.01x faster                                                             |
| go                     | 121 ms                                                                 | 120 ms: 1.01x faster                                                             |
| asyncio_websockets     | 557 ms                                                                 | 553 ms: 1.01x faster                                                             |
| meteor_contest         | 106 ms                                                                 | 106 ms: 1.00x faster                                                             |
| scimark_monte_carlo    | 69.5 ms                                                                | 69.1 ms: 1.00x faster                                                            |
| sqlglot_normalize      | 107 ms                                                                 | 106 ms: 1.00x faster                                                             |
| create_gc_cycles       | 2.66 ms                                                                | 2.67 ms: 1.00x slower                                                            |
| 2to3                   | 254 ms                                                                 | 254 ms: 1.00x slower                                                             |
| pyflate                | 457 ms                                                                 | 459 ms: 1.00x slower                                                             |
| hexiom                 | 6.26 ms                                                                | 6.28 ms: 1.00x slower                                                            |
| deepcopy_memo          | 31.0 us                                                                | 31.1 us: 1.00x slower                                                            |
| sqlglot_parse          | 1.29 ms                                                                | 1.30 ms: 1.00x slower                                                            |
| sqlglot_transpile      | 1.59 ms                                                                | 1.60 ms: 1.01x slower                                                            |
| xml_etree_generate     | 86.7 ms                                                                | 87.1 ms: 1.01x slower                                                            |
| xml_etree_process      | 59.8 ms                                                                | 60.1 ms: 1.01x slower                                                            |
| bench_thread_pool      | 837 us                                                                 | 842 us: 1.01x slower                                                             |
| docutils               | 2.64 sec                                                               | 2.66 sec: 1.01x slower                                                           |
| float                  | 79.7 ms                                                                | 80.3 ms: 1.01x slower                                                            |
| python_startup         | 11.7 ms                                                                | 11.8 ms: 1.01x slower                                                            |
| python_startup_no_site | 6.99 ms                                                                | 7.05 ms: 1.01x slower                                                            |
| richards               | 45.7 ms                                                                | 46.1 ms: 1.01x slower                                                            |
| regex_compile          | 130 ms                                                                 | 131 ms: 1.01x slower                                                             |
| deltablue              | 3.23 ms                                                                | 3.26 ms: 1.01x slower                                                            |
| scimark_lu             | 116 ms                                                                 | 117 ms: 1.01x slower                                                             |
| bench_mp_pool          | 77.8 ms                                                                | 78.7 ms: 1.01x slower                                                            |
| fannkuch               | 400 ms                                                                 | 405 ms: 1.01x slower                                                             |
| dulwich_log            | 63.2 ms                                                                | 64.0 ms: 1.01x slower                                                            |
| tornado_http           | 90.1 ms                                                                | 91.4 ms: 1.01x slower                                                            |
| genshi_xml             | 51.8 ms                                                                | 52.5 ms: 1.01x slower                                                            |
| richards_super         | 51.8 ms                                                                | 52.7 ms: 1.02x slower                                                            |
| logging_simple         | 5.54 us                                                                | 5.64 us: 1.02x slower                                                            |
| pickle_pure_python     | 309 us                                                                 | 315 us: 1.02x slower                                                             |
| scimark_sor            | 129 ms                                                                 | 132 ms: 1.02x slower                                                             |
| regex_v8               | 24.5 ms                                                                | 25.3 ms: 1.03x slower                                                            |
| chaos                  | 60.6 ms                                                                | 62.6 ms: 1.03x slower                                                            |
| gc_traversal           | 4.33 ms                                                                | 4.47 ms: 1.03x slower                                                            |
| genshi_text            | 22.8 ms                                                                | 23.8 ms: 1.05x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (29): sympy_expand, async_tree_cpu_io_mixed, pprint_safe_repr, async_tree_memoization, async_tree_none, json, deepcopy_reduce, thrift, json_loads, sqlglot_optimize, async_tree_none_tg, sympy_integrate, async_tree_cpu_io_mixed_tg, raytrace, deepcopy, mdp, pprint_pformat, sphinx, scimark_sparse_mat_mult, async_tree_io, async_tree_memoization_tg, xml_etree_iterparse, html5lib, telco, typing_runtime_protocols, pylint, async_tree_io_tg, nbody, logging_format

# HPT report

- Reliability score: 60.79% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x