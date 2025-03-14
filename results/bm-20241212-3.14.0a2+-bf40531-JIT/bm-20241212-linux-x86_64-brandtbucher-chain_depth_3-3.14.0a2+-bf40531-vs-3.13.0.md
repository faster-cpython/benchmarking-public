# Results vs. 3.13.0

- fork: brandtbucher
- ref: chain_depth_3
- machine: linux-x86_64
- commit hash: bf40531
- commit date: 2024-12-12
- overall geometric mean: 1.038x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.04x faster                                                  |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                |
| html5lib       | 63.4 ms                                                | 64.5 ms: 1.02x slower                                                 |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 607 ms: 1.42x faster                                                  |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                  |
| async_tree_none            | 350 ms                                                 | 271 ms: 1.29x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 339 ms: 1.29x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                                  |
| async_generators           | 433 ms                                                 | 448 ms: 1.03x slower                                                  |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 87.7 ms                                                | 81.0 ms: 1.08x faster                                                 |
| float          | 78.7 ms                                                | 75.6 ms: 1.04x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.47 ms: 1.08x faster                                                 |
| regex_v8       | 26.9 ms                                                | 25.0 ms: 1.07x faster                                                 |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 86.8 ms                                                | 77.3 ms: 1.12x faster                                                 |
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.12x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 1.90 sec: 1.11x faster                                                |
| xml_etree_process    | 60.5 ms                                                | 54.5 ms: 1.11x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 194 us: 1.10x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 95.0 ms: 1.07x faster                                                 |
| json_loads           | 27.2 us                                                | 26.2 us: 1.04x faster                                                 |
| pickle_pure_python   | 302 us                                                 | 317 us: 1.05x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                 |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 9.99 ms: 1.07x faster                                                 |
| django_template | 31.7 ms                                                | 33.8 ms: 1.07x slower                                                 |
| genshi_text     | 22.6 ms                                                | 24.4 ms: 1.08x slower                                                 |
| genshi_xml      | 50.5 ms                                                | 58.9 ms: 1.17x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 607 ms: 1.42x faster                                                  |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                 |
| deepcopy                   | 354 us                                                 | 271 us: 1.31x faster                                                  |
| richards                   | 47.5 ms                                                | 36.7 ms: 1.30x faster                                                 |
| async_tree_none            | 350 ms                                                 | 271 ms: 1.29x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 339 ms: 1.29x faster                                                  |
| richards_super             | 53.7 ms                                                | 42.6 ms: 1.26x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                                 |
| scimark_fft                | 367 ms                                                 | 318 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.14x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 77.3 ms: 1.12x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.12x faster                                                  |
| telco                      | 8.40 ms                                                | 7.53 ms: 1.12x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 1.90 sec: 1.11x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 54.5 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.57 ms: 1.10x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 194 us: 1.10x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 68.1 ms: 1.10x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.47 ms: 1.08x faster                                                 |
| pylint                     | 312 ms                                                 | 288 ms: 1.08x faster                                                  |
| nbody                      | 87.7 ms                                                | 81.0 ms: 1.08x faster                                                 |
| pathlib                    | 17.4 ms                                                | 16.1 ms: 1.08x faster                                                 |
| json                       | 5.32 ms                                                | 4.92 ms: 1.08x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 25.0 ms: 1.07x faster                                                 |
| go                         | 141 ms                                                 | 131 ms: 1.07x faster                                                  |
| mako                       | 10.7 ms                                                | 9.99 ms: 1.07x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.39 sec: 1.07x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 95.0 ms: 1.07x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                |
| pyflate                    | 470 ms                                                 | 448 ms: 1.05x faster                                                  |
| scimark_lu                 | 114 ms                                                 | 110 ms: 1.04x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 64.1 ms: 1.04x faster                                                 |
| float                      | 78.7 ms                                                | 75.6 ms: 1.04x faster                                                 |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                                  |
| 2to3                       | 266 ms                                                 | 257 ms: 1.04x faster                                                  |
| json_loads                 | 27.2 us                                                | 26.2 us: 1.04x faster                                                 |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                |
| thrift                     | 800 us                                                 | 778 us: 1.03x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.03x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.78 ms: 1.02x faster                                                 |
| connected_components       | 447 ms                                                 | 436 ms: 1.02x faster                                                  |
| fannkuch                   | 394 ms                                                 | 385 ms: 1.02x faster                                                  |
| spectral_norm              | 113 ms                                                 | 111 ms: 1.02x faster                                                  |
| shortest_path              | 487 ms                                                 | 478 ms: 1.02x faster                                                  |
| pprint_safe_repr           | 727 ms                                                 | 715 ms: 1.02x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                 |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                                |
| regex_dna                  | 220 ms                                                 | 218 ms: 1.01x faster                                                  |
| deltablue                  | 3.19 ms                                                | 3.17 ms: 1.01x faster                                                 |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.01x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                 |
| mdp                        | 2.54 sec                                               | 2.57 sec: 1.01x slower                                                |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                 |
| logging_simple             | 5.65 us                                                | 5.72 us: 1.01x slower                                                 |
| chaos                      | 58.0 ms                                                | 58.8 ms: 1.01x slower                                                 |
| html5lib                   | 63.4 ms                                                | 64.5 ms: 1.02x slower                                                 |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                                  |
| sympy_str                  | 273 ms                                                 | 280 ms: 1.03x slower                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.30 ms: 1.03x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.03x slower                                                  |
| async_generators           | 433 ms                                                 | 448 ms: 1.03x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                |
| sqlglot_transpile          | 1.57 ms                                                | 1.63 ms: 1.03x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 166 us: 1.04x slower                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 55.4 ms: 1.04x slower                                                 |
| sympy_integrate            | 19.8 ms                                                | 20.6 ms: 1.04x slower                                                 |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                 |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                                 |
| dulwich_log                | 64.6 ms                                                | 67.4 ms: 1.04x slower                                                 |
| sympy_expand               | 456 ms                                                 | 477 ms: 1.05x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 317 us: 1.05x slower                                                  |
| django_template            | 31.7 ms                                                | 33.8 ms: 1.07x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 875 us: 1.07x slower                                                  |
| genshi_text                | 22.6 ms                                                | 24.4 ms: 1.08x slower                                                 |
| raytrace                   | 262 ms                                                 | 283 ms: 1.08x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.10x slower                                                 |
| nqueens                    | 80.9 ms                                                | 89.5 ms: 1.11x slower                                                 |
| many_optionals             | 857 us                                                 | 976 us: 1.14x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.99 ms: 1.15x slower                                                 |
| genshi_xml                 | 50.5 ms                                                | 58.9 ms: 1.17x slower                                                 |
| generators                 | 28.8 ms                                                | 36.1 ms: 1.26x slower                                                 |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (5): djangocms, logging_format, asyncio_websockets, coverage, logging_silent
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241212-3.14.0a2+-bf40531-JIT/bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531.json: mypy2

- Geometric mean (including insignificant results): 1.038x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x