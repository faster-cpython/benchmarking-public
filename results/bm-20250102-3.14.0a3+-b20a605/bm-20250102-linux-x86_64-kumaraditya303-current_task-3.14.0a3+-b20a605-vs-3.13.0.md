# Results vs. 3.13.0

- fork: kumaraditya303
- ref: current_task
- machine: linux-x86_64
- commit hash: b20a605
- commit date: 2025-01-02
- overall geometric mean: 1.044x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                   |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                 |
| html5lib       | 63.4 ms                                                | 62.4 ms: 1.02x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 300 ms: 1.54x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 587 ms: 1.47x faster                                                   |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 242 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 475 ms: 1.14x faster                                                   |
| async_generators           | 433 ms                                                 | 422 ms: 1.03x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.8 ms: 1.08x faster                                                  |
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                                   |
| nbody          | 87.7 ms                                                | 94.7 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                  |
| regex_v8       | 26.9 ms                                                | 25.3 ms: 1.06x faster                                                  |
| regex_dna      | 220 ms                                                 | 213 ms: 1.03x faster                                                   |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.99 sec: 1.07x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 96.8 ms: 1.05x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 58.5 ms: 1.03x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 84.1 ms: 1.03x faster                                                  |
| json_loads           | 27.2 us                                                | 26.4 us: 1.03x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 31.7 ms                                                | 31.3 ms: 1.01x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 50.0 ms: 1.01x faster                                                  |
| genshi_text     | 22.6 ms                                                | 22.4 ms: 1.01x faster                                                  |
| mako            | 10.7 ms                                                | 11.7 ms: 1.10x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 300 ms: 1.54x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 587 ms: 1.47x faster                                                   |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                                   |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 242 ms: 1.32x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 31.1 us: 1.23x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.64 us: 1.23x faster                                                  |
| go                         | 141 ms                                                 | 119 ms: 1.18x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 475 ms: 1.14x faster                                                   |
| pylint                     | 312 ms                                                 | 277 ms: 1.13x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                   |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.09x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 68.8 ms: 1.09x faster                                                  |
| float                      | 78.7 ms                                                | 72.8 ms: 1.08x faster                                                  |
| json                       | 5.32 ms                                                | 4.95 ms: 1.08x faster                                                  |
| telco                      | 8.40 ms                                                | 7.84 ms: 1.07x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.07x faster                                                  |
| richards                   | 47.5 ms                                                | 44.5 ms: 1.07x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.99 sec: 1.07x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 25.3 ms: 1.06x faster                                                  |
| richards_super             | 53.7 ms                                                | 50.6 ms: 1.06x faster                                                  |
| pyflate                    | 470 ms                                                 | 444 ms: 1.06x faster                                                   |
| thrift                     | 800 us                                                 | 758 us: 1.06x faster                                                   |
| scimark_fft                | 367 ms                                                 | 350 ms: 1.05x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 96.8 ms: 1.05x faster                                                  |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.84 ms: 1.04x faster                                                  |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 58.5 ms: 1.03x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 84.1 ms: 1.03x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.55 sec: 1.03x faster                                                 |
| regex_dna                  | 220 ms                                                 | 213 ms: 1.03x faster                                                   |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                   |
| json_loads                 | 27.2 us                                                | 26.4 us: 1.03x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.76 ms: 1.03x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                   |
| connected_components       | 447 ms                                                 | 435 ms: 1.03x faster                                                   |
| async_generators           | 433 ms                                                 | 422 ms: 1.03x faster                                                   |
| generators                 | 28.8 ms                                                | 28.0 ms: 1.03x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                 |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                  |
| shortest_path              | 487 ms                                                 | 477 ms: 1.02x faster                                                   |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                   |
| html5lib                   | 63.4 ms                                                | 62.4 ms: 1.02x faster                                                  |
| nqueens                    | 80.9 ms                                                | 79.6 ms: 1.02x faster                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 52.6 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 727 ms                                                 | 716 ms: 1.01x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 63.8 ms: 1.01x faster                                                  |
| django_template            | 31.7 ms                                                | 31.3 ms: 1.01x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 50.0 ms: 1.01x faster                                                  |
| genshi_text                | 22.6 ms                                                | 22.4 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.01x faster                                                 |
| coverage                   | 82.8 ms                                                | 82.4 ms: 1.01x faster                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.44 ms: 1.01x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.00x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.00x slower                                                  |
| fannkuch                   | 394 ms                                                 | 395 ms: 1.00x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 67.3 ms: 1.01x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                                   |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                                   |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.28 ms: 1.03x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.28 ms: 1.03x slower                                                  |
| chaos                      | 58.0 ms                                                | 60.2 ms: 1.04x slower                                                  |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                                  |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.05x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.67 sec: 1.05x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 868 us: 1.06x slower                                                   |
| logging_silent             | 101 ns                                                 | 107 ns: 1.06x slower                                                   |
| nbody                      | 87.7 ms                                                | 94.7 ms: 1.08x slower                                                  |
| mako                       | 10.7 ms                                                | 11.7 ms: 1.10x slower                                                  |
| many_optionals             | 857 us                                                 | 952 us: 1.11x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.34x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (7): logging_format, logging_simple, meteor_contest, sympy_expand, asyncio_websockets, scimark_sor, djangocms
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x