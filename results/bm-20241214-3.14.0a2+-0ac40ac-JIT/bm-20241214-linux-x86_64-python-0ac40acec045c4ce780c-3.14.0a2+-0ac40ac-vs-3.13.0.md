# Results vs. 3.13.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.033x faster
- HPT reliability: 95.68%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.02x faster                                                   |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                 |
| html5lib       | 63.4 ms                                                | 65.3 ms: 1.03x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.06 sec: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 627 ms: 1.37x faster                                                   |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 336 ms: 1.30x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                   |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                   |
| async_generators           | 433 ms                                                 | 446 ms: 1.03x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 73.3 ms: 1.07x faster                                                  |
| nbody          | 87.7 ms                                                | 82.6 ms: 1.06x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.24 ms: 1.16x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.7 ms: 1.09x faster                                                  |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.85 sec: 1.15x faster                                                 |
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.12x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 78.3 ms: 1.11x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 193 us: 1.10x faster                                                   |
| xml_etree_process    | 60.5 ms                                                | 55.7 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 94.5 ms: 1.07x faster                                                  |
| json_loads           | 27.2 us                                                | 26.0 us: 1.04x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.3 ms: 1.04x faster                                                  |
| genshi_text     | 22.6 ms                                                | 23.8 ms: 1.05x slower                                                  |
| django_template | 31.7 ms                                                | 33.9 ms: 1.07x slower                                                  |
| genshi_xml      | 50.5 ms                                                | 58.6 ms: 1.16x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 627 ms: 1.37x faster                                                   |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                   |
| deepcopy                   | 354 us                                                 | 270 us: 1.31x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 336 ms: 1.30x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 29.8 us: 1.29x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.76 us: 1.17x faster                                                  |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.24 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.15x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.15x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.12x faster                                                   |
| go                         | 141 ms                                                 | 125 ms: 1.12x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 78.3 ms: 1.11x faster                                                  |
| telco                      | 8.40 ms                                                | 7.59 ms: 1.11x faster                                                  |
| json                       | 5.32 ms                                                | 4.81 ms: 1.11x faster                                                  |
| unpickle_pure_python       | 213 us                                                 | 193 us: 1.10x faster                                                   |
| spectral_norm              | 113 ms                                                 | 103 ms: 1.10x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 68.0 ms: 1.10x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 24.7 ms: 1.09x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 55.7 ms: 1.09x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 62.0 ms: 1.08x faster                                                  |
| pylint                     | 312 ms                                                 | 290 ms: 1.08x faster                                                   |
| float                      | 78.7 ms                                                | 73.3 ms: 1.07x faster                                                  |
| scimark_sor                | 122 ms                                                 | 114 ms: 1.07x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 94.5 ms: 1.07x faster                                                  |
| richards                   | 47.5 ms                                                | 44.7 ms: 1.06x faster                                                  |
| nbody                      | 87.7 ms                                                | 82.6 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.74 ms: 1.06x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.43 sec: 1.06x faster                                                 |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                                  |
| richards_super             | 53.7 ms                                                | 51.4 ms: 1.05x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                                  |
| json_loads                 | 27.2 us                                                | 26.0 us: 1.04x faster                                                  |
| thrift                     | 800 us                                                 | 769 us: 1.04x faster                                                   |
| pyflate                    | 470 ms                                                 | 452 ms: 1.04x faster                                                   |
| mako                       | 10.7 ms                                                | 10.3 ms: 1.04x faster                                                  |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                   |
| 2to3                       | 266 ms                                                 | 259 ms: 1.02x faster                                                   |
| fannkuch                   | 394 ms                                                 | 385 ms: 1.02x faster                                                   |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                 |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                                  |
| shortest_path              | 487 ms                                                 | 481 ms: 1.01x faster                                                   |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x faster                                                   |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| logging_format             | 6.23 us                                                | 6.27 us: 1.01x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                   |
| logging_simple             | 5.65 us                                                | 5.71 us: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.28 ms: 1.01x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 4.95 ms: 1.01x slower                                                  |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.01x slower                                                 |
| coverage                   | 82.8 ms                                                | 84.1 ms: 1.02x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.61 ms: 1.02x slower                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 54.8 ms: 1.03x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.06 sec: 1.03x slower                                                 |
| async_generators           | 433 ms                                                 | 446 ms: 1.03x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.29 ms: 1.03x slower                                                  |
| html5lib                   | 63.4 ms                                                | 65.3 ms: 1.03x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 752 ms: 1.04x slower                                                   |
| dulwich_log                | 64.6 ms                                                | 66.9 ms: 1.04x slower                                                  |
| sympy_str                  | 273 ms                                                 | 283 ms: 1.04x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.04x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                 |
| sympy_integrate            | 19.8 ms                                                | 20.8 ms: 1.05x slower                                                  |
| sympy_expand               | 456 ms                                                 | 478 ms: 1.05x slower                                                   |
| genshi_text                | 22.6 ms                                                | 23.8 ms: 1.05x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.69 sec: 1.06x slower                                                 |
| chaos                      | 58.0 ms                                                | 61.5 ms: 1.06x slower                                                  |
| logging_silent             | 101 ns                                                 | 107 ns: 1.06x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                                   |
| django_template            | 31.7 ms                                                | 33.9 ms: 1.07x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 887 us: 1.08x slower                                                   |
| raytrace                   | 262 ms                                                 | 284 ms: 1.08x slower                                                   |
| nqueens                    | 80.9 ms                                                | 89.1 ms: 1.10x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.12x slower                                                  |
| many_optionals             | 857 us                                                 | 985 us: 1.15x slower                                                   |
| hexiom                     | 6.08 ms                                                | 7.03 ms: 1.16x slower                                                  |
| genshi_xml                 | 50.5 ms                                                | 58.6 ms: 1.16x slower                                                  |
| generators                 | 28.8 ms                                                | 34.6 ms: 1.20x slower                                                  |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.39x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (3): regex_dna, djangocms, scimark_lu
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: mypy2

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 95.68% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x