# Results vs. 3.13.0

- fork: kumaraditya303
- ref: disable__asyncio
- machine: linux-x86_64
- commit hash: a0a0f85
- commit date: 2024-12-15
- overall geometric mean: 1.015x slower
- HPT reliability: 69.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                       |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                      |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators           | 433 ms                                                 | 423 ms: 1.03x faster                                                       |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                      |
| async_tree_io_tg           | 861 ms                                                 | 1.00 sec: 1.16x slower                                                     |
| async_tree_io              | 838 ms                                                 | 1.03 sec: 1.23x slower                                                     |
| async_tree_memoization_tg  | 463 ms                                                 | 580 ms: 1.25x slower                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 746 ms: 1.37x slower                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 796 ms: 1.39x slower                                                       |
| async_tree_memoization     | 437 ms                                                 | 632 ms: 1.45x slower                                                       |
| async_tree_none            | 350 ms                                                 | 522 ms: 1.49x slower                                                       |
| async_tree_none_tg         | 319 ms                                                 | 489 ms: 1.53x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.25x slower                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 77.0 ms: 1.02x faster                                                      |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                       |
| nbody          | 87.7 ms                                                | 91.8 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.36 ms: 1.12x faster                                                      |
| regex_v8       | 26.9 ms                                                | 25.4 ms: 1.06x faster                                                      |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                       |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 101 ms                                                 | 97.2 ms: 1.04x faster                                                      |
| json_loads           | 27.2 us                                                | 26.8 us: 1.01x faster                                                      |
| xml_etree_process    | 60.5 ms                                                | 59.8 ms: 1.01x faster                                                      |
| xml_etree_generate   | 86.8 ms                                                | 86.2 ms: 1.01x faster                                                      |
| tomli_loads          | 2.12 sec                                               | 2.11 sec: 1.00x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                       |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.06x slower                                                       |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.05 ms: 1.01x slower                                                      |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.1 ms: 1.02x faster                                                      |
| genshi_xml      | 50.5 ms                                                | 49.5 ms: 1.02x faster                                                      |
| django_template | 31.7 ms                                                | 32.1 ms: 1.01x slower                                                      |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                       |
| deepcopy_memo              | 38.4 us                                                | 30.6 us: 1.25x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                                      |
| go                         | 141 ms                                                 | 122 ms: 1.16x faster                                                       |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.36 ms: 1.12x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                       |
| telco                      | 8.40 ms                                                | 7.83 ms: 1.07x faster                                                      |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.07x faster                                                      |
| json                       | 5.32 ms                                                | 5.02 ms: 1.06x faster                                                      |
| generators                 | 28.8 ms                                                | 27.2 ms: 1.06x faster                                                      |
| thrift                     | 800 us                                                 | 756 us: 1.06x faster                                                       |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                     |
| regex_v8                   | 26.9 ms                                                | 25.4 ms: 1.06x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                       |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.2 ms: 1.04x faster                                                      |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 101 ms                                                 | 97.2 ms: 1.04x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.51 sec: 1.04x faster                                                     |
| djangocms                  | 22.3 us                                                | 21.5 us: 1.03x faster                                                      |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                     |
| crypto_pyaes               | 74.7 ms                                                | 72.7 ms: 1.03x faster                                                      |
| sqlglot_normalize          | 108 ms                                                 | 105 ms: 1.03x faster                                                       |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                       |
| async_generators           | 433 ms                                                 | 423 ms: 1.03x faster                                                       |
| nqueens                    | 80.9 ms                                                | 79.0 ms: 1.02x faster                                                      |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                      |
| genshi_text                | 22.6 ms                                                | 22.1 ms: 1.02x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                       |
| richards                   | 47.5 ms                                                | 46.5 ms: 1.02x faster                                                      |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                       |
| float                      | 78.7 ms                                                | 77.0 ms: 1.02x faster                                                      |
| genshi_xml                 | 50.5 ms                                                | 49.5 ms: 1.02x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.85 us: 1.02x faster                                                      |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                       |
| pyflate                    | 470 ms                                                 | 462 ms: 1.02x faster                                                       |
| logging_format             | 6.23 us                                                | 6.13 us: 1.02x faster                                                      |
| logging_simple             | 5.65 us                                                | 5.56 us: 1.02x faster                                                      |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.02x faster                                                       |
| connected_components       | 447 ms                                                 | 440 ms: 1.02x faster                                                       |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                                     |
| richards_super             | 53.7 ms                                                | 53.1 ms: 1.01x faster                                                      |
| json_loads                 | 27.2 us                                                | 26.8 us: 1.01x faster                                                      |
| xml_etree_process          | 60.5 ms                                                | 59.8 ms: 1.01x faster                                                      |
| sqlglot_optimize           | 53.4 ms                                                | 52.8 ms: 1.01x faster                                                      |
| shortest_path              | 487 ms                                                 | 483 ms: 1.01x faster                                                       |
| xml_etree_generate         | 86.8 ms                                                | 86.2 ms: 1.01x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 2.11 sec: 1.00x faster                                                     |
| fannkuch                   | 394 ms                                                 | 393 ms: 1.00x faster                                                       |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                       |
| scimark_fft                | 367 ms                                                 | 368 ms: 1.00x slower                                                       |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.00x slower                                                      |
| python_startup_no_site     | 7.00 ms                                                | 7.05 ms: 1.01x slower                                                      |
| spectral_norm              | 113 ms                                                 | 114 ms: 1.01x slower                                                       |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                                     |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                      |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                      |
| coverage                   | 82.8 ms                                                | 83.8 ms: 1.01x slower                                                      |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.01x slower                                                      |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                                       |
| dulwich_log                | 64.6 ms                                                | 65.7 ms: 1.02x slower                                                      |
| sqlglot_parse              | 1.26 ms                                                | 1.29 ms: 1.02x slower                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                      |
| hexiom                     | 6.08 ms                                                | 6.20 ms: 1.02x slower                                                      |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                       |
| scimark_monte_carlo        | 66.8 ms                                                | 68.4 ms: 1.02x slower                                                      |
| gc_traversal               | 4.90 ms                                                | 5.02 ms: 1.03x slower                                                      |
| deltablue                  | 3.19 ms                                                | 3.28 ms: 1.03x slower                                                      |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                       |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                      |
| scimark_sor                | 122 ms                                                 | 126 ms: 1.03x slower                                                       |
| mdp                        | 2.54 sec                                               | 2.64 sec: 1.04x slower                                                     |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                      |
| nbody                      | 87.7 ms                                                | 91.8 ms: 1.05x slower                                                      |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                       |
| logging_silent             | 101 ns                                                 | 106 ns: 1.05x slower                                                       |
| bench_thread_pool          | 818 us                                                 | 858 us: 1.05x slower                                                       |
| chaos                      | 58.0 ms                                                | 61.5 ms: 1.06x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.06x slower                                                       |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                      |
| many_optionals             | 857 us                                                 | 949 us: 1.11x slower                                                       |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                      |
| async_tree_io_tg           | 861 ms                                                 | 1.00 sec: 1.16x slower                                                     |
| async_tree_io              | 838 ms                                                 | 1.03 sec: 1.23x slower                                                     |
| async_tree_memoization_tg  | 463 ms                                                 | 580 ms: 1.25x slower                                                       |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 746 ms: 1.37x slower                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 796 ms: 1.39x slower                                                       |
| async_tree_memoization     | 437 ms                                                 | 632 ms: 1.45x slower                                                       |
| async_tree_none            | 350 ms                                                 | 522 ms: 1.49x slower                                                       |
| async_tree_none_tg         | 319 ms                                                 | 489 ms: 1.53x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                               |

Benchmark hidden because not significant (5): sympy_expand, scimark_sparse_mat_mult, docutils, pprint_safe_repr, asyncio_websockets
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241215-3.14.0a2+-a0a0f85/bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85.json: mypy2

- Geometric mean (including insignificant results): 1.015x slower

# HPT report

- Reliability score: 69.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x