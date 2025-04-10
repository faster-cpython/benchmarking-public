# Results vs. 3.13.0

- fork: iritkatriel
- ref: dicts
- machine: linux-x86_64
- commit hash: bf2d1dd
- commit date: 2025-04-10
- overall geometric mean: 1.068x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 249 ms: 1.07x faster                                         |
| html5lib       | 63.4 ms                                                | 61.3 ms: 1.03x faster                                        |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 308 ms: 1.42x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                         |
| async_tree_none            | 350 ms                                                 | 254 ms: 1.38x faster                                         |
| async_tree_io              | 838 ms                                                 | 609 ms: 1.38x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 474 ms: 1.21x faster                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                         |
| async_generators           | 433 ms                                                 | 394 ms: 1.10x faster                                         |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                        |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.5 ms: 1.18x faster                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| nbody          | 87.7 ms                                                | 92.5 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 22.6 ms: 1.19x faster                                        |
| regex_effbot   | 3.77 ms                                                | 3.38 ms: 1.11x faster                                        |
| regex_compile  | 132 ms                                                 | 123 ms: 1.07x faster                                         |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd |
|---------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads         | 2.12 sec                                               | 1.92 sec: 1.10x faster                                       |
| xml_etree_parse     | 154 ms                                                 | 141 ms: 1.09x faster                                         |
| xml_etree_process   | 60.5 ms                                                | 58.0 ms: 1.04x faster                                        |
| xml_etree_generate  | 86.8 ms                                                | 83.5 ms: 1.04x faster                                        |
| xml_etree_iterparse | 101 ms                                                 | 98.5 ms: 1.03x faster                                        |
| pickle_pure_python  | 302 us                                                 | 311 us: 1.03x slower                                         |
| json_loads          | 27.2 us                                                | 29.8 us: 1.10x slower                                        |
| json_dumps          | 10.1 ms                                                | 11.6 ms: 1.15x slower                                        |
| Geometric mean      | (ref)                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                        |
| python_startup_no_site | 7.00 ms                                                | 8.18 ms: 1.17x slower                                        |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                        |
| genshi_xml      | 50.5 ms                                                | 49.1 ms: 1.03x faster                                        |
| django_template | 31.7 ms                                                | 31.2 ms: 1.02x faster                                        |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                        |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.21 sec: 2.11x faster                                       |
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                         |
| deepcopy                   | 354 us                                                 | 246 us: 1.44x faster                                         |
| async_tree_memoization     | 437 ms                                                 | 308 ms: 1.42x faster                                         |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                         |
| async_tree_none            | 350 ms                                                 | 254 ms: 1.38x faster                                         |
| async_tree_io              | 838 ms                                                 | 609 ms: 1.38x faster                                         |
| deepcopy_memo              | 38.4 us                                                | 28.6 us: 1.34x faster                                        |
| go                         | 141 ms                                                 | 106 ms: 1.33x faster                                         |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.61 us: 1.24x faster                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 474 ms: 1.21x faster                                         |
| regex_v8                   | 26.9 ms                                                | 22.6 ms: 1.19x faster                                        |
| float                      | 78.7 ms                                                | 66.5 ms: 1.18x faster                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                         |
| spectral_norm              | 113 ms                                                 | 98.8 ms: 1.15x faster                                        |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                         |
| richards                   | 47.5 ms                                                | 42.2 ms: 1.13x faster                                        |
| regex_effbot               | 3.77 ms                                                | 3.38 ms: 1.11x faster                                        |
| logging_silent             | 101 ns                                                 | 90.8 ns: 1.11x faster                                        |
| richards_super             | 53.7 ms                                                | 48.4 ms: 1.11x faster                                        |
| tomli_loads                | 2.12 sec                                               | 1.92 sec: 1.10x faster                                       |
| async_generators           | 433 ms                                                 | 394 ms: 1.10x faster                                         |
| dulwich_log                | 64.6 ms                                                | 58.8 ms: 1.10x faster                                        |
| pyflate                    | 470 ms                                                 | 430 ms: 1.09x faster                                         |
| telco                      | 8.40 ms                                                | 7.69 ms: 1.09x faster                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.61 ms: 1.09x faster                                        |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                         |
| scimark_fft                | 367 ms                                                 | 338 ms: 1.08x faster                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.37 sec: 1.07x faster                                       |
| regex_compile              | 132 ms                                                 | 123 ms: 1.07x faster                                         |
| scimark_sor                | 122 ms                                                 | 114 ms: 1.07x faster                                         |
| 2to3                       | 266 ms                                                 | 249 ms: 1.07x faster                                         |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                        |
| chaos                      | 58.0 ms                                                | 54.9 ms: 1.06x faster                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 63.3 ms: 1.05x faster                                        |
| sympy_integrate            | 19.8 ms                                                | 18.8 ms: 1.05x faster                                        |
| k_core                     | 2.37 sec                                               | 2.26 sec: 1.05x faster                                       |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                        |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                       |
| xml_etree_process          | 60.5 ms                                                | 58.0 ms: 1.04x faster                                        |
| crypto_pyaes               | 74.7 ms                                                | 71.6 ms: 1.04x faster                                        |
| xml_etree_generate         | 86.8 ms                                                | 83.5 ms: 1.04x faster                                        |
| sympy_str                  | 273 ms                                                 | 263 ms: 1.04x faster                                         |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.04x faster                                         |
| html5lib                   | 63.4 ms                                                | 61.3 ms: 1.03x faster                                        |
| logging_simple             | 5.65 us                                                | 5.47 us: 1.03x faster                                        |
| logging_format             | 6.23 us                                                | 6.03 us: 1.03x faster                                        |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                        |
| genshi_xml                 | 50.5 ms                                                | 49.1 ms: 1.03x faster                                        |
| xml_etree_iterparse        | 101 ms                                                 | 98.5 ms: 1.03x faster                                        |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                         |
| raytrace                   | 262 ms                                                 | 255 ms: 1.02x faster                                         |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                         |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                       |
| pprint_safe_repr           | 727 ms                                                 | 714 ms: 1.02x faster                                         |
| nqueens                    | 80.9 ms                                                | 79.5 ms: 1.02x faster                                        |
| sympy_expand               | 456 ms                                                 | 448 ms: 1.02x faster                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                         |
| django_template            | 31.7 ms                                                | 31.2 ms: 1.02x faster                                        |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                       |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                        |
| hexiom                     | 6.08 ms                                                | 6.03 ms: 1.01x faster                                        |
| comprehensions             | 16.5 us                                                | 16.4 us: 1.01x faster                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                        |
| scimark_lu                 | 114 ms                                                 | 115 ms: 1.01x slower                                         |
| shortest_path              | 487 ms                                                 | 491 ms: 1.01x slower                                         |
| gc_traversal               | 4.90 ms                                                | 4.96 ms: 1.01x slower                                        |
| deltablue                  | 3.19 ms                                                | 3.26 ms: 1.02x slower                                        |
| coverage                   | 82.8 ms                                                | 84.7 ms: 1.02x slower                                        |
| fannkuch                   | 394 ms                                                 | 403 ms: 1.02x slower                                         |
| pickle_pure_python         | 302 us                                                 | 311 us: 1.03x slower                                         |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                        |
| json                       | 5.32 ms                                                | 5.52 ms: 1.04x slower                                        |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                        |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                        |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                         |
| generators                 | 28.8 ms                                                | 30.3 ms: 1.05x slower                                        |
| nbody                      | 87.7 ms                                                | 92.5 ms: 1.06x slower                                        |
| bench_thread_pool          | 818 us                                                 | 874 us: 1.07x slower                                         |
| many_optionals             | 857 us                                                 | 926 us: 1.08x slower                                         |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                        |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                        |
| python_startup_no_site     | 7.00 ms                                                | 8.18 ms: 1.17x slower                                        |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 82.2 ms: 3.43x slower                                        |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                 |

Benchmark hidden because not significant (4): asyncio_websockets, unpickle_pure_python, connected_components, docutils
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250410-3.14.0a6+-bf2d1dd/bm-20250410-linux-x86_64-iritkatriel-dicts-3.14.0a6+-bf2d1dd.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.068x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x