# Results vs. base

- fork: brandtbucher
- ref: warmup_4096
- machine: linux-x86_64
- commit hash: a2be6fd
- commit date: 2024-11-11
- overall geometric mean: 1.015x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 262 ms: 1.07x faster                                                |
| docutils       | 2.95 sec                                                               | 2.89 sec: 1.02x faster                                              |
| html5lib       | 67.0 ms                                                                | 66.7 ms: 1.00x faster                                               |
| sphinx         | 1.18 sec                                                               | 1.14 sec: 1.04x faster                                              |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 551 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed    | 581 ms                                                                 | 567 ms: 1.02x faster                                                |
| coroutines                 | 23.2 ms                                                                | 23.0 ms: 1.01x faster                                               |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_io, async_generators, asyncio_websockets, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.7 ms                                                                | 76.3 ms: 1.01x faster                                               |
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                |
| nbody          | 82.3 ms                                                                | 83.4 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 140 ms                                                                 | 134 ms: 1.05x faster                                                |
| regex_effbot   | 3.77 ms                                                                | 3.62 ms: 1.04x faster                                               |
| regex_dna      | 216 ms                                                                 | 211 ms: 1.02x faster                                                |
| regex_v8       | 24.6 ms                                                                | 24.6 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 219 us                                                                 | 193 us: 1.14x faster                                                |
| tomli_loads          | 2.00 sec                                                               | 1.95 sec: 1.02x faster                                              |
| json_dumps           | 11.1 ms                                                                | 10.9 ms: 1.02x faster                                               |
| pickle_pure_python   | 321 us                                                                 | 323 us: 1.01x slower                                                |
| xml_etree_iterparse  | 101 ms                                                                 | 101 ms: 1.01x slower                                                |
| xml_etree_process    | 56.0 ms                                                                | 56.9 ms: 1.02x slower                                               |
| xml_etree_generate   | 79.6 ms                                                                | 81.7 ms: 1.03x slower                                               |
| xml_etree_parse      | 148 ms                                                                 | 157 ms: 1.06x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                                | 7.05 ms: 1.01x faster                                               |
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 59.9 ms                                                                | 58.4 ms: 1.02x faster                                               |
| mako            | 10.3 ms                                                                | 10.3 ms: 1.01x slower                                               |
| django_template | 34.3 ms                                                                | 36.2 ms: 1.06x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_4096-3.14.0a1+-a2be6fd |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python       | 219 us                                                                 | 193 us: 1.14x faster                                                |
| sqlalchemy_declarative     | 148 ms                                                                 | 131 ms: 1.13x faster                                                |
| sympy_integrate            | 23.6 ms                                                                | 21.0 ms: 1.12x faster                                               |
| richards_super             | 47.1 ms                                                                | 42.2 ms: 1.11x faster                                               |
| pylint                     | 380 ms                                                                 | 342 ms: 1.11x faster                                                |
| sympy_sum                  | 176 ms                                                                 | 159 ms: 1.10x faster                                                |
| richards                   | 40.7 ms                                                                | 37.3 ms: 1.09x faster                                               |
| sqlglot_optimize           | 60.3 ms                                                                | 55.4 ms: 1.09x faster                                               |
| gc_traversal               | 4.74 ms                                                                | 4.36 ms: 1.09x faster                                               |
| bench_mp_pool              | 84.8 ms                                                                | 78.4 ms: 1.08x faster                                               |
| 2to3                       | 280 ms                                                                 | 262 ms: 1.07x faster                                                |
| regex_compile              | 140 ms                                                                 | 134 ms: 1.05x faster                                                |
| sympy_str                  | 305 ms                                                                 | 292 ms: 1.04x faster                                                |
| regex_effbot               | 3.77 ms                                                                | 3.62 ms: 1.04x faster                                               |
| sqlglot_normalize          | 114 ms                                                                 | 110 ms: 1.04x faster                                                |
| sqlglot_transpile          | 1.69 ms                                                                | 1.63 ms: 1.04x faster                                               |
| sphinx                     | 1.18 sec                                                               | 1.14 sec: 1.04x faster                                              |
| meteor_contest             | 109 ms                                                                 | 106 ms: 1.03x faster                                                |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 551 ms: 1.02x faster                                                |
| tomli_loads                | 2.00 sec                                                               | 1.95 sec: 1.02x faster                                              |
| genshi_xml                 | 59.9 ms                                                                | 58.4 ms: 1.02x faster                                               |
| async_tree_cpu_io_mixed    | 581 ms                                                                 | 567 ms: 1.02x faster                                                |
| regex_dna                  | 216 ms                                                                 | 211 ms: 1.02x faster                                                |
| raytrace                   | 283 ms                                                                 | 276 ms: 1.02x faster                                                |
| sqlalchemy_imperative      | 17.8 ms                                                                | 17.4 ms: 1.02x faster                                               |
| bench_thread_pool          | 889 us                                                                 | 869 us: 1.02x faster                                                |
| docutils                   | 2.95 sec                                                               | 2.89 sec: 1.02x faster                                              |
| json_dumps                 | 11.1 ms                                                                | 10.9 ms: 1.02x faster                                               |
| generators                 | 36.6 ms                                                                | 36.0 ms: 1.02x faster                                               |
| pprint_pformat             | 1.51 sec                                                               | 1.49 sec: 1.02x faster                                              |
| fannkuch                   | 389 ms                                                                 | 383 ms: 1.02x faster                                                |
| json                       | 4.98 ms                                                                | 4.90 ms: 1.02x faster                                               |
| create_gc_cycles           | 2.71 ms                                                                | 2.67 ms: 1.01x faster                                               |
| sympy_expand               | 509 ms                                                                 | 502 ms: 1.01x faster                                                |
| python_startup_no_site     | 7.14 ms                                                                | 7.05 ms: 1.01x faster                                               |
| python_startup             | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                               |
| coroutines                 | 23.2 ms                                                                | 23.0 ms: 1.01x faster                                               |
| bpe_tokeniser              | 4.53 sec                                                               | 4.48 sec: 1.01x faster                                              |
| shortest_path              | 482 ms                                                                 | 478 ms: 1.01x faster                                                |
| nqueens                    | 87.9 ms                                                                | 87.1 ms: 1.01x faster                                               |
| deltablue                  | 3.31 ms                                                                | 3.29 ms: 1.01x faster                                               |
| typing_runtime_protocols   | 170 us                                                                 | 168 us: 1.01x faster                                                |
| go                         | 133 ms                                                                 | 133 ms: 1.01x faster                                                |
| scimark_monte_carlo        | 64.8 ms                                                                | 64.4 ms: 1.01x faster                                               |
| float                      | 76.7 ms                                                                | 76.3 ms: 1.01x faster                                               |
| html5lib                   | 67.0 ms                                                                | 66.7 ms: 1.00x faster                                               |
| connected_components       | 437 ms                                                                 | 435 ms: 1.00x faster                                                |
| deepcopy_memo              | 29.6 us                                                                | 29.5 us: 1.00x faster                                               |
| pidigits                   | 187 ms                                                                 | 186 ms: 1.00x faster                                                |
| regex_v8                   | 24.6 ms                                                                | 24.6 ms: 1.00x slower                                               |
| pyflate                    | 449 ms                                                                 | 451 ms: 1.01x slower                                                |
| pickle_pure_python         | 321 us                                                                 | 323 us: 1.01x slower                                                |
| mako                       | 10.3 ms                                                                | 10.3 ms: 1.01x slower                                               |
| scimark_fft                | 318 ms                                                                 | 320 ms: 1.01x slower                                                |
| xml_etree_iterparse        | 101 ms                                                                 | 101 ms: 1.01x slower                                                |
| scimark_lu                 | 113 ms                                                                 | 115 ms: 1.01x slower                                                |
| scimark_sor                | 119 ms                                                                 | 120 ms: 1.01x slower                                                |
| nbody                      | 82.3 ms                                                                | 83.4 ms: 1.01x slower                                               |
| pycparser                  | 1.16 sec                                                               | 1.18 sec: 1.02x slower                                              |
| chaos                      | 59.1 ms                                                                | 60.1 ms: 1.02x slower                                               |
| xml_etree_process          | 56.0 ms                                                                | 56.9 ms: 1.02x slower                                               |
| logging_simple             | 5.56 us                                                                | 5.67 us: 1.02x slower                                               |
| spectral_norm              | 115 ms                                                                 | 117 ms: 1.02x slower                                                |
| scimark_sparse_mat_mult    | 4.62 ms                                                                | 4.73 ms: 1.02x slower                                               |
| xml_etree_generate         | 79.6 ms                                                                | 81.7 ms: 1.03x slower                                               |
| deepcopy_reduce            | 2.66 us                                                                | 2.73 us: 1.03x slower                                               |
| pathlib                    | 16.1 ms                                                                | 16.6 ms: 1.04x slower                                               |
| mdp                        | 2.62 sec                                                               | 2.75 sec: 1.05x slower                                              |
| xml_etree_parse            | 148 ms                                                                 | 157 ms: 1.06x slower                                                |
| django_template            | 34.3 ms                                                                | 36.2 ms: 1.06x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (24): async_tree_memoization, async_tree_memoization_tg, genshi_text, logging_silent, async_tree_none, comprehensions, json_loads, logging_format, sqlglot_parse, sqlite_synth, async_tree_io, crypto_pyaes, dulwich_log, async_generators, deepcopy, telco, thrift, asyncio_websockets, async_tree_none_tg, async_tree_io_tg, hexiom, coverage, pprint_safe_repr, k_core
Ignored benchmarks (3) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: djangocms, many_optionals, subparsers

- Geometric mean (including insignificant results): 1.015x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.96x