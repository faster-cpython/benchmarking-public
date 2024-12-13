# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_lto
- machine: linux-x86_64
- commit hash: f5bcb83
- commit date: 2024-12-13
- overall geometric mean: 1.018x faster
- HPT reliability: 88.06%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.01x faster                                               |
| docutils       | 2.58 sec                                               | 2.71 sec: 1.05x slower                                             |
| html5lib       | 63.4 ms                                                | 65.6 ms: 1.04x slower                                              |
| sphinx         | 1.03 sec                                               | 1.06 sec: 1.02x slower                                             |
| Geometric mean | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                               |
| async_tree_io              | 838 ms                                                 | 624 ms: 1.34x faster                                               |
| async_tree_none            | 350 ms                                                 | 270 ms: 1.30x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 342 ms: 1.28x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                               |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                               |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.04x slower                                              |
| async_generators           | 433 ms                                                 | 458 ms: 1.06x slower                                               |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 87.7 ms                                                | 82.8 ms: 1.06x faster                                              |
| float          | 78.7 ms                                                | 76.1 ms: 1.03x faster                                              |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.38 ms: 1.11x faster                                              |
| regex_v8       | 26.9 ms                                                | 24.9 ms: 1.08x faster                                              |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.13x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 77.6 ms: 1.12x faster                                              |
| tomli_loads          | 2.12 sec                                               | 1.92 sec: 1.10x faster                                             |
| xml_etree_process    | 60.5 ms                                                | 54.9 ms: 1.10x faster                                              |
| unpickle_pure_python | 213 us                                                 | 199 us: 1.07x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 95.2 ms: 1.06x faster                                              |
| json_loads           | 27.2 us                                                | 26.2 us: 1.04x faster                                              |
| pickle_pure_python   | 302 us                                                 | 326 us: 1.08x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                              |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.03 ms: 1.00x slower                                              |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.4 ms: 1.03x faster                                              |
| django_template | 31.7 ms                                                | 34.2 ms: 1.08x slower                                              |
| genshi_text     | 22.6 ms                                                | 25.2 ms: 1.11x slower                                              |
| genshi_xml      | 50.5 ms                                                | 60.3 ms: 1.19x slower                                              |
| Geometric mean  | (ref)                                                  | 1.09x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                               |
| async_tree_io              | 838 ms                                                 | 624 ms: 1.34x faster                                               |
| async_tree_none            | 350 ms                                                 | 270 ms: 1.30x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 29.8 us: 1.29x faster                                              |
| deepcopy                   | 354 us                                                 | 276 us: 1.29x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 342 ms: 1.28x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.13x faster                                               |
| richards                   | 47.5 ms                                                | 42.3 ms: 1.12x faster                                              |
| xml_etree_generate         | 86.8 ms                                                | 77.6 ms: 1.12x faster                                              |
| scimark_fft                | 367 ms                                                 | 329 ms: 1.11x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.38 ms: 1.11x faster                                              |
| tomli_loads                | 2.12 sec                                               | 1.92 sec: 1.10x faster                                             |
| telco                      | 8.40 ms                                                | 7.62 ms: 1.10x faster                                              |
| xml_etree_process          | 60.5 ms                                                | 54.9 ms: 1.10x faster                                              |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.63 ms: 1.09x faster                                              |
| json                       | 5.32 ms                                                | 4.90 ms: 1.09x faster                                              |
| crypto_pyaes               | 74.7 ms                                                | 69.3 ms: 1.08x faster                                              |
| regex_v8                   | 26.9 ms                                                | 24.9 ms: 1.08x faster                                              |
| unpickle_pure_python       | 213 us                                                 | 199 us: 1.07x faster                                               |
| gc_traversal               | 4.90 ms                                                | 4.57 ms: 1.07x faster                                              |
| pylint                     | 312 ms                                                 | 293 ms: 1.07x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 95.2 ms: 1.06x faster                                              |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.41 sec: 1.06x faster                                             |
| nbody                      | 87.7 ms                                                | 82.8 ms: 1.06x faster                                              |
| richards_super             | 53.7 ms                                                | 51.3 ms: 1.05x faster                                              |
| json_loads                 | 27.2 us                                                | 26.2 us: 1.04x faster                                              |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                               |
| float                      | 78.7 ms                                                | 76.1 ms: 1.03x faster                                              |
| pyflate                    | 470 ms                                                 | 455 ms: 1.03x faster                                               |
| mako                       | 10.7 ms                                                | 10.4 ms: 1.03x faster                                              |
| k_core                     | 2.37 sec                                               | 2.32 sec: 1.02x faster                                             |
| thrift                     | 800 us                                                 | 782 us: 1.02x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.84 us: 1.02x faster                                              |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                               |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                               |
| connected_components       | 447 ms                                                 | 440 ms: 1.02x faster                                               |
| 2to3                       | 266 ms                                                 | 262 ms: 1.01x faster                                               |
| fannkuch                   | 394 ms                                                 | 388 ms: 1.01x faster                                               |
| scimark_monte_carlo        | 66.8 ms                                                | 66.0 ms: 1.01x faster                                              |
| pycparser                  | 1.20 sec                                               | 1.19 sec: 1.01x faster                                             |
| shortest_path              | 487 ms                                                 | 484 ms: 1.01x faster                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.44 ms: 1.00x faster                                              |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                               |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 7.03 ms: 1.00x slower                                              |
| spectral_norm              | 113 ms                                                 | 114 ms: 1.00x slower                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.0 ms: 1.01x slower                                              |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                              |
| coverage                   | 82.8 ms                                                | 83.6 ms: 1.01x slower                                              |
| mdp                        | 2.54 sec                                               | 2.58 sec: 1.02x slower                                             |
| pprint_safe_repr           | 727 ms                                                 | 740 ms: 1.02x slower                                               |
| sphinx                     | 1.03 sec                                               | 1.06 sec: 1.02x slower                                             |
| deltablue                  | 3.19 ms                                                | 3.27 ms: 1.02x slower                                              |
| logging_silent             | 101 ns                                                 | 104 ns: 1.03x slower                                               |
| sqlglot_normalize          | 108 ms                                                 | 111 ms: 1.03x slower                                               |
| html5lib                   | 63.4 ms                                                | 65.6 ms: 1.04x slower                                              |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.04x slower                                              |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                               |
| docutils                   | 2.58 sec                                               | 2.71 sec: 1.05x slower                                             |
| logging_simple             | 5.65 us                                                | 5.92 us: 1.05x slower                                              |
| pprint_pformat             | 1.48 sec                                               | 1.55 sec: 1.05x slower                                             |
| logging_format             | 6.23 us                                                | 6.55 us: 1.05x slower                                              |
| sympy_str                  | 273 ms                                                 | 288 ms: 1.05x slower                                               |
| sympy_sum                  | 150 ms                                                 | 159 ms: 1.05x slower                                               |
| sympy_integrate            | 19.8 ms                                                | 20.9 ms: 1.06x slower                                              |
| sqlglot_optimize           | 53.4 ms                                                | 56.4 ms: 1.06x slower                                              |
| async_generators           | 433 ms                                                 | 458 ms: 1.06x slower                                               |
| dulwich_log                | 64.6 ms                                                | 68.6 ms: 1.06x slower                                              |
| sqlglot_transpile          | 1.57 ms                                                | 1.67 ms: 1.07x slower                                              |
| sqlglot_parse              | 1.26 ms                                                | 1.35 ms: 1.07x slower                                              |
| sympy_expand               | 456 ms                                                 | 490 ms: 1.07x slower                                               |
| bench_thread_pool          | 818 us                                                 | 881 us: 1.08x slower                                               |
| pickle_pure_python         | 302 us                                                 | 326 us: 1.08x slower                                               |
| django_template            | 31.7 ms                                                | 34.2 ms: 1.08x slower                                              |
| chaos                      | 58.0 ms                                                | 62.9 ms: 1.08x slower                                              |
| comprehensions             | 16.5 us                                                | 18.1 us: 1.10x slower                                              |
| go                         | 141 ms                                                 | 155 ms: 1.10x slower                                               |
| nqueens                    | 80.9 ms                                                | 89.3 ms: 1.10x slower                                              |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                              |
| genshi_text                | 22.6 ms                                                | 25.2 ms: 1.11x slower                                              |
| many_optionals             | 857 us                                                 | 993 us: 1.16x slower                                               |
| raytrace                   | 262 ms                                                 | 305 ms: 1.16x slower                                               |
| genshi_xml                 | 50.5 ms                                                | 60.3 ms: 1.19x slower                                              |
| hexiom                     | 6.08 ms                                                | 7.77 ms: 1.28x slower                                              |
| generators                 | 28.8 ms                                                | 37.4 ms: 1.30x slower                                              |
| subparsers                 | 15.5 ms                                                | 21.1 ms: 1.37x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 81.3 ms: 3.39x slower                                              |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (4): scimark_lu, meteor_contest, regex_compile, djangocms
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241213-3.14.0a2+-f5bcb83-JIT/bm-20241213-linux-x86_64-brandtbucher-justin_lto-3.14.0a2+-f5bcb83.json: mypy2

- Geometric mean (including insignificant results): 1.018x faster

# HPT report

- Reliability score: 88.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x