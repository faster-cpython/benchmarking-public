# Results vs. 3.13.0

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 1e0f842
- commit date: 2025-01-24
- overall geometric mean: 1.102x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 311 ms: 1.17x slower                                                             |
| docutils       | 2.58 sec                                               | 2.84 sec: 1.10x slower                                                           |
| html5lib       | 63.4 ms                                                | 68.8 ms: 1.09x slower                                                            |
| sphinx         | 1.03 sec                                               | 1.13 sec: 1.10x slower                                                           |
| Geometric mean | (ref)                                                  | 1.11x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 556 ms: 1.55x faster                                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 327 ms: 1.42x faster                                                             |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.30x faster                                                             |
| async_tree_none            | 350 ms                                                 | 289 ms: 1.21x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 368 ms: 1.19x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 527 ms: 1.09x faster                                                             |
| async_generators           | 433 ms                                                 | 442 ms: 1.02x slower                                                             |
| coroutines                 | 22.2 ms                                                | 25.9 ms: 1.17x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.17x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 79.9 ms: 1.02x slower                                                            |
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                                             |
| nbody          | 87.7 ms                                                | 147 ms: 1.67x slower                                                             |
| Geometric mean | (ref)                                                  | 1.20x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.28 ms: 1.15x faster                                                            |
| regex_v8       | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                            |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                                             |
| regex_compile  | 132 ms                                                 | 151 ms: 1.14x slower                                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 95.3 ms: 1.06x faster                                                            |
| xml_etree_parse      | 154 ms                                                 | 148 ms: 1.04x faster                                                             |
| xml_etree_generate   | 86.8 ms                                                | 96.2 ms: 1.11x slower                                                            |
| xml_etree_process    | 60.5 ms                                                | 68.7 ms: 1.14x slower                                                            |
| tomli_loads          | 2.12 sec                                               | 2.44 sec: 1.15x slower                                                           |
| json_loads           | 27.2 us                                                | 31.6 us: 1.16x slower                                                            |
| unpickle_pure_python | 213 us                                                 | 258 us: 1.21x slower                                                             |
| pickle_pure_python   | 302 us                                                 | 374 us: 1.24x slower                                                             |
| json_dumps           | 10.1 ms                                                | 12.7 ms: 1.26x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.12x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.1 ms: 1.19x slower                                                            |
| python_startup_no_site | 7.00 ms                                                | 9.38 ms: 1.34x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 61.1 ms: 1.21x slower                                                            |
| genshi_text     | 22.6 ms                                                | 28.7 ms: 1.27x slower                                                            |
| django_template | 31.7 ms                                                | 41.7 ms: 1.32x slower                                                            |
| mako            | 10.7 ms                                                | 16.8 ms: 1.58x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.34x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 556 ms: 1.55x faster                                                             |
| create_gc_cycles           | 2.45 ms                                                | 1.70 ms: 1.44x faster                                                            |
| async_tree_memoization_tg  | 463 ms                                                 | 327 ms: 1.42x faster                                                             |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.30x faster                                                             |
| async_tree_none            | 350 ms                                                 | 289 ms: 1.21x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 368 ms: 1.19x faster                                                             |
| regex_effbot               | 3.77 ms                                                | 3.28 ms: 1.15x faster                                                            |
| deepcopy                   | 354 us                                                 | 313 us: 1.13x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 527 ms: 1.09x faster                                                             |
| regex_v8                   | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                            |
| sqlite_synth               | 2.90 us                                                | 2.71 us: 1.07x faster                                                            |
| gc_traversal               | 4.90 ms                                                | 4.61 ms: 1.06x faster                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 95.3 ms: 1.06x faster                                                            |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.06x faster                                                            |
| xml_etree_parse            | 154 ms                                                 | 148 ms: 1.04x faster                                                             |
| regex_dna                  | 220 ms                                                 | 218 ms: 1.01x faster                                                             |
| pycparser                  | 1.20 sec                                               | 1.19 sec: 1.01x faster                                                           |
| float                      | 78.7 ms                                                | 79.9 ms: 1.02x slower                                                            |
| async_generators           | 433 ms                                                 | 442 ms: 1.02x slower                                                             |
| deepcopy_reduce            | 3.24 us                                                | 3.31 us: 1.02x slower                                                            |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                                             |
| go                         | 141 ms                                                 | 144 ms: 1.03x slower                                                             |
| spectral_norm              | 113 ms                                                 | 117 ms: 1.04x slower                                                             |
| k_core                     | 2.37 sec                                               | 2.46 sec: 1.04x slower                                                           |
| deepcopy_memo              | 38.4 us                                                | 39.8 us: 1.04x slower                                                            |
| json                       | 5.32 ms                                                | 5.56 ms: 1.04x slower                                                            |
| dulwich_log                | 64.6 ms                                                | 69.7 ms: 1.08x slower                                                            |
| mdp                        | 2.54 sec                                               | 2.76 sec: 1.09x slower                                                           |
| html5lib                   | 63.4 ms                                                | 68.8 ms: 1.09x slower                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 5.10 sec: 1.09x slower                                                           |
| sphinx                     | 1.03 sec                                               | 1.13 sec: 1.10x slower                                                           |
| docutils                   | 2.58 sec                                               | 2.84 sec: 1.10x slower                                                           |
| telco                      | 8.40 ms                                                | 9.28 ms: 1.10x slower                                                            |
| generators                 | 28.8 ms                                                | 31.8 ms: 1.11x slower                                                            |
| xml_etree_generate         | 86.8 ms                                                | 96.2 ms: 1.11x slower                                                            |
| sqlglot_normalize          | 108 ms                                                 | 122 ms: 1.13x slower                                                             |
| xml_etree_process          | 60.5 ms                                                | 68.7 ms: 1.14x slower                                                            |
| regex_compile              | 132 ms                                                 | 151 ms: 1.14x slower                                                             |
| sqlglot_optimize           | 53.4 ms                                                | 61.1 ms: 1.14x slower                                                            |
| richards                   | 47.5 ms                                                | 54.6 ms: 1.15x slower                                                            |
| tomli_loads                | 2.12 sec                                               | 2.44 sec: 1.15x slower                                                           |
| pyflate                    | 470 ms                                                 | 545 ms: 1.16x slower                                                             |
| scimark_fft                | 367 ms                                                 | 426 ms: 1.16x slower                                                             |
| json_loads                 | 27.2 us                                                | 31.6 us: 1.16x slower                                                            |
| coroutines                 | 22.2 ms                                                | 25.9 ms: 1.17x slower                                                            |
| sympy_expand               | 456 ms                                                 | 533 ms: 1.17x slower                                                             |
| shortest_path              | 487 ms                                                 | 569 ms: 1.17x slower                                                             |
| 2to3                       | 266 ms                                                 | 311 ms: 1.17x slower                                                             |
| scimark_sor                | 122 ms                                                 | 143 ms: 1.17x slower                                                             |
| connected_components       | 447 ms                                                 | 526 ms: 1.18x slower                                                             |
| sympy_str                  | 273 ms                                                 | 322 ms: 1.18x slower                                                             |
| logging_silent             | 101 ns                                                 | 119 ns: 1.18x slower                                                             |
| pprint_safe_repr           | 727 ms                                                 | 861 ms: 1.18x slower                                                             |
| sympy_sum                  | 150 ms                                                 | 179 ms: 1.19x slower                                                             |
| thrift                     | 800 us                                                 | 951 us: 1.19x slower                                                             |
| python_startup             | 12.7 ms                                                | 15.1 ms: 1.19x slower                                                            |
| logging_simple             | 5.65 us                                                | 6.74 us: 1.19x slower                                                            |
| richards_super             | 53.7 ms                                                | 64.5 ms: 1.20x slower                                                            |
| pprint_pformat             | 1.48 sec                                               | 1.77 sec: 1.20x slower                                                           |
| logging_format             | 6.23 us                                                | 7.52 us: 1.21x slower                                                            |
| unpickle_pure_python       | 213 us                                                 | 258 us: 1.21x slower                                                             |
| genshi_xml                 | 50.5 ms                                                | 61.1 ms: 1.21x slower                                                            |
| sympy_integrate            | 19.8 ms                                                | 24.1 ms: 1.21x slower                                                            |
| crypto_pyaes               | 74.7 ms                                                | 91.1 ms: 1.22x slower                                                            |
| sqlalchemy_imperative      | 16.9 ms                                                | 20.7 ms: 1.22x slower                                                            |
| nqueens                    | 80.9 ms                                                | 99.6 ms: 1.23x slower                                                            |
| meteor_contest             | 108 ms                                                 | 134 ms: 1.23x slower                                                             |
| scimark_lu                 | 114 ms                                                 | 141 ms: 1.23x slower                                                             |
| pickle_pure_python         | 302 us                                                 | 374 us: 1.24x slower                                                             |
| sqlalchemy_declarative     | 133 ms                                                 | 165 ms: 1.24x slower                                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.27 ms: 1.25x slower                                                            |
| sqlglot_parse              | 1.26 ms                                                | 1.58 ms: 1.25x slower                                                            |
| json_dumps                 | 10.1 ms                                                | 12.7 ms: 1.26x slower                                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.98 ms: 1.26x slower                                                            |
| genshi_text                | 22.6 ms                                                | 28.7 ms: 1.27x slower                                                            |
| many_optionals             | 857 us                                                 | 1.10 ms: 1.28x slower                                                            |
| comprehensions             | 16.5 us                                                | 21.1 us: 1.28x slower                                                            |
| chaos                      | 58.0 ms                                                | 74.6 ms: 1.29x slower                                                            |
| coverage                   | 82.8 ms                                                | 107 ms: 1.29x slower                                                             |
| hexiom                     | 6.08 ms                                                | 7.87 ms: 1.30x slower                                                            |
| typing_runtime_protocols   | 160 us                                                 | 211 us: 1.31x slower                                                             |
| scimark_monte_carlo        | 66.8 ms                                                | 87.8 ms: 1.32x slower                                                            |
| django_template            | 31.7 ms                                                | 41.7 ms: 1.32x slower                                                            |
| fannkuch                   | 394 ms                                                 | 524 ms: 1.33x slower                                                             |
| python_startup_no_site     | 7.00 ms                                                | 9.38 ms: 1.34x slower                                                            |
| raytrace                   | 262 ms                                                 | 357 ms: 1.37x slower                                                             |
| deltablue                  | 3.19 ms                                                | 4.83 ms: 1.51x slower                                                            |
| mako                       | 10.7 ms                                                | 16.8 ms: 1.58x slower                                                            |
| subparsers                 | 15.5 ms                                                | 24.6 ms: 1.59x slower                                                            |
| nbody                      | 87.7 ms                                                | 147 ms: 1.67x slower                                                             |
| bench_mp_pool              | 24.0 ms                                                | 89.6 ms: 3.74x slower                                                            |
| bench_thread_pool          | 818 us                                                 | 3.48 ms: 4.26x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.14x slower                                                                     |

Benchmark hidden because not significant (2): asyncio_websockets, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.102x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.22x