# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: outline
- machine: linux-x86_64
- commit hash: 69dad45
- commit date: 2025-05-08
- overall geometric mean: 1.025x faster
- HPT reliability: 75.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 265 ms: 1.00x faster                                                |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.04x slower                                              |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 319 ms: 1.37x faster                                                |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.32x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                |
| async_generators           | 433 ms                                                 | 426 ms: 1.02x faster                                                |
| coroutines                 | 22.2 ms                                                | 24.5 ms: 1.10x slower                                               |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.4 ms: 1.13x faster                                               |
| pidigits       | 186 ms                                                 | 195 ms: 1.05x slower                                                |
| nbody          | 87.7 ms                                                | 99.3 ms: 1.13x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 2.95 ms: 1.28x faster                                               |
| regex_v8       | 26.9 ms                                                | 22.4 ms: 1.20x faster                                               |
| regex_dna      | 220 ms                                                 | 195 ms: 1.12x faster                                                |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.15x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                                |
| xml_etree_generate   | 86.8 ms                                                | 83.8 ms: 1.04x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 58.7 ms: 1.03x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.3 ms: 1.03x faster                                               |
| tomli_loads          | 2.12 sec                                               | 2.06 sec: 1.03x faster                                              |
| json_loads           | 27.2 us                                                | 29.4 us: 1.08x slower                                               |
| unpickle_pure_python | 213 us                                                 | 234 us: 1.10x slower                                                |
| pickle_pure_python   | 302 us                                                 | 335 us: 1.11x slower                                                |
| json_dumps           | 10.1 ms                                                | 12.1 ms: 1.20x slower                                               |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.96 ms: 1.01x faster                                               |
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                               |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                               |
| genshi_xml      | 50.5 ms                                                | 49.7 ms: 1.02x faster                                               |
| django_template | 31.7 ms                                                | 32.9 ms: 1.04x slower                                               |
| mako            | 10.7 ms                                                | 11.7 ms: 1.09x slower                                               |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.29 sec: 1.97x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 319 ms: 1.37x faster                                                |
| deepcopy                   | 354 us                                                 | 260 us: 1.37x faster                                                |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.32x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                |
| regex_effbot               | 3.77 ms                                                | 2.95 ms: 1.28x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 30.8 us: 1.25x faster                                               |
| richards                   | 47.5 ms                                                | 38.5 ms: 1.24x faster                                               |
| richards_super             | 53.7 ms                                                | 43.8 ms: 1.23x faster                                               |
| regex_v8                   | 26.9 ms                                                | 22.4 ms: 1.20x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                |
| float                      | 78.7 ms                                                | 69.4 ms: 1.13x faster                                               |
| regex_dna                  | 220 ms                                                 | 195 ms: 1.12x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                |
| pylint                     | 312 ms                                                 | 285 ms: 1.09x faster                                                |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                               |
| go                         | 141 ms                                                 | 135 ms: 1.04x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                              |
| logging_silent             | 101 ns                                                 | 97.4 ns: 1.04x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                               |
| xml_etree_generate         | 86.8 ms                                                | 83.8 ms: 1.04x faster                                               |
| gc_traversal               | 4.90 ms                                                | 4.73 ms: 1.04x faster                                               |
| dulwich_log                | 64.6 ms                                                | 62.5 ms: 1.03x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 58.7 ms: 1.03x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 98.3 ms: 1.03x faster                                               |
| tomli_loads                | 2.12 sec                                               | 2.06 sec: 1.03x faster                                              |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                               |
| telco                      | 8.40 ms                                                | 8.21 ms: 1.02x faster                                               |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                               |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                |
| pyflate                    | 470 ms                                                 | 462 ms: 1.02x faster                                                |
| async_generators           | 433 ms                                                 | 426 ms: 1.02x faster                                                |
| genshi_xml                 | 50.5 ms                                                | 49.7 ms: 1.02x faster                                               |
| scimark_fft                | 367 ms                                                 | 362 ms: 1.01x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                               |
| json                       | 5.32 ms                                                | 5.26 ms: 1.01x faster                                               |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                |
| python_startup_no_site     | 7.00 ms                                                | 6.96 ms: 1.01x faster                                               |
| 2to3                       | 266 ms                                                 | 265 ms: 1.00x faster                                                |
| sympy_str                  | 273 ms                                                 | 275 ms: 1.01x slower                                                |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 135 ms: 1.01x slower                                                |
| logging_simple             | 5.65 us                                                | 5.74 us: 1.02x slower                                               |
| meteor_contest             | 108 ms                                                 | 111 ms: 1.02x slower                                                |
| connected_components       | 447 ms                                                 | 459 ms: 1.03x slower                                                |
| logging_format             | 6.23 us                                                | 6.41 us: 1.03x slower                                               |
| nqueens                    | 80.9 ms                                                | 83.7 ms: 1.04x slower                                               |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.04x slower                                              |
| django_template            | 31.7 ms                                                | 32.9 ms: 1.04x slower                                               |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                               |
| spectral_norm              | 113 ms                                                 | 118 ms: 1.05x slower                                                |
| pidigits                   | 186 ms                                                 | 195 ms: 1.05x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.57 ms: 1.05x slower                                               |
| generators                 | 28.8 ms                                                | 30.3 ms: 1.05x slower                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.8 ms: 1.05x slower                                               |
| chaos                      | 58.0 ms                                                | 61.1 ms: 1.05x slower                                               |
| sympy_expand               | 456 ms                                                 | 481 ms: 1.05x slower                                                |
| coverage                   | 82.8 ms                                                | 88.0 ms: 1.06x slower                                               |
| crypto_pyaes               | 74.7 ms                                                | 80.0 ms: 1.07x slower                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 71.6 ms: 1.07x slower                                               |
| raytrace                   | 262 ms                                                 | 282 ms: 1.08x slower                                                |
| json_loads                 | 27.2 us                                                | 29.4 us: 1.08x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 175 us: 1.09x slower                                                |
| mako                       | 10.7 ms                                                | 11.7 ms: 1.09x slower                                               |
| unpickle_pure_python       | 213 us                                                 | 234 us: 1.10x slower                                                |
| bench_thread_pool          | 818 us                                                 | 900 us: 1.10x slower                                                |
| coroutines                 | 22.2 ms                                                | 24.5 ms: 1.10x slower                                               |
| pickle_pure_python         | 302 us                                                 | 335 us: 1.11x slower                                                |
| fannkuch                   | 394 ms                                                 | 437 ms: 1.11x slower                                                |
| deltablue                  | 3.19 ms                                                | 3.55 ms: 1.11x slower                                               |
| pprint_safe_repr           | 727 ms                                                 | 820 ms: 1.13x slower                                                |
| nbody                      | 87.7 ms                                                | 99.3 ms: 1.13x slower                                               |
| comprehensions             | 16.5 us                                                | 18.7 us: 1.13x slower                                               |
| pprint_pformat             | 1.48 sec                                               | 1.69 sec: 1.14x slower                                              |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.79 ms: 1.15x slower                                               |
| many_optionals             | 857 us                                                 | 994 us: 1.16x slower                                                |
| hexiom                     | 6.08 ms                                                | 7.08 ms: 1.17x slower                                               |
| json_dumps                 | 10.1 ms                                                | 12.1 ms: 1.20x slower                                               |
| subparsers                 | 15.5 ms                                                | 22.9 ms: 1.48x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 93.4 ms: 3.89x slower                                               |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (4): k_core, sphinx, scimark_sor, asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250508-3.14.0a7+-69dad45-JIT/bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 75.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x