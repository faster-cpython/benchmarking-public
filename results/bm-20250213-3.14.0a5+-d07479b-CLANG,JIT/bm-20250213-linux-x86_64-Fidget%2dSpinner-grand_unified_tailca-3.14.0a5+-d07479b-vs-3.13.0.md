# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: grand_unified_tailca
- machine: linux-x86_64
- commit hash: d07479b
- commit date: 2025-02-13
- overall geometric mean: 1.067x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                             |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                           |
| html5lib       | 63.4 ms                                                | 58.4 ms: 1.08x faster                                                            |
| sphinx         | 1.03 sec                                               | 999 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                             |
| async_tree_io_tg           | 861 ms                                                 | 625 ms: 1.38x faster                                                             |
| async_tree_io              | 838 ms                                                 | 611 ms: 1.37x faster                                                             |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                             |
| async_generators           | 433 ms                                                 | 395 ms: 1.10x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 526 ms: 1.09x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 514 ms: 1.06x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                                     |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.2 ms: 1.19x faster                                                            |
| nbody          | 87.7 ms                                                | 86.9 ms: 1.01x faster                                                            |
| pidigits       | 186 ms                                                 | 222 ms: 1.19x slower                                                             |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.15 ms: 1.19x faster                                                            |
| regex_dna      | 220 ms                                                 | 196 ms: 1.12x faster                                                             |
| regex_v8       | 26.9 ms                                                | 24.3 ms: 1.10x faster                                                            |
| regex_compile  | 132 ms                                                 | 124 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.81 sec: 1.17x faster                                                           |
| xml_etree_process    | 60.5 ms                                                | 55.7 ms: 1.09x faster                                                            |
| xml_etree_generate   | 86.8 ms                                                | 80.4 ms: 1.08x faster                                                            |
| unpickle_pure_python | 213 us                                                 | 211 us: 1.01x faster                                                             |
| xml_etree_iterparse  | 101 ms                                                 | 102 ms: 1.01x slower                                                             |
| xml_etree_parse      | 154 ms                                                 | 158 ms: 1.02x slower                                                             |
| pickle_pure_python   | 302 us                                                 | 312 us: 1.03x slower                                                             |
| json_loads           | 27.2 us                                                | 30.6 us: 1.13x slower                                                            |
| json_dumps           | 10.1 ms                                                | 12.2 ms: 1.21x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.01 ms: 1.00x slower                                                            |
| python_startup         | 12.7 ms                                                | 12.7 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.5 ms: 1.10x faster                                                            |
| genshi_xml      | 50.5 ms                                                | 47.6 ms: 1.06x faster                                                            |
| django_template | 31.7 ms                                                | 30.4 ms: 1.04x faster                                                            |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-Fidget%2dSpinner-grand_unified_tailca-3.14.0a5+-d07479b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                             |
| deepcopy                   | 354 us                                                 | 242 us: 1.46x faster                                                             |
| spectral_norm              | 113 ms                                                 | 81.4 ms: 1.39x faster                                                            |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                             |
| async_tree_io_tg           | 861 ms                                                 | 625 ms: 1.38x faster                                                             |
| async_tree_io              | 838 ms                                                 | 611 ms: 1.37x faster                                                             |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                                             |
| deepcopy_memo              | 38.4 us                                                | 28.9 us: 1.33x faster                                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.47 us: 1.31x faster                                                            |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                             |
| scimark_fft                | 367 ms                                                 | 286 ms: 1.28x faster                                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.00 ms: 1.26x faster                                                            |
| pathlib                    | 17.4 ms                                                | 14.5 ms: 1.20x faster                                                            |
| regex_effbot               | 3.77 ms                                                | 3.15 ms: 1.19x faster                                                            |
| richards                   | 47.5 ms                                                | 40.0 ms: 1.19x faster                                                            |
| float                      | 78.7 ms                                                | 66.2 ms: 1.19x faster                                                            |
| telco                      | 8.40 ms                                                | 7.14 ms: 1.18x faster                                                            |
| tomli_loads                | 2.12 sec                                               | 1.81 sec: 1.17x faster                                                           |
| go                         | 141 ms                                                 | 120 ms: 1.17x faster                                                             |
| logging_silent             | 101 ns                                                 | 86.5 ns: 1.17x faster                                                            |
| pyflate                    | 470 ms                                                 | 407 ms: 1.15x faster                                                             |
| richards_super             | 53.7 ms                                                | 46.8 ms: 1.15x faster                                                            |
| scimark_sor                | 122 ms                                                 | 107 ms: 1.14x faster                                                             |
| pylint                     | 312 ms                                                 | 274 ms: 1.14x faster                                                             |
| regex_dna                  | 220 ms                                                 | 196 ms: 1.12x faster                                                             |
| scimark_monte_carlo        | 66.8 ms                                                | 60.2 ms: 1.11x faster                                                            |
| regex_v8                   | 26.9 ms                                                | 24.3 ms: 1.10x faster                                                            |
| genshi_text                | 22.6 ms                                                | 20.5 ms: 1.10x faster                                                            |
| async_generators           | 433 ms                                                 | 395 ms: 1.10x faster                                                             |
| sqlite_synth               | 2.90 us                                                | 2.65 us: 1.10x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 526 ms: 1.09x faster                                                             |
| xml_etree_process          | 60.5 ms                                                | 55.7 ms: 1.09x faster                                                            |
| scimark_lu                 | 114 ms                                                 | 105 ms: 1.09x faster                                                             |
| html5lib                   | 63.4 ms                                                | 58.4 ms: 1.08x faster                                                            |
| xml_etree_generate         | 86.8 ms                                                | 80.4 ms: 1.08x faster                                                            |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                           |
| thrift                     | 800 us                                                 | 742 us: 1.08x faster                                                             |
| chaos                      | 58.0 ms                                                | 53.9 ms: 1.08x faster                                                            |
| logging_simple             | 5.65 us                                                | 5.29 us: 1.07x faster                                                            |
| logging_format             | 6.23 us                                                | 5.87 us: 1.06x faster                                                            |
| regex_compile              | 132 ms                                                 | 124 ms: 1.06x faster                                                             |
| genshi_xml                 | 50.5 ms                                                | 47.6 ms: 1.06x faster                                                            |
| generators                 | 28.8 ms                                                | 27.2 ms: 1.06x faster                                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.43 sec: 1.06x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 514 ms: 1.06x faster                                                             |
| nqueens                    | 80.9 ms                                                | 77.2 ms: 1.05x faster                                                            |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                             |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                             |
| sqlglot_normalize          | 108 ms                                                 | 103 ms: 1.04x faster                                                             |
| django_template            | 31.7 ms                                                | 30.4 ms: 1.04x faster                                                            |
| coverage                   | 82.8 ms                                                | 79.6 ms: 1.04x faster                                                            |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.3 ms: 1.04x faster                                                            |
| sphinx                     | 1.03 sec                                               | 999 ms: 1.03x faster                                                             |
| typing_runtime_protocols   | 160 us                                                 | 155 us: 1.03x faster                                                             |
| crypto_pyaes               | 74.7 ms                                                | 72.6 ms: 1.03x faster                                                            |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.03x faster                                                            |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.03x faster                                                             |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.02x faster                                                             |
| deltablue                  | 3.19 ms                                                | 3.14 ms: 1.02x faster                                                            |
| raytrace                   | 262 ms                                                 | 258 ms: 1.01x faster                                                             |
| dulwich_log                | 64.6 ms                                                | 63.9 ms: 1.01x faster                                                            |
| unpickle_pure_python       | 213 us                                                 | 211 us: 1.01x faster                                                             |
| nbody                      | 87.7 ms                                                | 86.9 ms: 1.01x faster                                                            |
| sqlglot_optimize           | 53.4 ms                                                | 52.9 ms: 1.01x faster                                                            |
| python_startup_no_site     | 7.00 ms                                                | 7.01 ms: 1.00x slower                                                            |
| python_startup             | 12.7 ms                                                | 12.7 ms: 1.00x slower                                                            |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.00x slower                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 102 ms: 1.01x slower                                                             |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                                             |
| fannkuch                   | 394 ms                                                 | 400 ms: 1.02x slower                                                             |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                            |
| gc_traversal               | 4.90 ms                                                | 4.98 ms: 1.02x slower                                                            |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                           |
| pprint_safe_repr           | 727 ms                                                 | 743 ms: 1.02x slower                                                             |
| xml_etree_parse            | 154 ms                                                 | 158 ms: 1.02x slower                                                             |
| bench_thread_pool          | 818 us                                                 | 837 us: 1.02x slower                                                             |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                            |
| json                       | 5.32 ms                                                | 5.49 ms: 1.03x slower                                                            |
| pickle_pure_python         | 302 us                                                 | 312 us: 1.03x slower                                                             |
| connected_components       | 447 ms                                                 | 461 ms: 1.03x slower                                                             |
| create_gc_cycles           | 2.45 ms                                                | 2.54 ms: 1.04x slower                                                            |
| meteor_contest             | 108 ms                                                 | 113 ms: 1.04x slower                                                             |
| hexiom                     | 6.08 ms                                                | 6.43 ms: 1.06x slower                                                            |
| pprint_pformat             | 1.48 sec                                               | 1.57 sec: 1.06x slower                                                           |
| many_optionals             | 857 us                                                 | 934 us: 1.09x slower                                                             |
| json_loads                 | 27.2 us                                                | 30.6 us: 1.13x slower                                                            |
| mdp                        | 2.54 sec                                               | 2.90 sec: 1.14x slower                                                           |
| pidigits                   | 186 ms                                                 | 222 ms: 1.19x slower                                                             |
| json_dumps                 | 10.1 ms                                                | 12.2 ms: 1.21x slower                                                            |
| subparsers                 | 15.5 ms                                                | 20.3 ms: 1.31x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 79.6 ms: 3.32x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                                     |

Benchmark hidden because not significant (5): k_core, sqlglot_parse, asyncio_websockets, sympy_expand, coroutines
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.067x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x