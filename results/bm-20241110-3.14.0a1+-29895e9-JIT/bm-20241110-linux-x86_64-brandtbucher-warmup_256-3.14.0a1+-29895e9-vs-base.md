# Results vs. base

- fork: brandtbucher
- ref: warmup_256
- machine: linux-x86_64
- commit hash: 29895e9
- commit date: 2024-11-10
- overall geometric mean: 1.008x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 278 ms: 1.01x faster                                               |
| docutils       | 2.95 sec                                                               | 2.90 sec: 1.02x faster                                             |
| html5lib       | 67.0 ms                                                                | 65.4 ms: 1.02x faster                                              |
| sphinx         | 1.18 sec                                                               | 1.15 sec: 1.02x faster                                             |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                | 22.9 ms: 1.02x faster                                              |
| async_generators           | 456 ms                                                                 | 449 ms: 1.02x faster                                               |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 569 ms: 1.01x slower                                               |
| asyncio_websockets         | 551 ms                                                                 | 555 ms: 1.01x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_none, async_tree_io_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 82.3 ms                                                                | 80.9 ms: 1.02x faster                                              |
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                                | 3.69 ms: 1.02x faster                                              |
| regex_compile  | 140 ms                                                                 | 137 ms: 1.02x faster                                               |
| regex_dna      | 216 ms                                                                 | 215 ms: 1.01x faster                                               |
| regex_v8       | 24.6 ms                                                                | 24.8 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 219 us                                                                 | 196 us: 1.12x faster                                               |
| tomli_loads          | 2.00 sec                                                               | 1.94 sec: 1.03x faster                                             |
| xml_etree_generate   | 79.6 ms                                                                | 78.2 ms: 1.02x faster                                              |
| json_dumps           | 11.1 ms                                                                | 10.9 ms: 1.01x faster                                              |
| xml_etree_process    | 56.0 ms                                                                | 55.5 ms: 1.01x faster                                              |
| pickle_pure_python   | 321 us                                                                 | 328 us: 1.02x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.02x faster                                                       |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                                | 7.06 ms: 1.01x faster                                              |
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                              |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 59.9 ms                                                                | 57.1 ms: 1.05x faster                                              |
| mako            | 10.3 ms                                                                | 10.2 ms: 1.00x faster                                              |
| genshi_text     | 25.1 ms                                                                | 25.3 ms: 1.01x slower                                              |
| django_template | 34.3 ms                                                                | 35.9 ms: 1.05x slower                                              |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241110-linux-x86_64-brandtbucher-warmup_256-3.14.0a1+-29895e9 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python       | 219 us                                                                 | 196 us: 1.12x faster                                               |
| gc_traversal               | 4.74 ms                                                                | 4.38 ms: 1.08x faster                                              |
| bench_mp_pool              | 84.8 ms                                                                | 80.3 ms: 1.06x faster                                              |
| genshi_xml                 | 59.9 ms                                                                | 57.1 ms: 1.05x faster                                              |
| sqlglot_optimize           | 60.3 ms                                                                | 58.1 ms: 1.04x faster                                              |
| sympy_integrate            | 23.6 ms                                                                | 22.8 ms: 1.04x faster                                              |
| sympy_sum                  | 176 ms                                                                 | 170 ms: 1.03x faster                                               |
| tomli_loads                | 2.00 sec                                                               | 1.94 sec: 1.03x faster                                             |
| comprehensions             | 17.5 us                                                                | 17.0 us: 1.03x faster                                              |
| raytrace                   | 283 ms                                                                 | 275 ms: 1.03x faster                                               |
| mdp                        | 2.62 sec                                                               | 2.55 sec: 1.03x faster                                             |
| richards                   | 40.7 ms                                                                | 39.7 ms: 1.03x faster                                              |
| html5lib                   | 67.0 ms                                                                | 65.4 ms: 1.02x faster                                              |
| regex_effbot               | 3.77 ms                                                                | 3.69 ms: 1.02x faster                                              |
| sphinx                     | 1.18 sec                                                               | 1.15 sec: 1.02x faster                                             |
| logging_silent             | 102 ns                                                                 | 99.5 ns: 1.02x faster                                              |
| richards_super             | 47.1 ms                                                                | 46.1 ms: 1.02x faster                                              |
| regex_compile              | 140 ms                                                                 | 137 ms: 1.02x faster                                               |
| meteor_contest             | 109 ms                                                                 | 107 ms: 1.02x faster                                               |
| create_gc_cycles           | 2.71 ms                                                                | 2.66 ms: 1.02x faster                                              |
| xml_etree_generate         | 79.6 ms                                                                | 78.2 ms: 1.02x faster                                              |
| sqlalchemy_imperative      | 17.8 ms                                                                | 17.5 ms: 1.02x faster                                              |
| sympy_str                  | 305 ms                                                                 | 300 ms: 1.02x faster                                               |
| sqlalchemy_declarative     | 148 ms                                                                 | 145 ms: 1.02x faster                                               |
| nbody                      | 82.3 ms                                                                | 80.9 ms: 1.02x faster                                              |
| go                         | 133 ms                                                                 | 131 ms: 1.02x faster                                               |
| sympy_expand               | 509 ms                                                                 | 500 ms: 1.02x faster                                               |
| bpe_tokeniser              | 4.53 sec                                                               | 4.45 sec: 1.02x faster                                             |
| coroutines                 | 23.2 ms                                                                | 22.9 ms: 1.02x faster                                              |
| deltablue                  | 3.31 ms                                                                | 3.26 ms: 1.02x faster                                              |
| fannkuch                   | 389 ms                                                                 | 383 ms: 1.02x faster                                               |
| docutils                   | 2.95 sec                                                               | 2.90 sec: 1.02x faster                                             |
| async_generators           | 456 ms                                                                 | 449 ms: 1.02x faster                                               |
| spectral_norm              | 115 ms                                                                 | 113 ms: 1.01x faster                                               |
| typing_runtime_protocols   | 170 us                                                                 | 168 us: 1.01x faster                                               |
| coverage                   | 84.9 ms                                                                | 84.0 ms: 1.01x faster                                              |
| 2to3                       | 280 ms                                                                 | 278 ms: 1.01x faster                                               |
| python_startup_no_site     | 7.14 ms                                                                | 7.06 ms: 1.01x faster                                              |
| json_dumps                 | 11.1 ms                                                                | 10.9 ms: 1.01x faster                                              |
| python_startup             | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                              |
| xml_etree_process          | 56.0 ms                                                                | 55.5 ms: 1.01x faster                                              |
| regex_dna                  | 216 ms                                                                 | 215 ms: 1.01x faster                                               |
| mako                       | 10.3 ms                                                                | 10.2 ms: 1.00x faster                                              |
| dulwich_log                | 67.7 ms                                                                | 67.4 ms: 1.00x faster                                              |
| bench_thread_pool          | 889 us                                                                 | 886 us: 1.00x faster                                               |
| pidigits                   | 187 ms                                                                 | 187 ms: 1.00x slower                                               |
| scimark_lu                 | 113 ms                                                                 | 114 ms: 1.00x slower                                               |
| pyflate                    | 449 ms                                                                 | 451 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 569 ms: 1.01x slower                                               |
| asyncio_websockets         | 551 ms                                                                 | 555 ms: 1.01x slower                                               |
| thrift                     | 779 us                                                                 | 786 us: 1.01x slower                                               |
| logging_simple             | 5.56 us                                                                | 5.62 us: 1.01x slower                                              |
| regex_v8                   | 24.6 ms                                                                | 24.8 ms: 1.01x slower                                              |
| genshi_text                | 25.1 ms                                                                | 25.3 ms: 1.01x slower                                              |
| scimark_fft                | 318 ms                                                                 | 322 ms: 1.01x slower                                               |
| deepcopy                   | 267 us                                                                 | 272 us: 1.02x slower                                               |
| pprint_pformat             | 1.51 sec                                                               | 1.54 sec: 1.02x slower                                             |
| pathlib                    | 16.1 ms                                                                | 16.4 ms: 1.02x slower                                              |
| scimark_sor                | 119 ms                                                                 | 121 ms: 1.02x slower                                               |
| pprint_safe_repr           | 724 ms                                                                 | 739 ms: 1.02x slower                                               |
| pickle_pure_python         | 321 us                                                                 | 328 us: 1.02x slower                                               |
| shortest_path              | 482 ms                                                                 | 496 ms: 1.03x slower                                               |
| deepcopy_reduce            | 2.66 us                                                                | 2.76 us: 1.04x slower                                              |
| django_template            | 34.3 ms                                                                | 35.9 ms: 1.05x slower                                              |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (30): pylint, pycparser, async_tree_memoization, crypto_pyaes, xml_etree_parse, deepcopy_memo, xml_etree_iterparse, sqlglot_parse, float, logging_format, nqueens, scimark_monte_carlo, hexiom, async_tree_none, sqlglot_normalize, async_tree_io_tg, connected_components, sqlite_synth, async_tree_io, sqlglot_transpile, async_tree_memoization_tg, k_core, generators, json, chaos, async_tree_cpu_io_mixed, scimark_sparse_mat_mult, telco, async_tree_none_tg, json_loads
Ignored benchmarks (3) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: djangocms, many_optionals, subparsers

- Geometric mean (including insignificant results): 1.008x faster
# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x