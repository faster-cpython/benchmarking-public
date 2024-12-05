# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_cold_18
- machine: linux-x86_64
- commit hash: 1cd9228
- commit date: 2024-12-04
- overall geometric mean: 1.031x faster
- HPT reliability: 96.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                   |
| docutils       | 2.58 sec                                               | 2.72 sec: 1.05x slower                                                 |
| html5lib       | 63.4 ms                                                | 65.2 ms: 1.03x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.06 sec: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 628 ms: 1.37x faster                                                   |
| async_tree_io              | 838 ms                                                 | 626 ms: 1.34x faster                                                   |
| async_tree_none            | 350 ms                                                 | 271 ms: 1.29x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 341 ms: 1.28x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                   |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 87.7 ms                                                | 81.3 ms: 1.08x faster                                                  |
| float          | 78.7 ms                                                | 75.5 ms: 1.04x faster                                                  |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.26 ms: 1.15x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                  |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                   |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.13x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 78.0 ms: 1.11x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 55.2 ms: 1.10x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 1.93 sec: 1.10x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 197 us: 1.08x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 95.0 ms: 1.07x faster                                                  |
| json_loads           | 27.2 us                                                | 26.2 us: 1.04x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                  |
| genshi_text     | 22.6 ms                                                | 24.2 ms: 1.07x slower                                                  |
| django_template | 31.7 ms                                                | 34.0 ms: 1.07x slower                                                  |
| genshi_xml      | 50.5 ms                                                | 56.7 ms: 1.12x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_18-3.14.0a2+-1cd9228 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 628 ms: 1.37x faster                                                   |
| async_tree_io              | 838 ms                                                 | 626 ms: 1.34x faster                                                   |
| deepcopy                   | 354 us                                                 | 266 us: 1.33x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                  |
| richards                   | 47.5 ms                                                | 36.6 ms: 1.30x faster                                                  |
| async_tree_none            | 350 ms                                                 | 271 ms: 1.29x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 341 ms: 1.28x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                   |
| richards_super             | 53.7 ms                                                | 43.1 ms: 1.25x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.26 ms: 1.15x faster                                                  |
| scimark_fft                | 367 ms                                                 | 321 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.13x faster                                                   |
| json                       | 5.32 ms                                                | 4.76 ms: 1.12x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 78.0 ms: 1.11x faster                                                  |
| telco                      | 8.40 ms                                                | 7.63 ms: 1.10x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 55.2 ms: 1.10x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.93 sec: 1.10x faster                                                 |
| crypto_pyaes               | 74.7 ms                                                | 68.4 ms: 1.09x faster                                                  |
| unpickle_pure_python       | 213 us                                                 | 197 us: 1.08x faster                                                   |
| nbody                      | 87.7 ms                                                | 81.3 ms: 1.08x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.38 sec: 1.07x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 95.0 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.72 ms: 1.07x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.3 ms: 1.06x faster                                                  |
| pylint                     | 312 ms                                                 | 294 ms: 1.06x faster                                                   |
| mako                       | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                  |
| pyflate                    | 470 ms                                                 | 450 ms: 1.04x faster                                                   |
| float                      | 78.7 ms                                                | 75.5 ms: 1.04x faster                                                  |
| go                         | 141 ms                                                 | 135 ms: 1.04x faster                                                   |
| connected_components       | 447 ms                                                 | 431 ms: 1.04x faster                                                   |
| json_loads                 | 27.2 us                                                | 26.2 us: 1.04x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 64.9 ms: 1.03x faster                                                  |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                   |
| fannkuch                   | 394 ms                                                 | 384 ms: 1.02x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 727 ms                                                 | 711 ms: 1.02x faster                                                   |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                   |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                                   |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.02x faster                                                 |
| shortest_path              | 487 ms                                                 | 481 ms: 1.01x faster                                                   |
| thrift                     | 800 us                                                 | 791 us: 1.01x faster                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                                  |
| deltablue                  | 3.19 ms                                                | 3.18 ms: 1.00x faster                                                  |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                  |
| logging_simple             | 5.65 us                                                | 5.72 us: 1.01x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 4.96 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                   |
| logging_silent             | 101 ns                                                 | 103 ns: 1.02x slower                                                   |
| coverage                   | 82.8 ms                                                | 84.3 ms: 1.02x slower                                                  |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                                   |
| sphinx                     | 1.03 sec                                               | 1.06 sec: 1.03x slower                                                 |
| html5lib                   | 63.4 ms                                                | 65.2 ms: 1.03x slower                                                  |
| chaos                      | 58.0 ms                                                | 59.9 ms: 1.03x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                                   |
| sympy_str                  | 273 ms                                                 | 284 ms: 1.04x slower                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 55.6 ms: 1.04x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 20.7 ms: 1.05x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.64 ms: 1.05x slower                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.32 ms: 1.05x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 67.7 ms: 1.05x slower                                                  |
| async_generators           | 433 ms                                                 | 456 ms: 1.05x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.4 us: 1.05x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.72 sec: 1.05x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                                   |
| mdp                        | 2.54 sec                                               | 2.70 sec: 1.06x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 874 us: 1.07x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                  |
| genshi_text                | 22.6 ms                                                | 24.2 ms: 1.07x slower                                                  |
| sympy_expand               | 456 ms                                                 | 490 ms: 1.07x slower                                                   |
| django_template            | 31.7 ms                                                | 34.0 ms: 1.07x slower                                                  |
| raytrace                   | 262 ms                                                 | 288 ms: 1.10x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                  |
| nqueens                    | 80.9 ms                                                | 90.6 ms: 1.12x slower                                                  |
| genshi_xml                 | 50.5 ms                                                | 56.7 ms: 1.12x slower                                                  |
| many_optionals             | 857 us                                                 | 974 us: 1.14x slower                                                   |
| hexiom                     | 6.08 ms                                                | 7.04 ms: 1.16x slower                                                  |
| generators                 | 28.8 ms                                                | 36.6 ms: 1.27x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.5 ms: 3.40x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (6): pycparser, djangocms, asyncio_websockets, meteor_contest, logging_format, spectral_norm
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 96.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x