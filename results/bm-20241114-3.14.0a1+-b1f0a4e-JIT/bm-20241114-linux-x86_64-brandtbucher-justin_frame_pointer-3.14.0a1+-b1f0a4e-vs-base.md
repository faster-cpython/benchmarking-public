# Results vs. base

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-x86_64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.021x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 286 ms: 1.02x slower                                                         |
| docutils       | 2.95 sec                                                               | 2.96 sec: 1.01x slower                                                       |
| html5lib       | 67.0 ms                                                                | 66.6 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                | 22.9 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 569 ms: 1.01x slower                                                         |
| async_generators           | 456 ms                                                                 | 460 ms: 1.01x slower                                                         |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (8): async_tree_none_tg, asyncio_websockets, async_tree_io_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.7 ms                                                                | 79.2 ms: 1.03x slower                                                        |
| nbody          | 82.3 ms                                                                | 91.0 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 216 ms                                                                 | 215 ms: 1.01x faster                                                         |
| regex_v8       | 24.6 ms                                                                | 24.8 ms: 1.01x slower                                                        |
| regex_compile  | 140 ms                                                                 | 143 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                                 | 102 ms: 1.02x slower                                                         |
| json_dumps           | 11.1 ms                                                                | 11.3 ms: 1.02x slower                                                        |
| unpickle_pure_python | 219 us                                                                 | 224 us: 1.02x slower                                                         |
| pickle_pure_python   | 321 us                                                                 | 329 us: 1.03x slower                                                         |
| xml_etree_process    | 56.0 ms                                                                | 58.1 ms: 1.04x slower                                                        |
| xml_etree_generate   | 79.6 ms                                                                | 82.8 ms: 1.04x slower                                                        |
| tomli_loads          | 2.00 sec                                                               | 2.08 sec: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                                | 7.11 ms: 1.00x faster                                                        |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 34.3 ms                                                                | 34.6 ms: 1.01x slower                                                        |
| genshi_text     | 25.1 ms                                                                | 25.6 ms: 1.02x slower                                                        |
| mako            | 10.3 ms                                                                | 10.9 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                                | 4.52 ms: 1.05x faster                                                        |
| coroutines                 | 23.2 ms                                                                | 22.9 ms: 1.01x faster                                                        |
| regex_dna                  | 216 ms                                                                 | 215 ms: 1.01x faster                                                         |
| html5lib                   | 67.0 ms                                                                | 66.6 ms: 1.01x faster                                                        |
| create_gc_cycles           | 2.71 ms                                                                | 2.70 ms: 1.01x faster                                                        |
| mdp                        | 2.62 sec                                                               | 2.61 sec: 1.00x faster                                                       |
| python_startup_no_site     | 7.14 ms                                                                | 7.11 ms: 1.00x faster                                                        |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| docutils                   | 2.95 sec                                                               | 2.96 sec: 1.01x slower                                                       |
| sympy_str                  | 305 ms                                                                 | 307 ms: 1.01x slower                                                         |
| pathlib                    | 16.1 ms                                                                | 16.2 ms: 1.01x slower                                                        |
| sqlalchemy_declarative     | 148 ms                                                                 | 149 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 569 ms: 1.01x slower                                                         |
| regex_v8                   | 24.6 ms                                                                | 24.8 ms: 1.01x slower                                                        |
| async_generators           | 456 ms                                                                 | 460 ms: 1.01x slower                                                         |
| subparsers                 | 21.4 ms                                                                | 21.6 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 170 us                                                                 | 171 us: 1.01x slower                                                         |
| thrift                     | 779 us                                                                 | 787 us: 1.01x slower                                                         |
| sympy_integrate            | 23.6 ms                                                                | 23.8 ms: 1.01x slower                                                        |
| django_template            | 34.3 ms                                                                | 34.6 ms: 1.01x slower                                                        |
| sympy_sum                  | 176 ms                                                                 | 178 ms: 1.01x slower                                                         |
| many_optionals             | 1.05 ms                                                                | 1.06 ms: 1.01x slower                                                        |
| raytrace                   | 283 ms                                                                 | 287 ms: 1.01x slower                                                         |
| logging_format             | 6.17 us                                                                | 6.26 us: 1.01x slower                                                        |
| sqlglot_optimize           | 60.3 ms                                                                | 61.3 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.33 ms                                                                | 1.35 ms: 1.02x slower                                                        |
| 2to3                       | 280 ms                                                                 | 286 ms: 1.02x slower                                                         |
| xml_etree_iterparse        | 101 ms                                                                 | 102 ms: 1.02x slower                                                         |
| regex_compile              | 140 ms                                                                 | 143 ms: 1.02x slower                                                         |
| dulwich_log                | 67.7 ms                                                                | 69.1 ms: 1.02x slower                                                        |
| richards_super             | 47.1 ms                                                                | 48.0 ms: 1.02x slower                                                        |
| bench_thread_pool          | 889 us                                                                 | 907 us: 1.02x slower                                                         |
| json_dumps                 | 11.1 ms                                                                | 11.3 ms: 1.02x slower                                                        |
| genshi_text                | 25.1 ms                                                                | 25.6 ms: 1.02x slower                                                        |
| shortest_path              | 482 ms                                                                 | 492 ms: 1.02x slower                                                         |
| sqlglot_transpile          | 1.69 ms                                                                | 1.73 ms: 1.02x slower                                                        |
| meteor_contest             | 109 ms                                                                 | 112 ms: 1.02x slower                                                         |
| unpickle_pure_python       | 219 us                                                                 | 224 us: 1.02x slower                                                         |
| telco                      | 7.67 ms                                                                | 7.85 ms: 1.02x slower                                                        |
| pickle_pure_python         | 321 us                                                                 | 329 us: 1.03x slower                                                         |
| sqlglot_normalize          | 114 ms                                                                 | 118 ms: 1.03x slower                                                         |
| connected_components       | 437 ms                                                                 | 450 ms: 1.03x slower                                                         |
| float                      | 76.7 ms                                                                | 79.2 ms: 1.03x slower                                                        |
| bpe_tokeniser              | 4.53 sec                                                               | 4.68 sec: 1.03x slower                                                       |
| xml_etree_process          | 56.0 ms                                                                | 58.1 ms: 1.04x slower                                                        |
| deepcopy                   | 267 us                                                                 | 278 us: 1.04x slower                                                         |
| xml_etree_generate         | 79.6 ms                                                                | 82.8 ms: 1.04x slower                                                        |
| scimark_lu                 | 113 ms                                                                 | 118 ms: 1.04x slower                                                         |
| logging_simple             | 5.56 us                                                                | 5.78 us: 1.04x slower                                                        |
| nqueens                    | 87.9 ms                                                                | 91.5 ms: 1.04x slower                                                        |
| pprint_safe_repr           | 724 ms                                                                 | 756 ms: 1.04x slower                                                         |
| tomli_loads                | 2.00 sec                                                               | 2.08 sec: 1.04x slower                                                       |
| chaos                      | 59.1 ms                                                                | 61.7 ms: 1.04x slower                                                        |
| fannkuch                   | 389 ms                                                                 | 407 ms: 1.04x slower                                                         |
| deepcopy_reduce            | 2.66 us                                                                | 2.78 us: 1.05x slower                                                        |
| go                         | 133 ms                                                                 | 140 ms: 1.05x slower                                                         |
| pprint_pformat             | 1.51 sec                                                               | 1.59 sec: 1.05x slower                                                       |
| scimark_monte_carlo        | 64.8 ms                                                                | 68.1 ms: 1.05x slower                                                        |
| crypto_pyaes               | 68.5 ms                                                                | 72.2 ms: 1.05x slower                                                        |
| scimark_sor                | 119 ms                                                                 | 125 ms: 1.05x slower                                                         |
| mako                       | 10.3 ms                                                                | 10.9 ms: 1.06x slower                                                        |
| richards                   | 40.7 ms                                                                | 43.2 ms: 1.06x slower                                                        |
| hexiom                     | 7.08 ms                                                                | 7.53 ms: 1.06x slower                                                        |
| logging_silent             | 102 ns                                                                 | 109 ns: 1.07x slower                                                         |
| comprehensions             | 17.5 us                                                                | 18.8 us: 1.07x slower                                                        |
| spectral_norm              | 115 ms                                                                 | 123 ms: 1.07x slower                                                         |
| deepcopy_memo              | 29.6 us                                                                | 31.8 us: 1.07x slower                                                        |
| scimark_fft                | 318 ms                                                                 | 343 ms: 1.08x slower                                                         |
| scimark_sparse_mat_mult    | 4.62 ms                                                                | 5.01 ms: 1.08x slower                                                        |
| generators                 | 36.6 ms                                                                | 39.7 ms: 1.08x slower                                                        |
| pyflate                    | 449 ms                                                                 | 487 ms: 1.09x slower                                                         |
| deltablue                  | 3.31 ms                                                                | 3.61 ms: 1.09x slower                                                        |
| nbody                      | 82.3 ms                                                                | 91.0 ms: 1.11x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (24): coverage, genshi_xml, sympy_expand, pidigits, regex_effbot, bench_mp_pool, json_loads, pycparser, async_tree_none_tg, asyncio_websockets, sqlalchemy_imperative, sqlite_synth, async_tree_io_tg, pylint, xml_etree_parse, sphinx, json, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed, k_core, async_tree_none, async_tree_memoization, djangocms

- Geometric mean (including insignificant results): 1.021x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x