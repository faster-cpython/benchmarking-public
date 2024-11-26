# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-x86_64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.029x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 286 ms: 1.07x slower                                                         |
| docutils       | 2.59 sec                                               | 2.96 sec: 1.14x slower                                                       |
| html5lib       | 64.2 ms                                                | 66.6 ms: 1.04x slower                                                        |
| sphinx         | 1.03 sec                                               | 1.19 sec: 1.15x slower                                                       |
| Geometric mean | (ref)                                                  | 1.10x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 383 ms: 1.21x faster                                                         |
| async_tree_none            | 351 ms                                                 | 335 ms: 1.05x faster                                                         |
| async_tree_memoization     | 442 ms                                                 | 424 ms: 1.04x faster                                                         |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                        |
| async_tree_io              | 842 ms                                                 | 867 ms: 1.03x slower                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 569 ms: 1.04x slower                                                         |
| async_generators           | 436 ms                                                 | 460 ms: 1.06x slower                                                         |
| async_tree_io_tg           | 857 ms                                                 | 981 ms: 1.15x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 91.0 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                        |
| regex_dna      | 218 ms                                                 | 215 ms: 1.02x faster                                                         |
| regex_effbot   | 3.73 ms                                                | 3.77 ms: 1.01x slower                                                        |
| regex_compile  | 132 ms                                                 | 143 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 82.8 ms: 1.05x faster                                                        |
| xml_etree_process    | 60.6 ms                                                | 58.1 ms: 1.04x faster                                                        |
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.04x faster                                                         |
| tomli_loads          | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                       |
| json_loads           | 27.2 us                                                | 26.8 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 102 ms: 1.01x slower                                                         |
| unpickle_pure_python | 216 us                                                 | 224 us: 1.04x slower                                                         |
| pickle_pure_python   | 310 us                                                 | 329 us: 1.06x slower                                                         |
| json_dumps           | 10.6 ms                                                | 11.3 ms: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.11 ms: 1.02x slower                                                        |
| python_startup         | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.9 ms: 1.02x faster                                                        |
| django_template | 35.2 ms                                                | 34.6 ms: 1.01x faster                                                        |
| genshi_text     | 23.5 ms                                                | 25.6 ms: 1.09x slower                                                        |
| genshi_xml      | 50.9 ms                                                | 59.8 ms: 1.17x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 278 us: 1.29x faster                                                         |
| deepcopy_memo              | 39.1 us                                                | 31.8 us: 1.23x faster                                                        |
| async_tree_memoization_tg  | 464 ms                                                 | 383 ms: 1.21x faster                                                         |
| deepcopy_reduce            | 3.20 us                                                | 2.78 us: 1.15x faster                                                        |
| richards_super             | 54.9 ms                                                | 48.0 ms: 1.14x faster                                                        |
| richards                   | 48.7 ms                                                | 43.2 ms: 1.13x faster                                                        |
| telco                      | 8.54 ms                                                | 7.85 ms: 1.09x faster                                                        |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                        |
| json                       | 5.36 ms                                                | 5.01 ms: 1.07x faster                                                        |
| scimark_fft                | 364 ms                                                 | 343 ms: 1.06x faster                                                         |
| regex_v8                   | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                        |
| xml_etree_generate         | 86.7 ms                                                | 82.8 ms: 1.05x faster                                                        |
| async_tree_none            | 351 ms                                                 | 335 ms: 1.05x faster                                                         |
| xml_etree_process          | 60.6 ms                                                | 58.1 ms: 1.04x faster                                                        |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.04x faster                                                         |
| mdp                        | 2.72 sec                                               | 2.61 sec: 1.04x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 424 ms: 1.04x faster                                                         |
| crypto_pyaes               | 75.3 ms                                                | 72.2 ms: 1.04x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                       |
| go                         | 144 ms                                                 | 140 ms: 1.03x faster                                                         |
| thrift                     | 809 us                                                 | 787 us: 1.03x faster                                                         |
| tomli_loads                | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                       |
| logging_format             | 6.40 us                                                | 6.26 us: 1.02x faster                                                        |
| mako                       | 11.1 ms                                                | 10.9 ms: 1.02x faster                                                        |
| regex_dna                  | 218 ms                                                 | 215 ms: 1.02x faster                                                         |
| json_loads                 | 27.2 us                                                | 26.8 us: 1.02x faster                                                        |
| django_template            | 35.2 ms                                                | 34.6 ms: 1.01x faster                                                        |
| bpe_tokeniser              | 4.75 sec                                               | 4.68 sec: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.01 ms: 1.01x faster                                                        |
| coverage                   | 84.0 ms                                                | 84.4 ms: 1.01x slower                                                        |
| scimark_monte_carlo        | 67.4 ms                                                | 68.1 ms: 1.01x slower                                                        |
| regex_effbot               | 3.73 ms                                                | 3.77 ms: 1.01x slower                                                        |
| coroutines                 | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                        |
| logging_simple             | 5.72 us                                                | 5.78 us: 1.01x slower                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 102 ms: 1.01x slower                                                         |
| connected_components       | 444 ms                                                 | 450 ms: 1.01x slower                                                         |
| scimark_sor                | 124 ms                                                 | 125 ms: 1.01x slower                                                         |
| python_startup_no_site     | 6.96 ms                                                | 7.11 ms: 1.02x slower                                                        |
| shortest_path              | 481 ms                                                 | 492 ms: 1.02x slower                                                         |
| meteor_contest             | 109 ms                                                 | 112 ms: 1.03x slower                                                         |
| python_startup             | 12.5 ms                                                | 12.8 ms: 1.03x slower                                                        |
| async_tree_io              | 842 ms                                                 | 867 ms: 1.03x slower                                                         |
| pyflate                    | 471 ms                                                 | 487 ms: 1.03x slower                                                         |
| gc_traversal               | 4.37 ms                                                | 4.52 ms: 1.04x slower                                                        |
| html5lib                   | 64.2 ms                                                | 66.6 ms: 1.04x slower                                                        |
| pprint_safe_repr           | 728 ms                                                 | 756 ms: 1.04x slower                                                         |
| unpickle_pure_python       | 216 us                                                 | 224 us: 1.04x slower                                                         |
| typing_runtime_protocols   | 165 us                                                 | 171 us: 1.04x slower                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 569 ms: 1.04x slower                                                         |
| sqlalchemy_imperative      | 17.1 ms                                                | 17.9 ms: 1.05x slower                                                        |
| nbody                      | 87.0 ms                                                | 91.0 ms: 1.05x slower                                                        |
| scimark_lu                 | 113 ms                                                 | 118 ms: 1.05x slower                                                         |
| async_generators           | 436 ms                                                 | 460 ms: 1.06x slower                                                         |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                        |
| pickle_pure_python         | 310 us                                                 | 329 us: 1.06x slower                                                         |
| chaos                      | 58.1 ms                                                | 61.7 ms: 1.06x slower                                                        |
| pprint_pformat             | 1.49 sec                                               | 1.59 sec: 1.06x slower                                                       |
| spectral_norm              | 115 ms                                                 | 123 ms: 1.07x slower                                                         |
| json_dumps                 | 10.6 ms                                                | 11.3 ms: 1.07x slower                                                        |
| 2to3                       | 267 ms                                                 | 286 ms: 1.07x slower                                                         |
| logging_silent             | 102 ns                                                 | 109 ns: 1.07x slower                                                         |
| raytrace                   | 267 ms                                                 | 287 ms: 1.07x slower                                                         |
| dulwich_log                | 64.3 ms                                                | 69.1 ms: 1.07x slower                                                        |
| regex_compile              | 132 ms                                                 | 143 ms: 1.08x slower                                                         |
| genshi_text                | 23.5 ms                                                | 25.6 ms: 1.09x slower                                                        |
| sqlglot_transpile          | 1.58 ms                                                | 1.73 ms: 1.09x slower                                                        |
| sqlglot_normalize          | 108 ms                                                 | 118 ms: 1.09x slower                                                         |
| sympy_expand               | 463 ms                                                 | 508 ms: 1.10x slower                                                         |
| bench_thread_pool          | 822 us                                                 | 907 us: 1.10x slower                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 149 ms: 1.11x slower                                                         |
| sympy_str                  | 275 ms                                                 | 307 ms: 1.12x slower                                                         |
| deltablue                  | 3.23 ms                                                | 3.61 ms: 1.12x slower                                                        |
| create_gc_cycles           | 2.41 ms                                                | 2.70 ms: 1.12x slower                                                        |
| comprehensions             | 16.5 us                                                | 18.8 us: 1.14x slower                                                        |
| sqlglot_optimize           | 53.7 ms                                                | 61.3 ms: 1.14x slower                                                        |
| docutils                   | 2.59 sec                                               | 2.96 sec: 1.14x slower                                                       |
| async_tree_io_tg           | 857 ms                                                 | 981 ms: 1.15x slower                                                         |
| sphinx                     | 1.03 sec                                               | 1.19 sec: 1.15x slower                                                       |
| nqueens                    | 78.4 ms                                                | 91.5 ms: 1.17x slower                                                        |
| genshi_xml                 | 50.9 ms                                                | 59.8 ms: 1.17x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 178 ms: 1.18x slower                                                         |
| sympy_integrate            | 19.9 ms                                                | 23.8 ms: 1.20x slower                                                        |
| pylint                     | 313 ms                                                 | 381 ms: 1.22x slower                                                         |
| hexiom                     | 6.16 ms                                                | 7.53 ms: 1.22x slower                                                        |
| generators                 | 29.0 ms                                                | 39.7 ms: 1.37x slower                                                        |
| k_core                     | 2.35 sec                                               | 3.65 sec: 1.55x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 84.8 ms: 3.53x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                                 |

Benchmark hidden because not significant (6): float, asyncio_websockets, pidigits, async_tree_none_tg, fannkuch, async_tree_cpu_io_mixed
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.029x slower
# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.08x