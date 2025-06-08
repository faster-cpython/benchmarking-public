# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.163x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 292 ms: 1.10x slower                                                  |
| docutils       | 2.58 sec                                               | 2.86 sec: 1.11x slower                                                |
| html5lib       | 63.4 ms                                                | 67.7 ms: 1.07x slower                                                 |
| sphinx         | 1.03 sec                                               | 1.13 sec: 1.10x slower                                                |
| Geometric mean | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 353 ms: 1.31x faster                                                  |
| async_tree_io              | 838 ms                                                 | 666 ms: 1.26x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 349 ms: 1.25x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 696 ms: 1.24x faster                                                  |
| async_tree_none            | 350 ms                                                 | 291 ms: 1.20x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 281 ms: 1.14x faster                                                  |
| async_generators           | 433 ms                                                 | 419 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 596 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 589 ms: 1.08x slower                                                  |
| coroutines                 | 22.2 ms                                                | 27.0 ms: 1.22x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 75.0 ms: 1.05x faster                                                 |
| pidigits       | 186 ms                                                 | 207 ms: 1.11x slower                                                  |
| nbody          | 87.7 ms                                                | 106 ms: 1.21x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.01 ms: 1.25x faster                                                 |
| regex_v8       | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                 |
| regex_dna      | 220 ms                                                 | 203 ms: 1.08x faster                                                  |
| regex_compile  | 132 ms                                                 | 144 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 162 ms: 1.05x slower                                                  |
| tomli_loads          | 2.12 sec                                               | 2.24 sec: 1.06x slower                                                |
| xml_etree_iterparse  | 101 ms                                                 | 111 ms: 1.10x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 256 us: 1.20x slower                                                  |
| json_loads           | 27.2 us                                                | 33.6 us: 1.24x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 375 us: 1.24x slower                                                  |
| xml_etree_process    | 60.5 ms                                                | 75.3 ms: 1.24x slower                                                 |
| xml_etree_generate   | 86.8 ms                                                | 110 ms: 1.27x slower                                                  |
| json_dumps           | 10.1 ms                                                | 13.4 ms: 1.33x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.19x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                 |
| python_startup_no_site | 7.00 ms                                                | 7.35 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 25.4 ms: 1.12x slower                                                 |
| genshi_xml      | 50.5 ms                                                | 57.2 ms: 1.13x slower                                                 |
| django_template | 31.7 ms                                                | 40.2 ms: 1.27x slower                                                 |
| mako            | 10.7 ms                                                | 13.8 ms: 1.29x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.20x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.48 sec: 1.72x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 353 ms: 1.31x faster                                                  |
| async_tree_io              | 838 ms                                                 | 666 ms: 1.26x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.01 ms: 1.25x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 349 ms: 1.25x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 696 ms: 1.24x faster                                                  |
| async_tree_none            | 350 ms                                                 | 291 ms: 1.20x faster                                                  |
| go                         | 141 ms                                                 | 119 ms: 1.19x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 281 ms: 1.14x faster                                                  |
| deepcopy                   | 354 us                                                 | 314 us: 1.13x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 34.3 us: 1.12x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                 |
| regex_dna                  | 220 ms                                                 | 203 ms: 1.08x faster                                                  |
| float                      | 78.7 ms                                                | 75.0 ms: 1.05x faster                                                 |
| async_generators           | 433 ms                                                 | 419 ms: 1.03x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 64.3 ms: 1.01x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.42 sec: 1.02x slower                                                |
| deepcopy_reduce            | 3.24 us                                                | 3.34 us: 1.03x slower                                                 |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 596 ms: 1.04x slower                                                  |
| spectral_norm              | 113 ms                                                 | 118 ms: 1.04x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 5.13 ms: 1.05x slower                                                 |
| xml_etree_parse            | 154 ms                                                 | 162 ms: 1.05x slower                                                  |
| pathlib                    | 17.4 ms                                                | 18.2 ms: 1.05x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 7.35 ms: 1.05x slower                                                 |
| pycparser                  | 1.20 sec                                               | 1.26 sec: 1.05x slower                                                |
| tomli_loads                | 2.12 sec                                               | 2.24 sec: 1.06x slower                                                |
| sympy_integrate            | 19.8 ms                                                | 21.0 ms: 1.06x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.61 ms: 1.06x slower                                                 |
| html5lib                   | 63.4 ms                                                | 67.7 ms: 1.07x slower                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 589 ms: 1.08x slower                                                  |
| meteor_contest             | 108 ms                                                 | 119 ms: 1.09x slower                                                  |
| regex_compile              | 132 ms                                                 | 144 ms: 1.09x slower                                                  |
| 2to3                       | 266 ms                                                 | 292 ms: 1.10x slower                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 111 ms: 1.10x slower                                                  |
| shortest_path              | 487 ms                                                 | 534 ms: 1.10x slower                                                  |
| connected_components       | 447 ms                                                 | 491 ms: 1.10x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.13 sec: 1.10x slower                                                |
| hexiom                     | 6.08 ms                                                | 6.71 ms: 1.10x slower                                                 |
| sqlite_synth               | 2.90 us                                                | 3.21 us: 1.10x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.86 sec: 1.11x slower                                                |
| pidigits                   | 186 ms                                                 | 207 ms: 1.11x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 167 ms: 1.11x slower                                                  |
| scimark_sor                | 122 ms                                                 | 137 ms: 1.12x slower                                                  |
| scimark_fft                | 367 ms                                                 | 412 ms: 1.12x slower                                                  |
| genshi_text                | 22.6 ms                                                | 25.4 ms: 1.12x slower                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.68 ms: 1.13x slower                                                 |
| genshi_xml                 | 50.5 ms                                                | 57.2 ms: 1.13x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 5.32 sec: 1.14x slower                                                |
| richards                   | 47.5 ms                                                | 54.0 ms: 1.14x slower                                                 |
| sympy_str                  | 273 ms                                                 | 310 ms: 1.14x slower                                                  |
| richards_super             | 53.7 ms                                                | 61.4 ms: 1.14x slower                                                 |
| generators                 | 28.8 ms                                                | 32.9 ms: 1.14x slower                                                 |
| json                       | 5.32 ms                                                | 6.11 ms: 1.15x slower                                                 |
| telco                      | 8.40 ms                                                | 9.64 ms: 1.15x slower                                                 |
| comprehensions             | 16.5 us                                                | 19.2 us: 1.16x slower                                                 |
| crypto_pyaes               | 74.7 ms                                                | 86.9 ms: 1.16x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 133 ms: 1.16x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 954 us: 1.17x slower                                                  |
| sympy_expand               | 456 ms                                                 | 534 ms: 1.17x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 78.2 ms: 1.17x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 256 us: 1.20x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.84 ms: 1.20x slower                                                 |
| chaos                      | 58.0 ms                                                | 69.9 ms: 1.20x slower                                                 |
| nbody                      | 87.7 ms                                                | 106 ms: 1.21x slower                                                  |
| coroutines                 | 22.2 ms                                                | 27.0 ms: 1.22x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 197 us: 1.23x slower                                                  |
| raytrace                   | 262 ms                                                 | 322 ms: 1.23x slower                                                  |
| json_loads                 | 27.2 us                                                | 33.6 us: 1.24x slower                                                 |
| nqueens                    | 80.9 ms                                                | 100 ms: 1.24x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 375 us: 1.24x slower                                                  |
| xml_etree_process          | 60.5 ms                                                | 75.3 ms: 1.24x slower                                                 |
| fannkuch                   | 394 ms                                                 | 491 ms: 1.25x slower                                                  |
| many_optionals             | 857 us                                                 | 1.08 ms: 1.26x slower                                                 |
| xml_etree_generate         | 86.8 ms                                                | 110 ms: 1.27x slower                                                  |
| django_template            | 31.7 ms                                                | 40.2 ms: 1.27x slower                                                 |
| mako                       | 10.7 ms                                                | 13.8 ms: 1.29x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 13.4 ms: 1.33x slower                                                 |
| logging_simple             | 5.65 us                                                | 7.51 us: 1.33x slower                                                 |
| logging_format             | 6.23 us                                                | 8.46 us: 1.36x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 1.00 sec: 1.38x slower                                                |
| pprint_pformat             | 1.48 sec                                               | 2.05 sec: 1.39x slower                                                |
| subparsers                 | 15.5 ms                                                | 28.0 ms: 1.81x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 104 ms: 4.35x slower                                                  |
| logging_silent             | 101 ns                                                 | 625 ns: 6.19x slower                                                  |
| coverage                   | 82.8 ms                                                | 519 ms: 6.26x slower                                                  |
| thrift                     | 800 us                                                 | 149 ms: 186.37x slower                                                |
| Geometric mean             | (ref)                                                  | 1.21x slower                                                          |

Benchmark hidden because not significant (3): pylint, pyflate, asyncio_websockets
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.163x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.05x