# Results vs. base

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 696d3fd
- commit date: 2025-03-30
- overall geometric mean: 1.032x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 262 ms: 1.03x slower                                          |
| docutils       | 2.61 sec                                                               | 2.65 sec: 1.02x slower                                        |
| html5lib       | 62.7 ms                                                                | 64.2 ms: 1.02x slower                                         |
| sphinx         | 1.01 sec                                                               | 1.03 sec: 1.02x slower                                        |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                | 22.2 ms: 1.05x faster                                         |
| async_tree_none_tg         | 250 ms                                                                 | 242 ms: 1.04x faster                                          |
| async_tree_none            | 261 ms                                                                 | 255 ms: 1.02x faster                                          |
| async_tree_io              | 615 ms                                                                 | 603 ms: 1.02x faster                                          |
| async_tree_cpu_io_mixed_tg | 477 ms                                                                 | 473 ms: 1.01x faster                                          |
| async_tree_cpu_io_mixed    | 490 ms                                                                 | 493 ms: 1.01x slower                                          |
| async_tree_memoization     | 314 ms                                                                 | 316 ms: 1.01x slower                                          |
| async_generators           | 395 ms                                                                 | 400 ms: 1.01x slower                                          |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                  |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_memoization_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 189 ms: 1.01x slower                                          |
| nbody          | 96.9 ms                                                                | 111 ms: 1.15x slower                                          |
| float          | 69.5 ms                                                                | 85.4 ms: 1.23x slower                                         |
| Geometric mean | (ref)                                                                  | 1.13x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_dna      | 221 ms                                                                 | 220 ms: 1.01x faster                                          |
| regex_effbot   | 3.34 ms                                                                | 3.32 ms: 1.00x faster                                         |
| regex_compile  | 126 ms                                                                 | 134 ms: 1.06x slower                                          |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 1.96 sec                                                               | 1.89 sec: 1.04x faster                                        |
| json_dumps           | 11.9 ms                                                                | 11.5 ms: 1.03x faster                                         |
| xml_etree_parse      | 141 ms                                                                 | 142 ms: 1.01x slower                                          |
| xml_etree_iterparse  | 99.1 ms                                                                | 100 ms: 1.01x slower                                          |
| xml_etree_generate   | 85.3 ms                                                                | 87.2 ms: 1.02x slower                                         |
| xml_etree_process    | 59.1 ms                                                                | 60.7 ms: 1.03x slower                                         |
| pickle_pure_python   | 315 us                                                                 | 330 us: 1.05x slower                                          |
| unpickle_pure_python | 218 us                                                                 | 228 us: 1.05x slower                                          |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                  |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 8.17 ms                                                                | 8.18 ms: 1.00x slower                                         |
| python_startup         | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                         |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 21.3 ms                                                                | 21.8 ms: 1.02x slower                                         |
| genshi_xml      | 49.0 ms                                                                | 50.3 ms: 1.03x slower                                         |
| mako            | 11.4 ms                                                                | 11.9 ms: 1.04x slower                                         |
| django_template | 31.3 ms                                                                | 32.7 ms: 1.05x slower                                         |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20250328-linux-x86_64-python-00f0771e4dbd8c8b66b3-3.14.0a6+-00f0771 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| coroutines                 | 23.2 ms                                                                | 22.2 ms: 1.05x faster                                         |
| gc_traversal               | 5.06 ms                                                                | 4.86 ms: 1.04x faster                                         |
| tomli_loads                | 1.96 sec                                                               | 1.89 sec: 1.04x faster                                        |
| async_tree_none_tg         | 250 ms                                                                 | 242 ms: 1.04x faster                                          |
| json_dumps                 | 11.9 ms                                                                | 11.5 ms: 1.03x faster                                         |
| async_tree_none            | 261 ms                                                                 | 255 ms: 1.02x faster                                          |
| async_tree_io              | 615 ms                                                                 | 603 ms: 1.02x faster                                          |
| bpe_tokeniser              | 4.63 sec                                                               | 4.54 sec: 1.02x faster                                        |
| async_tree_cpu_io_mixed_tg | 477 ms                                                                 | 473 ms: 1.01x faster                                          |
| hexiom                     | 6.18 ms                                                                | 6.13 ms: 1.01x faster                                         |
| regex_dna                  | 221 ms                                                                 | 220 ms: 1.01x faster                                          |
| regex_effbot               | 3.34 ms                                                                | 3.32 ms: 1.00x faster                                         |
| python_startup_no_site     | 8.17 ms                                                                | 8.18 ms: 1.00x slower                                         |
| python_startup             | 13.1 ms                                                                | 13.1 ms: 1.00x slower                                         |
| bench_mp_pool              | 83.2 ms                                                                | 83.7 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed    | 490 ms                                                                 | 493 ms: 1.01x slower                                          |
| logging_format             | 6.20 us                                                                | 6.24 us: 1.01x slower                                         |
| async_tree_memoization     | 314 ms                                                                 | 316 ms: 1.01x slower                                          |
| create_gc_cycles           | 2.49 ms                                                                | 2.51 ms: 1.01x slower                                         |
| meteor_contest             | 107 ms                                                                 | 108 ms: 1.01x slower                                          |
| xml_etree_parse            | 141 ms                                                                 | 142 ms: 1.01x slower                                          |
| async_generators           | 395 ms                                                                 | 400 ms: 1.01x slower                                          |
| xml_etree_iterparse        | 99.1 ms                                                                | 100 ms: 1.01x slower                                          |
| deepcopy_reduce            | 2.70 us                                                                | 2.73 us: 1.01x slower                                         |
| sqlalchemy_imperative      | 16.8 ms                                                                | 17.0 ms: 1.01x slower                                         |
| logging_simple             | 5.59 us                                                                | 5.66 us: 1.01x slower                                         |
| pidigits                   | 187 ms                                                                 | 189 ms: 1.01x slower                                          |
| fannkuch                   | 425 ms                                                                 | 431 ms: 1.01x slower                                          |
| bench_thread_pool          | 871 us                                                                 | 884 us: 1.01x slower                                          |
| sympy_expand               | 459 ms                                                                 | 466 ms: 1.02x slower                                          |
| docutils                   | 2.61 sec                                                               | 2.65 sec: 1.02x slower                                        |
| sqlite_synth               | 2.78 us                                                                | 2.82 us: 1.02x slower                                         |
| sqlalchemy_declarative     | 130 ms                                                                 | 133 ms: 1.02x slower                                          |
| sphinx                     | 1.01 sec                                                               | 1.03 sec: 1.02x slower                                        |
| pprint_pformat             | 1.50 sec                                                               | 1.53 sec: 1.02x slower                                        |
| many_optionals             | 947 us                                                                 | 966 us: 1.02x slower                                          |
| richards                   | 44.4 ms                                                                | 45.3 ms: 1.02x slower                                         |
| sqlglot_v2_transpile       | 1.58 ms                                                                | 1.62 ms: 1.02x slower                                         |
| sympy_integrate            | 19.5 ms                                                                | 19.9 ms: 1.02x slower                                         |
| sympy_str                  | 268 ms                                                                 | 274 ms: 1.02x slower                                          |
| genshi_text                | 21.3 ms                                                                | 21.8 ms: 1.02x slower                                         |
| xml_etree_generate         | 85.3 ms                                                                | 87.2 ms: 1.02x slower                                         |
| sqlglot_v2_parse           | 1.27 ms                                                                | 1.30 ms: 1.02x slower                                         |
| pprint_safe_repr           | 730 ms                                                                 | 747 ms: 1.02x slower                                          |
| html5lib                   | 62.7 ms                                                                | 64.2 ms: 1.02x slower                                         |
| connected_components       | 458 ms                                                                 | 469 ms: 1.02x slower                                          |
| coverage                   | 84.0 ms                                                                | 86.1 ms: 1.03x slower                                         |
| sqlglot_v2_optimize        | 53.2 ms                                                                | 54.6 ms: 1.03x slower                                         |
| genshi_xml                 | 49.0 ms                                                                | 50.3 ms: 1.03x slower                                         |
| typing_runtime_protocols   | 161 us                                                                 | 165 us: 1.03x slower                                          |
| xml_etree_process          | 59.1 ms                                                                | 60.7 ms: 1.03x slower                                         |
| sqlglot_v2_normalize       | 106 ms                                                                 | 109 ms: 1.03x slower                                          |
| sympy_sum                  | 148 ms                                                                 | 152 ms: 1.03x slower                                          |
| 2to3                       | 254 ms                                                                 | 262 ms: 1.03x slower                                          |
| subparsers                 | 20.8 ms                                                                | 21.4 ms: 1.03x slower                                         |
| logging_silent             | 97.8 ns                                                                | 101 ns: 1.03x slower                                          |
| dulwich_log                | 58.3 ms                                                                | 60.1 ms: 1.03x slower                                         |
| richards_super             | 50.2 ms                                                                | 51.8 ms: 1.03x slower                                         |
| comprehensions             | 17.0 us                                                                | 17.6 us: 1.03x slower                                         |
| deepcopy                   | 252 us                                                                 | 260 us: 1.03x slower                                          |
| pycparser                  | 1.17 sec                                                               | 1.21 sec: 1.04x slower                                        |
| deepcopy_memo              | 29.3 us                                                                | 30.4 us: 1.04x slower                                         |
| mako                       | 11.4 ms                                                                | 11.9 ms: 1.04x slower                                         |
| django_template            | 31.3 ms                                                                | 32.7 ms: 1.05x slower                                         |
| pickle_pure_python         | 315 us                                                                 | 330 us: 1.05x slower                                          |
| unpickle_pure_python       | 218 us                                                                 | 228 us: 1.05x slower                                          |
| mdp                        | 1.23 sec                                                               | 1.29 sec: 1.05x slower                                        |
| chaos                      | 57.6 ms                                                                | 60.6 ms: 1.05x slower                                         |
| nqueens                    | 81.3 ms                                                                | 85.5 ms: 1.05x slower                                         |
| scimark_monte_carlo        | 66.2 ms                                                                | 69.9 ms: 1.06x slower                                         |
| generators                 | 28.1 ms                                                                | 29.7 ms: 1.06x slower                                         |
| regex_compile              | 126 ms                                                                 | 134 ms: 1.06x slower                                          |
| go                         | 113 ms                                                                 | 122 ms: 1.08x slower                                          |
| raytrace                   | 262 ms                                                                 | 283 ms: 1.08x slower                                          |
| crypto_pyaes               | 74.8 ms                                                                | 82.9 ms: 1.11x slower                                         |
| scimark_lu                 | 114 ms                                                                 | 127 ms: 1.11x slower                                          |
| scimark_sor                | 119 ms                                                                 | 134 ms: 1.12x slower                                          |
| nbody                      | 96.9 ms                                                                | 111 ms: 1.15x slower                                          |
| deltablue                  | 3.09 ms                                                                | 3.65 ms: 1.18x slower                                         |
| float                      | 69.5 ms                                                                | 85.4 ms: 1.23x slower                                         |
| spectral_norm              | 99.5 ms                                                                | 127 ms: 1.27x slower                                          |
| scimark_fft                | 350 ms                                                                 | 450 ms: 1.28x slower                                          |
| scimark_sparse_mat_mult    | 4.68 ms                                                                | 6.30 ms: 1.34x slower                                         |
| Geometric mean             | (ref)                                                                  | 1.03x slower                                                  |

Benchmark hidden because not significant (12): async_tree_io_tg, async_tree_memoization_tg, pyflate, regex_v8, k_core, telco, asyncio_websockets, pathlib, json_loads, json, shortest_path, pylint

- Geometric mean (including insignificant results): 1.032x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.99x