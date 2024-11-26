# Results vs. base

- fork: brandtbucher
- ref: warmup_1024
- machine: linux-x86_64
- commit hash: aaa9ae0
- commit date: 2024-11-11
- overall geometric mean: 1.010x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                 | 269 ms: 1.04x faster                                                |
| docutils       | 2.95 sec                                                               | 2.88 sec: 1.02x faster                                              |
| html5lib       | 67.0 ms                                                                | 66.8 ms: 1.00x faster                                               |
| sphinx         | 1.18 sec                                                               | 1.15 sec: 1.03x faster                                              |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                | 22.6 ms: 1.03x faster                                               |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 558 ms: 1.01x faster                                                |
| async_generators           | 456 ms                                                                 | 458 ms: 1.01x slower                                                |
| asyncio_websockets         | 551 ms                                                                 | 555 ms: 1.01x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io, async_tree_memoization, async_tree_none, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 186 ms: 1.00x faster                                                |
| nbody          | 82.3 ms                                                                | 83.9 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                                | 3.53 ms: 1.07x faster                                               |
| regex_compile  | 140 ms                                                                 | 136 ms: 1.03x faster                                                |
| regex_v8       | 24.6 ms                                                                | 24.3 ms: 1.01x faster                                               |
| regex_dna      | 216 ms                                                                 | 216 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 219 us                                                                 | 198 us: 1.11x faster                                                |
| tomli_loads          | 2.00 sec                                                               | 1.94 sec: 1.03x faster                                              |
| json_dumps           | 11.1 ms                                                                | 10.9 ms: 1.01x faster                                               |
| xml_etree_iterparse  | 101 ms                                                                 | 99.3 ms: 1.01x faster                                               |
| xml_etree_process    | 56.0 ms                                                                | 55.4 ms: 1.01x faster                                               |
| xml_etree_generate   | 79.6 ms                                                                | 78.9 ms: 1.01x faster                                               |
| Geometric mean       | (ref)                                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (3): xml_etree_parse, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 7.14 ms                                                                | 7.07 ms: 1.01x faster                                               |
| python_startup         | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 59.9 ms                                                                | 56.7 ms: 1.06x faster                                               |
| genshi_text     | 25.1 ms                                                                | 24.1 ms: 1.04x faster                                               |
| mako            | 10.3 ms                                                                | 10.1 ms: 1.02x faster                                               |
| django_template | 34.3 ms                                                                | 36.6 ms: 1.07x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python       | 219 us                                                                 | 198 us: 1.11x faster                                                |
| richards                   | 40.7 ms                                                                | 37.9 ms: 1.07x faster                                               |
| sqlalchemy_declarative     | 148 ms                                                                 | 138 ms: 1.07x faster                                                |
| bench_mp_pool              | 84.8 ms                                                                | 79.3 ms: 1.07x faster                                               |
| regex_effbot               | 3.77 ms                                                                | 3.53 ms: 1.07x faster                                               |
| sqlglot_optimize           | 60.3 ms                                                                | 57.0 ms: 1.06x faster                                               |
| genshi_xml                 | 59.9 ms                                                                | 56.7 ms: 1.06x faster                                               |
| sympy_integrate            | 23.6 ms                                                                | 22.3 ms: 1.05x faster                                               |
| 2to3                       | 280 ms                                                                 | 269 ms: 1.04x faster                                                |
| richards_super             | 47.1 ms                                                                | 45.3 ms: 1.04x faster                                               |
| genshi_text                | 25.1 ms                                                                | 24.1 ms: 1.04x faster                                               |
| gc_traversal               | 4.74 ms                                                                | 4.56 ms: 1.04x faster                                               |
| sympy_sum                  | 176 ms                                                                 | 170 ms: 1.04x faster                                                |
| pprint_pformat             | 1.51 sec                                                               | 1.47 sec: 1.03x faster                                              |
| tomli_loads                | 2.00 sec                                                               | 1.94 sec: 1.03x faster                                              |
| regex_compile              | 140 ms                                                                 | 136 ms: 1.03x faster                                                |
| logging_silent             | 102 ns                                                                 | 98.8 ns: 1.03x faster                                               |
| sphinx                     | 1.18 sec                                                               | 1.15 sec: 1.03x faster                                              |
| comprehensions             | 17.5 us                                                                | 17.1 us: 1.03x faster                                               |
| coroutines                 | 23.2 ms                                                                | 22.6 ms: 1.03x faster                                               |
| generators                 | 36.6 ms                                                                | 35.7 ms: 1.03x faster                                               |
| sqlglot_transpile          | 1.69 ms                                                                | 1.65 ms: 1.03x faster                                               |
| meteor_contest             | 109 ms                                                                 | 107 ms: 1.02x faster                                                |
| sympy_str                  | 305 ms                                                                 | 298 ms: 1.02x faster                                                |
| docutils                   | 2.95 sec                                                               | 2.88 sec: 1.02x faster                                              |
| coverage                   | 84.9 ms                                                                | 83.4 ms: 1.02x faster                                               |
| spectral_norm              | 115 ms                                                                 | 113 ms: 1.02x faster                                                |
| mako                       | 10.3 ms                                                                | 10.1 ms: 1.02x faster                                               |
| go                         | 133 ms                                                                 | 131 ms: 1.02x faster                                                |
| deltablue                  | 3.31 ms                                                                | 3.26 ms: 1.02x faster                                               |
| pyflate                    | 449 ms                                                                 | 441 ms: 1.02x faster                                                |
| typing_runtime_protocols   | 170 us                                                                 | 167 us: 1.02x faster                                                |
| json_dumps                 | 11.1 ms                                                                | 10.9 ms: 1.01x faster                                               |
| regex_v8                   | 24.6 ms                                                                | 24.3 ms: 1.01x faster                                               |
| xml_etree_iterparse        | 101 ms                                                                 | 99.3 ms: 1.01x faster                                               |
| json                       | 4.98 ms                                                                | 4.92 ms: 1.01x faster                                               |
| async_tree_cpu_io_mixed_tg | 565 ms                                                                 | 558 ms: 1.01x faster                                                |
| sympy_expand               | 509 ms                                                                 | 503 ms: 1.01x faster                                                |
| fannkuch                   | 389 ms                                                                 | 385 ms: 1.01x faster                                                |
| xml_etree_process          | 56.0 ms                                                                | 55.4 ms: 1.01x faster                                               |
| raytrace                   | 283 ms                                                                 | 280 ms: 1.01x faster                                                |
| crypto_pyaes               | 68.5 ms                                                                | 67.8 ms: 1.01x faster                                               |
| python_startup_no_site     | 7.14 ms                                                                | 7.07 ms: 1.01x faster                                               |
| xml_etree_generate         | 79.6 ms                                                                | 78.9 ms: 1.01x faster                                               |
| python_startup             | 12.8 ms                                                                | 12.7 ms: 1.01x faster                                               |
| bench_thread_pool          | 889 us                                                                 | 882 us: 1.01x faster                                                |
| sqlite_synth               | 2.80 us                                                                | 2.78 us: 1.01x faster                                               |
| create_gc_cycles           | 2.71 ms                                                                | 2.69 ms: 1.01x faster                                               |
| telco                      | 7.67 ms                                                                | 7.61 ms: 1.01x faster                                               |
| logging_format             | 6.17 us                                                                | 6.13 us: 1.01x faster                                               |
| bpe_tokeniser              | 4.53 sec                                                               | 4.49 sec: 1.01x faster                                              |
| chaos                      | 59.1 ms                                                                | 58.7 ms: 1.01x faster                                               |
| dulwich_log                | 67.7 ms                                                                | 67.3 ms: 1.01x faster                                               |
| html5lib                   | 67.0 ms                                                                | 66.8 ms: 1.00x faster                                               |
| regex_dna                  | 216 ms                                                                 | 216 ms: 1.00x faster                                                |
| pidigits                   | 187 ms                                                                 | 186 ms: 1.00x faster                                                |
| async_generators           | 456 ms                                                                 | 458 ms: 1.01x slower                                                |
| asyncio_websockets         | 551 ms                                                                 | 555 ms: 1.01x slower                                                |
| deepcopy_memo              | 29.6 us                                                                | 29.8 us: 1.01x slower                                               |
| thrift                     | 779 us                                                                 | 786 us: 1.01x slower                                                |
| pathlib                    | 16.1 ms                                                                | 16.3 ms: 1.02x slower                                               |
| logging_simple             | 5.56 us                                                                | 5.65 us: 1.02x slower                                               |
| deepcopy                   | 267 us                                                                 | 272 us: 1.02x slower                                                |
| scimark_sor                | 119 ms                                                                 | 121 ms: 1.02x slower                                                |
| nbody                      | 82.3 ms                                                                | 83.9 ms: 1.02x slower                                               |
| pycparser                  | 1.16 sec                                                               | 1.19 sec: 1.02x slower                                              |
| scimark_monte_carlo        | 64.8 ms                                                                | 66.2 ms: 1.02x slower                                               |
| hexiom                     | 7.08 ms                                                                | 7.27 ms: 1.03x slower                                               |
| scimark_sparse_mat_mult    | 4.62 ms                                                                | 4.74 ms: 1.03x slower                                               |
| scimark_lu                 | 113 ms                                                                 | 117 ms: 1.03x slower                                                |
| deepcopy_reduce            | 2.66 us                                                                | 2.75 us: 1.03x slower                                               |
| mdp                        | 2.62 sec                                                               | 2.73 sec: 1.04x slower                                              |
| django_template            | 34.3 ms                                                                | 36.6 ms: 1.07x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (21): pylint, pprint_safe_repr, async_tree_cpu_io_mixed, xml_etree_parse, float, nqueens, sqlalchemy_imperative, sqlglot_normalize, scimark_fft, shortest_path, sqlglot_parse, connected_components, async_tree_memoization_tg, pickle_pure_python, async_tree_io, json_loads, async_tree_memoization, async_tree_none, async_tree_io_tg, k_core, async_tree_none_tg
Ignored benchmarks (3) of results/bm-20241107-3.14.0a1+-09d6f5d-JIT/bm-20241107-linux-x86_64-python-09d6f5dc7824c74672ad-3.14.0a1+-09d6f5d.json: djangocms, many_optionals, subparsers

- Geometric mean (including insignificant results): 1.010x faster
# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x