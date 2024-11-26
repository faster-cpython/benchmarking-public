# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_64
- machine: linux-x86_64
- commit hash: 48ade84
- commit date: 2024-11-08
- overall geometric mean: 1.004x slower
- HPT reliability: 79.75%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 277 ms: 1.04x slower                                              |
| docutils       | 2.59 sec                                               | 2.92 sec: 1.13x slower                                            |
| html5lib       | 64.2 ms                                                | 65.8 ms: 1.03x slower                                             |
| sphinx         | 1.03 sec                                               | 1.17 sec: 1.14x slower                                            |
| Geometric mean | (ref)                                                  | 1.08x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 383 ms: 1.21x faster                                              |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                              |
| async_tree_none            | 351 ms                                                 | 332 ms: 1.05x faster                                              |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                              |
| async_generators           | 436 ms                                                 | 452 ms: 1.04x slower                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 567 ms: 1.04x slower                                              |
| async_tree_io_tg           | 857 ms                                                 | 978 ms: 1.14x slower                                              |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (4): coroutines, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 82.6 ms: 1.05x faster                                             |
| float          | 79.2 ms                                                | 76.8 ms: 1.03x faster                                             |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.62 ms: 1.03x faster                                             |
| regex_v8       | 26.2 ms                                                | 25.5 ms: 1.03x faster                                             |
| regex_dna      | 218 ms                                                 | 214 ms: 1.02x faster                                              |
| regex_compile  | 132 ms                                                 | 137 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 216 us                                                 | 196 us: 1.10x faster                                              |
| xml_etree_generate   | 86.7 ms                                                | 79.1 ms: 1.10x faster                                             |
| xml_etree_process    | 60.6 ms                                                | 55.4 ms: 1.09x faster                                             |
| tomli_loads          | 2.14 sec                                               | 1.97 sec: 1.09x faster                                            |
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.04x faster                                              |
| json_loads           | 27.2 us                                                | 26.6 us: 1.02x faster                                             |
| xml_etree_iterparse  | 101 ms                                                 | 101 ms: 1.00x faster                                              |
| json_dumps           | 10.6 ms                                                | 10.8 ms: 1.03x slower                                             |
| pickle_pure_python   | 310 us                                                 | 321 us: 1.03x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                             |
| python_startup_no_site | 6.96 ms                                                | 7.12 ms: 1.02x slower                                             |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.1 ms: 1.10x faster                                             |
| django_template | 35.2 ms                                                | 36.2 ms: 1.03x slower                                             |
| genshi_text     | 23.5 ms                                                | 25.2 ms: 1.07x slower                                             |
| genshi_xml      | 50.9 ms                                                | 58.8 ms: 1.16x slower                                             |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 29.5 us: 1.33x faster                                             |
| deepcopy                   | 358 us                                                 | 271 us: 1.32x faster                                              |
| async_tree_memoization_tg  | 464 ms                                                 | 383 ms: 1.21x faster                                              |
| deepcopy_reduce            | 3.20 us                                                | 2.73 us: 1.17x faster                                             |
| richards                   | 48.7 ms                                                | 42.4 ms: 1.15x faster                                             |
| scimark_fft                | 364 ms                                                 | 320 ms: 1.14x faster                                              |
| richards_super             | 54.9 ms                                                | 48.2 ms: 1.14x faster                                             |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.49 ms: 1.12x faster                                             |
| telco                      | 8.54 ms                                                | 7.61 ms: 1.12x faster                                             |
| unpickle_pure_python       | 216 us                                                 | 196 us: 1.10x faster                                              |
| mako                       | 11.1 ms                                                | 10.1 ms: 1.10x faster                                             |
| pathlib                    | 17.5 ms                                                | 16.0 ms: 1.10x faster                                             |
| xml_etree_generate         | 86.7 ms                                                | 79.1 ms: 1.10x faster                                             |
| crypto_pyaes               | 75.3 ms                                                | 68.7 ms: 1.10x faster                                             |
| xml_etree_process          | 60.6 ms                                                | 55.4 ms: 1.09x faster                                             |
| tomli_loads                | 2.14 sec                                               | 1.97 sec: 1.09x faster                                            |
| json                       | 5.36 ms                                                | 4.99 ms: 1.07x faster                                             |
| mdp                        | 2.72 sec                                               | 2.56 sec: 1.06x faster                                            |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                              |
| async_tree_none            | 351 ms                                                 | 332 ms: 1.05x faster                                              |
| nbody                      | 87.0 ms                                                | 82.6 ms: 1.05x faster                                             |
| bpe_tokeniser              | 4.75 sec                                               | 4.52 sec: 1.05x faster                                            |
| go                         | 144 ms                                                 | 137 ms: 1.05x faster                                              |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.04x faster                                              |
| fannkuch                   | 404 ms                                                 | 388 ms: 1.04x faster                                              |
| scimark_monte_carlo        | 67.4 ms                                                | 64.7 ms: 1.04x faster                                             |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                            |
| scimark_sor                | 124 ms                                                 | 120 ms: 1.03x faster                                              |
| pyflate                    | 471 ms                                                 | 457 ms: 1.03x faster                                              |
| thrift                     | 809 us                                                 | 785 us: 1.03x faster                                              |
| float                      | 79.2 ms                                                | 76.8 ms: 1.03x faster                                             |
| regex_effbot               | 3.73 ms                                                | 3.62 ms: 1.03x faster                                             |
| regex_v8                   | 26.2 ms                                                | 25.5 ms: 1.03x faster                                             |
| regex_dna                  | 218 ms                                                 | 214 ms: 1.02x faster                                              |
| json_loads                 | 27.2 us                                                | 26.6 us: 1.02x faster                                             |
| logging_silent             | 102 ns                                                 | 100 ns: 1.02x faster                                              |
| logging_format             | 6.40 us                                                | 6.31 us: 1.01x faster                                             |
| connected_components       | 444 ms                                                 | 439 ms: 1.01x faster                                              |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 101 ms: 1.00x faster                                              |
| coverage                   | 84.0 ms                                                | 83.6 ms: 1.00x faster                                             |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                              |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                              |
| pprint_pformat             | 1.49 sec                                               | 1.51 sec: 1.01x slower                                            |
| chaos                      | 58.1 ms                                                | 59.0 ms: 1.02x slower                                             |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                             |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                              |
| deltablue                  | 3.23 ms                                                | 3.30 ms: 1.02x slower                                             |
| python_startup_no_site     | 6.96 ms                                                | 7.12 ms: 1.02x slower                                             |
| html5lib                   | 64.2 ms                                                | 65.8 ms: 1.03x slower                                             |
| json_dumps                 | 10.6 ms                                                | 10.8 ms: 1.03x slower                                             |
| django_template            | 35.2 ms                                                | 36.2 ms: 1.03x slower                                             |
| pickle_pure_python         | 310 us                                                 | 321 us: 1.03x slower                                              |
| async_generators           | 436 ms                                                 | 452 ms: 1.04x slower                                              |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.7 ms: 1.04x slower                                             |
| 2to3                       | 267 ms                                                 | 277 ms: 1.04x slower                                              |
| regex_compile              | 132 ms                                                 | 137 ms: 1.04x slower                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 567 ms: 1.04x slower                                              |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.05x slower                                             |
| comprehensions             | 16.5 us                                                | 17.3 us: 1.05x slower                                             |
| sqlglot_normalize          | 108 ms                                                 | 113 ms: 1.05x slower                                              |
| dulwich_log                | 64.3 ms                                                | 67.8 ms: 1.05x slower                                             |
| raytrace                   | 267 ms                                                 | 285 ms: 1.07x slower                                              |
| sqlglot_transpile          | 1.58 ms                                                | 1.70 ms: 1.07x slower                                             |
| genshi_text                | 23.5 ms                                                | 25.2 ms: 1.07x slower                                             |
| sympy_expand               | 463 ms                                                 | 502 ms: 1.08x slower                                              |
| bench_thread_pool          | 822 us                                                 | 891 us: 1.08x slower                                              |
| sqlglot_optimize           | 53.7 ms                                                | 59.1 ms: 1.10x slower                                             |
| gc_traversal               | 4.37 ms                                                | 4.81 ms: 1.10x slower                                             |
| sqlalchemy_declarative     | 133 ms                                                 | 147 ms: 1.10x slower                                              |
| sympy_str                  | 275 ms                                                 | 303 ms: 1.10x slower                                              |
| nqueens                    | 78.4 ms                                                | 87.9 ms: 1.12x slower                                             |
| create_gc_cycles           | 2.41 ms                                                | 2.70 ms: 1.12x slower                                             |
| docutils                   | 2.59 sec                                               | 2.92 sec: 1.13x slower                                            |
| sphinx                     | 1.03 sec                                               | 1.17 sec: 1.14x slower                                            |
| async_tree_io_tg           | 857 ms                                                 | 978 ms: 1.14x slower                                              |
| genshi_xml                 | 50.9 ms                                                | 58.8 ms: 1.16x slower                                             |
| sympy_sum                  | 150 ms                                                 | 174 ms: 1.16x slower                                              |
| hexiom                     | 6.16 ms                                                | 7.15 ms: 1.16x slower                                             |
| sympy_integrate            | 19.9 ms                                                | 23.2 ms: 1.17x slower                                             |
| pylint                     | 313 ms                                                 | 379 ms: 1.21x slower                                              |
| generators                 | 29.0 ms                                                | 36.2 ms: 1.25x slower                                             |
| k_core                     | 2.35 sec                                               | 3.63 sec: 1.54x slower                                            |
| bench_mp_pool              | 24.0 ms                                                | 82.5 ms: 3.44x slower                                             |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                      |

Benchmark hidden because not significant (9): shortest_path, pprint_safe_repr, spectral_norm, coroutines, logging_simple, async_tree_cpu_io_mixed, async_tree_none_tg, typing_runtime_protocols, async_tree_io
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241108-3.14.0a1+-48ade84-JIT/bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84.json: sqlite_synth

- Geometric mean (including insignificant results): 1.004x slower
# HPT report

- Reliability score: 79.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x