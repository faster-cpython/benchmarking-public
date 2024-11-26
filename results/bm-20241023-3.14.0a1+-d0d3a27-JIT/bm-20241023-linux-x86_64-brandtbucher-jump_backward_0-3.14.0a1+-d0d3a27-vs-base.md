# Results vs. base

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: d0d3a27
- commit date: 2024-10-23
- overall geometric mean: 1.048x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 279 ms                                                                 | 288 ms: 1.03x slower                                                    |
| docutils       | 2.91 sec                                                               | 3.41 sec: 1.17x slower                                                  |
| html5lib       | 65.2 ms                                                                | 70.3 ms: 1.08x slower                                                   |
| sphinx         | 1.17 sec                                                               | 1.36 sec: 1.16x slower                                                  |
| tornado_http   | 94.6 ms                                                                | 112 ms: 1.18x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.12x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 977 ms                                                                 | 956 ms: 1.02x faster                                                    |
| asyncio_websockets         | 554 ms                                                                 | 558 ms: 1.01x slower                                                    |
| async_generators           | 460 ms                                                                 | 468 ms: 1.02x slower                                                    |
| async_tree_none_tg         | 322 ms                                                                 | 331 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed    | 577 ms                                                                 | 596 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                 | 584 ms: 1.04x slower                                                    |
| async_tree_none            | 336 ms                                                                 | 350 ms: 1.04x slower                                                    |
| async_tree_memoization     | 416 ms                                                                 | 434 ms: 1.04x slower                                                    |
| async_tree_memoization_tg  | 380 ms                                                                 | 408 ms: 1.07x slower                                                    |
| async_tree_io              | 855 ms                                                                 | 940 ms: 1.10x slower                                                    |
| coroutines                 | 23.1 ms                                                                | 26.6 ms: 1.15x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.05x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 76.1 ms                                                                | 75.5 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 217 ms                                                                 | 223 ms: 1.03x slower                                                    |
| regex_effbot   | 3.77 ms                                                                | 3.94 ms: 1.04x slower                                                   |
| regex_v8       | 24.7 ms                                                                | 26.1 ms: 1.06x slower                                                   |
| regex_compile  | 139 ms                                                                 | 147 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 316 us                                                                 | 296 us: 1.07x faster                                                    |
| xml_etree_parse      | 149 ms                                                                 | 146 ms: 1.02x faster                                                    |
| xml_etree_iterparse  | 100 ms                                                                 | 99.4 ms: 1.01x faster                                                   |
| json_dumps           | 11.0 ms                                                                | 11.0 ms: 1.01x faster                                                   |
| json_loads           | 26.6 us                                                                | 26.7 us: 1.00x slower                                                   |
| tomli_loads          | 1.92 sec                                                               | 1.95 sec: 1.02x slower                                                  |
| unpickle_pure_python | 216 us                                                                 | 226 us: 1.04x slower                                                    |
| xml_etree_generate   | 78.4 ms                                                                | 82.8 ms: 1.06x slower                                                   |
| xml_etree_process    | 55.3 ms                                                                | 59.8 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.8 ms                                                                | 11.9 ms: 1.01x slower                                                   |
| python_startup_no_site | 7.05 ms                                                                | 7.22 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                                  | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|-----------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 26.3 ms                                                                | 26.6 ms: 1.01x slower                                                   |
| genshi_xml      | 61.8 ms                                                                | 62.8 ms: 1.02x slower                                                   |
| mako            | 9.87 ms                                                                | 10.5 ms: 1.06x slower                                                   |
| django_template | 37.1 ms                                                                | 40.5 ms: 1.09x slower                                                   |
| Geometric mean  | (ref)                                                                  | 1.05x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------------------|:----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python         | 316 us                                                                 | 296 us: 1.07x faster                                                    |
| scimark_monte_carlo        | 64.5 ms                                                                | 62.3 ms: 1.04x faster                                                   |
| go                         | 133 ms                                                                 | 129 ms: 1.04x faster                                                    |
| async_tree_io_tg           | 977 ms                                                                 | 956 ms: 1.02x faster                                                    |
| xml_etree_parse            | 149 ms                                                                 | 146 ms: 1.02x faster                                                    |
| nqueens                    | 88.8 ms                                                                | 87.3 ms: 1.02x faster                                                   |
| scimark_fft                | 323 ms                                                                 | 319 ms: 1.01x faster                                                    |
| xml_etree_iterparse        | 100 ms                                                                 | 99.4 ms: 1.01x faster                                                   |
| scimark_lu                 | 115 ms                                                                 | 114 ms: 1.01x faster                                                    |
| float                      | 76.1 ms                                                                | 75.5 ms: 1.01x faster                                                   |
| logging_silent             | 109 ns                                                                 | 108 ns: 1.01x faster                                                    |
| json_dumps                 | 11.0 ms                                                                | 11.0 ms: 1.01x faster                                                   |
| spectral_norm              | 116 ms                                                                 | 115 ms: 1.01x faster                                                    |
| json_loads                 | 26.6 us                                                                | 26.7 us: 1.00x slower                                                   |
| fannkuch                   | 376 ms                                                                 | 378 ms: 1.00x slower                                                    |
| telco                      | 7.59 ms                                                                | 7.64 ms: 1.01x slower                                                   |
| asyncio_websockets         | 554 ms                                                                 | 558 ms: 1.01x slower                                                    |
| bpe_tokeniser              | 4.44 sec                                                               | 4.48 sec: 1.01x slower                                                  |
| create_gc_cycles           | 2.67 ms                                                                | 2.69 ms: 1.01x slower                                                   |
| pathlib                    | 16.2 ms                                                                | 16.4 ms: 1.01x slower                                                   |
| genshi_text                | 26.3 ms                                                                | 26.6 ms: 1.01x slower                                                   |
| scimark_sor                | 119 ms                                                                 | 120 ms: 1.01x slower                                                    |
| scimark_sparse_mat_mult    | 4.60 ms                                                                | 4.66 ms: 1.01x slower                                                   |
| python_startup             | 11.8 ms                                                                | 11.9 ms: 1.01x slower                                                   |
| genshi_xml                 | 61.8 ms                                                                | 62.8 ms: 1.02x slower                                                   |
| async_generators           | 460 ms                                                                 | 468 ms: 1.02x slower                                                    |
| tomli_loads                | 1.92 sec                                                               | 1.95 sec: 1.02x slower                                                  |
| python_startup_no_site     | 7.05 ms                                                                | 7.22 ms: 1.02x slower                                                   |
| deepcopy                   | 269 us                                                                 | 276 us: 1.02x slower                                                    |
| regex_dna                  | 217 ms                                                                 | 223 ms: 1.03x slower                                                    |
| generators                 | 35.5 ms                                                                | 36.5 ms: 1.03x slower                                                   |
| deepcopy_memo              | 29.3 us                                                                | 30.1 us: 1.03x slower                                                   |
| coverage                   | 84.4 ms                                                                | 86.9 ms: 1.03x slower                                                   |
| async_tree_none_tg         | 322 ms                                                                 | 331 ms: 1.03x slower                                                    |
| 2to3                       | 279 ms                                                                 | 288 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed    | 577 ms                                                                 | 596 ms: 1.03x slower                                                    |
| mdp                        | 2.57 sec                                                               | 2.65 sec: 1.03x slower                                                  |
| dulwich_log                | 66.4 ms                                                                | 68.6 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed_tg | 563 ms                                                                 | 584 ms: 1.04x slower                                                    |
| async_tree_none            | 336 ms                                                                 | 350 ms: 1.04x slower                                                    |
| raytrace                   | 283 ms                                                                 | 295 ms: 1.04x slower                                                    |
| async_tree_memoization     | 416 ms                                                                 | 434 ms: 1.04x slower                                                    |
| regex_effbot               | 3.77 ms                                                                | 3.94 ms: 1.04x slower                                                   |
| unpickle_pure_python       | 216 us                                                                 | 226 us: 1.04x slower                                                    |
| thrift                     | 789 us                                                                 | 826 us: 1.05x slower                                                    |
| comprehensions             | 17.0 us                                                                | 17.8 us: 1.05x slower                                                   |
| hexiom                     | 7.13 ms                                                                | 7.48 ms: 1.05x slower                                                   |
| deepcopy_reduce            | 2.77 us                                                                | 2.91 us: 1.05x slower                                                   |
| pyflate                    | 445 ms                                                                 | 467 ms: 1.05x slower                                                    |
| sqlglot_normalize          | 115 ms                                                                 | 121 ms: 1.05x slower                                                    |
| xml_etree_generate         | 78.4 ms                                                                | 82.8 ms: 1.06x slower                                                   |
| regex_v8                   | 24.7 ms                                                                | 26.1 ms: 1.06x slower                                                   |
| regex_compile              | 139 ms                                                                 | 147 ms: 1.06x slower                                                    |
| mako                       | 9.87 ms                                                                | 10.5 ms: 1.06x slower                                                   |
| gc_traversal               | 4.55 ms                                                                | 4.85 ms: 1.06x slower                                                   |
| sympy_expand               | 503 ms                                                                 | 536 ms: 1.07x slower                                                    |
| bench_mp_pool              | 83.7 ms                                                                | 89.9 ms: 1.07x slower                                                   |
| async_tree_memoization_tg  | 380 ms                                                                 | 408 ms: 1.07x slower                                                    |
| sqlglot_parse              | 1.34 ms                                                                | 1.44 ms: 1.08x slower                                                   |
| html5lib                   | 65.2 ms                                                                | 70.3 ms: 1.08x slower                                                   |
| xml_etree_process          | 55.3 ms                                                                | 59.8 ms: 1.08x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                                | 1.85 ms: 1.08x slower                                                   |
| sympy_str                  | 306 ms                                                                 | 333 ms: 1.09x slower                                                    |
| django_template            | 37.1 ms                                                                | 40.5 ms: 1.09x slower                                                   |
| bench_thread_pool          | 877 us                                                                 | 963 us: 1.10x slower                                                    |
| async_tree_io              | 855 ms                                                                 | 940 ms: 1.10x slower                                                    |
| sqlglot_optimize           | 60.1 ms                                                                | 67.2 ms: 1.12x slower                                                   |
| coroutines                 | 23.1 ms                                                                | 26.6 ms: 1.15x slower                                                   |
| pycparser                  | 1.15 sec                                                               | 1.34 sec: 1.16x slower                                                  |
| sphinx                     | 1.17 sec                                                               | 1.36 sec: 1.16x slower                                                  |
| sympy_integrate            | 23.6 ms                                                                | 27.6 ms: 1.17x slower                                                   |
| docutils                   | 2.91 sec                                                               | 3.41 sec: 1.17x slower                                                  |
| sympy_sum                  | 177 ms                                                                 | 208 ms: 1.18x slower                                                    |
| tornado_http               | 94.6 ms                                                                | 112 ms: 1.18x slower                                                    |
| richards                   | 41.8 ms                                                                | 49.9 ms: 1.19x slower                                                   |
| logging_format             | 6.22 us                                                                | 7.43 us: 1.20x slower                                                   |
| richards_super             | 45.5 ms                                                                | 55.2 ms: 1.21x slower                                                   |
| logging_simple             | 5.61 us                                                                | 6.90 us: 1.23x slower                                                   |
| deltablue                  | 3.23 ms                                                                | 4.03 ms: 1.25x slower                                                   |
| pylint                     | 325 ms                                                                 | 468 ms: 1.44x slower                                                    |
| Geometric mean             | (ref)                                                                  | 1.05x slower                                                            |

Benchmark hidden because not significant (9): pprint_pformat, pprint_safe_repr, typing_runtime_protocols, nbody, chaos, json, pidigits, crypto_pyaes, meteor_contest
Ignored benchmarks (2) of results/bm-20241022-3.14.0a1+-34653bb-JIT/bm-20241022-linux-x86_64-python-34653bba644aa5481613-3.14.0a1+-34653bb.json: sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.048x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.04x