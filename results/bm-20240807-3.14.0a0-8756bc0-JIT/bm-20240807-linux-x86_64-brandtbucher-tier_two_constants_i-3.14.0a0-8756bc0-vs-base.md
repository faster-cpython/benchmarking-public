# Results vs. base

- fork: brandtbucher
- ref: tier_two_constants_i
- machine: linux-x86_64
- commit hash: 8756bc0
- commit date: 2024-08-07
- overall geometric mean: 1.00x faster
- HPT reliability: 96.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 275 ms                                                                | 274 ms: 1.00x faster                                                        |
| docutils       | 2.92 sec                                                              | 2.90 sec: 1.01x faster                                                      |
| html5lib       | 63.8 ms                                                               | 65.9 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp_ssl  | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                                      |
| coroutines       | 22.9 ms                                                               | 23.1 ms: 1.01x slower                                                       |
| async_generators | 453 ms                                                                | 456 ms: 1.01x slower                                                        |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io, async_tree_memoization_tg, async_tree_none, asyncio_websockets, async_tree_none_tg, asyncio_tcp, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                | 186 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.83 ms                                                               | 3.58 ms: 1.07x faster                                                       |
| regex_compile  | 135 ms                                                                | 134 ms: 1.00x faster                                                        |
| regex_v8       | 24.4 ms                                                               | 24.5 ms: 1.00x slower                                                       |
| regex_dna      | 223 ms                                                                | 224 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 81.6 ms                                                               | 79.7 ms: 1.02x faster                                                       |
| xml_etree_process    | 57.2 ms                                                               | 56.3 ms: 1.02x faster                                                       |
| pickle_pure_python   | 300 us                                                                | 295 us: 1.02x faster                                                        |
| unpickle_pure_python | 215 us                                                                | 214 us: 1.00x faster                                                        |
| json_loads           | 27.7 us                                                               | 28.8 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (4): xml_etree_iterparse, tomli_loads, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.17 ms                                                               | 7.15 ms: 1.00x faster                                                       |
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text    | 24.5 ms                                                               | 24.0 ms: 1.02x faster                                                       |
| mako           | 9.85 ms                                                               | 9.71 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark              | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants_i-3.14.0a0-8756bc0 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot           | 3.83 ms                                                               | 3.58 ms: 1.07x faster                                                       |
| pycparser              | 1.19 sec                                                              | 1.13 sec: 1.05x faster                                                      |
| gc_traversal           | 3.85 ms                                                               | 3.67 ms: 1.05x faster                                                       |
| xml_etree_generate     | 81.6 ms                                                               | 79.7 ms: 1.02x faster                                                       |
| telco                  | 7.97 ms                                                               | 7.80 ms: 1.02x faster                                                       |
| scimark_sor            | 117 ms                                                                | 115 ms: 1.02x faster                                                        |
| genshi_text            | 24.5 ms                                                               | 24.0 ms: 1.02x faster                                                       |
| xml_etree_process      | 57.2 ms                                                               | 56.3 ms: 1.02x faster                                                       |
| pickle_pure_python     | 300 us                                                                | 295 us: 1.02x faster                                                        |
| logging_silent         | 104 ns                                                                | 103 ns: 1.02x faster                                                        |
| bpe_tokeniser          | 4.52 sec                                                              | 4.45 sec: 1.01x faster                                                      |
| mako                   | 9.85 ms                                                               | 9.71 ms: 1.01x faster                                                       |
| thrift                 | 797 us                                                                | 787 us: 1.01x faster                                                        |
| deepcopy_memo          | 29.1 us                                                               | 28.8 us: 1.01x faster                                                       |
| create_gc_cycles       | 1.78 ms                                                               | 1.76 ms: 1.01x faster                                                       |
| deltablue              | 3.58 ms                                                               | 3.54 ms: 1.01x faster                                                       |
| deepcopy               | 273 us                                                                | 271 us: 1.01x faster                                                        |
| crypto_pyaes           | 66.8 ms                                                               | 66.2 ms: 1.01x faster                                                       |
| hexiom                 | 6.71 ms                                                               | 6.66 ms: 1.01x faster                                                       |
| generators             | 32.9 ms                                                               | 32.6 ms: 1.01x faster                                                       |
| richards_super         | 47.5 ms                                                               | 47.2 ms: 1.01x faster                                                       |
| docutils               | 2.92 sec                                                              | 2.90 sec: 1.01x faster                                                      |
| sqlglot_optimize       | 55.9 ms                                                               | 55.6 ms: 1.00x faster                                                       |
| pathlib                | 16.1 ms                                                               | 16.0 ms: 1.00x faster                                                       |
| regex_compile          | 135 ms                                                                | 134 ms: 1.00x faster                                                        |
| sympy_integrate        | 22.6 ms                                                               | 22.5 ms: 1.00x faster                                                       |
| 2to3                   | 275 ms                                                                | 274 ms: 1.00x faster                                                        |
| unpickle_pure_python   | 215 us                                                                | 214 us: 1.00x faster                                                        |
| raytrace               | 269 ms                                                                | 268 ms: 1.00x faster                                                        |
| bench_thread_pool      | 822 us                                                                | 819 us: 1.00x faster                                                        |
| python_startup_no_site | 7.17 ms                                                               | 7.15 ms: 1.00x faster                                                       |
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.00x faster                                                       |
| pidigits               | 186 ms                                                                | 186 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl        | 1.81 sec                                                              | 1.81 sec: 1.00x slower                                                      |
| regex_v8               | 24.4 ms                                                               | 24.5 ms: 1.00x slower                                                       |
| sympy_str              | 298 ms                                                                | 299 ms: 1.01x slower                                                        |
| sqlglot_parse          | 1.29 ms                                                               | 1.30 ms: 1.01x slower                                                       |
| coroutines             | 22.9 ms                                                               | 23.1 ms: 1.01x slower                                                       |
| async_generators       | 453 ms                                                                | 456 ms: 1.01x slower                                                        |
| regex_dna              | 223 ms                                                                | 224 ms: 1.01x slower                                                        |
| pyflate                | 432 ms                                                                | 435 ms: 1.01x slower                                                        |
| scimark_fft            | 307 ms                                                                | 310 ms: 1.01x slower                                                        |
| scimark_monte_carlo    | 60.7 ms                                                               | 61.4 ms: 1.01x slower                                                       |
| pprint_pformat         | 1.49 sec                                                              | 1.51 sec: 1.02x slower                                                      |
| spectral_norm          | 100 ms                                                                | 102 ms: 1.02x slower                                                        |
| html5lib               | 63.8 ms                                                               | 65.9 ms: 1.03x slower                                                       |
| json_loads             | 27.7 us                                                               | 28.8 us: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                |

Benchmark hidden because not significant (42): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, deepcopy_reduce, async_tree_io, logging_format, genshi_xml, async_tree_memoization_tg, django_template, scimark_lu, typing_runtime_protocols, logging_simple, sympy_sum, meteor_contest, async_tree_none, nqueens, xml_etree_iterparse, scimark_sparse_mat_mult, sqlglot_transpile, go, pylint, nbody, bench_mp_pool, chaos, mdp, tornado_http, asyncio_websockets, fannkuch, float, richards, comprehensions, sqlglot_normalize, async_tree_none_tg, tomli_loads, coverage, asyncio_tcp, json_dumps, async_tree_io_tg, sympy_expand, json, pprint_safe_repr, xml_etree_parse

# HPT report

- Reliability score: 96.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x