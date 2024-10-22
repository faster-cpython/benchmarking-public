# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.00x slower
- HPT reliability: 98.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.66 sec                                                              | 2.67 sec: 1.00x slower                                                |
| html5lib       | 63.1 ms                                                               | 61.8 ms: 1.02x faster                                                 |
| tornado_http   | 90.1 ms                                                               | 90.8 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_generators | 437 ms                                                                | 431 ms: 1.01x faster                                                  |
| coroutines       | 23.1 ms                                                               | 23.0 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl  | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                                |
| async_tree_io    | 930 ms                                                                | 928 ms: 1.00x faster                                                  |
| asyncio_tcp      | 478 ms                                                                | 482 ms: 1.01x slower                                                  |
| Geometric mean   | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 77.5 ms                                                               | 77.8 ms: 1.00x slower                                                 |
| nbody          | 84.1 ms                                                               | 85.8 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.81 ms                                                               | 3.76 ms: 1.01x faster                                                 |
| regex_compile  | 128 ms                                                                | 130 ms: 1.02x slower                                                  |
| regex_dna      | 220 ms                                                                | 225 ms: 1.02x slower                                                  |
| regex_v8       | 26.2 ms                                                               | 26.8 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.09 sec                                                              | 2.05 sec: 1.02x faster                                                |
| xml_etree_generate   | 84.6 ms                                                               | 84.9 ms: 1.00x slower                                                 |
| pickle_pure_python   | 301 us                                                                | 302 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 104 ms                                                                | 105 ms: 1.01x slower                                                  |
| unpickle_pure_python | 213 us                                                                | 216 us: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (4): xml_etree_parse, json_dumps, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| python_startup_no_site | 7.11 ms                                                               | 7.05 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.3 ms                                                               | 11.2 ms: 1.01x faster                                                 |
| django_template | 33.7 ms                                                               | 33.5 ms: 1.00x faster                                                 |
| genshi_xml      | 49.5 ms                                                               | 51.5 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| html5lib                 | 63.1 ms                                                               | 61.8 ms: 1.02x faster                                                 |
| tomli_loads              | 2.09 sec                                                              | 2.05 sec: 1.02x faster                                                |
| async_generators         | 437 ms                                                                | 431 ms: 1.01x faster                                                  |
| telco                    | 8.42 ms                                                               | 8.31 ms: 1.01x faster                                                 |
| nqueens                  | 81.3 ms                                                               | 80.4 ms: 1.01x faster                                                 |
| regex_effbot             | 3.81 ms                                                               | 3.76 ms: 1.01x faster                                                 |
| python_startup           | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                 |
| spectral_norm            | 114 ms                                                                | 113 ms: 1.01x faster                                                  |
| python_startup_no_site   | 7.11 ms                                                               | 7.05 ms: 1.01x faster                                                 |
| json                     | 5.32 ms                                                               | 5.27 ms: 1.01x faster                                                 |
| sqlglot_parse            | 1.30 ms                                                               | 1.29 ms: 1.01x faster                                                 |
| mako                     | 11.3 ms                                                               | 11.2 ms: 1.01x faster                                                 |
| meteor_contest           | 107 ms                                                                | 106 ms: 1.01x faster                                                  |
| coroutines               | 23.1 ms                                                               | 23.0 ms: 1.01x faster                                                 |
| create_gc_cycles         | 1.74 ms                                                               | 1.74 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                                |
| django_template          | 33.7 ms                                                               | 33.5 ms: 1.00x faster                                                 |
| comprehensions           | 16.6 us                                                               | 16.5 us: 1.00x faster                                                 |
| sqlglot_optimize         | 53.6 ms                                                               | 53.4 ms: 1.00x faster                                                 |
| async_tree_io            | 930 ms                                                                | 928 ms: 1.00x faster                                                  |
| fannkuch                 | 406 ms                                                                | 407 ms: 1.00x slower                                                  |
| xml_etree_generate       | 84.6 ms                                                               | 84.9 ms: 1.00x slower                                                 |
| float                    | 77.5 ms                                                               | 77.8 ms: 1.00x slower                                                 |
| docutils                 | 2.66 sec                                                              | 2.67 sec: 1.00x slower                                                |
| generators               | 27.7 ms                                                               | 27.8 ms: 1.00x slower                                                 |
| chaos                    | 58.4 ms                                                               | 58.7 ms: 1.01x slower                                                 |
| deepcopy_memo            | 29.7 us                                                               | 29.8 us: 1.01x slower                                                 |
| pickle_pure_python       | 301 us                                                                | 302 us: 1.01x slower                                                  |
| scimark_sor              | 125 ms                                                                | 126 ms: 1.01x slower                                                  |
| asyncio_tcp              | 478 ms                                                                | 482 ms: 1.01x slower                                                  |
| tornado_http             | 90.1 ms                                                               | 90.8 ms: 1.01x slower                                                 |
| pyflate                  | 474 ms                                                                | 478 ms: 1.01x slower                                                  |
| bench_thread_pool        | 780 us                                                                | 787 us: 1.01x slower                                                  |
| sympy_expand             | 455 ms                                                                | 459 ms: 1.01x slower                                                  |
| sympy_str                | 267 ms                                                                | 270 ms: 1.01x slower                                                  |
| thrift                   | 771 us                                                                | 778 us: 1.01x slower                                                  |
| pprint_pformat           | 1.45 sec                                                              | 1.47 sec: 1.01x slower                                                |
| xml_etree_iterparse      | 104 ms                                                                | 105 ms: 1.01x slower                                                  |
| deepcopy_reduce          | 2.72 us                                                               | 2.75 us: 1.01x slower                                                 |
| deepcopy                 | 261 us                                                                | 264 us: 1.01x slower                                                  |
| go                       | 118 ms                                                                | 119 ms: 1.01x slower                                                  |
| scimark_lu               | 113 ms                                                                | 114 ms: 1.01x slower                                                  |
| sympy_sum                | 147 ms                                                                | 149 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult  | 4.71 ms                                                               | 4.77 ms: 1.01x slower                                                 |
| logging_format           | 6.08 us                                                               | 6.17 us: 1.01x slower                                                 |
| pprint_safe_repr         | 704 ms                                                                | 714 ms: 1.01x slower                                                  |
| unpickle_pure_python     | 213 us                                                                | 216 us: 1.01x slower                                                  |
| gc_traversal             | 3.72 ms                                                               | 3.78 ms: 1.02x slower                                                 |
| regex_compile            | 128 ms                                                                | 130 ms: 1.02x slower                                                  |
| nbody                    | 84.1 ms                                                               | 85.8 ms: 1.02x slower                                                 |
| mdp                      | 2.52 sec                                                              | 2.57 sec: 1.02x slower                                                |
| regex_dna                | 220 ms                                                                | 225 ms: 1.02x slower                                                  |
| raytrace                 | 259 ms                                                                | 264 ms: 1.02x slower                                                  |
| regex_v8                 | 26.2 ms                                                               | 26.8 ms: 1.02x slower                                                 |
| scimark_monte_carlo      | 66.5 ms                                                               | 68.2 ms: 1.03x slower                                                 |
| scimark_fft              | 353 ms                                                                | 363 ms: 1.03x slower                                                  |
| genshi_xml               | 49.5 ms                                                               | 51.5 ms: 1.04x slower                                                 |
| logging_silent           | 97.9 ns                                                               | 102 ns: 1.05x slower                                                  |
| typing_runtime_protocols | 158 us                                                                | 165 us: 1.05x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (30): async_tree_memoization, xml_etree_parse, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_none, coverage, crypto_pyaes, richards, sqlglot_normalize, deltablue, hexiom, sqlglot_transpile, 2to3, json_dumps, pidigits, richards_super, json_loads, bench_mp_pool, sympy_integrate, xml_etree_process, pylint, bpe_tokeniser, asyncio_websockets, pycparser, genshi_text, logging_simple, async_tree_cpu_io_mixed_tg, pathlib, async_tree_cpu_io_mixed

# HPT report

- Reliability score: 98.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x