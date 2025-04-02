# Results vs. base

- fork: brandtbucher
- ref: unbox_unsigned
- machine: linux-x86_64
- commit hash: f31fd63
- commit date: 2025-04-01
- overall geometric mean: 1.028x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 264 ms: 1.04x slower                                                   |
| docutils       | 2.61 sec                                                               | 2.65 sec: 1.01x slower                                                 |
| html5lib       | 62.7 ms                                                                | 63.8 ms: 1.02x slower                                                  |
| sphinx         | 1.01 sec                                                               | 1.03 sec: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                | 21.6 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed    | 490 ms                                                                 | 494 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed_tg | 477 ms                                                                 | 484 ms: 1.01x slower                                                   |
| async_generators           | 395 ms                                                                 | 400 ms: 1.01x slower                                                   |
| async_tree_none            | 261 ms                                                                 | 266 ms: 1.02x slower                                                   |
| async_tree_io              | 615 ms                                                                 | 631 ms: 1.02x slower                                                   |
| async_tree_none_tg         | 250 ms                                                                 | 257 ms: 1.03x slower                                                   |
| async_tree_memoization     | 314 ms                                                                 | 322 ms: 1.03x slower                                                   |
| async_tree_memoization_tg  | 317 ms                                                                 | 326 ms: 1.03x slower                                                   |
| async_tree_io_tg           | 614 ms                                                                 | 634 ms: 1.03x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x slower                                                   |
| nbody          | 96.9 ms                                                                | 98.1 ms: 1.01x slower                                                  |
| float          | 69.5 ms                                                                | 75.0 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                                 | 217 ms: 1.02x faster                                                   |
| regex_effbot   | 3.34 ms                                                                | 3.30 ms: 1.01x faster                                                  |
| regex_v8       | 23.3 ms                                                                | 23.5 ms: 1.01x slower                                                  |
| regex_compile  | 126 ms                                                                 | 133 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.96 sec                                                               | 1.88 sec: 1.05x faster                                                 |
| json_dumps           | 11.9 ms                                                                | 11.6 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 99.1 ms                                                                | 99.8 ms: 1.01x slower                                                  |
| xml_etree_generate   | 85.3 ms                                                                | 86.1 ms: 1.01x slower                                                  |
| xml_etree_process    | 59.1 ms                                                                | 60.0 ms: 1.02x slower                                                  |
| unpickle_pure_python | 218 us                                                                 | 230 us: 1.06x slower                                                   |
| pickle_pure_python   | 315 us                                                                 | 333 us: 1.06x slower                                                   |
| json_loads           | 29.6 us                                                                | 32.3 us: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 8.17 ms                                                                | 8.23 ms: 1.01x slower                                                  |
| python_startup         | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                                | 49.7 ms: 1.01x slower                                                  |
| genshi_text     | 21.3 ms                                                                | 21.9 ms: 1.03x slower                                                  |
| django_template | 31.3 ms                                                                | 32.7 ms: 1.05x slower                                                  |
| mako            | 11.4 ms                                                                | 12.3 ms: 1.08x slower                                                  |
| Geometric mean  | (ref)                                                                  | 1.04x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                | 21.6 ms: 1.07x faster                                                  |
| tomli_loads                | 1.96 sec                                                               | 1.88 sec: 1.05x faster                                                 |
| gc_traversal               | 5.06 ms                                                                | 4.91 ms: 1.03x faster                                                  |
| bpe_tokeniser              | 4.63 sec                                                               | 4.51 sec: 1.03x faster                                                 |
| json_dumps                 | 11.9 ms                                                                | 11.6 ms: 1.03x faster                                                  |
| spectral_norm              | 99.5 ms                                                                | 97.4 ms: 1.02x faster                                                  |
| regex_dna                  | 221 ms                                                                 | 217 ms: 1.02x faster                                                   |
| pathlib                    | 16.8 ms                                                                | 16.6 ms: 1.01x faster                                                  |
| regex_effbot               | 3.34 ms                                                                | 3.30 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                                 | 187 ms: 1.00x slower                                                   |
| create_gc_cycles           | 2.49 ms                                                                | 2.49 ms: 1.00x slower                                                  |
| python_startup_no_site     | 8.17 ms                                                                | 8.23 ms: 1.01x slower                                                  |
| xml_etree_iterparse        | 99.1 ms                                                                | 99.8 ms: 1.01x slower                                                  |
| python_startup             | 13.1 ms                                                                | 13.2 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed    | 490 ms                                                                 | 494 ms: 1.01x slower                                                   |
| xml_etree_generate         | 85.3 ms                                                                | 86.1 ms: 1.01x slower                                                  |
| sqlite_synth               | 2.78 us                                                                | 2.81 us: 1.01x slower                                                  |
| telco                      | 7.93 ms                                                                | 8.01 ms: 1.01x slower                                                  |
| bench_mp_pool              | 83.2 ms                                                                | 84.1 ms: 1.01x slower                                                  |
| regex_v8                   | 23.3 ms                                                                | 23.5 ms: 1.01x slower                                                  |
| nbody                      | 96.9 ms                                                                | 98.1 ms: 1.01x slower                                                  |
| meteor_contest             | 107 ms                                                                 | 108 ms: 1.01x slower                                                   |
| genshi_xml                 | 49.0 ms                                                                | 49.7 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 477 ms                                                                 | 484 ms: 1.01x slower                                                   |
| docutils                   | 2.61 sec                                                               | 2.65 sec: 1.01x slower                                                 |
| async_generators           | 395 ms                                                                 | 400 ms: 1.01x slower                                                   |
| coverage                   | 84.0 ms                                                                | 85.2 ms: 1.01x slower                                                  |
| xml_etree_process          | 59.1 ms                                                                | 60.0 ms: 1.02x slower                                                  |
| mdp                        | 1.23 sec                                                               | 1.25 sec: 1.02x slower                                                 |
| html5lib                   | 62.7 ms                                                                | 63.8 ms: 1.02x slower                                                  |
| generators                 | 28.1 ms                                                                | 28.6 ms: 1.02x slower                                                  |
| sympy_expand               | 459 ms                                                                 | 467 ms: 1.02x slower                                                   |
| sphinx                     | 1.01 sec                                                               | 1.03 sec: 1.02x slower                                                 |
| pycparser                  | 1.17 sec                                                               | 1.19 sec: 1.02x slower                                                 |
| bench_thread_pool          | 871 us                                                                 | 889 us: 1.02x slower                                                   |
| async_tree_none            | 261 ms                                                                 | 266 ms: 1.02x slower                                                   |
| sqlalchemy_imperative      | 16.8 ms                                                                | 17.2 ms: 1.02x slower                                                  |
| sqlalchemy_declarative     | 130 ms                                                                 | 133 ms: 1.02x slower                                                   |
| sympy_integrate            | 19.5 ms                                                                | 19.9 ms: 1.02x slower                                                  |
| nqueens                    | 81.3 ms                                                                | 83.2 ms: 1.02x slower                                                  |
| fannkuch                   | 425 ms                                                                 | 435 ms: 1.02x slower                                                   |
| async_tree_io              | 615 ms                                                                 | 631 ms: 1.02x slower                                                   |
| genshi_text                | 21.3 ms                                                                | 21.9 ms: 1.03x slower                                                  |
| many_optionals             | 947 us                                                                 | 972 us: 1.03x slower                                                   |
| sympy_str                  | 268 ms                                                                 | 275 ms: 1.03x slower                                                   |
| comprehensions             | 17.0 us                                                                | 17.5 us: 1.03x slower                                                  |
| async_tree_none_tg         | 250 ms                                                                 | 257 ms: 1.03x slower                                                   |
| async_tree_memoization     | 314 ms                                                                 | 322 ms: 1.03x slower                                                   |
| sqlglot_v2_normalize       | 106 ms                                                                 | 109 ms: 1.03x slower                                                   |
| async_tree_memoization_tg  | 317 ms                                                                 | 326 ms: 1.03x slower                                                   |
| deepcopy_reduce            | 2.70 us                                                                | 2.77 us: 1.03x slower                                                  |
| sqlglot_v2_optimize        | 53.2 ms                                                                | 54.8 ms: 1.03x slower                                                  |
| async_tree_io_tg           | 614 ms                                                                 | 634 ms: 1.03x slower                                                   |
| sympy_sum                  | 148 ms                                                                 | 153 ms: 1.03x slower                                                   |
| subparsers                 | 20.8 ms                                                                | 21.5 ms: 1.04x slower                                                  |
| logging_format             | 6.20 us                                                                | 6.42 us: 1.04x slower                                                  |
| hexiom                     | 6.18 ms                                                                | 6.41 ms: 1.04x slower                                                  |
| dulwich_log                | 58.3 ms                                                                | 60.4 ms: 1.04x slower                                                  |
| logging_simple             | 5.59 us                                                                | 5.80 us: 1.04x slower                                                  |
| 2to3                       | 254 ms                                                                 | 264 ms: 1.04x slower                                                   |
| pyflate                    | 456 ms                                                                 | 474 ms: 1.04x slower                                                   |
| chaos                      | 57.6 ms                                                                | 60.0 ms: 1.04x slower                                                  |
| deepcopy                   | 252 us                                                                 | 262 us: 1.04x slower                                                   |
| sqlglot_v2_transpile       | 1.58 ms                                                                | 1.65 ms: 1.04x slower                                                  |
| typing_runtime_protocols   | 161 us                                                                 | 168 us: 1.05x slower                                                   |
| django_template            | 31.3 ms                                                                | 32.7 ms: 1.05x slower                                                  |
| json                       | 5.25 ms                                                                | 5.50 ms: 1.05x slower                                                  |
| sqlglot_v2_parse           | 1.27 ms                                                                | 1.33 ms: 1.05x slower                                                  |
| regex_compile              | 126 ms                                                                 | 133 ms: 1.05x slower                                                   |
| scimark_monte_carlo        | 66.2 ms                                                                | 70.0 ms: 1.06x slower                                                  |
| unpickle_pure_python       | 218 us                                                                 | 230 us: 1.06x slower                                                   |
| raytrace                   | 262 ms                                                                 | 278 ms: 1.06x slower                                                   |
| pickle_pure_python         | 315 us                                                                 | 333 us: 1.06x slower                                                   |
| pprint_pformat             | 1.50 sec                                                               | 1.59 sec: 1.06x slower                                                 |
| richards                   | 44.4 ms                                                                | 47.1 ms: 1.06x slower                                                  |
| richards_super             | 50.2 ms                                                                | 53.3 ms: 1.06x slower                                                  |
| deepcopy_memo              | 29.3 us                                                                | 31.2 us: 1.06x slower                                                  |
| pprint_safe_repr           | 730 ms                                                                 | 777 ms: 1.07x slower                                                   |
| scimark_sparse_mat_mult    | 4.68 ms                                                                | 5.02 ms: 1.07x slower                                                  |
| mako                       | 11.4 ms                                                                | 12.3 ms: 1.08x slower                                                  |
| float                      | 69.5 ms                                                                | 75.0 ms: 1.08x slower                                                  |
| scimark_sor                | 119 ms                                                                 | 128 ms: 1.08x slower                                                   |
| logging_silent             | 97.8 ns                                                                | 106 ns: 1.08x slower                                                   |
| json_loads                 | 29.6 us                                                                | 32.3 us: 1.09x slower                                                  |
| crypto_pyaes               | 74.8 ms                                                                | 81.7 ms: 1.09x slower                                                  |
| scimark_fft                | 350 ms                                                                 | 383 ms: 1.09x slower                                                   |
| scimark_lu                 | 114 ms                                                                 | 125 ms: 1.09x slower                                                   |
| go                         | 113 ms                                                                 | 126 ms: 1.11x slower                                                   |
| deltablue                  | 3.09 ms                                                                | 3.74 ms: 1.21x slower                                                  |
| Geometric mean             | (ref)                                                                  | 1.03x slower                                                           |

Benchmark hidden because not significant (6): connected_components, asyncio_websockets, shortest_path, xml_etree_parse, k_core, pylint

- Geometric mean (including insignificant results): 1.028x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x