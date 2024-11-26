# Results vs. 3.13.0

- fork: brandtbucher
- ref: 6de23b358e9e3dd796a2
- machine: linux-x86_64
- commit hash: 6de23b3
- commit date: 2024-11-14
- overall geometric mean: 1.119x slower
- HPT reliability: 96.91%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 1.29 sec: 4.82x slower                                                       |
| docutils       | 2.59 sec                                               | 6.92 sec: 2.67x slower                                                       |
| html5lib       | 64.2 ms                                                | 67.2 ms: 1.05x slower                                                        |
| sphinx         | 1.03 sec                                               | 3.01 sec: 2.91x slower                                                       |
| Geometric mean | (ref)                                                  | 2.50x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                                         |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                                         |
| async_tree_none            | 351 ms                                                 | 335 ms: 1.05x faster                                                         |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 586 ms: 1.02x slower                                                         |
| async_tree_io              | 842 ms                                                 | 865 ms: 1.03x slower                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 569 ms: 1.04x slower                                                         |
| async_generators           | 436 ms                                                 | 459 ms: 1.05x slower                                                         |
| async_tree_io_tg           | 857 ms                                                 | 978 ms: 1.14x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 82.1 ms: 1.06x faster                                                        |
| float          | 79.2 ms                                                | 77.0 ms: 1.03x faster                                                        |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.70 ms: 1.01x faster                                                        |
| regex_compile  | 132 ms                                                 | 226 ms: 1.71x slower                                                         |
| regex_v8       | 26.2 ms                                                | 48.9 ms: 1.86x slower                                                        |
| Geometric mean | (ref)                                                  | 1.33x slower                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                       |
| xml_etree_generate   | 86.7 ms                                                | 79.0 ms: 1.10x faster                                                        |
| xml_etree_process    | 60.6 ms                                                | 57.9 ms: 1.05x faster                                                        |
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.05x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 103 ms: 1.02x slower                                                         |
| unpickle_pure_python | 216 us                                                 | 222 us: 1.03x slower                                                         |
| json_loads           | 27.2 us                                                | 34.0 us: 1.25x slower                                                        |
| json_dumps           | 10.6 ms                                                | 13.5 ms: 1.27x slower                                                        |
| pickle_pure_python   | 310 us                                                 | 623 us: 2.01x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.16 ms: 1.03x slower                                                        |
| python_startup         | 12.5 ms                                                | 12.9 ms: 1.03x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.10x faster                                                        |
| django_template | 35.2 ms                                                | 33.8 ms: 1.04x faster                                                        |
| genshi_text     | 23.5 ms                                                | 26.6 ms: 1.13x slower                                                        |
| genshi_xml      | 50.9 ms                                                | 61.8 ms: 1.21x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 271 us: 1.32x faster                                                         |
| deepcopy_memo              | 39.1 us                                                | 30.0 us: 1.31x faster                                                        |
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                                         |
| richards_super             | 54.9 ms                                                | 45.7 ms: 1.20x faster                                                        |
| deepcopy_reduce            | 3.20 us                                                | 2.68 us: 1.20x faster                                                        |
| richards                   | 48.7 ms                                                | 41.1 ms: 1.18x faster                                                        |
| scimark_fft                | 364 ms                                                 | 317 ms: 1.15x faster                                                         |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.47 ms: 1.13x faster                                                        |
| mako                       | 11.1 ms                                                | 10.0 ms: 1.10x faster                                                        |
| tomli_loads                | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                       |
| xml_etree_generate         | 86.7 ms                                                | 79.0 ms: 1.10x faster                                                        |
| crypto_pyaes               | 75.3 ms                                                | 69.4 ms: 1.08x faster                                                        |
| pathlib                    | 17.5 ms                                                | 16.3 ms: 1.08x faster                                                        |
| go                         | 144 ms                                                 | 136 ms: 1.06x faster                                                         |
| nbody                      | 87.0 ms                                                | 82.1 ms: 1.06x faster                                                        |
| fannkuch                   | 404 ms                                                 | 382 ms: 1.06x faster                                                         |
| bpe_tokeniser              | 4.75 sec                                               | 4.49 sec: 1.06x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 418 ms: 1.06x faster                                                         |
| scimark_monte_carlo        | 67.4 ms                                                | 64.3 ms: 1.05x faster                                                        |
| xml_etree_process          | 60.6 ms                                                | 57.9 ms: 1.05x faster                                                        |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.05x faster                                                         |
| scimark_sor                | 124 ms                                                 | 118 ms: 1.05x faster                                                         |
| async_tree_none            | 351 ms                                                 | 335 ms: 1.05x faster                                                         |
| django_template            | 35.2 ms                                                | 33.8 ms: 1.04x faster                                                        |
| mdp                        | 2.72 sec                                               | 2.63 sec: 1.03x faster                                                       |
| logging_format             | 6.40 us                                                | 6.21 us: 1.03x faster                                                        |
| float                      | 79.2 ms                                                | 77.0 ms: 1.03x faster                                                        |
| logging_silent             | 102 ns                                                 | 99.1 ns: 1.03x faster                                                        |
| pprint_safe_repr           | 728 ms                                                 | 711 ms: 1.02x faster                                                         |
| logging_simple             | 5.72 us                                                | 5.61 us: 1.02x faster                                                        |
| connected_components       | 444 ms                                                 | 437 ms: 1.02x faster                                                         |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.01x faster                                                         |
| regex_effbot               | 3.73 ms                                                | 3.70 ms: 1.01x faster                                                        |
| spectral_norm              | 115 ms                                                 | 115 ms: 1.00x faster                                                         |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                         |
| pycparser                  | 1.20 sec                                               | 1.21 sec: 1.01x slower                                                       |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 586 ms: 1.02x slower                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 103 ms: 1.02x slower                                                         |
| typing_runtime_protocols   | 165 us                                                 | 169 us: 1.03x slower                                                         |
| chaos                      | 58.1 ms                                                | 59.7 ms: 1.03x slower                                                        |
| async_tree_io              | 842 ms                                                 | 865 ms: 1.03x slower                                                         |
| python_startup_no_site     | 6.96 ms                                                | 7.16 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 216 us                                                 | 222 us: 1.03x slower                                                         |
| deltablue                  | 3.23 ms                                                | 3.32 ms: 1.03x slower                                                        |
| python_startup             | 12.5 ms                                                | 12.9 ms: 1.03x slower                                                        |
| raytrace                   | 267 ms                                                 | 276 ms: 1.03x slower                                                         |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 569 ms: 1.04x slower                                                         |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.8 ms: 1.04x slower                                                        |
| gc_traversal               | 4.37 ms                                                | 4.57 ms: 1.04x slower                                                        |
| html5lib                   | 64.2 ms                                                | 67.2 ms: 1.05x slower                                                        |
| scimark_lu                 | 113 ms                                                 | 119 ms: 1.05x slower                                                         |
| async_generators           | 436 ms                                                 | 459 ms: 1.05x slower                                                         |
| comprehensions             | 16.5 us                                                | 17.4 us: 1.06x slower                                                        |
| sqlglot_transpile          | 1.58 ms                                                | 1.70 ms: 1.07x slower                                                        |
| pyflate                    | 471 ms                                                 | 509 ms: 1.08x slower                                                         |
| bench_thread_pool          | 822 us                                                 | 889 us: 1.08x slower                                                         |
| create_gc_cycles           | 2.41 ms                                                | 2.70 ms: 1.12x slower                                                        |
| genshi_text                | 23.5 ms                                                | 26.6 ms: 1.13x slower                                                        |
| nqueens                    | 78.4 ms                                                | 89.2 ms: 1.14x slower                                                        |
| async_tree_io_tg           | 857 ms                                                 | 978 ms: 1.14x slower                                                         |
| json                       | 5.36 ms                                                | 6.16 ms: 1.15x slower                                                        |
| hexiom                     | 6.16 ms                                                | 7.10 ms: 1.15x slower                                                        |
| genshi_xml                 | 50.9 ms                                                | 61.8 ms: 1.21x slower                                                        |
| telco                      | 8.54 ms                                                | 10.4 ms: 1.22x slower                                                        |
| generators                 | 29.0 ms                                                | 36.1 ms: 1.25x slower                                                        |
| json_loads                 | 27.2 us                                                | 34.0 us: 1.25x slower                                                        |
| json_dumps                 | 10.6 ms                                                | 13.5 ms: 1.27x slower                                                        |
| sympy_expand               | 463 ms                                                 | 599 ms: 1.29x slower                                                         |
| sympy_integrate            | 19.9 ms                                                | 26.3 ms: 1.32x slower                                                        |
| thrift                     | 809 us                                                 | 1.10 ms: 1.36x slower                                                        |
| dulwich_log                | 64.3 ms                                                | 96.5 ms: 1.50x slower                                                        |
| k_core                     | 2.35 sec                                               | 3.58 sec: 1.52x slower                                                       |
| sympy_str                  | 275 ms                                                 | 457 ms: 1.66x slower                                                         |
| regex_compile              | 132 ms                                                 | 226 ms: 1.71x slower                                                         |
| sqlglot_normalize          | 108 ms                                                 | 194 ms: 1.80x slower                                                         |
| regex_v8                   | 26.2 ms                                                | 48.9 ms: 1.86x slower                                                        |
| pickle_pure_python         | 310 us                                                 | 623 us: 2.01x slower                                                         |
| sympy_sum                  | 150 ms                                                 | 317 ms: 2.11x slower                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 284 ms: 2.13x slower                                                         |
| sqlglot_optimize           | 53.7 ms                                                | 140 ms: 2.61x slower                                                         |
| docutils                   | 2.59 sec                                               | 6.92 sec: 2.67x slower                                                       |
| sphinx                     | 1.03 sec                                               | 3.01 sec: 2.91x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 108 ms: 4.49x slower                                                         |
| 2to3                       | 267 ms                                                 | 1.29 sec: 4.82x slower                                                       |
| pylint                     | 313 ms                                                 | 2.03 sec: 6.50x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.16x slower                                                                 |

Benchmark hidden because not significant (6): pprint_pformat, regex_dna, shortest_path, asyncio_websockets, coverage, async_tree_none_tg
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (2) of results/bm-20241114-3.14.0a1+-6de23b3-JIT/bm-20241114-linux-x86_64-brandtbucher-6de23b358e9e3dd796a2-3.14.0a1+-6de23b3.json: djangocms, sqlite_synth

- Geometric mean (including insignificant results): 1.119x slower
# HPT report

- Reliability score: 96.91% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x