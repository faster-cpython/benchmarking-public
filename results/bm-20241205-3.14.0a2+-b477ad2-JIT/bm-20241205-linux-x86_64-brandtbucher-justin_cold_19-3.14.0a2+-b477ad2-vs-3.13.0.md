# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_cold_19
- machine: linux-x86_64
- commit hash: b477ad2
- commit date: 2024-12-05
- overall geometric mean: 1.031x faster
- HPT reliability: 97.59%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                                   |
| docutils       | 2.58 sec                                               | 2.78 sec: 1.07x slower                                                 |
| html5lib       | 63.4 ms                                                | 64.2 ms: 1.01x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.07 sec: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.38x faster                                                   |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 342 ms: 1.28x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.14x faster                                                   |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                   |
| async_generators           | 433 ms                                                 | 452 ms: 1.04x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 75.8 ms: 1.04x faster                                                  |
| nbody          | 87.7 ms                                                | 86.0 ms: 1.02x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.25 ms: 1.16x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                  |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                   |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.12x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 78.5 ms: 1.11x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 54.7 ms: 1.11x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 1.92 sec: 1.10x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 195 us: 1.10x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 94.5 ms: 1.07x faster                                                  |
| json_loads           | 27.2 us                                                | 26.0 us: 1.04x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.04 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 9.98 ms: 1.07x faster                                                  |
| genshi_text     | 22.6 ms                                                | 24.1 ms: 1.07x slower                                                  |
| django_template | 31.7 ms                                                | 33.9 ms: 1.07x slower                                                  |
| genshi_xml      | 50.5 ms                                                | 57.1 ms: 1.13x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 626 ms: 1.38x faster                                                   |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                   |
| deepcopy                   | 354 us                                                 | 268 us: 1.32x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 29.1 us: 1.32x faster                                                  |
| richards                   | 47.5 ms                                                | 36.6 ms: 1.30x faster                                                  |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 342 ms: 1.28x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                   |
| richards_super             | 53.7 ms                                                | 43.1 ms: 1.25x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.25 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.14x faster                                                   |
| scimark_fft                | 367 ms                                                 | 325 ms: 1.13x faster                                                   |
| json                       | 5.32 ms                                                | 4.74 ms: 1.12x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.12x faster                                                   |
| telco                      | 8.40 ms                                                | 7.51 ms: 1.12x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 78.5 ms: 1.11x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 54.7 ms: 1.11x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.92 sec: 1.10x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 195 us: 1.10x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 68.5 ms: 1.09x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 94.5 ms: 1.07x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.38 sec: 1.07x faster                                                 |
| mako                       | 10.7 ms                                                | 9.98 ms: 1.07x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.3 ms: 1.07x faster                                                  |
| pylint                     | 312 ms                                                 | 294 ms: 1.06x faster                                                   |
| pyflate                    | 470 ms                                                 | 445 ms: 1.06x faster                                                   |
| go                         | 141 ms                                                 | 134 ms: 1.05x faster                                                   |
| json_loads                 | 27.2 us                                                | 26.0 us: 1.04x faster                                                  |
| connected_components       | 447 ms                                                 | 429 ms: 1.04x faster                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 64.2 ms: 1.04x faster                                                  |
| float                      | 78.7 ms                                                | 75.8 ms: 1.04x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                 |
| fannkuch                   | 394 ms                                                 | 381 ms: 1.03x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.74 ms: 1.03x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.82 us: 1.03x faster                                                  |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                                   |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                   |
| thrift                     | 800 us                                                 | 782 us: 1.02x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                   |
| nbody                      | 87.7 ms                                                | 86.0 ms: 1.02x faster                                                  |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                   |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                   |
| shortest_path              | 487 ms                                                 | 479 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 727 ms                                                 | 717 ms: 1.01x faster                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.44 ms: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                   |
| python_startup_no_site     | 7.00 ms                                                | 7.04 ms: 1.01x slower                                                  |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                   |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| logging_simple             | 5.65 us                                                | 5.73 us: 1.01x slower                                                  |
| html5lib                   | 63.4 ms                                                | 64.2 ms: 1.01x slower                                                  |
| logging_format             | 6.23 us                                                | 6.34 us: 1.02x slower                                                  |
| coverage                   | 82.8 ms                                                | 84.5 ms: 1.02x slower                                                  |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                                   |
| logging_silent             | 101 ns                                                 | 103 ns: 1.02x slower                                                   |
| djangocms                  | 22.3 us                                                | 22.8 us: 1.02x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                                   |
| chaos                      | 58.0 ms                                                | 60.1 ms: 1.04x slower                                                  |
| sympy_str                  | 273 ms                                                 | 283 ms: 1.04x slower                                                   |
| sqlglot_parse              | 1.26 ms                                                | 1.31 ms: 1.04x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.63 ms: 1.04x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.07 sec: 1.04x slower                                                 |
| sqlglot_optimize           | 53.4 ms                                                | 55.6 ms: 1.04x slower                                                  |
| async_generators           | 433 ms                                                 | 452 ms: 1.04x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.05x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 67.6 ms: 1.05x slower                                                  |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.05x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 20.7 ms: 1.05x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 171 us: 1.07x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                                   |
| genshi_text                | 22.6 ms                                                | 24.1 ms: 1.07x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 875 us: 1.07x slower                                                   |
| django_template            | 31.7 ms                                                | 33.9 ms: 1.07x slower                                                  |
| sympy_expand               | 456 ms                                                 | 490 ms: 1.07x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.78 sec: 1.07x slower                                                 |
| mdp                        | 2.54 sec                                               | 2.74 sec: 1.08x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                  |
| raytrace                   | 262 ms                                                 | 287 ms: 1.10x slower                                                   |
| nqueens                    | 80.9 ms                                                | 90.3 ms: 1.12x slower                                                  |
| genshi_xml                 | 50.5 ms                                                | 57.1 ms: 1.13x slower                                                  |
| many_optionals             | 857 us                                                 | 980 us: 1.14x slower                                                   |
| hexiom                     | 6.08 ms                                                | 7.04 ms: 1.16x slower                                                  |
| generators                 | 28.8 ms                                                | 36.4 ms: 1.27x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.3 ms: 3.39x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (6): pprint_pformat, scimark_sparse_mat_mult, deltablue, pycparser, scimark_lu, spectral_norm
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 97.59% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x