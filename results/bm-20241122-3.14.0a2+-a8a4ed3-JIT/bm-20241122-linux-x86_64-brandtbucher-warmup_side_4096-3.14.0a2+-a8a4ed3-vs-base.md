# Results vs. base

- fork: brandtbucher
- ref: warmup_side_4096
- machine: linux-x86_64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.003x faster
- HPT reliability: 97.27%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 261 ms                                                                 | 260 ms: 1.00x faster                                                     |
| docutils       | 2.83 sec                                                               | 2.77 sec: 1.02x faster                                                   |
| sphinx         | 1.11 sec                                                               | 1.09 sec: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| coroutines       | 23.1 ms                                                                | 22.7 ms: 1.02x faster                                                    |
| async_generators | 454 ms                                                                 | 461 ms: 1.02x slower                                                     |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (9): async_tree_none, async_tree_none_tg, async_tree_io, asyncio_websockets, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 188 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 132 ms                                                                 | 129 ms: 1.02x faster                                                     |
| regex_v8       | 25.5 ms                                                                | 25.9 ms: 1.02x slower                                                    |
| regex_dna      | 215 ms                                                                 | 219 ms: 1.02x slower                                                     |
| regex_effbot   | 3.30 ms                                                                | 3.36 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|--------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate | 82.2 ms                                                                | 78.5 ms: 1.05x faster                                                    |
| xml_etree_process  | 57.2 ms                                                                | 55.4 ms: 1.03x faster                                                    |
| json_loads         | 26.8 us                                                                | 26.2 us: 1.02x faster                                                    |
| json_dumps         | 11.1 ms                                                                | 11.2 ms: 1.01x slower                                                    |
| pickle_pure_python | 316 us                                                                 | 320 us: 1.01x slower                                                     |
| Geometric mean     | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (4): xml_etree_parse, unpickle_pure_python, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                    |
| python_startup_no_site | 7.06 ms                                                                | 7.09 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 10.1 ms                                                                | 9.96 ms: 1.02x faster                                                    |
| genshi_text    | 24.9 ms                                                                | 25.4 ms: 1.02x slower                                                    |
| genshi_xml     | 57.4 ms                                                                | 59.6 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20241122-linux-x86_64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                     | 2.78 sec                                                               | 2.59 sec: 1.07x faster                                                   |
| scimark_sparse_mat_mult | 4.81 ms                                                                | 4.57 ms: 1.05x faster                                                    |
| xml_etree_generate      | 82.2 ms                                                                | 78.5 ms: 1.05x faster                                                    |
| pylint                  | 283 ms                                                                 | 272 ms: 1.04x faster                                                     |
| scimark_lu              | 116 ms                                                                 | 112 ms: 1.04x faster                                                     |
| pycparser               | 1.18 sec                                                               | 1.14 sec: 1.03x faster                                                   |
| xml_etree_process       | 57.2 ms                                                                | 55.4 ms: 1.03x faster                                                    |
| comprehensions          | 17.7 us                                                                | 17.2 us: 1.03x faster                                                    |
| sympy_sum               | 160 ms                                                                 | 156 ms: 1.03x faster                                                     |
| json_loads              | 26.8 us                                                                | 26.2 us: 1.02x faster                                                    |
| docutils                | 2.83 sec                                                               | 2.77 sec: 1.02x faster                                                   |
| sympy_str               | 287 ms                                                                 | 281 ms: 1.02x faster                                                     |
| regex_compile           | 132 ms                                                                 | 129 ms: 1.02x faster                                                     |
| many_optionals          | 988 us                                                                 | 968 us: 1.02x faster                                                     |
| scimark_monte_carlo     | 66.0 ms                                                                | 64.6 ms: 1.02x faster                                                    |
| sqlglot_transpile       | 1.65 ms                                                                | 1.62 ms: 1.02x faster                                                    |
| go                      | 136 ms                                                                 | 133 ms: 1.02x faster                                                     |
| deepcopy_memo           | 29.7 us                                                                | 29.2 us: 1.02x faster                                                    |
| sphinx                  | 1.11 sec                                                               | 1.09 sec: 1.02x faster                                                   |
| coroutines              | 23.1 ms                                                                | 22.7 ms: 1.02x faster                                                    |
| mako                    | 10.1 ms                                                                | 9.96 ms: 1.02x faster                                                    |
| sqlalchemy_declarative  | 131 ms                                                                 | 129 ms: 1.02x faster                                                     |
| sympy_integrate         | 21.0 ms                                                                | 20.7 ms: 1.01x faster                                                    |
| nqueens                 | 89.2 ms                                                                | 88.1 ms: 1.01x faster                                                    |
| sqlglot_parse           | 1.34 ms                                                                | 1.32 ms: 1.01x faster                                                    |
| pprint_safe_repr        | 723 ms                                                                 | 715 ms: 1.01x faster                                                     |
| logging_silent          | 102 ns                                                                 | 101 ns: 1.01x faster                                                     |
| thrift                  | 780 us                                                                 | 772 us: 1.01x faster                                                     |
| sqlglot_normalize       | 112 ms                                                                 | 111 ms: 1.01x faster                                                     |
| connected_components    | 440 ms                                                                 | 435 ms: 1.01x faster                                                     |
| hexiom                  | 7.11 ms                                                                | 7.04 ms: 1.01x faster                                                    |
| dulwich_log             | 68.0 ms                                                                | 67.4 ms: 1.01x faster                                                    |
| shortest_path           | 485 ms                                                                 | 480 ms: 1.01x faster                                                     |
| sympy_expand            | 481 ms                                                                 | 477 ms: 1.01x faster                                                     |
| deepcopy                | 269 us                                                                 | 267 us: 1.01x faster                                                     |
| 2to3                    | 261 ms                                                                 | 260 ms: 1.00x faster                                                     |
| bpe_tokeniser           | 4.53 sec                                                               | 4.51 sec: 1.00x faster                                                   |
| bench_thread_pool       | 873 us                                                                 | 874 us: 1.00x slower                                                     |
| bench_mp_pool           | 79.0 ms                                                                | 79.3 ms: 1.00x slower                                                    |
| python_startup          | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                                    |
| python_startup_no_site  | 7.06 ms                                                                | 7.09 ms: 1.01x slower                                                    |
| pidigits                | 186 ms                                                                 | 188 ms: 1.01x slower                                                     |
| pathlib                 | 16.2 ms                                                                | 16.4 ms: 1.01x slower                                                    |
| json_dumps              | 11.1 ms                                                                | 11.2 ms: 1.01x slower                                                    |
| create_gc_cycles        | 2.65 ms                                                                | 2.67 ms: 1.01x slower                                                    |
| pickle_pure_python      | 316 us                                                                 | 320 us: 1.01x slower                                                     |
| subparsers              | 21.1 ms                                                                | 21.3 ms: 1.01x slower                                                    |
| raytrace                | 281 ms                                                                 | 284 ms: 1.01x slower                                                     |
| logging_simple          | 5.63 us                                                                | 5.70 us: 1.01x slower                                                    |
| logging_format          | 6.20 us                                                                | 6.28 us: 1.01x slower                                                    |
| pyflate                 | 436 ms                                                                 | 442 ms: 1.01x slower                                                     |
| telco                   | 7.47 ms                                                                | 7.57 ms: 1.01x slower                                                    |
| regex_v8                | 25.5 ms                                                                | 25.9 ms: 1.02x slower                                                    |
| regex_dna               | 215 ms                                                                 | 219 ms: 1.02x slower                                                     |
| regex_effbot            | 3.30 ms                                                                | 3.36 ms: 1.02x slower                                                    |
| async_generators        | 454 ms                                                                 | 461 ms: 1.02x slower                                                     |
| genshi_text             | 24.9 ms                                                                | 25.4 ms: 1.02x slower                                                    |
| spectral_norm           | 112 ms                                                                 | 114 ms: 1.02x slower                                                     |
| generators              | 35.7 ms                                                                | 36.5 ms: 1.02x slower                                                    |
| richards                | 37.4 ms                                                                | 38.5 ms: 1.03x slower                                                    |
| richards_super          | 43.0 ms                                                                | 44.5 ms: 1.04x slower                                                    |
| genshi_xml              | 57.4 ms                                                                | 59.6 ms: 1.04x slower                                                    |
| gc_traversal            | 4.31 ms                                                                | 4.68 ms: 1.09x slower                                                    |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (34): djangocms, xml_etree_parse, pprint_pformat, float, sqlalchemy_imperative, sqlite_synth, fannkuch, scimark_sor, typing_runtime_protocols, unpickle_pure_python, meteor_contest, coverage, chaos, xml_etree_iterparse, nbody, async_tree_none, sqlglot_optimize, k_core, async_tree_none_tg, html5lib, deltablue, json, async_tree_io, scimark_fft, asyncio_websockets, django_template, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization, tomli_loads, async_tree_cpu_io_mixed_tg, deepcopy_reduce, async_tree_cpu_io_mixed, crypto_pyaes

- Geometric mean (including insignificant results): 1.003x faster
# HPT report

- Reliability score: 97.27% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x