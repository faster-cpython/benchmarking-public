# Results vs. 3.13.0

- fork: python
- ref: 759a54d28ffe7eac8c23
- machine: linux-x86_64
- commit hash: 759a54d
- commit date: 2024-10-22
- overall geometric mean: 1.011x slower
- HPT reliability: 82.18%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 314 ms: 1.07x slower                                                         |
| docutils       | 2.81 sec                                                     | 3.22 sec: 1.15x slower                                                       |
| html5lib       | 72.9 ms                                                      | 71.0 ms: 1.03x faster                                                        |
| sphinx         | 1.11 sec                                                     | 1.28 sec: 1.15x slower                                                       |
| tornado_http   | 119 ms                                                       | 124 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 377 ms: 1.21x faster                                                         |
| async_tree_memoization     | 447 ms                                                       | 412 ms: 1.09x faster                                                         |
| async_tree_none            | 370 ms                                                       | 342 ms: 1.08x faster                                                         |
| async_tree_none_tg         | 342 ms                                                       | 328 ms: 1.04x faster                                                         |
| asyncio_websockets         | 395 ms                                                       | 382 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 576 ms: 1.03x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 564 ms: 1.02x faster                                                         |
| async_tree_io_tg           | 823 ms                                                       | 870 ms: 1.06x slower                                                         |
| async_generators           | 364 ms                                                       | 390 ms: 1.07x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 85.6 ms: 1.08x faster                                                        |
| float          | 81.6 ms                                                      | 79.4 ms: 1.03x faster                                                        |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 242 ms: 1.02x slower                                                         |
| regex_v8       | 24.9 ms                                                      | 25.5 ms: 1.02x slower                                                        |
| regex_compile  | 143 ms                                                       | 147 ms: 1.03x slower                                                         |
| regex_effbot   | 3.51 ms                                                      | 3.65 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.10 sec: 1.16x faster                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 84.5 ms: 1.01x faster                                                        |
| xml_etree_process    | 60.7 ms                                                      | 60.3 ms: 1.01x faster                                                        |
| xml_etree_iterparse  | 99.8 ms                                                      | 101 ms: 1.01x slower                                                         |
| json_dumps           | 10.8 ms                                                      | 11.0 ms: 1.02x slower                                                        |
| unpickle_pure_python | 216 us                                                       | 220 us: 1.02x slower                                                         |
| xml_etree_parse      | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| pickle_pure_python   | 322 us                                                       | 333 us: 1.04x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 14.9 ms: 1.05x faster                                                        |
| python_startup_no_site | 8.93 ms                                                      | 9.05 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.42 ms: 1.10x faster                                                        |
| genshi_xml      | 58.0 ms                                                      | 63.6 ms: 1.10x slower                                                        |
| genshi_text     | 27.2 ms                                                      | 30.2 ms: 1.11x slower                                                        |
| django_template | 38.9 ms                                                      | 43.4 ms: 1.12x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.06x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241022-pythonperf2-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 30.0 us: 1.30x faster                                                        |
| deepcopy                   | 388 us                                                       | 309 us: 1.26x faster                                                         |
| async_tree_memoization_tg  | 458 ms                                                       | 377 ms: 1.21x faster                                                         |
| richards_super             | 60.2 ms                                                      | 51.0 ms: 1.18x faster                                                        |
| scimark_sor                | 125 ms                                                       | 106 ms: 1.18x faster                                                         |
| tomli_loads                | 2.43 sec                                                     | 2.10 sec: 1.16x faster                                                       |
| deepcopy_reduce            | 3.49 us                                                      | 3.03 us: 1.15x faster                                                        |
| richards                   | 52.5 ms                                                      | 46.1 ms: 1.14x faster                                                        |
| telco                      | 8.77 ms                                                      | 7.75 ms: 1.13x faster                                                        |
| mako                       | 10.3 ms                                                      | 9.42 ms: 1.10x faster                                                        |
| pyflate                    | 493 ms                                                       | 452 ms: 1.09x faster                                                         |
| go                         | 167 ms                                                       | 154 ms: 1.09x faster                                                         |
| async_tree_memoization     | 447 ms                                                       | 412 ms: 1.09x faster                                                         |
| async_tree_none            | 370 ms                                                       | 342 ms: 1.08x faster                                                         |
| pathlib                    | 17.4 ms                                                      | 16.1 ms: 1.08x faster                                                        |
| nbody                      | 92.1 ms                                                      | 85.6 ms: 1.08x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.77 sec: 1.07x faster                                                       |
| json                       | 5.62 ms                                                      | 5.26 ms: 1.07x faster                                                        |
| pprint_safe_repr           | 835 ms                                                       | 794 ms: 1.05x faster                                                         |
| python_startup             | 15.6 ms                                                      | 14.9 ms: 1.05x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 328 ms: 1.04x faster                                                         |
| scimark_fft                | 298 ms                                                       | 287 ms: 1.04x faster                                                         |
| dulwich_log                | 65.5 ms                                                      | 63.1 ms: 1.04x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 382 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 576 ms: 1.03x faster                                                         |
| deltablue                  | 3.38 ms                                                      | 3.29 ms: 1.03x faster                                                        |
| float                      | 81.6 ms                                                      | 79.4 ms: 1.03x faster                                                        |
| html5lib                   | 72.9 ms                                                      | 71.0 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.67 sec: 1.02x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 95.7 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 564 ms: 1.02x faster                                                         |
| pycparser                  | 1.28 sec                                                     | 1.27 sec: 1.01x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 84.5 ms: 1.01x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 60.3 ms: 1.01x faster                                                        |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                                         |
| meteor_contest             | 130 ms                                                       | 131 ms: 1.01x slower                                                         |
| xml_etree_iterparse        | 99.8 ms                                                      | 101 ms: 1.01x slower                                                         |
| logging_silent             | 97.5 ns                                                      | 98.2 ns: 1.01x slower                                                        |
| thrift                     | 918 us                                                       | 928 us: 1.01x slower                                                         |
| python_startup_no_site     | 8.93 ms                                                      | 9.05 ms: 1.01x slower                                                        |
| regex_dna                  | 238 ms                                                       | 242 ms: 1.02x slower                                                         |
| json_dumps                 | 10.8 ms                                                      | 11.0 ms: 1.02x slower                                                        |
| unpickle_pure_python       | 216 us                                                       | 220 us: 1.02x slower                                                         |
| regex_v8                   | 24.9 ms                                                      | 25.5 ms: 1.02x slower                                                        |
| bench_thread_pool          | 929 us                                                       | 950 us: 1.02x slower                                                         |
| logging_format             | 6.95 us                                                      | 7.12 us: 1.02x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 147 ms: 1.02x slower                                                         |
| regex_compile              | 143 ms                                                       | 147 ms: 1.03x slower                                                         |
| typing_runtime_protocols   | 176 us                                                       | 181 us: 1.03x slower                                                         |
| pickle_pure_python         | 322 us                                                       | 333 us: 1.04x slower                                                         |
| regex_effbot               | 3.51 ms                                                      | 3.65 ms: 1.04x slower                                                        |
| tornado_http               | 119 ms                                                       | 124 ms: 1.04x slower                                                         |
| logging_simple             | 6.28 us                                                      | 6.54 us: 1.04x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.40 ms: 1.04x slower                                                        |
| mdp                        | 2.53 sec                                                     | 2.66 sec: 1.05x slower                                                       |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.6 ms: 1.05x slower                                                        |
| sympy_expand               | 506 ms                                                       | 534 ms: 1.05x slower                                                         |
| async_tree_io_tg           | 823 ms                                                       | 870 ms: 1.06x slower                                                         |
| async_generators           | 364 ms                                                       | 390 ms: 1.07x slower                                                         |
| 2to3                       | 293 ms                                                       | 314 ms: 1.07x slower                                                         |
| comprehensions             | 17.3 us                                                      | 18.8 us: 1.09x slower                                                        |
| sympy_str                  | 297 ms                                                       | 323 ms: 1.09x slower                                                         |
| create_gc_cycles           | 2.65 ms                                                      | 2.89 ms: 1.09x slower                                                        |
| genshi_xml                 | 58.0 ms                                                      | 63.6 ms: 1.10x slower                                                        |
| sqlglot_parse              | 1.37 ms                                                      | 1.51 ms: 1.10x slower                                                        |
| genshi_text                | 27.2 ms                                                      | 30.2 ms: 1.11x slower                                                        |
| hexiom                     | 6.47 ms                                                      | 7.21 ms: 1.11x slower                                                        |
| django_template            | 38.9 ms                                                      | 43.4 ms: 1.12x slower                                                        |
| nqueens                    | 92.3 ms                                                      | 103 ms: 1.12x slower                                                         |
| sqlglot_normalize          | 119 ms                                                       | 133 ms: 1.12x slower                                                         |
| sqlglot_transpile          | 1.76 ms                                                      | 1.98 ms: 1.12x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.22 sec: 1.15x slower                                                       |
| chaos                      | 60.6 ms                                                      | 69.5 ms: 1.15x slower                                                        |
| sphinx                     | 1.11 sec                                                     | 1.28 sec: 1.15x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 177 ms: 1.15x slower                                                         |
| generators                 | 33.9 ms                                                      | 39.7 ms: 1.17x slower                                                        |
| sympy_integrate            | 23.4 ms                                                      | 27.6 ms: 1.18x slower                                                        |
| sqlglot_optimize           | 58.7 ms                                                      | 69.6 ms: 1.19x slower                                                        |
| pylint                     | 345 ms                                                       | 424 ms: 1.23x slower                                                         |
| gc_traversal               | 4.48 ms                                                      | 5.53 ms: 1.23x slower                                                        |
| raytrace                   | 267 ms                                                       | 336 ms: 1.26x slower                                                         |
| bench_mp_pool              | 4.82 ms                                                      | 2.18 sec: 452.88x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                 |

Benchmark hidden because not significant (6): fannkuch, crypto_pyaes, scimark_lu, json_loads, async_tree_io, coverage
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.011x slower
# HPT report

- Reliability score: 82.18% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x