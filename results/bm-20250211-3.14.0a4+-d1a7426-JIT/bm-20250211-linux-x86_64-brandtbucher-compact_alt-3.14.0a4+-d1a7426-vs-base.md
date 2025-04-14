# Results vs. base

- fork: brandtbucher
- ref: compact_alt
- machine: linux-x86_64
- commit hash: d1a7426
- commit date: 2025-02-11
- overall geometric mean: 1.024x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 258 ms                                                                 | 256 ms: 1.01x faster                                                |
| docutils       | 2.66 sec                                                               | 2.71 sec: 1.02x slower                                              |
| html5lib       | 60.8 ms                                                                | 59.8 ms: 1.02x faster                                               |
| sphinx         | 1.01 sec                                                               | 1.04 sec: 1.03x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_generators           | 409 ms                                                                 | 404 ms: 1.01x faster                                                |
| coroutines                 | 23.6 ms                                                                | 23.9 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed    | 501 ms                                                                 | 511 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg | 493 ms                                                                 | 504 ms: 1.02x slower                                                |
| async_tree_none            | 269 ms                                                                 | 275 ms: 1.02x slower                                                |
| async_tree_none_tg         | 260 ms                                                                 | 268 ms: 1.03x slower                                                |
| async_tree_memoization     | 329 ms                                                                 | 340 ms: 1.03x slower                                                |
| async_tree_memoization_tg  | 320 ms                                                                 | 334 ms: 1.04x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 95.5 ms                                                                | 93.7 ms: 1.02x faster                                               |
| pidigits       | 186 ms                                                                 | 189 ms: 1.02x slower                                                |
| float          | 70.8 ms                                                                | 75.5 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.18 ms                                                                | 3.11 ms: 1.02x faster                                               |
| regex_v8       | 23.8 ms                                                                | 24.2 ms: 1.02x slower                                               |
| regex_dna      | 206 ms                                                                 | 210 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.0 ms                                                                | 11.6 ms: 1.04x faster                                               |
| json_loads           | 28.9 us                                                                | 28.6 us: 1.01x faster                                               |
| xml_etree_parse      | 137 ms                                                                 | 140 ms: 1.02x slower                                                |
| xml_etree_generate   | 78.4 ms                                                                | 81.2 ms: 1.04x slower                                               |
| pickle_pure_python   | 315 us                                                                 | 330 us: 1.05x slower                                                |
| xml_etree_iterparse  | 95.4 ms                                                                | 101 ms: 1.06x slower                                                |
| xml_etree_process    | 55.1 ms                                                                | 58.6 ms: 1.06x slower                                               |
| unpickle_pure_python | 201 us                                                                 | 223 us: 1.11x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.03x slower                                                        |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                               |
| python_startup_no_site | 7.05 ms                                                                | 7.08 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 31.8 ms                                                                | 33.5 ms: 1.05x slower                                               |
| genshi_text     | 21.8 ms                                                                | 24.4 ms: 1.12x slower                                               |
| mako            | 9.88 ms                                                                | 11.2 ms: 1.13x slower                                               |
| genshi_xml      | 49.5 ms                                                                | 56.4 ms: 1.14x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.11x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| go                         | 129 ms                                                                 | 124 ms: 1.04x faster                                                |
| hexiom                     | 6.84 ms                                                                | 6.61 ms: 1.04x faster                                               |
| json_dumps                 | 12.0 ms                                                                | 11.6 ms: 1.04x faster                                               |
| logging_format             | 6.33 us                                                                | 6.14 us: 1.03x faster                                               |
| connected_components       | 439 ms                                                                 | 426 ms: 1.03x faster                                                |
| nqueens                    | 90.7 ms                                                                | 88.0 ms: 1.03x faster                                               |
| shortest_path              | 482 ms                                                                 | 470 ms: 1.03x faster                                                |
| regex_effbot               | 3.18 ms                                                                | 3.11 ms: 1.02x faster                                               |
| nbody                      | 95.5 ms                                                                | 93.7 ms: 1.02x faster                                               |
| pprint_pformat             | 1.57 sec                                                               | 1.55 sec: 1.02x faster                                              |
| html5lib                   | 60.8 ms                                                                | 59.8 ms: 1.02x faster                                               |
| meteor_contest             | 107 ms                                                                 | 105 ms: 1.02x faster                                                |
| async_generators           | 409 ms                                                                 | 404 ms: 1.01x faster                                                |
| json_loads                 | 28.9 us                                                                | 28.6 us: 1.01x faster                                               |
| logging_simple             | 5.69 us                                                                | 5.64 us: 1.01x faster                                               |
| 2to3                       | 258 ms                                                                 | 256 ms: 1.01x faster                                                |
| telco                      | 7.67 ms                                                                | 7.61 ms: 1.01x faster                                               |
| python_startup             | 12.8 ms                                                                | 12.9 ms: 1.00x slower                                               |
| python_startup_no_site     | 7.05 ms                                                                | 7.08 ms: 1.01x slower                                               |
| comprehensions             | 17.2 us                                                                | 17.3 us: 1.01x slower                                               |
| coverage                   | 89.0 ms                                                                | 89.6 ms: 1.01x slower                                               |
| bench_mp_pool              | 80.9 ms                                                                | 81.4 ms: 1.01x slower                                               |
| subparsers                 | 20.8 ms                                                                | 21.0 ms: 1.01x slower                                               |
| scimark_fft                | 313 ms                                                                 | 315 ms: 1.01x slower                                                |
| many_optionals             | 957 us                                                                 | 965 us: 1.01x slower                                                |
| thrift                     | 773 us                                                                 | 780 us: 1.01x slower                                                |
| create_gc_cycles           | 2.47 ms                                                                | 2.49 ms: 1.01x slower                                               |
| bpe_tokeniser              | 4.38 sec                                                               | 4.42 sec: 1.01x slower                                              |
| sqlalchemy_imperative      | 16.8 ms                                                                | 17.0 ms: 1.01x slower                                               |
| coroutines                 | 23.6 ms                                                                | 23.9 ms: 1.01x slower                                               |
| pprint_safe_repr           | 756 ms                                                                 | 765 ms: 1.01x slower                                                |
| bench_thread_pool          | 887 us                                                                 | 898 us: 1.01x slower                                                |
| sqlalchemy_declarative     | 130 ms                                                                 | 132 ms: 1.01x slower                                                |
| regex_v8                   | 23.8 ms                                                                | 24.2 ms: 1.02x slower                                               |
| dulwich_log                | 66.5 ms                                                                | 67.5 ms: 1.02x slower                                               |
| sympy_integrate            | 20.2 ms                                                                | 20.5 ms: 1.02x slower                                               |
| pidigits                   | 186 ms                                                                 | 189 ms: 1.02x slower                                                |
| crypto_pyaes               | 69.4 ms                                                                | 70.6 ms: 1.02x slower                                               |
| xml_etree_parse            | 137 ms                                                                 | 140 ms: 1.02x slower                                                |
| richards_super             | 50.9 ms                                                                | 51.8 ms: 1.02x slower                                               |
| docutils                   | 2.66 sec                                                               | 2.71 sec: 1.02x slower                                              |
| async_tree_cpu_io_mixed    | 501 ms                                                                 | 511 ms: 1.02x slower                                                |
| regex_dna                  | 206 ms                                                                 | 210 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg | 493 ms                                                                 | 504 ms: 1.02x slower                                                |
| async_tree_none            | 269 ms                                                                 | 275 ms: 1.02x slower                                                |
| sympy_str                  | 275 ms                                                                 | 281 ms: 1.02x slower                                                |
| raytrace                   | 274 ms                                                                 | 280 ms: 1.02x slower                                                |
| sympy_sum                  | 151 ms                                                                 | 155 ms: 1.03x slower                                                |
| sqlite_synth               | 2.70 us                                                                | 2.77 us: 1.03x slower                                               |
| pathlib                    | 16.3 ms                                                                | 16.7 ms: 1.03x slower                                               |
| sqlglot_parse              | 1.28 ms                                                                | 1.31 ms: 1.03x slower                                               |
| pyflate                    | 444 ms                                                                 | 457 ms: 1.03x slower                                                |
| sphinx                     | 1.01 sec                                                               | 1.04 sec: 1.03x slower                                              |
| sqlglot_transpile          | 1.58 ms                                                                | 1.63 ms: 1.03x slower                                               |
| richards                   | 44.4 ms                                                                | 45.7 ms: 1.03x slower                                               |
| async_tree_none_tg         | 260 ms                                                                 | 268 ms: 1.03x slower                                                |
| async_tree_memoization     | 329 ms                                                                 | 340 ms: 1.03x slower                                                |
| scimark_sparse_mat_mult    | 4.46 ms                                                                | 4.62 ms: 1.03x slower                                               |
| sympy_expand               | 468 ms                                                                 | 484 ms: 1.04x slower                                                |
| xml_etree_generate         | 78.4 ms                                                                | 81.2 ms: 1.04x slower                                               |
| sqlglot_optimize           | 53.4 ms                                                                | 55.5 ms: 1.04x slower                                               |
| typing_runtime_protocols   | 161 us                                                                 | 167 us: 1.04x slower                                                |
| async_tree_memoization_tg  | 320 ms                                                                 | 334 ms: 1.04x slower                                                |
| fannkuch                   | 395 ms                                                                 | 413 ms: 1.05x slower                                                |
| pickle_pure_python         | 315 us                                                                 | 330 us: 1.05x slower                                                |
| pylint                     | 280 ms                                                                 | 294 ms: 1.05x slower                                                |
| gc_traversal               | 4.80 ms                                                                | 5.05 ms: 1.05x slower                                               |
| django_template            | 31.8 ms                                                                | 33.5 ms: 1.05x slower                                               |
| xml_etree_iterparse        | 95.4 ms                                                                | 101 ms: 1.06x slower                                                |
| chaos                      | 58.6 ms                                                                | 61.9 ms: 1.06x slower                                               |
| deltablue                  | 3.34 ms                                                                | 3.54 ms: 1.06x slower                                               |
| xml_etree_process          | 55.1 ms                                                                | 58.6 ms: 1.06x slower                                               |
| deepcopy_reduce            | 2.66 us                                                                | 2.83 us: 1.07x slower                                               |
| float                      | 70.8 ms                                                                | 75.5 ms: 1.07x slower                                               |
| scimark_monte_carlo        | 65.8 ms                                                                | 70.4 ms: 1.07x slower                                               |
| sqlglot_normalize          | 106 ms                                                                 | 114 ms: 1.08x slower                                                |
| scimark_sor                | 117 ms                                                                 | 127 ms: 1.08x slower                                                |
| deepcopy_memo              | 29.9 us                                                                | 32.5 us: 1.09x slower                                               |
| deepcopy                   | 257 us                                                                 | 282 us: 1.10x slower                                                |
| generators                 | 28.1 ms                                                                | 30.9 ms: 1.10x slower                                               |
| unpickle_pure_python       | 201 us                                                                 | 223 us: 1.11x slower                                                |
| genshi_text                | 21.8 ms                                                                | 24.4 ms: 1.12x slower                                               |
| scimark_lu                 | 115 ms                                                                 | 129 ms: 1.13x slower                                                |
| spectral_norm              | 94.4 ms                                                                | 107 ms: 1.13x slower                                                |
| mako                       | 9.88 ms                                                                | 11.2 ms: 1.13x slower                                               |
| genshi_xml                 | 49.5 ms                                                                | 56.4 ms: 1.14x slower                                               |
| logging_silent             | 106 ns                                                                 | 134 ns: 1.26x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.03x slower                                                        |

Benchmark hidden because not significant (8): k_core, json, tomli_loads, asyncio_websockets, mdp, regex_compile, async_tree_io, async_tree_io_tg
Ignored benchmarks (1) of results/bm-20250209-3.14.0a4+-f72977b-JIT/bm-20250209-linux-x86_64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b.json: pycparser

- Geometric mean (including insignificant results): 1.024x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x