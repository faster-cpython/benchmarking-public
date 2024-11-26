# Results vs. base

- fork: brandtbucher
- ref: warmup_64
- machine: linux-x86_64
- commit hash: 48ade84
- commit date: 2024-11-08
- overall geometric mean: 1.003x faster
- HPT reliability: 92.20%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 277 ms: 1.01x faster                                              |
| docutils       | 2.95 sec                                                               | 2.92 sec: 1.01x faster                                            |
| html5lib       | 67.0 ms                                                                | 65.8 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|--------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| coroutines         | 23.2 ms                                                                | 22.8 ms: 1.02x faster                                             |
| async_generators   | 456 ms                                                                 | 452 ms: 1.01x faster                                              |
| asyncio_websockets | 551 ms                                                                 | 555 ms: 1.01x slower                                              |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                      |

Benchmark hidden because not significant (8): async_tree_io, async_tree_memoization, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                      |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                                | 3.62 ms: 1.04x faster                                             |
| regex_compile  | 140 ms                                                                 | 137 ms: 1.02x faster                                              |
| regex_dna      | 216 ms                                                                 | 214 ms: 1.01x faster                                              |
| regex_v8       | 24.6 ms                                                                | 25.5 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 219 us                                                                 | 196 us: 1.12x faster                                              |
| json_dumps           | 11.1 ms                                                                | 10.8 ms: 1.02x faster                                             |
| tomli_loads          | 2.00 sec                                                               | 1.97 sec: 1.01x faster                                            |
| xml_etree_process    | 56.0 ms                                                                | 55.4 ms: 1.01x faster                                             |
| xml_etree_generate   | 79.6 ms                                                                | 79.1 ms: 1.01x faster                                             |
| json_loads           | 26.8 us                                                                | 26.6 us: 1.01x faster                                             |
| Geometric mean       | (ref)                                                                  | 1.02x faster                                                      |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                             |
| python_startup_no_site | 7.14 ms                                                                | 7.12 ms: 1.00x faster                                             |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 59.9 ms                                                                | 58.8 ms: 1.02x faster                                             |
| mako            | 10.3 ms                                                                | 10.1 ms: 1.02x faster                                             |
| django_template | 34.3 ms                                                                | 36.2 ms: 1.06x slower                                             |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|--------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python     | 219 us                                                                 | 196 us: 1.12x faster                                              |
| regex_effbot             | 3.77 ms                                                                | 3.62 ms: 1.04x faster                                             |
| scimark_sparse_mat_mult  | 4.62 ms                                                                | 4.49 ms: 1.03x faster                                             |
| bench_mp_pool            | 84.8 ms                                                                | 82.5 ms: 1.03x faster                                             |
| mdp                      | 2.62 sec                                                               | 2.56 sec: 1.02x faster                                            |
| typing_runtime_protocols | 170 us                                                                 | 166 us: 1.02x faster                                              |
| coroutines               | 23.2 ms                                                                | 22.8 ms: 1.02x faster                                             |
| regex_compile            | 140 ms                                                                 | 137 ms: 1.02x faster                                              |
| json_dumps               | 11.1 ms                                                                | 10.8 ms: 1.02x faster                                             |
| sqlglot_optimize         | 60.3 ms                                                                | 59.1 ms: 1.02x faster                                             |
| html5lib                 | 67.0 ms                                                                | 65.8 ms: 1.02x faster                                             |
| genshi_xml               | 59.9 ms                                                                | 58.8 ms: 1.02x faster                                             |
| mako                     | 10.3 ms                                                                | 10.1 ms: 1.02x faster                                             |
| logging_silent           | 102 ns                                                                 | 100 ns: 1.02x faster                                              |
| coverage                 | 84.9 ms                                                                | 83.6 ms: 1.02x faster                                             |
| sympy_integrate          | 23.6 ms                                                                | 23.2 ms: 1.02x faster                                             |
| meteor_contest           | 109 ms                                                                 | 108 ms: 1.01x faster                                              |
| comprehensions           | 17.5 us                                                                | 17.3 us: 1.01x faster                                             |
| tomli_loads              | 2.00 sec                                                               | 1.97 sec: 1.01x faster                                            |
| sympy_expand             | 509 ms                                                                 | 502 ms: 1.01x faster                                              |
| generators               | 36.6 ms                                                                | 36.2 ms: 1.01x faster                                             |
| 2to3                     | 280 ms                                                                 | 277 ms: 1.01x faster                                              |
| regex_dna                | 216 ms                                                                 | 214 ms: 1.01x faster                                              |
| sqlglot_normalize        | 114 ms                                                                 | 113 ms: 1.01x faster                                              |
| sympy_sum                | 176 ms                                                                 | 174 ms: 1.01x faster                                              |
| python_startup           | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                             |
| xml_etree_process        | 56.0 ms                                                                | 55.4 ms: 1.01x faster                                             |
| async_generators         | 456 ms                                                                 | 452 ms: 1.01x faster                                              |
| docutils                 | 2.95 sec                                                               | 2.92 sec: 1.01x faster                                            |
| telco                    | 7.67 ms                                                                | 7.61 ms: 1.01x faster                                             |
| xml_etree_generate       | 79.6 ms                                                                | 79.1 ms: 1.01x faster                                             |
| json_loads               | 26.8 us                                                                | 26.6 us: 1.01x faster                                             |
| sympy_str                | 305 ms                                                                 | 303 ms: 1.01x faster                                              |
| pathlib                  | 16.1 ms                                                                | 16.0 ms: 1.01x faster                                             |
| deepcopy_memo            | 29.6 us                                                                | 29.5 us: 1.01x faster                                             |
| sqlalchemy_declarative   | 148 ms                                                                 | 147 ms: 1.00x faster                                              |
| shortest_path            | 482 ms                                                                 | 480 ms: 1.00x faster                                              |
| create_gc_cycles         | 2.71 ms                                                                | 2.70 ms: 1.00x faster                                             |
| python_startup_no_site   | 7.14 ms                                                                | 7.12 ms: 1.00x faster                                             |
| pidigits                 | 187 ms                                                                 | 186 ms: 1.00x faster                                              |
| bench_thread_pool        | 889 us                                                                 | 891 us: 1.00x slower                                              |
| connected_components     | 437 ms                                                                 | 439 ms: 1.00x slower                                              |
| spectral_norm            | 115 ms                                                                 | 115 ms: 1.00x slower                                              |
| scimark_fft              | 318 ms                                                                 | 320 ms: 1.01x slower                                              |
| asyncio_websockets       | 551 ms                                                                 | 555 ms: 1.01x slower                                              |
| thrift                   | 779 us                                                                 | 785 us: 1.01x slower                                              |
| scimark_sor              | 119 ms                                                                 | 120 ms: 1.01x slower                                              |
| raytrace                 | 283 ms                                                                 | 285 ms: 1.01x slower                                              |
| hexiom                   | 7.08 ms                                                                | 7.15 ms: 1.01x slower                                             |
| scimark_lu               | 113 ms                                                                 | 115 ms: 1.01x slower                                              |
| deepcopy                 | 267 us                                                                 | 271 us: 1.01x slower                                              |
| gc_traversal             | 4.74 ms                                                                | 4.81 ms: 1.02x slower                                             |
| pyflate                  | 449 ms                                                                 | 457 ms: 1.02x slower                                              |
| logging_format           | 6.17 us                                                                | 6.31 us: 1.02x slower                                             |
| richards_super           | 47.1 ms                                                                | 48.2 ms: 1.02x slower                                             |
| deepcopy_reduce          | 2.66 us                                                                | 2.73 us: 1.03x slower                                             |
| go                       | 133 ms                                                                 | 137 ms: 1.03x slower                                              |
| logging_simple           | 5.56 us                                                                | 5.74 us: 1.03x slower                                             |
| regex_v8                 | 24.6 ms                                                                | 25.5 ms: 1.04x slower                                             |
| richards                 | 40.7 ms                                                                | 42.4 ms: 1.04x slower                                             |
| django_template          | 34.3 ms                                                                | 36.2 ms: 1.06x slower                                             |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                      |

Benchmark hidden because not significant (33): sqlalchemy_imperative, async_tree_io, sphinx, deltablue, async_tree_memoization, fannkuch, bpe_tokeniser, pycparser, pylint, sqlite_synth, chaos, async_tree_io_tg, async_tree_cpu_io_mixed, pickle_pure_python, nqueens, scimark_monte_carlo, pprint_pformat, async_tree_none, float, dulwich_log, xml_etree_iterparse, nbody, k_core, json, sqlglot_transpile, xml_etree_parse, crypto_pyaes, async_tree_cpu_io_mixed_tg, sqlglot_parse, pprint_safe_repr, async_tree_none_tg, genshi_text, async_tree_memoization_tg
Ignored benchmarks (3) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: djangocms, many_optionals, subparsers

- Geometric mean (including insignificant results): 1.003x faster
# HPT report

- Reliability score: 92.20% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x