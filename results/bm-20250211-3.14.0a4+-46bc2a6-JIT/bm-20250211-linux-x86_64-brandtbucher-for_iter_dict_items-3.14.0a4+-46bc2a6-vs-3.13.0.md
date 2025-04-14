# Results vs. 3.13.0

- fork: brandtbucher
- ref: for_iter_dict_items
- machine: linux-x86_64
- commit hash: 46bc2a6
- commit date: 2025-02-11
- overall geometric mean: 1.042x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                        |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                      |
| html5lib       | 63.4 ms                                                | 61.8 ms: 1.03x faster                                                       |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                        |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                                        |
| async_tree_io              | 838 ms                                                 | 622 ms: 1.35x faster                                                        |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                                        |
| async_tree_none            | 350 ms                                                 | 268 ms: 1.31x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 259 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 494 ms: 1.10x faster                                                        |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                        |
| coroutines                 | 22.2 ms                                                | 22.7 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.1 ms: 1.14x faster                                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| nbody          | 87.7 ms                                                | 96.8 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                       |
| regex_v8       | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                       |
| regex_dna      | 220 ms                                                 | 207 ms: 1.06x faster                                                        |
| regex_compile  | 132 ms                                                 | 125 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.82 sec: 1.16x faster                                                      |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                        |
| xml_etree_generate   | 86.8 ms                                                | 78.2 ms: 1.11x faster                                                       |
| xml_etree_process    | 60.5 ms                                                | 54.9 ms: 1.10x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 199 us: 1.07x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 95.9 ms: 1.06x faster                                                       |
| pickle_pure_python   | 302 us                                                 | 316 us: 1.05x slower                                                        |
| json_loads           | 27.2 us                                                | 28.9 us: 1.07x slower                                                       |
| json_dumps           | 10.1 ms                                                | 12.0 ms: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.04 ms: 1.01x slower                                                       |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.0 ms: 1.06x faster                                                       |
| genshi_text     | 22.6 ms                                                | 21.9 ms: 1.03x faster                                                       |
| genshi_xml      | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                       |
| django_template | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-46bc2a6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                        |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                                        |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                                        |
| async_tree_io              | 838 ms                                                 | 622 ms: 1.35x faster                                                        |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                                        |
| async_tree_none            | 350 ms                                                 | 268 ms: 1.31x faster                                                        |
| deepcopy_memo              | 38.4 us                                                | 30.8 us: 1.25x faster                                                       |
| spectral_norm              | 113 ms                                                 | 90.9 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 259 ms: 1.23x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                       |
| scimark_fft                | 367 ms                                                 | 312 ms: 1.18x faster                                                        |
| tomli_loads                | 2.12 sec                                               | 1.82 sec: 1.16x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                        |
| float                      | 78.7 ms                                                | 69.1 ms: 1.14x faster                                                       |
| regex_v8                   | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                       |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.52 ms: 1.11x faster                                                       |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                        |
| xml_etree_generate         | 86.8 ms                                                | 78.2 ms: 1.11x faster                                                       |
| xml_etree_process          | 60.5 ms                                                | 54.9 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 494 ms: 1.10x faster                                                        |
| telco                      | 8.40 ms                                                | 7.71 ms: 1.09x faster                                                       |
| crypto_pyaes               | 74.7 ms                                                | 69.1 ms: 1.08x faster                                                       |
| richards                   | 47.5 ms                                                | 44.1 ms: 1.08x faster                                                       |
| richards_super             | 53.7 ms                                                | 50.1 ms: 1.07x faster                                                       |
| unpickle_pure_python       | 213 us                                                 | 199 us: 1.07x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.37 sec: 1.07x faster                                                      |
| go                         | 141 ms                                                 | 131 ms: 1.07x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                      |
| pathlib                    | 17.4 ms                                                | 16.3 ms: 1.07x faster                                                       |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                                       |
| pyflate                    | 470 ms                                                 | 441 ms: 1.07x faster                                                        |
| mako                       | 10.7 ms                                                | 10.0 ms: 1.06x faster                                                       |
| regex_dna                  | 220 ms                                                 | 207 ms: 1.06x faster                                                        |
| async_generators           | 433 ms                                                 | 410 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 95.9 ms: 1.06x faster                                                       |
| regex_compile              | 132 ms                                                 | 125 ms: 1.05x faster                                                        |
| thrift                     | 800 us                                                 | 763 us: 1.05x faster                                                        |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                                        |
| logging_format             | 6.23 us                                                | 6.00 us: 1.04x faster                                                       |
| json                       | 5.32 ms                                                | 5.14 ms: 1.03x faster                                                       |
| genshi_text                | 22.6 ms                                                | 21.9 ms: 1.03x faster                                                       |
| logging_simple             | 5.65 us                                                | 5.47 us: 1.03x faster                                                       |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                        |
| generators                 | 28.8 ms                                                | 28.0 ms: 1.03x faster                                                       |
| html5lib                   | 63.4 ms                                                | 61.8 ms: 1.03x faster                                                       |
| connected_components       | 447 ms                                                 | 437 ms: 1.02x faster                                                        |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                      |
| k_core                     | 2.37 sec                                               | 2.32 sec: 1.02x faster                                                      |
| genshi_xml                 | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                       |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                        |
| shortest_path              | 487 ms                                                 | 481 ms: 1.01x faster                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 66.0 ms: 1.01x faster                                                       |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.01x faster                                                        |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| chaos                      | 58.0 ms                                                | 58.3 ms: 1.01x slower                                                       |
| python_startup_no_site     | 7.00 ms                                                | 7.04 ms: 1.01x slower                                                       |
| mdp                        | 2.54 sec                                               | 2.56 sec: 1.01x slower                                                      |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                       |
| gc_traversal               | 4.90 ms                                                | 4.94 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                                        |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                                        |
| sympy_integrate            | 19.8 ms                                                | 20.3 ms: 1.02x slower                                                       |
| coroutines                 | 22.2 ms                                                | 22.7 ms: 1.02x slower                                                       |
| sympy_str                  | 273 ms                                                 | 280 ms: 1.03x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.61 ms: 1.03x slower                                                       |
| django_template            | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                       |
| dulwich_log                | 64.6 ms                                                | 66.4 ms: 1.03x slower                                                       |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                      |
| sqlglot_optimize           | 53.4 ms                                                | 55.2 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.26 ms                                                | 1.31 ms: 1.04x slower                                                       |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                                        |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                                       |
| logging_silent             | 101 ns                                                 | 106 ns: 1.04x slower                                                        |
| pickle_pure_python         | 302 us                                                 | 316 us: 1.05x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 760 ms: 1.05x slower                                                        |
| sympy_expand               | 456 ms                                                 | 481 ms: 1.05x slower                                                        |
| deltablue                  | 3.19 ms                                                | 3.38 ms: 1.06x slower                                                       |
| raytrace                   | 262 ms                                                 | 277 ms: 1.06x slower                                                        |
| pprint_pformat             | 1.48 sec                                               | 1.57 sec: 1.06x slower                                                      |
| json_loads                 | 27.2 us                                                | 28.9 us: 1.07x slower                                                       |
| coverage                   | 82.8 ms                                                | 89.0 ms: 1.07x slower                                                       |
| bench_thread_pool          | 818 us                                                 | 886 us: 1.08x slower                                                        |
| nqueens                    | 80.9 ms                                                | 89.2 ms: 1.10x slower                                                       |
| nbody                      | 87.7 ms                                                | 96.8 ms: 1.10x slower                                                       |
| many_optionals             | 857 us                                                 | 953 us: 1.11x slower                                                        |
| hexiom                     | 6.08 ms                                                | 6.93 ms: 1.14x slower                                                       |
| json_dumps                 | 10.1 ms                                                | 12.0 ms: 1.19x slower                                                       |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.34x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 81.0 ms: 3.38x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (3): sqlalchemy_imperative, asyncio_websockets, fannkuch
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x