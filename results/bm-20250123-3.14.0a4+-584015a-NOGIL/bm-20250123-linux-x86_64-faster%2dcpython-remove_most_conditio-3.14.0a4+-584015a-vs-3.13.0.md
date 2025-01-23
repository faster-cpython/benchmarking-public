# Results vs. 3.13.0

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 584015a
- commit date: 2025-01-23
- overall geometric mean: 1.107x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 313 ms: 1.18x slower                                                             |
| docutils       | 2.58 sec                                               | 2.91 sec: 1.13x slower                                                           |
| html5lib       | 63.4 ms                                                | 68.9 ms: 1.09x slower                                                            |
| sphinx         | 1.03 sec                                               | 1.16 sec: 1.13x slower                                                           |
| Geometric mean | (ref)                                                  | 1.13x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 568 ms: 1.52x faster                                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 334 ms: 1.39x faster                                                             |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                             |
| async_tree_none            | 350 ms                                                 | 294 ms: 1.19x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 373 ms: 1.17x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 532 ms: 1.08x faster                                                             |
| async_generators           | 433 ms                                                 | 438 ms: 1.01x slower                                                             |
| coroutines                 | 22.2 ms                                                | 25.9 ms: 1.17x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.16x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 182 ms: 1.03x faster                                                             |
| nbody          | 87.7 ms                                                | 137 ms: 1.56x slower                                                             |
| Geometric mean | (ref)                                                  | 1.15x slower                                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.48 ms: 1.08x faster                                                            |
| regex_v8       | 26.9 ms                                                | 25.4 ms: 1.06x faster                                                            |
| regex_dna      | 220 ms                                                 | 227 ms: 1.03x slower                                                             |
| regex_compile  | 132 ms                                                 | 152 ms: 1.15x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 95.9 ms: 1.06x faster                                                            |
| xml_etree_parse      | 154 ms                                                 | 150 ms: 1.03x faster                                                             |
| xml_etree_generate   | 86.8 ms                                                | 96.2 ms: 1.11x slower                                                            |
| xml_etree_process    | 60.5 ms                                                | 68.6 ms: 1.14x slower                                                            |
| tomli_loads          | 2.12 sec                                               | 2.43 sec: 1.15x slower                                                           |
| json_loads           | 27.2 us                                                | 31.4 us: 1.16x slower                                                            |
| unpickle_pure_python | 213 us                                                 | 261 us: 1.22x slower                                                             |
| pickle_pure_python   | 302 us                                                 | 377 us: 1.25x slower                                                             |
| json_dumps           | 10.1 ms                                                | 12.8 ms: 1.26x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.1 ms: 1.19x slower                                                            |
| python_startup_no_site | 7.00 ms                                                | 9.37 ms: 1.34x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 62.0 ms: 1.23x slower                                                            |
| genshi_text     | 22.6 ms                                                | 29.0 ms: 1.28x slower                                                            |
| django_template | 31.7 ms                                                | 42.9 ms: 1.35x slower                                                            |
| mako            | 10.7 ms                                                | 16.7 ms: 1.56x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.35x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-584015a |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 568 ms: 1.52x faster                                                             |
| create_gc_cycles           | 2.45 ms                                                | 1.72 ms: 1.42x faster                                                            |
| async_tree_memoization_tg  | 463 ms                                                 | 334 ms: 1.39x faster                                                             |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                             |
| async_tree_none            | 350 ms                                                 | 294 ms: 1.19x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 373 ms: 1.17x faster                                                             |
| deepcopy                   | 354 us                                                 | 315 us: 1.13x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                             |
| gc_traversal               | 4.90 ms                                                | 4.44 ms: 1.10x faster                                                            |
| regex_effbot               | 3.77 ms                                                | 3.48 ms: 1.08x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 532 ms: 1.08x faster                                                             |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                                            |
| regex_v8                   | 26.9 ms                                                | 25.4 ms: 1.06x faster                                                            |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.06x faster                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 95.9 ms: 1.06x faster                                                            |
| xml_etree_parse            | 154 ms                                                 | 150 ms: 1.03x faster                                                             |
| pidigits                   | 186 ms                                                 | 182 ms: 1.03x faster                                                             |
| async_generators           | 433 ms                                                 | 438 ms: 1.01x slower                                                             |
| deepcopy_reduce            | 3.24 us                                                | 3.30 us: 1.02x slower                                                            |
| pycparser                  | 1.20 sec                                               | 1.23 sec: 1.03x slower                                                           |
| regex_dna                  | 220 ms                                                 | 227 ms: 1.03x slower                                                             |
| k_core                     | 2.37 sec                                               | 2.45 sec: 1.03x slower                                                           |
| spectral_norm              | 113 ms                                                 | 117 ms: 1.04x slower                                                             |
| deepcopy_memo              | 38.4 us                                                | 40.0 us: 1.04x slower                                                            |
| go                         | 141 ms                                                 | 146 ms: 1.04x slower                                                             |
| json                       | 5.32 ms                                                | 5.58 ms: 1.05x slower                                                            |
| dulwich_log                | 64.6 ms                                                | 69.3 ms: 1.07x slower                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 5.07 sec: 1.08x slower                                                           |
| mdp                        | 2.54 sec                                               | 2.76 sec: 1.08x slower                                                           |
| html5lib                   | 63.4 ms                                                | 68.9 ms: 1.09x slower                                                            |
| telco                      | 8.40 ms                                                | 9.14 ms: 1.09x slower                                                            |
| xml_etree_generate         | 86.8 ms                                                | 96.2 ms: 1.11x slower                                                            |
| generators                 | 28.8 ms                                                | 32.0 ms: 1.11x slower                                                            |
| docutils                   | 2.58 sec                                               | 2.91 sec: 1.13x slower                                                           |
| sphinx                     | 1.03 sec                                               | 1.16 sec: 1.13x slower                                                           |
| xml_etree_process          | 60.5 ms                                                | 68.6 ms: 1.14x slower                                                            |
| sqlglot_normalize          | 108 ms                                                 | 123 ms: 1.14x slower                                                             |
| pyflate                    | 470 ms                                                 | 537 ms: 1.14x slower                                                             |
| scimark_fft                | 367 ms                                                 | 421 ms: 1.15x slower                                                             |
| tomli_loads                | 2.12 sec                                               | 2.43 sec: 1.15x slower                                                           |
| sqlglot_optimize           | 53.4 ms                                                | 61.5 ms: 1.15x slower                                                            |
| regex_compile              | 132 ms                                                 | 152 ms: 1.15x slower                                                             |
| json_loads                 | 27.2 us                                                | 31.4 us: 1.16x slower                                                            |
| coroutines                 | 22.2 ms                                                | 25.9 ms: 1.17x slower                                                            |
| shortest_path              | 487 ms                                                 | 569 ms: 1.17x slower                                                             |
| sympy_str                  | 273 ms                                                 | 321 ms: 1.18x slower                                                             |
| 2to3                       | 266 ms                                                 | 313 ms: 1.18x slower                                                             |
| thrift                     | 800 us                                                 | 943 us: 1.18x slower                                                             |
| sympy_expand               | 456 ms                                                 | 538 ms: 1.18x slower                                                             |
| scimark_sor                | 122 ms                                                 | 144 ms: 1.18x slower                                                             |
| connected_components       | 447 ms                                                 | 528 ms: 1.18x slower                                                             |
| sympy_sum                  | 150 ms                                                 | 178 ms: 1.18x slower                                                             |
| python_startup             | 12.7 ms                                                | 15.1 ms: 1.19x slower                                                            |
| pprint_safe_repr           | 727 ms                                                 | 867 ms: 1.19x slower                                                             |
| logging_silent             | 101 ns                                                 | 122 ns: 1.21x slower                                                             |
| logging_simple             | 5.65 us                                                | 6.83 us: 1.21x slower                                                            |
| pprint_pformat             | 1.48 sec                                               | 1.79 sec: 1.21x slower                                                           |
| crypto_pyaes               | 74.7 ms                                                | 90.7 ms: 1.21x slower                                                            |
| sqlalchemy_imperative      | 16.9 ms                                                | 20.6 ms: 1.22x slower                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.13 ms: 1.22x slower                                                            |
| sympy_integrate            | 19.8 ms                                                | 24.2 ms: 1.22x slower                                                            |
| unpickle_pure_python       | 213 us                                                 | 261 us: 1.22x slower                                                             |
| logging_format             | 6.23 us                                                | 7.64 us: 1.23x slower                                                            |
| genshi_xml                 | 50.5 ms                                                | 62.0 ms: 1.23x slower                                                            |
| sqlalchemy_declarative     | 133 ms                                                 | 164 ms: 1.23x slower                                                             |
| scimark_lu                 | 114 ms                                                 | 142 ms: 1.24x slower                                                             |
| meteor_contest             | 108 ms                                                 | 134 ms: 1.24x slower                                                             |
| pickle_pure_python         | 302 us                                                 | 377 us: 1.25x slower                                                             |
| sqlglot_parse              | 1.26 ms                                                | 1.58 ms: 1.25x slower                                                            |
| nqueens                    | 80.9 ms                                                | 101 ms: 1.25x slower                                                             |
| sqlglot_transpile          | 1.57 ms                                                | 1.98 ms: 1.26x slower                                                            |
| json_dumps                 | 10.1 ms                                                | 12.8 ms: 1.26x slower                                                            |
| comprehensions             | 16.5 us                                                | 21.0 us: 1.28x slower                                                            |
| many_optionals             | 857 us                                                 | 1.10 ms: 1.28x slower                                                            |
| genshi_text                | 22.6 ms                                                | 29.0 ms: 1.28x slower                                                            |
| coverage                   | 82.8 ms                                                | 107 ms: 1.29x slower                                                             |
| chaos                      | 58.0 ms                                                | 75.2 ms: 1.30x slower                                                            |
| hexiom                     | 6.08 ms                                                | 7.89 ms: 1.30x slower                                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 87.3 ms: 1.31x slower                                                            |
| richards                   | 47.5 ms                                                | 62.4 ms: 1.31x slower                                                            |
| fannkuch                   | 394 ms                                                 | 522 ms: 1.32x slower                                                             |
| typing_runtime_protocols   | 160 us                                                 | 213 us: 1.33x slower                                                             |
| richards_super             | 53.7 ms                                                | 71.8 ms: 1.34x slower                                                            |
| python_startup_no_site     | 7.00 ms                                                | 9.37 ms: 1.34x slower                                                            |
| django_template            | 31.7 ms                                                | 42.9 ms: 1.35x slower                                                            |
| raytrace                   | 262 ms                                                 | 359 ms: 1.37x slower                                                             |
| deltablue                  | 3.19 ms                                                | 4.84 ms: 1.52x slower                                                            |
| mako                       | 10.7 ms                                                | 16.7 ms: 1.56x slower                                                            |
| nbody                      | 87.7 ms                                                | 137 ms: 1.56x slower                                                             |
| subparsers                 | 15.5 ms                                                | 24.7 ms: 1.60x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 90.0 ms: 3.75x slower                                                            |
| bench_thread_pool          | 818 us                                                 | 3.47 ms: 4.25x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.15x slower                                                                     |

Benchmark hidden because not significant (3): float, asyncio_websockets, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.107x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.22x