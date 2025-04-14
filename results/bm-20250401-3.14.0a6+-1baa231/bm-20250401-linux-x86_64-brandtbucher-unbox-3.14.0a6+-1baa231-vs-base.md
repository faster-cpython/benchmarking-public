# Results vs. base

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 1baa231
- commit date: 2025-04-01
- overall geometric mean: 1.021x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 261 ms: 1.03x slower                                          |
| docutils       | 2.61 sec                                                               | 2.64 sec: 1.01x slower                                        |
| sphinx         | 1.01 sec                                                               | 1.03 sec: 1.01x slower                                        |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                | 21.5 ms: 1.08x faster                                         |
| async_tree_cpu_io_mixed    | 490 ms                                                                 | 494 ms: 1.01x slower                                          |
| async_tree_cpu_io_mixed_tg | 477 ms                                                                 | 483 ms: 1.01x slower                                          |
| async_tree_none            | 261 ms                                                                 | 264 ms: 1.01x slower                                          |
| async_generators           | 395 ms                                                                 | 401 ms: 1.01x slower                                          |
| async_tree_memoization_tg  | 317 ms                                                                 | 323 ms: 1.02x slower                                          |
| async_tree_none_tg         | 250 ms                                                                 | 256 ms: 1.02x slower                                          |
| async_tree_memoization     | 314 ms                                                                 | 321 ms: 1.02x slower                                          |
| async_tree_io              | 615 ms                                                                 | 630 ms: 1.02x slower                                          |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x slower                                          |
| nbody          | 96.9 ms                                                                | 98.5 ms: 1.02x slower                                         |
| float          | 69.5 ms                                                                | 74.8 ms: 1.08x slower                                         |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.34 ms                                                                | 3.24 ms: 1.03x faster                                         |
| regex_v8       | 23.3 ms                                                                | 22.9 ms: 1.02x faster                                         |
| regex_dna      | 221 ms                                                                 | 219 ms: 1.01x faster                                          |
| regex_compile  | 126 ms                                                                 | 131 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 1.96 sec                                                               | 1.83 sec: 1.07x faster                                        |
| json_dumps           | 11.9 ms                                                                | 11.6 ms: 1.02x faster                                         |
| xml_etree_parse      | 141 ms                                                                 | 141 ms: 1.00x slower                                          |
| xml_etree_iterparse  | 99.1 ms                                                                | 99.7 ms: 1.01x slower                                         |
| xml_etree_process    | 59.1 ms                                                                | 60.0 ms: 1.02x slower                                         |
| pickle_pure_python   | 315 us                                                                 | 325 us: 1.03x slower                                          |
| unpickle_pure_python | 218 us                                                                 | 225 us: 1.03x slower                                          |
| json_loads           | 29.6 us                                                                | 32.0 us: 1.08x slower                                         |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 8.17 ms                                                                | 8.19 ms: 1.00x slower                                         |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                         |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 21.3 ms                                                                | 21.8 ms: 1.02x slower                                         |
| genshi_xml      | 49.0 ms                                                                | 50.2 ms: 1.03x slower                                         |
| django_template | 31.3 ms                                                                | 32.5 ms: 1.04x slower                                         |
| mako            | 11.4 ms                                                                | 11.9 ms: 1.05x slower                                         |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                | 21.5 ms: 1.08x faster                                         |
| tomli_loads                | 1.96 sec                                                               | 1.83 sec: 1.07x faster                                        |
| bpe_tokeniser              | 4.63 sec                                                               | 4.48 sec: 1.03x faster                                        |
| regex_effbot               | 3.34 ms                                                                | 3.24 ms: 1.03x faster                                         |
| json_dumps                 | 11.9 ms                                                                | 11.6 ms: 1.02x faster                                         |
| regex_v8                   | 23.3 ms                                                                | 22.9 ms: 1.02x faster                                         |
| pathlib                    | 16.8 ms                                                                | 16.5 ms: 1.02x faster                                         |
| hexiom                     | 6.18 ms                                                                | 6.09 ms: 1.01x faster                                         |
| connected_components       | 458 ms                                                                 | 451 ms: 1.01x faster                                          |
| spectral_norm              | 99.5 ms                                                                | 98.2 ms: 1.01x faster                                         |
| regex_dna                  | 221 ms                                                                 | 219 ms: 1.01x faster                                          |
| gc_traversal               | 5.06 ms                                                                | 5.07 ms: 1.00x slower                                         |
| python_startup_no_site     | 8.17 ms                                                                | 8.19 ms: 1.00x slower                                         |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                         |
| xml_etree_parse            | 141 ms                                                                 | 141 ms: 1.00x slower                                          |
| pidigits                   | 187 ms                                                                 | 187 ms: 1.00x slower                                          |
| bench_mp_pool              | 83.2 ms                                                                | 83.6 ms: 1.01x slower                                         |
| xml_etree_iterparse        | 99.1 ms                                                                | 99.7 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed    | 490 ms                                                                 | 494 ms: 1.01x slower                                          |
| meteor_contest             | 107 ms                                                                 | 108 ms: 1.01x slower                                          |
| generators                 | 28.1 ms                                                                | 28.4 ms: 1.01x slower                                         |
| sqlglot_v2_normalize       | 106 ms                                                                 | 108 ms: 1.01x slower                                          |
| docutils                   | 2.61 sec                                                               | 2.64 sec: 1.01x slower                                        |
| sqlglot_v2_optimize        | 53.2 ms                                                                | 53.8 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed_tg | 477 ms                                                                 | 483 ms: 1.01x slower                                          |
| fannkuch                   | 425 ms                                                                 | 430 ms: 1.01x slower                                          |
| logging_format             | 6.20 us                                                                | 6.28 us: 1.01x slower                                         |
| sphinx                     | 1.01 sec                                                               | 1.03 sec: 1.01x slower                                        |
| async_tree_none            | 261 ms                                                                 | 264 ms: 1.01x slower                                          |
| async_generators           | 395 ms                                                                 | 401 ms: 1.01x slower                                          |
| xml_etree_process          | 59.1 ms                                                                | 60.0 ms: 1.02x slower                                         |
| nbody                      | 96.9 ms                                                                | 98.5 ms: 1.02x slower                                         |
| sqlalchemy_declarative     | 130 ms                                                                 | 132 ms: 1.02x slower                                          |
| sympy_expand               | 459 ms                                                                 | 467 ms: 1.02x slower                                          |
| many_optionals             | 947 us                                                                 | 964 us: 1.02x slower                                          |
| comprehensions             | 17.0 us                                                                | 17.4 us: 1.02x slower                                         |
| logging_simple             | 5.59 us                                                                | 5.70 us: 1.02x slower                                         |
| bench_thread_pool          | 871 us                                                                 | 889 us: 1.02x slower                                          |
| async_tree_memoization_tg  | 317 ms                                                                 | 323 ms: 1.02x slower                                          |
| mdp                        | 1.23 sec                                                               | 1.26 sec: 1.02x slower                                        |
| sympy_str                  | 268 ms                                                                 | 274 ms: 1.02x slower                                          |
| async_tree_none_tg         | 250 ms                                                                 | 256 ms: 1.02x slower                                          |
| genshi_text                | 21.3 ms                                                                | 21.8 ms: 1.02x slower                                         |
| async_tree_memoization     | 314 ms                                                                 | 321 ms: 1.02x slower                                          |
| dulwich_log                | 58.3 ms                                                                | 59.6 ms: 1.02x slower                                         |
| nqueens                    | 81.3 ms                                                                | 83.2 ms: 1.02x slower                                         |
| async_tree_io              | 615 ms                                                                 | 630 ms: 1.02x slower                                          |
| sqlalchemy_imperative      | 16.8 ms                                                                | 17.2 ms: 1.02x slower                                         |
| sympy_integrate            | 19.5 ms                                                                | 19.9 ms: 1.02x slower                                         |
| pycparser                  | 1.17 sec                                                               | 1.20 sec: 1.02x slower                                        |
| genshi_xml                 | 49.0 ms                                                                | 50.2 ms: 1.03x slower                                         |
| deepcopy_reduce            | 2.70 us                                                                | 2.76 us: 1.03x slower                                         |
| typing_runtime_protocols   | 161 us                                                                 | 165 us: 1.03x slower                                          |
| subparsers                 | 20.8 ms                                                                | 21.3 ms: 1.03x slower                                         |
| 2to3                       | 254 ms                                                                 | 261 ms: 1.03x slower                                          |
| sqlite_synth               | 2.78 us                                                                | 2.86 us: 1.03x slower                                         |
| sympy_sum                  | 148 ms                                                                 | 152 ms: 1.03x slower                                          |
| pyflate                    | 456 ms                                                                 | 469 ms: 1.03x slower                                          |
| raytrace                   | 262 ms                                                                 | 270 ms: 1.03x slower                                          |
| sqlglot_v2_transpile       | 1.58 ms                                                                | 1.63 ms: 1.03x slower                                         |
| pickle_pure_python         | 315 us                                                                 | 325 us: 1.03x slower                                          |
| sqlglot_v2_parse           | 1.27 ms                                                                | 1.31 ms: 1.03x slower                                         |
| unpickle_pure_python       | 218 us                                                                 | 225 us: 1.03x slower                                          |
| logging_silent             | 97.8 ns                                                                | 101 ns: 1.04x slower                                          |
| scimark_monte_carlo        | 66.2 ms                                                                | 68.7 ms: 1.04x slower                                         |
| django_template            | 31.3 ms                                                                | 32.5 ms: 1.04x slower                                         |
| regex_compile              | 126 ms                                                                 | 131 ms: 1.04x slower                                          |
| pprint_pformat             | 1.50 sec                                                               | 1.55 sec: 1.04x slower                                        |
| richards_super             | 50.2 ms                                                                | 52.2 ms: 1.04x slower                                         |
| pprint_safe_repr           | 730 ms                                                                 | 759 ms: 1.04x slower                                          |
| scimark_sor                | 119 ms                                                                 | 124 ms: 1.04x slower                                          |
| richards                   | 44.4 ms                                                                | 46.2 ms: 1.04x slower                                         |
| deepcopy                   | 252 us                                                                 | 263 us: 1.04x slower                                          |
| mako                       | 11.4 ms                                                                | 11.9 ms: 1.05x slower                                         |
| deepcopy_memo              | 29.3 us                                                                | 30.7 us: 1.05x slower                                         |
| json                       | 5.25 ms                                                                | 5.52 ms: 1.05x slower                                         |
| go                         | 113 ms                                                                 | 121 ms: 1.07x slower                                          |
| float                      | 69.5 ms                                                                | 74.8 ms: 1.08x slower                                         |
| json_loads                 | 29.6 us                                                                | 32.0 us: 1.08x slower                                         |
| scimark_lu                 | 114 ms                                                                 | 126 ms: 1.10x slower                                          |
| crypto_pyaes               | 74.8 ms                                                                | 83.0 ms: 1.11x slower                                         |
| scimark_fft                | 350 ms                                                                 | 394 ms: 1.13x slower                                          |
| deltablue                  | 3.09 ms                                                                | 3.55 ms: 1.15x slower                                         |
| scimark_sparse_mat_mult    | 4.68 ms                                                                | 5.43 ms: 1.16x slower                                         |
| Geometric mean             | (ref)                                                                  | 1.02x slower                                                  |

Benchmark hidden because not significant (11): chaos, asyncio_websockets, coverage, shortest_path, create_gc_cycles, k_core, xml_etree_generate, telco, html5lib, pylint, async_tree_io_tg

- Geometric mean (including insignificant results): 1.021x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x