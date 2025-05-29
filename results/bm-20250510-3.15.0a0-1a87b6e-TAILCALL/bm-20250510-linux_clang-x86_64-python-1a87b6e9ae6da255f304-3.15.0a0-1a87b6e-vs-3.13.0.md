# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.016x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 253 ms: 1.05x faster                                                  |
| docutils       | 2.58 sec                                               | 2.63 sec: 1.02x slower                                                |
| html5lib       | 63.4 ms                                                | 57.6 ms: 1.10x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                  |
| async_tree_io              | 838 ms                                                 | 585 ms: 1.43x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 308 ms: 1.42x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                  |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.30x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.13x faster                                                  |
| async_generators           | 433 ms                                                 | 394 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 496 ms: 1.10x faster                                                  |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.5 ms: 1.17x faster                                                 |
| nbody          | 87.7 ms                                                | 86.4 ms: 1.01x faster                                                 |
| pidigits       | 186 ms                                                 | 210 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 25.0 ms: 1.07x faster                                                 |
| regex_dna      | 220 ms                                                 | 206 ms: 1.07x faster                                                  |
| regex_compile  | 132 ms                                                 | 124 ms: 1.07x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.54 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                |
| xml_etree_process    | 60.5 ms                                                | 60.1 ms: 1.01x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 212 us: 1.01x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 308 us: 1.02x slower                                                  |
| xml_etree_generate   | 86.8 ms                                                | 88.6 ms: 1.02x slower                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.03x slower                                                  |
| xml_etree_parse      | 154 ms                                                 | 164 ms: 1.07x slower                                                  |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                 |
| json_dumps           | 10.1 ms                                                | 12.9 ms: 1.27x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.1 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.92 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 48.0 ms: 1.05x faster                                                 |
| django_template | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                 |
| mako            | 10.7 ms                                                | 12.2 ms: 1.14x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.09x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                  |
| deepcopy                   | 354 us                                                 | 246 us: 1.44x faster                                                  |
| async_tree_io              | 838 ms                                                 | 585 ms: 1.43x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 308 ms: 1.42x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                  |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 28.8 us: 1.33x faster                                                 |
| go                         | 141 ms                                                 | 107 ms: 1.31x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.30x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.60 us: 1.25x faster                                                 |
| scimark_fft                | 367 ms                                                 | 305 ms: 1.20x faster                                                  |
| spectral_norm              | 113 ms                                                 | 94.5 ms: 1.20x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.29 ms: 1.17x faster                                                 |
| float                      | 78.7 ms                                                | 67.5 ms: 1.17x faster                                                 |
| richards                   | 47.5 ms                                                | 41.0 ms: 1.16x faster                                                 |
| telco                      | 8.40 ms                                                | 7.33 ms: 1.15x faster                                                 |
| richards_super             | 53.7 ms                                                | 47.3 ms: 1.14x faster                                                 |
| scimark_sor                | 122 ms                                                 | 108 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.13x faster                                                  |
| pathlib                    | 17.4 ms                                                | 15.4 ms: 1.13x faster                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 59.7 ms: 1.12x faster                                                 |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 58.0 ms: 1.11x faster                                                 |
| pyflate                    | 470 ms                                                 | 423 ms: 1.11x faster                                                  |
| html5lib                   | 63.4 ms                                                | 57.6 ms: 1.10x faster                                                 |
| async_generators           | 433 ms                                                 | 394 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 496 ms: 1.10x faster                                                  |
| genshi_text                | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.34 sec: 1.08x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 18.4 ms: 1.08x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                |
| chaos                      | 58.0 ms                                                | 53.9 ms: 1.08x faster                                                 |
| scimark_lu                 | 114 ms                                                 | 106 ms: 1.08x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 25.0 ms: 1.07x faster                                                 |
| deltablue                  | 3.19 ms                                                | 2.98 ms: 1.07x faster                                                 |
| regex_dna                  | 220 ms                                                 | 206 ms: 1.07x faster                                                  |
| regex_compile              | 132 ms                                                 | 124 ms: 1.07x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.54 ms: 1.06x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.06x faster                                                 |
| hexiom                     | 6.08 ms                                                | 5.76 ms: 1.06x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 48.0 ms: 1.05x faster                                                 |
| 2to3                       | 266 ms                                                 | 253 ms: 1.05x faster                                                  |
| raytrace                   | 262 ms                                                 | 249 ms: 1.05x faster                                                  |
| python_startup             | 12.7 ms                                                | 12.1 ms: 1.04x faster                                                 |
| sympy_str                  | 273 ms                                                 | 262 ms: 1.04x faster                                                  |
| nqueens                    | 80.9 ms                                                | 78.1 ms: 1.04x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                  |
| comprehensions             | 16.5 us                                                | 16.0 us: 1.03x faster                                                 |
| sympy_expand               | 456 ms                                                 | 446 ms: 1.02x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 73.1 ms: 1.02x faster                                                 |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                |
| nbody                      | 87.7 ms                                                | 86.4 ms: 1.01x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.92 ms: 1.01x faster                                                 |
| django_template            | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 60.1 ms: 1.01x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 212 us: 1.01x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.88 ms: 1.00x faster                                                 |
| generators                 | 28.8 ms                                                | 28.9 ms: 1.01x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.63 sec: 1.02x slower                                                |
| pickle_pure_python         | 302 us                                                 | 308 us: 1.02x slower                                                  |
| xml_etree_generate         | 86.8 ms                                                | 88.6 ms: 1.02x slower                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 104 ms: 1.03x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 751 ms: 1.03x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.54 sec: 1.04x slower                                                |
| bench_thread_pool          | 818 us                                                 | 852 us: 1.04x slower                                                  |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                 |
| connected_components       | 447 ms                                                 | 466 ms: 1.04x slower                                                  |
| fannkuch                   | 394 ms                                                 | 412 ms: 1.05x slower                                                  |
| meteor_contest             | 108 ms                                                 | 115 ms: 1.06x slower                                                  |
| shortest_path              | 487 ms                                                 | 516 ms: 1.06x slower                                                  |
| xml_etree_parse            | 154 ms                                                 | 164 ms: 1.07x slower                                                  |
| logging_simple             | 5.65 us                                                | 6.04 us: 1.07x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.64 ms: 1.08x slower                                                 |
| logging_format             | 6.23 us                                                | 6.79 us: 1.09x slower                                                 |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                 |
| many_optionals             | 857 us                                                 | 960 us: 1.12x slower                                                  |
| pidigits                   | 186 ms                                                 | 210 ms: 1.13x slower                                                  |
| mako                       | 10.7 ms                                                | 12.2 ms: 1.14x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 12.9 ms: 1.27x slower                                                 |
| subparsers                 | 15.5 ms                                                | 22.8 ms: 1.47x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 92.5 ms: 3.86x slower                                                 |
| coverage                   | 82.8 ms                                                | 413 ms: 4.98x slower                                                  |
| logging_silent             | 101 ns                                                 | 508 ns: 5.03x slower                                                  |
| thrift                     | 800 us                                                 | 148 ms: 185.49x slower                                                |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (4): k_core, typing_runtime_protocols, json, asyncio_websockets
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (21) of results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-linux-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, asyncio_tcp, asyncio_tcp_ssl, dask, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.016x slower

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x