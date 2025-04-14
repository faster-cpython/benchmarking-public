# Results vs. 3.13.0

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 1e0f842
- commit date: 2025-01-24
- overall geometric mean: 1.105x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 313 ms: 1.18x slower                                                             |
| docutils       | 2.58 sec                                               | 2.87 sec: 1.11x slower                                                           |
| html5lib       | 63.4 ms                                                | 71.0 ms: 1.12x slower                                                            |
| sphinx         | 1.03 sec                                               | 1.14 sec: 1.11x slower                                                           |
| Geometric mean | (ref)                                                  | 1.13x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 574 ms: 1.50x faster                                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 335 ms: 1.38x faster                                                             |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                             |
| async_tree_none            | 350 ms                                                 | 296 ms: 1.18x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 375 ms: 1.17x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 491 ms: 1.11x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 534 ms: 1.07x faster                                                             |
| async_generators           | 433 ms                                                 | 440 ms: 1.02x slower                                                             |
| coroutines                 | 22.2 ms                                                | 25.6 ms: 1.15x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.16x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 181 ms: 1.03x faster                                                             |
| nbody          | 87.7 ms                                                | 143 ms: 1.63x slower                                                             |
| Geometric mean | (ref)                                                  | 1.16x slower                                                                     |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.50 ms: 1.08x faster                                                            |
| regex_v8       | 26.9 ms                                                | 25.1 ms: 1.07x faster                                                            |
| regex_dna      | 220 ms                                                 | 228 ms: 1.04x slower                                                             |
| regex_compile  | 132 ms                                                 | 151 ms: 1.15x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 94.9 ms: 1.07x faster                                                            |
| xml_etree_parse      | 154 ms                                                 | 149 ms: 1.04x faster                                                             |
| xml_etree_generate   | 86.8 ms                                                | 96.0 ms: 1.11x slower                                                            |
| xml_etree_process    | 60.5 ms                                                | 68.7 ms: 1.14x slower                                                            |
| tomli_loads          | 2.12 sec                                               | 2.43 sec: 1.15x slower                                                           |
| json_loads           | 27.2 us                                                | 31.8 us: 1.17x slower                                                            |
| unpickle_pure_python | 213 us                                                 | 261 us: 1.22x slower                                                             |
| pickle_pure_python   | 302 us                                                 | 376 us: 1.24x slower                                                             |
| json_dumps           | 10.1 ms                                                | 12.8 ms: 1.27x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.1 ms: 1.19x slower                                                            |
| python_startup_no_site | 7.00 ms                                                | 9.39 ms: 1.34x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 61.0 ms: 1.21x slower                                                            |
| genshi_text     | 22.6 ms                                                | 28.8 ms: 1.28x slower                                                            |
| django_template | 31.7 ms                                                | 41.4 ms: 1.31x slower                                                            |
| mako            | 10.7 ms                                                | 16.5 ms: 1.54x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.33x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 574 ms: 1.50x faster                                                             |
| create_gc_cycles           | 2.45 ms                                                | 1.70 ms: 1.44x faster                                                            |
| async_tree_memoization_tg  | 463 ms                                                 | 335 ms: 1.38x faster                                                             |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                             |
| async_tree_none            | 350 ms                                                 | 296 ms: 1.18x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 375 ms: 1.17x faster                                                             |
| gc_traversal               | 4.90 ms                                                | 4.22 ms: 1.16x faster                                                            |
| deepcopy                   | 354 us                                                 | 315 us: 1.12x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 491 ms: 1.11x faster                                                             |
| regex_effbot               | 3.77 ms                                                | 3.50 ms: 1.08x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 534 ms: 1.07x faster                                                             |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.07x faster                                                            |
| regex_v8                   | 26.9 ms                                                | 25.1 ms: 1.07x faster                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 94.9 ms: 1.07x faster                                                            |
| sqlite_synth               | 2.90 us                                                | 2.74 us: 1.06x faster                                                            |
| xml_etree_parse            | 154 ms                                                 | 149 ms: 1.04x faster                                                             |
| pidigits                   | 186 ms                                                 | 181 ms: 1.03x faster                                                             |
| async_generators           | 433 ms                                                 | 440 ms: 1.02x slower                                                             |
| deepcopy_reduce            | 3.24 us                                                | 3.30 us: 1.02x slower                                                            |
| deepcopy_memo              | 38.4 us                                                | 39.6 us: 1.03x slower                                                            |
| go                         | 141 ms                                                 | 145 ms: 1.03x slower                                                             |
| regex_dna                  | 220 ms                                                 | 228 ms: 1.04x slower                                                             |
| k_core                     | 2.37 sec                                               | 2.46 sec: 1.04x slower                                                           |
| spectral_norm              | 113 ms                                                 | 118 ms: 1.04x slower                                                             |
| pycparser                  | 1.20 sec                                               | 1.25 sec: 1.05x slower                                                           |
| json                       | 5.32 ms                                                | 5.61 ms: 1.05x slower                                                            |
| dulwich_log                | 64.6 ms                                                | 69.5 ms: 1.08x slower                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 5.05 sec: 1.08x slower                                                           |
| telco                      | 8.40 ms                                                | 9.22 ms: 1.10x slower                                                            |
| xml_etree_generate         | 86.8 ms                                                | 96.0 ms: 1.11x slower                                                            |
| sphinx                     | 1.03 sec                                               | 1.14 sec: 1.11x slower                                                           |
| docutils                   | 2.58 sec                                               | 2.87 sec: 1.11x slower                                                           |
| generators                 | 28.8 ms                                                | 32.1 ms: 1.12x slower                                                            |
| html5lib                   | 63.4 ms                                                | 71.0 ms: 1.12x slower                                                            |
| sqlglot_normalize          | 108 ms                                                 | 121 ms: 1.12x slower                                                             |
| pyflate                    | 470 ms                                                 | 531 ms: 1.13x slower                                                             |
| mdp                        | 2.54 sec                                               | 2.88 sec: 1.13x slower                                                           |
| xml_etree_process          | 60.5 ms                                                | 68.7 ms: 1.14x slower                                                            |
| sqlglot_optimize           | 53.4 ms                                                | 60.9 ms: 1.14x slower                                                            |
| regex_compile              | 132 ms                                                 | 151 ms: 1.15x slower                                                             |
| tomli_loads                | 2.12 sec                                               | 2.43 sec: 1.15x slower                                                           |
| coroutines                 | 22.2 ms                                                | 25.6 ms: 1.15x slower                                                            |
| logging_silent             | 101 ns                                                 | 117 ns: 1.15x slower                                                             |
| sympy_expand               | 456 ms                                                 | 531 ms: 1.16x slower                                                             |
| scimark_sor                | 122 ms                                                 | 143 ms: 1.17x slower                                                             |
| scimark_fft                | 367 ms                                                 | 429 ms: 1.17x slower                                                             |
| json_loads                 | 27.2 us                                                | 31.8 us: 1.17x slower                                                            |
| sympy_str                  | 273 ms                                                 | 320 ms: 1.17x slower                                                             |
| shortest_path              | 487 ms                                                 | 572 ms: 1.18x slower                                                             |
| 2to3                       | 266 ms                                                 | 313 ms: 1.18x slower                                                             |
| pprint_safe_repr           | 727 ms                                                 | 856 ms: 1.18x slower                                                             |
| sympy_sum                  | 150 ms                                                 | 177 ms: 1.18x slower                                                             |
| richards                   | 47.5 ms                                                | 56.1 ms: 1.18x slower                                                            |
| connected_components       | 447 ms                                                 | 529 ms: 1.18x slower                                                             |
| python_startup             | 12.7 ms                                                | 15.1 ms: 1.19x slower                                                            |
| logging_simple             | 5.65 us                                                | 6.74 us: 1.19x slower                                                            |
| pprint_pformat             | 1.48 sec                                               | 1.77 sec: 1.20x slower                                                           |
| thrift                     | 800 us                                                 | 959 us: 1.20x slower                                                             |
| richards_super             | 53.7 ms                                                | 64.6 ms: 1.20x slower                                                            |
| genshi_xml                 | 50.5 ms                                                | 61.0 ms: 1.21x slower                                                            |
| logging_format             | 6.23 us                                                | 7.54 us: 1.21x slower                                                            |
| sympy_integrate            | 19.8 ms                                                | 24.0 ms: 1.21x slower                                                            |
| crypto_pyaes               | 74.7 ms                                                | 91.0 ms: 1.22x slower                                                            |
| scimark_lu                 | 114 ms                                                 | 140 ms: 1.22x slower                                                             |
| unpickle_pure_python       | 213 us                                                 | 261 us: 1.22x slower                                                             |
| meteor_contest             | 108 ms                                                 | 133 ms: 1.23x slower                                                             |
| nqueens                    | 80.9 ms                                                | 99.5 ms: 1.23x slower                                                            |
| sqlalchemy_imperative      | 16.9 ms                                                | 20.8 ms: 1.23x slower                                                            |
| sqlalchemy_declarative     | 133 ms                                                 | 164 ms: 1.24x slower                                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.25 ms: 1.24x slower                                                            |
| pickle_pure_python         | 302 us                                                 | 376 us: 1.24x slower                                                             |
| sqlglot_parse              | 1.26 ms                                                | 1.58 ms: 1.25x slower                                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.97 ms: 1.26x slower                                                            |
| json_dumps                 | 10.1 ms                                                | 12.8 ms: 1.27x slower                                                            |
| comprehensions             | 16.5 us                                                | 21.0 us: 1.27x slower                                                            |
| genshi_text                | 22.6 ms                                                | 28.8 ms: 1.28x slower                                                            |
| many_optionals             | 857 us                                                 | 1.10 ms: 1.28x slower                                                            |
| hexiom                     | 6.08 ms                                                | 7.89 ms: 1.30x slower                                                            |
| chaos                      | 58.0 ms                                                | 75.5 ms: 1.30x slower                                                            |
| typing_runtime_protocols   | 160 us                                                 | 210 us: 1.31x slower                                                             |
| django_template            | 31.7 ms                                                | 41.4 ms: 1.31x slower                                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 87.5 ms: 1.31x slower                                                            |
| fannkuch                   | 394 ms                                                 | 517 ms: 1.31x slower                                                             |
| python_startup_no_site     | 7.00 ms                                                | 9.39 ms: 1.34x slower                                                            |
| coverage                   | 82.8 ms                                                | 114 ms: 1.38x slower                                                             |
| raytrace                   | 262 ms                                                 | 364 ms: 1.39x slower                                                             |
| deltablue                  | 3.19 ms                                                | 4.89 ms: 1.53x slower                                                            |
| mako                       | 10.7 ms                                                | 16.5 ms: 1.54x slower                                                            |
| subparsers                 | 15.5 ms                                                | 25.0 ms: 1.62x slower                                                            |
| nbody                      | 87.7 ms                                                | 143 ms: 1.63x slower                                                             |
| bench_mp_pool              | 24.0 ms                                                | 89.7 ms: 3.74x slower                                                            |
| bench_thread_pool          | 818 us                                                 | 3.50 ms: 4.28x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.15x slower                                                                     |

Benchmark hidden because not significant (3): float, asyncio_websockets, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.105x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 1.22x