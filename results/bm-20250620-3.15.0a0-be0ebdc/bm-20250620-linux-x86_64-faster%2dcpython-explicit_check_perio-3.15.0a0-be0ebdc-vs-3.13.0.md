# Results vs. 3.13.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-x86_64
- commit hash: be0ebdc
- commit date: 2025-06-20
- overall geometric mean: 1.028x faster
- HPT reliability: 95.64%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                                            |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                          |
| html5lib       | 63.4 ms                                                | 62.1 ms: 1.02x faster                                                           |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                            |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 637 ms: 1.35x faster                                                            |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 510 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 500 ms: 1.09x faster                                                            |
| async_generators           | 433 ms                                                 | 418 ms: 1.04x faster                                                            |
| coroutines                 | 22.2 ms                                                | 24.7 ms: 1.11x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 74.3 ms: 1.06x faster                                                           |
| pidigits       | 186 ms                                                 | 193 ms: 1.04x slower                                                            |
| nbody          | 87.7 ms                                                | 100 ms: 1.14x slower                                                            |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                           |
| regex_effbot   | 3.77 ms                                                | 3.33 ms: 1.13x faster                                                           |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                            |
| regex_compile  | 132 ms                                                 | 130 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                                            |
| tomli_loads          | 2.12 sec                                               | 2.01 sec: 1.05x faster                                                          |
| xml_etree_iterparse  | 101 ms                                                 | 99.1 ms: 1.02x faster                                                           |
| xml_etree_generate   | 86.8 ms                                                | 86.2 ms: 1.01x faster                                                           |
| unpickle_pure_python | 213 us                                                 | 225 us: 1.06x slower                                                            |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                                           |
| pickle_pure_python   | 302 us                                                 | 327 us: 1.08x slower                                                            |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.03x faster                                                           |
| python_startup_no_site | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.1 ms: 1.02x faster                                                           |
| genshi_xml      | 50.5 ms                                                | 51.2 ms: 1.02x slower                                                           |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                           |
| mako            | 10.7 ms                                                | 11.8 ms: 1.11x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                                          |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                            |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                            |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                                            |
| async_tree_io_tg           | 861 ms                                                 | 637 ms: 1.35x faster                                                            |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                            |
| deepcopy_memo              | 38.4 us                                                | 30.5 us: 1.26x faster                                                           |
| go                         | 141 ms                                                 | 114 ms: 1.23x faster                                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.75 us: 1.18x faster                                                           |
| regex_v8                   | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                           |
| regex_effbot               | 3.77 ms                                                | 3.33 ms: 1.13x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 510 ms: 1.12x faster                                                            |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                                            |
| spectral_norm              | 113 ms                                                 | 102 ms: 1.11x faster                                                            |
| pyflate                    | 470 ms                                                 | 431 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 500 ms: 1.09x faster                                                            |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                                            |
| dulwich_log                | 64.6 ms                                                | 59.5 ms: 1.09x faster                                                           |
| richards                   | 47.5 ms                                                | 44.6 ms: 1.07x faster                                                           |
| richards_super             | 53.7 ms                                                | 50.7 ms: 1.06x faster                                                           |
| float                      | 78.7 ms                                                | 74.3 ms: 1.06x faster                                                           |
| tomli_loads                | 2.12 sec                                               | 2.01 sec: 1.05x faster                                                          |
| telco                      | 8.40 ms                                                | 8.02 ms: 1.05x faster                                                           |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                                            |
| async_generators           | 433 ms                                                 | 418 ms: 1.04x faster                                                            |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.03x faster                                                           |
| sympy_integrate            | 19.8 ms                                                | 19.2 ms: 1.03x faster                                                           |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.57 sec: 1.03x faster                                                          |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                                            |
| thrift                     | 800 us                                                 | 780 us: 1.03x faster                                                            |
| genshi_text                | 22.6 ms                                                | 22.1 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 101 ms                                                 | 99.1 ms: 1.02x faster                                                           |
| html5lib                   | 63.4 ms                                                | 62.1 ms: 1.02x faster                                                           |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                          |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                                           |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                            |
| comprehensions             | 16.5 us                                                | 16.2 us: 1.02x faster                                                           |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.02x faster                                                            |
| sqlite_synth               | 2.90 us                                                | 2.86 us: 1.02x faster                                                           |
| regex_compile              | 132 ms                                                 | 130 ms: 1.01x faster                                                            |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.01x faster                                                          |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                            |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                            |
| xml_etree_generate         | 86.8 ms                                                | 86.2 ms: 1.01x faster                                                           |
| python_startup_no_site     | 7.00 ms                                                | 6.95 ms: 1.01x faster                                                           |
| scimark_fft                | 367 ms                                                 | 369 ms: 1.01x slower                                                            |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                          |
| nqueens                    | 80.9 ms                                                | 81.9 ms: 1.01x slower                                                           |
| gc_traversal               | 4.90 ms                                                | 4.96 ms: 1.01x slower                                                           |
| genshi_xml                 | 50.5 ms                                                | 51.2 ms: 1.02x slower                                                           |
| scimark_monte_carlo        | 66.8 ms                                                | 68.2 ms: 1.02x slower                                                           |
| crypto_pyaes               | 74.7 ms                                                | 76.4 ms: 1.02x slower                                                           |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                           |
| pidigits                   | 186 ms                                                 | 193 ms: 1.04x slower                                                            |
| generators                 | 28.8 ms                                                | 29.9 ms: 1.04x slower                                                           |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                            |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                            |
| hexiom                     | 6.08 ms                                                | 6.37 ms: 1.05x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 225 us: 1.06x slower                                                            |
| raytrace                   | 262 ms                                                 | 276 ms: 1.06x slower                                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                           |
| fannkuch                   | 394 ms                                                 | 417 ms: 1.06x slower                                                            |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                                           |
| coverage                   | 82.8 ms                                                | 87.7 ms: 1.06x slower                                                           |
| chaos                      | 58.0 ms                                                | 61.5 ms: 1.06x slower                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.37 ms: 1.07x slower                                                           |
| shortest_path              | 487 ms                                                 | 524 ms: 1.08x slower                                                            |
| connected_components       | 447 ms                                                 | 482 ms: 1.08x slower                                                            |
| pickle_pure_python         | 302 us                                                 | 327 us: 1.08x slower                                                            |
| mako                       | 10.7 ms                                                | 11.8 ms: 1.11x slower                                                           |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                           |
| coroutines                 | 22.2 ms                                                | 24.7 ms: 1.11x slower                                                           |
| deltablue                  | 3.19 ms                                                | 3.57 ms: 1.12x slower                                                           |
| logging_simple             | 5.65 us                                                | 6.33 us: 1.12x slower                                                           |
| pprint_pformat             | 1.48 sec                                               | 1.66 sec: 1.12x slower                                                          |
| pprint_safe_repr           | 727 ms                                                 | 815 ms: 1.12x slower                                                            |
| logging_format             | 6.23 us                                                | 7.02 us: 1.13x slower                                                           |
| many_optionals             | 857 us                                                 | 968 us: 1.13x slower                                                            |
| nbody                      | 87.7 ms                                                | 100 ms: 1.14x slower                                                            |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.53x slower                                                           |
| logging_silent             | 101 ns                                                 | 481 ns: 4.76x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (5): xml_etree_process, asyncio_websockets, sympy_expand, json, djangocms
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250620-3.15.0a0-be0ebdc/bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.028x faster

# HPT report

- Reliability score: 95.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x