# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.00x slower
- HPT reliability: 97.79%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 226 ms                                                                     | 228 ms: 1.01x slower                                                       |
| docutils       | 1.69 sec                                                                   | 1.70 sec: 1.00x slower                                                     |
| html5lib       | 39.6 ms                                                                    | 40.2 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none        | 207 ms                                                                     | 213 ms: 1.03x slower                                                       |
| async_tree_memoization | 257 ms                                                                     | 266 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (10): asyncio_tcp_ssl, async_tree_cpu_io_mixed, asyncio_tcp, async_generators, async_tree_cpu_io_mixed_tg, coroutines, async_tree_io, async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 84.9 ms                                                                    | 88.1 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 16.7 ms                                                                    | 14.5 ms: 1.15x faster                                                      |
| regex_dna      | 120 ms                                                                     | 115 ms: 1.04x faster                                                       |
| regex_effbot   | 1.59 ms                                                                    | 1.55 ms: 1.03x faster                                                      |
| regex_compile  | 89.9 ms                                                                    | 91.6 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 60.6 ms                                                                    | 57.6 ms: 1.05x faster                                                      |
| xml_etree_process    | 43.5 ms                                                                    | 41.3 ms: 1.05x faster                                                      |
| json_loads           | 14.4 us                                                                    | 14.2 us: 1.01x faster                                                      |
| pickle_pure_python   | 215 us                                                                     | 212 us: 1.01x faster                                                       |
| tomli_loads          | 1.62 sec                                                                   | 1.60 sec: 1.01x faster                                                     |
| unpickle_pure_python | 152 us                                                                     | 155 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 65.3 ms                                                                    | 66.6 ms: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 21.9 ms                                                                    | 22.2 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 25.1 ms                                                                    | 24.7 ms: 1.01x faster                                                      |
| genshi_text     | 16.9 ms                                                                    | 17.7 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|--------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8                 | 16.7 ms                                                                    | 14.5 ms: 1.15x faster                                                      |
| scimark_sparse_mat_mult  | 2.91 ms                                                                    | 2.69 ms: 1.08x faster                                                      |
| deepcopy_memo            | 22.1 us                                                                    | 20.7 us: 1.07x faster                                                      |
| xml_etree_generate       | 60.6 ms                                                                    | 57.6 ms: 1.05x faster                                                      |
| xml_etree_process        | 43.5 ms                                                                    | 41.3 ms: 1.05x faster                                                      |
| regex_dna                | 120 ms                                                                     | 115 ms: 1.04x faster                                                       |
| sqlglot_optimize         | 36.9 ms                                                                    | 35.7 ms: 1.03x faster                                                      |
| regex_effbot             | 1.59 ms                                                                    | 1.55 ms: 1.03x faster                                                      |
| generators               | 21.0 ms                                                                    | 20.7 ms: 1.02x faster                                                      |
| sympy_expand             | 307 ms                                                                     | 303 ms: 1.02x faster                                                       |
| json_loads               | 14.4 us                                                                    | 14.2 us: 1.01x faster                                                      |
| deepcopy_reduce          | 1.94 us                                                                    | 1.92 us: 1.01x faster                                                      |
| django_template          | 25.1 ms                                                                    | 24.7 ms: 1.01x faster                                                      |
| pickle_pure_python       | 215 us                                                                     | 212 us: 1.01x faster                                                       |
| nqueens                  | 64.9 ms                                                                    | 64.1 ms: 1.01x faster                                                      |
| meteor_contest           | 79.6 ms                                                                    | 78.8 ms: 1.01x faster                                                      |
| tomli_loads              | 1.62 sec                                                                   | 1.60 sec: 1.01x faster                                                     |
| docutils                 | 1.69 sec                                                                   | 1.70 sec: 1.00x slower                                                     |
| scimark_monte_carlo      | 50.6 ms                                                                    | 50.9 ms: 1.01x slower                                                      |
| sqlglot_transpile        | 1.11 ms                                                                    | 1.12 ms: 1.01x slower                                                      |
| 2to3                     | 226 ms                                                                     | 228 ms: 1.01x slower                                                       |
| pyflate                  | 323 ms                                                                     | 326 ms: 1.01x slower                                                       |
| pathlib                  | 78.7 ms                                                                    | 79.5 ms: 1.01x slower                                                      |
| deltablue                | 2.25 ms                                                                    | 2.28 ms: 1.01x slower                                                      |
| scimark_sor              | 91.7 ms                                                                    | 92.7 ms: 1.01x slower                                                      |
| scimark_fft              | 209 ms                                                                     | 211 ms: 1.01x slower                                                       |
| python_startup           | 21.9 ms                                                                    | 22.2 ms: 1.01x slower                                                      |
| mdp                      | 1.49 sec                                                                   | 1.51 sec: 1.01x slower                                                     |
| sympy_integrate          | 13.1 ms                                                                    | 13.3 ms: 1.01x slower                                                      |
| logging_format           | 6.70 us                                                                    | 6.79 us: 1.01x slower                                                      |
| richards_super           | 36.2 ms                                                                    | 36.7 ms: 1.01x slower                                                      |
| pprint_pformat           | 1.13 sec                                                                   | 1.15 sec: 1.01x slower                                                     |
| thrift                   | 511 us                                                                     | 519 us: 1.01x slower                                                       |
| html5lib                 | 39.6 ms                                                                    | 40.2 ms: 1.02x slower                                                      |
| telco                    | 5.08 ms                                                                    | 5.16 ms: 1.02x slower                                                      |
| crypto_pyaes             | 48.9 ms                                                                    | 49.8 ms: 1.02x slower                                                      |
| create_gc_cycles         | 900 us                                                                     | 917 us: 1.02x slower                                                       |
| unpickle_pure_python     | 152 us                                                                     | 155 us: 1.02x slower                                                       |
| chaos                    | 43.4 ms                                                                    | 44.2 ms: 1.02x slower                                                      |
| regex_compile            | 89.9 ms                                                                    | 91.6 ms: 1.02x slower                                                      |
| scimark_lu               | 61.9 ms                                                                    | 63.1 ms: 1.02x slower                                                      |
| xml_etree_iterparse      | 65.3 ms                                                                    | 66.6 ms: 1.02x slower                                                      |
| typing_runtime_protocols | 111 us                                                                     | 114 us: 1.02x slower                                                       |
| bench_mp_pool            | 68.7 ms                                                                    | 70.3 ms: 1.02x slower                                                      |
| go                       | 86.4 ms                                                                    | 88.6 ms: 1.03x slower                                                      |
| logging_silent           | 62.8 ns                                                                    | 64.4 ns: 1.03x slower                                                      |
| pprint_safe_repr         | 548 ms                                                                     | 563 ms: 1.03x slower                                                       |
| async_tree_none          | 207 ms                                                                     | 213 ms: 1.03x slower                                                       |
| hexiom                   | 4.41 ms                                                                    | 4.56 ms: 1.03x slower                                                      |
| async_tree_memoization   | 257 ms                                                                     | 266 ms: 1.03x slower                                                       |
| nbody                    | 84.9 ms                                                                    | 88.1 ms: 1.04x slower                                                      |
| fannkuch                 | 295 ms                                                                     | 307 ms: 1.04x slower                                                       |
| genshi_text              | 16.9 ms                                                                    | 17.7 ms: 1.05x slower                                                      |
| spectral_norm            | 70.4 ms                                                                    | 73.9 ms: 1.05x slower                                                      |
| Geometric mean           | (ref)                                                                      | 1.00x slower                                                               |

Benchmark hidden because not significant (34): pycparser, asyncio_tcp_ssl, mako, sqlglot_normalize, float, deepcopy, coverage, json, sympy_sum, json_dumps, tornado_http, pidigits, sqlglot_parse, async_tree_cpu_io_mixed, sympy_str, richards, asyncio_tcp, comprehensions, gc_traversal, xml_etree_parse, logging_simple, async_generators, async_tree_cpu_io_mixed_tg, dulwich_log, coroutines, pylint, async_tree_io, bench_thread_pool, async_tree_memoization_tg, python_startup_no_site, raytrace, async_tree_io_tg, genshi_xml, async_tree_none_tg

# HPT report

- Reliability score: 97.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown