# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                | 253 ms: 1.01x faster                                                  |
| docutils       | 2.66 sec                                                              | 2.64 sec: 1.01x faster                                                |
| tornado_http   | 90.4 ms                                                               | 89.5 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io    | 931 ms                                                                | 926 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl  | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                                |
| coroutines       | 22.8 ms                                                               | 23.2 ms: 1.02x slower                                                 |
| async_generators | 431 ms                                                                | 439 ms: 1.02x slower                                                  |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (9): async_tree_memoization, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed_tg, asyncio_tcp, asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 79.2 ms                                                               | 76.5 ms: 1.04x faster                                                 |
| nbody          | 87.8 ms                                                               | 85.3 ms: 1.03x faster                                                 |
| pidigits       | 186 ms                                                                | 186 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                                | 218 ms: 1.01x faster                                                  |
| regex_effbot   | 3.58 ms                                                               | 3.54 ms: 1.01x faster                                                 |
| regex_compile  | 129 ms                                                                | 129 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                                              | 2.05 sec: 1.03x faster                                                |
| xml_etree_parse      | 159 ms                                                                | 156 ms: 1.02x faster                                                  |
| json_dumps           | 10.6 ms                                                               | 10.4 ms: 1.02x faster                                                 |
| unpickle_pure_python | 215 us                                                                | 212 us: 1.01x faster                                                  |
| pickle_pure_python   | 304 us                                                                | 301 us: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (4): xml_etree_iterparse, xml_etree_process, json_loads, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 7.13 ms                                                               | 7.04 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.5 ms                                                               | 21.5 ms: 1.05x faster                                                 |
| genshi_xml      | 49.4 ms                                                               | 48.2 ms: 1.03x faster                                                 |
| django_template | 33.9 ms                                                               | 33.7 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal             | 3.72 ms                                                               | 3.54 ms: 1.05x faster                                                 |
| genshi_text              | 22.5 ms                                                               | 21.5 ms: 1.05x faster                                                 |
| generators               | 28.7 ms                                                               | 27.7 ms: 1.04x faster                                                 |
| deepcopy_reduce          | 2.75 us                                                               | 2.66 us: 1.04x faster                                                 |
| float                    | 79.2 ms                                                               | 76.5 ms: 1.04x faster                                                 |
| pprint_safe_repr         | 726 ms                                                                | 702 ms: 1.03x faster                                                  |
| scimark_sparse_mat_mult  | 4.92 ms                                                               | 4.77 ms: 1.03x faster                                                 |
| tomli_loads              | 2.11 sec                                                              | 2.05 sec: 1.03x faster                                                |
| nbody                    | 87.8 ms                                                               | 85.3 ms: 1.03x faster                                                 |
| genshi_xml               | 49.4 ms                                                               | 48.2 ms: 1.03x faster                                                 |
| scimark_sor              | 126 ms                                                                | 124 ms: 1.02x faster                                                  |
| xml_etree_parse          | 159 ms                                                                | 156 ms: 1.02x faster                                                  |
| pprint_pformat           | 1.47 sec                                                              | 1.44 sec: 1.02x faster                                                |
| pyflate                  | 470 ms                                                                | 461 ms: 1.02x faster                                                  |
| thrift                   | 775 us                                                                | 762 us: 1.02x faster                                                  |
| json_dumps               | 10.6 ms                                                               | 10.4 ms: 1.02x faster                                                 |
| scimark_lu               | 114 ms                                                                | 113 ms: 1.01x faster                                                  |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| pycparser                | 1.14 sec                                                              | 1.13 sec: 1.01x faster                                                |
| 2to3                     | 256 ms                                                                | 253 ms: 1.01x faster                                                  |
| regex_dna                | 221 ms                                                                | 218 ms: 1.01x faster                                                  |
| meteor_contest           | 107 ms                                                                | 106 ms: 1.01x faster                                                  |
| create_gc_cycles         | 1.76 ms                                                               | 1.73 ms: 1.01x faster                                                 |
| regex_effbot             | 3.58 ms                                                               | 3.54 ms: 1.01x faster                                                 |
| python_startup_no_site   | 7.13 ms                                                               | 7.04 ms: 1.01x faster                                                 |
| chaos                    | 58.9 ms                                                               | 58.2 ms: 1.01x faster                                                 |
| sqlglot_parse            | 1.29 ms                                                               | 1.28 ms: 1.01x faster                                                 |
| go                       | 119 ms                                                                | 117 ms: 1.01x faster                                                  |
| unpickle_pure_python     | 215 us                                                                | 212 us: 1.01x faster                                                  |
| deepcopy_memo            | 29.9 us                                                               | 29.6 us: 1.01x faster                                                 |
| deepcopy                 | 263 us                                                                | 260 us: 1.01x faster                                                  |
| sympy_sum                | 148 ms                                                                | 147 ms: 1.01x faster                                                  |
| pickle_pure_python       | 304 us                                                                | 301 us: 1.01x faster                                                  |
| sympy_integrate          | 19.7 ms                                                               | 19.5 ms: 1.01x faster                                                 |
| tornado_http             | 90.4 ms                                                               | 89.5 ms: 1.01x faster                                                 |
| scimark_fft              | 366 ms                                                                | 363 ms: 1.01x faster                                                  |
| richards_super           | 52.1 ms                                                               | 51.6 ms: 1.01x faster                                                 |
| scimark_monte_carlo      | 66.9 ms                                                               | 66.4 ms: 1.01x faster                                                 |
| sympy_expand             | 456 ms                                                                | 452 ms: 1.01x faster                                                  |
| sympy_str                | 269 ms                                                                | 267 ms: 1.01x faster                                                  |
| mdp                      | 2.52 sec                                                              | 2.50 sec: 1.01x faster                                                |
| async_tree_io            | 931 ms                                                                | 926 ms: 1.01x faster                                                  |
| sqlglot_transpile        | 1.58 ms                                                               | 1.57 ms: 1.01x faster                                                 |
| django_template          | 33.9 ms                                                               | 33.7 ms: 1.01x faster                                                 |
| raytrace                 | 262 ms                                                                | 261 ms: 1.01x faster                                                  |
| docutils                 | 2.66 sec                                                              | 2.64 sec: 1.01x faster                                                |
| regex_compile            | 129 ms                                                                | 129 ms: 1.00x faster                                                  |
| sqlglot_optimize         | 53.6 ms                                                               | 53.5 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                                |
| pidigits                 | 186 ms                                                                | 186 ms: 1.00x slower                                                  |
| comprehensions           | 16.5 us                                                               | 16.5 us: 1.00x slower                                                 |
| logging_format           | 6.06 us                                                               | 6.10 us: 1.01x slower                                                 |
| hexiom                   | 6.15 ms                                                               | 6.19 ms: 1.01x slower                                                 |
| sqlglot_normalize        | 107 ms                                                                | 108 ms: 1.01x slower                                                  |
| typing_runtime_protocols | 159 us                                                                | 161 us: 1.01x slower                                                  |
| coverage                 | 84.4 ms                                                               | 85.7 ms: 1.02x slower                                                 |
| logging_simple           | 5.49 us                                                               | 5.58 us: 1.02x slower                                                 |
| coroutines               | 22.8 ms                                                               | 23.2 ms: 1.02x slower                                                 |
| async_generators         | 431 ms                                                                | 439 ms: 1.02x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (30): async_tree_memoization, async_tree_io_tg, async_tree_none_tg, xml_etree_iterparse, telco, async_tree_memoization_tg, json, nqueens, async_tree_none, pathlib, pylint, spectral_norm, mako, bpe_tokeniser, xml_etree_process, async_tree_cpu_io_mixed_tg, regex_v8, crypto_pyaes, bench_thread_pool, asyncio_tcp, bench_mp_pool, json_loads, richards, asyncio_websockets, deltablue, fannkuch, xml_etree_generate, logging_silent, html5lib, async_tree_cpu_io_mixed

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x