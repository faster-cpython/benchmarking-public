# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: lower_jit_tier1
- machine: linux-x86_64
- commit hash: 4d50db6
- commit date: 2024-12-13
- overall geometric mean: 1.031x faster
- HPT reliability: 93.32%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                        |
| docutils       | 2.58 sec                                               | 2.73 sec: 1.06x slower                                                      |
| html5lib       | 63.4 ms                                                | 64.7 ms: 1.02x slower                                                       |
| sphinx         | 1.03 sec                                               | 1.06 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                                        |
| async_tree_io_tg           | 861 ms                                                 | 608 ms: 1.42x faster                                                        |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                        |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                        |
| async_tree_memoization     | 437 ms                                                 | 338 ms: 1.29x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                                        |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                        |
| async_generators           | 433 ms                                                 | 450 ms: 1.04x slower                                                        |
| coroutines                 | 22.2 ms                                                | 24.1 ms: 1.08x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 73.4 ms: 1.07x faster                                                       |
| nbody          | 87.7 ms                                                | 83.0 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.23 ms: 1.17x faster                                                       |
| regex_v8       | 26.9 ms                                                | 25.0 ms: 1.07x faster                                                       |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                        |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.89 sec: 1.12x faster                                                      |
| xml_etree_generate   | 86.8 ms                                                | 77.8 ms: 1.12x faster                                                       |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 55.0 ms: 1.10x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 195 us: 1.09x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 95.1 ms: 1.06x faster                                                       |
| json_loads           | 27.2 us                                                | 26.2 us: 1.04x faster                                                       |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                       |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.1 ms: 1.05x faster                                                       |
| genshi_text     | 22.6 ms                                                | 23.6 ms: 1.05x slower                                                       |
| django_template | 31.7 ms                                                | 33.4 ms: 1.05x slower                                                       |
| genshi_xml      | 50.5 ms                                                | 56.0 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 312 ms: 1.48x faster                                                        |
| async_tree_io_tg           | 861 ms                                                 | 608 ms: 1.42x faster                                                        |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                        |
| deepcopy                   | 354 us                                                 | 265 us: 1.34x faster                                                        |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                       |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                        |
| async_tree_memoization     | 437 ms                                                 | 338 ms: 1.29x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.23 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                                        |
| scimark_fft                | 367 ms                                                 | 325 ms: 1.13x faster                                                        |
| tomli_loads                | 2.12 sec                                               | 1.89 sec: 1.12x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 77.8 ms: 1.12x faster                                                       |
| go                         | 141 ms                                                 | 126 ms: 1.11x faster                                                        |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                        |
| telco                      | 8.40 ms                                                | 7.56 ms: 1.11x faster                                                       |
| json                       | 5.32 ms                                                | 4.81 ms: 1.11x faster                                                       |
| xml_etree_process          | 60.5 ms                                                | 55.0 ms: 1.10x faster                                                       |
| unpickle_pure_python       | 213 us                                                 | 195 us: 1.09x faster                                                        |
| crypto_pyaes               | 74.7 ms                                                | 68.7 ms: 1.09x faster                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.37 sec: 1.07x faster                                                      |
| regex_v8                   | 26.9 ms                                                | 25.0 ms: 1.07x faster                                                       |
| float                      | 78.7 ms                                                | 73.4 ms: 1.07x faster                                                       |
| pylint                     | 312 ms                                                 | 292 ms: 1.07x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 95.1 ms: 1.06x faster                                                       |
| pathlib                    | 17.4 ms                                                | 16.3 ms: 1.06x faster                                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.75 ms: 1.06x faster                                                       |
| scimark_monte_carlo        | 66.8 ms                                                | 63.2 ms: 1.06x faster                                                       |
| nbody                      | 87.7 ms                                                | 83.0 ms: 1.06x faster                                                       |
| mako                       | 10.7 ms                                                | 10.1 ms: 1.05x faster                                                       |
| richards                   | 47.5 ms                                                | 45.2 ms: 1.05x faster                                                       |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                                       |
| thrift                     | 800 us                                                 | 766 us: 1.04x faster                                                        |
| richards_super             | 53.7 ms                                                | 51.7 ms: 1.04x faster                                                       |
| json_loads                 | 27.2 us                                                | 26.2 us: 1.04x faster                                                       |
| gc_traversal               | 4.90 ms                                                | 4.73 ms: 1.03x faster                                                       |
| fannkuch                   | 394 ms                                                 | 381 ms: 1.03x faster                                                        |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                        |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                      |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                        |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                        |
| connected_components       | 447 ms                                                 | 439 ms: 1.02x faster                                                        |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                                       |
| pyflate                    | 470 ms                                                 | 465 ms: 1.01x faster                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.43 ms: 1.01x faster                                                       |
| spectral_norm              | 113 ms                                                 | 112 ms: 1.01x faster                                                        |
| regex_dna                  | 220 ms                                                 | 218 ms: 1.01x faster                                                        |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.00x faster                                                        |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                        |
| coverage                   | 82.8 ms                                                | 83.5 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                                        |
| python_startup_no_site     | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                       |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                       |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                                        |
| html5lib                   | 63.4 ms                                                | 64.7 ms: 1.02x slower                                                       |
| sqlglot_optimize           | 53.4 ms                                                | 54.7 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.26 ms                                                | 1.30 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 727 ms                                                 | 747 ms: 1.03x slower                                                        |
| sphinx                     | 1.03 sec                                               | 1.06 sec: 1.03x slower                                                      |
| chaos                      | 58.0 ms                                                | 59.7 ms: 1.03x slower                                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.62 ms: 1.03x slower                                                       |
| deltablue                  | 3.19 ms                                                | 3.29 ms: 1.03x slower                                                       |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                       |
| async_generators           | 433 ms                                                 | 450 ms: 1.04x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                                        |
| pprint_pformat             | 1.48 sec                                               | 1.54 sec: 1.04x slower                                                      |
| genshi_text                | 22.6 ms                                                | 23.6 ms: 1.05x slower                                                       |
| sympy_integrate            | 19.8 ms                                                | 20.8 ms: 1.05x slower                                                       |
| dulwich_log                | 64.6 ms                                                | 67.6 ms: 1.05x slower                                                       |
| sympy_str                  | 273 ms                                                 | 286 ms: 1.05x slower                                                        |
| django_template            | 31.7 ms                                                | 33.4 ms: 1.05x slower                                                       |
| docutils                   | 2.58 sec                                               | 2.73 sec: 1.06x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                        |
| sympy_expand               | 456 ms                                                 | 486 ms: 1.07x slower                                                        |
| bench_thread_pool          | 818 us                                                 | 882 us: 1.08x slower                                                        |
| coroutines                 | 22.2 ms                                                | 24.1 ms: 1.08x slower                                                       |
| raytrace                   | 262 ms                                                 | 284 ms: 1.08x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.08x slower                                                       |
| nqueens                    | 80.9 ms                                                | 88.4 ms: 1.09x slower                                                       |
| mdp                        | 2.54 sec                                               | 2.80 sec: 1.10x slower                                                      |
| genshi_xml                 | 50.5 ms                                                | 56.0 ms: 1.11x slower                                                       |
| logging_silent             | 101 ns                                                 | 114 ns: 1.13x slower                                                        |
| hexiom                     | 6.08 ms                                                | 6.94 ms: 1.14x slower                                                       |
| many_optionals             | 857 us                                                 | 988 us: 1.15x slower                                                        |
| generators                 | 28.8 ms                                                | 34.6 ms: 1.20x slower                                                       |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (7): scimark_lu, djangocms, logging_format, shortest_path, pidigits, pycparser, logging_simple
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241213-3.14.0a2+-4d50db6-JIT/bm-20241213-linux-x86_64-Fidget%2dSpinner-lower_jit_tier1-3.14.0a2+-4d50db6.json: mypy2

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 93.32% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x