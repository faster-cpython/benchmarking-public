# Results vs. 3.13.0

- fork: eendebakpt
- ref: int_freelist
- machine: linux-x86_64
- commit hash: b034948
- commit date: 2024-12-07
- overall geometric mean: 1.035x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                               |
| docutils       | 2.58 sec                                               | 2.56 sec: 1.01x faster                                             |
| html5lib       | 63.4 ms                                                | 63.0 ms: 1.01x faster                                              |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 329 ms: 1.41x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                               |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                               |
| async_tree_none            | 350 ms                                                 | 270 ms: 1.30x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 337 ms: 1.30x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 264 ms: 1.21x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                               |
| async_generators           | 433 ms                                                 | 416 ms: 1.04x faster                                               |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                               |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                              |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 77.2 ms: 1.02x faster                                              |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                               |
| nbody          | 87.7 ms                                                | 93.5 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.30 ms: 1.14x faster                                              |
| regex_v8       | 26.9 ms                                                | 25.5 ms: 1.05x faster                                              |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                               |
| regex_dna      | 220 ms                                                 | 217 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.06x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 146 ms: 1.06x faster                                               |
| tomli_loads          | 2.12 sec                                               | 2.03 sec: 1.04x faster                                             |
| json_loads           | 27.2 us                                                | 26.4 us: 1.03x faster                                              |
| xml_etree_iterparse  | 101 ms                                                 | 98.4 ms: 1.03x faster                                              |
| xml_etree_process    | 60.5 ms                                                | 59.4 ms: 1.02x faster                                              |
| xml_etree_generate   | 86.8 ms                                                | 85.3 ms: 1.02x faster                                              |
| unpickle_pure_python | 213 us                                                 | 222 us: 1.04x slower                                               |
| pickle_pure_python   | 302 us                                                 | 327 us: 1.08x slower                                               |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                              |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.04 ms: 1.00x slower                                              |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 31.7 ms                                                | 32.1 ms: 1.01x slower                                              |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                              |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                       |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 329 ms: 1.41x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                               |
| async_tree_io              | 838 ms                                                 | 601 ms: 1.40x faster                                               |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                               |
| async_tree_none            | 350 ms                                                 | 270 ms: 1.30x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 337 ms: 1.30x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 31.3 us: 1.22x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 264 ms: 1.21x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.72 us: 1.19x faster                                              |
| go                         | 141 ms                                                 | 119 ms: 1.18x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.30 ms: 1.14x faster                                              |
| pylint                     | 312 ms                                                 | 275 ms: 1.14x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                               |
| json                       | 5.32 ms                                                | 4.78 ms: 1.11x faster                                              |
| create_gc_cycles           | 2.45 ms                                                | 2.22 ms: 1.10x faster                                              |
| gc_traversal               | 4.90 ms                                                | 4.50 ms: 1.09x faster                                              |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.63 ms: 1.09x faster                                              |
| k_core                     | 2.37 sec                                               | 2.19 sec: 1.08x faster                                             |
| telco                      | 8.40 ms                                                | 7.81 ms: 1.07x faster                                              |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.07x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 146 ms: 1.06x faster                                               |
| regex_v8                   | 26.9 ms                                                | 25.5 ms: 1.05x faster                                              |
| spectral_norm              | 113 ms                                                 | 108 ms: 1.05x faster                                               |
| thrift                     | 800 us                                                 | 763 us: 1.05x faster                                               |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                               |
| tomli_loads                | 2.12 sec                                               | 2.03 sec: 1.04x faster                                             |
| async_generators           | 433 ms                                                 | 416 ms: 1.04x faster                                               |
| richards                   | 47.5 ms                                                | 45.7 ms: 1.04x faster                                              |
| pyflate                    | 470 ms                                                 | 452 ms: 1.04x faster                                               |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                             |
| bpe_tokeniser              | 4.69 sec                                               | 4.52 sec: 1.04x faster                                             |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                               |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                               |
| crypto_pyaes               | 74.7 ms                                                | 72.0 ms: 1.04x faster                                              |
| richards_super             | 53.7 ms                                                | 52.0 ms: 1.03x faster                                              |
| scimark_fft                | 367 ms                                                 | 356 ms: 1.03x faster                                               |
| json_loads                 | 27.2 us                                                | 26.4 us: 1.03x faster                                              |
| xml_etree_iterparse        | 101 ms                                                 | 98.4 ms: 1.03x faster                                              |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                             |
| sqlite_synth               | 2.90 us                                                | 2.84 us: 1.02x faster                                              |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                              |
| xml_etree_process          | 60.5 ms                                                | 59.4 ms: 1.02x faster                                              |
| float                      | 78.7 ms                                                | 77.2 ms: 1.02x faster                                              |
| xml_etree_generate         | 86.8 ms                                                | 85.3 ms: 1.02x faster                                              |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                               |
| shortest_path              | 487 ms                                                 | 480 ms: 1.01x faster                                               |
| connected_components       | 447 ms                                                 | 441 ms: 1.01x faster                                               |
| regex_dna                  | 220 ms                                                 | 217 ms: 1.01x faster                                               |
| generators                 | 28.8 ms                                                | 28.4 ms: 1.01x faster                                              |
| sympy_str                  | 273 ms                                                 | 270 ms: 1.01x faster                                               |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                               |
| logging_simple             | 5.65 us                                                | 5.60 us: 1.01x faster                                              |
| docutils                   | 2.58 sec                                               | 2.56 sec: 1.01x faster                                             |
| logging_format             | 6.23 us                                                | 6.19 us: 1.01x faster                                              |
| html5lib                   | 63.4 ms                                                | 63.0 ms: 1.01x faster                                              |
| dulwich_log                | 64.6 ms                                                | 64.3 ms: 1.00x faster                                              |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                               |
| sqlglot_optimize           | 53.4 ms                                                | 53.6 ms: 1.00x slower                                              |
| python_startup_no_site     | 7.00 ms                                                | 7.04 ms: 1.00x slower                                              |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                               |
| sympy_integrate            | 19.8 ms                                                | 20.0 ms: 1.01x slower                                              |
| coverage                   | 82.8 ms                                                | 83.5 ms: 1.01x slower                                              |
| sqlglot_parse              | 1.26 ms                                                | 1.28 ms: 1.01x slower                                              |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                              |
| sympy_expand               | 456 ms                                                 | 461 ms: 1.01x slower                                               |
| pprint_safe_repr           | 727 ms                                                 | 735 ms: 1.01x slower                                               |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                              |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.01x slower                                              |
| deltablue                  | 3.19 ms                                                | 3.24 ms: 1.02x slower                                              |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                               |
| pprint_pformat             | 1.48 sec                                               | 1.51 sec: 1.02x slower                                             |
| scimark_sor                | 122 ms                                                 | 125 ms: 1.02x slower                                               |
| raytrace                   | 262 ms                                                 | 268 ms: 1.03x slower                                               |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                              |
| scimark_monte_carlo        | 66.8 ms                                                | 69.1 ms: 1.04x slower                                              |
| fannkuch                   | 394 ms                                                 | 408 ms: 1.04x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.30 ms: 1.04x slower                                              |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                               |
| unpickle_pure_python       | 213 us                                                 | 222 us: 1.04x slower                                               |
| logging_silent             | 101 ns                                                 | 105 ns: 1.04x slower                                               |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                              |
| chaos                      | 58.0 ms                                                | 61.1 ms: 1.05x slower                                              |
| bench_thread_pool          | 818 us                                                 | 861 us: 1.05x slower                                               |
| mdp                        | 2.54 sec                                               | 2.68 sec: 1.05x slower                                             |
| nbody                      | 87.7 ms                                                | 93.5 ms: 1.07x slower                                              |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                              |
| pickle_pure_python         | 302 us                                                 | 327 us: 1.08x slower                                               |
| many_optionals             | 857 us                                                 | 947 us: 1.11x slower                                               |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                              |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 78.6 ms: 3.28x slower                                              |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                       |

Benchmark hidden because not significant (4): genshi_text, genshi_xml, djangocms, nqueens
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241207-3.14.0a2+-b034948/bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948.json: mypy2

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x