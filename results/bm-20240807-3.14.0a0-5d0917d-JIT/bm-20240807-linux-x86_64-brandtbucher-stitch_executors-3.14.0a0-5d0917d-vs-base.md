# Results vs. base

- fork: brandtbucher
- ref: stitch_executors
- machine: linux-x86_64
- commit hash: 5d0917d
- commit date: 2024-08-07
- overall geometric mean: 1.00x slower
- HPT reliability: 60.56%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 275 ms                                                                | 273 ms: 1.01x faster                                                    |
| docutils       | 2.92 sec                                                              | 2.96 sec: 1.01x slower                                                  |
| html5lib       | 63.8 ms                                                               | 65.8 ms: 1.03x slower                                                   |
| tornado_http   | 92.6 ms                                                               | 95.6 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|--------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| coroutines         | 22.9 ms                                                               | 22.6 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl    | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                  |
| asyncio_websockets | 554 ms                                                                | 557 ms: 1.00x slower                                                    |
| asyncio_tcp        | 498 ms                                                                | 502 ms: 1.01x slower                                                    |
| async_generators   | 453 ms                                                                | 458 ms: 1.01x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization, async_tree_io, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 79.1 ms                                                               | 79.7 ms: 1.01x slower                                                   |
| float          | 70.5 ms                                                               | 71.8 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.83 ms                                                               | 3.87 ms: 1.01x slower                                                   |
| regex_dna      | 223 ms                                                                | 232 ms: 1.04x slower                                                    |
| regex_v8       | 24.4 ms                                                               | 25.7 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 81.6 ms                                                               | 79.8 ms: 1.02x faster                                                   |
| xml_etree_process    | 57.2 ms                                                               | 56.6 ms: 1.01x faster                                                   |
| unpickle_pure_python | 215 us                                                                | 213 us: 1.01x faster                                                    |
| xml_etree_iterparse  | 99.2 ms                                                               | 99.7 ms: 1.01x slower                                                   |
| tomli_loads          | 1.91 sec                                                              | 1.95 sec: 1.02x slower                                                  |
| xml_etree_parse      | 146 ms                                                                | 148 ms: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (3): pickle_pure_python, json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.17 ms                                                               | 7.20 ms: 1.00x slower                                                   |
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 9.85 ms                                                               | 9.69 ms: 1.02x faster                                                   |
| genshi_text    | 24.5 ms                                                               | 25.0 ms: 1.02x slower                                                   |
| genshi_xml     | 53.4 ms                                                               | 56.1 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b | bm-20240807-linux-x86_64-brandtbucher-stitch_executors-3.14.0a0-5d0917d |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 4.55 ms                                                               | 4.14 ms: 1.10x faster                                                   |
| hexiom                   | 6.71 ms                                                               | 6.44 ms: 1.04x faster                                                   |
| scimark_lu               | 109 ms                                                                | 106 ms: 1.03x faster                                                    |
| pprint_pformat           | 1.49 sec                                                              | 1.45 sec: 1.03x faster                                                  |
| gc_traversal             | 3.85 ms                                                               | 3.75 ms: 1.03x faster                                                   |
| deepcopy_memo            | 29.1 us                                                               | 28.3 us: 1.03x faster                                                   |
| xml_etree_generate       | 81.6 ms                                                               | 79.8 ms: 1.02x faster                                                   |
| scimark_fft              | 307 ms                                                                | 300 ms: 1.02x faster                                                    |
| logging_format           | 6.17 us                                                               | 6.07 us: 1.02x faster                                                   |
| logging_silent           | 104 ns                                                                | 103 ns: 1.02x faster                                                    |
| mako                     | 9.85 ms                                                               | 9.69 ms: 1.02x faster                                                   |
| sqlglot_parse            | 1.29 ms                                                               | 1.27 ms: 1.02x faster                                                   |
| scimark_sor              | 117 ms                                                                | 115 ms: 1.02x faster                                                    |
| coroutines               | 22.9 ms                                                               | 22.6 ms: 1.01x faster                                                   |
| telco                    | 7.97 ms                                                               | 7.87 ms: 1.01x faster                                                   |
| go                       | 146 ms                                                                | 145 ms: 1.01x faster                                                    |
| coverage                 | 91.8 ms                                                               | 90.8 ms: 1.01x faster                                                   |
| deepcopy                 | 273 us                                                                | 270 us: 1.01x faster                                                    |
| crypto_pyaes             | 66.8 ms                                                               | 66.1 ms: 1.01x faster                                                   |
| sqlglot_transpile        | 1.62 ms                                                               | 1.60 ms: 1.01x faster                                                   |
| xml_etree_process        | 57.2 ms                                                               | 56.6 ms: 1.01x faster                                                   |
| unpickle_pure_python     | 215 us                                                                | 213 us: 1.01x faster                                                    |
| logging_simple           | 5.57 us                                                               | 5.53 us: 1.01x faster                                                   |
| pathlib                  | 16.1 ms                                                               | 16.0 ms: 1.01x faster                                                   |
| raytrace                 | 269 ms                                                                | 267 ms: 1.01x faster                                                    |
| 2to3                     | 275 ms                                                                | 273 ms: 1.01x faster                                                    |
| deltablue                | 3.58 ms                                                               | 3.56 ms: 1.01x faster                                                   |
| create_gc_cycles         | 1.78 ms                                                               | 1.77 ms: 1.01x faster                                                   |
| meteor_contest           | 105 ms                                                                | 105 ms: 1.00x faster                                                    |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                  |
| python_startup_no_site   | 7.17 ms                                                               | 7.20 ms: 1.00x slower                                                   |
| asyncio_websockets       | 554 ms                                                                | 557 ms: 1.00x slower                                                    |
| xml_etree_iterparse      | 99.2 ms                                                               | 99.7 ms: 1.01x slower                                                   |
| thrift                   | 797 us                                                                | 802 us: 1.01x slower                                                    |
| spectral_norm            | 100 ms                                                                | 101 ms: 1.01x slower                                                    |
| python_startup           | 10.6 ms                                                               | 10.6 ms: 1.01x slower                                                   |
| nbody                    | 79.1 ms                                                               | 79.7 ms: 1.01x slower                                                   |
| asyncio_tcp              | 498 ms                                                                | 502 ms: 1.01x slower                                                    |
| sympy_integrate          | 22.6 ms                                                               | 22.8 ms: 1.01x slower                                                   |
| bench_thread_pool        | 822 us                                                                | 829 us: 1.01x slower                                                    |
| richards                 | 41.2 ms                                                               | 41.5 ms: 1.01x slower                                                   |
| sqlglot_optimize         | 55.9 ms                                                               | 56.4 ms: 1.01x slower                                                   |
| regex_effbot             | 3.83 ms                                                               | 3.87 ms: 1.01x slower                                                   |
| async_generators         | 453 ms                                                                | 458 ms: 1.01x slower                                                    |
| docutils                 | 2.92 sec                                                              | 2.96 sec: 1.01x slower                                                  |
| typing_runtime_protocols | 171 us                                                                | 173 us: 1.02x slower                                                    |
| tomli_loads              | 1.91 sec                                                              | 1.95 sec: 1.02x slower                                                  |
| sympy_expand             | 508 ms                                                                | 517 ms: 1.02x slower                                                    |
| xml_etree_parse          | 146 ms                                                                | 148 ms: 1.02x slower                                                    |
| float                    | 70.5 ms                                                               | 71.8 ms: 1.02x slower                                                   |
| sympy_sum                | 170 ms                                                                | 174 ms: 1.02x slower                                                    |
| comprehensions           | 16.2 us                                                               | 16.6 us: 1.02x slower                                                   |
| genshi_text              | 24.5 ms                                                               | 25.0 ms: 1.02x slower                                                   |
| json                     | 5.09 ms                                                               | 5.20 ms: 1.02x slower                                                   |
| sympy_str                | 298 ms                                                                | 305 ms: 1.02x slower                                                    |
| html5lib                 | 63.8 ms                                                               | 65.8 ms: 1.03x slower                                                   |
| tornado_http             | 92.6 ms                                                               | 95.6 ms: 1.03x slower                                                   |
| pyflate                  | 432 ms                                                                | 448 ms: 1.04x slower                                                    |
| regex_dna                | 223 ms                                                                | 232 ms: 1.04x slower                                                    |
| genshi_xml               | 53.4 ms                                                               | 56.1 ms: 1.05x slower                                                   |
| regex_v8                 | 24.4 ms                                                               | 25.7 ms: 1.05x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (28): chaos, pprint_safe_repr, async_tree_cpu_io_mixed, sqlglot_normalize, deepcopy_reduce, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, pickle_pure_python, fannkuch, mdp, nqueens, richards_super, async_tree_none_tg, async_tree_memoization, bpe_tokeniser, regex_compile, bench_mp_pool, generators, pidigits, async_tree_io, json_loads, async_tree_none, pycparser, json_dumps, django_template, scimark_monte_carlo, async_tree_io_tg, pylint

# HPT report

- Reliability score: 60.56% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x