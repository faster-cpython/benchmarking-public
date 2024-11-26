# Results vs. base

- fork: brandtbucher
- ref: jump_backoff
- machine: linux-x86_64
- commit hash: 2e7a174
- commit date: 2024-11-13
- overall geometric mean: 1.010x faster
- HPT reliability: 90.28%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241113-pythonperf2-x86_64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 322 ms                                                                       | 297 ms: 1.09x faster                                                       |
| docutils       | 3.20 sec                                                                     | 3.14 sec: 1.02x faster                                                     |
| html5lib       | 74.2 ms                                                                      | 72.0 ms: 1.03x faster                                                      |
| sphinx         | 1.27 sec                                                                     | 1.24 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                                        | 1.04x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241113-pythonperf2-x86_64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 393 ms                                                                       | 385 ms: 1.02x faster                                                       |
| async_tree_memoization_tg  | 380 ms                                                                       | 376 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed_tg | 566 ms                                                                       | 563 ms: 1.01x faster                                                       |
| async_generators           | 473 ms                                                                       | 482 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                               |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_memoization, coroutines, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241113-pythonperf2-x86_64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 79.7 ms                                                                      | 80.1 ms: 1.01x slower                                                      |
| nbody          | 82.9 ms                                                                      | 87.7 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241113-pythonperf2-x86_64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 151 ms                                                                       | 142 ms: 1.07x faster                                                       |
| regex_v8       | 25.7 ms                                                                      | 25.6 ms: 1.00x faster                                                      |
| regex_dna      | 240 ms                                                                       | 249 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241113-pythonperf2-x86_64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                                       | 197 us: 1.14x faster                                                       |
| json_dumps           | 11.4 ms                                                                      | 11.2 ms: 1.02x faster                                                      |
| pickle_pure_python   | 340 us                                                                       | 334 us: 1.02x faster                                                       |
| tomli_loads          | 2.13 sec                                                                     | 2.14 sec: 1.00x slower                                                     |
| xml_etree_parse      | 149 ms                                                                       | 152 ms: 1.02x slower                                                       |
| xml_etree_process    | 57.9 ms                                                                      | 59.1 ms: 1.02x slower                                                      |
| xml_etree_generate   | 81.2 ms                                                                      | 83.1 ms: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                                        | 1.01x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241113-pythonperf2-x86_64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 9.02 ms                                                                      | 9.03 ms: 1.00x slower                                                      |
| python_startup         | 15.9 ms                                                                      | 15.9 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241113-pythonperf2-x86_64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 66.4 ms                                                                      | 60.7 ms: 1.10x faster                                                      |
| genshi_text     | 29.7 ms                                                                      | 27.6 ms: 1.08x faster                                                      |
| django_template | 44.2 ms                                                                      | 42.7 ms: 1.04x faster                                                      |
| mako            | 9.34 ms                                                                      | 9.49 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                                        | 1.05x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241113-pythonperf2-x86_64-python-c695e37a3f95c225ee08-3.14.0a1+-c695e37 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| sqlalchemy_declarative     | 168 ms                                                                       | 147 ms: 1.14x faster                                                       |
| unpickle_pure_python       | 224 us                                                                       | 197 us: 1.14x faster                                                       |
| sympy_integrate            | 27.4 ms                                                                      | 24.9 ms: 1.10x faster                                                      |
| genshi_xml                 | 66.4 ms                                                                      | 60.7 ms: 1.10x faster                                                      |
| 2to3                       | 322 ms                                                                       | 297 ms: 1.09x faster                                                       |
| sqlglot_optimize           | 69.4 ms                                                                      | 64.0 ms: 1.09x faster                                                      |
| richards_super             | 52.8 ms                                                                      | 48.7 ms: 1.08x faster                                                      |
| genshi_text                | 29.7 ms                                                                      | 27.6 ms: 1.08x faster                                                      |
| regex_compile              | 151 ms                                                                       | 142 ms: 1.07x faster                                                       |
| sympy_sum                  | 174 ms                                                                       | 163 ms: 1.07x faster                                                       |
| richards                   | 45.8 ms                                                                      | 43.2 ms: 1.06x faster                                                      |
| coverage                   | 84.4 ms                                                                      | 80.4 ms: 1.05x faster                                                      |
| pycparser                  | 1.30 sec                                                                     | 1.24 sec: 1.05x faster                                                     |
| django_template            | 44.2 ms                                                                      | 42.7 ms: 1.04x faster                                                      |
| sqlglot_transpile          | 1.98 ms                                                                      | 1.92 ms: 1.03x faster                                                      |
| html5lib                   | 74.2 ms                                                                      | 72.0 ms: 1.03x faster                                                      |
| pyflate                    | 477 ms                                                                       | 463 ms: 1.03x faster                                                       |
| sphinx                     | 1.27 sec                                                                     | 1.24 sec: 1.03x faster                                                     |
| logging_simple             | 6.72 us                                                                      | 6.53 us: 1.03x faster                                                      |
| sqlglot_normalize          | 133 ms                                                                       | 130 ms: 1.03x faster                                                       |
| deltablue                  | 3.35 ms                                                                      | 3.28 ms: 1.02x faster                                                      |
| asyncio_websockets         | 393 ms                                                                       | 385 ms: 1.02x faster                                                       |
| docutils                   | 3.20 sec                                                                     | 3.14 sec: 1.02x faster                                                     |
| json_dumps                 | 11.4 ms                                                                      | 11.2 ms: 1.02x faster                                                      |
| pickle_pure_python         | 340 us                                                                       | 334 us: 1.02x faster                                                       |
| typing_runtime_protocols   | 183 us                                                                       | 180 us: 1.02x faster                                                       |
| go                         | 155 ms                                                                       | 153 ms: 1.02x faster                                                       |
| chaos                      | 67.7 ms                                                                      | 66.7 ms: 1.01x faster                                                      |
| logging_format             | 7.36 us                                                                      | 7.27 us: 1.01x faster                                                      |
| async_tree_memoization_tg  | 380 ms                                                                       | 376 ms: 1.01x faster                                                       |
| sympy_str                  | 322 ms                                                                       | 319 ms: 1.01x faster                                                       |
| scimark_lu                 | 97.9 ms                                                                      | 97.0 ms: 1.01x faster                                                      |
| scimark_monte_carlo        | 69.5 ms                                                                      | 69.0 ms: 1.01x faster                                                      |
| scimark_sparse_mat_mult    | 4.81 ms                                                                      | 4.78 ms: 1.01x faster                                                      |
| deepcopy_memo              | 30.3 us                                                                      | 30.2 us: 1.01x faster                                                      |
| raytrace                   | 329 ms                                                                       | 327 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed_tg | 566 ms                                                                       | 563 ms: 1.01x faster                                                       |
| scimark_fft                | 309 ms                                                                       | 308 ms: 1.01x faster                                                       |
| mdp                        | 2.59 sec                                                                     | 2.58 sec: 1.00x faster                                                     |
| regex_v8                   | 25.7 ms                                                                      | 25.6 ms: 1.00x faster                                                      |
| python_startup_no_site     | 9.02 ms                                                                      | 9.03 ms: 1.00x slower                                                      |
| python_startup             | 15.9 ms                                                                      | 15.9 ms: 1.00x slower                                                      |
| tomli_loads                | 2.13 sec                                                                     | 2.14 sec: 1.00x slower                                                     |
| crypto_pyaes               | 73.3 ms                                                                      | 73.6 ms: 1.00x slower                                                      |
| float                      | 79.7 ms                                                                      | 80.1 ms: 1.01x slower                                                      |
| meteor_contest             | 131 ms                                                                       | 132 ms: 1.01x slower                                                       |
| nqueens                    | 101 ms                                                                       | 102 ms: 1.01x slower                                                       |
| pprint_pformat             | 1.63 sec                                                                     | 1.65 sec: 1.01x slower                                                     |
| sqlalchemy_imperative      | 18.5 ms                                                                      | 18.7 ms: 1.01x slower                                                      |
| k_core                     | 3.00 sec                                                                     | 3.04 sec: 1.01x slower                                                     |
| deepcopy                   | 314 us                                                                       | 318 us: 1.01x slower                                                       |
| sympy_expand               | 537 ms                                                                       | 545 ms: 1.01x slower                                                       |
| telco                      | 7.50 ms                                                                      | 7.62 ms: 1.02x slower                                                      |
| mako                       | 9.34 ms                                                                      | 9.49 ms: 1.02x slower                                                      |
| generators                 | 39.3 ms                                                                      | 39.9 ms: 1.02x slower                                                      |
| xml_etree_parse            | 149 ms                                                                       | 152 ms: 1.02x slower                                                       |
| shortest_path              | 434 ms                                                                       | 442 ms: 1.02x slower                                                       |
| dulwich_log                | 66.7 ms                                                                      | 68.0 ms: 1.02x slower                                                      |
| async_generators           | 473 ms                                                                       | 482 ms: 1.02x slower                                                       |
| pathlib                    | 16.1 ms                                                                      | 16.5 ms: 1.02x slower                                                      |
| xml_etree_process          | 57.9 ms                                                                      | 59.1 ms: 1.02x slower                                                      |
| hexiom                     | 7.12 ms                                                                      | 7.27 ms: 1.02x slower                                                      |
| xml_etree_generate         | 81.2 ms                                                                      | 83.1 ms: 1.02x slower                                                      |
| spectral_norm              | 96.0 ms                                                                      | 98.5 ms: 1.03x slower                                                      |
| pprint_safe_repr           | 795 ms                                                                       | 817 ms: 1.03x slower                                                       |
| scimark_sor                | 107 ms                                                                       | 111 ms: 1.03x slower                                                       |
| bpe_tokeniser              | 4.79 sec                                                                     | 4.95 sec: 1.03x slower                                                     |
| logging_silent             | 91.6 ns                                                                      | 95.1 ns: 1.04x slower                                                      |
| gc_traversal               | 5.87 ms                                                                      | 6.10 ms: 1.04x slower                                                      |
| regex_dna                  | 240 ms                                                                       | 249 ms: 1.04x slower                                                       |
| fannkuch                   | 376 ms                                                                       | 394 ms: 1.05x slower                                                       |
| nbody                      | 82.9 ms                                                                      | 87.7 ms: 1.06x slower                                                      |
| Geometric mean             | (ref)                                                                        | 1.01x faster                                                               |

Benchmark hidden because not significant (22): pylint, async_tree_none_tg, bench_thread_pool, json, async_tree_memoization, xml_etree_iterparse, coroutines, async_tree_cpu_io_mixed, connected_components, comprehensions, deepcopy_reduce, pidigits, create_gc_cycles, sqlite_synth, thrift, regex_effbot, async_tree_io_tg, sqlglot_parse, json_loads, async_tree_none, async_tree_io, bench_mp_pool

- Geometric mean (including insignificant results): 1.010x faster
# HPT report

- Reliability score: 90.28% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.96x