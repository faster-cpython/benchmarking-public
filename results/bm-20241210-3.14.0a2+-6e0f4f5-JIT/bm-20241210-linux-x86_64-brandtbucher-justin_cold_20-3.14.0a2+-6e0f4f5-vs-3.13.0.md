# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_cold_20
- machine: linux-x86_64
- commit hash: 6e0f4f5
- commit date: 2024-12-10
- overall geometric mean: 1.033x faster
- HPT reliability: 99.19%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                   |
| docutils       | 2.58 sec                                               | 2.79 sec: 1.08x slower                                                 |
| html5lib       | 63.4 ms                                                | 64.6 ms: 1.02x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.08 sec: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                                   |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                   |
| async_tree_none            | 350 ms                                                 | 272 ms: 1.29x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 342 ms: 1.28x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                   |
| async_generators           | 433 ms                                                 | 446 ms: 1.03x slower                                                   |
| coroutines                 | 22.2 ms                                                | 22.9 ms: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 75.3 ms: 1.05x faster                                                  |
| nbody          | 87.7 ms                                                | 84.4 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.46 ms: 1.09x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.7 ms: 1.09x faster                                                  |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                   |
| regex_dna      | 220 ms                                                 | 222 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.13x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 77.7 ms: 1.12x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 193 us: 1.10x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.92 sec: 1.10x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 54.9 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 94.7 ms: 1.07x faster                                                  |
| json_loads           | 27.2 us                                                | 26.2 us: 1.04x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 324 us: 1.07x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                  |
| genshi_text     | 22.6 ms                                                | 23.8 ms: 1.05x slower                                                  |
| django_template | 31.7 ms                                                | 33.6 ms: 1.06x slower                                                  |
| genshi_xml      | 50.5 ms                                                | 56.9 ms: 1.13x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 611 ms: 1.41x faster                                                   |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                  |
| async_tree_none            | 350 ms                                                 | 272 ms: 1.29x faster                                                   |
| deepcopy                   | 354 us                                                 | 276 us: 1.28x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 342 ms: 1.28x faster                                                   |
| richards                   | 47.5 ms                                                | 37.5 ms: 1.27x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                   |
| richards_super             | 53.7 ms                                                | 43.4 ms: 1.24x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.75 us: 1.18x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 498 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.13x faster                                                   |
| scimark_fft                | 367 ms                                                 | 328 ms: 1.12x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 77.7 ms: 1.12x faster                                                  |
| telco                      | 8.40 ms                                                | 7.52 ms: 1.12x faster                                                  |
| json                       | 5.32 ms                                                | 4.80 ms: 1.11x faster                                                  |
| unpickle_pure_python       | 213 us                                                 | 193 us: 1.10x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.92 sec: 1.10x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 54.9 ms: 1.10x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.46 ms: 1.09x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 24.7 ms: 1.09x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.07x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 94.7 ms: 1.07x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.40 sec: 1.07x faster                                                 |
| crypto_pyaes               | 74.7 ms                                                | 70.2 ms: 1.06x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                 |
| pylint                     | 312 ms                                                 | 295 ms: 1.06x faster                                                   |
| mako                       | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                  |
| go                         | 141 ms                                                 | 134 ms: 1.05x faster                                                   |
| float                      | 78.7 ms                                                | 75.3 ms: 1.05x faster                                                  |
| connected_components       | 447 ms                                                 | 429 ms: 1.04x faster                                                   |
| pyflate                    | 470 ms                                                 | 452 ms: 1.04x faster                                                   |
| nbody                      | 87.7 ms                                                | 84.4 ms: 1.04x faster                                                  |
| json_loads                 | 27.2 us                                                | 26.2 us: 1.04x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 64.6 ms: 1.03x faster                                                  |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                 |
| thrift                     | 800 us                                                 | 775 us: 1.03x faster                                                   |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.82 us: 1.03x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.91 ms: 1.02x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.78 ms: 1.02x faster                                                  |
| fannkuch                   | 394 ms                                                 | 385 ms: 1.02x faster                                                   |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                   |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| shortest_path              | 487 ms                                                 | 480 ms: 1.01x faster                                                   |
| pprint_safe_repr           | 727 ms                                                 | 718 ms: 1.01x faster                                                   |
| logging_silent             | 101 ns                                                 | 99.9 ns: 1.01x faster                                                  |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.01x faster                                                   |
| deltablue                  | 3.19 ms                                                | 3.16 ms: 1.01x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                  |
| spectral_norm              | 113 ms                                                 | 113 ms: 1.00x faster                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.01x slower                                                  |
| regex_dna                  | 220 ms                                                 | 222 ms: 1.01x slower                                                   |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| coverage                   | 82.8 ms                                                | 83.7 ms: 1.01x slower                                                  |
| logging_simple             | 5.65 us                                                | 5.73 us: 1.01x slower                                                  |
| logging_format             | 6.23 us                                                | 6.32 us: 1.01x slower                                                  |
| html5lib                   | 63.4 ms                                                | 64.6 ms: 1.02x slower                                                  |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                                   |
| async_generators           | 433 ms                                                 | 446 ms: 1.03x slower                                                   |
| chaos                      | 58.0 ms                                                | 59.7 ms: 1.03x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                   |
| coroutines                 | 22.2 ms                                                | 22.9 ms: 1.03x slower                                                  |
| sympy_str                  | 273 ms                                                 | 283 ms: 1.04x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.64 ms: 1.04x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 20.7 ms: 1.04x slower                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 55.6 ms: 1.04x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                   |
| sqlglot_parse              | 1.26 ms                                                | 1.32 ms: 1.05x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.08 sec: 1.05x slower                                                 |
| dulwich_log                | 64.6 ms                                                | 67.8 ms: 1.05x slower                                                  |
| genshi_text                | 22.6 ms                                                | 23.8 ms: 1.05x slower                                                  |
| django_template            | 31.7 ms                                                | 33.6 ms: 1.06x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.71 sec: 1.06x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 324 us: 1.07x slower                                                   |
| sympy_expand               | 456 ms                                                 | 490 ms: 1.07x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 881 us: 1.08x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.79 sec: 1.08x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.0 ms: 1.09x slower                                                  |
| raytrace                   | 262 ms                                                 | 286 ms: 1.09x slower                                                   |
| nqueens                    | 80.9 ms                                                | 90.0 ms: 1.11x slower                                                  |
| genshi_xml                 | 50.5 ms                                                | 56.9 ms: 1.13x slower                                                  |
| many_optionals             | 857 us                                                 | 979 us: 1.14x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.96 ms: 1.15x slower                                                  |
| generators                 | 28.8 ms                                                | 36.7 ms: 1.28x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.34x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (4): pprint_pformat, pidigits, asyncio_websockets, djangocms
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241210-3.14.0a2+-6e0f4f5-JIT/bm-20241210-linux-x86_64-brandtbucher-justin_cold_20-3.14.0a2+-6e0f4f5.json: mypy2

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 99.19% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x