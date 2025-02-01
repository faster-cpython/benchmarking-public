# Results vs. 3.13.0

- fork: faster-cpython
- ref: make_opcode_static
- machine: linux-x86_64
- commit hash: 536ee25
- commit date: 2025-01-31
- overall geometric mean: 1.069x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 279 ms: 1.05x faster                                                                 |
| docutils       | 2.83 sec                                                     | 2.84 sec: 1.00x slower                                                               |
| html5lib       | 73.5 ms                                                      | 65.7 ms: 1.12x faster                                                                |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                               |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 335 ms: 1.39x faster                                                                 |
| async_tree_none            | 376 ms                                                       | 288 ms: 1.31x faster                                                                 |
| async_tree_io              | 843 ms                                                       | 652 ms: 1.29x faster                                                                 |
| async_tree_memoization     | 453 ms                                                       | 351 ms: 1.29x faster                                                                 |
| async_tree_io_tg           | 831 ms                                                       | 645 ms: 1.29x faster                                                                 |
| async_tree_none_tg         | 346 ms                                                       | 276 ms: 1.26x faster                                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 520 ms: 1.16x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                                 |
| async_generators           | 457 ms                                                       | 411 ms: 1.11x faster                                                                 |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                                |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                                 |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.5 ms: 1.17x faster                                                                |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                         |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.13 ms: 1.17x faster                                                                |
| regex_dna      | 247 ms                                                       | 230 ms: 1.07x faster                                                                 |
| regex_compile  | 143 ms                                                       | 133 ms: 1.07x faster                                                                 |
| regex_v8       | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                                                |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.04 sec: 1.21x faster                                                               |
| xml_etree_parse      | 150 ms                                                       | 138 ms: 1.09x faster                                                                 |
| xml_etree_iterparse  | 103 ms                                                       | 96.3 ms: 1.07x faster                                                                |
| unpickle_pure_python | 217 us                                                       | 205 us: 1.06x faster                                                                 |
| xml_etree_process    | 61.2 ms                                                      | 59.8 ms: 1.02x faster                                                                |
| xml_etree_generate   | 86.5 ms                                                      | 84.7 ms: 1.02x faster                                                                |
| json_dumps           | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                                |
| json_loads           | 24.7 us                                                      | 26.5 us: 1.07x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                         |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.00 ms: 1.00x slower                                                                |
| python_startup         | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                                |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.0 ms: 1.14x faster                                                                |
| genshi_xml      | 57.1 ms                                                      | 51.8 ms: 1.10x faster                                                                |
| django_template | 36.4 ms                                                      | 35.1 ms: 1.03x faster                                                                |
| mako            | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                                |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-pythonperf2-x86_64-faster%2dcpython-make_opcode_static-3.14.0a4+-536ee25 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 277 us: 1.42x faster                                                                 |
| async_tree_memoization_tg  | 466 ms                                                       | 335 ms: 1.39x faster                                                                 |
| deepcopy_memo              | 38.6 us                                                      | 29.4 us: 1.31x faster                                                                |
| async_tree_none            | 376 ms                                                       | 288 ms: 1.31x faster                                                                 |
| go                         | 162 ms                                                       | 124 ms: 1.30x faster                                                                 |
| async_tree_io              | 843 ms                                                       | 652 ms: 1.29x faster                                                                 |
| async_tree_memoization     | 453 ms                                                       | 351 ms: 1.29x faster                                                                 |
| async_tree_io_tg           | 831 ms                                                       | 645 ms: 1.29x faster                                                                 |
| async_tree_none_tg         | 346 ms                                                       | 276 ms: 1.26x faster                                                                 |
| deepcopy_reduce            | 3.54 us                                                      | 2.86 us: 1.24x faster                                                                |
| tomli_loads                | 2.46 sec                                                     | 2.04 sec: 1.21x faster                                                               |
| spectral_norm              | 97.0 ms                                                      | 81.3 ms: 1.19x faster                                                                |
| generators                 | 33.6 ms                                                      | 28.2 ms: 1.19x faster                                                                |
| regex_effbot               | 3.67 ms                                                      | 3.13 ms: 1.17x faster                                                                |
| float                      | 81.3 ms                                                      | 69.5 ms: 1.17x faster                                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 520 ms: 1.16x faster                                                                 |
| richards                   | 52.9 ms                                                      | 46.1 ms: 1.15x faster                                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                                 |
| genshi_text                | 26.2 ms                                                      | 23.0 ms: 1.14x faster                                                                |
| pyflate                    | 503 ms                                                       | 442 ms: 1.14x faster                                                                 |
| richards_super             | 59.6 ms                                                      | 52.4 ms: 1.14x faster                                                                |
| bpe_tokeniser              | 5.09 sec                                                     | 4.51 sec: 1.13x faster                                                               |
| html5lib                   | 73.5 ms                                                      | 65.7 ms: 1.12x faster                                                                |
| async_generators           | 457 ms                                                       | 411 ms: 1.11x faster                                                                 |
| pylint                     | 347 ms                                                       | 313 ms: 1.11x faster                                                                 |
| pprint_safe_repr           | 843 ms                                                       | 762 ms: 1.11x faster                                                                 |
| pathlib                    | 17.5 ms                                                      | 15.9 ms: 1.10x faster                                                                |
| pprint_pformat             | 1.72 sec                                                     | 1.56 sec: 1.10x faster                                                               |
| genshi_xml                 | 57.1 ms                                                      | 51.8 ms: 1.10x faster                                                                |
| hexiom                     | 6.55 ms                                                      | 5.98 ms: 1.10x faster                                                                |
| telco                      | 8.79 ms                                                      | 8.07 ms: 1.09x faster                                                                |
| scimark_sor                | 123 ms                                                       | 113 ms: 1.09x faster                                                                 |
| xml_etree_parse            | 150 ms                                                       | 138 ms: 1.09x faster                                                                 |
| regex_dna                  | 247 ms                                                       | 230 ms: 1.07x faster                                                                 |
| regex_compile              | 143 ms                                                       | 133 ms: 1.07x faster                                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 96.3 ms: 1.07x faster                                                                |
| scimark_fft                | 328 ms                                                       | 309 ms: 1.06x faster                                                                 |
| unpickle_pure_python       | 217 us                                                       | 205 us: 1.06x faster                                                                 |
| thrift                     | 901 us                                                       | 853 us: 1.06x faster                                                                 |
| deltablue                  | 3.42 ms                                                      | 3.24 ms: 1.05x faster                                                                |
| sqlglot_parse              | 1.40 ms                                                      | 1.33 ms: 1.05x faster                                                                |
| 2to3                       | 293 ms                                                       | 279 ms: 1.05x faster                                                                 |
| sqlalchemy_declarative     | 148 ms                                                       | 141 ms: 1.05x faster                                                                 |
| nqueens                    | 90.7 ms                                                      | 86.6 ms: 1.05x faster                                                                |
| connected_components       | 432 ms                                                       | 414 ms: 1.05x faster                                                                 |
| sympy_expand               | 509 ms                                                       | 488 ms: 1.04x faster                                                                 |
| json                       | 5.69 ms                                                      | 5.45 ms: 1.04x faster                                                                |
| sqlglot_transpile          | 1.79 ms                                                      | 1.71 ms: 1.04x faster                                                                |
| sqlglot_optimize           | 59.3 ms                                                      | 56.8 ms: 1.04x faster                                                                |
| k_core                     | 2.17 sec                                                     | 2.08 sec: 1.04x faster                                                               |
| meteor_contest             | 130 ms                                                       | 124 ms: 1.04x faster                                                                 |
| sympy_str                  | 298 ms                                                       | 286 ms: 1.04x faster                                                                 |
| shortest_path              | 460 ms                                                       | 442 ms: 1.04x faster                                                                 |
| coroutines                 | 21.6 ms                                                      | 20.8 ms: 1.04x faster                                                                |
| sqlglot_normalize          | 119 ms                                                       | 115 ms: 1.04x faster                                                                 |
| regex_v8                   | 26.1 ms                                                      | 25.2 ms: 1.04x faster                                                                |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.6 ms: 1.04x faster                                                                |
| scimark_lu                 | 98.7 ms                                                      | 95.3 ms: 1.04x faster                                                                |
| django_template            | 36.4 ms                                                      | 35.1 ms: 1.03x faster                                                                |
| mdp                        | 2.54 sec                                                     | 2.46 sec: 1.03x faster                                                               |
| raytrace                   | 273 ms                                                       | 264 ms: 1.03x faster                                                                 |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                               |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                                |
| logging_simple             | 6.39 us                                                      | 6.21 us: 1.03x faster                                                                |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.03x faster                                                                 |
| scimark_monte_carlo        | 66.1 ms                                                      | 64.5 ms: 1.03x faster                                                                |
| sympy_integrate            | 23.6 ms                                                      | 23.0 ms: 1.02x faster                                                                |
| xml_etree_process          | 61.2 ms                                                      | 59.8 ms: 1.02x faster                                                                |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.67 ms: 1.02x faster                                                                |
| typing_runtime_protocols   | 169 us                                                       | 165 us: 1.02x faster                                                                 |
| xml_etree_generate         | 86.5 ms                                                      | 84.7 ms: 1.02x faster                                                                |
| comprehensions             | 17.0 us                                                      | 16.7 us: 1.02x faster                                                                |
| dulwich_log                | 68.2 ms                                                      | 66.9 ms: 1.02x faster                                                                |
| logging_format             | 6.94 us                                                      | 6.82 us: 1.02x faster                                                                |
| coverage                   | 80.0 ms                                                      | 78.6 ms: 1.02x faster                                                                |
| logging_silent             | 97.9 ns                                                      | 96.4 ns: 1.01x faster                                                                |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                                 |
| crypto_pyaes               | 73.3 ms                                                      | 72.7 ms: 1.01x faster                                                                |
| chaos                      | 60.2 ms                                                      | 59.8 ms: 1.01x faster                                                                |
| fannkuch                   | 363 ms                                                       | 362 ms: 1.00x faster                                                                 |
| docutils                   | 2.83 sec                                                     | 2.84 sec: 1.00x slower                                                               |
| python_startup_no_site     | 8.96 ms                                                      | 9.00 ms: 1.00x slower                                                                |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                                 |
| python_startup             | 15.9 ms                                                      | 16.1 ms: 1.01x slower                                                                |
| create_gc_cycles           | 2.68 ms                                                      | 2.76 ms: 1.03x slower                                                                |
| json_dumps                 | 11.1 ms                                                      | 11.6 ms: 1.04x slower                                                                |
| mako                       | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                                |
| json_loads                 | 24.7 us                                                      | 26.5 us: 1.07x slower                                                                |
| many_optionals             | 930 us                                                       | 1.01 ms: 1.08x slower                                                                |
| subparsers                 | 17.5 ms                                                      | 22.4 ms: 1.28x slower                                                                |
| gc_traversal               | 4.74 ms                                                      | 6.35 ms: 1.34x slower                                                                |
| bench_mp_pool              | 5.12 ms                                                      | 1.04 sec: 203.67x slower                                                             |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                         |

Benchmark hidden because not significant (4): bench_thread_pool, nbody, pickle_pure_python, pycparser
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.069x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.02x