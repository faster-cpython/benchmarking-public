# Results vs. 3.13.0

- fork: python
- ref: 4f18916c5c28321f363e
- machine: linux-aarch64
- commit hash: 4f18916
- commit date: 2025-04-26
- overall geometric mean: 1.083x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 288 ms: 1.08x faster                                                     |
| docutils       | 2.96 sec                                                 | 2.89 sec: 1.03x faster                                                   |
| html5lib       | 65.6 ms                                                  | 58.2 ms: 1.13x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.10 sec: 1.09x faster                                                   |
| Geometric mean | (ref)                                                    | 1.08x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 441 ms: 1.51x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 443 ms: 1.50x faster                                                     |
| async_tree_none            | 504 ms                                                   | 365 ms: 1.38x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 353 ms: 1.37x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 853 ms: 1.37x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 865 ms: 1.32x faster                                                     |
| async_generators           | 500 ms                                                   | 416 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 697 ms: 1.15x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 713 ms: 1.11x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.26x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 83.8 ms: 1.14x faster                                                    |
| nbody          | 118 ms                                                   | 126 ms: 1.06x slower                                                     |
| pidigits       | 238 ms                                                   | 290 ms: 1.22x slower                                                     |
| Geometric mean | (ref)                                                    | 1.04x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.02 ms: 1.27x faster                                                    |
| regex_compile  | 134 ms                                                   | 118 ms: 1.13x faster                                                     |
| regex_dna      | 263 ms                                                   | 234 ms: 1.12x faster                                                     |
| regex_v8       | 32.5 ms                                                  | 29.4 ms: 1.11x faster                                                    |
| Geometric mean | (ref)                                                    | 1.16x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate   | 118 ms                                                   | 104 ms: 1.13x faster                                                     |
| tomli_loads          | 2.67 sec                                                 | 2.36 sec: 1.13x faster                                                   |
| xml_etree_process    | 82.1 ms                                                  | 75.1 ms: 1.09x faster                                                    |
| unpickle_pure_python | 265 us                                                   | 246 us: 1.08x faster                                                     |
| xml_etree_iterparse  | 159 ms                                                   | 150 ms: 1.06x faster                                                     |
| Geometric mean       | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (4): json_dumps, pickle_pure_python, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.09x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 25.8 ms: 1.11x faster                                                    |
| genshi_xml      | 61.6 ms                                                  | 58.0 ms: 1.06x faster                                                    |
| django_template | 39.4 ms                                                  | 38.1 ms: 1.04x faster                                                    |
| Geometric mean  | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.59 sec: 2.17x faster                                                   |
| deepcopy                   | 479 us                                                   | 306 us: 1.57x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 34.8 us: 1.52x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 441 ms: 1.51x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 443 ms: 1.50x faster                                                     |
| async_tree_none            | 504 ms                                                   | 365 ms: 1.38x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 353 ms: 1.37x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 853 ms: 1.37x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 865 ms: 1.32x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.32 us: 1.28x faster                                                    |
| go                         | 164 ms                                                   | 129 ms: 1.27x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.02 ms: 1.27x faster                                                    |
| spectral_norm              | 143 ms                                                   | 118 ms: 1.21x faster                                                     |
| async_generators           | 500 ms                                                   | 416 ms: 1.20x faster                                                     |
| telco                      | 10.5 ms                                                  | 8.83 ms: 1.18x faster                                                    |
| logging_silent             | 135 ns                                                   | 116 ns: 1.16x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.19 sec: 1.16x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 21.1 ms: 1.15x faster                                                    |
| scimark_fft                | 463 ms                                                   | 401 ms: 1.15x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 697 ms: 1.15x faster                                                     |
| float                      | 95.8 ms                                                  | 83.8 ms: 1.14x faster                                                    |
| scimark_sor                | 164 ms                                                   | 144 ms: 1.14x faster                                                     |
| xml_etree_generate         | 118 ms                                                   | 104 ms: 1.13x faster                                                     |
| regex_compile              | 134 ms                                                   | 118 ms: 1.13x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.36 sec: 1.13x faster                                                   |
| pylint                     | 345 ms                                                   | 307 ms: 1.13x faster                                                     |
| generators                 | 40.3 ms                                                  | 35.8 ms: 1.13x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 58.2 ms: 1.13x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 78.1 ms: 1.12x faster                                                    |
| regex_dna                  | 263 ms                                                   | 234 ms: 1.12x faster                                                     |
| genshi_text                | 28.6 ms                                                  | 25.8 ms: 1.11x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.21 sec: 1.11x faster                                                   |
| richards                   | 54.5 ms                                                  | 49.3 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 713 ms: 1.11x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 29.4 ms: 1.11x faster                                                    |
| sympy_sum                  | 151 ms                                                   | 137 ms: 1.11x faster                                                     |
| sympy_integrate            | 21.4 ms                                                  | 19.4 ms: 1.10x faster                                                    |
| pyflate                    | 582 ms                                                   | 528 ms: 1.10x faster                                                     |
| xml_etree_process          | 82.1 ms                                                  | 75.1 ms: 1.09x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.10 sec: 1.09x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.75 sec: 1.09x faster                                                   |
| 2to3                       | 313 ms                                                   | 288 ms: 1.08x faster                                                     |
| logging_format             | 8.10 us                                                  | 7.47 us: 1.08x faster                                                    |
| coverage                   | 106 ms                                                   | 97.5 ms: 1.08x faster                                                    |
| pprint_safe_repr           | 962 ms                                                   | 890 ms: 1.08x faster                                                     |
| unpickle_pure_python       | 265 us                                                   | 246 us: 1.08x faster                                                     |
| pprint_pformat             | 1.99 sec                                                 | 1.85 sec: 1.07x faster                                                   |
| chaos                      | 70.7 ms                                                  | 65.9 ms: 1.07x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.82 us: 1.07x faster                                                    |
| deltablue                  | 3.97 ms                                                  | 3.72 ms: 1.06x faster                                                    |
| richards_super             | 60.8 ms                                                  | 57.1 ms: 1.06x faster                                                    |
| genshi_xml                 | 61.6 ms                                                  | 58.0 ms: 1.06x faster                                                    |
| logging_simple             | 7.25 us                                                  | 6.85 us: 1.06x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 150 ms: 1.06x faster                                                     |
| typing_runtime_protocols   | 197 us                                                   | 187 us: 1.05x faster                                                     |
| sympy_expand               | 472 ms                                                   | 450 ms: 1.05x faster                                                     |
| hexiom                     | 7.34 ms                                                  | 7.00 ms: 1.05x faster                                                    |
| django_template            | 39.4 ms                                                  | 38.1 ms: 1.04x faster                                                    |
| sympy_str                  | 265 ms                                                   | 256 ms: 1.03x faster                                                     |
| docutils                   | 2.96 sec                                                 | 2.89 sec: 1.03x faster                                                   |
| shortest_path              | 565 ms                                                   | 579 ms: 1.02x slower                                                     |
| connected_components       | 547 ms                                                   | 560 ms: 1.02x slower                                                     |
| nbody                      | 118 ms                                                   | 126 ms: 1.06x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.67 ms: 1.13x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.84 ms: 1.13x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| pidigits                   | 238 ms                                                   | 290 ms: 1.22x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 25.5 ms: 1.25x slower                                                    |
| many_optionals             | 626 us                                                   | 810 us: 1.29x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 3.29 sec: 408.14x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (20): coroutines, comprehensions, nqueens, sqlalchemy_declarative, scimark_lu, json_dumps, scimark_sparse_mat_mult, sqlalchemy_imperative, asyncio_websockets, mako, bench_thread_pool, pickle_pure_python, json, crypto_pyaes, xml_etree_parse, meteor_contest, python_startup, raytrace, json_loads, fannkuch
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (13) of results/bm-20250426-3.14.0a7+-4f18916-CLANG/bm-20250426-arminc-aarch64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.083x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.07x