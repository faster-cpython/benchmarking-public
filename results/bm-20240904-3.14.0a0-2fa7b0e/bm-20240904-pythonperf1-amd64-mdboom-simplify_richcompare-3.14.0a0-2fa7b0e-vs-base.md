# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.01x faster
- HPT reliability: 99.13%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 230 ms                                                                     | 228 ms: 1.01x faster                                                       |
| tornado_http   | 93.8 ms                                                                    | 93.2 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp    | 538 ms                                                                     | 522 ms: 1.03x faster                                                       |
| coroutines     | 14.3 ms                                                                    | 14.5 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (10): async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_generators, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none, async_tree_memoization, async_tree_none_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 89.2 ms                                                                    | 88.1 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                               |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 124 ms                                                                     | 115 ms: 1.08x faster                                                       |
| regex_v8       | 15.6 ms                                                                    | 14.5 ms: 1.08x faster                                                      |
| regex_effbot   | 1.64 ms                                                                    | 1.55 ms: 1.06x faster                                                      |
| regex_compile  | 91.2 ms                                                                    | 91.6 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                      | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|---------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate  | 59.5 ms                                                                    | 57.6 ms: 1.03x faster                                                      |
| tomli_loads         | 1.65 sec                                                                   | 1.60 sec: 1.03x faster                                                     |
| pickle_pure_python  | 217 us                                                                     | 212 us: 1.02x faster                                                       |
| json_loads          | 14.4 us                                                                    | 14.2 us: 1.01x faster                                                      |
| xml_etree_process   | 41.9 ms                                                                    | 41.3 ms: 1.01x faster                                                      |
| xml_etree_parse     | 94.4 ms                                                                    | 93.5 ms: 1.01x faster                                                      |
| xml_etree_iterparse | 65.8 ms                                                                    | 66.6 ms: 1.01x slower                                                      |
| Geometric mean      | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (2): json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.17 ms                                                                    | 7.04 ms: 1.02x faster                                                      |
| django_template | 25.0 ms                                                                    | 24.7 ms: 1.01x faster                                                      |
| genshi_text     | 16.9 ms                                                                    | 17.7 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                                      | 1.01x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240829-pythonperf1-amd64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240904-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|--------------------------|:--------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna                | 124 ms                                                                     | 115 ms: 1.08x faster                                                       |
| regex_v8                 | 15.6 ms                                                                    | 14.5 ms: 1.08x faster                                                      |
| scimark_sparse_mat_mult  | 2.89 ms                                                                    | 2.69 ms: 1.08x faster                                                      |
| regex_effbot             | 1.64 ms                                                                    | 1.55 ms: 1.06x faster                                                      |
| sqlglot_optimize         | 37.0 ms                                                                    | 35.7 ms: 1.04x faster                                                      |
| xml_etree_generate       | 59.5 ms                                                                    | 57.6 ms: 1.03x faster                                                      |
| scimark_sor              | 95.7 ms                                                                    | 92.7 ms: 1.03x faster                                                      |
| asyncio_tcp              | 538 ms                                                                     | 522 ms: 1.03x faster                                                       |
| deepcopy_memo            | 21.3 us                                                                    | 20.7 us: 1.03x faster                                                      |
| tomli_loads              | 1.65 sec                                                                   | 1.60 sec: 1.03x faster                                                     |
| sympy_expand             | 311 ms                                                                     | 303 ms: 1.03x faster                                                       |
| scimark_monte_carlo      | 52.4 ms                                                                    | 50.9 ms: 1.03x faster                                                      |
| nqueens                  | 65.8 ms                                                                    | 64.1 ms: 1.03x faster                                                      |
| dulwich_log              | 43.5 ms                                                                    | 42.4 ms: 1.03x faster                                                      |
| scimark_lu               | 64.6 ms                                                                    | 63.1 ms: 1.02x faster                                                      |
| sqlglot_parse            | 913 us                                                                     | 892 us: 1.02x faster                                                       |
| pickle_pure_python       | 217 us                                                                     | 212 us: 1.02x faster                                                       |
| coverage                 | 49.4 ms                                                                    | 48.4 ms: 1.02x faster                                                      |
| deepcopy                 | 192 us                                                                     | 189 us: 1.02x faster                                                       |
| mako                     | 7.17 ms                                                                    | 7.04 ms: 1.02x faster                                                      |
| deepcopy_reduce          | 1.95 us                                                                    | 1.92 us: 1.02x faster                                                      |
| sqlglot_normalize        | 195 ms                                                                     | 192 ms: 1.01x faster                                                       |
| json_loads               | 14.4 us                                                                    | 14.2 us: 1.01x faster                                                      |
| xml_etree_process        | 41.9 ms                                                                    | 41.3 ms: 1.01x faster                                                      |
| nbody                    | 89.2 ms                                                                    | 88.1 ms: 1.01x faster                                                      |
| sympy_sum                | 91.1 ms                                                                    | 90.0 ms: 1.01x faster                                                      |
| django_template          | 25.0 ms                                                                    | 24.7 ms: 1.01x faster                                                      |
| sqlglot_transpile        | 1.14 ms                                                                    | 1.12 ms: 1.01x faster                                                      |
| scimark_fft              | 214 ms                                                                     | 211 ms: 1.01x faster                                                       |
| deltablue                | 2.30 ms                                                                    | 2.28 ms: 1.01x faster                                                      |
| xml_etree_parse          | 94.4 ms                                                                    | 93.5 ms: 1.01x faster                                                      |
| 2to3                     | 230 ms                                                                     | 228 ms: 1.01x faster                                                       |
| richards                 | 32.6 ms                                                                    | 32.3 ms: 1.01x faster                                                      |
| pyflate                  | 329 ms                                                                     | 326 ms: 1.01x faster                                                       |
| sympy_str                | 178 ms                                                                     | 177 ms: 1.01x faster                                                       |
| tornado_http             | 93.8 ms                                                                    | 93.2 ms: 1.01x faster                                                      |
| thrift                   | 522 us                                                                     | 519 us: 1.01x faster                                                       |
| comprehensions           | 12.2 us                                                                    | 12.1 us: 1.00x faster                                                      |
| telco                    | 5.14 ms                                                                    | 5.16 ms: 1.00x slower                                                      |
| regex_compile            | 91.2 ms                                                                    | 91.6 ms: 1.00x slower                                                      |
| crypto_pyaes             | 49.6 ms                                                                    | 49.8 ms: 1.01x slower                                                      |
| logging_simple           | 6.34 us                                                                    | 6.37 us: 1.01x slower                                                      |
| meteor_contest           | 78.3 ms                                                                    | 78.8 ms: 1.01x slower                                                      |
| hexiom                   | 4.53 ms                                                                    | 4.56 ms: 1.01x slower                                                      |
| mdp                      | 1.50 sec                                                                   | 1.51 sec: 1.01x slower                                                     |
| go                       | 87.6 ms                                                                    | 88.6 ms: 1.01x slower                                                      |
| coroutines               | 14.3 ms                                                                    | 14.5 ms: 1.01x slower                                                      |
| xml_etree_iterparse      | 65.8 ms                                                                    | 66.6 ms: 1.01x slower                                                      |
| fannkuch                 | 303 ms                                                                     | 307 ms: 1.01x slower                                                       |
| bench_mp_pool            | 69.2 ms                                                                    | 70.3 ms: 1.02x slower                                                      |
| typing_runtime_protocols | 110 us                                                                     | 114 us: 1.03x slower                                                       |
| json                     | 3.02 ms                                                                    | 3.14 ms: 1.04x slower                                                      |
| genshi_text              | 16.9 ms                                                                    | 17.7 ms: 1.05x slower                                                      |
| spectral_norm            | 69.9 ms                                                                    | 73.9 ms: 1.06x slower                                                      |
| Geometric mean           | (ref)                                                                      | 1.01x faster                                                               |

Benchmark hidden because not significant (34): pycparser, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed_tg, float, gc_traversal, richards_super, docutils, json_dumps, pylint, pprint_pformat, unpickle_pure_python, logging_silent, async_generators, chaos, async_tree_cpu_io_mixed, generators, python_startup, async_tree_memoization_tg, pprint_safe_repr, async_tree_none, python_startup_no_site, pidigits, logging_format, pathlib, html5lib, create_gc_cycles, async_tree_memoization, sympy_integrate, async_tree_none_tg, raytrace, bench_thread_pool, genshi_xml, asyncio_tcp_ssl

# HPT report

- Reliability score: 99.13% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown