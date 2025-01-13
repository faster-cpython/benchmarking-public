# Results vs. 3.13.0

- fork: kumaraditya303
- ref: per_thread_tasks
- machine: linux-x86_64
- commit hash: cca4057
- commit date: 2025-01-12
- overall geometric mean: 1.172x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 340 ms: 1.28x slower                                                       |
| docutils       | 2.58 sec                                               | 2.98 sec: 1.15x slower                                                     |
| html5lib       | 63.4 ms                                                | 85.1 ms: 1.34x slower                                                      |
| sphinx         | 1.03 sec                                               | 1.16 sec: 1.13x slower                                                     |
| Geometric mean | (ref)                                                  | 1.22x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 682 ms: 1.26x faster                                                       |
| async_tree_memoization_tg  | 463 ms                                                 | 387 ms: 1.20x faster                                                       |
| async_tree_io              | 838 ms                                                 | 733 ms: 1.14x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 294 ms: 1.09x faster                                                       |
| async_tree_none            | 350 ms                                                 | 344 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 536 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 583 ms: 1.02x slower                                                       |
| async_generators           | 433 ms                                                 | 486 ms: 1.12x slower                                                       |
| coroutines                 | 22.2 ms                                                | 25.5 ms: 1.15x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (2): async_tree_memoization, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                                       |
| float          | 78.7 ms                                                | 105 ms: 1.33x slower                                                       |
| nbody          | 87.7 ms                                                | 140 ms: 1.59x slower                                                       |
| Geometric mean | (ref)                                                  | 1.29x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.46 ms: 1.09x faster                                                      |
| regex_v8       | 26.9 ms                                                | 25.3 ms: 1.06x faster                                                      |
| regex_dna      | 220 ms                                                 | 222 ms: 1.01x slower                                                       |
| regex_compile  | 132 ms                                                 | 162 ms: 1.23x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 96.0 ms: 1.05x faster                                                      |
| xml_etree_parse      | 154 ms                                                 | 148 ms: 1.04x faster                                                       |
| json_loads           | 27.2 us                                                | 29.6 us: 1.09x slower                                                      |
| tomli_loads          | 2.12 sec                                               | 2.36 sec: 1.11x slower                                                     |
| xml_etree_generate   | 86.8 ms                                                | 96.9 ms: 1.12x slower                                                      |
| xml_etree_process    | 60.5 ms                                                | 73.2 ms: 1.21x slower                                                      |
| json_dumps           | 10.1 ms                                                | 13.3 ms: 1.32x slower                                                      |
| unpickle_pure_python | 213 us                                                 | 310 us: 1.45x slower                                                       |
| pickle_pure_python   | 302 us                                                 | 472 us: 1.56x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.18x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.5 ms: 1.23x slower                                                      |
| python_startup_no_site | 7.00 ms                                                | 9.62 ms: 1.37x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.30x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 62.7 ms: 1.24x slower                                                      |
| genshi_text     | 22.6 ms                                                | 30.2 ms: 1.33x slower                                                      |
| django_template | 31.7 ms                                                | 45.9 ms: 1.45x slower                                                      |
| mako            | 10.7 ms                                                | 18.2 ms: 1.70x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.42x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 3.77 ms: 1.30x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 682 ms: 1.26x faster                                                       |
| async_tree_memoization_tg  | 463 ms                                                 | 387 ms: 1.20x faster                                                       |
| async_tree_io              | 838 ms                                                 | 733 ms: 1.14x faster                                                       |
| deepcopy                   | 354 us                                                 | 315 us: 1.13x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.46 ms: 1.09x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 294 ms: 1.09x faster                                                       |
| regex_v8                   | 26.9 ms                                                | 25.3 ms: 1.06x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 96.0 ms: 1.05x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 148 ms: 1.04x faster                                                       |
| create_gc_cycles           | 2.45 ms                                                | 2.35 ms: 1.04x faster                                                      |
| async_tree_none            | 350 ms                                                 | 344 ms: 1.02x faster                                                       |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 536 ms: 1.01x faster                                                       |
| regex_dna                  | 220 ms                                                 | 222 ms: 1.01x slower                                                       |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 583 ms: 1.02x slower                                                       |
| deepcopy_reduce            | 3.24 us                                                | 3.32 us: 1.02x slower                                                      |
| k_core                     | 2.37 sec                                               | 2.47 sec: 1.04x slower                                                     |
| deepcopy_memo              | 38.4 us                                                | 40.4 us: 1.05x slower                                                      |
| spectral_norm              | 113 ms                                                 | 123 ms: 1.08x slower                                                       |
| pylint                     | 312 ms                                                 | 339 ms: 1.09x slower                                                       |
| json_loads                 | 27.2 us                                                | 29.6 us: 1.09x slower                                                      |
| telco                      | 8.40 ms                                                | 9.18 ms: 1.09x slower                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 5.21 sec: 1.11x slower                                                     |
| tomli_loads                | 2.12 sec                                               | 2.36 sec: 1.11x slower                                                     |
| xml_etree_generate         | 86.8 ms                                                | 96.9 ms: 1.12x slower                                                      |
| async_generators           | 433 ms                                                 | 486 ms: 1.12x slower                                                       |
| pycparser                  | 1.20 sec                                               | 1.35 sec: 1.12x slower                                                     |
| sphinx                     | 1.03 sec                                               | 1.16 sec: 1.13x slower                                                     |
| scimark_fft                | 367 ms                                                 | 418 ms: 1.14x slower                                                       |
| coroutines                 | 22.2 ms                                                | 25.5 ms: 1.15x slower                                                      |
| docutils                   | 2.58 sec                                               | 2.98 sec: 1.15x slower                                                     |
| mdp                        | 2.54 sec                                               | 2.93 sec: 1.15x slower                                                     |
| dulwich_log                | 64.6 ms                                                | 74.8 ms: 1.16x slower                                                      |
| shortest_path              | 487 ms                                                 | 573 ms: 1.18x slower                                                       |
| connected_components       | 447 ms                                                 | 531 ms: 1.19x slower                                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.02 ms: 1.20x slower                                                      |
| meteor_contest             | 108 ms                                                 | 130 ms: 1.20x slower                                                       |
| sqlglot_normalize          | 108 ms                                                 | 130 ms: 1.20x slower                                                       |
| sympy_expand               | 456 ms                                                 | 552 ms: 1.21x slower                                                       |
| xml_etree_process          | 60.5 ms                                                | 73.2 ms: 1.21x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 182 ms: 1.21x slower                                                       |
| nqueens                    | 80.9 ms                                                | 98.3 ms: 1.21x slower                                                      |
| sympy_str                  | 273 ms                                                 | 333 ms: 1.22x slower                                                       |
| sqlglot_optimize           | 53.4 ms                                                | 65.2 ms: 1.22x slower                                                      |
| crypto_pyaes               | 74.7 ms                                                | 91.3 ms: 1.22x slower                                                      |
| python_startup             | 12.7 ms                                                | 15.5 ms: 1.23x slower                                                      |
| regex_compile              | 132 ms                                                 | 162 ms: 1.23x slower                                                       |
| sympy_integrate            | 19.8 ms                                                | 24.4 ms: 1.23x slower                                                      |
| genshi_xml                 | 50.5 ms                                                | 62.7 ms: 1.24x slower                                                      |
| coverage                   | 82.8 ms                                                | 103 ms: 1.25x slower                                                       |
| thrift                     | 800 us                                                 | 1.02 ms: 1.27x slower                                                      |
| generators                 | 28.8 ms                                                | 36.7 ms: 1.28x slower                                                      |
| 2to3                       | 266 ms                                                 | 340 ms: 1.28x slower                                                       |
| fannkuch                   | 394 ms                                                 | 507 ms: 1.29x slower                                                       |
| typing_runtime_protocols   | 160 us                                                 | 207 us: 1.29x slower                                                       |
| richards                   | 47.5 ms                                                | 62.5 ms: 1.31x slower                                                      |
| pprint_safe_repr           | 727 ms                                                 | 955 ms: 1.32x slower                                                       |
| json_dumps                 | 10.1 ms                                                | 13.3 ms: 1.32x slower                                                      |
| many_optionals             | 857 us                                                 | 1.13 ms: 1.32x slower                                                      |
| pyflate                    | 470 ms                                                 | 621 ms: 1.32x slower                                                       |
| float                      | 78.7 ms                                                | 105 ms: 1.33x slower                                                       |
| genshi_text                | 22.6 ms                                                | 30.2 ms: 1.33x slower                                                      |
| pprint_pformat             | 1.48 sec                                               | 1.98 sec: 1.34x slower                                                     |
| html5lib                   | 63.4 ms                                                | 85.1 ms: 1.34x slower                                                      |
| richards_super             | 53.7 ms                                                | 72.4 ms: 1.35x slower                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 180 ms: 1.36x slower                                                       |
| python_startup_no_site     | 7.00 ms                                                | 9.62 ms: 1.37x slower                                                      |
| scimark_lu                 | 114 ms                                                 | 157 ms: 1.38x slower                                                       |
| logging_simple             | 5.65 us                                                | 7.81 us: 1.38x slower                                                      |
| sqlalchemy_imperative      | 16.9 ms                                                | 23.6 ms: 1.39x slower                                                      |
| logging_format             | 6.23 us                                                | 8.71 us: 1.40x slower                                                      |
| django_template            | 31.7 ms                                                | 45.9 ms: 1.45x slower                                                      |
| unpickle_pure_python       | 213 us                                                 | 310 us: 1.45x slower                                                       |
| hexiom                     | 6.08 ms                                                | 9.07 ms: 1.49x slower                                                      |
| scimark_sor                | 122 ms                                                 | 183 ms: 1.50x slower                                                       |
| go                         | 141 ms                                                 | 214 ms: 1.52x slower                                                       |
| comprehensions             | 16.5 us                                                | 25.3 us: 1.53x slower                                                      |
| scimark_monte_carlo        | 66.8 ms                                                | 103 ms: 1.54x slower                                                       |
| pickle_pure_python         | 302 us                                                 | 472 us: 1.56x slower                                                       |
| chaos                      | 58.0 ms                                                | 92.4 ms: 1.59x slower                                                      |
| nbody                      | 87.7 ms                                                | 140 ms: 1.59x slower                                                       |
| sqlglot_transpile          | 1.57 ms                                                | 2.56 ms: 1.63x slower                                                      |
| subparsers                 | 15.5 ms                                                | 26.3 ms: 1.70x slower                                                      |
| mako                       | 10.7 ms                                                | 18.2 ms: 1.70x slower                                                      |
| sqlglot_parse              | 1.26 ms                                                | 2.19 ms: 1.73x slower                                                      |
| logging_silent             | 101 ns                                                 | 179 ns: 1.77x slower                                                       |
| raytrace                   | 262 ms                                                 | 470 ms: 1.80x slower                                                       |
| deltablue                  | 3.19 ms                                                | 6.93 ms: 2.17x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 95.3 ms: 3.97x slower                                                      |
| bench_thread_pool          | 818 us                                                 | 3.55 ms: 4.34x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.24x slower                                                               |

Benchmark hidden because not significant (3): json, async_tree_memoization, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.172x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.15x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: 1.21x