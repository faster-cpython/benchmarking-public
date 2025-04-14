# Results vs. 3.13.0

- fork: nelhage
- ref: computed_goto_nomerg
- machine: linux-x86_64
- commit hash: 4603470
- commit date: 2025-02-10
- overall geometric mean: 1.055x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 252 ms: 1.06x faster                                                    |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.00x faster                                                  |
| html5lib       | 63.4 ms                                                | 61.2 ms: 1.04x faster                                                   |
| sphinx         | 1.03 sec                                               | 995 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                                    |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 325 ms: 1.34x faster                                                    |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 259 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                    |
| async_generators           | 433 ms                                                 | 381 ms: 1.14x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                    |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.4 ms: 1.15x faster                                                   |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| nbody          | 87.7 ms                                                | 91.7 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.21 ms: 1.17x faster                                                   |
| regex_v8       | 26.9 ms                                                | 25.2 ms: 1.07x faster                                                   |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                    |
| regex_dna      | 220 ms                                                 | 211 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                    |
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 96.5 ms: 1.05x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 83.4 ms: 1.04x faster                                                   |
| xml_etree_process    | 60.5 ms                                                | 58.4 ms: 1.04x faster                                                   |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                    |
| pickle_pure_python   | 302 us                                                 | 317 us: 1.05x slower                                                    |
| json_loads           | 27.2 us                                                | 28.7 us: 1.06x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                   |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                   |
| genshi_xml     | 50.5 ms                                                | 48.1 ms: 1.05x faster                                                   |
| mako           | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                                    |
| deepcopy                   | 354 us                                                 | 258 us: 1.38x faster                                                    |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 325 ms: 1.34x faster                                                    |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                    |
| deepcopy_memo              | 38.4 us                                                | 30.4 us: 1.26x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 259 ms: 1.23x faster                                                    |
| go                         | 141 ms                                                 | 116 ms: 1.22x faster                                                    |
| spectral_norm              | 113 ms                                                 | 94.1 ms: 1.20x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.21 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                    |
| float                      | 78.7 ms                                                | 68.4 ms: 1.15x faster                                                   |
| pylint                     | 312 ms                                                 | 272 ms: 1.15x faster                                                    |
| async_generators           | 433 ms                                                 | 381 ms: 1.14x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                    |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                    |
| scimark_fft                | 367 ms                                                 | 339 ms: 1.08x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.33 sec: 1.08x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                  |
| pyflate                    | 470 ms                                                 | 435 ms: 1.08x faster                                                    |
| telco                      | 8.40 ms                                                | 7.80 ms: 1.08x faster                                                   |
| richards                   | 47.5 ms                                                | 44.3 ms: 1.07x faster                                                   |
| richards_super             | 53.7 ms                                                | 50.2 ms: 1.07x faster                                                   |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 25.2 ms: 1.07x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.07x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.3 ms: 1.07x faster                                                   |
| thrift                     | 800 us                                                 | 753 us: 1.06x faster                                                    |
| crypto_pyaes               | 74.7 ms                                                | 70.4 ms: 1.06x faster                                                   |
| 2to3                       | 266 ms                                                 | 252 ms: 1.06x faster                                                    |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                    |
| sqlglot_normalize          | 108 ms                                                 | 103 ms: 1.05x faster                                                    |
| genshi_xml                 | 50.5 ms                                                | 48.1 ms: 1.05x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 96.5 ms: 1.05x faster                                                   |
| logging_simple             | 5.65 us                                                | 5.39 us: 1.05x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.04x faster                                                    |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                  |
| regex_dna                  | 220 ms                                                 | 211 ms: 1.04x faster                                                    |
| xml_etree_generate         | 86.8 ms                                                | 83.4 ms: 1.04x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                                   |
| sphinx                     | 1.03 sec                                               | 995 ms: 1.04x faster                                                    |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.85 ms: 1.04x faster                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 51.5 ms: 1.04x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 58.4 ms: 1.04x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.73 ms: 1.04x faster                                                   |
| html5lib                   | 63.4 ms                                                | 61.2 ms: 1.04x faster                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.3 ms: 1.03x faster                                                   |
| json                       | 5.32 ms                                                | 5.15 ms: 1.03x faster                                                   |
| generators                 | 28.8 ms                                                | 27.8 ms: 1.03x faster                                                   |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                                    |
| mdp                        | 2.54 sec                                               | 2.46 sec: 1.03x faster                                                  |
| connected_components       | 447 ms                                                 | 434 ms: 1.03x faster                                                    |
| pprint_safe_repr           | 727 ms                                                 | 707 ms: 1.03x faster                                                    |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                    |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                    |
| shortest_path              | 487 ms                                                 | 474 ms: 1.03x faster                                                    |
| logging_format             | 6.23 us                                                | 6.07 us: 1.03x faster                                                   |
| sqlglot_parse              | 1.26 ms                                                | 1.23 ms: 1.02x faster                                                   |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                    |
| sqlglot_transpile          | 1.57 ms                                                | 1.54 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                                  |
| sympy_expand               | 456 ms                                                 | 450 ms: 1.01x faster                                                    |
| typing_runtime_protocols   | 160 us                                                 | 158 us: 1.01x faster                                                    |
| chaos                      | 58.0 ms                                                | 57.5 ms: 1.01x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                                   |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 66.2 ms: 1.01x faster                                                   |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| deltablue                  | 3.19 ms                                                | 3.18 ms: 1.00x faster                                                   |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.00x faster                                                  |
| hexiom                     | 6.08 ms                                                | 6.10 ms: 1.00x slower                                                   |
| python_startup_no_site     | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                   |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                    |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                   |
| fannkuch                   | 394 ms                                                 | 403 ms: 1.02x slower                                                    |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                    |
| raytrace                   | 262 ms                                                 | 268 ms: 1.02x slower                                                    |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                   |
| logging_silent             | 101 ns                                                 | 104 ns: 1.03x slower                                                    |
| nbody                      | 87.7 ms                                                | 91.7 ms: 1.05x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 317 us: 1.05x slower                                                    |
| bench_thread_pool          | 818 us                                                 | 860 us: 1.05x slower                                                    |
| json_loads                 | 27.2 us                                                | 28.7 us: 1.06x slower                                                   |
| coverage                   | 82.8 ms                                                | 89.5 ms: 1.08x slower                                                   |
| many_optionals             | 857 us                                                 | 931 us: 1.09x slower                                                    |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                   |
| subparsers                 | 15.5 ms                                                | 20.3 ms: 1.31x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (4): django_template, dulwich_log, nqueens, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.055x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x