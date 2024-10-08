# Results vs. base

- fork: brandtbucher
- ref: class_no_vectorcall
- machine: linux-x86_64
- commit hash: bfdd616
- commit date: 2024-08-21
- overall geometric mean: 1.00x slower
- HPT reliability: 95.67%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 284 ms                                                                | 283 ms: 1.00x faster                                                       |
| html5lib       | 66.2 ms                                                               | 66.6 ms: 1.01x slower                                                      |
| tornado_http   | 93.3 ms                                                               | 94.3 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines      | 23.5 ms                                                               | 23.0 ms: 1.02x faster                                                      |
| asyncio_tcp     | 497 ms                                                                | 493 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl | 1.80 sec                                                              | 1.80 sec: 1.00x faster                                                     |
| async_tree_none | 322 ms                                                                | 325 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (9): async_tree_io_tg, async_generators, async_tree_memoization, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 80.4 ms                                                               | 79.6 ms: 1.01x faster                                                      |
| pidigits       | 186 ms                                                                | 186 ms: 1.00x slower                                                       |
| float          | 70.4 ms                                                               | 70.7 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 141 ms                                                                | 142 ms: 1.00x slower                                                       |
| regex_dna      | 215 ms                                                                | 218 ms: 1.02x slower                                                       |
| regex_v8       | 24.3 ms                                                               | 25.2 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps         | 10.1 ms                                                               | 10.0 ms: 1.01x faster                                                      |
| xml_etree_generate | 77.4 ms                                                               | 77.7 ms: 1.00x slower                                                      |
| pickle_pure_python | 300 us                                                                | 305 us: 1.02x slower                                                       |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (6): xml_etree_parse, json_loads, unpickle_pure_python, xml_etree_iterparse, tomli_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                               | 7.11 ms: 1.01x faster                                                      |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                      |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 36.8 ms                                                               | 35.5 ms: 1.04x faster                                                      |
| genshi_text     | 24.7 ms                                                               | 25.9 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark              | bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d | bm-20240821-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-bfdd616 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template        | 36.8 ms                                                               | 35.5 ms: 1.04x faster                                                      |
| coroutines             | 23.5 ms                                                               | 23.0 ms: 1.02x faster                                                      |
| bpe_tokeniser          | 4.52 sec                                                              | 4.44 sec: 1.02x faster                                                     |
| nqueens                | 87.2 ms                                                               | 85.8 ms: 1.02x faster                                                      |
| logging_simple         | 5.58 us                                                               | 5.50 us: 1.02x faster                                                      |
| logging_format         | 6.10 us                                                               | 6.04 us: 1.01x faster                                                      |
| nbody                  | 80.4 ms                                                               | 79.6 ms: 1.01x faster                                                      |
| json_dumps             | 10.1 ms                                                               | 10.0 ms: 1.01x faster                                                      |
| sympy_sum              | 177 ms                                                                | 176 ms: 1.01x faster                                                       |
| asyncio_tcp            | 497 ms                                                                | 493 ms: 1.01x faster                                                       |
| fannkuch               | 370 ms                                                                | 367 ms: 1.01x faster                                                       |
| create_gc_cycles       | 1.74 ms                                                               | 1.73 ms: 1.01x faster                                                      |
| coverage               | 85.5 ms                                                               | 84.9 ms: 1.01x faster                                                      |
| sympy_integrate        | 23.1 ms                                                               | 23.0 ms: 1.01x faster                                                      |
| python_startup_no_site | 7.14 ms                                                               | 7.11 ms: 1.01x faster                                                      |
| 2to3                   | 284 ms                                                                | 283 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl        | 1.80 sec                                                              | 1.80 sec: 1.00x faster                                                     |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                      |
| bench_thread_pool      | 822 us                                                                | 821 us: 1.00x faster                                                       |
| regex_compile          | 141 ms                                                                | 142 ms: 1.00x slower                                                       |
| pidigits               | 186 ms                                                                | 186 ms: 1.00x slower                                                       |
| float                  | 70.4 ms                                                               | 70.7 ms: 1.00x slower                                                      |
| xml_etree_generate     | 77.4 ms                                                               | 77.7 ms: 1.00x slower                                                      |
| html5lib               | 66.2 ms                                                               | 66.6 ms: 1.01x slower                                                      |
| deltablue              | 3.13 ms                                                               | 3.15 ms: 1.01x slower                                                      |
| hexiom                 | 6.78 ms                                                               | 6.83 ms: 1.01x slower                                                      |
| sqlglot_normalize      | 114 ms                                                                | 115 ms: 1.01x slower                                                       |
| async_tree_none        | 322 ms                                                                | 325 ms: 1.01x slower                                                       |
| scimark_fft            | 310 ms                                                                | 313 ms: 1.01x slower                                                       |
| scimark_lu             | 110 ms                                                                | 111 ms: 1.01x slower                                                       |
| tornado_http           | 93.3 ms                                                               | 94.3 ms: 1.01x slower                                                      |
| deepcopy_reduce        | 2.71 us                                                               | 2.75 us: 1.01x slower                                                      |
| go                     | 144 ms                                                                | 146 ms: 1.01x slower                                                       |
| chaos                  | 58.4 ms                                                               | 59.2 ms: 1.01x slower                                                      |
| pickle_pure_python     | 300 us                                                                | 305 us: 1.02x slower                                                       |
| regex_dna              | 215 ms                                                                | 218 ms: 1.02x slower                                                       |
| deepcopy_memo          | 26.6 us                                                               | 27.1 us: 1.02x slower                                                      |
| logging_silent         | 98.2 ns                                                               | 100 ns: 1.02x slower                                                       |
| spectral_norm          | 98.9 ms                                                               | 101 ms: 1.03x slower                                                       |
| pprint_safe_repr       | 750 ms                                                                | 771 ms: 1.03x slower                                                       |
| pyflate                | 430 ms                                                                | 442 ms: 1.03x slower                                                       |
| scimark_monte_carlo    | 61.9 ms                                                               | 63.8 ms: 1.03x slower                                                      |
| regex_v8               | 24.3 ms                                                               | 25.2 ms: 1.04x slower                                                      |
| genshi_text            | 24.7 ms                                                               | 25.9 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                               |

Benchmark hidden because not significant (45): scimark_sparse_mat_mult, pycparser, pylint, crypto_pyaes, xml_etree_parse, async_tree_io_tg, json_loads, telco, unpickle_pure_python, sqlglot_transpile, meteor_contest, comprehensions, mdp, async_generators, regex_effbot, generators, sqlglot_optimize, pathlib, thrift, gc_traversal, docutils, pprint_pformat, richards_super, async_tree_memoization, richards, sympy_str, sympy_expand, bench_mp_pool, typing_runtime_protocols, asyncio_websockets, xml_etree_iterparse, deepcopy, mako, async_tree_cpu_io_mixed_tg, tomli_loads, json, xml_etree_process, async_tree_cpu_io_mixed, sqlglot_parse, async_tree_none_tg, genshi_xml, scimark_sor, raytrace, async_tree_memoization_tg, async_tree_io

# HPT report

- Reliability score: 95.67% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x