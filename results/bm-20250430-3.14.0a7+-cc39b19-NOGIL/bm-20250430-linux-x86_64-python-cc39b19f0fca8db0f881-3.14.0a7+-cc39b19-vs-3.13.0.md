# Results vs. 3.13.0

- fork: python
- ref: cc39b19f0fca8db0f881
- machine: linux-x86_64
- commit hash: cc39b19
- commit date: 2025-04-30
- overall geometric mean: 1.043x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 292 ms: 1.10x slower                                                   |
| docutils       | 2.58 sec                                               | 2.78 sec: 1.08x slower                                                 |
| html5lib       | 63.4 ms                                                | 67.6 ms: 1.07x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.10 sec: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 514 ms: 1.68x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 294 ms: 1.57x faster                                                   |
| async_tree_io              | 838 ms                                                 | 548 ms: 1.53x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 228 ms: 1.40x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 330 ms: 1.32x faster                                                   |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 459 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 500 ms: 1.15x faster                                                   |
| async_generators           | 433 ms                                                 | 442 ms: 1.02x slower                                                   |
| coroutines                 | 22.2 ms                                                | 24.9 ms: 1.12x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.9 ms: 1.11x faster                                                  |
| pidigits       | 186 ms                                                 | 181 ms: 1.03x faster                                                   |
| nbody          | 87.7 ms                                                | 129 ms: 1.47x slower                                                   |
| Geometric mean | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.4 ms: 1.20x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.17 ms: 1.19x faster                                                  |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                   |
| regex_compile  | 132 ms                                                 | 145 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 97.6 ms: 1.04x faster                                                  |
| xml_etree_parse      | 154 ms                                                 | 150 ms: 1.03x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 2.24 sec: 1.06x slower                                                 |
| xml_etree_generate   | 86.8 ms                                                | 96.3 ms: 1.11x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 239 us: 1.12x slower                                                   |
| xml_etree_process    | 60.5 ms                                                | 68.1 ms: 1.13x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 345 us: 1.14x slower                                                   |
| json_loads           | 27.2 us                                                | 32.6 us: 1.20x slower                                                  |
| json_dumps           | 10.1 ms                                                | 13.1 ms: 1.29x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.5 ms: 1.22x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 9.12 ms: 1.30x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 59.5 ms: 1.18x slower                                                  |
| genshi_text     | 22.6 ms                                                | 27.3 ms: 1.21x slower                                                  |
| django_template | 31.7 ms                                                | 39.3 ms: 1.24x slower                                                  |
| mako            | 10.7 ms                                                | 16.2 ms: 1.51x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.28x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 2.29 ms: 2.14x faster                                                  |
| mdp                        | 2.54 sec                                               | 1.39 sec: 1.83x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 514 ms: 1.68x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 294 ms: 1.57x faster                                                   |
| async_tree_io              | 838 ms                                                 | 548 ms: 1.53x faster                                                   |
| create_gc_cycles           | 2.45 ms                                                | 1.69 ms: 1.45x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 228 ms: 1.40x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 330 ms: 1.32x faster                                                   |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 22.4 ms: 1.20x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.17 ms: 1.19x faster                                                  |
| deepcopy                   | 354 us                                                 | 298 us: 1.19x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 459 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 500 ms: 1.15x faster                                                   |
| float                      | 78.7 ms                                                | 70.9 ms: 1.11x faster                                                  |
| pylint                     | 312 ms                                                 | 293 ms: 1.06x faster                                                   |
| go                         | 141 ms                                                 | 133 ms: 1.06x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 36.4 us: 1.05x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 97.6 ms: 1.04x faster                                                  |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 62.4 ms: 1.03x faster                                                  |
| pidigits                   | 186 ms                                                 | 181 ms: 1.03x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 150 ms: 1.03x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 3.16 us: 1.02x faster                                                  |
| pathlib                    | 17.4 ms                                                | 17.5 ms: 1.01x slower                                                  |
| async_generators           | 433 ms                                                 | 442 ms: 1.02x slower                                                   |
| k_core                     | 2.37 sec                                               | 2.43 sec: 1.02x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.84 sec: 1.03x slower                                                 |
| spectral_norm              | 113 ms                                                 | 119 ms: 1.05x slower                                                   |
| tomli_loads                | 2.12 sec                                               | 2.24 sec: 1.06x slower                                                 |
| sphinx                     | 1.03 sec                                               | 1.10 sec: 1.06x slower                                                 |
| json                       | 5.32 ms                                                | 5.66 ms: 1.06x slower                                                  |
| generators                 | 28.8 ms                                                | 30.6 ms: 1.06x slower                                                  |
| richards                   | 47.5 ms                                                | 50.6 ms: 1.06x slower                                                  |
| html5lib                   | 63.4 ms                                                | 67.6 ms: 1.07x slower                                                  |
| pyflate                    | 470 ms                                                 | 503 ms: 1.07x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.78 sec: 1.08x slower                                                 |
| telco                      | 8.40 ms                                                | 9.08 ms: 1.08x slower                                                  |
| logging_silent             | 101 ns                                                 | 110 ns: 1.09x slower                                                   |
| 2to3                       | 266 ms                                                 | 292 ms: 1.10x slower                                                   |
| regex_compile              | 132 ms                                                 | 145 ms: 1.10x slower                                                   |
| xml_etree_generate         | 86.8 ms                                                | 96.3 ms: 1.11x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 806 ms: 1.11x slower                                                   |
| richards_super             | 53.7 ms                                                | 60.0 ms: 1.12x slower                                                  |
| sympy_str                  | 273 ms                                                 | 305 ms: 1.12x slower                                                   |
| coroutines                 | 22.2 ms                                                | 24.9 ms: 1.12x slower                                                  |
| scimark_fft                | 367 ms                                                 | 411 ms: 1.12x slower                                                   |
| unpickle_pure_python       | 213 us                                                 | 239 us: 1.12x slower                                                   |
| scimark_sor                | 122 ms                                                 | 137 ms: 1.12x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.67 sec: 1.13x slower                                                 |
| xml_etree_process          | 60.5 ms                                                | 68.1 ms: 1.13x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 22.3 ms: 1.13x slower                                                  |
| sympy_expand               | 456 ms                                                 | 516 ms: 1.13x slower                                                   |
| nqueens                    | 80.9 ms                                                | 91.7 ms: 1.13x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 171 ms: 1.14x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 345 us: 1.14x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.70 ms: 1.16x slower                                                  |
| logging_simple             | 5.65 us                                                | 6.58 us: 1.16x slower                                                  |
| chaos                      | 58.0 ms                                                | 67.7 ms: 1.17x slower                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.87 ms: 1.17x slower                                                  |
| shortest_path              | 487 ms                                                 | 568 ms: 1.17x slower                                                   |
| genshi_xml                 | 50.5 ms                                                | 59.5 ms: 1.18x slower                                                  |
| connected_components       | 447 ms                                                 | 527 ms: 1.18x slower                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 157 ms: 1.18x slower                                                   |
| logging_format             | 6.23 us                                                | 7.38 us: 1.18x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 89.4 ms: 1.20x slower                                                  |
| many_optionals             | 857 us                                                 | 1.03 ms: 1.20x slower                                                  |
| comprehensions             | 16.5 us                                                | 19.7 us: 1.20x slower                                                  |
| hexiom                     | 6.08 ms                                                | 7.29 ms: 1.20x slower                                                  |
| json_loads                 | 27.2 us                                                | 32.6 us: 1.20x slower                                                  |
| genshi_text                | 22.6 ms                                                | 27.3 ms: 1.21x slower                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 20.4 ms: 1.21x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 139 ms: 1.21x slower                                                   |
| meteor_contest             | 108 ms                                                 | 132 ms: 1.22x slower                                                   |
| python_startup             | 12.7 ms                                                | 15.5 ms: 1.22x slower                                                  |
| raytrace                   | 262 ms                                                 | 321 ms: 1.23x slower                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 82.8 ms: 1.24x slower                                                  |
| django_template            | 31.7 ms                                                | 39.3 ms: 1.24x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 202 us: 1.26x slower                                                   |
| fannkuch                   | 394 ms                                                 | 503 ms: 1.28x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 13.1 ms: 1.29x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 9.12 ms: 1.30x slower                                                  |
| nbody                      | 87.7 ms                                                | 129 ms: 1.47x slower                                                   |
| coverage                   | 82.8 ms                                                | 123 ms: 1.48x slower                                                   |
| mako                       | 10.7 ms                                                | 16.2 ms: 1.51x slower                                                  |
| subparsers                 | 15.5 ms                                                | 23.6 ms: 1.52x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 90.6 ms: 3.78x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 3.27 ms: 4.00x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x slower                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250430-3.14.0a7+-cc39b19-NOGIL/bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.043x slower

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.23x