# Results vs. base

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: 85c5a08
- commit date: 2024-08-21
- overall geometric mean: 1.00x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 284 ms                                                                | 283 ms: 1.00x faster                                                      |
| docutils       | 3.05 sec                                                              | 3.06 sec: 1.00x slower                                                    |
| tornado_http   | 93.3 ms                                                               | 94.1 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines         | 23.5 ms                                                               | 22.7 ms: 1.04x faster                                                     |
| asyncio_tcp        | 497 ms                                                                | 496 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl    | 1.80 sec                                                              | 1.80 sec: 1.00x faster                                                    |
| async_generators   | 457 ms                                                                | 461 ms: 1.01x slower                                                      |
| async_tree_none_tg | 301 ms                                                                | 305 ms: 1.01x slower                                                      |
| async_tree_none    | 322 ms                                                                | 329 ms: 1.02x slower                                                      |
| Geometric mean     | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (7): async_tree_io_tg, asyncio_websockets, async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 186 ms: 1.00x slower                                                      |
| float          | 70.4 ms                                                               | 71.1 ms: 1.01x slower                                                     |
| nbody          | 80.4 ms                                                               | 82.2 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 24.3 ms                                                               | 23.8 ms: 1.02x faster                                                     |
| regex_effbot   | 3.58 ms                                                               | 3.55 ms: 1.01x faster                                                     |
| regex_compile  | 141 ms                                                                | 143 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads         | 28.6 us                                                               | 28.3 us: 1.01x faster                                                     |
| json_dumps         | 10.1 ms                                                               | 10.2 ms: 1.01x slower                                                     |
| xml_etree_generate | 77.4 ms                                                               | 78.1 ms: 1.01x slower                                                     |
| xml_etree_process  | 55.1 ms                                                               | 55.9 ms: 1.01x slower                                                     |
| pickle_pure_python | 300 us                                                                | 306 us: 1.02x slower                                                      |
| Geometric mean     | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (4): tomli_loads, unpickle_pure_python, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                               | 7.12 ms: 1.00x faster                                                     |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako           | 9.90 ms                                                               | 9.74 ms: 1.02x faster                                                     |
| genshi_xml     | 59.2 ms                                                               | 60.0 ms: 1.01x slower                                                     |
| genshi_text    | 24.7 ms                                                               | 25.6 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240820-linux-x86_64-python-f88c14d412522587085a-3.14.0a0-f88c14d | bm-20240821-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-85c5a08 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines               | 23.5 ms                                                               | 22.7 ms: 1.04x faster                                                     |
| deepcopy_reduce          | 2.71 us                                                               | 2.64 us: 1.03x faster                                                     |
| regex_v8                 | 24.3 ms                                                               | 23.8 ms: 1.02x faster                                                     |
| crypto_pyaes             | 66.5 ms                                                               | 65.3 ms: 1.02x faster                                                     |
| logging_format           | 6.10 us                                                               | 6.00 us: 1.02x faster                                                     |
| mako                     | 9.90 ms                                                               | 9.74 ms: 1.02x faster                                                     |
| logging_simple           | 5.58 us                                                               | 5.51 us: 1.01x faster                                                     |
| nqueens                  | 87.2 ms                                                               | 86.1 ms: 1.01x faster                                                     |
| deepcopy                 | 269 us                                                                | 266 us: 1.01x faster                                                      |
| json_loads               | 28.6 us                                                               | 28.3 us: 1.01x faster                                                     |
| regex_effbot             | 3.58 ms                                                               | 3.55 ms: 1.01x faster                                                     |
| thrift                   | 793 us                                                                | 787 us: 1.01x faster                                                      |
| telco                    | 7.74 ms                                                               | 7.69 ms: 1.01x faster                                                     |
| scimark_fft              | 310 ms                                                                | 308 ms: 1.01x faster                                                      |
| bpe_tokeniser            | 4.52 sec                                                              | 4.49 sec: 1.01x faster                                                    |
| 2to3                     | 284 ms                                                                | 283 ms: 1.00x faster                                                      |
| python_startup_no_site   | 7.14 ms                                                               | 7.12 ms: 1.00x faster                                                     |
| gc_traversal             | 3.57 ms                                                               | 3.56 ms: 1.00x faster                                                     |
| create_gc_cycles         | 1.74 ms                                                               | 1.74 ms: 1.00x faster                                                     |
| asyncio_tcp              | 497 ms                                                                | 496 ms: 1.00x faster                                                      |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.80 sec: 1.00x faster                                                    |
| pidigits                 | 186 ms                                                                | 186 ms: 1.00x slower                                                      |
| docutils                 | 3.05 sec                                                              | 3.06 sec: 1.00x slower                                                    |
| sympy_sum                | 177 ms                                                                | 178 ms: 1.00x slower                                                      |
| deltablue                | 3.13 ms                                                               | 3.14 ms: 1.00x slower                                                     |
| richards                 | 39.3 ms                                                               | 39.4 ms: 1.00x slower                                                     |
| sympy_expand             | 511 ms                                                                | 514 ms: 1.01x slower                                                      |
| sympy_integrate          | 23.1 ms                                                               | 23.3 ms: 1.01x slower                                                     |
| sqlglot_normalize        | 114 ms                                                                | 115 ms: 1.01x slower                                                      |
| meteor_contest           | 106 ms                                                                | 106 ms: 1.01x slower                                                      |
| spectral_norm            | 98.9 ms                                                               | 99.6 ms: 1.01x slower                                                     |
| fannkuch                 | 370 ms                                                                | 373 ms: 1.01x slower                                                      |
| sqlglot_parse            | 1.31 ms                                                               | 1.32 ms: 1.01x slower                                                     |
| sympy_str                | 304 ms                                                                | 306 ms: 1.01x slower                                                      |
| sqlglot_transpile        | 1.68 ms                                                               | 1.70 ms: 1.01x slower                                                     |
| tornado_http             | 93.3 ms                                                               | 94.1 ms: 1.01x slower                                                     |
| chaos                    | 58.4 ms                                                               | 58.9 ms: 1.01x slower                                                     |
| async_generators         | 457 ms                                                                | 461 ms: 1.01x slower                                                      |
| float                    | 70.4 ms                                                               | 71.1 ms: 1.01x slower                                                     |
| json_dumps               | 10.1 ms                                                               | 10.2 ms: 1.01x slower                                                     |
| xml_etree_generate       | 77.4 ms                                                               | 78.1 ms: 1.01x slower                                                     |
| scimark_monte_carlo      | 61.9 ms                                                               | 62.6 ms: 1.01x slower                                                     |
| regex_compile            | 141 ms                                                                | 143 ms: 1.01x slower                                                      |
| pathlib                  | 15.9 ms                                                               | 16.1 ms: 1.01x slower                                                     |
| scimark_lu               | 110 ms                                                                | 111 ms: 1.01x slower                                                      |
| genshi_xml               | 59.2 ms                                                               | 60.0 ms: 1.01x slower                                                     |
| pycparser                | 1.16 sec                                                              | 1.18 sec: 1.01x slower                                                    |
| raytrace                 | 271 ms                                                                | 274 ms: 1.01x slower                                                      |
| xml_etree_process        | 55.1 ms                                                               | 55.9 ms: 1.01x slower                                                     |
| hexiom                   | 6.78 ms                                                               | 6.87 ms: 1.01x slower                                                     |
| async_tree_none_tg       | 301 ms                                                                | 305 ms: 1.01x slower                                                      |
| typing_runtime_protocols | 167 us                                                                | 170 us: 1.02x slower                                                      |
| pickle_pure_python       | 300 us                                                                | 306 us: 1.02x slower                                                      |
| async_tree_none          | 322 ms                                                                | 329 ms: 1.02x slower                                                      |
| pyflate                  | 430 ms                                                                | 438 ms: 1.02x slower                                                      |
| nbody                    | 80.4 ms                                                               | 82.2 ms: 1.02x slower                                                     |
| deepcopy_memo            | 26.6 us                                                               | 27.3 us: 1.02x slower                                                     |
| go                       | 144 ms                                                                | 148 ms: 1.03x slower                                                      |
| genshi_text              | 24.7 ms                                                               | 25.6 ms: 1.04x slower                                                     |
| logging_silent           | 98.2 ns                                                               | 103 ns: 1.05x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (28): scimark_sparse_mat_mult, pprint_pformat, coverage, generators, richards_super, scimark_sor, mdp, tomli_loads, sqlglot_optimize, regex_dna, unpickle_pure_python, bench_thread_pool, bench_mp_pool, async_tree_io_tg, asyncio_websockets, django_template, comprehensions, xml_etree_iterparse, html5lib, pylint, xml_etree_parse, json, pprint_safe_repr, async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg

# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x