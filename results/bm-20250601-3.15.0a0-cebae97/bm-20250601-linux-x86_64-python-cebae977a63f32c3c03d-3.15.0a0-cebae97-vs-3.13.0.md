# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.160x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 289 ms: 1.09x slower                                                  |
| docutils       | 2.58 sec                                               | 2.84 sec: 1.10x slower                                                |
| html5lib       | 63.4 ms                                                | 66.2 ms: 1.04x slower                                                 |
| sphinx         | 1.03 sec                                               | 1.12 sec: 1.09x slower                                                |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 352 ms: 1.31x faster                                                  |
| async_tree_io              | 838 ms                                                 | 662 ms: 1.27x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 350 ms: 1.25x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 696 ms: 1.24x faster                                                  |
| async_tree_none            | 350 ms                                                 | 291 ms: 1.20x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 279 ms: 1.14x faster                                                  |
| async_generators           | 433 ms                                                 | 416 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 607 ms: 1.06x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 598 ms: 1.10x slower                                                  |
| coroutines                 | 22.2 ms                                                | 28.1 ms: 1.27x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 75.1 ms: 1.05x faster                                                 |
| pidigits       | 186 ms                                                 | 202 ms: 1.09x slower                                                  |
| nbody          | 87.7 ms                                                | 109 ms: 1.24x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.00 ms: 1.25x faster                                                 |
| regex_v8       | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                 |
| regex_dna      | 220 ms                                                 | 204 ms: 1.08x faster                                                  |
| regex_compile  | 132 ms                                                 | 143 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 161 ms: 1.04x slower                                                  |
| tomli_loads          | 2.12 sec                                               | 2.25 sec: 1.06x slower                                                |
| xml_etree_iterparse  | 101 ms                                                 | 111 ms: 1.09x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 255 us: 1.20x slower                                                  |
| xml_etree_process    | 60.5 ms                                                | 73.6 ms: 1.22x slower                                                 |
| xml_etree_generate   | 86.8 ms                                                | 107 ms: 1.23x slower                                                  |
| json_loads           | 27.2 us                                                | 33.9 us: 1.25x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 380 us: 1.26x slower                                                  |
| json_dumps           | 10.1 ms                                                | 13.3 ms: 1.32x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.18x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                 |
| python_startup_no_site | 7.00 ms                                                | 7.42 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 25.0 ms: 1.11x slower                                                 |
| genshi_xml      | 50.5 ms                                                | 57.5 ms: 1.14x slower                                                 |
| django_template | 31.7 ms                                                | 40.3 ms: 1.27x slower                                                 |
| mako            | 10.7 ms                                                | 13.7 ms: 1.28x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.20x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.47 sec: 1.73x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 352 ms: 1.31x faster                                                  |
| async_tree_io              | 838 ms                                                 | 662 ms: 1.27x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.00 ms: 1.25x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 350 ms: 1.25x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 696 ms: 1.24x faster                                                  |
| async_tree_none            | 350 ms                                                 | 291 ms: 1.20x faster                                                  |
| go                         | 141 ms                                                 | 119 ms: 1.18x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 279 ms: 1.14x faster                                                  |
| deepcopy                   | 354 us                                                 | 310 us: 1.14x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 34.0 us: 1.13x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                 |
| regex_dna                  | 220 ms                                                 | 204 ms: 1.08x faster                                                  |
| float                      | 78.7 ms                                                | 75.1 ms: 1.05x faster                                                 |
| async_generators           | 433 ms                                                 | 416 ms: 1.04x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 64.0 ms: 1.01x faster                                                 |
| pyflate                    | 470 ms                                                 | 476 ms: 1.01x slower                                                  |
| deepcopy_reduce            | 3.24 us                                                | 3.30 us: 1.02x slower                                                 |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                 |
| pycparser                  | 1.20 sec                                               | 1.25 sec: 1.04x slower                                                |
| html5lib                   | 63.4 ms                                                | 66.2 ms: 1.04x slower                                                 |
| xml_etree_parse            | 154 ms                                                 | 161 ms: 1.04x slower                                                  |
| pathlib                    | 17.4 ms                                                | 18.2 ms: 1.05x slower                                                 |
| gc_traversal               | 4.90 ms                                                | 5.16 ms: 1.05x slower                                                 |
| sympy_integrate            | 19.8 ms                                                | 20.9 ms: 1.06x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 7.42 ms: 1.06x slower                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 607 ms: 1.06x slower                                                  |
| tomli_loads                | 2.12 sec                                               | 2.25 sec: 1.06x slower                                                |
| meteor_contest             | 108 ms                                                 | 116 ms: 1.07x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.63 ms: 1.07x slower                                                 |
| pidigits                   | 186 ms                                                 | 202 ms: 1.09x slower                                                  |
| regex_compile              | 132 ms                                                 | 143 ms: 1.09x slower                                                  |
| shortest_path              | 487 ms                                                 | 529 ms: 1.09x slower                                                  |
| 2to3                       | 266 ms                                                 | 289 ms: 1.09x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.12 sec: 1.09x slower                                                |
| connected_components       | 447 ms                                                 | 487 ms: 1.09x slower                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 111 ms: 1.09x slower                                                  |
| sqlite_synth               | 2.90 us                                                | 3.17 us: 1.09x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.66 ms: 1.10x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.84 sec: 1.10x slower                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 598 ms: 1.10x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 166 ms: 1.10x slower                                                  |
| genshi_text                | 22.6 ms                                                | 25.0 ms: 1.11x slower                                                 |
| scimark_sor                | 122 ms                                                 | 136 ms: 1.11x slower                                                  |
| telco                      | 8.40 ms                                                | 9.39 ms: 1.12x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 5.25 sec: 1.12x slower                                                |
| sympy_str                  | 273 ms                                                 | 307 ms: 1.13x slower                                                  |
| generators                 | 28.8 ms                                                | 32.4 ms: 1.13x slower                                                 |
| genshi_xml                 | 50.5 ms                                                | 57.5 ms: 1.14x slower                                                 |
| richards                   | 47.5 ms                                                | 54.3 ms: 1.14x slower                                                 |
| scimark_fft                | 367 ms                                                 | 420 ms: 1.14x slower                                                  |
| richards_super             | 53.7 ms                                                | 61.5 ms: 1.14x slower                                                 |
| json                       | 5.32 ms                                                | 6.11 ms: 1.15x slower                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.78 ms: 1.15x slower                                                 |
| comprehensions             | 16.5 us                                                | 19.1 us: 1.16x slower                                                 |
| crypto_pyaes               | 74.7 ms                                                | 87.1 ms: 1.17x slower                                                 |
| sympy_expand               | 456 ms                                                 | 534 ms: 1.17x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 957 us: 1.17x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 134 ms: 1.17x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 78.2 ms: 1.17x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 255 us: 1.20x slower                                                  |
| chaos                      | 58.0 ms                                                | 69.9 ms: 1.20x slower                                                 |
| deltablue                  | 3.19 ms                                                | 3.86 ms: 1.21x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 195 us: 1.22x slower                                                  |
| xml_etree_process          | 60.5 ms                                                | 73.6 ms: 1.22x slower                                                 |
| raytrace                   | 262 ms                                                 | 319 ms: 1.22x slower                                                  |
| nqueens                    | 80.9 ms                                                | 99.3 ms: 1.23x slower                                                 |
| xml_etree_generate         | 86.8 ms                                                | 107 ms: 1.23x slower                                                  |
| nbody                      | 87.7 ms                                                | 109 ms: 1.24x slower                                                  |
| fannkuch                   | 394 ms                                                 | 491 ms: 1.25x slower                                                  |
| json_loads                 | 27.2 us                                                | 33.9 us: 1.25x slower                                                 |
| many_optionals             | 857 us                                                 | 1.07 ms: 1.25x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 380 us: 1.26x slower                                                  |
| coroutines                 | 22.2 ms                                                | 28.1 ms: 1.27x slower                                                 |
| django_template            | 31.7 ms                                                | 40.3 ms: 1.27x slower                                                 |
| mako                       | 10.7 ms                                                | 13.7 ms: 1.28x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 13.3 ms: 1.32x slower                                                 |
| logging_simple             | 5.65 us                                                | 7.52 us: 1.33x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 988 ms: 1.36x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 2.01 sec: 1.36x slower                                                |
| logging_format             | 6.23 us                                                | 8.58 us: 1.38x slower                                                 |
| subparsers                 | 15.5 ms                                                | 28.0 ms: 1.81x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 104 ms: 4.34x slower                                                  |
| coverage                   | 82.8 ms                                                | 514 ms: 6.21x slower                                                  |
| logging_silent             | 101 ns                                                 | 651 ns: 6.44x slower                                                  |
| thrift                     | 800 us                                                 | 149 ms: 186.09x slower                                                |
| Geometric mean             | (ref)                                                  | 1.21x slower                                                          |

Benchmark hidden because not significant (4): pylint, spectral_norm, asyncio_websockets, k_core
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.160x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.05x