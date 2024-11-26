# Results vs. 3.13.0

- fork: faster-cpython
- ref: load_const_return_re
- machine: linux-x86_64
- commit hash: 031f320
- commit date: 2024-10-23
- overall geometric mean: 1.008x slower
- HPT reliability: 59.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 317 ms: 1.08x slower                                                                   |
| docutils       | 2.81 sec                                                     | 3.19 sec: 1.14x slower                                                                 |
| html5lib       | 72.9 ms                                                      | 71.8 ms: 1.02x faster                                                                  |
| sphinx         | 1.11 sec                                                     | 1.26 sec: 1.13x slower                                                                 |
| tornado_http   | 119 ms                                                       | 123 ms: 1.03x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 371 ms: 1.23x faster                                                                   |
| async_tree_none            | 370 ms                                                       | 337 ms: 1.10x faster                                                                   |
| async_tree_memoization     | 447 ms                                                       | 409 ms: 1.09x faster                                                                   |
| async_tree_none_tg         | 342 ms                                                       | 321 ms: 1.07x faster                                                                   |
| coroutines                 | 21.6 ms                                                      | 20.4 ms: 1.06x faster                                                                  |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                                   |
| asyncio_websockets         | 395 ms                                                       | 385 ms: 1.03x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 560 ms: 1.02x faster                                                                   |
| async_generators           | 364 ms                                                       | 380 ms: 1.05x slower                                                                   |
| async_tree_io_tg           | 823 ms                                                       | 861 ms: 1.05x slower                                                                   |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                           |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 85.3 ms: 1.08x faster                                                                  |
| float          | 81.6 ms                                                      | 80.7 ms: 1.01x faster                                                                  |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 234 ms: 1.02x faster                                                                   |
| regex_v8       | 24.9 ms                                                      | 24.8 ms: 1.01x faster                                                                  |
| regex_effbot   | 3.51 ms                                                      | 3.60 ms: 1.02x slower                                                                  |
| regex_compile  | 143 ms                                                       | 147 ms: 1.03x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.13 sec: 1.15x faster                                                                 |
| xml_etree_process    | 60.7 ms                                                      | 56.9 ms: 1.07x faster                                                                  |
| xml_etree_generate   | 85.2 ms                                                      | 80.0 ms: 1.06x faster                                                                  |
| json_loads           | 24.7 us                                                      | 24.6 us: 1.01x faster                                                                  |
| json_dumps           | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                                                  |
| xml_etree_iterparse  | 99.8 ms                                                      | 101 ms: 1.02x slower                                                                   |
| xml_etree_parse      | 144 ms                                                       | 147 ms: 1.02x slower                                                                   |
| unpickle_pure_python | 216 us                                                       | 222 us: 1.03x slower                                                                   |
| pickle_pure_python   | 322 us                                                       | 340 us: 1.06x slower                                                                   |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 15.1 ms: 1.04x faster                                                                  |
| python_startup_no_site | 8.93 ms                                                      | 9.11 ms: 1.02x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.01x faster                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.44 ms: 1.09x faster                                                                  |
| genshi_text     | 27.2 ms                                                      | 29.9 ms: 1.10x slower                                                                  |
| django_template | 38.9 ms                                                      | 43.8 ms: 1.13x slower                                                                  |
| genshi_xml      | 58.0 ms                                                      | 66.9 ms: 1.15x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.07x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-pythonperf2-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-031f320 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 30.3 us: 1.28x faster                                                                  |
| async_tree_memoization_tg  | 458 ms                                                       | 371 ms: 1.23x faster                                                                   |
| deepcopy                   | 388 us                                                       | 316 us: 1.23x faster                                                                   |
| scimark_sor                | 125 ms                                                       | 104 ms: 1.20x faster                                                                   |
| deepcopy_reduce            | 3.49 us                                                      | 3.04 us: 1.15x faster                                                                  |
| tomli_loads                | 2.43 sec                                                     | 2.13 sec: 1.15x faster                                                                 |
| telco                      | 8.77 ms                                                      | 7.69 ms: 1.14x faster                                                                  |
| richards_super             | 60.2 ms                                                      | 54.6 ms: 1.10x faster                                                                  |
| async_tree_none            | 370 ms                                                       | 337 ms: 1.10x faster                                                                   |
| async_tree_memoization     | 447 ms                                                       | 409 ms: 1.09x faster                                                                   |
| mako                       | 10.3 ms                                                      | 9.44 ms: 1.09x faster                                                                  |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                                  |
| richards                   | 52.5 ms                                                      | 48.3 ms: 1.09x faster                                                                  |
| pyflate                    | 493 ms                                                       | 456 ms: 1.08x faster                                                                   |
| nbody                      | 92.1 ms                                                      | 85.3 ms: 1.08x faster                                                                  |
| json                       | 5.62 ms                                                      | 5.21 ms: 1.08x faster                                                                  |
| bpe_tokeniser              | 5.09 sec                                                     | 4.77 sec: 1.07x faster                                                                 |
| xml_etree_process          | 60.7 ms                                                      | 56.9 ms: 1.07x faster                                                                  |
| async_tree_none_tg         | 342 ms                                                       | 321 ms: 1.07x faster                                                                   |
| coverage                   | 84.5 ms                                                      | 79.3 ms: 1.07x faster                                                                  |
| xml_etree_generate         | 85.2 ms                                                      | 80.0 ms: 1.06x faster                                                                  |
| pprint_safe_repr           | 835 ms                                                       | 784 ms: 1.06x faster                                                                   |
| go                         | 167 ms                                                       | 157 ms: 1.06x faster                                                                   |
| coroutines                 | 21.6 ms                                                      | 20.4 ms: 1.06x faster                                                                  |
| pprint_pformat             | 1.70 sec                                                     | 1.62 sec: 1.05x faster                                                                 |
| spectral_norm              | 97.4 ms                                                      | 93.3 ms: 1.04x faster                                                                  |
| python_startup             | 15.6 ms                                                      | 15.1 ms: 1.04x faster                                                                  |
| scimark_fft                | 298 ms                                                       | 288 ms: 1.04x faster                                                                   |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 575 ms: 1.04x faster                                                                   |
| thrift                     | 918 us                                                       | 887 us: 1.03x faster                                                                   |
| deltablue                  | 3.38 ms                                                      | 3.29 ms: 1.03x faster                                                                  |
| dulwich_log                | 65.5 ms                                                      | 63.8 ms: 1.03x faster                                                                  |
| asyncio_websockets         | 395 ms                                                       | 385 ms: 1.03x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 560 ms: 1.02x faster                                                                   |
| fannkuch                   | 384 ms                                                       | 375 ms: 1.02x faster                                                                   |
| regex_dna                  | 238 ms                                                       | 234 ms: 1.02x faster                                                                   |
| html5lib                   | 72.9 ms                                                      | 71.8 ms: 1.02x faster                                                                  |
| float                      | 81.6 ms                                                      | 80.7 ms: 1.01x faster                                                                  |
| json_loads                 | 24.7 us                                                      | 24.6 us: 1.01x faster                                                                  |
| regex_v8                   | 24.9 ms                                                      | 24.8 ms: 1.01x faster                                                                  |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                                                   |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.25 ms: 1.01x slower                                                                  |
| json_dumps                 | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                                                  |
| pycparser                  | 1.28 sec                                                     | 1.30 sec: 1.01x slower                                                                 |
| xml_etree_iterparse        | 99.8 ms                                                      | 101 ms: 1.02x slower                                                                   |
| python_startup_no_site     | 8.93 ms                                                      | 9.11 ms: 1.02x slower                                                                  |
| xml_etree_parse            | 144 ms                                                       | 147 ms: 1.02x slower                                                                   |
| regex_effbot               | 3.51 ms                                                      | 3.60 ms: 1.02x slower                                                                  |
| unpickle_pure_python       | 216 us                                                       | 222 us: 1.03x slower                                                                   |
| bench_thread_pool          | 929 us                                                       | 954 us: 1.03x slower                                                                   |
| mdp                        | 2.53 sec                                                     | 2.60 sec: 1.03x slower                                                                 |
| regex_compile              | 143 ms                                                       | 147 ms: 1.03x slower                                                                   |
| logging_format             | 6.95 us                                                      | 7.18 us: 1.03x slower                                                                  |
| tornado_http               | 119 ms                                                       | 123 ms: 1.03x slower                                                                   |
| typing_runtime_protocols   | 176 us                                                       | 182 us: 1.03x slower                                                                   |
| async_generators           | 364 ms                                                       | 380 ms: 1.05x slower                                                                   |
| async_tree_io_tg           | 823 ms                                                       | 861 ms: 1.05x slower                                                                   |
| sympy_expand               | 506 ms                                                       | 533 ms: 1.05x slower                                                                   |
| pickle_pure_python         | 322 us                                                       | 340 us: 1.06x slower                                                                   |
| logging_silent             | 97.5 ns                                                      | 103 ns: 1.06x slower                                                                   |
| logging_simple             | 6.28 us                                                      | 6.69 us: 1.07x slower                                                                  |
| scimark_monte_carlo        | 65.2 ms                                                      | 70.3 ms: 1.08x slower                                                                  |
| nqueens                    | 92.3 ms                                                      | 99.5 ms: 1.08x slower                                                                  |
| sympy_str                  | 297 ms                                                       | 321 ms: 1.08x slower                                                                   |
| 2to3                       | 293 ms                                                       | 317 ms: 1.08x slower                                                                   |
| comprehensions             | 17.3 us                                                      | 18.9 us: 1.09x slower                                                                  |
| genshi_text                | 27.2 ms                                                      | 29.9 ms: 1.10x slower                                                                  |
| create_gc_cycles           | 2.65 ms                                                      | 2.92 ms: 1.10x slower                                                                  |
| sqlglot_parse              | 1.37 ms                                                      | 1.52 ms: 1.11x slower                                                                  |
| hexiom                     | 6.47 ms                                                      | 7.20 ms: 1.11x slower                                                                  |
| chaos                      | 60.6 ms                                                      | 67.7 ms: 1.12x slower                                                                  |
| sqlglot_transpile          | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                                  |
| django_template            | 38.9 ms                                                      | 43.8 ms: 1.13x slower                                                                  |
| sphinx                     | 1.11 sec                                                     | 1.26 sec: 1.13x slower                                                                 |
| sqlglot_normalize          | 119 ms                                                       | 135 ms: 1.13x slower                                                                   |
| docutils                   | 2.81 sec                                                     | 3.19 sec: 1.14x slower                                                                 |
| sympy_sum                  | 154 ms                                                       | 175 ms: 1.14x slower                                                                   |
| generators                 | 33.9 ms                                                      | 38.9 ms: 1.15x slower                                                                  |
| genshi_xml                 | 58.0 ms                                                      | 66.9 ms: 1.15x slower                                                                  |
| sympy_integrate            | 23.4 ms                                                      | 27.3 ms: 1.17x slower                                                                  |
| sqlglot_optimize           | 58.7 ms                                                      | 69.7 ms: 1.19x slower                                                                  |
| pylint                     | 345 ms                                                       | 415 ms: 1.20x slower                                                                   |
| raytrace                   | 267 ms                                                       | 323 ms: 1.21x slower                                                                   |
| gc_traversal               | 4.48 ms                                                      | 5.80 ms: 1.29x slower                                                                  |
| bench_mp_pool              | 4.82 ms                                                      | 2.57 sec: 533.53x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                           |

Benchmark hidden because not significant (4): async_tree_io, crypto_pyaes, scimark_lu, meteor_contest
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.008x slower
# HPT report

- Reliability score: 59.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x