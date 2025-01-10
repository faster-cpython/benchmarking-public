# Results vs. 3.13.0

- fork: kumaraditya303
- ref: current_task
- machine: linux-x86_64
- commit hash: b20a605
- commit date: 2025-01-02
- overall geometric mean: 1.178x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 346 ms: 1.30x slower                                                   |
| docutils       | 2.58 sec                                               | 2.96 sec: 1.15x slower                                                 |
| html5lib       | 63.4 ms                                                | 87.3 ms: 1.38x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.16 sec: 1.12x slower                                                 |
| Geometric mean | (ref)                                                  | 1.23x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 680 ms: 1.27x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 383 ms: 1.21x faster                                                   |
| async_tree_io              | 838 ms                                                 | 724 ms: 1.16x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 291 ms: 1.10x faster                                                   |
| async_tree_none            | 350 ms                                                 | 335 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 529 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 578 ms: 1.01x slower                                                   |
| async_generators           | 433 ms                                                 | 497 ms: 1.15x slower                                                   |
| coroutines                 | 22.2 ms                                                | 26.7 ms: 1.20x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (2): async_tree_memoization, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 181 ms: 1.03x faster                                                   |
| float          | 78.7 ms                                                | 107 ms: 1.36x slower                                                   |
| nbody          | 87.7 ms                                                | 135 ms: 1.54x slower                                                   |
| Geometric mean | (ref)                                                  | 1.27x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.33 ms: 1.13x faster                                                  |
| regex_v8       | 26.9 ms                                                | 26.2 ms: 1.03x faster                                                  |
| regex_dna      | 220 ms                                                 | 226 ms: 1.03x slower                                                   |
| regex_compile  | 132 ms                                                 | 164 ms: 1.24x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 96.2 ms: 1.05x faster                                                  |
| xml_etree_parse      | 154 ms                                                 | 149 ms: 1.03x faster                                                   |
| json_loads           | 27.2 us                                                | 29.4 us: 1.08x slower                                                  |
| xml_etree_generate   | 86.8 ms                                                | 96.2 ms: 1.11x slower                                                  |
| tomli_loads          | 2.12 sec                                               | 2.48 sec: 1.17x slower                                                 |
| xml_etree_process    | 60.5 ms                                                | 72.4 ms: 1.20x slower                                                  |
| json_dumps           | 10.1 ms                                                | 13.2 ms: 1.30x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 313 us: 1.47x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 475 us: 1.57x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.19x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.5 ms: 1.23x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 9.60 ms: 1.37x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.30x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 63.1 ms: 1.25x slower                                                  |
| genshi_text     | 22.6 ms                                                | 30.3 ms: 1.34x slower                                                  |
| django_template | 31.7 ms                                                | 46.9 ms: 1.48x slower                                                  |
| mako            | 10.7 ms                                                | 18.2 ms: 1.70x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.43x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 3.67 ms: 1.33x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 680 ms: 1.27x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 383 ms: 1.21x faster                                                   |
| async_tree_io              | 838 ms                                                 | 724 ms: 1.16x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.33 ms: 1.13x faster                                                  |
| deepcopy                   | 354 us                                                 | 316 us: 1.12x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 291 ms: 1.10x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 96.2 ms: 1.05x faster                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.34 ms: 1.05x faster                                                  |
| async_tree_none            | 350 ms                                                 | 335 ms: 1.05x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 149 ms: 1.03x faster                                                   |
| pidigits                   | 186 ms                                                 | 181 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 529 ms: 1.03x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 26.2 ms: 1.03x faster                                                  |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.84 us: 1.02x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 578 ms: 1.01x slower                                                   |
| regex_dna                  | 220 ms                                                 | 226 ms: 1.03x slower                                                   |
| deepcopy_reduce            | 3.24 us                                                | 3.36 us: 1.04x slower                                                  |
| deepcopy_memo              | 38.4 us                                                | 40.2 us: 1.05x slower                                                  |
| k_core                     | 2.37 sec                                               | 2.50 sec: 1.06x slower                                                 |
| json_loads                 | 27.2 us                                                | 29.4 us: 1.08x slower                                                  |
| telco                      | 8.40 ms                                                | 9.14 ms: 1.09x slower                                                  |
| pylint                     | 312 ms                                                 | 340 ms: 1.09x slower                                                   |
| spectral_norm              | 113 ms                                                 | 125 ms: 1.10x slower                                                   |
| xml_etree_generate         | 86.8 ms                                                | 96.2 ms: 1.11x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.16 sec: 1.12x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 5.29 sec: 1.13x slower                                                 |
| pycparser                  | 1.20 sec                                               | 1.36 sec: 1.13x slower                                                 |
| scimark_fft                | 367 ms                                                 | 419 ms: 1.14x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.96 sec: 1.15x slower                                                 |
| async_generators           | 433 ms                                                 | 497 ms: 1.15x slower                                                   |
| dulwich_log                | 64.6 ms                                                | 75.1 ms: 1.16x slower                                                  |
| tomli_loads                | 2.12 sec                                               | 2.48 sec: 1.17x slower                                                 |
| shortest_path              | 487 ms                                                 | 579 ms: 1.19x slower                                                   |
| mdp                        | 2.54 sec                                               | 3.03 sec: 1.19x slower                                                 |
| sqlglot_normalize          | 108 ms                                                 | 129 ms: 1.19x slower                                                   |
| xml_etree_process          | 60.5 ms                                                | 72.4 ms: 1.20x slower                                                  |
| coroutines                 | 22.2 ms                                                | 26.7 ms: 1.20x slower                                                  |
| connected_components       | 447 ms                                                 | 539 ms: 1.21x slower                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.08 ms: 1.21x slower                                                  |
| meteor_contest             | 108 ms                                                 | 131 ms: 1.21x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 183 ms: 1.21x slower                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 64.9 ms: 1.22x slower                                                  |
| sympy_expand               | 456 ms                                                 | 556 ms: 1.22x slower                                                   |
| sympy_str                  | 273 ms                                                 | 334 ms: 1.22x slower                                                   |
| python_startup             | 12.7 ms                                                | 15.5 ms: 1.23x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 91.9 ms: 1.23x slower                                                  |
| coverage                   | 82.8 ms                                                | 102 ms: 1.23x slower                                                   |
| sympy_integrate            | 19.8 ms                                                | 24.5 ms: 1.24x slower                                                  |
| nqueens                    | 80.9 ms                                                | 100 ms: 1.24x slower                                                   |
| regex_compile              | 132 ms                                                 | 164 ms: 1.24x slower                                                   |
| genshi_xml                 | 50.5 ms                                                | 63.1 ms: 1.25x slower                                                  |
| thrift                     | 800 us                                                 | 1.01 ms: 1.27x slower                                                  |
| generators                 | 28.8 ms                                                | 36.9 ms: 1.28x slower                                                  |
| 2to3                       | 266 ms                                                 | 346 ms: 1.30x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 13.2 ms: 1.30x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 208 us: 1.30x slower                                                   |
| richards                   | 47.5 ms                                                | 62.5 ms: 1.31x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 958 ms: 1.32x slower                                                   |
| many_optionals             | 857 us                                                 | 1.13 ms: 1.32x slower                                                  |
| fannkuch                   | 394 ms                                                 | 525 ms: 1.33x slower                                                   |
| genshi_text                | 22.6 ms                                                | 30.3 ms: 1.34x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 155 ms: 1.35x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 2.00 sec: 1.35x slower                                                 |
| float                      | 78.7 ms                                                | 107 ms: 1.36x slower                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 181 ms: 1.36x slower                                                   |
| python_startup_no_site     | 7.00 ms                                                | 9.60 ms: 1.37x slower                                                  |
| richards_super             | 53.7 ms                                                | 73.9 ms: 1.37x slower                                                  |
| html5lib                   | 63.4 ms                                                | 87.3 ms: 1.38x slower                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 23.4 ms: 1.39x slower                                                  |
| logging_simple             | 5.65 us                                                | 7.84 us: 1.39x slower                                                  |
| pyflate                    | 470 ms                                                 | 659 ms: 1.40x slower                                                   |
| logging_format             | 6.23 us                                                | 8.79 us: 1.41x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 313 us: 1.47x slower                                                   |
| django_template            | 31.7 ms                                                | 46.9 ms: 1.48x slower                                                  |
| comprehensions             | 16.5 us                                                | 25.4 us: 1.54x slower                                                  |
| nbody                      | 87.7 ms                                                | 135 ms: 1.54x slower                                                   |
| hexiom                     | 6.08 ms                                                | 9.49 ms: 1.56x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 475 us: 1.57x slower                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 105 ms: 1.58x slower                                                   |
| go                         | 141 ms                                                 | 222 ms: 1.58x slower                                                   |
| chaos                      | 58.0 ms                                                | 93.4 ms: 1.61x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 2.54 ms: 1.62x slower                                                  |
| mako                       | 10.7 ms                                                | 18.2 ms: 1.70x slower                                                  |
| subparsers                 | 15.5 ms                                                | 26.6 ms: 1.72x slower                                                  |
| scimark_sor                | 122 ms                                                 | 211 ms: 1.73x slower                                                   |
| logging_silent             | 101 ns                                                 | 175 ns: 1.73x slower                                                   |
| sqlglot_parse              | 1.26 ms                                                | 2.19 ms: 1.73x slower                                                  |
| raytrace                   | 262 ms                                                 | 471 ms: 1.80x slower                                                   |
| deltablue                  | 3.19 ms                                                | 7.04 ms: 2.21x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 95.3 ms: 3.97x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 3.56 ms: 4.36x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.25x slower                                                           |

Benchmark hidden because not significant (3): async_tree_memoization, json, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.178x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.15x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: 1.21x