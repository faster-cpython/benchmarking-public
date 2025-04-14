# Results vs. 3.13.0

- fork: faster-cpython
- ref: single_point_of_allo
- machine: linux-x86_64
- commit hash: af468a2
- commit date: 2025-03-13
- overall geometric mean: 1.012x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 271 ms: 1.02x slower                                                             |
| docutils       | 2.58 sec                                               | 2.71 sec: 1.05x slower                                                           |
| sphinx         | 1.03 sec                                               | 1.07 sec: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                     |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 330 ms: 1.40x faster                                                             |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                             |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                             |
| async_tree_io_tg           | 861 ms                                                 | 657 ms: 1.31x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 336 ms: 1.30x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                             |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                            |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                                             |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 75.7 ms: 1.04x faster                                                            |
| pidigits       | 186 ms                                                 | 191 ms: 1.02x slower                                                             |
| nbody          | 87.7 ms                                                | 124 ms: 1.42x slower                                                             |
| Geometric mean | (ref)                                                  | 1.12x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 24.3 ms: 1.11x faster                                                            |
| regex_effbot   | 3.77 ms                                                | 3.53 ms: 1.07x faster                                                            |
| regex_compile  | 132 ms                                                 | 134 ms: 1.01x slower                                                             |
| regex_dna      | 220 ms                                                 | 227 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.08x faster                                                             |
| xml_etree_generate   | 86.8 ms                                                | 87.5 ms: 1.01x slower                                                            |
| tomli_loads          | 2.12 sec                                               | 2.13 sec: 1.01x slower                                                           |
| xml_etree_iterparse  | 101 ms                                                 | 103 ms: 1.02x slower                                                             |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                             |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.08x slower                                                             |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                            |
| json_loads           | 27.2 us                                                | 32.6 us: 1.20x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.04x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.3 ms: 1.05x slower                                                            |
| python_startup_no_site | 7.00 ms                                                | 8.30 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 23.0 ms: 1.02x slower                                                            |
| mako            | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                            |
| genshi_xml      | 50.5 ms                                                | 52.5 ms: 1.04x slower                                                            |
| django_template | 31.7 ms                                                | 33.6 ms: 1.06x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 330 ms: 1.40x faster                                                             |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                             |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                             |
| async_tree_io_tg           | 861 ms                                                 | 657 ms: 1.31x faster                                                             |
| deepcopy                   | 354 us                                                 | 272 us: 1.30x faster                                                             |
| deepcopy_memo              | 38.4 us                                                | 29.5 us: 1.30x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 336 ms: 1.30x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                             |
| go                         | 141 ms                                                 | 117 ms: 1.21x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 488 ms: 1.11x faster                                                             |
| deepcopy_reduce            | 3.24 us                                                | 2.91 us: 1.11x faster                                                            |
| regex_v8                   | 26.9 ms                                                | 24.3 ms: 1.11x faster                                                            |
| richards                   | 47.5 ms                                                | 43.8 ms: 1.09x faster                                                            |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.08x faster                                                             |
| pylint                     | 312 ms                                                 | 289 ms: 1.08x faster                                                             |
| richards_super             | 53.7 ms                                                | 50.3 ms: 1.07x faster                                                            |
| regex_effbot               | 3.77 ms                                                | 3.53 ms: 1.07x faster                                                            |
| dulwich_log                | 64.6 ms                                                | 61.4 ms: 1.05x faster                                                            |
| float                      | 78.7 ms                                                | 75.7 ms: 1.04x faster                                                            |
| telco                      | 8.40 ms                                                | 8.13 ms: 1.03x faster                                                            |
| generators                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                            |
| gc_traversal               | 4.90 ms                                                | 4.75 ms: 1.03x faster                                                            |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.02x faster                                                           |
| deltablue                  | 3.19 ms                                                | 3.21 ms: 1.01x slower                                                            |
| xml_etree_generate         | 86.8 ms                                                | 87.5 ms: 1.01x slower                                                            |
| tomli_loads                | 2.12 sec                                               | 2.13 sec: 1.01x slower                                                           |
| crypto_pyaes               | 74.7 ms                                                | 75.3 ms: 1.01x slower                                                            |
| sqlite_synth               | 2.90 us                                                | 2.93 us: 1.01x slower                                                            |
| regex_compile              | 132 ms                                                 | 134 ms: 1.01x slower                                                             |
| mdp                        | 2.54 sec                                               | 2.57 sec: 1.01x slower                                                           |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                            |
| pathlib                    | 17.4 ms                                                | 17.6 ms: 1.01x slower                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 103 ms: 1.02x slower                                                             |
| pycparser                  | 1.20 sec                                               | 1.22 sec: 1.02x slower                                                           |
| genshi_text                | 22.6 ms                                                | 23.0 ms: 1.02x slower                                                            |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                             |
| hexiom                     | 6.08 ms                                                | 6.19 ms: 1.02x slower                                                            |
| pyflate                    | 470 ms                                                 | 479 ms: 1.02x slower                                                             |
| logging_simple             | 5.65 us                                                | 5.76 us: 1.02x slower                                                            |
| 2to3                       | 266 ms                                                 | 271 ms: 1.02x slower                                                             |
| sqlalchemy_declarative     | 133 ms                                                 | 136 ms: 1.02x slower                                                             |
| pidigits                   | 186 ms                                                 | 191 ms: 1.02x slower                                                             |
| coverage                   | 82.8 ms                                                | 85.4 ms: 1.03x slower                                                            |
| shortest_path              | 487 ms                                                 | 502 ms: 1.03x slower                                                             |
| regex_dna                  | 220 ms                                                 | 227 ms: 1.03x slower                                                             |
| thrift                     | 800 us                                                 | 828 us: 1.04x slower                                                             |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                            |
| sympy_integrate            | 19.8 ms                                                | 20.6 ms: 1.04x slower                                                            |
| sphinx                     | 1.03 sec                                               | 1.07 sec: 1.04x slower                                                           |
| genshi_xml                 | 50.5 ms                                                | 52.5 ms: 1.04x slower                                                            |
| sympy_sum                  | 150 ms                                                 | 157 ms: 1.04x slower                                                             |
| pprint_safe_repr           | 727 ms                                                 | 757 ms: 1.04x slower                                                             |
| logging_format             | 6.23 us                                                | 6.51 us: 1.04x slower                                                            |
| connected_components       | 447 ms                                                 | 467 ms: 1.04x slower                                                             |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                            |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                                             |
| docutils                   | 2.58 sec                                               | 2.71 sec: 1.05x slower                                                           |
| python_startup             | 12.7 ms                                                | 13.3 ms: 1.05x slower                                                            |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.9 ms: 1.06x slower                                                            |
| pprint_pformat             | 1.48 sec                                               | 1.57 sec: 1.06x slower                                                           |
| django_template            | 31.7 ms                                                | 33.6 ms: 1.06x slower                                                            |
| comprehensions             | 16.5 us                                                | 17.5 us: 1.06x slower                                                            |
| logging_silent             | 101 ns                                                 | 108 ns: 1.07x slower                                                             |
| sympy_str                  | 273 ms                                                 | 293 ms: 1.07x slower                                                             |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.08x slower                                                             |
| json                       | 5.32 ms                                                | 5.77 ms: 1.08x slower                                                            |
| sympy_expand               | 456 ms                                                 | 501 ms: 1.10x slower                                                             |
| bench_thread_pool          | 818 us                                                 | 906 us: 1.11x slower                                                             |
| nqueens                    | 80.9 ms                                                | 89.7 ms: 1.11x slower                                                            |
| scimark_sor                | 122 ms                                                 | 136 ms: 1.11x slower                                                             |
| scimark_lu                 | 114 ms                                                 | 128 ms: 1.12x slower                                                             |
| spectral_norm              | 113 ms                                                 | 127 ms: 1.12x slower                                                             |
| bpe_tokeniser              | 4.69 sec                                               | 5.26 sec: 1.12x slower                                                           |
| chaos                      | 58.0 ms                                                | 65.3 ms: 1.12x slower                                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 76.0 ms: 1.14x slower                                                            |
| raytrace                   | 262 ms                                                 | 298 ms: 1.14x slower                                                             |
| typing_runtime_protocols   | 160 us                                                 | 183 us: 1.15x slower                                                             |
| scimark_fft                | 367 ms                                                 | 423 ms: 1.15x slower                                                             |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                            |
| many_optionals             | 857 us                                                 | 1.00 ms: 1.17x slower                                                            |
| python_startup_no_site     | 7.00 ms                                                | 8.30 ms: 1.19x slower                                                            |
| fannkuch                   | 394 ms                                                 | 467 ms: 1.19x slower                                                             |
| json_loads                 | 27.2 us                                                | 32.6 us: 1.20x slower                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.40 ms: 1.27x slower                                                            |
| subparsers                 | 15.5 ms                                                | 21.7 ms: 1.41x slower                                                            |
| nbody                      | 87.7 ms                                                | 124 ms: 1.42x slower                                                             |
| bench_mp_pool              | 24.0 ms                                                | 84.9 ms: 3.54x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                                     |

Benchmark hidden because not significant (4): html5lib, meteor_contest, xml_etree_process, asyncio_websockets
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250313-3.14.0a5+-af468a2/bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.012x slower

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x