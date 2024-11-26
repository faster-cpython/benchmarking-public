# Results vs. 3.13.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: linux-x86_64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.007x slower
- HPT reliability: 53.40%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 317 ms: 1.08x slower                                                         |
| docutils       | 2.81 sec                                                     | 3.21 sec: 1.14x slower                                                       |
| html5lib       | 72.9 ms                                                      | 72.2 ms: 1.01x faster                                                        |
| sphinx         | 1.11 sec                                                     | 1.27 sec: 1.14x slower                                                       |
| tornado_http   | 119 ms                                                       | 123 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 378 ms: 1.21x faster                                                         |
| async_tree_none            | 370 ms                                                       | 343 ms: 1.08x faster                                                         |
| async_tree_memoization     | 447 ms                                                       | 417 ms: 1.07x faster                                                         |
| async_tree_none_tg         | 342 ms                                                       | 326 ms: 1.05x faster                                                         |
| asyncio_websockets         | 395 ms                                                       | 382 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 581 ms: 1.03x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 568 ms: 1.01x faster                                                         |
| async_tree_io              | 832 ms                                                       | 846 ms: 1.02x slower                                                         |
| async_generators           | 364 ms                                                       | 382 ms: 1.05x slower                                                         |
| async_tree_io_tg           | 823 ms                                                       | 874 ms: 1.06x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 85.2 ms: 1.08x faster                                                        |
| float          | 81.6 ms                                                      | 79.2 ms: 1.03x faster                                                        |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 244 ms: 1.02x slower                                                         |
| regex_v8       | 24.9 ms                                                      | 25.6 ms: 1.03x slower                                                        |
| regex_compile  | 143 ms                                                       | 147 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.09 sec: 1.16x faster                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 82.3 ms: 1.04x faster                                                        |
| xml_etree_process    | 60.7 ms                                                      | 59.0 ms: 1.03x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 141 ms: 1.02x faster                                                         |
| unpickle_pure_python | 216 us                                                       | 217 us: 1.00x slower                                                         |
| json_loads           | 24.7 us                                                      | 24.8 us: 1.01x slower                                                        |
| json_dumps           | 10.8 ms                                                      | 11.0 ms: 1.02x slower                                                        |
| pickle_pure_python   | 322 us                                                       | 337 us: 1.05x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 14.8 ms: 1.06x faster                                                        |
| python_startup_no_site | 8.93 ms                                                      | 8.99 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.48 ms: 1.09x faster                                                        |
| genshi_text     | 27.2 ms                                                      | 27.6 ms: 1.02x slower                                                        |
| genshi_xml      | 58.0 ms                                                      | 63.2 ms: 1.09x slower                                                        |
| django_template | 38.9 ms                                                      | 44.8 ms: 1.15x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 30.0 us: 1.30x faster                                                        |
| deepcopy                   | 388 us                                                       | 307 us: 1.26x faster                                                         |
| async_tree_memoization_tg  | 458 ms                                                       | 378 ms: 1.21x faster                                                         |
| scimark_sor                | 125 ms                                                       | 105 ms: 1.19x faster                                                         |
| tomli_loads                | 2.43 sec                                                     | 2.09 sec: 1.16x faster                                                       |
| deepcopy_reduce            | 3.49 us                                                      | 3.07 us: 1.14x faster                                                        |
| richards                   | 52.5 ms                                                      | 46.4 ms: 1.13x faster                                                        |
| telco                      | 8.77 ms                                                      | 7.75 ms: 1.13x faster                                                        |
| json                       | 5.62 ms                                                      | 5.15 ms: 1.09x faster                                                        |
| mako                       | 10.3 ms                                                      | 9.48 ms: 1.09x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                        |
| richards_super             | 60.2 ms                                                      | 55.4 ms: 1.09x faster                                                        |
| nbody                      | 92.1 ms                                                      | 85.2 ms: 1.08x faster                                                        |
| pyflate                    | 493 ms                                                       | 456 ms: 1.08x faster                                                         |
| go                         | 167 ms                                                       | 155 ms: 1.08x faster                                                         |
| async_tree_none            | 370 ms                                                       | 343 ms: 1.08x faster                                                         |
| async_tree_memoization     | 447 ms                                                       | 417 ms: 1.07x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.77 sec: 1.07x faster                                                       |
| pprint_safe_repr           | 835 ms                                                       | 788 ms: 1.06x faster                                                         |
| logging_silent             | 97.5 ns                                                      | 92.0 ns: 1.06x faster                                                        |
| python_startup             | 15.6 ms                                                      | 14.8 ms: 1.06x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 92.5 ms: 1.05x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 326 ms: 1.05x faster                                                         |
| pprint_pformat             | 1.70 sec                                                     | 1.62 sec: 1.05x faster                                                       |
| fannkuch                   | 384 ms                                                       | 368 ms: 1.05x faster                                                         |
| coverage                   | 84.5 ms                                                      | 81.3 ms: 1.04x faster                                                        |
| dulwich_log                | 65.5 ms                                                      | 63.1 ms: 1.04x faster                                                        |
| xml_etree_generate         | 85.2 ms                                                      | 82.3 ms: 1.04x faster                                                        |
| scimark_fft                | 298 ms                                                       | 288 ms: 1.04x faster                                                         |
| asyncio_websockets         | 395 ms                                                       | 382 ms: 1.03x faster                                                         |
| float                      | 81.6 ms                                                      | 79.2 ms: 1.03x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 59.0 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 581 ms: 1.03x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                        |
| thrift                     | 918 us                                                       | 898 us: 1.02x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 141 ms: 1.02x faster                                                         |
| deltablue                  | 3.38 ms                                                      | 3.33 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 568 ms: 1.01x faster                                                         |
| crypto_pyaes               | 73.5 ms                                                      | 72.8 ms: 1.01x faster                                                        |
| html5lib                   | 72.9 ms                                                      | 72.2 ms: 1.01x faster                                                        |
| scimark_lu                 | 97.4 ms                                                      | 96.5 ms: 1.01x faster                                                        |
| meteor_contest             | 130 ms                                                       | 130 ms: 1.00x faster                                                         |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                                         |
| unpickle_pure_python       | 216 us                                                       | 217 us: 1.00x slower                                                         |
| json_loads                 | 24.7 us                                                      | 24.8 us: 1.01x slower                                                        |
| python_startup_no_site     | 8.93 ms                                                      | 8.99 ms: 1.01x slower                                                        |
| genshi_text                | 27.2 ms                                                      | 27.6 ms: 1.02x slower                                                        |
| bench_thread_pool          | 929 us                                                       | 945 us: 1.02x slower                                                         |
| async_tree_io              | 832 ms                                                       | 846 ms: 1.02x slower                                                         |
| json_dumps                 | 10.8 ms                                                      | 11.0 ms: 1.02x slower                                                        |
| mdp                        | 2.53 sec                                                     | 2.58 sec: 1.02x slower                                                       |
| regex_dna                  | 238 ms                                                       | 244 ms: 1.02x slower                                                         |
| regex_v8                   | 24.9 ms                                                      | 25.6 ms: 1.03x slower                                                        |
| regex_compile              | 143 ms                                                       | 147 ms: 1.03x slower                                                         |
| tornado_http               | 119 ms                                                       | 123 ms: 1.03x slower                                                         |
| typing_runtime_protocols   | 176 us                                                       | 183 us: 1.05x slower                                                         |
| pickle_pure_python         | 322 us                                                       | 337 us: 1.05x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.42 ms: 1.05x slower                                                        |
| async_generators           | 364 ms                                                       | 382 ms: 1.05x slower                                                         |
| sympy_expand               | 506 ms                                                       | 533 ms: 1.05x slower                                                         |
| async_tree_io_tg           | 823 ms                                                       | 874 ms: 1.06x slower                                                         |
| scimark_monte_carlo        | 65.2 ms                                                      | 69.3 ms: 1.06x slower                                                        |
| comprehensions             | 17.3 us                                                      | 18.7 us: 1.08x slower                                                        |
| sympy_str                  | 297 ms                                                       | 321 ms: 1.08x slower                                                         |
| logging_format             | 6.95 us                                                      | 7.53 us: 1.08x slower                                                        |
| 2to3                       | 293 ms                                                       | 317 ms: 1.08x slower                                                         |
| genshi_xml                 | 58.0 ms                                                      | 63.2 ms: 1.09x slower                                                        |
| logging_simple             | 6.28 us                                                      | 6.84 us: 1.09x slower                                                        |
| create_gc_cycles           | 2.65 ms                                                      | 2.89 ms: 1.09x slower                                                        |
| hexiom                     | 6.47 ms                                                      | 7.19 ms: 1.11x slower                                                        |
| nqueens                    | 92.3 ms                                                      | 102 ms: 1.11x slower                                                         |
| sqlglot_parse              | 1.37 ms                                                      | 1.52 ms: 1.11x slower                                                        |
| chaos                      | 60.6 ms                                                      | 68.1 ms: 1.12x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                        |
| sqlglot_normalize          | 119 ms                                                       | 135 ms: 1.13x slower                                                         |
| sympy_sum                  | 154 ms                                                       | 175 ms: 1.14x slower                                                         |
| sphinx                     | 1.11 sec                                                     | 1.27 sec: 1.14x slower                                                       |
| generators                 | 33.9 ms                                                      | 38.7 ms: 1.14x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.21 sec: 1.14x slower                                                       |
| django_template            | 38.9 ms                                                      | 44.8 ms: 1.15x slower                                                        |
| raytrace                   | 267 ms                                                       | 310 ms: 1.16x slower                                                         |
| gc_traversal               | 4.48 ms                                                      | 5.21 ms: 1.16x slower                                                        |
| sympy_integrate            | 23.4 ms                                                      | 27.3 ms: 1.17x slower                                                        |
| sqlglot_optimize           | 58.7 ms                                                      | 70.2 ms: 1.20x slower                                                        |
| pylint                     | 345 ms                                                       | 422 ms: 1.22x slower                                                         |
| bench_mp_pool              | 4.82 ms                                                      | 1.74 sec: 361.98x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                                 |

Benchmark hidden because not significant (3): xml_etree_iterparse, pycparser, regex_effbot
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.007x slower
# HPT report

- Reliability score: 53.40% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x