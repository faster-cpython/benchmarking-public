# Results vs. 3.13.0

- fork: kumaraditya303
- ref: fast_state
- machine: linux-x86_64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.178x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 345 ms: 1.30x slower                                                 |
| docutils       | 2.58 sec                                               | 2.99 sec: 1.16x slower                                               |
| html5lib       | 63.4 ms                                                | 85.7 ms: 1.35x slower                                                |
| sphinx         | 1.03 sec                                               | 1.17 sec: 1.13x slower                                               |
| Geometric mean | (ref)                                                  | 1.23x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 675 ms: 1.27x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 385 ms: 1.20x faster                                                 |
| async_tree_io              | 838 ms                                                 | 726 ms: 1.15x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 292 ms: 1.09x faster                                                 |
| async_tree_none            | 350 ms                                                 | 339 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 529 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 580 ms: 1.01x slower                                                 |
| async_generators           | 433 ms                                                 | 501 ms: 1.16x slower                                                 |
| coroutines                 | 22.2 ms                                                | 26.8 ms: 1.20x slower                                                |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                         |

Benchmark hidden because not significant (2): async_tree_memoization, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 181 ms: 1.03x faster                                                 |
| float          | 78.7 ms                                                | 105 ms: 1.34x slower                                                 |
| nbody          | 87.7 ms                                                | 136 ms: 1.56x slower                                                 |
| Geometric mean | (ref)                                                  | 1.27x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 25.2 ms: 1.06x faster                                                |
| regex_effbot   | 3.77 ms                                                | 3.59 ms: 1.05x faster                                                |
| regex_dna      | 220 ms                                                 | 231 ms: 1.05x slower                                                 |
| regex_compile  | 132 ms                                                 | 162 ms: 1.23x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 95.7 ms: 1.06x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 148 ms: 1.04x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 96.2 ms: 1.11x slower                                                |
| json_loads           | 27.2 us                                                | 30.3 us: 1.11x slower                                                |
| xml_etree_process    | 60.5 ms                                                | 72.3 ms: 1.19x slower                                                |
| tomli_loads          | 2.12 sec                                               | 2.55 sec: 1.21x slower                                               |
| json_dumps           | 10.1 ms                                                | 13.0 ms: 1.29x slower                                                |
| unpickle_pure_python | 213 us                                                 | 314 us: 1.47x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 482 us: 1.59x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.19x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.5 ms: 1.22x slower                                                |
| python_startup_no_site | 7.00 ms                                                | 9.59 ms: 1.37x slower                                                |
| Geometric mean         | (ref)                                                  | 1.29x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 63.0 ms: 1.25x slower                                                |
| genshi_text     | 22.6 ms                                                | 30.4 ms: 1.34x slower                                                |
| django_template | 31.7 ms                                                | 46.5 ms: 1.47x slower                                                |
| mako            | 10.7 ms                                                | 18.2 ms: 1.71x slower                                                |
| Geometric mean  | (ref)                                                  | 1.43x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 3.75 ms: 1.31x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 675 ms: 1.27x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 385 ms: 1.20x faster                                                 |
| async_tree_io              | 838 ms                                                 | 726 ms: 1.15x faster                                                 |
| deepcopy                   | 354 us                                                 | 319 us: 1.11x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 292 ms: 1.09x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 25.2 ms: 1.06x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 95.7 ms: 1.06x faster                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.33 ms: 1.05x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.59 ms: 1.05x faster                                                |
| xml_etree_parse            | 154 ms                                                 | 148 ms: 1.04x faster                                                 |
| async_tree_none            | 350 ms                                                 | 339 ms: 1.03x faster                                                 |
| pidigits                   | 186 ms                                                 | 181 ms: 1.03x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.83 us: 1.03x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 529 ms: 1.03x faster                                                 |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 580 ms: 1.01x slower                                                 |
| deepcopy_reduce            | 3.24 us                                                | 3.32 us: 1.02x slower                                                |
| k_core                     | 2.37 sec                                               | 2.47 sec: 1.04x slower                                               |
| regex_dna                  | 220 ms                                                 | 231 ms: 1.05x slower                                                 |
| deepcopy_memo              | 38.4 us                                                | 40.3 us: 1.05x slower                                                |
| pylint                     | 312 ms                                                 | 341 ms: 1.09x slower                                                 |
| telco                      | 8.40 ms                                                | 9.21 ms: 1.10x slower                                                |
| xml_etree_generate         | 86.8 ms                                                | 96.2 ms: 1.11x slower                                                |
| json_loads                 | 27.2 us                                                | 30.3 us: 1.11x slower                                                |
| spectral_norm              | 113 ms                                                 | 127 ms: 1.12x slower                                                 |
| mdp                        | 2.54 sec                                               | 2.86 sec: 1.12x slower                                               |
| sphinx                     | 1.03 sec                                               | 1.17 sec: 1.13x slower                                               |
| bpe_tokeniser              | 4.69 sec                                               | 5.30 sec: 1.13x slower                                               |
| scimark_fft                | 367 ms                                                 | 417 ms: 1.14x slower                                                 |
| pycparser                  | 1.20 sec                                               | 1.37 sec: 1.14x slower                                               |
| async_generators           | 433 ms                                                 | 501 ms: 1.16x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.99 sec: 1.16x slower                                               |
| dulwich_log                | 64.6 ms                                                | 75.5 ms: 1.17x slower                                                |
| shortest_path              | 487 ms                                                 | 578 ms: 1.19x slower                                                 |
| xml_etree_process          | 60.5 ms                                                | 72.3 ms: 1.19x slower                                                |
| sqlglot_normalize          | 108 ms                                                 | 129 ms: 1.20x slower                                                 |
| connected_components       | 447 ms                                                 | 537 ms: 1.20x slower                                                 |
| coroutines                 | 22.2 ms                                                | 26.8 ms: 1.20x slower                                                |
| tomli_loads                | 2.12 sec                                               | 2.55 sec: 1.21x slower                                               |
| meteor_contest             | 108 ms                                                 | 131 ms: 1.21x slower                                                 |
| sqlglot_optimize           | 53.4 ms                                                | 64.7 ms: 1.21x slower                                                |
| sympy_sum                  | 150 ms                                                 | 183 ms: 1.21x slower                                                 |
| sympy_expand               | 456 ms                                                 | 555 ms: 1.22x slower                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.14 ms: 1.22x slower                                                |
| sympy_str                  | 273 ms                                                 | 333 ms: 1.22x slower                                                 |
| python_startup             | 12.7 ms                                                | 15.5 ms: 1.22x slower                                                |
| regex_compile              | 132 ms                                                 | 162 ms: 1.23x slower                                                 |
| nqueens                    | 80.9 ms                                                | 99.8 ms: 1.23x slower                                                |
| sympy_integrate            | 19.8 ms                                                | 24.5 ms: 1.24x slower                                                |
| crypto_pyaes               | 74.7 ms                                                | 92.3 ms: 1.24x slower                                                |
| coverage                   | 82.8 ms                                                | 103 ms: 1.24x slower                                                 |
| generators                 | 28.8 ms                                                | 35.9 ms: 1.25x slower                                                |
| genshi_xml                 | 50.5 ms                                                | 63.0 ms: 1.25x slower                                                |
| thrift                     | 800 us                                                 | 1.01 ms: 1.26x slower                                                |
| json_dumps                 | 10.1 ms                                                | 13.0 ms: 1.29x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 206 us: 1.29x slower                                                 |
| 2to3                       | 266 ms                                                 | 345 ms: 1.30x slower                                                 |
| richards_super             | 53.7 ms                                                | 70.3 ms: 1.31x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 956 ms: 1.32x slower                                                 |
| many_optionals             | 857 us                                                 | 1.13 ms: 1.32x slower                                                |
| richards                   | 47.5 ms                                                | 63.1 ms: 1.33x slower                                                |
| fannkuch                   | 394 ms                                                 | 526 ms: 1.34x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.98 sec: 1.34x slower                                               |
| float                      | 78.7 ms                                                | 105 ms: 1.34x slower                                                 |
| genshi_text                | 22.6 ms                                                | 30.4 ms: 1.34x slower                                                |
| scimark_lu                 | 114 ms                                                 | 154 ms: 1.35x slower                                                 |
| html5lib                   | 63.4 ms                                                | 85.7 ms: 1.35x slower                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 180 ms: 1.36x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 9.59 ms: 1.37x slower                                                |
| pyflate                    | 470 ms                                                 | 651 ms: 1.39x slower                                                 |
| sqlalchemy_imperative      | 16.9 ms                                                | 23.5 ms: 1.39x slower                                                |
| logging_simple             | 5.65 us                                                | 7.92 us: 1.40x slower                                                |
| logging_format             | 6.23 us                                                | 8.81 us: 1.41x slower                                                |
| django_template            | 31.7 ms                                                | 46.5 ms: 1.47x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 314 us: 1.47x slower                                                 |
| comprehensions             | 16.5 us                                                | 25.4 us: 1.54x slower                                                |
| go                         | 141 ms                                                 | 218 ms: 1.55x slower                                                 |
| nbody                      | 87.7 ms                                                | 136 ms: 1.56x slower                                                 |
| hexiom                     | 6.08 ms                                                | 9.50 ms: 1.56x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 105 ms: 1.57x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 482 us: 1.59x slower                                                 |
| chaos                      | 58.0 ms                                                | 92.7 ms: 1.60x slower                                                |
| sqlglot_transpile          | 1.57 ms                                                | 2.55 ms: 1.63x slower                                                |
| mako                       | 10.7 ms                                                | 18.2 ms: 1.71x slower                                                |
| subparsers                 | 15.5 ms                                                | 26.5 ms: 1.71x slower                                                |
| logging_silent             | 101 ns                                                 | 176 ns: 1.74x slower                                                 |
| sqlglot_parse              | 1.26 ms                                                | 2.21 ms: 1.75x slower                                                |
| raytrace                   | 262 ms                                                 | 465 ms: 1.78x slower                                                 |
| scimark_sor                | 122 ms                                                 | 223 ms: 1.83x slower                                                 |
| deltablue                  | 3.19 ms                                                | 7.05 ms: 2.21x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 95.0 ms: 3.96x slower                                                |
| bench_thread_pool          | 818 us                                                 | 3.56 ms: 4.35x slower                                                |
| Geometric mean             | (ref)                                                  | 1.25x slower                                                         |

Benchmark hidden because not significant (3): async_tree_memoization, json, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-7de6e22-NOGIL/bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: mypy2

- Geometric mean (including insignificant results): 1.178x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.15x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: 1.22x