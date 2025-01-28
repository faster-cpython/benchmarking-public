# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: py_likely_unlikely
- machine: linux-x86_64
- commit hash: 2b26797
- commit date: 2025-01-29
- overall geometric mean: 1.027x faster
- HPT reliability: 95.02%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.02x faster                                                           |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                         |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                           |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                                           |
| async_tree_io              | 838 ms                                                 | 625 ms: 1.34x faster                                                           |
| async_tree_none            | 350 ms                                                 | 273 ms: 1.28x faster                                                           |
| async_tree_memoization     | 437 ms                                                 | 341 ms: 1.28x faster                                                           |
| async_tree_none_tg         | 319 ms                                                 | 258 ms: 1.24x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                           |
| async_generators           | 433 ms                                                 | 406 ms: 1.07x faster                                                           |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                           |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.4 ms: 1.18x faster                                                          |
| nbody          | 87.7 ms                                                | 86.6 ms: 1.01x faster                                                          |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.23 ms: 1.17x faster                                                          |
| regex_v8       | 26.9 ms                                                | 24.1 ms: 1.11x faster                                                          |
| regex_dna      | 220 ms                                                 | 208 ms: 1.06x faster                                                           |
| regex_compile  | 132 ms                                                 | 131 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                         |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                           |
| xml_etree_process    | 60.5 ms                                                | 55.6 ms: 1.09x faster                                                          |
| xml_etree_generate   | 86.8 ms                                                | 81.5 ms: 1.07x faster                                                          |
| unpickle_pure_python | 213 us                                                 | 202 us: 1.06x faster                                                           |
| xml_etree_iterparse  | 101 ms                                                 | 95.9 ms: 1.06x faster                                                          |
| pickle_pure_python   | 302 us                                                 | 317 us: 1.05x slower                                                           |
| json_loads           | 27.2 us                                                | 29.3 us: 1.08x slower                                                          |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.12 ms: 1.02x slower                                                          |
| python_startup         | 12.7 ms                                                | 13.0 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.2 ms: 1.05x faster                                                          |
| genshi_text     | 22.6 ms                                                | 23.9 ms: 1.06x slower                                                          |
| django_template | 31.7 ms                                                | 33.6 ms: 1.06x slower                                                          |
| genshi_xml      | 50.5 ms                                                | 60.1 ms: 1.19x slower                                                          |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                           |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                                           |
| async_tree_io              | 838 ms                                                 | 625 ms: 1.34x faster                                                           |
| deepcopy                   | 354 us                                                 | 270 us: 1.31x faster                                                           |
| async_tree_none            | 350 ms                                                 | 273 ms: 1.28x faster                                                           |
| async_tree_memoization     | 437 ms                                                 | 341 ms: 1.28x faster                                                           |
| async_tree_none_tg         | 319 ms                                                 | 258 ms: 1.24x faster                                                           |
| deepcopy_memo              | 38.4 us                                                | 31.5 us: 1.22x faster                                                          |
| float                      | 78.7 ms                                                | 66.4 ms: 1.18x faster                                                          |
| deepcopy_reduce            | 3.24 us                                                | 2.75 us: 1.18x faster                                                          |
| scimark_fft                | 367 ms                                                 | 314 ms: 1.17x faster                                                           |
| regex_effbot               | 3.77 ms                                                | 3.23 ms: 1.17x faster                                                          |
| spectral_norm              | 113 ms                                                 | 97.1 ms: 1.17x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                           |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                           |
| regex_v8                   | 26.9 ms                                                | 24.1 ms: 1.11x faster                                                          |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                           |
| crypto_pyaes               | 74.7 ms                                                | 67.7 ms: 1.10x faster                                                          |
| richards_super             | 53.7 ms                                                | 48.8 ms: 1.10x faster                                                          |
| telco                      | 8.40 ms                                                | 7.70 ms: 1.09x faster                                                          |
| xml_etree_process          | 60.5 ms                                                | 55.6 ms: 1.09x faster                                                          |
| pylint                     | 312 ms                                                 | 289 ms: 1.08x faster                                                           |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.07x faster                                                          |
| async_generators           | 433 ms                                                 | 406 ms: 1.07x faster                                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.71 ms: 1.07x faster                                                          |
| xml_etree_generate         | 86.8 ms                                                | 81.5 ms: 1.07x faster                                                          |
| sqlite_synth               | 2.90 us                                                | 2.74 us: 1.06x faster                                                          |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.06x faster                                                           |
| unpickle_pure_python       | 213 us                                                 | 202 us: 1.06x faster                                                           |
| xml_etree_iterparse        | 101 ms                                                 | 95.9 ms: 1.06x faster                                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.46 sec: 1.05x faster                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 63.5 ms: 1.05x faster                                                          |
| mako                       | 10.7 ms                                                | 10.2 ms: 1.05x faster                                                          |
| pyflate                    | 470 ms                                                 | 449 ms: 1.05x faster                                                           |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                                           |
| richards                   | 47.5 ms                                                | 45.6 ms: 1.04x faster                                                          |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                         |
| gc_traversal               | 4.90 ms                                                | 4.73 ms: 1.04x faster                                                          |
| go                         | 141 ms                                                 | 136 ms: 1.04x faster                                                           |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                         |
| json                       | 5.32 ms                                                | 5.21 ms: 1.02x faster                                                          |
| thrift                     | 800 us                                                 | 783 us: 1.02x faster                                                           |
| 2to3                       | 266 ms                                                 | 262 ms: 1.02x faster                                                           |
| connected_components       | 447 ms                                                 | 441 ms: 1.01x faster                                                           |
| nbody                      | 87.7 ms                                                | 86.6 ms: 1.01x faster                                                          |
| shortest_path              | 487 ms                                                 | 484 ms: 1.01x faster                                                           |
| regex_compile              | 132 ms                                                 | 131 ms: 1.01x faster                                                           |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.00x faster                                                           |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                           |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                           |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                          |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.0 ms: 1.01x slower                                                          |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                           |
| mdp                        | 2.54 sec                                               | 2.57 sec: 1.01x slower                                                         |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                                           |
| python_startup_no_site     | 7.00 ms                                                | 7.12 ms: 1.02x slower                                                          |
| chaos                      | 58.0 ms                                                | 59.0 ms: 1.02x slower                                                          |
| sqlglot_parse              | 1.26 ms                                                | 1.29 ms: 1.02x slower                                                          |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                         |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                           |
| logging_format             | 6.23 us                                                | 6.34 us: 1.02x slower                                                          |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                          |
| logging_simple             | 5.65 us                                                | 5.78 us: 1.02x slower                                                          |
| python_startup             | 12.7 ms                                                | 13.0 ms: 1.02x slower                                                          |
| deltablue                  | 3.19 ms                                                | 3.28 ms: 1.03x slower                                                          |
| sqlglot_optimize           | 53.4 ms                                                | 55.1 ms: 1.03x slower                                                          |
| sympy_str                  | 273 ms                                                 | 282 ms: 1.03x slower                                                           |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                                           |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                          |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                         |
| sympy_expand               | 456 ms                                                 | 476 ms: 1.04x slower                                                           |
| sympy_sum                  | 150 ms                                                 | 157 ms: 1.04x slower                                                           |
| sympy_integrate            | 19.8 ms                                                | 20.8 ms: 1.05x slower                                                          |
| pickle_pure_python         | 302 us                                                 | 317 us: 1.05x slower                                                           |
| pprint_safe_repr           | 727 ms                                                 | 762 ms: 1.05x slower                                                           |
| pprint_pformat             | 1.48 sec                                               | 1.55 sec: 1.05x slower                                                         |
| dulwich_log                | 64.6 ms                                                | 67.9 ms: 1.05x slower                                                          |
| genshi_text                | 22.6 ms                                                | 23.9 ms: 1.06x slower                                                          |
| django_template            | 31.7 ms                                                | 33.6 ms: 1.06x slower                                                          |
| json_loads                 | 27.2 us                                                | 29.3 us: 1.08x slower                                                          |
| coverage                   | 82.8 ms                                                | 90.5 ms: 1.09x slower                                                          |
| logging_silent             | 101 ns                                                 | 111 ns: 1.09x slower                                                           |
| raytrace                   | 262 ms                                                 | 287 ms: 1.10x slower                                                           |
| bench_thread_pool          | 818 us                                                 | 898 us: 1.10x slower                                                           |
| comprehensions             | 16.5 us                                                | 18.1 us: 1.10x slower                                                          |
| nqueens                    | 80.9 ms                                                | 91.3 ms: 1.13x slower                                                          |
| many_optionals             | 857 us                                                 | 978 us: 1.14x slower                                                           |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                          |
| genshi_xml                 | 50.5 ms                                                | 60.1 ms: 1.19x slower                                                          |
| hexiom                     | 6.08 ms                                                | 7.31 ms: 1.20x slower                                                          |
| generators                 | 28.8 ms                                                | 37.3 ms: 1.30x slower                                                          |
| subparsers                 | 15.5 ms                                                | 21.1 ms: 1.36x slower                                                          |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): html5lib, fannkuch
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.027x faster

# HPT report

- Reliability score: 95.02% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x