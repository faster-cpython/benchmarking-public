# Results vs. 3.13.0

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 1e0f842
- commit date: 2025-01-24
- overall geometric mean: 1.067x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 280 ms: 1.05x faster                                                                   |
| docutils       | 2.83 sec                                                     | 2.87 sec: 1.01x slower                                                                 |
| html5lib       | 73.5 ms                                                      | 66.3 ms: 1.11x faster                                                                  |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                                   |
| async_tree_io              | 843 ms                                                       | 645 ms: 1.31x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 289 ms: 1.30x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 350 ms: 1.30x faster                                                                   |
| async_tree_io_tg           | 831 ms                                                       | 645 ms: 1.29x faster                                                                   |
| async_tree_none_tg         | 346 ms                                                       | 278 ms: 1.24x faster                                                                   |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 522 ms: 1.16x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                                   |
| async_generators           | 457 ms                                                       | 405 ms: 1.13x faster                                                                   |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                                  |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 68.7 ms: 1.18x faster                                                                  |
| nbody          | 89.3 ms                                                      | 87.8 ms: 1.02x faster                                                                  |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.13 ms: 1.17x faster                                                                  |
| regex_compile  | 143 ms                                                       | 135 ms: 1.06x faster                                                                   |
| regex_dna      | 247 ms                                                       | 236 ms: 1.05x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.04 sec: 1.21x faster                                                                 |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.10x faster                                                                   |
| unpickle_pure_python | 217 us                                                       | 205 us: 1.06x faster                                                                   |
| xml_etree_process    | 61.2 ms                                                      | 58.7 ms: 1.04x faster                                                                  |
| xml_etree_generate   | 86.5 ms                                                      | 84.1 ms: 1.03x faster                                                                  |
| xml_etree_iterparse  | 103 ms                                                       | 104 ms: 1.02x slower                                                                   |
| json_loads           | 24.7 us                                                      | 25.6 us: 1.04x slower                                                                  |
| json_dumps           | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                           |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 8.97 ms: 1.00x slower                                                                  |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.00x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.5 ms: 1.11x faster                                                                  |
| genshi_xml      | 57.1 ms                                                      | 52.3 ms: 1.09x faster                                                                  |
| django_template | 36.4 ms                                                      | 35.8 ms: 1.02x faster                                                                  |
| mako            | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                                   |
| deepcopy                   | 392 us                                                       | 282 us: 1.39x faster                                                                   |
| async_tree_io              | 843 ms                                                       | 645 ms: 1.31x faster                                                                   |
| async_tree_none            | 376 ms                                                       | 289 ms: 1.30x faster                                                                   |
| go                         | 162 ms                                                       | 125 ms: 1.30x faster                                                                   |
| async_tree_memoization     | 453 ms                                                       | 350 ms: 1.30x faster                                                                   |
| async_tree_io_tg           | 831 ms                                                       | 645 ms: 1.29x faster                                                                   |
| deepcopy_memo              | 38.6 us                                                      | 30.2 us: 1.28x faster                                                                  |
| async_tree_none_tg         | 346 ms                                                       | 278 ms: 1.24x faster                                                                   |
| deepcopy_reduce            | 3.54 us                                                      | 2.91 us: 1.22x faster                                                                  |
| tomli_loads                | 2.46 sec                                                     | 2.04 sec: 1.21x faster                                                                 |
| generators                 | 33.6 ms                                                      | 28.0 ms: 1.20x faster                                                                  |
| float                      | 81.3 ms                                                      | 68.7 ms: 1.18x faster                                                                  |
| regex_effbot               | 3.67 ms                                                      | 3.13 ms: 1.17x faster                                                                  |
| richards                   | 52.9 ms                                                      | 45.4 ms: 1.17x faster                                                                  |
| spectral_norm              | 97.0 ms                                                      | 83.2 ms: 1.17x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 522 ms: 1.16x faster                                                                   |
| richards_super             | 59.6 ms                                                      | 51.6 ms: 1.15x faster                                                                  |
| scimark_sor                | 123 ms                                                       | 107 ms: 1.15x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                                   |
| async_generators           | 457 ms                                                       | 405 ms: 1.13x faster                                                                   |
| genshi_text                | 26.2 ms                                                      | 23.5 ms: 1.11x faster                                                                  |
| pyflate                    | 503 ms                                                       | 452 ms: 1.11x faster                                                                   |
| html5lib                   | 73.5 ms                                                      | 66.3 ms: 1.11x faster                                                                  |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.10x faster                                                                   |
| pylint                     | 347 ms                                                       | 314 ms: 1.10x faster                                                                   |
| pathlib                    | 17.5 ms                                                      | 15.9 ms: 1.10x faster                                                                  |
| bpe_tokeniser              | 5.09 sec                                                     | 4.62 sec: 1.10x faster                                                                 |
| telco                      | 8.79 ms                                                      | 8.03 ms: 1.10x faster                                                                  |
| pprint_pformat             | 1.72 sec                                                     | 1.57 sec: 1.09x faster                                                                 |
| genshi_xml                 | 57.1 ms                                                      | 52.3 ms: 1.09x faster                                                                  |
| scimark_fft                | 328 ms                                                       | 300 ms: 1.09x faster                                                                   |
| hexiom                     | 6.55 ms                                                      | 6.02 ms: 1.09x faster                                                                  |
| pprint_safe_repr           | 843 ms                                                       | 778 ms: 1.08x faster                                                                   |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.0 ms: 1.07x faster                                                                  |
| sqlglot_parse              | 1.40 ms                                                      | 1.31 ms: 1.07x faster                                                                  |
| unpickle_pure_python       | 217 us                                                       | 205 us: 1.06x faster                                                                   |
| json                       | 5.69 ms                                                      | 5.36 ms: 1.06x faster                                                                  |
| scimark_lu                 | 98.7 ms                                                      | 93.1 ms: 1.06x faster                                                                  |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.51 ms: 1.06x faster                                                                  |
| sqlglot_normalize          | 119 ms                                                       | 113 ms: 1.06x faster                                                                   |
| regex_compile              | 143 ms                                                       | 135 ms: 1.06x faster                                                                   |
| sqlglot_transpile          | 1.79 ms                                                      | 1.70 ms: 1.05x faster                                                                  |
| sqlite_synth               | 2.91 us                                                      | 2.78 us: 1.05x faster                                                                  |
| regex_dna                  | 247 ms                                                       | 236 ms: 1.05x faster                                                                   |
| 2to3                       | 293 ms                                                       | 280 ms: 1.05x faster                                                                   |
| coverage                   | 80.0 ms                                                      | 76.5 ms: 1.05x faster                                                                  |
| connected_components       | 432 ms                                                       | 414 ms: 1.04x faster                                                                   |
| deltablue                  | 3.42 ms                                                      | 3.28 ms: 1.04x faster                                                                  |
| xml_etree_process          | 61.2 ms                                                      | 58.7 ms: 1.04x faster                                                                  |
| k_core                     | 2.17 sec                                                     | 2.08 sec: 1.04x faster                                                                 |
| coroutines                 | 21.6 ms                                                      | 20.7 ms: 1.04x faster                                                                  |
| shortest_path              | 460 ms                                                       | 442 ms: 1.04x faster                                                                   |
| mdp                        | 2.54 sec                                                     | 2.44 sec: 1.04x faster                                                                 |
| sqlglot_optimize           | 59.3 ms                                                      | 57.1 ms: 1.04x faster                                                                  |
| sqlalchemy_declarative     | 148 ms                                                       | 143 ms: 1.04x faster                                                                   |
| raytrace                   | 273 ms                                                       | 263 ms: 1.04x faster                                                                   |
| logging_simple             | 6.39 us                                                      | 6.17 us: 1.04x faster                                                                  |
| sympy_str                  | 298 ms                                                       | 288 ms: 1.04x faster                                                                   |
| chaos                      | 60.2 ms                                                      | 58.2 ms: 1.03x faster                                                                  |
| sympy_expand               | 509 ms                                                       | 493 ms: 1.03x faster                                                                   |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.7 ms: 1.03x faster                                                                  |
| sympy_sum                  | 155 ms                                                       | 150 ms: 1.03x faster                                                                   |
| thrift                     | 901 us                                                       | 874 us: 1.03x faster                                                                   |
| pycparser                  | 1.24 sec                                                     | 1.21 sec: 1.03x faster                                                                 |
| xml_etree_generate         | 86.5 ms                                                      | 84.1 ms: 1.03x faster                                                                  |
| dulwich_log                | 68.2 ms                                                      | 66.3 ms: 1.03x faster                                                                  |
| sympy_integrate            | 23.6 ms                                                      | 22.9 ms: 1.03x faster                                                                  |
| logging_format             | 6.94 us                                                      | 6.75 us: 1.03x faster                                                                  |
| nqueens                    | 90.7 ms                                                      | 88.7 ms: 1.02x faster                                                                  |
| bench_thread_pool          | 942 us                                                       | 922 us: 1.02x faster                                                                   |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                                 |
| nbody                      | 89.3 ms                                                      | 87.8 ms: 1.02x faster                                                                  |
| django_template            | 36.4 ms                                                      | 35.8 ms: 1.02x faster                                                                  |
| meteor_contest             | 130 ms                                                       | 128 ms: 1.02x faster                                                                   |
| fannkuch                   | 363 ms                                                       | 361 ms: 1.01x faster                                                                   |
| logging_silent             | 97.9 ns                                                      | 97.4 ns: 1.00x faster                                                                  |
| python_startup_no_site     | 8.96 ms                                                      | 8.97 ms: 1.00x slower                                                                  |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.00x slower                                                                  |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                                   |
| crypto_pyaes               | 73.3 ms                                                      | 73.8 ms: 1.01x slower                                                                  |
| docutils                   | 2.83 sec                                                     | 2.87 sec: 1.01x slower                                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 104 ms: 1.02x slower                                                                   |
| typing_runtime_protocols   | 169 us                                                       | 174 us: 1.03x slower                                                                   |
| create_gc_cycles           | 2.68 ms                                                      | 2.78 ms: 1.04x slower                                                                  |
| json_loads                 | 24.7 us                                                      | 25.6 us: 1.04x slower                                                                  |
| comprehensions             | 17.0 us                                                      | 17.8 us: 1.05x slower                                                                  |
| mako                       | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                                  |
| json_dumps                 | 11.1 ms                                                      | 11.7 ms: 1.05x slower                                                                  |
| many_optionals             | 930 us                                                       | 1.01 ms: 1.08x slower                                                                  |
| subparsers                 | 17.5 ms                                                      | 23.0 ms: 1.32x slower                                                                  |
| gc_traversal               | 4.74 ms                                                      | 6.32 ms: 1.33x slower                                                                  |
| bench_mp_pool              | 5.12 ms                                                      | 1.02 sec: 198.39x slower                                                               |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, pickle_pure_python, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.067x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.02x