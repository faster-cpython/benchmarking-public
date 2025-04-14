# Results vs. 3.13.0

- fork: python
- ref: v3.13.2
- machine: linux-x86_64
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.003x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 266 ms: 1.00x slower                                   |
| chameleon      | 6.81 ms                                                | 6.89 ms: 1.01x slower                                  |
| html5lib       | 63.4 ms                                                | 64.7 ms: 1.02x slower                                  |
| tornado_http   | 91.2 ms                                                | 91.7 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_generators           | 433 ms                                                 | 392 ms: 1.10x faster                                   |
| async_tree_none_tg         | 319 ms                                                 | 312 ms: 1.02x faster                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 455 ms: 1.02x faster                                   |
| coroutines                 | 22.2 ms                                                | 22.4 ms: 1.01x slower                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 581 ms: 1.01x slower                                   |
| async_tree_memoization     | 437 ms                                                 | 457 ms: 1.05x slower                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 599 ms: 1.10x slower                                   |
| Geometric mean             | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_none, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.38 ms: 1.11x faster                                  |
| regex_v8       | 26.9 ms                                                | 26.4 ms: 1.02x faster                                  |
| regex_compile  | 132 ms                                                 | 131 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                  |
| xml_etree_generate   | 86.8 ms                                                | 86.2 ms: 1.01x faster                                  |
| xml_etree_parse      | 154 ms                                                 | 155 ms: 1.01x slower                                   |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                   |
| xml_etree_iterparse  | 101 ms                                                 | 103 ms: 1.02x slower                                   |
| json_dumps           | 10.1 ms                                                | 10.4 ms: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (3): tomli_loads, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.99 ms: 1.00x faster                                  |
| python_startup         | 12.7 ms                                                | 12.7 ms: 1.00x slower                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 51.0 ms: 1.01x slower                                  |
| django_template | 31.7 ms                                                | 32.1 ms: 1.01x slower                                  |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                  |
| Geometric mean  | (ref)                                                  | 1.02x slower                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot               | 3.77 ms                                                | 3.38 ms: 1.11x faster                                  |
| async_generators           | 433 ms                                                 | 392 ms: 1.10x faster                                   |
| gc_traversal               | 4.90 ms                                                | 4.65 ms: 1.05x faster                                  |
| json                       | 5.32 ms                                                | 5.13 ms: 1.04x faster                                  |
| nqueens                    | 80.9 ms                                                | 78.1 ms: 1.04x faster                                  |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                 |
| async_tree_none_tg         | 319 ms                                                 | 312 ms: 1.02x faster                                   |
| spectral_norm              | 113 ms                                                 | 111 ms: 1.02x faster                                   |
| regex_v8                   | 26.9 ms                                                | 26.4 ms: 1.02x faster                                  |
| async_tree_memoization_tg  | 463 ms                                                 | 455 ms: 1.02x faster                                   |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                  |
| scimark_fft                | 367 ms                                                 | 361 ms: 1.02x faster                                   |
| thrift                     | 800 us                                                 | 789 us: 1.01x faster                                   |
| deepcopy_reduce            | 3.24 us                                                | 3.21 us: 1.01x faster                                  |
| regex_compile              | 132 ms                                                 | 131 ms: 1.01x faster                                   |
| xml_etree_generate         | 86.8 ms                                                | 86.2 ms: 1.01x faster                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.44 ms: 1.00x faster                                  |
| bench_thread_pool          | 818 us                                                 | 815 us: 1.00x faster                                   |
| deltablue                  | 3.19 ms                                                | 3.18 ms: 1.00x faster                                  |
| python_startup_no_site     | 7.00 ms                                                | 6.99 ms: 1.00x faster                                  |
| 2to3                       | 266 ms                                                 | 266 ms: 1.00x slower                                   |
| bench_mp_pool              | 24.0 ms                                                | 24.0 ms: 1.00x slower                                  |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.00x slower                                   |
| dulwich_log                | 64.6 ms                                                | 64.9 ms: 1.00x slower                                  |
| python_startup             | 12.7 ms                                                | 12.7 ms: 1.00x slower                                  |
| tornado_http               | 91.2 ms                                                | 91.7 ms: 1.01x slower                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                  |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                   |
| richards                   | 47.5 ms                                                | 47.8 ms: 1.01x slower                                  |
| xml_etree_parse            | 154 ms                                                 | 155 ms: 1.01x slower                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.0 ms: 1.01x slower                                  |
| typing_runtime_protocols   | 160 us                                                 | 161 us: 1.01x slower                                   |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                   |
| mdp                        | 2.54 sec                                               | 2.56 sec: 1.01x slower                                 |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.07 ms: 1.01x slower                                  |
| pyflate                    | 470 ms                                                 | 474 ms: 1.01x slower                                   |
| subparsers                 | 15.5 ms                                                | 15.6 ms: 1.01x slower                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.73 sec: 1.01x slower                                 |
| deepcopy_memo              | 38.4 us                                                | 38.8 us: 1.01x slower                                  |
| coroutines                 | 22.2 ms                                                | 22.4 ms: 1.01x slower                                  |
| genshi_xml                 | 50.5 ms                                                | 51.0 ms: 1.01x slower                                  |
| sqlglot_optimize           | 53.4 ms                                                | 53.9 ms: 1.01x slower                                  |
| gunicorn                   | 1.18 ms                                                | 1.20 ms: 1.01x slower                                  |
| chameleon                  | 6.81 ms                                                | 6.89 ms: 1.01x slower                                  |
| logging_simple             | 5.65 us                                                | 5.72 us: 1.01x slower                                  |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                  |
| generators                 | 28.8 ms                                                | 29.2 ms: 1.01x slower                                  |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.01x slower                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 581 ms: 1.01x slower                                   |
| many_optionals             | 857 us                                                 | 869 us: 1.01x slower                                   |
| pprint_safe_repr           | 727 ms                                                 | 737 ms: 1.01x slower                                   |
| sympy_expand               | 456 ms                                                 | 463 ms: 1.02x slower                                   |
| deepcopy                   | 354 us                                                 | 360 us: 1.02x slower                                   |
| fannkuch                   | 394 ms                                                 | 400 ms: 1.02x slower                                   |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                   |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                   |
| chaos                      | 58.0 ms                                                | 59.0 ms: 1.02x slower                                  |
| xml_etree_iterparse        | 101 ms                                                 | 103 ms: 1.02x slower                                   |
| pprint_pformat             | 1.48 sec                                               | 1.51 sec: 1.02x slower                                 |
| html5lib                   | 63.4 ms                                                | 64.7 ms: 1.02x slower                                  |
| gevent_hub                 | 1.05 ns                                                | 1.07 ns: 1.02x slower                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 68.2 ms: 1.02x slower                                  |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                   |
| hexiom                     | 6.08 ms                                                | 6.21 ms: 1.02x slower                                  |
| coverage                   | 82.8 ms                                                | 84.8 ms: 1.02x slower                                  |
| richards_super             | 53.7 ms                                                | 55.1 ms: 1.02x slower                                  |
| telco                      | 8.40 ms                                                | 8.62 ms: 1.03x slower                                  |
| json_dumps                 | 10.1 ms                                                | 10.4 ms: 1.03x slower                                  |
| logging_format             | 6.23 us                                                | 6.43 us: 1.03x slower                                  |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                  |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                   |
| async_tree_memoization     | 437 ms                                                 | 457 ms: 1.05x slower                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 599 ms: 1.10x slower                                   |
| Geometric mean             | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (27): logging_silent, k_core, tomli_loads, djangocms, crypto_pyaes, sqlite_synth, sqlalchemy_declarative, regex_dna, xml_etree_process, docutils, go, shortest_path, sympy_str, pathlib, sphinx, sympy_integrate, sqlglot_parse, asyncio_websockets, nbody, float, genshi_text, connected_components, async_tree_none, pickle_pure_python, pylint, async_tree_io, async_tree_io_tg

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x