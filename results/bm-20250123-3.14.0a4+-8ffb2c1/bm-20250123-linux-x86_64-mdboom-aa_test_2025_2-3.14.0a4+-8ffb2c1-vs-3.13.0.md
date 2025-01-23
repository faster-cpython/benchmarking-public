# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-x86_64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.040x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.04x faster                                             |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.01x slower                                           |
| html5lib       | 63.4 ms                                                | 62.2 ms: 1.02x faster                                            |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 306 ms: 1.51x faster                                             |
| async_tree_io_tg           | 861 ms                                                 | 585 ms: 1.47x faster                                             |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                             |
| async_tree_none            | 350 ms                                                 | 254 ms: 1.38x faster                                             |
| async_tree_memoization     | 437 ms                                                 | 321 ms: 1.36x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                             |
| async_generators           | 433 ms                                                 | 391 ms: 1.11x faster                                             |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                            |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.9 ms: 1.09x faster                                            |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                             |
| nbody          | 87.7 ms                                                | 96.2 ms: 1.10x slower                                            |
| Geometric mean | (ref)                                                  | 1.00x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.24 ms: 1.16x faster                                            |
| regex_v8       | 26.9 ms                                                | 25.2 ms: 1.07x faster                                            |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                             |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                             |
| tomli_loads          | 2.12 sec                                               | 1.99 sec: 1.07x faster                                           |
| xml_etree_iterparse  | 101 ms                                                 | 97.1 ms: 1.04x faster                                            |
| xml_etree_generate   | 86.8 ms                                                | 84.5 ms: 1.03x faster                                            |
| xml_etree_process    | 60.5 ms                                                | 61.4 ms: 1.02x slower                                            |
| unpickle_pure_python | 213 us                                                 | 226 us: 1.06x slower                                             |
| json_loads           | 27.2 us                                                | 29.2 us: 1.08x slower                                            |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.08x slower                                             |
| json_dumps           | 10.1 ms                                                | 11.9 ms: 1.18x slower                                            |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.11 ms: 1.02x slower                                            |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                            |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.9 ms: 1.03x faster                                            |
| genshi_xml      | 50.5 ms                                                | 49.7 ms: 1.01x faster                                            |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                            |
| mako            | 10.7 ms                                                | 11.1 ms: 1.04x slower                                            |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-linux-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 306 ms: 1.51x faster                                             |
| async_tree_io_tg           | 861 ms                                                 | 585 ms: 1.47x faster                                             |
| async_tree_io              | 838 ms                                                 | 598 ms: 1.40x faster                                             |
| async_tree_none            | 350 ms                                                 | 254 ms: 1.38x faster                                             |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                             |
| async_tree_memoization     | 437 ms                                                 | 321 ms: 1.36x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.29x faster                                             |
| deepcopy_memo              | 38.4 us                                                | 30.8 us: 1.25x faster                                            |
| deepcopy_reduce            | 3.24 us                                                | 2.63 us: 1.23x faster                                            |
| go                         | 141 ms                                                 | 116 ms: 1.21x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                             |
| regex_effbot               | 3.77 ms                                                | 3.24 ms: 1.16x faster                                            |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                             |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                             |
| async_generators           | 433 ms                                                 | 391 ms: 1.11x faster                                             |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                             |
| float                      | 78.7 ms                                                | 71.9 ms: 1.09x faster                                            |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.09x faster                                             |
| richards                   | 47.5 ms                                                | 43.8 ms: 1.08x faster                                            |
| richards_super             | 53.7 ms                                                | 50.1 ms: 1.07x faster                                            |
| regex_v8                   | 26.9 ms                                                | 25.2 ms: 1.07x faster                                            |
| tomli_loads                | 2.12 sec                                               | 1.99 sec: 1.07x faster                                           |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                           |
| telco                      | 8.40 ms                                                | 7.99 ms: 1.05x faster                                            |
| scimark_fft                | 367 ms                                                 | 349 ms: 1.05x faster                                             |
| pathlib                    | 17.4 ms                                                | 16.6 ms: 1.05x faster                                            |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                            |
| pyflate                    | 470 ms                                                 | 450 ms: 1.04x faster                                             |
| xml_etree_iterparse        | 101 ms                                                 | 97.1 ms: 1.04x faster                                            |
| thrift                     | 800 us                                                 | 769 us: 1.04x faster                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.51 sec: 1.04x faster                                           |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                           |
| generators                 | 28.8 ms                                                | 27.7 ms: 1.04x faster                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.85 ms: 1.04x faster                                            |
| 2to3                       | 266 ms                                                 | 257 ms: 1.04x faster                                             |
| genshi_text                | 22.6 ms                                                | 21.9 ms: 1.03x faster                                            |
| sqlglot_normalize          | 108 ms                                                 | 105 ms: 1.03x faster                                             |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                             |
| xml_etree_generate         | 86.8 ms                                                | 84.5 ms: 1.03x faster                                            |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                             |
| shortest_path              | 487 ms                                                 | 476 ms: 1.02x faster                                             |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                             |
| html5lib                   | 63.4 ms                                                | 62.2 ms: 1.02x faster                                            |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                             |
| json                       | 5.32 ms                                                | 5.23 ms: 1.02x faster                                            |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                             |
| crypto_pyaes               | 74.7 ms                                                | 73.4 ms: 1.02x faster                                            |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.02x faster                                             |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                           |
| genshi_xml                 | 50.5 ms                                                | 49.7 ms: 1.01x faster                                            |
| mdp                        | 2.54 sec                                               | 2.51 sec: 1.01x faster                                           |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                             |
| sqlglot_transpile          | 1.57 ms                                                | 1.55 ms: 1.01x faster                                            |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                            |
| deltablue                  | 3.19 ms                                                | 3.16 ms: 1.01x faster                                            |
| sqlglot_parse              | 1.26 ms                                                | 1.25 ms: 1.01x faster                                            |
| nqueens                    | 80.9 ms                                                | 80.2 ms: 1.01x faster                                            |
| sqlglot_optimize           | 53.4 ms                                                | 53.0 ms: 1.01x faster                                            |
| sympy_expand               | 456 ms                                                 | 454 ms: 1.01x faster                                             |
| scimark_sor                | 122 ms                                                 | 122 ms: 1.00x faster                                             |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                             |
| sympy_integrate            | 19.8 ms                                                | 19.8 ms: 1.00x faster                                            |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.01x slower                                           |
| dulwich_log                | 64.6 ms                                                | 65.1 ms: 1.01x slower                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                            |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                             |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                             |
| xml_etree_process          | 60.5 ms                                                | 61.4 ms: 1.02x slower                                            |
| python_startup_no_site     | 7.00 ms                                                | 7.11 ms: 1.02x slower                                            |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                            |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                            |
| logging_silent             | 101 ns                                                 | 103 ns: 1.02x slower                                             |
| logging_simple             | 5.65 us                                                | 5.77 us: 1.02x slower                                            |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                            |
| fannkuch                   | 394 ms                                                 | 404 ms: 1.03x slower                                             |
| gc_traversal               | 4.90 ms                                                | 5.03 ms: 1.03x slower                                            |
| logging_format             | 6.23 us                                                | 6.44 us: 1.03x slower                                            |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                             |
| hexiom                     | 6.08 ms                                                | 6.28 ms: 1.03x slower                                            |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                            |
| unpickle_pure_python       | 213 us                                                 | 226 us: 1.06x slower                                             |
| bench_thread_pool          | 818 us                                                 | 866 us: 1.06x slower                                             |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                            |
| json_loads                 | 27.2 us                                                | 29.2 us: 1.08x slower                                            |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.08x slower                                             |
| coverage                   | 82.8 ms                                                | 90.7 ms: 1.09x slower                                            |
| nbody                      | 87.7 ms                                                | 96.2 ms: 1.10x slower                                            |
| many_optionals             | 857 us                                                 | 952 us: 1.11x slower                                             |
| json_dumps                 | 10.1 ms                                                | 11.9 ms: 1.18x slower                                            |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.33x slower                                            |
| bench_mp_pool              | 24.0 ms                                                | 81.8 ms: 3.41x slower                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                     |

Benchmark hidden because not significant (5): pprint_safe_repr, chaos, asyncio_websockets, pprint_pformat, scimark_monte_carlo
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x