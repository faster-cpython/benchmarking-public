# Results vs. 3.13.0

- fork: eendebakpt
- ref: binaryops_shift
- machine: linux-x86_64
- commit hash: 1895d69
- commit date: 2025-01-31
- overall geometric mean: 1.048x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 253 ms: 1.05x faster                                                  |
| html5lib       | 63.4 ms                                                | 60.2 ms: 1.05x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 609 ms: 1.41x faster                                                  |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 323 ms: 1.35x faster                                                  |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                  |
| async_generators           | 433 ms                                                 | 384 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                                  |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.03x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.1 ms: 1.11x faster                                                 |
| nbody          | 87.7 ms                                                | 94.4 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.34 ms: 1.13x faster                                                 |
| regex_v8       | 26.9 ms                                                | 25.4 ms: 1.06x faster                                                 |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                                  |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.07x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 97.4 ms: 1.04x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 58.4 ms: 1.04x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 83.9 ms: 1.03x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.06x slower                                                  |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                                 |
| json_dumps           | 10.1 ms                                                | 12.0 ms: 1.18x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                 |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                 |
| genshi_xml     | 50.5 ms                                                | 48.0 ms: 1.05x faster                                                 |
| mako           | 10.7 ms                                                | 11.5 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 609 ms: 1.41x faster                                                  |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                                  |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 323 ms: 1.35x faster                                                  |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 30.4 us: 1.26x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.21x faster                                                 |
| spectral_norm              | 113 ms                                                 | 94.0 ms: 1.21x faster                                                 |
| go                         | 141 ms                                                 | 118 ms: 1.19x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 495 ms: 1.16x faster                                                  |
| pylint                     | 312 ms                                                 | 272 ms: 1.14x faster                                                  |
| async_generators           | 433 ms                                                 | 384 ms: 1.13x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.34 ms: 1.13x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 489 ms: 1.11x faster                                                  |
| pyflate                    | 470 ms                                                 | 424 ms: 1.11x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                  |
| float                      | 78.7 ms                                                | 71.1 ms: 1.11x faster                                                 |
| pathlib                    | 17.4 ms                                                | 15.7 ms: 1.10x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.61 ms: 1.09x faster                                                 |
| scimark_fft                | 367 ms                                                 | 339 ms: 1.08x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.07x faster                                                |
| richards                   | 47.5 ms                                                | 44.4 ms: 1.07x faster                                                 |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                 |
| telco                      | 8.40 ms                                                | 7.91 ms: 1.06x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                                |
| regex_v8                   | 26.9 ms                                                | 25.4 ms: 1.06x faster                                                 |
| crypto_pyaes               | 74.7 ms                                                | 70.7 ms: 1.06x faster                                                 |
| thrift                     | 800 us                                                 | 759 us: 1.05x faster                                                  |
| html5lib                   | 63.4 ms                                                | 60.2 ms: 1.05x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 48.0 ms: 1.05x faster                                                 |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                                  |
| 2to3                       | 266 ms                                                 | 253 ms: 1.05x faster                                                  |
| richards_super             | 53.7 ms                                                | 51.2 ms: 1.05x faster                                                 |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                  |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 97.4 ms: 1.04x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 58.4 ms: 1.04x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 83.9 ms: 1.03x faster                                                 |
| logging_format             | 6.23 us                                                | 6.03 us: 1.03x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                |
| logging_simple             | 5.65 us                                                | 5.48 us: 1.03x faster                                                 |
| sqlglot_optimize           | 53.4 ms                                                | 51.8 ms: 1.03x faster                                                 |
| connected_components       | 447 ms                                                 | 434 ms: 1.03x faster                                                  |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.03x faster                                                |
| gc_traversal               | 4.90 ms                                                | 4.77 ms: 1.03x faster                                                 |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.03x faster                                                  |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.03x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.5 ms: 1.03x faster                                                 |
| shortest_path              | 487 ms                                                 | 475 ms: 1.02x faster                                                  |
| generators                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                                 |
| json                       | 5.32 ms                                                | 5.23 ms: 1.02x faster                                                 |
| typing_runtime_protocols   | 160 us                                                 | 157 us: 1.02x faster                                                  |
| sympy_expand               | 456 ms                                                 | 450 ms: 1.01x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 64.1 ms: 1.01x faster                                                 |
| nqueens                    | 80.9 ms                                                | 80.3 ms: 1.01x faster                                                 |
| sympy_integrate            | 19.8 ms                                                | 19.7 ms: 1.01x faster                                                 |
| comprehensions             | 16.5 us                                                | 16.4 us: 1.00x faster                                                 |
| chaos                      | 58.0 ms                                                | 58.5 ms: 1.01x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 67.4 ms: 1.01x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 734 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.51 sec: 1.02x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.26 ms: 1.03x slower                                                 |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.03x slower                                                 |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                                  |
| fannkuch                   | 394 ms                                                 | 412 ms: 1.05x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 860 us: 1.05x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.06x slower                                                  |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                                 |
| nbody                      | 87.7 ms                                                | 94.4 ms: 1.08x slower                                                 |
| mako                       | 10.7 ms                                                | 11.5 ms: 1.08x slower                                                 |
| coverage                   | 82.8 ms                                                | 89.8 ms: 1.08x slower                                                 |
| logging_silent             | 101 ns                                                 | 110 ns: 1.09x slower                                                  |
| many_optionals             | 857 us                                                 | 933 us: 1.09x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 12.0 ms: 1.18x slower                                                 |
| subparsers                 | 15.5 ms                                                | 20.3 ms: 1.31x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 81.3 ms: 3.39x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (9): deltablue, scimark_sor, sqlglot_transpile, pidigits, docutils, sqlglot_parse, django_template, asyncio_websockets, create_gc_cycles
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x