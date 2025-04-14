# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_optimizer_equali
- machine: linux-x86_64
- commit hash: 3f0f396
- commit date: 2025-03-06
- overall geometric mean: 1.039x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                         |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                       |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 320 ms: 1.45x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                         |
| async_tree_io              | 838 ms                                                 | 618 ms: 1.36x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 332 ms: 1.31x faster                                                         |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                         |
| async_generators           | 433 ms                                                 | 404 ms: 1.07x faster                                                         |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.0 ms: 1.12x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| nbody          | 87.7 ms                                                | 98.9 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.40 ms: 1.11x faster                                                        |
| regex_v8       | 26.9 ms                                                | 25.5 ms: 1.05x faster                                                        |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.85 sec: 1.14x faster                                                       |
| xml_etree_generate   | 86.8 ms                                                | 79.6 ms: 1.09x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 56.9 ms: 1.06x faster                                                        |
| xml_etree_parse      | 154 ms                                                 | 146 ms: 1.05x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 207 us: 1.03x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                                        |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                                         |
| json_loads           | 27.2 us                                                | 29.7 us: 1.09x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.15 ms: 1.02x slower                                                        |
| python_startup         | 12.7 ms                                                | 13.0 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.05x faster                                                        |
| genshi_xml      | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                        |
| mako            | 10.7 ms                                                | 10.6 ms: 1.01x faster                                                        |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 320 ms: 1.45x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                         |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                         |
| async_tree_io              | 838 ms                                                 | 618 ms: 1.36x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 332 ms: 1.31x faster                                                         |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 29.7 us: 1.29x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.21x faster                                                        |
| spectral_norm              | 113 ms                                                 | 94.4 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                         |
| go                         | 141 ms                                                 | 120 ms: 1.18x faster                                                         |
| scimark_fft                | 367 ms                                                 | 313 ms: 1.17x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.44 ms: 1.13x faster                                                        |
| float                      | 78.7 ms                                                | 70.0 ms: 1.12x faster                                                        |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.40 ms: 1.11x faster                                                        |
| pyflate                    | 470 ms                                                 | 427 ms: 1.10x faster                                                         |
| telco                      | 8.40 ms                                                | 7.66 ms: 1.10x faster                                                        |
| xml_etree_generate         | 86.8 ms                                                | 79.6 ms: 1.09x faster                                                        |
| richards                   | 47.5 ms                                                | 44.1 ms: 1.08x faster                                                        |
| async_generators           | 433 ms                                                 | 404 ms: 1.07x faster                                                         |
| richards_super             | 53.7 ms                                                | 50.4 ms: 1.07x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 56.9 ms: 1.06x faster                                                        |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                                        |
| thrift                     | 800 us                                                 | 758 us: 1.05x faster                                                         |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.05x faster                                                        |
| xml_etree_parse            | 154 ms                                                 | 146 ms: 1.05x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 25.5 ms: 1.05x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.47 sec: 1.05x faster                                                       |
| logging_simple             | 5.65 us                                                | 5.45 us: 1.04x faster                                                        |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                       |
| unpickle_pure_python       | 213 us                                                 | 207 us: 1.03x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                                        |
| logging_format             | 6.23 us                                                | 6.08 us: 1.03x faster                                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                         |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                                       |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                         |
| generators                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.02x faster                                                         |
| connected_components       | 447 ms                                                 | 439 ms: 1.02x faster                                                         |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                       |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.01x faster                                                        |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                                        |
| shortest_path              | 487 ms                                                 | 480 ms: 1.01x faster                                                         |
| genshi_xml                 | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                        |
| crypto_pyaes               | 74.7 ms                                                | 74.1 ms: 1.01x faster                                                        |
| mako                       | 10.7 ms                                                | 10.6 ms: 1.01x faster                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.44 ms: 1.00x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| sqlglot_optimize           | 53.4 ms                                                | 53.6 ms: 1.01x slower                                                        |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                        |
| coverage                   | 82.8 ms                                                | 83.8 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 737 ms: 1.01x slower                                                         |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.26 ms                                                | 1.29 ms: 1.02x slower                                                        |
| python_startup_no_site     | 7.00 ms                                                | 7.15 ms: 1.02x slower                                                        |
| sympy_expand               | 456 ms                                                 | 466 ms: 1.02x slower                                                         |
| gc_traversal               | 4.90 ms                                                | 5.00 ms: 1.02x slower                                                        |
| nqueens                    | 80.9 ms                                                | 82.8 ms: 1.02x slower                                                        |
| python_startup             | 12.7 ms                                                | 13.0 ms: 1.02x slower                                                        |
| fannkuch                   | 394 ms                                                 | 403 ms: 1.02x slower                                                         |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.03x slower                                                         |
| chaos                      | 58.0 ms                                                | 59.6 ms: 1.03x slower                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 68.8 ms: 1.03x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                       |
| pprint_pformat             | 1.48 sec                                               | 1.53 sec: 1.03x slower                                                       |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                         |
| dulwich_log                | 64.6 ms                                                | 67.1 ms: 1.04x slower                                                        |
| deltablue                  | 3.19 ms                                                | 3.34 ms: 1.04x slower                                                        |
| logging_silent             | 101 ns                                                 | 106 ns: 1.05x slower                                                         |
| hexiom                     | 6.08 ms                                                | 6.40 ms: 1.05x slower                                                        |
| raytrace                   | 262 ms                                                 | 277 ms: 1.06x slower                                                         |
| comprehensions             | 16.5 us                                                | 17.6 us: 1.07x slower                                                        |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 876 us: 1.07x slower                                                         |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.09x slower                                                        |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                        |
| many_optionals             | 857 us                                                 | 958 us: 1.12x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                        |
| nbody                      | 87.7 ms                                                | 98.9 ms: 1.13x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.34x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.7 ms: 3.41x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (8): sphinx, scimark_sor, sympy_str, sympy_sum, json, asyncio_websockets, regex_dna, meteor_contest
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x