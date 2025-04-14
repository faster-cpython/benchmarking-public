# Results vs. 3.13.0

- fork: faster-cpython
- ref: c_recursion_limit
- machine: linux-x86_64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.047x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                          |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.00x slower                                                        |
| html5lib       | 63.4 ms                                                | 61.2 ms: 1.04x faster                                                         |
| sphinx         | 1.03 sec                                               | 999 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 323 ms: 1.35x faster                                                          |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                          |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                          |
| async_generators           | 433 ms                                                 | 389 ms: 1.11x faster                                                          |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.9 ms: 1.11x faster                                                         |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                          |
| nbody          | 87.7 ms                                                | 93.6 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.15 ms: 1.20x faster                                                         |
| regex_v8       | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                         |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                  |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                          |
| tomli_loads          | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 97.4 ms: 1.04x faster                                                         |
| xml_etree_process    | 60.5 ms                                                | 58.8 ms: 1.03x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 84.5 ms: 1.03x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                          |
| pickle_pure_python   | 302 us                                                 | 313 us: 1.04x slower                                                          |
| json_loads           | 27.2 us                                                | 30.4 us: 1.12x slower                                                         |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                         |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.6 ms: 1.05x faster                                                         |
| genshi_xml      | 50.5 ms                                                | 49.3 ms: 1.02x faster                                                         |
| django_template | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                         |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                          |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 323 ms: 1.35x faster                                                          |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                          |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                          |
| deepcopy_memo              | 38.4 us                                                | 29.9 us: 1.28x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                          |
| go                         | 141 ms                                                 | 115 ms: 1.22x faster                                                          |
| regex_effbot               | 3.77 ms                                                | 3.15 ms: 1.20x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                          |
| spectral_norm              | 113 ms                                                 | 96.9 ms: 1.17x faster                                                         |
| pylint                     | 312 ms                                                 | 274 ms: 1.14x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                          |
| async_generators           | 433 ms                                                 | 389 ms: 1.11x faster                                                          |
| float                      | 78.7 ms                                                | 70.9 ms: 1.11x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                          |
| richards                   | 47.5 ms                                                | 43.6 ms: 1.09x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                        |
| telco                      | 8.40 ms                                                | 7.75 ms: 1.08x faster                                                         |
| richards_super             | 53.7 ms                                                | 49.8 ms: 1.08x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                         |
| scimark_fft                | 367 ms                                                 | 342 ms: 1.07x faster                                                          |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                        |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                          |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.47 sec: 1.05x faster                                                        |
| genshi_text                | 22.6 ms                                                | 21.6 ms: 1.05x faster                                                         |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                          |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                                         |
| thrift                     | 800 us                                                 | 767 us: 1.04x faster                                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.83 ms: 1.04x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 97.4 ms: 1.04x faster                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                          |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                        |
| html5lib                   | 63.4 ms                                                | 61.2 ms: 1.04x faster                                                         |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.03x faster                                                          |
| sphinx                     | 1.03 sec                                               | 999 ms: 1.03x faster                                                          |
| pyflate                    | 470 ms                                                 | 455 ms: 1.03x faster                                                          |
| logging_simple             | 5.65 us                                                | 5.49 us: 1.03x faster                                                         |
| crypto_pyaes               | 74.7 ms                                                | 72.6 ms: 1.03x faster                                                         |
| xml_etree_process          | 60.5 ms                                                | 58.8 ms: 1.03x faster                                                         |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                          |
| xml_etree_generate         | 86.8 ms                                                | 84.5 ms: 1.03x faster                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                         |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                          |
| logging_format             | 6.23 us                                                | 6.07 us: 1.03x faster                                                         |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.02x faster                                                        |
| genshi_xml                 | 50.5 ms                                                | 49.3 ms: 1.02x faster                                                         |
| connected_components       | 447 ms                                                 | 436 ms: 1.02x faster                                                          |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                          |
| sqlglot_optimize           | 53.4 ms                                                | 52.3 ms: 1.02x faster                                                         |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                          |
| shortest_path              | 487 ms                                                 | 477 ms: 1.02x faster                                                          |
| typing_runtime_protocols   | 160 us                                                 | 158 us: 1.02x faster                                                          |
| deltablue                  | 3.19 ms                                                | 3.15 ms: 1.01x faster                                                         |
| generators                 | 28.8 ms                                                | 28.4 ms: 1.01x faster                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                                        |
| pprint_safe_repr           | 727 ms                                                 | 719 ms: 1.01x faster                                                          |
| sympy_integrate            | 19.8 ms                                                | 19.7 ms: 1.01x faster                                                         |
| sympy_expand               | 456 ms                                                 | 453 ms: 1.01x faster                                                          |
| sqlglot_parse              | 1.26 ms                                                | 1.26 ms: 1.01x faster                                                         |
| comprehensions             | 16.5 us                                                | 16.4 us: 1.01x faster                                                         |
| chaos                      | 58.0 ms                                                | 57.7 ms: 1.01x faster                                                         |
| dulwich_log                | 64.6 ms                                                | 64.3 ms: 1.00x faster                                                         |
| sqlglot_transpile          | 1.57 ms                                                | 1.56 ms: 1.00x faster                                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                          |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.00x slower                                                        |
| gc_traversal               | 4.90 ms                                                | 4.93 ms: 1.01x slower                                                         |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                         |
| nqueens                    | 80.9 ms                                                | 81.7 ms: 1.01x slower                                                         |
| django_template            | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                         |
| json                       | 5.32 ms                                                | 5.38 ms: 1.01x slower                                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                         |
| hexiom                     | 6.08 ms                                                | 6.15 ms: 1.01x slower                                                         |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                          |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                          |
| logging_silent             | 101 ns                                                 | 103 ns: 1.02x slower                                                          |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                         |
| fannkuch                   | 394 ms                                                 | 403 ms: 1.02x slower                                                          |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                         |
| raytrace                   | 262 ms                                                 | 269 ms: 1.03x slower                                                          |
| pickle_pure_python         | 302 us                                                 | 313 us: 1.04x slower                                                          |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 866 us: 1.06x slower                                                          |
| nbody                      | 87.7 ms                                                | 93.6 ms: 1.07x slower                                                         |
| many_optionals             | 857 us                                                 | 935 us: 1.09x slower                                                          |
| coverage                   | 82.8 ms                                                | 90.8 ms: 1.10x slower                                                         |
| json_loads                 | 27.2 us                                                | 30.4 us: 1.12x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                         |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.33x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                  |

Benchmark hidden because not significant (3): scimark_monte_carlo, regex_dna, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x