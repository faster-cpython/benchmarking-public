# Results vs. base

- fork: brandtbucher
- ref: warmup_2048
- machine: linux-x86_64
- commit hash: f863657
- commit date: 2024-11-12
- overall geometric mean: 1.008x faster
- HPT reliability: 99.58%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 267 ms: 1.05x faster                                                |
| docutils       | 2.95 sec                                                               | 2.91 sec: 1.01x faster                                              |
| html5lib       | 67.0 ms                                                                | 65.6 ms: 1.02x faster                                               |
| sphinx         | 1.18 sec                                                               | 1.15 sec: 1.02x faster                                              |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 978 ms                                                                 | 964 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 559 ms: 1.01x faster                                                |
| async_generators           | 456 ms                                                                 | 452 ms: 1.01x faster                                                |
| asyncio_websockets         | 551 ms                                                                 | 556 ms: 1.01x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, async_tree_none, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.7 ms                                                                | 76.0 ms: 1.01x faster                                               |
| nbody          | 82.3 ms                                                                | 81.9 ms: 1.00x faster                                               |
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 140 ms                                                                 | 135 ms: 1.03x faster                                                |
| regex_effbot   | 3.77 ms                                                                | 3.72 ms: 1.01x faster                                               |
| regex_v8       | 24.6 ms                                                                | 24.7 ms: 1.00x slower                                               |
| regex_dna      | 216 ms                                                                 | 218 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.00 sec                                                               | 1.97 sec: 1.01x faster                                              |
| json_dumps           | 11.1 ms                                                                | 10.9 ms: 1.01x faster                                               |
| xml_etree_generate   | 79.6 ms                                                                | 79.3 ms: 1.00x faster                                               |
| unpickle_pure_python | 219 us                                                                 | 218 us: 1.00x faster                                                |
| json_loads           | 26.8 us                                                                | 27.0 us: 1.01x slower                                               |
| pickle_pure_python   | 321 us                                                                 | 325 us: 1.01x slower                                                |
| xml_etree_iterparse  | 101 ms                                                                 | 103 ms: 1.02x slower                                                |
| xml_etree_parse      | 148 ms                                                                 | 154 ms: 1.04x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                                | 7.05 ms: 1.01x faster                                               |
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 59.9 ms                                                                | 58.4 ms: 1.03x faster                                               |
| genshi_text     | 25.1 ms                                                                | 24.5 ms: 1.02x faster                                               |
| mako            | 10.3 ms                                                                | 10.2 ms: 1.01x faster                                               |
| django_template | 34.3 ms                                                                | 36.4 ms: 1.06x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pylint                     | 380 ms                                                                 | 349 ms: 1.09x faster                                                |
| sqlalchemy_declarative     | 148 ms                                                                 | 136 ms: 1.09x faster                                                |
| sympy_integrate            | 23.6 ms                                                                | 21.9 ms: 1.08x faster                                               |
| bench_mp_pool              | 84.8 ms                                                                | 78.8 ms: 1.08x faster                                               |
| sqlglot_optimize           | 60.3 ms                                                                | 56.4 ms: 1.07x faster                                               |
| 2to3                       | 280 ms                                                                 | 267 ms: 1.05x faster                                                |
| gc_traversal               | 4.74 ms                                                                | 4.52 ms: 1.05x faster                                               |
| sympy_sum                  | 176 ms                                                                 | 168 ms: 1.05x faster                                                |
| logging_silent             | 102 ns                                                                 | 97.9 ns: 1.04x faster                                               |
| regex_compile              | 140 ms                                                                 | 135 ms: 1.03x faster                                                |
| richards_super             | 47.1 ms                                                                | 45.7 ms: 1.03x faster                                               |
| meteor_contest             | 109 ms                                                                 | 106 ms: 1.03x faster                                                |
| genshi_xml                 | 59.9 ms                                                                | 58.4 ms: 1.03x faster                                               |
| sqlglot_transpile          | 1.69 ms                                                                | 1.65 ms: 1.02x faster                                               |
| sphinx                     | 1.18 sec                                                               | 1.15 sec: 1.02x faster                                              |
| generators                 | 36.6 ms                                                                | 35.8 ms: 1.02x faster                                               |
| html5lib                   | 67.0 ms                                                                | 65.6 ms: 1.02x faster                                               |
| raytrace                   | 283 ms                                                                 | 277 ms: 1.02x faster                                                |
| genshi_text                | 25.1 ms                                                                | 24.5 ms: 1.02x faster                                               |
| sqlglot_normalize          | 114 ms                                                                 | 112 ms: 1.02x faster                                                |
| richards                   | 40.7 ms                                                                | 39.9 ms: 1.02x faster                                               |
| sympy_str                  | 305 ms                                                                 | 299 ms: 1.02x faster                                                |
| comprehensions             | 17.5 us                                                                | 17.2 us: 1.02x faster                                               |
| create_gc_cycles           | 2.71 ms                                                                | 2.67 ms: 1.02x faster                                               |
| async_tree_io_tg           | 978 ms                                                                 | 964 ms: 1.02x faster                                                |
| json                       | 4.98 ms                                                                | 4.91 ms: 1.01x faster                                               |
| bpe_tokeniser              | 4.53 sec                                                               | 4.46 sec: 1.01x faster                                              |
| bench_thread_pool          | 889 us                                                                 | 877 us: 1.01x faster                                                |
| regex_effbot               | 3.77 ms                                                                | 3.72 ms: 1.01x faster                                               |
| docutils                   | 2.95 sec                                                               | 2.91 sec: 1.01x faster                                              |
| python_startup_no_site     | 7.14 ms                                                                | 7.05 ms: 1.01x faster                                               |
| python_startup             | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                               |
| tomli_loads                | 2.00 sec                                                               | 1.97 sec: 1.01x faster                                              |
| json_dumps                 | 11.1 ms                                                                | 10.9 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 559 ms: 1.01x faster                                                |
| async_generators           | 456 ms                                                                 | 452 ms: 1.01x faster                                                |
| float                      | 76.7 ms                                                                | 76.0 ms: 1.01x faster                                               |
| sympy_expand               | 509 ms                                                                 | 504 ms: 1.01x faster                                                |
| deepcopy_memo              | 29.6 us                                                                | 29.4 us: 1.01x faster                                               |
| mako                       | 10.3 ms                                                                | 10.2 ms: 1.01x faster                                               |
| deltablue                  | 3.31 ms                                                                | 3.29 ms: 1.01x faster                                               |
| telco                      | 7.67 ms                                                                | 7.63 ms: 1.01x faster                                               |
| dulwich_log                | 67.7 ms                                                                | 67.4 ms: 1.01x faster                                               |
| nbody                      | 82.3 ms                                                                | 81.9 ms: 1.00x faster                                               |
| xml_etree_generate         | 79.6 ms                                                                | 79.3 ms: 1.00x faster                                               |
| unpickle_pure_python       | 219 us                                                                 | 218 us: 1.00x faster                                                |
| pidigits                   | 187 ms                                                                 | 186 ms: 1.00x faster                                                |
| shortest_path              | 482 ms                                                                 | 483 ms: 1.00x slower                                                |
| regex_v8                   | 24.6 ms                                                                | 24.7 ms: 1.00x slower                                               |
| go                         | 133 ms                                                                 | 134 ms: 1.00x slower                                                |
| scimark_fft                | 318 ms                                                                 | 319 ms: 1.01x slower                                                |
| scimark_monte_carlo        | 64.8 ms                                                                | 65.1 ms: 1.01x slower                                               |
| hexiom                     | 7.08 ms                                                                | 7.13 ms: 1.01x slower                                               |
| json_loads                 | 26.8 us                                                                | 27.0 us: 1.01x slower                                               |
| asyncio_websockets         | 551 ms                                                                 | 556 ms: 1.01x slower                                                |
| regex_dna                  | 216 ms                                                                 | 218 ms: 1.01x slower                                                |
| logging_simple             | 5.56 us                                                                | 5.61 us: 1.01x slower                                               |
| deepcopy                   | 267 us                                                                 | 270 us: 1.01x slower                                                |
| pprint_safe_repr           | 724 ms                                                                 | 733 ms: 1.01x slower                                                |
| pickle_pure_python         | 321 us                                                                 | 325 us: 1.01x slower                                                |
| thrift                     | 779 us                                                                 | 790 us: 1.01x slower                                                |
| scimark_sor                | 119 ms                                                                 | 121 ms: 1.02x slower                                                |
| pyflate                    | 449 ms                                                                 | 459 ms: 1.02x slower                                                |
| chaos                      | 59.1 ms                                                                | 60.5 ms: 1.02x slower                                               |
| xml_etree_iterparse        | 101 ms                                                                 | 103 ms: 1.02x slower                                                |
| deepcopy_reduce            | 2.66 us                                                                | 2.72 us: 1.02x slower                                               |
| scimark_lu                 | 113 ms                                                                 | 117 ms: 1.03x slower                                                |
| xml_etree_parse            | 148 ms                                                                 | 154 ms: 1.04x slower                                                |
| mdp                        | 2.62 sec                                                               | 2.73 sec: 1.04x slower                                              |
| django_template            | 34.3 ms                                                                | 36.4 ms: 1.06x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (24): async_tree_memoization, pycparser, async_tree_cpu_io_mixed, sqlalchemy_imperative, fannkuch, logging_format, async_tree_none_tg, spectral_norm, pprint_pformat, crypto_pyaes, nqueens, typing_runtime_protocols, sqlite_synth, async_tree_io, pathlib, scimark_sparse_mat_mult, async_tree_memoization_tg, sqlglot_parse, async_tree_none, connected_components, coverage, coroutines, xml_etree_process, k_core
Ignored benchmarks (3) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: djangocms, many_optionals, subparsers

- Geometric mean (including insignificant results): 1.008x faster
# HPT report

- Reliability score: 99.58% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x