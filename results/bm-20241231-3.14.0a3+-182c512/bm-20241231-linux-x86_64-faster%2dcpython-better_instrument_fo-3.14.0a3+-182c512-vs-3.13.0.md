# Results vs. 3.13.0

- fork: faster-cpython
- ref: better_instrument_fo
- machine: linux-x86_64
- commit hash: 182c512
- commit date: 2024-12-31
- overall geometric mean: 1.042x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                             |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                           |
| html5lib       | 63.4 ms                                                | 62.5 ms: 1.01x faster                                                            |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 302 ms: 1.53x faster                                                             |
| async_tree_io_tg           | 861 ms                                                 | 594 ms: 1.45x faster                                                             |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 329 ms: 1.33x faster                                                             |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.32x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 244 ms: 1.31x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 482 ms: 1.19x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 466 ms: 1.17x faster                                                             |
| async_generators           | 433 ms                                                 | 421 ms: 1.03x faster                                                             |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.04x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 73.2 ms: 1.07x faster                                                            |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                             |
| nbody          | 87.7 ms                                                | 95.9 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.28 ms: 1.15x faster                                                            |
| regex_v8       | 26.9 ms                                                | 25.4 ms: 1.06x faster                                                            |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.13x faster                                                             |
| tomli_loads          | 2.12 sec                                               | 2.01 sec: 1.06x faster                                                           |
| xml_etree_iterparse  | 101 ms                                                 | 97.0 ms: 1.04x faster                                                            |
| xml_etree_generate   | 86.8 ms                                                | 84.1 ms: 1.03x faster                                                            |
| xml_etree_process    | 60.5 ms                                                | 58.7 ms: 1.03x faster                                                            |
| json_loads           | 27.2 us                                                | 26.5 us: 1.03x faster                                                            |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                             |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                             |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.12x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                            |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                            |
| genshi_text     | 22.6 ms                                                | 22.4 ms: 1.01x faster                                                            |
| django_template | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                            |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 302 ms: 1.53x faster                                                             |
| async_tree_io_tg           | 861 ms                                                 | 594 ms: 1.45x faster                                                             |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                                             |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 329 ms: 1.33x faster                                                             |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.32x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 244 ms: 1.31x faster                                                             |
| deepcopy_memo              | 38.4 us                                                | 30.7 us: 1.25x faster                                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.65 us: 1.22x faster                                                            |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 482 ms: 1.19x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 466 ms: 1.17x faster                                                             |
| regex_effbot               | 3.77 ms                                                | 3.28 ms: 1.15x faster                                                            |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.13x faster                                                             |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                             |
| richards                   | 47.5 ms                                                | 43.6 ms: 1.09x faster                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.64 ms: 1.08x faster                                                            |
| telco                      | 8.40 ms                                                | 7.74 ms: 1.08x faster                                                            |
| pathlib                    | 17.4 ms                                                | 16.1 ms: 1.08x faster                                                            |
| json                       | 5.32 ms                                                | 4.94 ms: 1.08x faster                                                            |
| spectral_norm              | 113 ms                                                 | 105 ms: 1.08x faster                                                             |
| float                      | 78.7 ms                                                | 73.2 ms: 1.07x faster                                                            |
| richards_super             | 53.7 ms                                                | 50.5 ms: 1.06x faster                                                            |
| scimark_fft                | 367 ms                                                 | 346 ms: 1.06x faster                                                             |
| regex_v8                   | 26.9 ms                                                | 25.4 ms: 1.06x faster                                                            |
| tomli_loads                | 2.12 sec                                               | 2.01 sec: 1.06x faster                                                           |
| crypto_pyaes               | 74.7 ms                                                | 71.4 ms: 1.05x faster                                                            |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                           |
| xml_etree_iterparse        | 101 ms                                                 | 97.0 ms: 1.04x faster                                                            |
| thrift                     | 800 us                                                 | 767 us: 1.04x faster                                                             |
| generators                 | 28.8 ms                                                | 27.6 ms: 1.04x faster                                                            |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                             |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                            |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.03x faster                                                             |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                             |
| xml_etree_generate         | 86.8 ms                                                | 84.1 ms: 1.03x faster                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.55 sec: 1.03x faster                                                           |
| xml_etree_process          | 60.5 ms                                                | 58.7 ms: 1.03x faster                                                            |
| djangocms                  | 22.3 us                                                | 21.7 us: 1.03x faster                                                            |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                             |
| async_generators           | 433 ms                                                 | 421 ms: 1.03x faster                                                             |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                           |
| json_loads                 | 27.2 us                                                | 26.5 us: 1.03x faster                                                            |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.5 ms: 1.03x faster                                                            |
| pyflate                    | 470 ms                                                 | 459 ms: 1.02x faster                                                             |
| shortest_path              | 487 ms                                                 | 476 ms: 1.02x faster                                                             |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                                             |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                             |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                           |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.02x faster                                                             |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                                             |
| html5lib                   | 63.4 ms                                                | 62.5 ms: 1.01x faster                                                            |
| genshi_xml                 | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                            |
| sqlglot_optimize           | 53.4 ms                                                | 52.7 ms: 1.01x faster                                                            |
| logging_format             | 6.23 us                                                | 6.16 us: 1.01x faster                                                            |
| genshi_text                | 22.6 ms                                                | 22.4 ms: 1.01x faster                                                            |
| dulwich_log                | 64.6 ms                                                | 64.1 ms: 1.01x faster                                                            |
| logging_simple             | 5.65 us                                                | 5.61 us: 1.01x faster                                                            |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                             |
| nqueens                    | 80.9 ms                                                | 81.3 ms: 1.01x slower                                                            |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.01x slower                                                            |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                           |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.01x slower                                                            |
| coverage                   | 82.8 ms                                                | 83.4 ms: 1.01x slower                                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                            |
| pprint_safe_repr           | 727 ms                                                 | 733 ms: 1.01x slower                                                             |
| django_template            | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                            |
| gc_traversal               | 4.90 ms                                                | 4.95 ms: 1.01x slower                                                            |
| python_startup_no_site     | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                            |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.01x slower                                                             |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                                             |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                            |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 67.7 ms: 1.01x slower                                                            |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                            |
| deltablue                  | 3.19 ms                                                | 3.26 ms: 1.02x slower                                                            |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                             |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                             |
| hexiom                     | 6.08 ms                                                | 6.28 ms: 1.03x slower                                                            |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                             |
| fannkuch                   | 394 ms                                                 | 410 ms: 1.04x slower                                                             |
| chaos                      | 58.0 ms                                                | 60.5 ms: 1.04x slower                                                            |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.04x slower                                                            |
| bench_thread_pool          | 818 us                                                 | 865 us: 1.06x slower                                                             |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                             |
| logging_silent             | 101 ns                                                 | 108 ns: 1.07x slower                                                             |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                            |
| nbody                      | 87.7 ms                                                | 95.9 ms: 1.09x slower                                                            |
| many_optionals             | 857 us                                                 | 951 us: 1.11x slower                                                             |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.12x slower                                                            |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 82.2 ms: 3.43x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (5): sympy_expand, mdp, asyncio_websockets, regex_dna, pprint_pformat
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241231-3.14.0a3+-182c512/bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512.json: mypy2

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x