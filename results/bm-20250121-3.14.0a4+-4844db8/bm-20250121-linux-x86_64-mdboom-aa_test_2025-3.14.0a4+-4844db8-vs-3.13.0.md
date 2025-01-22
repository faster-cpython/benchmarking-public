# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025
- machine: linux-x86_64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.045x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                           |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.00x slower                                         |
| html5lib       | 63.4 ms                                                | 61.2 ms: 1.04x faster                                          |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                           |
| async_tree_io_tg           | 861 ms                                                 | 585 ms: 1.47x faster                                           |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                           |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                           |
| async_tree_memoization     | 437 ms                                                 | 323 ms: 1.35x faster                                           |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 482 ms: 1.19x faster                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 465 ms: 1.17x faster                                           |
| async_generators           | 433 ms                                                 | 389 ms: 1.11x faster                                           |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.04x slower                                          |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.1 ms: 1.12x faster                                          |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                           |
| nbody          | 87.7 ms                                                | 94.0 ms: 1.07x slower                                          |
| Geometric mean | (ref)                                                  | 1.01x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.31 ms: 1.14x faster                                          |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                           |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                           |
| regex_v8       | 26.9 ms                                                | 26.3 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                  | 1.06x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                           |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.07x faster                                         |
| xml_etree_iterparse  | 101 ms                                                 | 97.8 ms: 1.04x faster                                          |
| xml_etree_generate   | 86.8 ms                                                | 84.6 ms: 1.03x faster                                          |
| xml_etree_process    | 60.5 ms                                                | 61.4 ms: 1.01x slower                                          |
| unpickle_pure_python | 213 us                                                 | 226 us: 1.06x slower                                           |
| json_loads           | 27.2 us                                                | 28.9 us: 1.07x slower                                          |
| pickle_pure_python   | 302 us                                                 | 328 us: 1.08x slower                                           |
| json_dumps           | 10.1 ms                                                | 12.0 ms: 1.19x slower                                          |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.02 ms: 1.00x slower                                          |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                          |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.8 ms: 1.04x faster                                          |
| genshi_xml      | 50.5 ms                                                | 50.0 ms: 1.01x faster                                          |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                          |
| mako            | 10.7 ms                                                | 11.2 ms: 1.05x slower                                          |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                           |
| async_tree_io_tg           | 861 ms                                                 | 585 ms: 1.47x faster                                           |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                           |
| deepcopy                   | 354 us                                                 | 258 us: 1.38x faster                                           |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                           |
| async_tree_memoization     | 437 ms                                                 | 323 ms: 1.35x faster                                           |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                           |
| deepcopy_memo              | 38.4 us                                                | 30.8 us: 1.24x faster                                          |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.21x faster                                          |
| go                         | 141 ms                                                 | 116 ms: 1.21x faster                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 482 ms: 1.19x faster                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 465 ms: 1.17x faster                                           |
| spectral_norm              | 113 ms                                                 | 97.9 ms: 1.16x faster                                          |
| regex_effbot               | 3.77 ms                                                | 3.31 ms: 1.14x faster                                          |
| pylint                     | 312 ms                                                 | 274 ms: 1.14x faster                                           |
| float                      | 78.7 ms                                                | 70.1 ms: 1.12x faster                                          |
| async_generators           | 433 ms                                                 | 389 ms: 1.11x faster                                           |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.54 ms: 1.11x faster                                          |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                           |
| pathlib                    | 17.4 ms                                                | 15.8 ms: 1.10x faster                                          |
| richards                   | 47.5 ms                                                | 43.3 ms: 1.10x faster                                          |
| scimark_fft                | 367 ms                                                 | 337 ms: 1.09x faster                                           |
| richards_super             | 53.7 ms                                                | 49.7 ms: 1.08x faster                                          |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.07x faster                                         |
| gc_traversal               | 4.90 ms                                                | 4.62 ms: 1.06x faster                                          |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                           |
| telco                      | 8.40 ms                                                | 8.02 ms: 1.05x faster                                          |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.49 sec: 1.04x faster                                         |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                           |
| crypto_pyaes               | 74.7 ms                                                | 71.8 ms: 1.04x faster                                          |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                         |
| html5lib                   | 63.4 ms                                                | 61.2 ms: 1.04x faster                                          |
| genshi_text                | 22.6 ms                                                | 21.8 ms: 1.04x faster                                          |
| xml_etree_iterparse        | 101 ms                                                 | 97.8 ms: 1.04x faster                                          |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                           |
| sqlglot_normalize          | 108 ms                                                 | 105 ms: 1.03x faster                                           |
| generators                 | 28.8 ms                                                | 28.0 ms: 1.03x faster                                          |
| mdp                        | 2.54 sec                                               | 2.47 sec: 1.03x faster                                         |
| xml_etree_generate         | 86.8 ms                                                | 84.6 ms: 1.03x faster                                          |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.03x faster                                           |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.03x faster                                           |
| connected_components       | 447 ms                                                 | 436 ms: 1.02x faster                                           |
| regex_v8                   | 26.9 ms                                                | 26.3 ms: 1.02x faster                                          |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                           |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                           |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                           |
| shortest_path              | 487 ms                                                 | 477 ms: 1.02x faster                                           |
| deltablue                  | 3.19 ms                                                | 3.14 ms: 1.02x faster                                          |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                         |
| pyflate                    | 470 ms                                                 | 462 ms: 1.02x faster                                           |
| thrift                     | 800 us                                                 | 787 us: 1.02x faster                                           |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                          |
| json                       | 5.32 ms                                                | 5.25 ms: 1.01x faster                                          |
| nqueens                    | 80.9 ms                                                | 79.9 ms: 1.01x faster                                          |
| pycparser                  | 1.20 sec                                               | 1.19 sec: 1.01x faster                                         |
| genshi_xml                 | 50.5 ms                                                | 50.0 ms: 1.01x faster                                          |
| scimark_monte_carlo        | 66.8 ms                                                | 66.3 ms: 1.01x faster                                          |
| sqlglot_transpile          | 1.57 ms                                                | 1.56 ms: 1.01x faster                                          |
| sympy_integrate            | 19.8 ms                                                | 19.7 ms: 1.01x faster                                          |
| sqlglot_parse              | 1.26 ms                                                | 1.26 ms: 1.01x faster                                          |
| sqlglot_optimize           | 53.4 ms                                                | 53.1 ms: 1.01x faster                                          |
| create_gc_cycles           | 2.45 ms                                                | 2.44 ms: 1.00x faster                                          |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                           |
| python_startup_no_site     | 7.00 ms                                                | 7.02 ms: 1.00x slower                                          |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.00x slower                                         |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                         |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                          |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                          |
| logging_simple             | 5.65 us                                                | 5.73 us: 1.01x slower                                          |
| xml_etree_process          | 60.5 ms                                                | 61.4 ms: 1.01x slower                                          |
| logging_silent             | 101 ns                                                 | 103 ns: 1.01x slower                                           |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                          |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                           |
| fannkuch                   | 394 ms                                                 | 404 ms: 1.03x slower                                           |
| typing_runtime_protocols   | 160 us                                                 | 165 us: 1.03x slower                                           |
| hexiom                     | 6.08 ms                                                | 6.29 ms: 1.04x slower                                          |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                           |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.04x slower                                          |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                          |
| bench_thread_pool          | 818 us                                                 | 862 us: 1.05x slower                                           |
| unpickle_pure_python       | 213 us                                                 | 226 us: 1.06x slower                                           |
| json_loads                 | 27.2 us                                                | 28.9 us: 1.07x slower                                          |
| nbody                      | 87.7 ms                                                | 94.0 ms: 1.07x slower                                          |
| pickle_pure_python         | 302 us                                                 | 328 us: 1.08x slower                                           |
| coverage                   | 82.8 ms                                                | 90.1 ms: 1.09x slower                                          |
| many_optionals             | 857 us                                                 | 949 us: 1.11x slower                                           |
| json_dumps                 | 10.1 ms                                                | 12.0 ms: 1.19x slower                                          |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                          |
| bench_mp_pool              | 24.0 ms                                                | 81.0 ms: 3.38x slower                                          |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                   |

Benchmark hidden because not significant (6): sympy_expand, logging_format, dulwich_log, pprint_safe_repr, asyncio_websockets, chaos
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x