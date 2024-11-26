# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-x86_64
- commit hash: 925b70b
- commit date: 2024-11-14
- overall geometric mean: 1.031x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 286 ms: 1.07x slower                                                         |
| docutils       | 2.59 sec                                               | 2.97 sec: 1.15x slower                                                       |
| html5lib       | 64.2 ms                                                | 67.9 ms: 1.06x slower                                                        |
| sphinx         | 1.03 sec                                               | 1.19 sec: 1.15x slower                                                       |
| Geometric mean | (ref)                                                  | 1.11x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 381 ms: 1.22x faster                                                         |
| async_tree_memoization     | 442 ms                                                 | 425 ms: 1.04x faster                                                         |
| async_tree_none            | 351 ms                                                 | 337 ms: 1.04x faster                                                         |
| coroutines                 | 22.7 ms                                                | 22.8 ms: 1.01x slower                                                        |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 564 ms: 1.03x slower                                                         |
| async_tree_io              | 842 ms                                                 | 876 ms: 1.04x slower                                                         |
| async_generators           | 436 ms                                                 | 455 ms: 1.04x slower                                                         |
| async_tree_io_tg           | 857 ms                                                 | 984 ms: 1.15x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                         |
| nbody          | 87.0 ms                                                | 90.0 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                        |
| regex_dna      | 218 ms                                                 | 217 ms: 1.01x faster                                                         |
| regex_effbot   | 3.73 ms                                                | 3.72 ms: 1.00x faster                                                        |
| regex_compile  | 132 ms                                                 | 144 ms: 1.09x slower                                                         |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 82.5 ms: 1.05x faster                                                        |
| xml_etree_process    | 60.6 ms                                                | 57.8 ms: 1.05x faster                                                        |
| tomli_loads          | 2.14 sec                                               | 2.05 sec: 1.05x faster                                                       |
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.05x faster                                                         |
| json_loads           | 27.2 us                                                | 27.0 us: 1.01x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 102 ms: 1.01x slower                                                         |
| unpickle_pure_python | 216 us                                                 | 223 us: 1.04x slower                                                         |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                        |
| pickle_pure_python   | 310 us                                                 | 332 us: 1.07x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.11 ms: 1.02x slower                                                        |
| python_startup         | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.8 ms: 1.02x faster                                                        |
| django_template | 35.2 ms                                                | 34.6 ms: 1.01x faster                                                        |
| genshi_text     | 23.5 ms                                                | 27.2 ms: 1.16x slower                                                        |
| genshi_xml      | 50.9 ms                                                | 62.0 ms: 1.22x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.08x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 281 us: 1.27x faster                                                         |
| deepcopy_memo              | 39.1 us                                                | 32.0 us: 1.22x faster                                                        |
| async_tree_memoization_tg  | 464 ms                                                 | 381 ms: 1.22x faster                                                         |
| richards_super             | 54.9 ms                                                | 47.9 ms: 1.15x faster                                                        |
| deepcopy_reduce            | 3.20 us                                                | 2.79 us: 1.15x faster                                                        |
| richards                   | 48.7 ms                                                | 43.2 ms: 1.13x faster                                                        |
| telco                      | 8.54 ms                                                | 7.83 ms: 1.09x faster                                                        |
| scimark_fft                | 364 ms                                                 | 337 ms: 1.08x faster                                                         |
| pathlib                    | 17.5 ms                                                | 16.4 ms: 1.07x faster                                                        |
| json                       | 5.36 ms                                                | 5.02 ms: 1.07x faster                                                        |
| regex_v8                   | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                        |
| xml_etree_generate         | 86.7 ms                                                | 82.5 ms: 1.05x faster                                                        |
| xml_etree_process          | 60.6 ms                                                | 57.8 ms: 1.05x faster                                                        |
| logging_format             | 6.40 us                                                | 6.11 us: 1.05x faster                                                        |
| tomli_loads                | 2.14 sec                                               | 2.05 sec: 1.05x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.05x faster                                                         |
| crypto_pyaes               | 75.3 ms                                                | 72.3 ms: 1.04x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 425 ms: 1.04x faster                                                         |
| async_tree_none            | 351 ms                                                 | 337 ms: 1.04x faster                                                         |
| go                         | 144 ms                                                 | 139 ms: 1.03x faster                                                         |
| thrift                     | 809 us                                                 | 785 us: 1.03x faster                                                         |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                       |
| mako                       | 11.1 ms                                                | 10.8 ms: 1.02x faster                                                        |
| logging_simple             | 5.72 us                                                | 5.60 us: 1.02x faster                                                        |
| bpe_tokeniser              | 4.75 sec                                               | 4.67 sec: 1.02x faster                                                       |
| django_template            | 35.2 ms                                                | 34.6 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.97 ms: 1.01x faster                                                        |
| json_loads                 | 27.2 us                                                | 27.0 us: 1.01x faster                                                        |
| regex_dna                  | 218 ms                                                 | 217 ms: 1.01x faster                                                         |
| scimark_monte_carlo        | 67.4 ms                                                | 67.2 ms: 1.00x faster                                                        |
| regex_effbot               | 3.73 ms                                                | 3.72 ms: 1.00x faster                                                        |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                         |
| coroutines                 | 22.7 ms                                                | 22.8 ms: 1.01x slower                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 102 ms: 1.01x slower                                                         |
| mdp                        | 2.72 sec                                               | 2.75 sec: 1.01x slower                                                       |
| coverage                   | 84.0 ms                                                | 84.9 ms: 1.01x slower                                                        |
| scimark_sor                | 124 ms                                                 | 126 ms: 1.02x slower                                                         |
| connected_components       | 444 ms                                                 | 453 ms: 1.02x slower                                                         |
| python_startup_no_site     | 6.96 ms                                                | 7.11 ms: 1.02x slower                                                        |
| pyflate                    | 471 ms                                                 | 482 ms: 1.02x slower                                                         |
| python_startup             | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                        |
| shortest_path              | 481 ms                                                 | 495 ms: 1.03x slower                                                         |
| meteor_contest             | 109 ms                                                 | 112 ms: 1.03x slower                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 564 ms: 1.03x slower                                                         |
| pprint_pformat             | 1.49 sec                                               | 1.54 sec: 1.03x slower                                                       |
| nbody                      | 87.0 ms                                                | 90.0 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 216 us                                                 | 223 us: 1.04x slower                                                         |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.7 ms: 1.04x slower                                                        |
| async_tree_io              | 842 ms                                                 | 876 ms: 1.04x slower                                                         |
| async_generators           | 436 ms                                                 | 455 ms: 1.04x slower                                                         |
| pprint_safe_repr           | 728 ms                                                 | 760 ms: 1.04x slower                                                         |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                        |
| scimark_lu                 | 113 ms                                                 | 119 ms: 1.06x slower                                                         |
| html5lib                   | 64.2 ms                                                | 67.9 ms: 1.06x slower                                                        |
| dulwich_log                | 64.3 ms                                                | 68.1 ms: 1.06x slower                                                        |
| typing_runtime_protocols   | 165 us                                                 | 175 us: 1.06x slower                                                         |
| logging_silent             | 102 ns                                                 | 108 ns: 1.06x slower                                                         |
| spectral_norm              | 115 ms                                                 | 122 ms: 1.06x slower                                                         |
| gc_traversal               | 4.37 ms                                                | 4.64 ms: 1.06x slower                                                        |
| chaos                      | 58.1 ms                                                | 61.9 ms: 1.07x slower                                                        |
| sqlglot_parse              | 1.27 ms                                                | 1.36 ms: 1.07x slower                                                        |
| pickle_pure_python         | 310 us                                                 | 332 us: 1.07x slower                                                         |
| 2to3                       | 267 ms                                                 | 286 ms: 1.07x slower                                                         |
| raytrace                   | 267 ms                                                 | 288 ms: 1.08x slower                                                         |
| regex_compile              | 132 ms                                                 | 144 ms: 1.09x slower                                                         |
| sqlglot_transpile          | 1.58 ms                                                | 1.73 ms: 1.09x slower                                                        |
| sqlglot_normalize          | 108 ms                                                 | 118 ms: 1.09x slower                                                         |
| sympy_expand               | 463 ms                                                 | 510 ms: 1.10x slower                                                         |
| bench_thread_pool          | 822 us                                                 | 908 us: 1.11x slower                                                         |
| deltablue                  | 3.23 ms                                                | 3.57 ms: 1.11x slower                                                        |
| sympy_str                  | 275 ms                                                 | 307 ms: 1.12x slower                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 149 ms: 1.12x slower                                                         |
| create_gc_cycles           | 2.41 ms                                                | 2.70 ms: 1.12x slower                                                        |
| comprehensions             | 16.5 us                                                | 18.8 us: 1.14x slower                                                        |
| docutils                   | 2.59 sec                                               | 2.97 sec: 1.15x slower                                                       |
| sqlglot_optimize           | 53.7 ms                                                | 61.7 ms: 1.15x slower                                                        |
| async_tree_io_tg           | 857 ms                                                 | 984 ms: 1.15x slower                                                         |
| sphinx                     | 1.03 sec                                               | 1.19 sec: 1.15x slower                                                       |
| genshi_text                | 23.5 ms                                                | 27.2 ms: 1.16x slower                                                        |
| nqueens                    | 78.4 ms                                                | 92.2 ms: 1.18x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 178 ms: 1.18x slower                                                         |
| sympy_integrate            | 19.9 ms                                                | 23.9 ms: 1.20x slower                                                        |
| pylint                     | 313 ms                                                 | 380 ms: 1.22x slower                                                         |
| genshi_xml                 | 50.9 ms                                                | 62.0 ms: 1.22x slower                                                        |
| hexiom                     | 6.16 ms                                                | 7.57 ms: 1.23x slower                                                        |
| generators                 | 29.0 ms                                                | 41.9 ms: 1.45x slower                                                        |
| k_core                     | 2.35 sec                                               | 3.64 sec: 1.55x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 84.6 ms: 3.53x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                                 |

Benchmark hidden because not significant (5): float, async_tree_cpu_io_mixed, fannkuch, asyncio_websockets, async_tree_none_tg
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (2) of results/bm-20241114-3.14.0a1+-925b70b-JIT/bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b.json: djangocms, sqlite_synth

- Geometric mean (including insignificant results): 1.031x slower
# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.08x