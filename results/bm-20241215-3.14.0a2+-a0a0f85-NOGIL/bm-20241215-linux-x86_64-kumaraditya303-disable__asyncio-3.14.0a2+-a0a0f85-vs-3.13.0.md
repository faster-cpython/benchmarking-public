# Results vs. 3.13.0

- fork: kumaraditya303
- ref: disable__asyncio
- machine: linux-x86_64
- commit hash: a0a0f85
- commit date: 2024-12-15
- overall geometric mean: 1.258x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 353 ms: 1.33x slower                                                       |
| docutils       | 2.58 sec                                               | 3.02 sec: 1.17x slower                                                     |
| html5lib       | 63.4 ms                                                | 92.3 ms: 1.46x slower                                                      |
| sphinx         | 1.03 sec                                               | 1.19 sec: 1.15x slower                                                     |
| Geometric mean | (ref)                                                  | 1.27x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators           | 433 ms                                                 | 505 ms: 1.17x slower                                                       |
| coroutines                 | 22.2 ms                                                | 26.5 ms: 1.19x slower                                                      |
| async_tree_io_tg           | 861 ms                                                 | 1.28 sec: 1.49x slower                                                     |
| async_tree_io              | 838 ms                                                 | 1.37 sec: 1.63x slower                                                     |
| async_tree_memoization_tg  | 463 ms                                                 | 805 ms: 1.74x slower                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 951 ms: 1.75x slower                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 1.03 sec: 1.80x slower                                                     |
| async_tree_memoization     | 437 ms                                                 | 884 ms: 2.02x slower                                                       |
| async_tree_none            | 350 ms                                                 | 733 ms: 2.09x slower                                                       |
| async_tree_none_tg         | 319 ms                                                 | 679 ms: 2.13x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.59x slower                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                                       |
| nbody          | 87.7 ms                                                | 139 ms: 1.59x slower                                                       |
| float          | 78.7 ms                                                | 131 ms: 1.66x slower                                                       |
| Geometric mean | (ref)                                                  | 1.39x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.50 ms: 1.08x faster                                                      |
| regex_v8       | 26.9 ms                                                | 26.0 ms: 1.03x faster                                                      |
| regex_dna      | 220 ms                                                 | 226 ms: 1.03x slower                                                       |
| regex_compile  | 132 ms                                                 | 171 ms: 1.30x slower                                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 95.9 ms: 1.06x faster                                                      |
| xml_etree_parse      | 154 ms                                                 | 148 ms: 1.04x faster                                                       |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                      |
| xml_etree_generate   | 86.8 ms                                                | 97.0 ms: 1.12x slower                                                      |
| xml_etree_process    | 60.5 ms                                                | 75.4 ms: 1.25x slower                                                      |
| tomli_loads          | 2.12 sec                                               | 2.78 sec: 1.31x slower                                                     |
| json_dumps           | 10.1 ms                                                | 13.7 ms: 1.36x slower                                                      |
| unpickle_pure_python | 213 us                                                 | 320 us: 1.50x slower                                                       |
| pickle_pure_python   | 302 us                                                 | 475 us: 1.57x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.22x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 16.3 ms: 1.29x slower                                                      |
| python_startup_no_site | 7.00 ms                                                | 9.76 ms: 1.39x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.34x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 63.7 ms: 1.26x slower                                                      |
| genshi_text     | 22.6 ms                                                | 31.7 ms: 1.40x slower                                                      |
| django_template | 31.7 ms                                                | 47.3 ms: 1.49x slower                                                      |
| mako            | 10.7 ms                                                | 18.4 ms: 1.72x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.46x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 3.80 ms: 1.29x faster                                                      |
| deepcopy                   | 354 us                                                 | 317 us: 1.12x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.50 ms: 1.08x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 95.9 ms: 1.06x faster                                                      |
| create_gc_cycles           | 2.45 ms                                                | 2.32 ms: 1.05x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 148 ms: 1.04x faster                                                       |
| regex_v8                   | 26.9 ms                                                | 26.0 ms: 1.03x faster                                                      |
| pathlib                    | 17.4 ms                                                | 17.6 ms: 1.01x slower                                                      |
| sqlite_synth               | 2.90 us                                                | 2.94 us: 1.01x slower                                                      |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                                       |
| json                       | 5.32 ms                                                | 5.46 ms: 1.02x slower                                                      |
| regex_dna                  | 220 ms                                                 | 226 ms: 1.03x slower                                                       |
| deepcopy_reduce            | 3.24 us                                                | 3.37 us: 1.04x slower                                                      |
| deepcopy_memo              | 38.4 us                                                | 40.6 us: 1.06x slower                                                      |
| k_core                     | 2.37 sec                                               | 2.56 sec: 1.08x slower                                                     |
| telco                      | 8.40 ms                                                | 9.15 ms: 1.09x slower                                                      |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                      |
| xml_etree_generate         | 86.8 ms                                                | 97.0 ms: 1.12x slower                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 5.27 sec: 1.12x slower                                                     |
| sphinx                     | 1.03 sec                                               | 1.19 sec: 1.15x slower                                                     |
| pylint                     | 312 ms                                                 | 362 ms: 1.16x slower                                                       |
| async_generators           | 433 ms                                                 | 505 ms: 1.17x slower                                                       |
| docutils                   | 2.58 sec                                               | 3.02 sec: 1.17x slower                                                     |
| coroutines                 | 22.2 ms                                                | 26.5 ms: 1.19x slower                                                      |
| connected_components       | 447 ms                                                 | 536 ms: 1.20x slower                                                       |
| shortest_path              | 487 ms                                                 | 584 ms: 1.20x slower                                                       |
| mdp                        | 2.54 sec                                               | 3.07 sec: 1.21x slower                                                     |
| meteor_contest             | 108 ms                                                 | 131 ms: 1.21x slower                                                       |
| pycparser                  | 1.20 sec                                               | 1.45 sec: 1.21x slower                                                     |
| sqlglot_normalize          | 108 ms                                                 | 131 ms: 1.21x slower                                                       |
| spectral_norm              | 113 ms                                                 | 138 ms: 1.22x slower                                                       |
| scimark_fft                | 367 ms                                                 | 449 ms: 1.22x slower                                                       |
| nqueens                    | 80.9 ms                                                | 99.1 ms: 1.23x slower                                                      |
| crypto_pyaes               | 74.7 ms                                                | 92.5 ms: 1.24x slower                                                      |
| sqlglot_optimize           | 53.4 ms                                                | 66.1 ms: 1.24x slower                                                      |
| dulwich_log                | 64.6 ms                                                | 80.4 ms: 1.24x slower                                                      |
| generators                 | 28.8 ms                                                | 35.9 ms: 1.25x slower                                                      |
| xml_etree_process          | 60.5 ms                                                | 75.4 ms: 1.25x slower                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.34 ms: 1.26x slower                                                      |
| genshi_xml                 | 50.5 ms                                                | 63.7 ms: 1.26x slower                                                      |
| python_startup             | 12.7 ms                                                | 16.3 ms: 1.29x slower                                                      |
| coverage                   | 82.8 ms                                                | 107 ms: 1.29x slower                                                       |
| regex_compile              | 132 ms                                                 | 171 ms: 1.30x slower                                                       |
| typing_runtime_protocols   | 160 us                                                 | 209 us: 1.31x slower                                                       |
| sympy_integrate            | 19.8 ms                                                | 26.0 ms: 1.31x slower                                                      |
| tomli_loads                | 2.12 sec                                               | 2.78 sec: 1.31x slower                                                     |
| 2to3                       | 266 ms                                                 | 353 ms: 1.33x slower                                                       |
| fannkuch                   | 394 ms                                                 | 533 ms: 1.35x slower                                                       |
| json_dumps                 | 10.1 ms                                                | 13.7 ms: 1.36x slower                                                      |
| many_optionals             | 857 us                                                 | 1.17 ms: 1.37x slower                                                      |
| sympy_str                  | 273 ms                                                 | 373 ms: 1.37x slower                                                       |
| pprint_safe_repr           | 727 ms                                                 | 998 ms: 1.37x slower                                                       |
| thrift                     | 800 us                                                 | 1.11 ms: 1.39x slower                                                      |
| python_startup_no_site     | 7.00 ms                                                | 9.76 ms: 1.39x slower                                                      |
| pprint_pformat             | 1.48 sec                                               | 2.07 sec: 1.40x slower                                                     |
| genshi_text                | 22.6 ms                                                | 31.7 ms: 1.40x slower                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 191 ms: 1.44x slower                                                       |
| html5lib                   | 63.4 ms                                                | 92.3 ms: 1.46x slower                                                      |
| richards_super             | 53.7 ms                                                | 79.1 ms: 1.47x slower                                                      |
| pyflate                    | 470 ms                                                 | 693 ms: 1.48x slower                                                       |
| sympy_expand               | 456 ms                                                 | 673 ms: 1.48x slower                                                       |
| richards                   | 47.5 ms                                                | 70.2 ms: 1.48x slower                                                      |
| sqlalchemy_imperative      | 16.9 ms                                                | 25.1 ms: 1.48x slower                                                      |
| async_tree_io_tg           | 861 ms                                                 | 1.28 sec: 1.49x slower                                                     |
| django_template            | 31.7 ms                                                | 47.3 ms: 1.49x slower                                                      |
| unpickle_pure_python       | 213 us                                                 | 320 us: 1.50x slower                                                       |
| scimark_lu                 | 114 ms                                                 | 176 ms: 1.54x slower                                                       |
| sympy_sum                  | 150 ms                                                 | 233 ms: 1.55x slower                                                       |
| comprehensions             | 16.5 us                                                | 25.8 us: 1.56x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 475 us: 1.57x slower                                                       |
| nbody                      | 87.7 ms                                                | 139 ms: 1.59x slower                                                       |
| hexiom                     | 6.08 ms                                                | 9.72 ms: 1.60x slower                                                      |
| logging_format             | 6.23 us                                                | 10.1 us: 1.62x slower                                                      |
| async_tree_io              | 838 ms                                                 | 1.37 sec: 1.63x slower                                                     |
| logging_simple             | 5.65 us                                                | 9.26 us: 1.64x slower                                                      |
| float                      | 78.7 ms                                                | 131 ms: 1.66x slower                                                       |
| scimark_monte_carlo        | 66.8 ms                                                | 113 ms: 1.70x slower                                                       |
| logging_silent             | 101 ns                                                 | 173 ns: 1.71x slower                                                       |
| chaos                      | 58.0 ms                                                | 99.7 ms: 1.72x slower                                                      |
| mako                       | 10.7 ms                                                | 18.4 ms: 1.72x slower                                                      |
| go                         | 141 ms                                                 | 243 ms: 1.73x slower                                                       |
| async_tree_memoization_tg  | 463 ms                                                 | 805 ms: 1.74x slower                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 951 ms: 1.75x slower                                                       |
| sqlglot_transpile          | 1.57 ms                                                | 2.78 ms: 1.77x slower                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 1.03 sec: 1.80x slower                                                     |
| subparsers                 | 15.5 ms                                                | 28.3 ms: 1.83x slower                                                      |
| sqlglot_parse              | 1.26 ms                                                | 2.42 ms: 1.92x slower                                                      |
| raytrace                   | 262 ms                                                 | 505 ms: 1.93x slower                                                       |
| scimark_sor                | 122 ms                                                 | 237 ms: 1.94x slower                                                       |
| async_tree_memoization     | 437 ms                                                 | 884 ms: 2.02x slower                                                       |
| async_tree_none            | 350 ms                                                 | 733 ms: 2.09x slower                                                       |
| async_tree_none_tg         | 319 ms                                                 | 679 ms: 2.13x slower                                                       |
| deltablue                  | 3.19 ms                                                | 7.56 ms: 2.37x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 102 ms: 4.27x slower                                                       |
| bench_thread_pool          | 818 us                                                 | 3.59 ms: 4.39x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.38x slower                                                               |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241215-3.14.0a2+-a0a0f85-NOGIL/bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85.json: mypy2

- Geometric mean (including insignificant results): 1.258x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.28x
- 95% likely to have a slowdown of 1.26x
- 99% likely to have a slowdown of 1.24x

# Memory
- memory change: 1.24x