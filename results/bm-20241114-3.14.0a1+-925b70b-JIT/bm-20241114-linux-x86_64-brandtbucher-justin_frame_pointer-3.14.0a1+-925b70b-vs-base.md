# Results vs. base

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-x86_64
- commit hash: 925b70b
- commit date: 2024-11-14
- overall geometric mean: 1.023x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 286 ms: 1.02x slower                                                         |
| docutils       | 2.95 sec                                                               | 2.97 sec: 1.01x slower                                                       |
| html5lib       | 67.0 ms                                                                | 67.9 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| coroutines       | 23.2 ms                                                                | 22.8 ms: 1.02x faster                                                        |
| async_generators | 456 ms                                                                 | 455 ms: 1.00x faster                                                         |
| async_tree_none  | 332 ms                                                                 | 337 ms: 1.01x slower                                                         |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.7 ms                                                                | 79.1 ms: 1.03x slower                                                        |
| nbody          | 82.3 ms                                                                | 90.0 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                                | 3.72 ms: 1.01x faster                                                        |
| regex_dna      | 216 ms                                                                 | 217 ms: 1.00x slower                                                         |
| regex_v8       | 24.6 ms                                                                | 24.8 ms: 1.01x slower                                                        |
| regex_compile  | 140 ms                                                                 | 144 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_loads           | 26.8 us                                                                | 27.0 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 101 ms                                                                 | 102 ms: 1.02x slower                                                         |
| unpickle_pure_python | 219 us                                                                 | 223 us: 1.02x slower                                                         |
| tomli_loads          | 2.00 sec                                                               | 2.05 sec: 1.02x slower                                                       |
| xml_etree_process    | 56.0 ms                                                                | 57.8 ms: 1.03x slower                                                        |
| pickle_pure_python   | 321 us                                                                 | 332 us: 1.03x slower                                                         |
| xml_etree_generate   | 79.6 ms                                                                | 82.5 ms: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                                | 7.11 ms: 1.00x faster                                                        |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 59.9 ms                                                                | 62.0 ms: 1.04x slower                                                        |
| mako           | 10.3 ms                                                                | 10.8 ms: 1.05x slower                                                        |
| genshi_text    | 25.1 ms                                                                | 27.2 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241114-linux-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-925b70b |
|--------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal             | 4.74 ms                                                                | 4.64 ms: 1.02x faster                                                        |
| coroutines               | 23.2 ms                                                                | 22.8 ms: 1.02x faster                                                        |
| regex_effbot             | 3.77 ms                                                                | 3.72 ms: 1.01x faster                                                        |
| logging_format           | 6.17 us                                                                | 6.11 us: 1.01x faster                                                        |
| create_gc_cycles         | 2.71 ms                                                                | 2.70 ms: 1.01x faster                                                        |
| python_startup_no_site   | 7.14 ms                                                                | 7.11 ms: 1.00x faster                                                        |
| python_startup           | 12.8 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| async_generators         | 456 ms                                                                 | 455 ms: 1.00x faster                                                         |
| regex_dna                | 216 ms                                                                 | 217 ms: 1.00x slower                                                         |
| dulwich_log              | 67.7 ms                                                                | 68.1 ms: 1.01x slower                                                        |
| json_loads               | 26.8 us                                                                | 27.0 us: 1.01x slower                                                        |
| regex_v8                 | 24.6 ms                                                                | 24.8 ms: 1.01x slower                                                        |
| sympy_str                | 305 ms                                                                 | 307 ms: 1.01x slower                                                         |
| thrift                   | 779 us                                                                 | 785 us: 1.01x slower                                                         |
| docutils                 | 2.95 sec                                                               | 2.97 sec: 1.01x slower                                                       |
| sqlalchemy_declarative   | 148 ms                                                                 | 149 ms: 1.01x slower                                                         |
| sympy_sum                | 176 ms                                                                 | 178 ms: 1.01x slower                                                         |
| sqlite_synth             | 2.80 us                                                                | 2.83 us: 1.01x slower                                                        |
| html5lib                 | 67.0 ms                                                                | 67.9 ms: 1.01x slower                                                        |
| sympy_integrate          | 23.6 ms                                                                | 23.9 ms: 1.01x slower                                                        |
| async_tree_none          | 332 ms                                                                 | 337 ms: 1.01x slower                                                         |
| xml_etree_iterparse      | 101 ms                                                                 | 102 ms: 1.02x slower                                                         |
| richards_super           | 47.1 ms                                                                | 47.9 ms: 1.02x slower                                                        |
| unpickle_pure_python     | 219 us                                                                 | 223 us: 1.02x slower                                                         |
| raytrace                 | 283 ms                                                                 | 288 ms: 1.02x slower                                                         |
| pathlib                  | 16.1 ms                                                                | 16.4 ms: 1.02x slower                                                        |
| pprint_pformat           | 1.51 sec                                                               | 1.54 sec: 1.02x slower                                                       |
| 2to3                     | 280 ms                                                                 | 286 ms: 1.02x slower                                                         |
| telco                    | 7.67 ms                                                                | 7.83 ms: 1.02x slower                                                        |
| bench_thread_pool        | 889 us                                                                 | 908 us: 1.02x slower                                                         |
| sqlglot_transpile        | 1.69 ms                                                                | 1.73 ms: 1.02x slower                                                        |
| sqlglot_parse            | 1.33 ms                                                                | 1.36 ms: 1.02x slower                                                        |
| sqlglot_optimize         | 60.3 ms                                                                | 61.7 ms: 1.02x slower                                                        |
| tomli_loads              | 2.00 sec                                                               | 2.05 sec: 1.02x slower                                                       |
| regex_compile            | 140 ms                                                                 | 144 ms: 1.03x slower                                                         |
| shortest_path            | 482 ms                                                                 | 495 ms: 1.03x slower                                                         |
| meteor_contest           | 109 ms                                                                 | 112 ms: 1.03x slower                                                         |
| typing_runtime_protocols | 170 us                                                                 | 175 us: 1.03x slower                                                         |
| sqlglot_normalize        | 114 ms                                                                 | 118 ms: 1.03x slower                                                         |
| float                    | 76.7 ms                                                                | 79.1 ms: 1.03x slower                                                        |
| bpe_tokeniser            | 4.53 sec                                                               | 4.67 sec: 1.03x slower                                                       |
| xml_etree_process        | 56.0 ms                                                                | 57.8 ms: 1.03x slower                                                        |
| pickle_pure_python       | 321 us                                                                 | 332 us: 1.03x slower                                                         |
| connected_components     | 437 ms                                                                 | 453 ms: 1.04x slower                                                         |
| genshi_xml               | 59.9 ms                                                                | 62.0 ms: 1.04x slower                                                        |
| xml_etree_generate       | 79.6 ms                                                                | 82.5 ms: 1.04x slower                                                        |
| scimark_monte_carlo      | 64.8 ms                                                                | 67.2 ms: 1.04x slower                                                        |
| fannkuch                 | 389 ms                                                                 | 405 ms: 1.04x slower                                                         |
| go                       | 133 ms                                                                 | 139 ms: 1.05x slower                                                         |
| chaos                    | 59.1 ms                                                                | 61.9 ms: 1.05x slower                                                        |
| nqueens                  | 87.9 ms                                                                | 92.2 ms: 1.05x slower                                                        |
| mdp                      | 2.62 sec                                                               | 2.75 sec: 1.05x slower                                                       |
| pprint_safe_repr         | 724 ms                                                                 | 760 ms: 1.05x slower                                                         |
| deepcopy_reduce          | 2.66 us                                                                | 2.79 us: 1.05x slower                                                        |
| scimark_lu               | 113 ms                                                                 | 119 ms: 1.05x slower                                                         |
| deepcopy                 | 267 us                                                                 | 281 us: 1.05x slower                                                         |
| mako                     | 10.3 ms                                                                | 10.8 ms: 1.05x slower                                                        |
| crypto_pyaes             | 68.5 ms                                                                | 72.3 ms: 1.06x slower                                                        |
| scimark_sor              | 119 ms                                                                 | 126 ms: 1.06x slower                                                         |
| logging_silent           | 102 ns                                                                 | 108 ns: 1.06x slower                                                         |
| scimark_fft              | 318 ms                                                                 | 337 ms: 1.06x slower                                                         |
| richards                 | 40.7 ms                                                                | 43.2 ms: 1.06x slower                                                        |
| spectral_norm            | 115 ms                                                                 | 122 ms: 1.07x slower                                                         |
| hexiom                   | 7.08 ms                                                                | 7.57 ms: 1.07x slower                                                        |
| pyflate                  | 449 ms                                                                 | 482 ms: 1.07x slower                                                         |
| comprehensions           | 17.5 us                                                                | 18.8 us: 1.07x slower                                                        |
| scimark_sparse_mat_mult  | 4.62 ms                                                                | 4.97 ms: 1.08x slower                                                        |
| deltablue                | 3.31 ms                                                                | 3.57 ms: 1.08x slower                                                        |
| deepcopy_memo            | 29.6 us                                                                | 32.0 us: 1.08x slower                                                        |
| genshi_text              | 25.1 ms                                                                | 27.2 ms: 1.08x slower                                                        |
| nbody                    | 82.3 ms                                                                | 90.0 ms: 1.09x slower                                                        |
| generators               | 36.6 ms                                                                | 41.9 ms: 1.15x slower                                                        |
| Geometric mean           | (ref)                                                                  | 1.03x slower                                                                 |

Benchmark hidden because not significant (23): djangocms, async_tree_cpu_io_mixed, sqlalchemy_imperative, bench_mp_pool, async_tree_cpu_io_mixed_tg, pidigits, coverage, pylint, sympy_expand, asyncio_websockets, async_tree_memoization_tg, xml_etree_parse, k_core, json_dumps, async_tree_io_tg, pycparser, sphinx, logging_simple, json, django_template, async_tree_memoization, async_tree_none_tg, async_tree_io
Ignored benchmarks (2) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: many_optionals, subparsers

- Geometric mean (including insignificant results): 1.023x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x