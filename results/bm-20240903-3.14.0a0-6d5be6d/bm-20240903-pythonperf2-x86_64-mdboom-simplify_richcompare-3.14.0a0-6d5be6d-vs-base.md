# Results vs. base

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.00x slower
- HPT reliability: 58.71%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                      | 283 ms: 1.00x slower                                                        |
| html5lib       | 71.1 ms                                                                     | 70.2 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines       | 22.3 ms                                                                     | 21.6 ms: 1.03x faster                                                       |
| async_generators | 364 ms                                                                      | 360 ms: 1.01x faster                                                        |
| asyncio_tcp      | 367 ms                                                                      | 370 ms: 1.01x slower                                                        |
| async_tree_io    | 800 ms                                                                      | 818 ms: 1.02x slower                                                        |
| Geometric mean   | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.9 ms                                                                     | 80.0 ms: 1.01x slower                                                       |
| nbody          | 86.8 ms                                                                     | 91.4 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 240 ms                                                                      | 232 ms: 1.03x faster                                                        |
| regex_effbot   | 3.58 ms                                                                     | 3.48 ms: 1.03x faster                                                       |
| regex_v8       | 26.1 ms                                                                     | 27.0 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 11.0 ms                                                                     | 10.8 ms: 1.02x faster                                                       |
| xml_etree_generate   | 85.7 ms                                                                     | 86.3 ms: 1.01x slower                                                       |
| xml_etree_parse      | 144 ms                                                                      | 145 ms: 1.01x slower                                                        |
| tomli_loads          | 2.54 sec                                                                    | 2.57 sec: 1.01x slower                                                      |
| xml_etree_iterparse  | 102 ms                                                                      | 103 ms: 1.01x slower                                                        |
| unpickle_pure_python | 214 us                                                                      | 217 us: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (3): xml_etree_process, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 40.0 ms                                                                     | 39.7 ms: 1.01x faster                                                       |
| genshi_text     | 25.1 ms                                                                     | 25.9 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                | bm-20240829-pythonperf2-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|--------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 4.34 ms                                                                     | 4.16 ms: 1.04x faster                                                       |
| raytrace                 | 280 ms                                                                      | 268 ms: 1.04x faster                                                        |
| thrift                   | 886 us                                                                      | 856 us: 1.04x faster                                                        |
| regex_dna                | 240 ms                                                                      | 232 ms: 1.03x faster                                                        |
| deepcopy_memo            | 30.5 us                                                                     | 29.5 us: 1.03x faster                                                       |
| coroutines               | 22.3 ms                                                                     | 21.6 ms: 1.03x faster                                                       |
| regex_effbot             | 3.58 ms                                                                     | 3.48 ms: 1.03x faster                                                       |
| coverage                 | 85.0 ms                                                                     | 82.6 ms: 1.03x faster                                                       |
| telco                    | 8.41 ms                                                                     | 8.21 ms: 1.02x faster                                                       |
| pathlib                  | 15.9 ms                                                                     | 15.6 ms: 1.02x faster                                                       |
| json_dumps               | 11.0 ms                                                                     | 10.8 ms: 1.02x faster                                                       |
| logging_simple           | 6.38 us                                                                     | 6.26 us: 1.02x faster                                                       |
| scimark_monte_carlo      | 66.0 ms                                                                     | 64.8 ms: 1.02x faster                                                       |
| nqueens                  | 89.3 ms                                                                     | 87.8 ms: 1.02x faster                                                       |
| logging_silent           | 99.1 ns                                                                     | 97.4 ns: 1.02x faster                                                       |
| scimark_fft              | 305 ms                                                                      | 300 ms: 1.02x faster                                                        |
| meteor_contest           | 127 ms                                                                      | 125 ms: 1.01x faster                                                        |
| deltablue                | 3.48 ms                                                                     | 3.43 ms: 1.01x faster                                                       |
| html5lib                 | 71.1 ms                                                                     | 70.2 ms: 1.01x faster                                                       |
| scimark_lu               | 96.0 ms                                                                     | 94.8 ms: 1.01x faster                                                       |
| comprehensions           | 17.6 us                                                                     | 17.4 us: 1.01x faster                                                       |
| crypto_pyaes             | 73.6 ms                                                                     | 72.8 ms: 1.01x faster                                                       |
| async_generators         | 364 ms                                                                      | 360 ms: 1.01x faster                                                        |
| richards_super           | 57.0 ms                                                                     | 56.4 ms: 1.01x faster                                                       |
| mdp                      | 2.50 sec                                                                    | 2.47 sec: 1.01x faster                                                      |
| django_template          | 40.0 ms                                                                     | 39.7 ms: 1.01x faster                                                       |
| json                     | 5.32 ms                                                                     | 5.28 ms: 1.01x faster                                                       |
| bpe_tokeniser            | 4.91 sec                                                                    | 4.88 sec: 1.01x faster                                                      |
| gc_traversal             | 4.46 ms                                                                     | 4.43 ms: 1.01x faster                                                       |
| logging_format           | 6.90 us                                                                     | 6.86 us: 1.01x faster                                                       |
| richards                 | 50.5 ms                                                                     | 50.2 ms: 1.01x faster                                                       |
| sqlglot_transpile        | 1.80 ms                                                                     | 1.81 ms: 1.00x slower                                                       |
| 2to3                     | 281 ms                                                                      | 283 ms: 1.00x slower                                                        |
| sqlglot_normalize        | 120 ms                                                                      | 120 ms: 1.01x slower                                                        |
| sympy_integrate          | 22.8 ms                                                                     | 23.0 ms: 1.01x slower                                                       |
| sqlglot_optimize         | 59.0 ms                                                                     | 59.3 ms: 1.01x slower                                                       |
| sympy_expand             | 493 ms                                                                      | 496 ms: 1.01x slower                                                        |
| asyncio_tcp              | 367 ms                                                                      | 370 ms: 1.01x slower                                                        |
| xml_etree_generate       | 85.7 ms                                                                     | 86.3 ms: 1.01x slower                                                       |
| xml_etree_parse          | 144 ms                                                                      | 145 ms: 1.01x slower                                                        |
| spectral_norm            | 96.6 ms                                                                     | 97.3 ms: 1.01x slower                                                       |
| deepcopy                 | 286 us                                                                      | 288 us: 1.01x slower                                                        |
| typing_runtime_protocols | 174 us                                                                      | 176 us: 1.01x slower                                                        |
| tomli_loads              | 2.54 sec                                                                    | 2.57 sec: 1.01x slower                                                      |
| xml_etree_iterparse      | 102 ms                                                                      | 103 ms: 1.01x slower                                                        |
| float                    | 78.9 ms                                                                     | 80.0 ms: 1.01x slower                                                       |
| unpickle_pure_python     | 214 us                                                                      | 217 us: 1.01x slower                                                        |
| chaos                    | 60.7 ms                                                                     | 61.8 ms: 1.02x slower                                                       |
| create_gc_cycles         | 1.97 ms                                                                     | 2.01 ms: 1.02x slower                                                       |
| async_tree_io            | 800 ms                                                                      | 818 ms: 1.02x slower                                                        |
| genshi_text              | 25.1 ms                                                                     | 25.9 ms: 1.03x slower                                                       |
| go                       | 132 ms                                                                      | 136 ms: 1.03x slower                                                        |
| regex_v8                 | 26.1 ms                                                                     | 27.0 ms: 1.03x slower                                                       |
| pyflate                  | 460 ms                                                                      | 476 ms: 1.03x slower                                                        |
| generators               | 28.4 ms                                                                     | 29.4 ms: 1.03x slower                                                       |
| fannkuch                 | 347 ms                                                                      | 362 ms: 1.04x slower                                                        |
| nbody                    | 86.8 ms                                                                     | 91.4 ms: 1.05x slower                                                       |
| bench_mp_pool            | 4.42 ms                                                                     | 4.68 ms: 1.06x slower                                                       |
| scimark_sor              | 110 ms                                                                      | 118 ms: 1.07x slower                                                        |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (30): pycparser, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, docutils, pprint_safe_repr, xml_etree_process, pprint_pformat, pickle_pure_python, python_startup, sympy_str, regex_compile, python_startup_no_site, asyncio_tcp_ssl, async_tree_memoization_tg, hexiom, sqlglot_parse, pidigits, sympy_sum, pylint, genshi_xml, async_tree_memoization, mako, async_tree_none_tg, tornado_http, deepcopy_reduce, asyncio_websockets, async_tree_io_tg, bench_thread_pool, json_loads

# HPT report

- Reliability score: 58.71% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x