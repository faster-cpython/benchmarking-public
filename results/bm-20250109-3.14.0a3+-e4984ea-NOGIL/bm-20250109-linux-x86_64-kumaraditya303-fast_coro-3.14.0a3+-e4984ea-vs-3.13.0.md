# Results vs. 3.13.0

- fork: kumaraditya303
- ref: fast_coro
- machine: linux-x86_64
- commit hash: e4984ea
- commit date: 2025-01-09
- overall geometric mean: 1.174x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 342 ms: 1.28x slower                                                |
| docutils       | 2.58 sec                                               | 3.01 sec: 1.16x slower                                              |
| html5lib       | 63.4 ms                                                | 84.9 ms: 1.34x slower                                               |
| sphinx         | 1.03 sec                                               | 1.17 sec: 1.14x slower                                              |
| Geometric mean | (ref)                                                  | 1.23x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg          | 861 ms                                                 | 683 ms: 1.26x faster                                                |
| async_tree_memoization_tg | 463 ms                                                 | 387 ms: 1.20x faster                                                |
| async_tree_io             | 838 ms                                                 | 732 ms: 1.15x faster                                                |
| async_tree_none_tg        | 319 ms                                                 | 294 ms: 1.08x faster                                                |
| async_tree_none           | 350 ms                                                 | 341 ms: 1.03x faster                                                |
| async_tree_cpu_io_mixed   | 573 ms                                                 | 587 ms: 1.03x slower                                                |
| coroutines                | 22.2 ms                                                | 25.4 ms: 1.14x slower                                               |
| async_generators          | 433 ms                                                 | 496 ms: 1.15x slower                                                |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (3): async_tree_memoization, asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 181 ms: 1.03x faster                                                |
| float          | 78.7 ms                                                | 103 ms: 1.31x slower                                                |
| nbody          | 87.7 ms                                                | 135 ms: 1.53x slower                                                |
| Geometric mean | (ref)                                                  | 1.25x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 25.3 ms: 1.06x faster                                               |
| regex_effbot   | 3.77 ms                                                | 3.60 ms: 1.05x faster                                               |
| regex_dna      | 220 ms                                                 | 233 ms: 1.06x slower                                                |
| regex_compile  | 132 ms                                                 | 161 ms: 1.22x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 96.3 ms: 1.05x faster                                               |
| xml_etree_parse      | 154 ms                                                 | 148 ms: 1.04x faster                                                |
| json_loads           | 27.2 us                                                | 29.7 us: 1.09x slower                                               |
| tomli_loads          | 2.12 sec                                               | 2.35 sec: 1.11x slower                                              |
| xml_etree_generate   | 86.8 ms                                                | 100.0 ms: 1.15x slower                                              |
| xml_etree_process    | 60.5 ms                                                | 74.2 ms: 1.23x slower                                               |
| json_dumps           | 10.1 ms                                                | 13.4 ms: 1.32x slower                                               |
| unpickle_pure_python | 213 us                                                 | 309 us: 1.45x slower                                                |
| pickle_pure_python   | 302 us                                                 | 468 us: 1.55x slower                                                |
| Geometric mean       | (ref)                                                  | 1.19x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.6 ms: 1.23x slower                                               |
| python_startup_no_site | 7.00 ms                                                | 9.65 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.30x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 63.1 ms: 1.25x slower                                               |
| genshi_text     | 22.6 ms                                                | 30.2 ms: 1.34x slower                                               |
| django_template | 31.7 ms                                                | 46.6 ms: 1.47x slower                                               |
| mako            | 10.7 ms                                                | 18.1 ms: 1.70x slower                                               |
| Geometric mean  | (ref)                                                  | 1.43x slower                                                        |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg          | 861 ms                                                 | 683 ms: 1.26x faster                                                |
| gc_traversal              | 4.90 ms                                                | 4.08 ms: 1.20x faster                                               |
| async_tree_memoization_tg | 463 ms                                                 | 387 ms: 1.20x faster                                                |
| async_tree_io             | 838 ms                                                 | 732 ms: 1.15x faster                                                |
| deepcopy                  | 354 us                                                 | 317 us: 1.12x faster                                                |
| async_tree_none_tg        | 319 ms                                                 | 294 ms: 1.08x faster                                                |
| regex_v8                  | 26.9 ms                                                | 25.3 ms: 1.06x faster                                               |
| sqlite_synth              | 2.90 us                                                | 2.75 us: 1.05x faster                                               |
| xml_etree_iterparse       | 101 ms                                                 | 96.3 ms: 1.05x faster                                               |
| regex_effbot              | 3.77 ms                                                | 3.60 ms: 1.05x faster                                               |
| xml_etree_parse           | 154 ms                                                 | 148 ms: 1.04x faster                                                |
| create_gc_cycles          | 2.45 ms                                                | 2.38 ms: 1.03x faster                                               |
| pidigits                  | 186 ms                                                 | 181 ms: 1.03x faster                                                |
| async_tree_none           | 350 ms                                                 | 341 ms: 1.03x faster                                                |
| pathlib                   | 17.4 ms                                                | 17.0 ms: 1.02x faster                                               |
| json                      | 5.32 ms                                                | 5.40 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed   | 573 ms                                                 | 587 ms: 1.03x slower                                                |
| deepcopy_reduce           | 3.24 us                                                | 3.34 us: 1.03x slower                                               |
| k_core                    | 2.37 sec                                               | 2.46 sec: 1.04x slower                                              |
| deepcopy_memo             | 38.4 us                                                | 40.3 us: 1.05x slower                                               |
| regex_dna                 | 220 ms                                                 | 233 ms: 1.06x slower                                                |
| pylint                    | 312 ms                                                 | 339 ms: 1.09x slower                                                |
| json_loads                | 27.2 us                                                | 29.7 us: 1.09x slower                                               |
| spectral_norm             | 113 ms                                                 | 125 ms: 1.10x slower                                                |
| telco                     | 8.40 ms                                                | 9.32 ms: 1.11x slower                                               |
| tomli_loads               | 2.12 sec                                               | 2.35 sec: 1.11x slower                                              |
| bpe_tokeniser             | 4.69 sec                                               | 5.22 sec: 1.11x slower                                              |
| pycparser                 | 1.20 sec                                               | 1.34 sec: 1.12x slower                                              |
| sphinx                    | 1.03 sec                                               | 1.17 sec: 1.14x slower                                              |
| scimark_fft               | 367 ms                                                 | 418 ms: 1.14x slower                                                |
| coroutines                | 22.2 ms                                                | 25.4 ms: 1.14x slower                                               |
| async_generators          | 433 ms                                                 | 496 ms: 1.15x slower                                                |
| xml_etree_generate        | 86.8 ms                                                | 100.0 ms: 1.15x slower                                              |
| dulwich_log               | 64.6 ms                                                | 74.9 ms: 1.16x slower                                               |
| docutils                  | 2.58 sec                                               | 3.01 sec: 1.16x slower                                              |
| shortest_path             | 487 ms                                                 | 575 ms: 1.18x slower                                                |
| mdp                       | 2.54 sec                                               | 3.01 sec: 1.18x slower                                              |
| connected_components      | 447 ms                                                 | 530 ms: 1.19x slower                                                |
| sqlglot_normalize         | 108 ms                                                 | 130 ms: 1.20x slower                                                |
| nqueens                   | 80.9 ms                                                | 97.8 ms: 1.21x slower                                               |
| sympy_expand              | 456 ms                                                 | 555 ms: 1.22x slower                                                |
| sympy_str                 | 273 ms                                                 | 333 ms: 1.22x slower                                                |
| sqlglot_optimize          | 53.4 ms                                                | 65.1 ms: 1.22x slower                                               |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 6.13 ms: 1.22x slower                                               |
| sympy_sum                 | 150 ms                                                 | 184 ms: 1.22x slower                                                |
| meteor_contest            | 108 ms                                                 | 133 ms: 1.22x slower                                                |
| regex_compile             | 132 ms                                                 | 161 ms: 1.22x slower                                                |
| sympy_integrate           | 19.8 ms                                                | 24.3 ms: 1.23x slower                                               |
| xml_etree_process         | 60.5 ms                                                | 74.2 ms: 1.23x slower                                               |
| coverage                  | 82.8 ms                                                | 102 ms: 1.23x slower                                                |
| crypto_pyaes              | 74.7 ms                                                | 91.8 ms: 1.23x slower                                               |
| python_startup            | 12.7 ms                                                | 15.6 ms: 1.23x slower                                               |
| genshi_xml                | 50.5 ms                                                | 63.1 ms: 1.25x slower                                               |
| thrift                    | 800 us                                                 | 1.00 ms: 1.26x slower                                               |
| generators                | 28.8 ms                                                | 36.9 ms: 1.28x slower                                               |
| 2to3                      | 266 ms                                                 | 342 ms: 1.28x slower                                                |
| typing_runtime_protocols  | 160 us                                                 | 208 us: 1.30x slower                                                |
| pprint_safe_repr          | 727 ms                                                 | 949 ms: 1.31x slower                                                |
| fannkuch                  | 394 ms                                                 | 514 ms: 1.31x slower                                                |
| richards                  | 47.5 ms                                                | 62.3 ms: 1.31x slower                                               |
| float                     | 78.7 ms                                                | 103 ms: 1.31x slower                                                |
| many_optionals            | 857 us                                                 | 1.13 ms: 1.32x slower                                               |
| richards_super            | 53.7 ms                                                | 70.9 ms: 1.32x slower                                               |
| json_dumps                | 10.1 ms                                                | 13.4 ms: 1.32x slower                                               |
| pprint_pformat            | 1.48 sec                                               | 1.97 sec: 1.33x slower                                              |
| genshi_text               | 22.6 ms                                                | 30.2 ms: 1.34x slower                                               |
| html5lib                  | 63.4 ms                                                | 84.9 ms: 1.34x slower                                               |
| pyflate                   | 470 ms                                                 | 636 ms: 1.35x slower                                                |
| sqlalchemy_declarative    | 133 ms                                                 | 182 ms: 1.37x slower                                                |
| logging_simple            | 5.65 us                                                | 7.74 us: 1.37x slower                                               |
| logging_format            | 6.23 us                                                | 8.57 us: 1.38x slower                                               |
| scimark_lu                | 114 ms                                                 | 158 ms: 1.38x slower                                                |
| python_startup_no_site    | 7.00 ms                                                | 9.65 ms: 1.38x slower                                               |
| sqlalchemy_imperative     | 16.9 ms                                                | 23.6 ms: 1.40x slower                                               |
| unpickle_pure_python      | 213 us                                                 | 309 us: 1.45x slower                                                |
| django_template           | 31.7 ms                                                | 46.6 ms: 1.47x slower                                               |
| hexiom                    | 6.08 ms                                                | 9.06 ms: 1.49x slower                                               |
| scimark_sor               | 122 ms                                                 | 183 ms: 1.49x slower                                                |
| go                        | 141 ms                                                 | 212 ms: 1.51x slower                                                |
| scimark_monte_carlo       | 66.8 ms                                                | 102 ms: 1.53x slower                                                |
| nbody                     | 87.7 ms                                                | 135 ms: 1.53x slower                                                |
| pickle_pure_python        | 302 us                                                 | 468 us: 1.55x slower                                                |
| comprehensions            | 16.5 us                                                | 25.6 us: 1.56x slower                                               |
| chaos                     | 58.0 ms                                                | 92.1 ms: 1.59x slower                                               |
| sqlglot_transpile         | 1.57 ms                                                | 2.51 ms: 1.60x slower                                               |
| logging_silent            | 101 ns                                                 | 171 ns: 1.69x slower                                                |
| mako                      | 10.7 ms                                                | 18.1 ms: 1.70x slower                                               |
| sqlglot_parse             | 1.26 ms                                                | 2.16 ms: 1.70x slower                                               |
| subparsers                | 15.5 ms                                                | 26.3 ms: 1.70x slower                                               |
| raytrace                  | 262 ms                                                 | 469 ms: 1.79x slower                                                |
| deltablue                 | 3.19 ms                                                | 6.85 ms: 2.14x slower                                               |
| bench_mp_pool             | 24.0 ms                                                | 95.3 ms: 3.98x slower                                               |
| bench_thread_pool         | 818 us                                                 | 3.56 ms: 4.35x slower                                               |
| Geometric mean            | (ref)                                                  | 1.25x slower                                                        |

Benchmark hidden because not significant (3): async_tree_memoization, asyncio_websockets, async_tree_cpu_io_mixed_tg
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.174x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.15x
- 99% likely to have a slowdown of 1.13x

# Memory
- memory change: 1.21x