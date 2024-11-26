# Results vs. base

- fork: brandtbucher
- ref: warmup_8192
- machine: linux-x86_64
- commit hash: 1236a9d
- commit date: 2024-11-12
- overall geometric mean: 1.018x faster
- HPT reliability: 99.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 258 ms: 1.09x faster                                                |
| docutils       | 2.95 sec                                                               | 2.86 sec: 1.03x faster                                              |
| html5lib       | 67.0 ms                                                                | 66.6 ms: 1.01x faster                                               |
| sphinx         | 1.18 sec                                                               | 1.13 sec: 1.04x faster                                              |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines     | 23.2 ms                                                                | 22.7 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (10): async_tree_memoization_tg, async_tree_memoization, async_generators, async_tree_io, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 82.3 ms                                                                | 82.9 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 140 ms                                                                 | 131 ms: 1.07x faster                                                |
| regex_effbot   | 3.77 ms                                                                | 3.59 ms: 1.05x faster                                               |
| regex_dna      | 216 ms                                                                 | 216 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 219 us                                                                 | 195 us: 1.12x faster                                                |
| tomli_loads          | 2.00 sec                                                               | 1.96 sec: 1.02x faster                                              |
| xml_etree_process    | 56.0 ms                                                                | 55.5 ms: 1.01x faster                                               |
| xml_etree_generate   | 79.6 ms                                                                | 78.9 ms: 1.01x faster                                               |
| pickle_pure_python   | 321 us                                                                 | 318 us: 1.01x faster                                                |
| json_loads           | 26.8 us                                                                | 27.0 us: 1.01x slower                                               |
| xml_etree_iterparse  | 101 ms                                                                 | 103 ms: 1.02x slower                                                |
| xml_etree_parse      | 148 ms                                                                 | 158 ms: 1.06x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                               |
| python_startup_no_site | 7.14 ms                                                                | 7.04 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 59.9 ms                                                                | 56.0 ms: 1.07x faster                                               |
| genshi_text     | 25.1 ms                                                                | 24.4 ms: 1.03x faster                                               |
| mako            | 10.3 ms                                                                | 10.1 ms: 1.01x faster                                               |
| django_template | 34.3 ms                                                                | 35.6 ms: 1.04x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_8192-3.14.0a1+-1236a9d |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| sympy_integrate          | 23.6 ms                                                                | 20.7 ms: 1.14x faster                                               |
| sqlalchemy_declarative   | 148 ms                                                                 | 131 ms: 1.13x faster                                                |
| pylint                   | 380 ms                                                                 | 336 ms: 1.13x faster                                                |
| richards_super           | 47.1 ms                                                                | 41.8 ms: 1.12x faster                                               |
| unpickle_pure_python     | 219 us                                                                 | 195 us: 1.12x faster                                                |
| sympy_sum                | 176 ms                                                                 | 157 ms: 1.12x faster                                                |
| richards                 | 40.7 ms                                                                | 36.7 ms: 1.11x faster                                               |
| sqlglot_optimize         | 60.3 ms                                                                | 54.8 ms: 1.10x faster                                               |
| 2to3                     | 280 ms                                                                 | 258 ms: 1.09x faster                                                |
| bench_mp_pool            | 84.8 ms                                                                | 78.2 ms: 1.08x faster                                               |
| regex_compile            | 140 ms                                                                 | 131 ms: 1.07x faster                                                |
| genshi_xml               | 59.9 ms                                                                | 56.0 ms: 1.07x faster                                               |
| sympy_str                | 305 ms                                                                 | 289 ms: 1.06x faster                                                |
| regex_effbot             | 3.77 ms                                                                | 3.59 ms: 1.05x faster                                               |
| sphinx                   | 1.18 sec                                                               | 1.13 sec: 1.04x faster                                              |
| sqlglot_normalize        | 114 ms                                                                 | 110 ms: 1.04x faster                                                |
| deltablue                | 3.31 ms                                                                | 3.20 ms: 1.04x faster                                               |
| sqlglot_transpile        | 1.69 ms                                                                | 1.63 ms: 1.04x faster                                               |
| sqlalchemy_imperative    | 17.8 ms                                                                | 17.2 ms: 1.03x faster                                               |
| docutils                 | 2.95 sec                                                               | 2.86 sec: 1.03x faster                                              |
| mdp                      | 2.62 sec                                                               | 2.55 sec: 1.03x faster                                              |
| raytrace                 | 283 ms                                                                 | 275 ms: 1.03x faster                                                |
| genshi_text              | 25.1 ms                                                                | 24.4 ms: 1.03x faster                                               |
| coroutines               | 23.2 ms                                                                | 22.7 ms: 1.03x faster                                               |
| bench_thread_pool        | 889 us                                                                 | 867 us: 1.03x faster                                                |
| tomli_loads              | 2.00 sec                                                               | 1.96 sec: 1.02x faster                                              |
| logging_format           | 6.17 us                                                                | 6.05 us: 1.02x faster                                               |
| logging_silent           | 102 ns                                                                 | 100.0 ns: 1.02x faster                                              |
| go                       | 133 ms                                                                 | 131 ms: 1.02x faster                                                |
| sympy_expand             | 509 ms                                                                 | 500 ms: 1.02x faster                                                |
| typing_runtime_protocols | 170 us                                                                 | 167 us: 1.02x faster                                                |
| python_startup           | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                               |
| python_startup_no_site   | 7.14 ms                                                                | 7.04 ms: 1.01x faster                                               |
| telco                    | 7.67 ms                                                                | 7.57 ms: 1.01x faster                                               |
| mako                     | 10.3 ms                                                                | 10.1 ms: 1.01x faster                                               |
| scimark_monte_carlo      | 64.8 ms                                                                | 64.0 ms: 1.01x faster                                               |
| dulwich_log              | 67.7 ms                                                                | 67.0 ms: 1.01x faster                                               |
| sqlite_synth             | 2.80 us                                                                | 2.77 us: 1.01x faster                                               |
| generators               | 36.6 ms                                                                | 36.3 ms: 1.01x faster                                               |
| hexiom                   | 7.08 ms                                                                | 7.02 ms: 1.01x faster                                               |
| xml_etree_process        | 56.0 ms                                                                | 55.5 ms: 1.01x faster                                               |
| xml_etree_generate       | 79.6 ms                                                                | 78.9 ms: 1.01x faster                                               |
| create_gc_cycles         | 2.71 ms                                                                | 2.69 ms: 1.01x faster                                               |
| pickle_pure_python       | 321 us                                                                 | 318 us: 1.01x faster                                                |
| crypto_pyaes             | 68.5 ms                                                                | 68.0 ms: 1.01x faster                                               |
| bpe_tokeniser            | 4.53 sec                                                               | 4.50 sec: 1.01x faster                                              |
| html5lib                 | 67.0 ms                                                                | 66.6 ms: 1.01x faster                                               |
| thrift                   | 779 us                                                                 | 776 us: 1.00x faster                                                |
| connected_components     | 437 ms                                                                 | 436 ms: 1.00x faster                                                |
| comprehensions           | 17.5 us                                                                | 17.5 us: 1.00x faster                                               |
| regex_dna                | 216 ms                                                                 | 216 ms: 1.00x faster                                                |
| nbody                    | 82.3 ms                                                                | 82.9 ms: 1.01x slower                                               |
| scimark_fft              | 318 ms                                                                 | 320 ms: 1.01x slower                                                |
| json_loads               | 26.8 us                                                                | 27.0 us: 1.01x slower                                               |
| deepcopy                 | 267 us                                                                 | 270 us: 1.01x slower                                                |
| deepcopy_memo            | 29.6 us                                                                | 30.0 us: 1.01x slower                                               |
| gc_traversal             | 4.74 ms                                                                | 4.80 ms: 1.01x slower                                               |
| pprint_safe_repr         | 724 ms                                                                 | 734 ms: 1.01x slower                                                |
| pyflate                  | 449 ms                                                                 | 455 ms: 1.02x slower                                                |
| nqueens                  | 87.9 ms                                                                | 89.3 ms: 1.02x slower                                               |
| scimark_sor              | 119 ms                                                                 | 121 ms: 1.02x slower                                                |
| xml_etree_iterparse      | 101 ms                                                                 | 103 ms: 1.02x slower                                                |
| deepcopy_reduce          | 2.66 us                                                                | 2.73 us: 1.03x slower                                               |
| pycparser                | 1.16 sec                                                               | 1.20 sec: 1.03x slower                                              |
| django_template          | 34.3 ms                                                                | 35.6 ms: 1.04x slower                                               |
| scimark_sparse_mat_mult  | 4.62 ms                                                                | 4.80 ms: 1.04x slower                                               |
| xml_etree_parse          | 148 ms                                                                 | 158 ms: 1.06x slower                                                |
| Geometric mean           | (ref)                                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (27): logging_simple, async_tree_memoization_tg, async_tree_memoization, float, async_generators, json, async_tree_io, pathlib, json_dumps, async_tree_io_tg, shortest_path, meteor_contest, spectral_norm, coverage, async_tree_none, pidigits, async_tree_cpu_io_mixed, k_core, async_tree_cpu_io_mixed_tg, asyncio_websockets, scimark_lu, regex_v8, sqlglot_parse, pprint_pformat, chaos, fannkuch, async_tree_none_tg
Ignored benchmarks (3) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: djangocms, many_optionals, subparsers

- Geometric mean (including insignificant results): 1.018x faster
# HPT report

- Reliability score: 99.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x