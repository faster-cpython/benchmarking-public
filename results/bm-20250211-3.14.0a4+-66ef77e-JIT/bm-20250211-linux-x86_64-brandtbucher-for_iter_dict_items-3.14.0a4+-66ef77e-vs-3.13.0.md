# Results vs. 3.13.0

- fork: brandtbucher
- ref: for_iter_dict_items
- machine: linux-x86_64
- commit hash: 66ef77e
- commit date: 2025-02-11
- overall geometric mean: 1.041x faster
- HPT reliability: 99.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                                        |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                      |
| html5lib       | 63.4 ms                                                | 61.5 ms: 1.03x faster                                                       |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                        |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                        |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                        |
| async_tree_memoization     | 437 ms                                                 | 326 ms: 1.34x faster                                                        |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 258 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                        |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                        |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.9 ms: 1.11x faster                                                       |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| nbody          | 87.7 ms                                                | 97.4 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                       |
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                       |
| regex_dna      | 220 ms                                                 | 206 ms: 1.07x faster                                                        |
| regex_compile  | 132 ms                                                 | 125 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.85 sec: 1.14x faster                                                      |
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                        |
| xml_etree_generate   | 86.8 ms                                                | 78.2 ms: 1.11x faster                                                       |
| xml_etree_process    | 60.5 ms                                                | 55.1 ms: 1.10x faster                                                       |
| unpickle_pure_python | 213 us                                                 | 198 us: 1.08x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 95.8 ms: 1.06x faster                                                       |
| pickle_pure_python   | 302 us                                                 | 314 us: 1.04x slower                                                        |
| json_loads           | 27.2 us                                                | 28.6 us: 1.05x slower                                                       |
| json_dumps           | 10.1 ms                                                | 11.9 ms: 1.17x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                       |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 10.7 ms                                                | 9.97 ms: 1.07x faster                                                       |
| genshi_text    | 22.6 ms                                                | 21.9 ms: 1.03x faster                                                       |
| genshi_xml     | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-for_iter_dict_items-3.14.0a4+-66ef77e |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                        |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                        |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                                        |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                        |
| async_tree_memoization     | 437 ms                                                 | 326 ms: 1.34x faster                                                        |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                        |
| deepcopy_memo              | 38.4 us                                                | 30.3 us: 1.27x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 258 ms: 1.24x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                       |
| spectral_norm              | 113 ms                                                 | 94.9 ms: 1.19x faster                                                       |
| scimark_fft                | 367 ms                                                 | 311 ms: 1.18x faster                                                        |
| regex_effbot               | 3.77 ms                                                | 3.20 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.39 ms: 1.15x faster                                                       |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                        |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                       |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                        |
| pylint                     | 312 ms                                                 | 280 ms: 1.12x faster                                                        |
| xml_etree_generate         | 86.8 ms                                                | 78.2 ms: 1.11x faster                                                       |
| float                      | 78.7 ms                                                | 70.9 ms: 1.11x faster                                                       |
| telco                      | 8.40 ms                                                | 7.61 ms: 1.10x faster                                                       |
| xml_etree_process          | 60.5 ms                                                | 55.1 ms: 1.10x faster                                                       |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                                        |
| crypto_pyaes               | 74.7 ms                                                | 69.1 ms: 1.08x faster                                                       |
| richards                   | 47.5 ms                                                | 44.0 ms: 1.08x faster                                                       |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                      |
| unpickle_pure_python       | 213 us                                                 | 198 us: 1.08x faster                                                        |
| richards_super             | 53.7 ms                                                | 50.1 ms: 1.07x faster                                                       |
| mako                       | 10.7 ms                                                | 9.97 ms: 1.07x faster                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.38 sec: 1.07x faster                                                      |
| regex_dna                  | 220 ms                                                 | 206 ms: 1.07x faster                                                        |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                                       |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 101 ms                                                 | 95.8 ms: 1.06x faster                                                       |
| thrift                     | 800 us                                                 | 759 us: 1.05x faster                                                        |
| regex_compile              | 132 ms                                                 | 125 ms: 1.05x faster                                                        |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                        |
| json                       | 5.32 ms                                                | 5.13 ms: 1.04x faster                                                       |
| html5lib                   | 63.4 ms                                                | 61.5 ms: 1.03x faster                                                       |
| generators                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                       |
| genshi_text                | 22.6 ms                                                | 21.9 ms: 1.03x faster                                                       |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                                        |
| logging_simple             | 5.65 us                                                | 5.52 us: 1.02x faster                                                       |
| logging_format             | 6.23 us                                                | 6.10 us: 1.02x faster                                                       |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                        |
| connected_components       | 447 ms                                                 | 439 ms: 1.02x faster                                                        |
| genshi_xml                 | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                       |
| scimark_monte_carlo        | 66.8 ms                                                | 65.6 ms: 1.02x faster                                                       |
| pyflate                    | 470 ms                                                 | 462 ms: 1.02x faster                                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                        |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                      |
| shortest_path              | 487 ms                                                 | 484 ms: 1.01x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                                        |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                        |
| chaos                      | 58.0 ms                                                | 58.6 ms: 1.01x slower                                                       |
| python_startup_no_site     | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                                        |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                       |
| sympy_integrate            | 19.8 ms                                                | 20.2 ms: 1.02x slower                                                       |
| gc_traversal               | 4.90 ms                                                | 4.99 ms: 1.02x slower                                                       |
| dulwich_log                | 64.6 ms                                                | 66.0 ms: 1.02x slower                                                       |
| sympy_str                  | 273 ms                                                 | 281 ms: 1.03x slower                                                        |
| sqlglot_parse              | 1.26 ms                                                | 1.31 ms: 1.03x slower                                                       |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                      |
| pprint_pformat             | 1.48 sec                                               | 1.53 sec: 1.04x slower                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.63 ms: 1.04x slower                                                       |
| sqlglot_optimize           | 53.4 ms                                                | 55.4 ms: 1.04x slower                                                       |
| pickle_pure_python         | 302 us                                                 | 314 us: 1.04x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 157 ms: 1.04x slower                                                        |
| pprint_safe_repr           | 727 ms                                                 | 760 ms: 1.05x slower                                                        |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                       |
| json_loads                 | 27.2 us                                                | 28.6 us: 1.05x slower                                                       |
| sympy_expand               | 456 ms                                                 | 482 ms: 1.06x slower                                                        |
| comprehensions             | 16.5 us                                                | 17.4 us: 1.06x slower                                                       |
| logging_silent             | 101 ns                                                 | 107 ns: 1.06x slower                                                        |
| raytrace                   | 262 ms                                                 | 277 ms: 1.06x slower                                                        |
| deltablue                  | 3.19 ms                                                | 3.43 ms: 1.07x slower                                                       |
| coverage                   | 82.8 ms                                                | 89.1 ms: 1.08x slower                                                       |
| bench_thread_pool          | 818 us                                                 | 888 us: 1.09x slower                                                        |
| many_optionals             | 857 us                                                 | 952 us: 1.11x slower                                                        |
| nbody                      | 87.7 ms                                                | 97.4 ms: 1.11x slower                                                       |
| nqueens                    | 80.9 ms                                                | 90.0 ms: 1.11x slower                                                       |
| hexiom                     | 6.08 ms                                                | 6.93 ms: 1.14x slower                                                       |
| json_dumps                 | 10.1 ms                                                | 11.9 ms: 1.17x slower                                                       |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.34x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (7): k_core, meteor_contest, django_template, asyncio_websockets, fannkuch, sqlalchemy_imperative, mdp
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 99.69% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x