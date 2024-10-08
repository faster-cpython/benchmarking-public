# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 230 ms                                                                     | 228 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators | 247 ms                                                                     | 243 ms: 1.01x faster                                                       |
| coroutines       | 14.3 ms                                                                    | 14.2 ms: 1.01x faster                                                      |
| Geometric mean   | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (10): async_tree_memoization, async_tree_io_tg, asyncio_tcp, async_tree_none_tg, async_tree_none, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 89.2 ms                                                                    | 82.8 ms: 1.08x faster                                                      |
| float          | 57.0 ms                                                                    | 55.9 ms: 1.02x faster                                                      |
| pidigits       | 150 ms                                                                     | 151 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.64 ms                                                                    | 1.61 ms: 1.02x faster                                                      |
| regex_dna      | 124 ms                                                                     | 123 ms: 1.01x faster                                                       |
| regex_compile  | 91.2 ms                                                                    | 90.9 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                                   | 1.58 sec: 1.04x faster                                                     |
| unpickle_pure_python | 155 us                                                                     | 149 us: 1.04x faster                                                       |
| xml_etree_process    | 41.9 ms                                                                    | 40.5 ms: 1.03x faster                                                      |
| pickle_pure_python   | 217 us                                                                     | 210 us: 1.03x faster                                                       |
| xml_etree_generate   | 59.5 ms                                                                    | 57.7 ms: 1.03x faster                                                      |
| xml_etree_parse      | 94.4 ms                                                                    | 95.0 ms: 1.01x slower                                                      |
| json_loads           | 14.4 us                                                                    | 14.5 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                      | 1.02x faster                                                               |

Benchmark hidden because not significant (2): json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.17 ms                                                                    | 6.90 ms: 1.04x faster                                                      |
| django_template | 25.0 ms                                                                    | 24.3 ms: 1.03x faster                                                      |
| Geometric mean  | (ref)                                                                      | 1.02x faster                                                               |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| scimark_sparse_mat_mult | 2.89 ms                                                                    | 2.63 ms: 1.10x faster                                                      |
| scimark_fft             | 214 ms                                                                     | 197 ms: 1.08x faster                                                       |
| nbody                   | 89.2 ms                                                                    | 82.8 ms: 1.08x faster                                                      |
| scimark_sor             | 95.7 ms                                                                    | 89.4 ms: 1.07x faster                                                      |
| scimark_monte_carlo     | 52.4 ms                                                                    | 49.0 ms: 1.07x faster                                                      |
| deepcopy_memo           | 21.3 us                                                                    | 20.0 us: 1.06x faster                                                      |
| spectral_norm           | 69.9 ms                                                                    | 66.0 ms: 1.06x faster                                                      |
| scimark_lu              | 64.6 ms                                                                    | 61.2 ms: 1.06x faster                                                      |
| fannkuch                | 303 ms                                                                     | 288 ms: 1.05x faster                                                       |
| tomli_loads             | 1.65 sec                                                                   | 1.58 sec: 1.04x faster                                                     |
| mako                    | 7.17 ms                                                                    | 6.90 ms: 1.04x faster                                                      |
| unpickle_pure_python    | 155 us                                                                     | 149 us: 1.04x faster                                                       |
| hexiom                  | 4.53 ms                                                                    | 4.37 ms: 1.03x faster                                                      |
| xml_etree_process       | 41.9 ms                                                                    | 40.5 ms: 1.03x faster                                                      |
| deepcopy                | 192 us                                                                     | 186 us: 1.03x faster                                                       |
| sqlglot_optimize        | 37.0 ms                                                                    | 35.9 ms: 1.03x faster                                                      |
| pickle_pure_python      | 217 us                                                                     | 210 us: 1.03x faster                                                       |
| nqueens                 | 65.8 ms                                                                    | 63.8 ms: 1.03x faster                                                      |
| chaos                   | 44.2 ms                                                                    | 42.8 ms: 1.03x faster                                                      |
| sqlglot_parse           | 913 us                                                                     | 886 us: 1.03x faster                                                       |
| xml_etree_generate      | 59.5 ms                                                                    | 57.7 ms: 1.03x faster                                                      |
| django_template         | 25.0 ms                                                                    | 24.3 ms: 1.03x faster                                                      |
| go                      | 87.6 ms                                                                    | 85.1 ms: 1.03x faster                                                      |
| sqlglot_transpile       | 1.14 ms                                                                    | 1.10 ms: 1.03x faster                                                      |
| sympy_expand            | 311 ms                                                                     | 303 ms: 1.03x faster                                                       |
| pprint_pformat          | 1.15 sec                                                                   | 1.12 sec: 1.03x faster                                                     |
| richards                | 32.6 ms                                                                    | 31.8 ms: 1.02x faster                                                      |
| pyflate                 | 329 ms                                                                     | 321 ms: 1.02x faster                                                       |
| dulwich_log             | 43.5 ms                                                                    | 42.5 ms: 1.02x faster                                                      |
| richards_super          | 36.9 ms                                                                    | 36.0 ms: 1.02x faster                                                      |
| crypto_pyaes            | 49.6 ms                                                                    | 48.5 ms: 1.02x faster                                                      |
| comprehensions          | 12.2 us                                                                    | 11.9 us: 1.02x faster                                                      |
| sqlglot_normalize       | 195 ms                                                                     | 191 ms: 1.02x faster                                                       |
| pprint_safe_repr        | 562 ms                                                                     | 551 ms: 1.02x faster                                                       |
| float                   | 57.0 ms                                                                    | 55.9 ms: 1.02x faster                                                      |
| raytrace                | 189 ms                                                                     | 185 ms: 1.02x faster                                                       |
| regex_effbot            | 1.64 ms                                                                    | 1.61 ms: 1.02x faster                                                      |
| deltablue               | 2.30 ms                                                                    | 2.26 ms: 1.02x faster                                                      |
| thrift                  | 522 us                                                                     | 514 us: 1.02x faster                                                       |
| sympy_sum               | 91.1 ms                                                                    | 89.6 ms: 1.02x faster                                                      |
| deepcopy_reduce         | 1.95 us                                                                    | 1.92 us: 1.01x faster                                                      |
| async_generators        | 247 ms                                                                     | 243 ms: 1.01x faster                                                       |
| coverage                | 49.4 ms                                                                    | 48.7 ms: 1.01x faster                                                      |
| sympy_str               | 178 ms                                                                     | 176 ms: 1.01x faster                                                       |
| logging_silent          | 64.4 ns                                                                    | 63.7 ns: 1.01x faster                                                      |
| coroutines              | 14.3 ms                                                                    | 14.2 ms: 1.01x faster                                                      |
| 2to3                    | 230 ms                                                                     | 228 ms: 1.01x faster                                                       |
| gc_traversal            | 1.57 ms                                                                    | 1.56 ms: 1.01x faster                                                      |
| regex_dna               | 124 ms                                                                     | 123 ms: 1.01x faster                                                       |
| regex_compile           | 91.2 ms                                                                    | 90.9 ms: 1.00x faster                                                      |
| mdp                     | 1.50 sec                                                                   | 1.50 sec: 1.00x slower                                                     |
| pidigits                | 150 ms                                                                     | 151 ms: 1.00x slower                                                       |
| xml_etree_parse         | 94.4 ms                                                                    | 95.0 ms: 1.01x slower                                                      |
| json_loads              | 14.4 us                                                                    | 14.5 us: 1.01x slower                                                      |
| json                    | 3.02 ms                                                                    | 3.07 ms: 1.02x slower                                                      |
| logging_simple          | 6.34 us                                                                    | 6.45 us: 1.02x slower                                                      |
| bench_mp_pool           | 69.2 ms                                                                    | 70.6 ms: 1.02x slower                                                      |
| generators              | 20.7 ms                                                                    | 21.1 ms: 1.02x slower                                                      |
| logging_format          | 6.77 us                                                                    | 6.91 us: 1.02x slower                                                      |
| telco                   | 5.14 ms                                                                    | 5.30 ms: 1.03x slower                                                      |
| Geometric mean          | (ref)                                                                      | 1.02x faster                                                               |

Benchmark hidden because not significant (28): async_tree_memoization, async_tree_io_tg, asyncio_tcp, pylint, async_tree_none_tg, async_tree_none, async_tree_memoization_tg, tornado_http, async_tree_io, genshi_xml, json_dumps, html5lib, sympy_integrate, docutils, async_tree_cpu_io_mixed_tg, genshi_text, pathlib, meteor_contest, regex_v8, xml_etree_iterparse, async_tree_cpu_io_mixed, create_gc_cycles, python_startup, typing_runtime_protocols, python_startup_no_site, pycparser, bench_thread_pool, asyncio_tcp_ssl

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown