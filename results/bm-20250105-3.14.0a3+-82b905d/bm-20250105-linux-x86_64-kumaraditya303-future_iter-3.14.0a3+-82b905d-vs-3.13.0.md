# Results vs. 3.13.0

- fork: kumaraditya303
- ref: future_iter
- machine: linux-x86_64
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.037x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.04x faster                                                  |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                |
| html5lib       | 63.4 ms                                                | 62.4 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 301 ms: 1.54x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 594 ms: 1.45x faster                                                  |
| async_tree_io              | 838 ms                                                 | 588 ms: 1.43x faster                                                  |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 326 ms: 1.34x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 468 ms: 1.16x faster                                                  |
| async_generators           | 433 ms                                                 | 416 ms: 1.04x faster                                                  |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.05x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.5 ms: 1.08x faster                                                 |
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                                  |
| nbody          | 87.7 ms                                                | 94.1 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.47 ms: 1.09x faster                                                 |
| regex_v8       | 26.9 ms                                                | 26.1 ms: 1.03x faster                                                 |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                  |
| regex_dna      | 220 ms                                                 | 221 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.13x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 96.6 ms: 1.05x faster                                                 |
| json_loads           | 27.2 us                                                | 26.5 us: 1.03x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 85.1 ms: 1.02x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 59.5 ms: 1.02x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.05 ms: 1.01x slower                                                 |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.4 ms: 1.01x faster                                                 |
| django_template | 31.7 ms                                                | 31.5 ms: 1.01x faster                                                 |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 301 ms: 1.54x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 594 ms: 1.45x faster                                                  |
| async_tree_io              | 838 ms                                                 | 588 ms: 1.43x faster                                                  |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                                  |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 326 ms: 1.34x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                 |
| deepcopy_memo              | 38.4 us                                                | 31.5 us: 1.22x faster                                                 |
| go                         | 141 ms                                                 | 119 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 468 ms: 1.16x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.13x faster                                                  |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                  |
| spectral_norm              | 113 ms                                                 | 103 ms: 1.09x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.47 ms: 1.09x faster                                                 |
| float                      | 78.7 ms                                                | 72.5 ms: 1.08x faster                                                 |
| json                       | 5.32 ms                                                | 4.95 ms: 1.08x faster                                                 |
| telco                      | 8.40 ms                                                | 7.83 ms: 1.07x faster                                                 |
| richards                   | 47.5 ms                                                | 44.4 ms: 1.07x faster                                                 |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.07x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                |
| richards_super             | 53.7 ms                                                | 50.9 ms: 1.06x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.77 ms: 1.06x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 96.6 ms: 1.05x faster                                                 |
| scimark_fft                | 367 ms                                                 | 350 ms: 1.05x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 71.3 ms: 1.05x faster                                                 |
| generators                 | 28.8 ms                                                | 27.6 ms: 1.04x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                |
| async_generators           | 433 ms                                                 | 416 ms: 1.04x faster                                                  |
| 2to3                       | 266 ms                                                 | 257 ms: 1.04x faster                                                  |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.55 sec: 1.03x faster                                                |
| regex_v8                   | 26.9 ms                                                | 26.1 ms: 1.03x faster                                                 |
| json_loads                 | 27.2 us                                                | 26.5 us: 1.03x faster                                                 |
| thrift                     | 800 us                                                 | 780 us: 1.03x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.78 ms: 1.02x faster                                                 |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 85.1 ms: 1.02x faster                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 59.5 ms: 1.02x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                |
| html5lib                   | 63.4 ms                                                | 62.4 ms: 1.02x faster                                                 |
| connected_components       | 447 ms                                                 | 441 ms: 1.01x faster                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 52.6 ms: 1.01x faster                                                 |
| shortest_path              | 487 ms                                                 | 482 ms: 1.01x faster                                                  |
| genshi_text                | 22.6 ms                                                | 22.4 ms: 1.01x faster                                                 |
| sympy_str                  | 273 ms                                                 | 271 ms: 1.01x faster                                                  |
| nqueens                    | 80.9 ms                                                | 80.3 ms: 1.01x faster                                                 |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                 |
| dulwich_log                | 64.6 ms                                                | 64.2 ms: 1.01x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.01x faster                                                  |
| django_template            | 31.7 ms                                                | 31.5 ms: 1.01x faster                                                 |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.01x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 7.05 ms: 1.01x slower                                                 |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.01x slower                                                  |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.01x slower                                                  |
| logging_format             | 6.23 us                                                | 6.28 us: 1.01x slower                                                 |
| sympy_expand               | 456 ms                                                 | 460 ms: 1.01x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 20.0 ms: 1.01x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 734 ms: 1.01x slower                                                  |
| coverage                   | 82.8 ms                                                | 83.6 ms: 1.01x slower                                                 |
| pyflate                    | 470 ms                                                 | 474 ms: 1.01x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 68.0 ms: 1.02x slower                                                 |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                                  |
| logging_simple             | 5.65 us                                                | 5.76 us: 1.02x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.51 sec: 1.02x slower                                                |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                  |
| logging_silent             | 101 ns                                                 | 104 ns: 1.03x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.28 ms: 1.03x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                  |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                 |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                  |
| fannkuch                   | 394 ms                                                 | 410 ms: 1.04x slower                                                  |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.05x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.39 ms: 1.05x slower                                                 |
| mdp                        | 2.54 sec                                               | 2.68 sec: 1.05x slower                                                |
| chaos                      | 58.0 ms                                                | 61.2 ms: 1.05x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 869 us: 1.06x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                                  |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                 |
| nbody                      | 87.7 ms                                                | 94.1 ms: 1.07x slower                                                 |
| many_optionals             | 857 us                                                 | 947 us: 1.11x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                 |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 82.1 ms: 3.43x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (5): sphinx, genshi_xml, meteor_contest, create_gc_cycles, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250105-3.14.0a3+-82b905d/bm-20250105-linux-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d.json: mypy2

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x