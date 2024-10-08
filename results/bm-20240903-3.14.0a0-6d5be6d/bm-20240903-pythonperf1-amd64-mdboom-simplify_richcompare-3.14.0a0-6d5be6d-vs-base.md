# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.00x faster
- HPT reliability: 72.60%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.69 sec                                                                   | 1.71 sec: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| coroutines       | 14.2 ms                                                                    | 14.0 ms: 1.02x faster                                                      |
| async_generators | 238 ms                                                                     | 247 ms: 1.04x slower                                                       |
| Geometric mean   | (ref)                                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (10): async_tree_none_tg, async_tree_io, async_tree_none, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization, asyncio_tcp, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 85.1 ms                                                                    | 80.9 ms: 1.05x faster                                                      |
| float          | 56.0 ms                                                                    | 56.5 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 89.9 ms                                                                    | 91.4 ms: 1.02x slower                                                      |
| regex_effbot   | 1.55 ms                                                                    | 1.58 ms: 1.02x slower                                                      |
| regex_dna      | 115 ms                                                                     | 120 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 6.35 ms                                                                    | 6.28 ms: 1.01x faster                                                      |
| unpickle_pure_python | 148 us                                                                     | 148 us: 1.00x slower                                                       |
| tomli_loads          | 1.57 sec                                                                   | 1.58 sec: 1.01x slower                                                     |
| xml_etree_process    | 41.0 ms                                                                    | 41.5 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 65.1 ms                                                                    | 66.1 ms: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                                    | 14.4 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 36.9 ms                                                                    | 35.7 ms: 1.03x faster                                                      |
| genshi_text     | 16.9 ms                                                                    | 17.0 ms: 1.01x slower                                                      |
| django_template | 24.7 ms                                                                    | 24.9 ms: 1.01x slower                                                      |
| Geometric mean  | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pycparser               | 870 ms                                                                     | 744 ms: 1.17x faster                                                       |
| nbody                   | 85.1 ms                                                                    | 80.9 ms: 1.05x faster                                                      |
| scimark_sparse_mat_mult | 2.81 ms                                                                    | 2.70 ms: 1.04x faster                                                      |
| genshi_xml              | 36.9 ms                                                                    | 35.7 ms: 1.03x faster                                                      |
| bench_mp_pool           | 70.3 ms                                                                    | 68.5 ms: 1.03x faster                                                      |
| richards                | 32.4 ms                                                                    | 31.6 ms: 1.03x faster                                                      |
| scimark_monte_carlo     | 50.3 ms                                                                    | 49.2 ms: 1.02x faster                                                      |
| scimark_sor             | 89.4 ms                                                                    | 87.7 ms: 1.02x faster                                                      |
| coroutines              | 14.2 ms                                                                    | 14.0 ms: 1.02x faster                                                      |
| generators              | 21.1 ms                                                                    | 20.8 ms: 1.01x faster                                                      |
| richards_super          | 36.5 ms                                                                    | 36.1 ms: 1.01x faster                                                      |
| json_dumps              | 6.35 ms                                                                    | 6.28 ms: 1.01x faster                                                      |
| deepcopy_memo           | 20.1 us                                                                    | 19.9 us: 1.01x faster                                                      |
| go                      | 85.4 ms                                                                    | 84.5 ms: 1.01x faster                                                      |
| logging_silent          | 63.3 ns                                                                    | 62.7 ns: 1.01x faster                                                      |
| meteor_contest          | 77.7 ms                                                                    | 77.0 ms: 1.01x faster                                                      |
| scimark_lu              | 63.0 ms                                                                    | 62.6 ms: 1.01x faster                                                      |
| sqlglot_optimize        | 36.2 ms                                                                    | 35.9 ms: 1.01x faster                                                      |
| sqlglot_normalize       | 191 ms                                                                     | 190 ms: 1.00x faster                                                       |
| chaos                   | 43.0 ms                                                                    | 42.8 ms: 1.00x faster                                                      |
| deltablue               | 2.24 ms                                                                    | 2.23 ms: 1.00x faster                                                      |
| hexiom                  | 4.33 ms                                                                    | 4.32 ms: 1.00x faster                                                      |
| unpickle_pure_python    | 148 us                                                                     | 148 us: 1.00x slower                                                       |
| pprint_pformat          | 1.11 sec                                                                   | 1.12 sec: 1.00x slower                                                     |
| comprehensions          | 11.8 us                                                                    | 11.9 us: 1.00x slower                                                      |
| crypto_pyaes            | 47.7 ms                                                                    | 47.9 ms: 1.01x slower                                                      |
| dulwich_log             | 42.6 ms                                                                    | 42.8 ms: 1.01x slower                                                      |
| sqlglot_parse           | 879 us                                                                     | 884 us: 1.01x slower                                                       |
| docutils                | 1.69 sec                                                                   | 1.71 sec: 1.01x slower                                                     |
| sympy_sum               | 89.3 ms                                                                    | 89.9 ms: 1.01x slower                                                      |
| genshi_text             | 16.9 ms                                                                    | 17.0 ms: 1.01x slower                                                      |
| logging_simple          | 6.33 us                                                                    | 6.38 us: 1.01x slower                                                      |
| tomli_loads             | 1.57 sec                                                                   | 1.58 sec: 1.01x slower                                                     |
| float                   | 56.0 ms                                                                    | 56.5 ms: 1.01x slower                                                      |
| django_template         | 24.7 ms                                                                    | 24.9 ms: 1.01x slower                                                      |
| sqlglot_transpile       | 1.09 ms                                                                    | 1.11 ms: 1.01x slower                                                      |
| sympy_str               | 175 ms                                                                     | 177 ms: 1.01x slower                                                       |
| xml_etree_process       | 41.0 ms                                                                    | 41.5 ms: 1.01x slower                                                      |
| sympy_integrate         | 13.0 ms                                                                    | 13.2 ms: 1.01x slower                                                      |
| sympy_expand            | 301 ms                                                                     | 305 ms: 1.01x slower                                                       |
| logging_format          | 6.72 us                                                                    | 6.82 us: 1.01x slower                                                      |
| xml_etree_iterparse     | 65.1 ms                                                                    | 66.1 ms: 1.02x slower                                                      |
| regex_compile           | 89.9 ms                                                                    | 91.4 ms: 1.02x slower                                                      |
| deepcopy_reduce         | 1.89 us                                                                    | 1.92 us: 1.02x slower                                                      |
| regex_effbot            | 1.55 ms                                                                    | 1.58 ms: 1.02x slower                                                      |
| pyflate                 | 316 ms                                                                     | 323 ms: 1.02x slower                                                       |
| nqueens                 | 62.6 ms                                                                    | 64.0 ms: 1.02x slower                                                      |
| thrift                  | 510 us                                                                     | 522 us: 1.02x slower                                                       |
| deepcopy                | 184 us                                                                     | 189 us: 1.03x slower                                                       |
| json_loads              | 14.0 us                                                                    | 14.4 us: 1.03x slower                                                      |
| async_generators        | 238 ms                                                                     | 247 ms: 1.04x slower                                                       |
| coverage                | 47.0 ms                                                                    | 48.7 ms: 1.04x slower                                                      |
| regex_dna               | 115 ms                                                                     | 120 ms: 1.04x slower                                                       |
| mdp                     | 1.45 sec                                                                   | 1.56 sec: 1.07x slower                                                     |
| Geometric mean          | (ref)                                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (34): regex_v8, async_tree_none_tg, async_tree_io, mako, async_tree_none, 2to3, async_tree_io_tg, async_tree_cpu_io_mixed_tg, python_startup_no_site, pathlib, bench_thread_pool, create_gc_cycles, python_startup, pprint_safe_repr, json, async_tree_memoization_tg, xml_etree_parse, typing_runtime_protocols, gc_traversal, async_tree_cpu_io_mixed, pidigits, pylint, spectral_norm, async_tree_memoization, fannkuch, html5lib, telco, xml_etree_generate, pickle_pure_python, raytrace, tornado_http, asyncio_tcp, asyncio_tcp_ssl, scimark_fft

# HPT report

- Reliability score: 72.60% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown