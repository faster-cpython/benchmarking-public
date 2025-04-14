# Results vs. base

- fork: brandtbucher
- ref: non_methods
- machine: linux-x86_64
- commit hash: fe5b174
- commit date: 2025-04-07
- overall geometric mean: 1.004x faster
- HPT reliability: 98.55%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250408-linux-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6+-e2b35ee | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| html5lib       | 62.0 ms                                                                | 61.2 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250408-linux-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6+-e2b35ee | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 23.8 ms                                                                | 23.2 ms: 1.02x faster                                               |
| async_generators           | 394 ms                                                                 | 389 ms: 1.01x faster                                                |
| async_tree_memoization     | 310 ms                                                                 | 308 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed    | 476 ms                                                                 | 483 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 477 ms: 1.01x slower                                                |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250408-linux-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6+-e2b35ee | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 66.8 ms                                                                | 65.8 ms: 1.02x faster                                               |
| nbody          | 91.7 ms                                                                | 90.9 ms: 1.01x faster                                               |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250408-linux-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6+-e2b35ee | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.22 ms                                                                | 3.19 ms: 1.01x faster                                               |
| regex_compile  | 124 ms                                                                 | 123 ms: 1.01x faster                                                |
| regex_v8       | 23.1 ms                                                                | 24.1 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250408-linux-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6+-e2b35ee | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 219 us                                                                 | 213 us: 1.03x faster                                                |
| tomli_loads          | 1.92 sec                                                               | 1.89 sec: 1.02x faster                                              |
| xml_etree_parse      | 142 ms                                                                 | 141 ms: 1.01x faster                                                |
| xml_etree_generate   | 83.6 ms                                                                | 83.2 ms: 1.00x faster                                               |
| json_dumps           | 11.4 ms                                                                | 11.7 ms: 1.02x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (4): xml_etree_iterparse, xml_etree_process, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250408-linux-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6+-e2b35ee | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                               |
| python_startup_no_site | 8.18 ms                                                                | 8.21 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250408-linux-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6+-e2b35ee | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 49.3 ms                                                                | 48.6 ms: 1.01x faster                                               |
| django_template | 31.9 ms                                                                | 31.5 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250408-linux-x86_64-python-e2b35ee22950bc5dc541-3.14.0a6+-e2b35ee | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| gc_traversal               | 4.96 ms                                                                | 4.64 ms: 1.07x faster                                               |
| coverage                   | 88.4 ms                                                                | 85.1 ms: 1.04x faster                                               |
| pycparser                  | 1.15 sec                                                               | 1.12 sec: 1.03x faster                                              |
| unpickle_pure_python       | 219 us                                                                 | 213 us: 1.03x faster                                                |
| coroutines                 | 23.8 ms                                                                | 23.2 ms: 1.02x faster                                               |
| comprehensions             | 16.8 us                                                                | 16.4 us: 1.02x faster                                               |
| bpe_tokeniser              | 4.58 sec                                                               | 4.49 sec: 1.02x faster                                              |
| deepcopy_memo              | 28.9 us                                                                | 28.4 us: 1.02x faster                                               |
| sqlglot_v2_parse           | 1.23 ms                                                                | 1.21 ms: 1.02x faster                                               |
| spectral_norm              | 99.3 ms                                                                | 97.7 ms: 1.02x faster                                               |
| tomli_loads                | 1.92 sec                                                               | 1.89 sec: 1.02x faster                                              |
| float                      | 66.8 ms                                                                | 65.8 ms: 1.02x faster                                               |
| telco                      | 7.77 ms                                                                | 7.65 ms: 1.01x faster                                               |
| pyflate                    | 449 ms                                                                 | 443 ms: 1.01x faster                                                |
| async_generators           | 394 ms                                                                 | 389 ms: 1.01x faster                                                |
| typing_runtime_protocols   | 165 us                                                                 | 163 us: 1.01x faster                                                |
| genshi_xml                 | 49.3 ms                                                                | 48.6 ms: 1.01x faster                                               |
| richards_super             | 48.4 ms                                                                | 47.8 ms: 1.01x faster                                               |
| html5lib                   | 62.0 ms                                                                | 61.2 ms: 1.01x faster                                               |
| deltablue                  | 3.31 ms                                                                | 3.27 ms: 1.01x faster                                               |
| scimark_monte_carlo        | 64.9 ms                                                                | 64.1 ms: 1.01x faster                                               |
| django_template            | 31.9 ms                                                                | 31.5 ms: 1.01x faster                                               |
| sqlglot_v2_transpile       | 1.53 ms                                                                | 1.52 ms: 1.01x faster                                               |
| richards                   | 42.6 ms                                                                | 42.2 ms: 1.01x faster                                               |
| regex_effbot               | 3.22 ms                                                                | 3.19 ms: 1.01x faster                                               |
| regex_compile              | 124 ms                                                                 | 123 ms: 1.01x faster                                                |
| nbody                      | 91.7 ms                                                                | 90.9 ms: 1.01x faster                                               |
| sympy_expand               | 457 ms                                                                 | 453 ms: 1.01x faster                                                |
| deepcopy                   | 248 us                                                                 | 246 us: 1.01x faster                                                |
| async_tree_memoization     | 310 ms                                                                 | 308 ms: 1.01x faster                                                |
| xml_etree_parse            | 142 ms                                                                 | 141 ms: 1.01x faster                                                |
| pathlib                    | 16.6 ms                                                                | 16.5 ms: 1.01x faster                                               |
| xml_etree_generate         | 83.6 ms                                                                | 83.2 ms: 1.00x faster                                               |
| bench_thread_pool          | 880 us                                                                 | 877 us: 1.00x faster                                                |
| sqlglot_v2_optimize        | 52.0 ms                                                                | 51.8 ms: 1.00x faster                                               |
| sympy_sum                  | 148 ms                                                                 | 148 ms: 1.00x faster                                                |
| logging_silent             | 93.9 ns                                                                | 93.5 ns: 1.00x faster                                               |
| crypto_pyaes               | 72.5 ms                                                                | 72.3 ms: 1.00x faster                                               |
| many_optionals             | 927 us                                                                 | 924 us: 1.00x faster                                                |
| python_startup             | 13.2 ms                                                                | 13.2 ms: 1.00x slower                                               |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                                |
| python_startup_no_site     | 8.18 ms                                                                | 8.21 ms: 1.00x slower                                               |
| nqueens                    | 79.5 ms                                                                | 79.8 ms: 1.00x slower                                               |
| scimark_fft                | 335 ms                                                                 | 336 ms: 1.01x slower                                                |
| dulwich_log                | 59.0 ms                                                                | 59.4 ms: 1.01x slower                                               |
| chaos                      | 54.7 ms                                                                | 55.3 ms: 1.01x slower                                               |
| deepcopy_reduce            | 2.58 us                                                                | 2.60 us: 1.01x slower                                               |
| async_tree_cpu_io_mixed    | 476 ms                                                                 | 483 ms: 1.01x slower                                                |
| scimark_sparse_mat_mult    | 4.53 ms                                                                | 4.60 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed_tg | 471 ms                                                                 | 477 ms: 1.01x slower                                                |
| hexiom                     | 6.08 ms                                                                | 6.18 ms: 1.02x slower                                               |
| connected_components       | 449 ms                                                                 | 457 ms: 1.02x slower                                                |
| json_dumps                 | 11.4 ms                                                                | 11.7 ms: 1.02x slower                                               |
| generators                 | 29.5 ms                                                                | 30.1 ms: 1.02x slower                                               |
| regex_v8                   | 23.1 ms                                                                | 24.1 ms: 1.04x slower                                               |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (40): async_tree_io_tg, sqlite_synth, async_tree_none, xml_etree_iterparse, pprint_pformat, json, xml_etree_process, json_loads, sqlglot_v2_normalize, meteor_contest, subparsers, async_tree_none_tg, pickle_pure_python, async_tree_memoization_tg, async_tree_io, fannkuch, sphinx, sqlalchemy_declarative, mako, pylint, regex_dna, pprint_safe_repr, bench_mp_pool, sqlalchemy_imperative, create_gc_cycles, asyncio_websockets, go, shortest_path, sympy_str, 2to3, docutils, sympy_integrate, mdp, scimark_sor, raytrace, k_core, genshi_text, logging_simple, scimark_lu, logging_format

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 98.55% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x