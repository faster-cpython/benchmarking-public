# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_cold_16
- machine: linux-x86_64
- commit hash: 189256b
- commit date: 2024-12-04
- overall geometric mean: 1.030x faster
- HPT reliability: 97.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                   |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                 |
| html5lib       | 63.4 ms                                                | 64.9 ms: 1.02x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 609 ms: 1.41x faster                                                   |
| async_tree_io              | 838 ms                                                 | 623 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 271 ms: 1.29x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 340 ms: 1.29x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                   |
| async_generators           | 433 ms                                                 | 453 ms: 1.05x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 87.7 ms                                                | 80.5 ms: 1.09x faster                                                  |
| float          | 78.7 ms                                                | 75.9 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.5 ms: 1.09x faster                                                  |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                   |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 77.8 ms: 1.12x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 194 us: 1.10x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 55.4 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 94.9 ms: 1.07x faster                                                  |
| json_loads           | 27.2 us                                                | 26.3 us: 1.03x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.06x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                  |
| genshi_text     | 22.6 ms                                                | 23.9 ms: 1.06x slower                                                  |
| django_template | 31.7 ms                                                | 34.1 ms: 1.08x slower                                                  |
| genshi_xml      | 50.5 ms                                                | 56.7 ms: 1.12x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241204-linux-x86_64-brandtbucher-justin_cold_16-3.14.0a2+-189256b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 609 ms: 1.41x faster                                                   |
| async_tree_io              | 838 ms                                                 | 623 ms: 1.35x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                  |
| deepcopy                   | 354 us                                                 | 271 us: 1.31x faster                                                   |
| async_tree_none            | 350 ms                                                 | 271 ms: 1.29x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 340 ms: 1.29x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                   |
| richards_super             | 53.7 ms                                                | 42.8 ms: 1.26x faster                                                  |
| richards                   | 47.5 ms                                                | 37.9 ms: 1.26x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.78 us: 1.17x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                   |
| scimark_fft                | 367 ms                                                 | 327 ms: 1.12x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 77.8 ms: 1.12x faster                                                  |
| telco                      | 8.40 ms                                                | 7.53 ms: 1.12x faster                                                  |
| unpickle_pure_python       | 213 us                                                 | 194 us: 1.10x faster                                                   |
| json                       | 5.32 ms                                                | 4.85 ms: 1.10x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 24.5 ms: 1.09x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 55.4 ms: 1.09x faster                                                  |
| nbody                      | 87.7 ms                                                | 80.5 ms: 1.09x faster                                                  |
| pylint                     | 312 ms                                                 | 287 ms: 1.09x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 69.4 ms: 1.08x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.07x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 94.9 ms: 1.07x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.41 sec: 1.06x faster                                                 |
| mako                       | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                  |
| go                         | 141 ms                                                 | 135 ms: 1.04x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                  |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                                   |
| float                      | 78.7 ms                                                | 75.9 ms: 1.04x faster                                                  |
| pyflate                    | 470 ms                                                 | 454 ms: 1.03x faster                                                   |
| json_loads                 | 27.2 us                                                | 26.3 us: 1.03x faster                                                  |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                 |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                   |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                   |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                                   |
| scimark_lu                 | 114 ms                                                 | 112 ms: 1.02x faster                                                   |
| thrift                     | 800 us                                                 | 784 us: 1.02x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 727 ms                                                 | 720 ms: 1.01x faster                                                   |
| shortest_path              | 487 ms                                                 | 484 ms: 1.01x faster                                                   |
| deltablue                  | 3.19 ms                                                | 3.18 ms: 1.00x faster                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                                 |
| coverage                   | 82.8 ms                                                | 83.6 ms: 1.01x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                  |
| spectral_norm              | 113 ms                                                 | 114 ms: 1.01x slower                                                   |
| logging_format             | 6.23 us                                                | 6.31 us: 1.01x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                 |
| logging_simple             | 5.65 us                                                | 5.75 us: 1.02x slower                                                  |
| html5lib                   | 63.4 ms                                                | 64.9 ms: 1.02x slower                                                  |
| sqlglot_normalize          | 108 ms                                                 | 111 ms: 1.03x slower                                                   |
| sympy_str                  | 273 ms                                                 | 281 ms: 1.03x slower                                                   |
| gc_traversal               | 4.90 ms                                                | 5.04 ms: 1.03x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                 |
| sympy_expand               | 456 ms                                                 | 474 ms: 1.04x slower                                                   |
| chaos                      | 58.0 ms                                                | 60.4 ms: 1.04x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 20.7 ms: 1.04x slower                                                  |
| async_generators           | 433 ms                                                 | 453 ms: 1.05x slower                                                   |
| sqlglot_parse              | 1.26 ms                                                | 1.32 ms: 1.05x slower                                                  |
| logging_silent             | 101 ns                                                 | 106 ns: 1.05x slower                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 55.9 ms: 1.05x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.65 ms: 1.05x slower                                                  |
| comprehensions             | 16.5 us                                                | 17.3 us: 1.05x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.06x slower                                                   |
| genshi_text                | 22.6 ms                                                | 23.9 ms: 1.06x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.70 sec: 1.06x slower                                                 |
| dulwich_log                | 64.6 ms                                                | 68.6 ms: 1.06x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 879 us: 1.07x slower                                                   |
| django_template            | 31.7 ms                                                | 34.1 ms: 1.08x slower                                                  |
| raytrace                   | 262 ms                                                 | 289 ms: 1.10x slower                                                   |
| nqueens                    | 80.9 ms                                                | 89.7 ms: 1.11x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                  |
| genshi_xml                 | 50.5 ms                                                | 56.7 ms: 1.12x slower                                                  |
| many_optionals             | 857 us                                                 | 979 us: 1.14x slower                                                   |
| hexiom                     | 6.08 ms                                                | 7.05 ms: 1.16x slower                                                  |
| generators                 | 28.8 ms                                                | 36.8 ms: 1.28x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (9): scimark_monte_carlo, scimark_sparse_mat_mult, pycparser, sqlalchemy_imperative, fannkuch, pidigits, meteor_contest, asyncio_websockets, djangocms
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 97.80% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x