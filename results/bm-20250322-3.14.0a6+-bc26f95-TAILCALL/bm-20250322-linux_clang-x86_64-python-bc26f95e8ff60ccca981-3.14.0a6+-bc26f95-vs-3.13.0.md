# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.068x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 251 ms: 1.06x faster                                                   |
| docutils       | 2.58 sec                                               | 2.56 sec: 1.01x faster                                                 |
| html5lib       | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                  |
| sphinx         | 1.03 sec                                               | 982 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 303 ms: 1.53x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 305 ms: 1.43x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 605 ms: 1.42x faster                                                   |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                                   |
| async_tree_none            | 350 ms                                                 | 252 ms: 1.39x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 243 ms: 1.31x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                   |
| async_generators           | 433 ms                                                 | 385 ms: 1.12x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                           |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.8 ms: 1.13x faster                                                  |
| nbody          | 87.7 ms                                                | 90.8 ms: 1.04x slower                                                  |
| pidigits       | 186 ms                                                 | 202 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.04 ms: 1.24x faster                                                  |
| regex_dna      | 220 ms                                                 | 186 ms: 1.18x faster                                                   |
| regex_v8       | 26.9 ms                                                | 22.8 ms: 1.18x faster                                                  |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.92 sec: 1.10x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 58.3 ms: 1.04x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 86.0 ms: 1.01x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                   |
| xml_etree_parse      | 154 ms                                                 | 159 ms: 1.03x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 312 us: 1.03x slower                                                   |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                                  |
| json_dumps           | 10.1 ms                                                | 12.2 ms: 1.21x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 8.11 ms: 1.16x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.6 ms: 1.10x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 47.8 ms: 1.06x faster                                                  |
| django_template | 31.7 ms                                                | 30.8 ms: 1.03x faster                                                  |
| mako            | 10.7 ms                                                | 11.9 ms: 1.12x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 303 ms: 1.53x faster                                                   |
| deepcopy                   | 354 us                                                 | 244 us: 1.45x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 305 ms: 1.43x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 605 ms: 1.42x faster                                                   |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                                   |
| async_tree_none            | 350 ms                                                 | 252 ms: 1.39x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 28.9 us: 1.33x faster                                                  |
| spectral_norm              | 113 ms                                                 | 85.8 ms: 1.32x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 243 ms: 1.31x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 3.95 ms: 1.27x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.58 us: 1.26x faster                                                  |
| go                         | 141 ms                                                 | 113 ms: 1.24x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.04 ms: 1.24x faster                                                  |
| scimark_fft                | 367 ms                                                 | 300 ms: 1.22x faster                                                   |
| regex_dna                  | 220 ms                                                 | 186 ms: 1.18x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 22.8 ms: 1.18x faster                                                  |
| pathlib                    | 17.4 ms                                                | 15.0 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                   |
| pylint                     | 312 ms                                                 | 272 ms: 1.15x faster                                                   |
| richards                   | 47.5 ms                                                | 41.7 ms: 1.14x faster                                                  |
| scimark_sor                | 122 ms                                                 | 108 ms: 1.13x faster                                                   |
| pyflate                    | 470 ms                                                 | 415 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                   |
| richards_super             | 53.7 ms                                                | 47.7 ms: 1.13x faster                                                  |
| float                      | 78.7 ms                                                | 69.8 ms: 1.13x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 57.4 ms: 1.13x faster                                                  |
| async_generators           | 433 ms                                                 | 385 ms: 1.12x faster                                                   |
| telco                      | 8.40 ms                                                | 7.47 ms: 1.12x faster                                                  |
| logging_silent             | 101 ns                                                 | 90.4 ns: 1.12x faster                                                  |
| scimark_lu                 | 114 ms                                                 | 104 ms: 1.10x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.92 sec: 1.10x faster                                                 |
| genshi_text                | 22.6 ms                                                | 20.6 ms: 1.10x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.67 us: 1.09x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 61.6 ms: 1.08x faster                                                  |
| thrift                     | 800 us                                                 | 751 us: 1.06x faster                                                   |
| 2to3                       | 266 ms                                                 | 251 ms: 1.06x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 47.8 ms: 1.06x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.1 ms: 1.05x faster                                                  |
| sphinx                     | 1.03 sec                                               | 982 ms: 1.05x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                 |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                   |
| deltablue                  | 3.19 ms                                                | 3.04 ms: 1.05x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 18.9 ms: 1.05x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.48 sec: 1.05x faster                                                 |
| sympy_str                  | 273 ms                                                 | 262 ms: 1.04x faster                                                   |
| typing_runtime_protocols   | 160 us                                                 | 154 us: 1.04x faster                                                   |
| chaos                      | 58.0 ms                                                | 55.7 ms: 1.04x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 145 ms: 1.04x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 58.3 ms: 1.04x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.48 us: 1.03x faster                                                  |
| logging_format             | 6.23 us                                                | 6.04 us: 1.03x faster                                                  |
| django_template            | 31.7 ms                                                | 30.8 ms: 1.03x faster                                                  |
| html5lib                   | 63.4 ms                                                | 61.7 ms: 1.03x faster                                                  |
| sympy_expand               | 456 ms                                                 | 445 ms: 1.03x faster                                                   |
| coverage                   | 82.8 ms                                                | 80.8 ms: 1.02x faster                                                  |
| nqueens                    | 80.9 ms                                                | 79.4 ms: 1.02x faster                                                  |
| hexiom                     | 6.08 ms                                                | 6.00 ms: 1.01x faster                                                  |
| raytrace                   | 262 ms                                                 | 258 ms: 1.01x faster                                                   |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                                  |
| json                       | 5.32 ms                                                | 5.26 ms: 1.01x faster                                                  |
| docutils                   | 2.58 sec                                               | 2.56 sec: 1.01x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 86.0 ms: 1.01x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.86 ms: 1.01x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 74.3 ms: 1.01x faster                                                  |
| generators                 | 28.8 ms                                                | 28.6 ms: 1.01x faster                                                  |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.02x slower                                                   |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 839 us: 1.03x slower                                                   |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                   |
| shortest_path              | 487 ms                                                 | 500 ms: 1.03x slower                                                   |
| xml_etree_parse            | 154 ms                                                 | 159 ms: 1.03x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 312 us: 1.03x slower                                                   |
| nbody                      | 87.7 ms                                                | 90.8 ms: 1.04x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 755 ms: 1.04x slower                                                   |
| fannkuch                   | 394 ms                                                 | 410 ms: 1.04x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.55 ms: 1.04x slower                                                  |
| connected_components       | 447 ms                                                 | 466 ms: 1.04x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.54 sec: 1.04x slower                                                 |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                                  |
| many_optionals             | 857 us                                                 | 924 us: 1.08x slower                                                   |
| pidigits                   | 186 ms                                                 | 202 ms: 1.08x slower                                                   |
| mako                       | 10.7 ms                                                | 11.9 ms: 1.12x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.92 sec: 1.15x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 8.11 ms: 1.16x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 12.2 ms: 1.21x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.4 ms: 1.32x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (4): k_core, coroutines, xml_etree_iterparse, asyncio_websockets
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.068x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x