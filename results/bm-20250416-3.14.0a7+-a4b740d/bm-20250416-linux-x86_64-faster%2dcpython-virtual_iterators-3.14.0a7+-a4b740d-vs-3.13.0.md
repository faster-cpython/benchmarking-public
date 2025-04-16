# Results vs. 3.13.0

- fork: faster-cpython
- ref: virtual_iterators
- machine: linux-x86_64
- commit hash: a4b740d
- commit date: 2025-04-16
- overall geometric mean: 1.064x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 250 ms: 1.06x faster                                                          |
| docutils       | 2.58 sec                                               | 2.56 sec: 1.01x faster                                                        |
| html5lib       | 63.4 ms                                                | 59.6 ms: 1.06x faster                                                         |
| sphinx         | 1.03 sec                                               | 993 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 309 ms: 1.41x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                          |
| async_tree_io              | 838 ms                                                 | 610 ms: 1.37x faster                                                          |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 480 ms: 1.19x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                                          |
| async_generators           | 433 ms                                                 | 394 ms: 1.10x faster                                                          |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.0 ms: 1.14x faster                                                         |
| nbody          | 87.7 ms                                                | 93.9 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.02 ms: 1.25x faster                                                         |
| regex_v8       | 26.9 ms                                                | 22.3 ms: 1.21x faster                                                         |
| regex_dna      | 220 ms                                                 | 203 ms: 1.08x faster                                                          |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                          |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                        |
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                                          |
| xml_etree_process    | 60.5 ms                                                | 57.8 ms: 1.05x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 83.2 ms: 1.04x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                          |
| pickle_pure_python   | 302 us                                                 | 317 us: 1.05x slower                                                          |
| json_loads           | 27.2 us                                                | 30.1 us: 1.11x slower                                                         |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                         |
| python_startup_no_site | 7.00 ms                                                | 8.23 ms: 1.18x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.6 ms: 1.10x faster                                                         |
| genshi_xml      | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                         |
| django_template | 31.7 ms                                                | 31.0 ms: 1.02x faster                                                         |
| mako            | 10.7 ms                                                | 11.3 ms: 1.05x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.20 sec: 2.12x faster                                                        |
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                          |
| deepcopy                   | 354 us                                                 | 250 us: 1.42x faster                                                          |
| async_tree_memoization     | 437 ms                                                 | 309 ms: 1.41x faster                                                          |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                          |
| async_tree_io              | 838 ms                                                 | 610 ms: 1.37x faster                                                          |
| async_tree_none            | 350 ms                                                 | 256 ms: 1.37x faster                                                          |
| deepcopy_memo              | 38.4 us                                                | 28.7 us: 1.34x faster                                                         |
| go                         | 141 ms                                                 | 108 ms: 1.30x faster                                                          |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                          |
| regex_effbot               | 3.77 ms                                                | 3.02 ms: 1.25x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.65 us: 1.22x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 22.3 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 480 ms: 1.19x faster                                                          |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                                          |
| float                      | 78.7 ms                                                | 69.0 ms: 1.14x faster                                                         |
| richards                   | 47.5 ms                                                | 42.9 ms: 1.11x faster                                                         |
| genshi_text                | 22.6 ms                                                | 20.6 ms: 1.10x faster                                                         |
| telco                      | 8.40 ms                                                | 7.64 ms: 1.10x faster                                                         |
| async_generators           | 433 ms                                                 | 394 ms: 1.10x faster                                                          |
| richards_super             | 53.7 ms                                                | 49.1 ms: 1.09x faster                                                         |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.09x faster                                                          |
| pycparser                  | 1.20 sec                                               | 1.10 sec: 1.09x faster                                                        |
| pyflate                    | 470 ms                                                 | 431 ms: 1.09x faster                                                          |
| tomli_loads                | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                        |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                                          |
| dulwich_log                | 64.6 ms                                                | 59.5 ms: 1.09x faster                                                         |
| regex_dna                  | 220 ms                                                 | 203 ms: 1.08x faster                                                          |
| 2to3                       | 266 ms                                                 | 250 ms: 1.06x faster                                                          |
| html5lib                   | 63.4 ms                                                | 59.6 ms: 1.06x faster                                                         |
| logging_silent             | 101 ns                                                 | 95.3 ns: 1.06x faster                                                         |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                          |
| xml_etree_process          | 60.5 ms                                                | 57.8 ms: 1.05x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                        |
| xml_etree_generate         | 86.8 ms                                                | 83.2 ms: 1.04x faster                                                         |
| meteor_contest             | 108 ms                                                 | 104 ms: 1.04x faster                                                          |
| sphinx                     | 1.03 sec                                               | 993 ms: 1.04x faster                                                          |
| comprehensions             | 16.5 us                                                | 15.9 us: 1.04x faster                                                         |
| logging_simple             | 5.65 us                                                | 5.46 us: 1.04x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                         |
| pprint_safe_repr           | 727 ms                                                 | 702 ms: 1.03x faster                                                          |
| logging_format             | 6.23 us                                                | 6.02 us: 1.03x faster                                                         |
| pathlib                    | 17.4 ms                                                | 16.8 ms: 1.03x faster                                                         |
| genshi_xml                 | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.44 sec: 1.03x faster                                                        |
| chaos                      | 58.0 ms                                                | 56.5 ms: 1.03x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.58 sec: 1.02x faster                                                        |
| scimark_fft                | 367 ms                                                 | 358 ms: 1.02x faster                                                          |
| django_template            | 31.7 ms                                                | 31.0 ms: 1.02x faster                                                         |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                          |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.96 ms: 1.01x faster                                                         |
| crypto_pyaes               | 74.7 ms                                                | 73.8 ms: 1.01x faster                                                         |
| docutils                   | 2.58 sec                                               | 2.56 sec: 1.01x faster                                                        |
| nqueens                    | 80.9 ms                                                | 80.1 ms: 1.01x faster                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 66.2 ms: 1.01x faster                                                         |
| raytrace                   | 262 ms                                                 | 260 ms: 1.01x faster                                                          |
| generators                 | 28.8 ms                                                | 28.9 ms: 1.00x slower                                                         |
| hexiom                     | 6.08 ms                                                | 6.11 ms: 1.00x slower                                                         |
| connected_components       | 447 ms                                                 | 453 ms: 1.01x slower                                                          |
| shortest_path              | 487 ms                                                 | 493 ms: 1.01x slower                                                          |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                                         |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                          |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                          |
| gc_traversal               | 4.90 ms                                                | 5.05 ms: 1.03x slower                                                         |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                         |
| coverage                   | 82.8 ms                                                | 86.8 ms: 1.05x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 317 us: 1.05x slower                                                          |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.05x slower                                                         |
| fannkuch                   | 394 ms                                                 | 417 ms: 1.06x slower                                                          |
| deltablue                  | 3.19 ms                                                | 3.39 ms: 1.06x slower                                                         |
| nbody                      | 87.7 ms                                                | 93.9 ms: 1.07x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 880 us: 1.08x slower                                                          |
| many_optionals             | 857 us                                                 | 923 us: 1.08x slower                                                          |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                         |
| json_loads                 | 27.2 us                                                | 30.1 us: 1.11x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                         |
| python_startup_no_site     | 7.00 ms                                                | 8.23 ms: 1.18x slower                                                         |
| subparsers                 | 15.5 ms                                                | 20.5 ms: 1.33x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 81.8 ms: 3.41x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                                  |

Benchmark hidden because not significant (4): typing_runtime_protocols, pidigits, asyncio_websockets, json
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250416-3.14.0a7+-a4b740d/bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x