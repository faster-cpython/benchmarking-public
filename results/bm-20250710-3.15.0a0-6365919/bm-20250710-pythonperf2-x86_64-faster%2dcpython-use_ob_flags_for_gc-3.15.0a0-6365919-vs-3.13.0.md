# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_ob_flags_for_gc
- machine: linux-x86_64
- commit hash: 6365919
- commit date: 2025-07-10
- overall geometric mean: 1.047x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                                 |
| docutils       | 2.83 sec                                                     | 2.87 sec: 1.01x slower                                                               |
| html5lib       | 73.5 ms                                                      | 65.9 ms: 1.11x faster                                                                |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                               |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 330 ms: 1.41x faster                                                                 |
| async_tree_none            | 376 ms                                                       | 269 ms: 1.40x faster                                                                 |
| async_tree_memoization     | 453 ms                                                       | 325 ms: 1.39x faster                                                                 |
| async_tree_io              | 843 ms                                                       | 614 ms: 1.37x faster                                                                 |
| async_tree_io_tg           | 831 ms                                                       | 627 ms: 1.33x faster                                                                 |
| async_tree_none_tg         | 346 ms                                                       | 271 ms: 1.28x faster                                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 496 ms: 1.22x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                                 |
| async_generators           | 457 ms                                                       | 435 ms: 1.05x faster                                                                 |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                                 |
| coroutines                 | 21.6 ms                                                      | 22.9 ms: 1.06x slower                                                                |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.4 ms: 1.16x faster                                                                |
| pidigits       | 252 ms                                                       | 256 ms: 1.01x slower                                                                 |
| nbody          | 89.3 ms                                                      | 94.7 ms: 1.06x slower                                                                |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 225 ms: 1.10x faster                                                                 |
| regex_compile  | 143 ms                                                       | 131 ms: 1.09x faster                                                                 |
| regex_v8       | 26.1 ms                                                      | 24.1 ms: 1.09x faster                                                                |
| regex_effbot   | 3.67 ms                                                      | 3.50 ms: 1.05x faster                                                                |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.02 sec: 1.22x faster                                                               |
| xml_etree_parse      | 150 ms                                                       | 138 ms: 1.09x faster                                                                 |
| xml_etree_process    | 61.2 ms                                                      | 58.2 ms: 1.05x faster                                                                |
| xml_etree_iterparse  | 103 ms                                                       | 98.1 ms: 1.05x faster                                                                |
| unpickle_pure_python | 217 us                                                       | 208 us: 1.05x faster                                                                 |
| xml_etree_generate   | 86.5 ms                                                      | 84.4 ms: 1.03x faster                                                                |
| json_dumps           | 11.1 ms                                                      | 11.2 ms: 1.01x slower                                                                |
| json_loads           | 24.7 us                                                      | 25.0 us: 1.01x slower                                                                |
| pickle_pure_python   | 323 us                                                       | 328 us: 1.01x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.05x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.2 ms: 1.04x faster                                                                |
| python_startup_no_site | 8.96 ms                                                      | 8.77 ms: 1.02x faster                                                                |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.0 ms: 1.14x faster                                                                |
| genshi_xml      | 57.1 ms                                                      | 52.9 ms: 1.08x faster                                                                |
| django_template | 36.4 ms                                                      | 35.2 ms: 1.03x faster                                                                |
| mako            | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                                                |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.28 sec: 1.98x faster                                                               |
| deepcopy                   | 392 us                                                       | 268 us: 1.46x faster                                                                 |
| deepcopy_memo              | 38.6 us                                                      | 27.1 us: 1.42x faster                                                                |
| async_tree_memoization_tg  | 466 ms                                                       | 330 ms: 1.41x faster                                                                 |
| async_tree_none            | 376 ms                                                       | 269 ms: 1.40x faster                                                                 |
| async_tree_memoization     | 453 ms                                                       | 325 ms: 1.39x faster                                                                 |
| async_tree_io              | 843 ms                                                       | 614 ms: 1.37x faster                                                                 |
| go                         | 162 ms                                                       | 118 ms: 1.37x faster                                                                 |
| async_tree_io_tg           | 831 ms                                                       | 627 ms: 1.33x faster                                                                 |
| async_tree_none_tg         | 346 ms                                                       | 271 ms: 1.28x faster                                                                 |
| pyflate                    | 503 ms                                                       | 409 ms: 1.23x faster                                                                 |
| tomli_loads                | 2.46 sec                                                     | 2.02 sec: 1.22x faster                                                               |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 496 ms: 1.22x faster                                                                 |
| deepcopy_reduce            | 3.54 us                                                      | 2.93 us: 1.21x faster                                                                |
| scimark_sor                | 123 ms                                                       | 103 ms: 1.20x faster                                                                 |
| richards                   | 52.9 ms                                                      | 45.1 ms: 1.17x faster                                                                |
| richards_super             | 59.6 ms                                                      | 51.1 ms: 1.16x faster                                                                |
| float                      | 81.3 ms                                                      | 70.4 ms: 1.16x faster                                                                |
| dulwich_log                | 68.2 ms                                                      | 59.2 ms: 1.15x faster                                                                |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                                 |
| genshi_text                | 26.2 ms                                                      | 23.0 ms: 1.14x faster                                                                |
| spectral_norm              | 97.0 ms                                                      | 85.2 ms: 1.14x faster                                                                |
| pprint_pformat             | 1.72 sec                                                     | 1.53 sec: 1.13x faster                                                               |
| pprint_safe_repr           | 843 ms                                                       | 748 ms: 1.13x faster                                                                 |
| generators                 | 33.6 ms                                                      | 30.0 ms: 1.12x faster                                                                |
| hexiom                     | 6.55 ms                                                      | 5.87 ms: 1.12x faster                                                                |
| html5lib                   | 73.5 ms                                                      | 65.9 ms: 1.11x faster                                                                |
| scimark_monte_carlo        | 66.1 ms                                                      | 60.2 ms: 1.10x faster                                                                |
| regex_dna                  | 247 ms                                                       | 225 ms: 1.10x faster                                                                 |
| regex_compile              | 143 ms                                                       | 131 ms: 1.09x faster                                                                 |
| xml_etree_parse            | 150 ms                                                       | 138 ms: 1.09x faster                                                                 |
| bpe_tokeniser              | 5.09 sec                                                     | 4.69 sec: 1.09x faster                                                               |
| regex_v8                   | 26.1 ms                                                      | 24.1 ms: 1.09x faster                                                                |
| meteor_contest             | 130 ms                                                       | 120 ms: 1.08x faster                                                                 |
| deltablue                  | 3.42 ms                                                      | 3.15 ms: 1.08x faster                                                                |
| json                       | 5.69 ms                                                      | 5.26 ms: 1.08x faster                                                                |
| genshi_xml                 | 57.1 ms                                                      | 52.9 ms: 1.08x faster                                                                |
| pylint                     | 347 ms                                                       | 322 ms: 1.08x faster                                                                 |
| sympy_integrate            | 23.6 ms                                                      | 22.0 ms: 1.07x faster                                                                |
| scimark_fft                | 328 ms                                                       | 307 ms: 1.07x faster                                                                 |
| logging_simple             | 6.39 us                                                      | 6.03 us: 1.06x faster                                                                |
| logging_silent             | 97.9 ns                                                      | 93.1 ns: 1.05x faster                                                                |
| thrift                     | 901 us                                                       | 857 us: 1.05x faster                                                                 |
| xml_etree_process          | 61.2 ms                                                      | 58.2 ms: 1.05x faster                                                                |
| async_generators           | 457 ms                                                       | 435 ms: 1.05x faster                                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 98.1 ms: 1.05x faster                                                                |
| regex_effbot               | 3.67 ms                                                      | 3.50 ms: 1.05x faster                                                                |
| logging_format             | 6.94 us                                                      | 6.63 us: 1.05x faster                                                                |
| sympy_expand               | 509 ms                                                       | 487 ms: 1.05x faster                                                                 |
| unpickle_pure_python       | 217 us                                                       | 208 us: 1.05x faster                                                                 |
| python_startup             | 15.9 ms                                                      | 15.2 ms: 1.04x faster                                                                |
| k_core                     | 2.17 sec                                                     | 2.08 sec: 1.04x faster                                                               |
| sympy_str                  | 298 ms                                                       | 286 ms: 1.04x faster                                                                 |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                                 |
| pathlib                    | 17.5 ms                                                      | 16.9 ms: 1.04x faster                                                                |
| scimark_lu                 | 98.7 ms                                                      | 95.3 ms: 1.04x faster                                                                |
| chaos                      | 60.2 ms                                                      | 58.2 ms: 1.03x faster                                                                |
| django_template            | 36.4 ms                                                      | 35.2 ms: 1.03x faster                                                                |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                               |
| comprehensions             | 17.0 us                                                      | 16.5 us: 1.03x faster                                                                |
| sympy_sum                  | 155 ms                                                       | 150 ms: 1.03x faster                                                                 |
| xml_etree_generate         | 86.5 ms                                                      | 84.4 ms: 1.03x faster                                                                |
| python_startup_no_site     | 8.96 ms                                                      | 8.77 ms: 1.02x faster                                                                |
| connected_components       | 432 ms                                                       | 423 ms: 1.02x faster                                                                 |
| sqlite_synth               | 2.91 us                                                      | 2.85 us: 1.02x faster                                                                |
| typing_runtime_protocols   | 169 us                                                       | 166 us: 1.02x faster                                                                 |
| shortest_path              | 460 ms                                                       | 453 ms: 1.02x faster                                                                 |
| asyncio_websockets         | 388 ms                                                       | 383 ms: 1.01x faster                                                                 |
| coverage                   | 80.0 ms                                                      | 80.3 ms: 1.00x slower                                                                |
| json_dumps                 | 11.1 ms                                                      | 11.2 ms: 1.01x slower                                                                |
| json_loads                 | 24.7 us                                                      | 25.0 us: 1.01x slower                                                                |
| pidigits                   | 252 ms                                                       | 256 ms: 1.01x slower                                                                 |
| docutils                   | 2.83 sec                                                     | 2.87 sec: 1.01x slower                                                               |
| pickle_pure_python         | 323 us                                                       | 328 us: 1.01x slower                                                                 |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.87 ms: 1.02x slower                                                                |
| crypto_pyaes               | 73.3 ms                                                      | 74.9 ms: 1.02x slower                                                                |
| fannkuch                   | 363 ms                                                       | 371 ms: 1.02x slower                                                                 |
| nqueens                    | 90.7 ms                                                      | 92.8 ms: 1.02x slower                                                                |
| mako                       | 10.4 ms                                                      | 10.7 ms: 1.03x slower                                                                |
| create_gc_cycles           | 2.68 ms                                                      | 2.77 ms: 1.03x slower                                                                |
| raytrace                   | 273 ms                                                       | 282 ms: 1.03x slower                                                                 |
| nbody                      | 89.3 ms                                                      | 94.7 ms: 1.06x slower                                                                |
| coroutines                 | 21.6 ms                                                      | 22.9 ms: 1.06x slower                                                                |
| many_optionals             | 930 us                                                       | 1.04 ms: 1.11x slower                                                                |
| gc_traversal               | 4.74 ms                                                      | 5.88 ms: 1.24x slower                                                                |
| subparsers                 | 17.5 ms                                                      | 25.3 ms: 1.45x slower                                                                |
| telco                      | 8.79 ms                                                      | 158 ms: 17.95x slower                                                                |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                         |

Benchmark hidden because not significant (2): djangocms, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250710-3.15.0a0-6365919/bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.10x