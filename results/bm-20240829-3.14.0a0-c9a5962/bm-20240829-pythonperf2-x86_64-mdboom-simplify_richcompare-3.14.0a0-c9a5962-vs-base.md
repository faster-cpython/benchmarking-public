# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.01x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 2.92 sec                                                                    | 2.91 sec: 1.01x faster                                                      |
| html5lib       | 71.1 ms                                                                     | 69.2 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines             | 22.3 ms                                                                     | 21.6 ms: 1.04x faster                                                       |
| async_generators       | 364 ms                                                                      | 361 ms: 1.01x faster                                                        |
| async_tree_memoization | 398 ms                                                                      | 395 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl        | 1.58 sec                                                                    | 1.57 sec: 1.00x faster                                                      |
| async_tree_io          | 800 ms                                                                      | 817 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, asyncio_tcp, async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 86.8 ms                                                                     | 84.1 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.58 ms                                                                     | 3.42 ms: 1.05x faster                                                       |
| regex_compile  | 141 ms                                                                      | 139 ms: 1.01x faster                                                        |
| regex_v8       | 26.1 ms                                                                     | 27.3 ms: 1.05x slower                                                       |
| regex_dna      | 240 ms                                                                      | 254 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 60.1 ms                                                                     | 58.8 ms: 1.02x faster                                                       |
| json_dumps           | 11.0 ms                                                                     | 10.8 ms: 1.02x faster                                                       |
| xml_etree_generate   | 85.7 ms                                                                     | 84.1 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 102 ms                                                                      | 100 ms: 1.01x faster                                                        |
| unpickle_pure_python | 214 us                                                                      | 212 us: 1.01x faster                                                        |
| xml_etree_parse      | 144 ms                                                                      | 143 ms: 1.01x faster                                                        |
| json_loads           | 24.9 us                                                                     | 25.1 us: 1.01x slower                                                       |
| tomli_loads          | 2.54 sec                                                                    | 2.60 sec: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| python_startup_no_site | 9.05 ms                                                                     | 9.08 ms: 1.00x slower                                                       |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 25.1 ms                                                                     | 24.6 ms: 1.02x faster                                                       |
| genshi_xml      | 55.0 ms                                                                     | 54.5 ms: 1.01x faster                                                       |
| django_template | 40.0 ms                                                                     | 40.2 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|--------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                   | 886 us                                                                      | 841 us: 1.05x faster                                                        |
| deepcopy_memo            | 30.5 us                                                                     | 28.9 us: 1.05x faster                                                       |
| regex_effbot             | 3.58 ms                                                                     | 3.42 ms: 1.05x faster                                                       |
| raytrace                 | 280 ms                                                                      | 268 ms: 1.04x faster                                                        |
| coroutines               | 22.3 ms                                                                     | 21.6 ms: 1.04x faster                                                       |
| coverage                 | 85.0 ms                                                                     | 82.1 ms: 1.04x faster                                                       |
| deltablue                | 3.48 ms                                                                     | 3.37 ms: 1.03x faster                                                       |
| nbody                    | 86.8 ms                                                                     | 84.1 ms: 1.03x faster                                                       |
| html5lib                 | 71.1 ms                                                                     | 69.2 ms: 1.03x faster                                                       |
| logging_simple           | 6.38 us                                                                     | 6.22 us: 1.03x faster                                                       |
| pycparser                | 1.25 sec                                                                    | 1.22 sec: 1.03x faster                                                      |
| richards_super           | 57.0 ms                                                                     | 55.7 ms: 1.02x faster                                                       |
| xml_etree_process        | 60.1 ms                                                                     | 58.8 ms: 1.02x faster                                                       |
| genshi_text              | 25.1 ms                                                                     | 24.6 ms: 1.02x faster                                                       |
| telco                    | 8.41 ms                                                                     | 8.24 ms: 1.02x faster                                                       |
| json_dumps               | 11.0 ms                                                                     | 10.8 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult  | 4.34 ms                                                                     | 4.26 ms: 1.02x faster                                                       |
| scimark_monte_carlo      | 66.0 ms                                                                     | 64.7 ms: 1.02x faster                                                       |
| scimark_fft              | 305 ms                                                                      | 299 ms: 1.02x faster                                                        |
| xml_etree_generate       | 85.7 ms                                                                     | 84.1 ms: 1.02x faster                                                       |
| richards                 | 50.5 ms                                                                     | 49.6 ms: 1.02x faster                                                       |
| json                     | 5.32 ms                                                                     | 5.23 ms: 1.02x faster                                                       |
| typing_runtime_protocols | 174 us                                                                      | 172 us: 1.02x faster                                                        |
| logging_silent           | 99.1 ns                                                                     | 97.5 ns: 1.02x faster                                                       |
| xml_etree_iterparse      | 102 ms                                                                      | 100 ms: 1.01x faster                                                        |
| logging_format           | 6.90 us                                                                     | 6.81 us: 1.01x faster                                                       |
| scimark_sor              | 110 ms                                                                      | 109 ms: 1.01x faster                                                        |
| genshi_xml               | 55.0 ms                                                                     | 54.5 ms: 1.01x faster                                                       |
| sqlglot_transpile        | 1.80 ms                                                                     | 1.78 ms: 1.01x faster                                                       |
| sqlglot_parse            | 1.42 ms                                                                     | 1.41 ms: 1.01x faster                                                       |
| unpickle_pure_python     | 214 us                                                                      | 212 us: 1.01x faster                                                        |
| pprint_pformat           | 1.65 sec                                                                    | 1.64 sec: 1.01x faster                                                      |
| regex_compile            | 141 ms                                                                      | 139 ms: 1.01x faster                                                        |
| async_generators         | 364 ms                                                                      | 361 ms: 1.01x faster                                                        |
| comprehensions           | 17.6 us                                                                     | 17.4 us: 1.01x faster                                                       |
| pprint_safe_repr         | 802 ms                                                                      | 796 ms: 1.01x faster                                                        |
| async_tree_memoization   | 398 ms                                                                      | 395 ms: 1.01x faster                                                        |
| pathlib                  | 15.9 ms                                                                     | 15.8 ms: 1.01x faster                                                       |
| xml_etree_parse          | 144 ms                                                                      | 143 ms: 1.01x faster                                                        |
| spectral_norm            | 96.6 ms                                                                     | 96.0 ms: 1.01x faster                                                       |
| docutils                 | 2.92 sec                                                                    | 2.91 sec: 1.01x faster                                                      |
| meteor_contest           | 127 ms                                                                      | 126 ms: 1.00x faster                                                        |
| chaos                    | 60.7 ms                                                                     | 60.5 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl          | 1.58 sec                                                                    | 1.57 sec: 1.00x faster                                                      |
| python_startup           | 13.4 ms                                                                     | 13.4 ms: 1.00x slower                                                       |
| sympy_integrate          | 22.8 ms                                                                     | 22.9 ms: 1.00x slower                                                       |
| sqlglot_optimize         | 59.0 ms                                                                     | 59.2 ms: 1.00x slower                                                       |
| sympy_sum                | 151 ms                                                                      | 151 ms: 1.00x slower                                                        |
| python_startup_no_site   | 9.05 ms                                                                     | 9.08 ms: 1.00x slower                                                       |
| sqlglot_normalize        | 120 ms                                                                      | 120 ms: 1.00x slower                                                        |
| sympy_str                | 289 ms                                                                      | 290 ms: 1.00x slower                                                        |
| json_loads               | 24.9 us                                                                     | 25.1 us: 1.01x slower                                                       |
| django_template          | 40.0 ms                                                                     | 40.2 ms: 1.01x slower                                                       |
| sympy_expand             | 493 ms                                                                      | 496 ms: 1.01x slower                                                        |
| mdp                      | 2.50 sec                                                                    | 2.52 sec: 1.01x slower                                                      |
| go                       | 132 ms                                                                      | 135 ms: 1.02x slower                                                        |
| create_gc_cycles         | 1.97 ms                                                                     | 2.00 ms: 1.02x slower                                                       |
| hexiom                   | 6.21 ms                                                                     | 6.31 ms: 1.02x slower                                                       |
| fannkuch                 | 347 ms                                                                      | 354 ms: 1.02x slower                                                        |
| async_tree_io            | 800 ms                                                                      | 817 ms: 1.02x slower                                                        |
| tomli_loads              | 2.54 sec                                                                    | 2.60 sec: 1.02x slower                                                      |
| regex_v8                 | 26.1 ms                                                                     | 27.3 ms: 1.05x slower                                                       |
| pyflate                  | 460 ms                                                                      | 484 ms: 1.05x slower                                                        |
| bench_mp_pool            | 4.42 ms                                                                     | 4.65 ms: 1.05x slower                                                       |
| regex_dna                | 240 ms                                                                      | 254 ms: 1.06x slower                                                        |
| Geometric mean           | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (24): async_tree_io_tg, bench_thread_pool, async_tree_none, mako, deepcopy_reduce, tornado_http, pickle_pure_python, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, deepcopy, crypto_pyaes, pylint, 2to3, pidigits, float, bpe_tokeniser, scimark_lu, asyncio_tcp, async_tree_cpu_io_mixed_tg, nqueens, asyncio_websockets, generators, gc_traversal

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x