# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.69 sec                                                                   | 1.71 sec: 1.01x slower                                                     |
| html5lib       | 40.4 ms                                                                    | 39.7 ms: 1.02x faster                                                      |
| tornado_http   | 92.8 ms                                                                    | 93.8 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines             | 14.2 ms                                                                    | 14.6 ms: 1.03x slower                                                      |
| async_tree_memoization | 254 ms                                                                     | 264 ms: 1.04x slower                                                       |
| async_generators       | 238 ms                                                                     | 251 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                                      | 1.02x slower                                                               |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none_tg, async_tree_none, async_tree_io_tg, asyncio_tcp, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 151 ms                                                                     | 151 ms: 1.00x slower                                                       |
| nbody          | 85.1 ms                                                                    | 87.8 ms: 1.03x slower                                                      |
| float          | 56.0 ms                                                                    | 58.6 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.03x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.55 ms                                                                    | 1.59 ms: 1.02x slower                                                      |
| regex_compile  | 89.9 ms                                                                    | 92.4 ms: 1.03x slower                                                      |
| regex_dna      | 115 ms                                                                     | 120 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                      | 1.03x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.1 ms                                                                    | 66.3 ms: 1.02x slower                                                      |
| xml_etree_generate   | 58.2 ms                                                                    | 59.4 ms: 1.02x slower                                                      |
| pickle_pure_python   | 209 us                                                                     | 214 us: 1.02x slower                                                       |
| xml_etree_process    | 41.0 ms                                                                    | 42.3 ms: 1.03x slower                                                      |
| json_loads           | 14.0 us                                                                    | 14.5 us: 1.03x slower                                                      |
| tomli_loads          | 1.57 sec                                                                   | 1.62 sec: 1.03x slower                                                     |
| unpickle_pure_python | 148 us                                                                     | 155 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                                      | 1.02x slower                                                               |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 22.0 ms                                                                    | 22.4 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 36.9 ms                                                                    | 35.9 ms: 1.03x faster                                                      |
| genshi_text     | 16.9 ms                                                                    | 17.2 ms: 1.02x slower                                                      |
| mako            | 6.99 ms                                                                    | 7.12 ms: 1.02x slower                                                      |
| django_template | 24.7 ms                                                                    | 25.5 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                                      | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark               | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators              | 21.1 ms                                                                    | 20.5 ms: 1.03x faster                                                      |
| genshi_xml              | 36.9 ms                                                                    | 35.9 ms: 1.03x faster                                                      |
| bench_mp_pool           | 70.3 ms                                                                    | 69.0 ms: 1.02x faster                                                      |
| html5lib                | 40.4 ms                                                                    | 39.7 ms: 1.02x faster                                                      |
| richards                | 32.4 ms                                                                    | 32.5 ms: 1.00x slower                                                      |
| pidigits                | 151 ms                                                                     | 151 ms: 1.00x slower                                                       |
| docutils                | 1.69 sec                                                                   | 1.71 sec: 1.01x slower                                                     |
| dulwich_log             | 42.6 ms                                                                    | 42.9 ms: 1.01x slower                                                      |
| tornado_http            | 92.8 ms                                                                    | 93.8 ms: 1.01x slower                                                      |
| sqlglot_optimize        | 36.2 ms                                                                    | 36.6 ms: 1.01x slower                                                      |
| sympy_expand            | 301 ms                                                                     | 305 ms: 1.01x slower                                                       |
| sqlglot_normalize       | 191 ms                                                                     | 194 ms: 1.01x slower                                                       |
| richards_super          | 36.5 ms                                                                    | 37.2 ms: 1.02x slower                                                      |
| xml_etree_iterparse     | 65.1 ms                                                                    | 66.3 ms: 1.02x slower                                                      |
| genshi_text             | 16.9 ms                                                                    | 17.2 ms: 1.02x slower                                                      |
| python_startup          | 22.0 ms                                                                    | 22.4 ms: 1.02x slower                                                      |
| mako                    | 6.99 ms                                                                    | 7.12 ms: 1.02x slower                                                      |
| sympy_str               | 175 ms                                                                     | 178 ms: 1.02x slower                                                       |
| logging_format          | 6.72 us                                                                    | 6.85 us: 1.02x slower                                                      |
| sympy_sum               | 89.3 ms                                                                    | 91.1 ms: 1.02x slower                                                      |
| xml_etree_generate      | 58.2 ms                                                                    | 59.4 ms: 1.02x slower                                                      |
| deltablue               | 2.24 ms                                                                    | 2.28 ms: 1.02x slower                                                      |
| deepcopy                | 184 us                                                                     | 188 us: 1.02x slower                                                       |
| thrift                  | 510 us                                                                     | 521 us: 1.02x slower                                                       |
| pickle_pure_python      | 209 us                                                                     | 214 us: 1.02x slower                                                       |
| sympy_integrate         | 13.0 ms                                                                    | 13.3 ms: 1.02x slower                                                      |
| meteor_contest          | 77.7 ms                                                                    | 79.5 ms: 1.02x slower                                                      |
| regex_effbot            | 1.55 ms                                                                    | 1.59 ms: 1.02x slower                                                      |
| logging_simple          | 6.33 us                                                                    | 6.48 us: 1.02x slower                                                      |
| logging_silent          | 63.3 ns                                                                    | 64.8 ns: 1.02x slower                                                      |
| comprehensions          | 11.8 us                                                                    | 12.1 us: 1.02x slower                                                      |
| scimark_monte_carlo     | 50.3 ms                                                                    | 51.6 ms: 1.03x slower                                                      |
| regex_compile           | 89.9 ms                                                                    | 92.4 ms: 1.03x slower                                                      |
| coroutines              | 14.2 ms                                                                    | 14.6 ms: 1.03x slower                                                      |
| deepcopy_reduce         | 1.89 us                                                                    | 1.95 us: 1.03x slower                                                      |
| xml_etree_process       | 41.0 ms                                                                    | 42.3 ms: 1.03x slower                                                      |
| nbody                   | 85.1 ms                                                                    | 87.8 ms: 1.03x slower                                                      |
| go                      | 85.4 ms                                                                    | 88.1 ms: 1.03x slower                                                      |
| chaos                   | 43.0 ms                                                                    | 44.4 ms: 1.03x slower                                                      |
| mdp                     | 1.45 sec                                                                   | 1.50 sec: 1.03x slower                                                     |
| django_template         | 24.7 ms                                                                    | 25.5 ms: 1.03x slower                                                      |
| json_loads              | 14.0 us                                                                    | 14.5 us: 1.03x slower                                                      |
| pprint_pformat          | 1.11 sec                                                                   | 1.15 sec: 1.03x slower                                                     |
| nqueens                 | 62.6 ms                                                                    | 64.7 ms: 1.03x slower                                                      |
| tomli_loads             | 1.57 sec                                                                   | 1.62 sec: 1.03x slower                                                     |
| crypto_pyaes            | 47.7 ms                                                                    | 49.3 ms: 1.03x slower                                                      |
| sqlglot_parse           | 879 us                                                                     | 910 us: 1.04x slower                                                       |
| scimark_lu              | 63.0 ms                                                                    | 65.3 ms: 1.04x slower                                                      |
| pyflate                 | 316 ms                                                                     | 327 ms: 1.04x slower                                                       |
| sqlglot_transpile       | 1.09 ms                                                                    | 1.13 ms: 1.04x slower                                                      |
| telco                   | 5.01 ms                                                                    | 5.20 ms: 1.04x slower                                                      |
| scimark_sparse_mat_mult | 2.81 ms                                                                    | 2.92 ms: 1.04x slower                                                      |
| async_tree_memoization  | 254 ms                                                                     | 264 ms: 1.04x slower                                                       |
| regex_dna               | 115 ms                                                                     | 120 ms: 1.04x slower                                                       |
| raytrace                | 190 ms                                                                     | 198 ms: 1.04x slower                                                       |
| fannkuch                | 288 ms                                                                     | 300 ms: 1.04x slower                                                       |
| hexiom                  | 4.33 ms                                                                    | 4.52 ms: 1.04x slower                                                      |
| pprint_safe_repr        | 544 ms                                                                     | 569 ms: 1.05x slower                                                       |
| float                   | 56.0 ms                                                                    | 58.6 ms: 1.05x slower                                                      |
| scimark_fft             | 204 ms                                                                     | 214 ms: 1.05x slower                                                       |
| scimark_sor             | 89.4 ms                                                                    | 93.8 ms: 1.05x slower                                                      |
| unpickle_pure_python    | 148 us                                                                     | 155 us: 1.05x slower                                                       |
| async_generators        | 238 ms                                                                     | 251 ms: 1.05x slower                                                       |
| deepcopy_memo           | 20.1 us                                                                    | 21.2 us: 1.05x slower                                                      |
| coverage                | 47.0 ms                                                                    | 49.9 ms: 1.06x slower                                                      |
| spectral_norm           | 67.0 ms                                                                    | 72.2 ms: 1.08x slower                                                      |
| Geometric mean          | (ref)                                                                      | 1.02x slower                                                               |

Benchmark hidden because not significant (22): pycparser, json, json_dumps, pylint, python_startup_no_site, bench_thread_pool, xml_etree_parse, async_tree_cpu_io_mixed_tg, gc_traversal, async_tree_io, async_tree_cpu_io_mixed, 2to3, pathlib, async_tree_memoization_tg, typing_runtime_protocols, create_gc_cycles, async_tree_none_tg, async_tree_none, async_tree_io_tg, asyncio_tcp, regex_v8, asyncio_tcp_ssl

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown