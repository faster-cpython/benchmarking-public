# Results vs. base

- fork: faster-cpython
- ref: split_load_const
- machine: linux-x86_64
- commit hash: f934559
- commit date: 2024-10-25
- overall geometric mean: 1.004x faster
- HPT reliability: 99.56%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 2.67 sec                                                               | 2.65 sec: 1.01x faster                                                       |
| html5lib       | 63.7 ms                                                                | 63.9 ms: 1.00x slower                                                        |
| tornado_http   | 90.1 ms                                                                | 91.1 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_generators           | 439 ms                                                                 | 428 ms: 1.02x faster                                                         |
| async_tree_io              | 857 ms                                                                 | 838 ms: 1.02x faster                                                         |
| asyncio_websockets         | 556 ms                                                                 | 553 ms: 1.01x faster                                                         |
| async_tree_io_tg           | 979 ms                                                                 | 981 ms: 1.00x slower                                                         |
| async_tree_cpu_io_mixed_tg | 555 ms                                                                 | 559 ms: 1.01x slower                                                         |
| coroutines                 | 23.0 ms                                                                | 23.9 ms: 1.04x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (5): async_tree_none, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 80.4 ms                                                                | 79.4 ms: 1.01x faster                                                        |
| nbody          | 95.5 ms                                                                | 94.4 ms: 1.01x faster                                                        |
| pidigits       | 188 ms                                                                 | 187 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.78 ms                                                                | 3.69 ms: 1.03x faster                                                        |
| regex_v8       | 25.1 ms                                                                | 24.7 ms: 1.02x faster                                                        |
| regex_compile  | 129 ms                                                                 | 129 ms: 1.00x slower                                                         |
| regex_dna      | 216 ms                                                                 | 217 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 11.5 ms                                                                | 11.3 ms: 1.02x faster                                                        |
| unpickle_pure_python | 221 us                                                                 | 217 us: 1.02x faster                                                         |
| xml_etree_parse      | 160 ms                                                                 | 157 ms: 1.02x faster                                                         |
| xml_etree_generate   | 86.4 ms                                                                | 85.4 ms: 1.01x faster                                                        |
| xml_etree_iterparse  | 106 ms                                                                 | 105 ms: 1.01x faster                                                         |
| pickle_pure_python   | 311 us                                                                 | 313 us: 1.00x slower                                                         |
| tomli_loads          | 2.08 sec                                                               | 2.13 sec: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup | 11.8 ms                                                                | 11.8 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 22.8 ms                                                                | 22.2 ms: 1.03x faster                                                        |
| genshi_xml      | 51.3 ms                                                                | 50.4 ms: 1.02x faster                                                        |
| django_template | 34.7 ms                                                                | 34.6 ms: 1.00x faster                                                        |
| mako            | 11.5 ms                                                                | 11.7 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.69 sec                                                               | 2.58 sec: 1.04x faster                                                       |
| typing_runtime_protocols   | 164 us                                                                 | 158 us: 1.04x faster                                                         |
| scimark_sparse_mat_mult    | 5.02 ms                                                                | 4.85 ms: 1.04x faster                                                        |
| scimark_fft                | 378 ms                                                                 | 365 ms: 1.03x faster                                                         |
| deepcopy_reduce            | 2.74 us                                                                | 2.67 us: 1.03x faster                                                        |
| genshi_text                | 22.8 ms                                                                | 22.2 ms: 1.03x faster                                                        |
| regex_effbot               | 3.78 ms                                                                | 3.69 ms: 1.03x faster                                                        |
| async_generators           | 439 ms                                                                 | 428 ms: 1.02x faster                                                         |
| async_tree_io              | 857 ms                                                                 | 838 ms: 1.02x faster                                                         |
| richards                   | 46.8 ms                                                                | 45.8 ms: 1.02x faster                                                        |
| generators                 | 28.6 ms                                                                | 28.0 ms: 1.02x faster                                                        |
| meteor_contest             | 108 ms                                                                 | 106 ms: 1.02x faster                                                         |
| json_dumps                 | 11.5 ms                                                                | 11.3 ms: 1.02x faster                                                        |
| genshi_xml                 | 51.3 ms                                                                | 50.4 ms: 1.02x faster                                                        |
| pyflate                    | 473 ms                                                                 | 465 ms: 1.02x faster                                                         |
| unpickle_pure_python       | 221 us                                                                 | 217 us: 1.02x faster                                                         |
| regex_v8                   | 25.1 ms                                                                | 24.7 ms: 1.02x faster                                                        |
| deepcopy_memo              | 31.1 us                                                                | 30.6 us: 1.02x faster                                                        |
| xml_etree_parse            | 160 ms                                                                 | 157 ms: 1.02x faster                                                         |
| crypto_pyaes               | 73.7 ms                                                                | 72.5 ms: 1.02x faster                                                        |
| bpe_tokeniser              | 4.85 sec                                                               | 4.77 sec: 1.02x faster                                                       |
| coverage                   | 85.9 ms                                                                | 84.7 ms: 1.02x faster                                                        |
| float                      | 80.4 ms                                                                | 79.4 ms: 1.01x faster                                                        |
| nqueens                    | 81.4 ms                                                                | 80.5 ms: 1.01x faster                                                        |
| nbody                      | 95.5 ms                                                                | 94.4 ms: 1.01x faster                                                        |
| hexiom                     | 6.37 ms                                                                | 6.29 ms: 1.01x faster                                                        |
| go                         | 122 ms                                                                 | 121 ms: 1.01x faster                                                         |
| xml_etree_generate         | 86.4 ms                                                                | 85.4 ms: 1.01x faster                                                        |
| scimark_sor                | 129 ms                                                                 | 127 ms: 1.01x faster                                                         |
| telco                      | 8.01 ms                                                                | 7.94 ms: 1.01x faster                                                        |
| xml_etree_iterparse        | 106 ms                                                                 | 105 ms: 1.01x faster                                                         |
| richards_super             | 52.7 ms                                                                | 52.3 ms: 1.01x faster                                                        |
| pprint_safe_repr           | 736 ms                                                                 | 730 ms: 1.01x faster                                                         |
| sqlglot_normalize          | 107 ms                                                                 | 106 ms: 1.01x faster                                                         |
| sqlglot_parse              | 1.30 ms                                                                | 1.29 ms: 1.01x faster                                                        |
| sqlglot_transpile          | 1.60 ms                                                                | 1.59 ms: 1.01x faster                                                        |
| chaos                      | 61.2 ms                                                                | 60.9 ms: 1.01x faster                                                        |
| deepcopy                   | 262 us                                                                 | 261 us: 1.01x faster                                                         |
| deltablue                  | 3.30 ms                                                                | 3.29 ms: 1.01x faster                                                        |
| asyncio_websockets         | 556 ms                                                                 | 553 ms: 1.01x faster                                                         |
| docutils                   | 2.67 sec                                                               | 2.65 sec: 1.01x faster                                                       |
| pidigits                   | 188 ms                                                                 | 187 ms: 1.01x faster                                                         |
| django_template            | 34.7 ms                                                                | 34.6 ms: 1.00x faster                                                        |
| sqlglot_optimize           | 53.4 ms                                                                | 53.2 ms: 1.00x faster                                                        |
| pprint_pformat             | 1.50 sec                                                               | 1.50 sec: 1.00x faster                                                       |
| sqlalchemy_declarative     | 128 ms                                                                 | 127 ms: 1.00x faster                                                         |
| comprehensions             | 16.7 us                                                                | 16.7 us: 1.00x faster                                                        |
| python_startup             | 11.8 ms                                                                | 11.8 ms: 1.00x faster                                                        |
| async_tree_io_tg           | 979 ms                                                                 | 981 ms: 1.00x slower                                                         |
| regex_compile              | 129 ms                                                                 | 129 ms: 1.00x slower                                                         |
| dulwich_log                | 63.5 ms                                                                | 63.6 ms: 1.00x slower                                                        |
| bench_thread_pool          | 839 us                                                                 | 841 us: 1.00x slower                                                         |
| regex_dna                  | 216 ms                                                                 | 217 ms: 1.00x slower                                                         |
| sympy_sum                  | 147 ms                                                                 | 147 ms: 1.00x slower                                                         |
| html5lib                   | 63.7 ms                                                                | 63.9 ms: 1.00x slower                                                        |
| pickle_pure_python         | 311 us                                                                 | 313 us: 1.00x slower                                                         |
| fannkuch                   | 403 ms                                                                 | 405 ms: 1.01x slower                                                         |
| logging_simple             | 5.55 us                                                                | 5.58 us: 1.01x slower                                                        |
| async_tree_cpu_io_mixed_tg | 555 ms                                                                 | 559 ms: 1.01x slower                                                         |
| create_gc_cycles           | 2.66 ms                                                                | 2.68 ms: 1.01x slower                                                        |
| json                       | 4.79 ms                                                                | 4.84 ms: 1.01x slower                                                        |
| logging_format             | 6.17 us                                                                | 6.23 us: 1.01x slower                                                        |
| tornado_http               | 90.1 ms                                                                | 91.1 ms: 1.01x slower                                                        |
| pathlib                    | 15.9 ms                                                                | 16.1 ms: 1.01x slower                                                        |
| mako                       | 11.5 ms                                                                | 11.7 ms: 1.01x slower                                                        |
| spectral_norm              | 116 ms                                                                 | 118 ms: 1.02x slower                                                         |
| tomli_loads                | 2.08 sec                                                               | 2.13 sec: 1.03x slower                                                       |
| coroutines                 | 23.0 ms                                                                | 23.9 ms: 1.04x slower                                                        |
| pycparser                  | 1.13 sec                                                               | 1.18 sec: 1.04x slower                                                       |
| gc_traversal               | 4.38 ms                                                                | 4.71 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (21): async_tree_none, async_tree_memoization, scimark_monte_carlo, xml_etree_process, bench_mp_pool, sphinx, pylint, logging_silent, async_tree_memoization_tg, 2to3, sympy_integrate, json_loads, python_startup_no_site, scimark_lu, sqlalchemy_imperative, raytrace, sympy_expand, sympy_str, async_tree_none_tg, thrift, async_tree_cpu_io_mixed

- Geometric mean (including insignificant results): 1.004x faster
# HPT report

- Reliability score: 99.56% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x