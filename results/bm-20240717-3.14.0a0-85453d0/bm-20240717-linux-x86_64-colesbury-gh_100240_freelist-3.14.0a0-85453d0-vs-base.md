# Results vs. base

- fork: colesbury
- ref: gh_100240_freelist
- machine: linux-x86_64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.00x slower
- HPT reliability: 68.18%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240717-linux-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| html5lib       | 64.3 ms                                                               | 64.9 ms: 1.01x slower                                                  |
| tornado_http   | 90.3 ms                                                               | 90.0 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_none, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240717-linux-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 187 ms: 1.00x slower                                                   |
| nbody          | 85.6 ms                                                               | 86.9 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240717-linux-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 25.7 ms                                                               | 23.8 ms: 1.08x faster                                                  |
| regex_dna      | 224 ms                                                                | 216 ms: 1.04x faster                                                   |
| regex_effbot   | 3.72 ms                                                               | 3.66 ms: 1.02x faster                                                  |
| regex_compile  | 130 ms                                                                | 130 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240717-linux-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 10.3 ms                                                               | 10.3 ms: 1.01x faster                                                  |
| xml_etree_generate   | 84.9 ms                                                               | 85.6 ms: 1.01x slower                                                  |
| xml_etree_process    | 58.7 ms                                                               | 59.2 ms: 1.01x slower                                                  |
| unpickle_pure_python | 209 us                                                                | 212 us: 1.01x slower                                                   |
| pickle_pure_python   | 295 us                                                                | 300 us: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (4): json_loads, xml_etree_parse, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240717-linux-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                  |
| python_startup_no_site | 7.08 ms                                                               | 7.08 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240717-linux-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 33.5 ms                                                               | 33.8 ms: 1.01x slower                                                  |
| genshi_text     | 22.8 ms                                                               | 23.1 ms: 1.01x slower                                                  |
| mako            | 10.9 ms                                                               | 11.1 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                           |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20240717-linux-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-linux-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8                | 25.7 ms                                                               | 23.8 ms: 1.08x faster                                                  |
| gc_traversal            | 3.74 ms                                                               | 3.53 ms: 1.06x faster                                                  |
| regex_dna               | 224 ms                                                                | 216 ms: 1.04x faster                                                   |
| pycparser               | 1.17 sec                                                              | 1.13 sec: 1.03x faster                                                 |
| logging_silent          | 104 ns                                                                | 101 ns: 1.02x faster                                                   |
| regex_effbot            | 3.72 ms                                                               | 3.66 ms: 1.02x faster                                                  |
| telco                   | 8.17 ms                                                               | 8.03 ms: 1.02x faster                                                  |
| scimark_sparse_mat_mult | 4.67 ms                                                               | 4.59 ms: 1.02x faster                                                  |
| scimark_lu              | 113 ms                                                                | 111 ms: 1.01x faster                                                   |
| deepcopy_reduce         | 2.70 us                                                               | 2.66 us: 1.01x faster                                                  |
| bpe_tokeniser           | 4.85 sec                                                              | 4.80 sec: 1.01x faster                                                 |
| scimark_monte_carlo     | 67.0 ms                                                               | 66.4 ms: 1.01x faster                                                  |
| sympy_str               | 272 ms                                                                | 270 ms: 1.01x faster                                                   |
| json_dumps              | 10.3 ms                                                               | 10.3 ms: 1.01x faster                                                  |
| pathlib                 | 15.9 ms                                                               | 15.8 ms: 1.00x faster                                                  |
| tornado_http            | 90.3 ms                                                               | 90.0 ms: 1.00x faster                                                  |
| raytrace                | 259 ms                                                                | 258 ms: 1.00x faster                                                   |
| nqueens                 | 79.4 ms                                                               | 79.1 ms: 1.00x faster                                                  |
| mdp                     | 2.52 sec                                                              | 2.51 sec: 1.00x faster                                                 |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                                 |
| sympy_integrate         | 19.7 ms                                                               | 19.7 ms: 1.00x faster                                                  |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                  |
| python_startup_no_site  | 7.08 ms                                                               | 7.08 ms: 1.00x faster                                                  |
| pidigits                | 187 ms                                                                | 187 ms: 1.00x slower                                                   |
| chaos                   | 58.2 ms                                                               | 58.4 ms: 1.00x slower                                                  |
| create_gc_cycles        | 1.73 ms                                                               | 1.74 ms: 1.00x slower                                                  |
| pprint_safe_repr        | 730 ms                                                                | 734 ms: 1.01x slower                                                   |
| bench_thread_pool       | 782 us                                                                | 786 us: 1.01x slower                                                   |
| regex_compile           | 130 ms                                                                | 130 ms: 1.01x slower                                                   |
| deepcopy_memo           | 29.5 us                                                               | 29.7 us: 1.01x slower                                                  |
| comprehensions          | 16.5 us                                                               | 16.6 us: 1.01x slower                                                  |
| sqlglot_optimize        | 52.9 ms                                                               | 53.3 ms: 1.01x slower                                                  |
| logging_format          | 6.11 us                                                               | 6.16 us: 1.01x slower                                                  |
| xml_etree_generate      | 84.9 ms                                                               | 85.6 ms: 1.01x slower                                                  |
| xml_etree_process       | 58.7 ms                                                               | 59.2 ms: 1.01x slower                                                  |
| logging_simple          | 5.46 us                                                               | 5.51 us: 1.01x slower                                                  |
| hexiom                  | 6.11 ms                                                               | 6.16 ms: 1.01x slower                                                  |
| django_template         | 33.5 ms                                                               | 33.8 ms: 1.01x slower                                                  |
| unpickle_pure_python    | 209 us                                                                | 212 us: 1.01x slower                                                   |
| html5lib                | 64.3 ms                                                               | 64.9 ms: 1.01x slower                                                  |
| genshi_text             | 22.8 ms                                                               | 23.1 ms: 1.01x slower                                                  |
| sqlglot_transpile       | 1.56 ms                                                               | 1.58 ms: 1.01x slower                                                  |
| crypto_pyaes            | 71.2 ms                                                               | 72.1 ms: 1.01x slower                                                  |
| richards                | 46.1 ms                                                               | 46.6 ms: 1.01x slower                                                  |
| sqlglot_parse           | 1.27 ms                                                               | 1.29 ms: 1.01x slower                                                  |
| deltablue               | 3.20 ms                                                               | 3.24 ms: 1.01x slower                                                  |
| async_generators        | 432 ms                                                                | 438 ms: 1.01x slower                                                   |
| meteor_contest          | 107 ms                                                                | 109 ms: 1.01x slower                                                   |
| dulwich_log             | 63.5 ms                                                               | 64.4 ms: 1.01x slower                                                  |
| nbody                   | 85.6 ms                                                               | 86.9 ms: 1.02x slower                                                  |
| go                      | 139 ms                                                                | 141 ms: 1.02x slower                                                   |
| pyflate                 | 461 ms                                                                | 469 ms: 1.02x slower                                                   |
| pickle_pure_python      | 295 us                                                                | 300 us: 1.02x slower                                                   |
| richards_super          | 52.1 ms                                                               | 53.1 ms: 1.02x slower                                                  |
| generators              | 29.4 ms                                                               | 29.9 ms: 1.02x slower                                                  |
| scimark_fft             | 357 ms                                                                | 363 ms: 1.02x slower                                                   |
| coroutines              | 22.7 ms                                                               | 23.2 ms: 1.02x slower                                                  |
| mako                    | 10.9 ms                                                               | 11.1 ms: 1.03x slower                                                  |
| spectral_norm           | 110 ms                                                                | 113 ms: 1.03x slower                                                   |
| scimark_sor             | 125 ms                                                                | 129 ms: 1.04x slower                                                   |
| fannkuch                | 387 ms                                                                | 408 ms: 1.05x slower                                                   |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (29): async_tree_io, async_tree_none, json_loads, async_tree_memoization_tg, xml_etree_parse, async_tree_none_tg, async_tree_io_tg, sympy_expand, typing_runtime_protocols, pprint_pformat, async_tree_memoization, async_tree_cpu_io_mixed_tg, float, docutils, thrift, asyncio_tcp, pylint, bench_mp_pool, 2to3, deepcopy, async_tree_cpu_io_mixed, xml_etree_iterparse, json, sqlglot_normalize, asyncio_websockets, sympy_sum, genshi_xml, coverage, tomli_loads

# HPT report

- Reliability score: 68.18% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x