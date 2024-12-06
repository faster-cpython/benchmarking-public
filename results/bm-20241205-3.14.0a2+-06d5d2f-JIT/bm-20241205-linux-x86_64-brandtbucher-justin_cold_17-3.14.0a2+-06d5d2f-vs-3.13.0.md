# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_cold_17
- machine: linux-x86_64
- commit hash: 06d5d2f
- commit date: 2024-12-05
- overall geometric mean: 1.033x faster
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.03x faster                                                   |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.05x slower                                                 |
| html5lib       | 63.4 ms                                                | 63.8 ms: 1.01x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 272 ms: 1.29x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 342 ms: 1.28x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                   |
| async_generators           | 433 ms                                                 | 446 ms: 1.03x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 87.7 ms                                                | 83.1 ms: 1.05x faster                                                  |
| float          | 78.7 ms                                                | 75.5 ms: 1.04x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.43 ms: 1.10x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                  |
| regex_dna      | 220 ms                                                 | 213 ms: 1.03x faster                                                   |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.13x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 78.5 ms: 1.11x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 1.92 sec: 1.10x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 55.0 ms: 1.10x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 194 us: 1.10x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 94.8 ms: 1.07x faster                                                  |
| json_loads           | 27.2 us                                                | 26.1 us: 1.04x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.0 ms: 1.06x faster                                                  |
| genshi_text     | 22.6 ms                                                | 24.1 ms: 1.06x slower                                                  |
| django_template | 31.7 ms                                                | 33.9 ms: 1.07x slower                                                  |
| genshi_xml      | 50.5 ms                                                | 58.2 ms: 1.15x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_17-3.14.0a2+-06d5d2f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 28.8 us: 1.33x faster                                                  |
| deepcopy                   | 354 us                                                 | 268 us: 1.32x faster                                                   |
| richards                   | 47.5 ms                                                | 36.6 ms: 1.30x faster                                                  |
| async_tree_none            | 350 ms                                                 | 272 ms: 1.29x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 342 ms: 1.28x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                   |
| richards_super             | 53.7 ms                                                | 43.5 ms: 1.24x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.75 us: 1.18x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.13x faster                                                   |
| scimark_fft                | 367 ms                                                 | 326 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                   |
| telco                      | 8.40 ms                                                | 7.52 ms: 1.12x faster                                                  |
| json                       | 5.32 ms                                                | 4.78 ms: 1.11x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 78.5 ms: 1.11x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.92 sec: 1.10x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 55.0 ms: 1.10x faster                                                  |
| unpickle_pure_python       | 213 us                                                 | 194 us: 1.10x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.43 ms: 1.10x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 68.6 ms: 1.09x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.38 sec: 1.07x faster                                                 |
| pylint                     | 312 ms                                                 | 292 ms: 1.07x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 94.8 ms: 1.07x faster                                                  |
| mako                       | 10.7 ms                                                | 10.0 ms: 1.06x faster                                                  |
| go                         | 141 ms                                                 | 132 ms: 1.06x faster                                                   |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                                  |
| nbody                      | 87.7 ms                                                | 83.1 ms: 1.05x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                                  |
| float                      | 78.7 ms                                                | 75.5 ms: 1.04x faster                                                  |
| json_loads                 | 27.2 us                                                | 26.1 us: 1.04x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.84 ms: 1.04x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                 |
| regex_dna                  | 220 ms                                                 | 213 ms: 1.03x faster                                                   |
| 2to3                       | 266 ms                                                 | 257 ms: 1.03x faster                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 64.8 ms: 1.03x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                   |
| pprint_safe_repr           | 727 ms                                                 | 708 ms: 1.03x faster                                                   |
| pyflate                    | 470 ms                                                 | 458 ms: 1.03x faster                                                   |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                   |
| connected_components       | 447 ms                                                 | 437 ms: 1.02x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.32 sec: 1.02x faster                                                 |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                                 |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                  |
| fannkuch                   | 394 ms                                                 | 388 ms: 1.02x faster                                                   |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.01x faster                                                   |
| logging_silent             | 101 ns                                                 | 99.8 ns: 1.01x faster                                                  |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| thrift                     | 800 us                                                 | 792 us: 1.01x faster                                                   |
| shortest_path              | 487 ms                                                 | 483 ms: 1.01x faster                                                   |
| deltablue                  | 3.19 ms                                                | 3.17 ms: 1.01x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.88 ms: 1.00x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| html5lib                   | 63.4 ms                                                | 63.8 ms: 1.01x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                  |
| chaos                      | 58.0 ms                                                | 58.6 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| coverage                   | 82.8 ms                                                | 83.9 ms: 1.01x slower                                                  |
| logging_simple             | 5.65 us                                                | 5.74 us: 1.02x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                 |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                                   |
| async_generators           | 433 ms                                                 | 446 ms: 1.03x slower                                                   |
| sympy_str                  | 273 ms                                                 | 282 ms: 1.03x slower                                                   |
| sqlglot_transpile          | 1.57 ms                                                | 1.63 ms: 1.04x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                                   |
| sqlglot_parse              | 1.26 ms                                                | 1.31 ms: 1.04x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 20.6 ms: 1.04x slower                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 55.7 ms: 1.04x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 67.4 ms: 1.04x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.05x slower                                                 |
| sympy_expand               | 456 ms                                                 | 477 ms: 1.05x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.3 us: 1.05x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                   |
| genshi_text                | 22.6 ms                                                | 24.1 ms: 1.06x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 873 us: 1.07x slower                                                   |
| django_template            | 31.7 ms                                                | 33.9 ms: 1.07x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.75 sec: 1.08x slower                                                 |
| raytrace                   | 262 ms                                                 | 283 ms: 1.08x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.10x slower                                                  |
| nqueens                    | 80.9 ms                                                | 90.9 ms: 1.12x slower                                                  |
| many_optionals             | 857 us                                                 | 970 us: 1.13x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.99 ms: 1.15x slower                                                  |
| genshi_xml                 | 50.5 ms                                                | 58.2 ms: 1.15x slower                                                  |
| generators                 | 28.8 ms                                                | 36.2 ms: 1.26x slower                                                  |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.3 ms: 3.39x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (4): spectral_norm, asyncio_websockets, logging_format, djangocms
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 99.75% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x