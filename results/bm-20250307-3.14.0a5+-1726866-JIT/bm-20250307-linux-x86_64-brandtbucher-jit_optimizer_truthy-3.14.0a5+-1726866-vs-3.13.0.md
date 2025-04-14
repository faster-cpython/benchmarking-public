# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_optimizer_truthy
- machine: linux-x86_64
- commit hash: 1726866
- commit date: 2025-03-07
- overall geometric mean: 1.044x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                         |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                       |
| html5lib       | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 610 ms: 1.37x faster                                                         |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 330 ms: 1.32x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                         |
| async_generators           | 433 ms                                                 | 408 ms: 1.06x faster                                                         |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.8 ms: 1.13x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| nbody          | 87.7 ms                                                | 88.2 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.39 ms: 1.11x faster                                                        |
| regex_v8       | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                        |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.87 sec: 1.13x faster                                                       |
| xml_etree_generate   | 86.8 ms                                                | 79.4 ms: 1.09x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 56.0 ms: 1.08x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 202 us: 1.05x faster                                                         |
| xml_etree_parse      | 154 ms                                                 | 147 ms: 1.05x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 99.4 ms: 1.02x faster                                                        |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                                         |
| json_loads           | 27.2 us                                                | 30.0 us: 1.11x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.13 ms: 1.02x slower                                                        |
| python_startup         | 12.7 ms                                                | 13.0 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                        |
| mako            | 10.7 ms                                                | 10.5 ms: 1.02x faster                                                        |
| genshi_xml      | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                        |
| django_template | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-linux-x86_64-brandtbucher-jit_optimizer_truthy-3.14.0a5+-1726866 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 610 ms: 1.37x faster                                                         |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                         |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 330 ms: 1.32x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 29.2 us: 1.32x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.61 us: 1.24x faster                                                        |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                                         |
| spectral_norm              | 113 ms                                                 | 95.7 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                         |
| scimark_fft                | 367 ms                                                 | 317 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 1.87 sec: 1.13x faster                                                       |
| float                      | 78.7 ms                                                | 69.8 ms: 1.13x faster                                                        |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.39 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.55 ms: 1.10x faster                                                        |
| xml_etree_generate         | 86.8 ms                                                | 79.4 ms: 1.09x faster                                                        |
| telco                      | 8.40 ms                                                | 7.68 ms: 1.09x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 56.0 ms: 1.08x faster                                                        |
| regex_v8                   | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                        |
| richards                   | 47.5 ms                                                | 44.3 ms: 1.07x faster                                                        |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                                        |
| gc_traversal               | 4.90 ms                                                | 4.60 ms: 1.06x faster                                                        |
| async_generators           | 433 ms                                                 | 408 ms: 1.06x faster                                                         |
| richards_super             | 53.7 ms                                                | 50.7 ms: 1.06x faster                                                        |
| thrift                     | 800 us                                                 | 755 us: 1.06x faster                                                         |
| pyflate                    | 470 ms                                                 | 443 ms: 1.06x faster                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.43 sec: 1.06x faster                                                       |
| unpickle_pure_python       | 213 us                                                 | 202 us: 1.05x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 147 ms: 1.05x faster                                                         |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                        |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| generators                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                       |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                        |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                       |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                         |
| sqlglot_normalize          | 108 ms                                                 | 105 ms: 1.02x faster                                                         |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                         |
| html5lib                   | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                        |
| logging_simple             | 5.65 us                                                | 5.54 us: 1.02x faster                                                        |
| logging_format             | 6.23 us                                                | 6.11 us: 1.02x faster                                                        |
| connected_components       | 447 ms                                                 | 439 ms: 1.02x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 99.4 ms: 1.02x faster                                                        |
| mako                       | 10.7 ms                                                | 10.5 ms: 1.02x faster                                                        |
| mdp                        | 2.54 sec                                               | 2.51 sec: 1.01x faster                                                       |
| genshi_xml                 | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                        |
| shortest_path              | 487 ms                                                 | 482 ms: 1.01x faster                                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.43 ms: 1.01x faster                                                        |
| django_template            | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                        |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x faster                                                         |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                         |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.01x faster                                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| sqlglot_optimize           | 53.4 ms                                                | 53.5 ms: 1.00x slower                                                        |
| nbody                      | 87.7 ms                                                | 88.2 ms: 1.01x slower                                                        |
| nqueens                    | 80.9 ms                                                | 81.5 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                                         |
| coverage                   | 82.8 ms                                                | 83.8 ms: 1.01x slower                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 67.8 ms: 1.01x slower                                                        |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.26 ms                                                | 1.29 ms: 1.02x slower                                                        |
| pprint_pformat             | 1.48 sec                                               | 1.51 sec: 1.02x slower                                                       |
| python_startup_no_site     | 7.00 ms                                                | 7.13 ms: 1.02x slower                                                        |
| chaos                      | 58.0 ms                                                | 59.2 ms: 1.02x slower                                                        |
| deltablue                  | 3.19 ms                                                | 3.26 ms: 1.02x slower                                                        |
| fannkuch                   | 394 ms                                                 | 402 ms: 1.02x slower                                                         |
| sympy_expand               | 456 ms                                                 | 467 ms: 1.02x slower                                                         |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                         |
| python_startup             | 12.7 ms                                                | 13.0 ms: 1.02x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                       |
| pprint_safe_repr           | 727 ms                                                 | 747 ms: 1.03x slower                                                         |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                         |
| dulwich_log                | 64.6 ms                                                | 67.3 ms: 1.04x slower                                                        |
| hexiom                     | 6.08 ms                                                | 6.37 ms: 1.05x slower                                                        |
| logging_silent             | 101 ns                                                 | 107 ns: 1.06x slower                                                         |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                        |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 876 us: 1.07x slower                                                         |
| comprehensions             | 16.5 us                                                | 17.7 us: 1.07x slower                                                        |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.11x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.12x slower                                                        |
| many_optionals             | 857 us                                                 | 964 us: 1.13x slower                                                         |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.8 ms: 3.41x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (7): sphinx, regex_dna, sqlalchemy_imperative, sympy_str, crypto_pyaes, asyncio_websockets, json
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x