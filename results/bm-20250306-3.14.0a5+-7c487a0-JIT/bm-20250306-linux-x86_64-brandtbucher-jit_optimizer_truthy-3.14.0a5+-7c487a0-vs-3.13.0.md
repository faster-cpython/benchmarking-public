# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_optimizer_truthy
- machine: linux-x86_64
- commit hash: 7c487a0
- commit date: 2025-03-06
- overall geometric mean: 1.041x faster
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-7c487a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                         |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                       |
| html5lib       | 63.4 ms                                                | 62.7 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-7c487a0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 623 ms: 1.38x faster                                                         |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                                         |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 329 ms: 1.33x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                         |
| async_generators           | 433 ms                                                 | 408 ms: 1.06x faster                                                         |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.10x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-7c487a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.9 ms: 1.14x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| nbody          | 87.7 ms                                                | 89.7 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-7c487a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.48 ms: 1.08x faster                                                        |
| regex_v8       | 26.9 ms                                                | 25.2 ms: 1.06x faster                                                        |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| regex_dna      | 220 ms                                                 | 226 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-7c487a0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                       |
| xml_etree_generate   | 86.8 ms                                                | 78.5 ms: 1.11x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 55.8 ms: 1.08x faster                                                        |
| xml_etree_parse      | 154 ms                                                 | 147 ms: 1.05x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 208 us: 1.03x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 99.2 ms: 1.02x faster                                                        |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                         |
| json_loads           | 27.2 us                                                | 30.1 us: 1.11x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-7c487a0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.17 ms: 1.02x slower                                                        |
| python_startup         | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-7c487a0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.2 ms: 1.04x faster                                                        |
| genshi_text     | 22.6 ms                                                | 21.9 ms: 1.03x faster                                                        |
| genshi_xml      | 50.5 ms                                                | 50.2 ms: 1.01x faster                                                        |
| django_template | 31.7 ms                                                | 31.8 ms: 1.00x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-7c487a0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 623 ms: 1.38x faster                                                         |
| async_tree_io              | 838 ms                                                 | 607 ms: 1.38x faster                                                         |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                                         |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 29.0 us: 1.33x faster                                                        |
| async_tree_memoization     | 437 ms                                                 | 329 ms: 1.33x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                        |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                                         |
| scimark_fft                | 367 ms                                                 | 312 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                       |
| float                      | 78.7 ms                                                | 68.9 ms: 1.14x faster                                                        |
| spectral_norm              | 113 ms                                                 | 99.8 ms: 1.13x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 483 ms: 1.13x faster                                                         |
| pylint                     | 312 ms                                                 | 280 ms: 1.12x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 78.5 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.56 ms: 1.10x faster                                                        |
| telco                      | 8.40 ms                                                | 7.69 ms: 1.09x faster                                                        |
| richards                   | 47.5 ms                                                | 43.8 ms: 1.09x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 55.8 ms: 1.08x faster                                                        |
| regex_effbot               | 3.77 ms                                                | 3.48 ms: 1.08x faster                                                        |
| richards_super             | 53.7 ms                                                | 50.0 ms: 1.07x faster                                                        |
| thrift                     | 800 us                                                 | 748 us: 1.07x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                                        |
| regex_v8                   | 26.9 ms                                                | 25.2 ms: 1.06x faster                                                        |
| async_generators           | 433 ms                                                 | 408 ms: 1.06x faster                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.46 sec: 1.05x faster                                                       |
| xml_etree_parse            | 154 ms                                                 | 147 ms: 1.05x faster                                                         |
| pyflate                    | 470 ms                                                 | 448 ms: 1.05x faster                                                         |
| mako                       | 10.7 ms                                                | 10.2 ms: 1.04x faster                                                        |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                        |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| genshi_text                | 22.6 ms                                                | 21.9 ms: 1.03x faster                                                        |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                       |
| generators                 | 28.8 ms                                                | 28.0 ms: 1.03x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 208 us: 1.03x faster                                                         |
| logging_simple             | 5.65 us                                                | 5.52 us: 1.02x faster                                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                         |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                                       |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                         |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 99.2 ms: 1.02x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                       |
| shortest_path              | 487 ms                                                 | 480 ms: 1.01x faster                                                         |
| logging_format             | 6.23 us                                                | 6.15 us: 1.01x faster                                                        |
| html5lib                   | 63.4 ms                                                | 62.7 ms: 1.01x faster                                                        |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                        |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                         |
| connected_components       | 447 ms                                                 | 443 ms: 1.01x faster                                                         |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x faster                                                         |
| crypto_pyaes               | 74.7 ms                                                | 74.2 ms: 1.01x faster                                                        |
| genshi_xml                 | 50.5 ms                                                | 50.2 ms: 1.01x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                        |
| django_template            | 31.7 ms                                                | 31.8 ms: 1.00x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 731 ms: 1.01x slower                                                         |
| sqlglot_optimize           | 53.4 ms                                                | 53.8 ms: 1.01x slower                                                        |
| nqueens                    | 80.9 ms                                                | 81.9 ms: 1.01x slower                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 67.7 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                        |
| sympy_integrate            | 19.8 ms                                                | 20.2 ms: 1.02x slower                                                        |
| chaos                      | 58.0 ms                                                | 59.1 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.26 ms                                                | 1.29 ms: 1.02x slower                                                        |
| logging_silent             | 101 ns                                                 | 103 ns: 1.02x slower                                                         |
| deltablue                  | 3.19 ms                                                | 3.26 ms: 1.02x slower                                                        |
| nbody                      | 87.7 ms                                                | 89.7 ms: 1.02x slower                                                        |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                         |
| python_startup_no_site     | 7.00 ms                                                | 7.17 ms: 1.02x slower                                                        |
| gc_traversal               | 4.90 ms                                                | 5.02 ms: 1.02x slower                                                        |
| regex_dna                  | 220 ms                                                 | 226 ms: 1.03x slower                                                         |
| python_startup             | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                        |
| coverage                   | 82.8 ms                                                | 85.1 ms: 1.03x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                       |
| pprint_pformat             | 1.48 sec                                               | 1.53 sec: 1.03x slower                                                       |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                         |
| sympy_expand               | 456 ms                                                 | 473 ms: 1.04x slower                                                         |
| dulwich_log                | 64.6 ms                                                | 67.0 ms: 1.04x slower                                                        |
| hexiom                     | 6.08 ms                                                | 6.32 ms: 1.04x slower                                                        |
| fannkuch                   | 394 ms                                                 | 411 ms: 1.04x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 876 us: 1.07x slower                                                         |
| comprehensions             | 16.5 us                                                | 17.7 us: 1.07x slower                                                        |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.10x slower                                                        |
| json_loads                 | 27.2 us                                                | 30.1 us: 1.11x slower                                                        |
| many_optionals             | 857 us                                                 | 958 us: 1.12x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.13x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 82.0 ms: 3.42x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (6): sphinx, asyncio_websockets, json, typing_runtime_protocols, sympy_sum, sympy_str
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x