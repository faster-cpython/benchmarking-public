# Results vs. 3.13.0

- fork: faster-cpython
- ref: no_conditional_stack
- machine: linux-x86_64
- commit hash: d5e47ea
- commit date: 2025-01-20
- overall geometric mean: 1.105x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 313 ms: 1.18x slower                                                             |
| docutils       | 2.58 sec                                               | 2.87 sec: 1.11x slower                                                           |
| html5lib       | 63.4 ms                                                | 71.2 ms: 1.12x slower                                                            |
| sphinx         | 1.03 sec                                               | 1.15 sec: 1.12x slower                                                           |
| Geometric mean | (ref)                                                  | 1.13x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 551 ms: 1.56x faster                                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                             |
| async_tree_io              | 838 ms                                                 | 606 ms: 1.38x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 241 ms: 1.33x faster                                                             |
| async_tree_none            | 350 ms                                                 | 292 ms: 1.20x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 372 ms: 1.18x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 469 ms: 1.16x faster                                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 523 ms: 1.10x faster                                                             |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                                             |
| coroutines                 | 22.2 ms                                                | 25.5 ms: 1.15x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 78.9 ms: 1.00x slower                                                            |
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                                             |
| nbody          | 87.7 ms                                                | 139 ms: 1.58x slower                                                             |
| Geometric mean | (ref)                                                  | 1.17x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.36 ms: 1.12x faster                                                            |
| regex_v8       | 26.9 ms                                                | 25.0 ms: 1.08x faster                                                            |
| regex_dna      | 220 ms                                                 | 223 ms: 1.02x slower                                                             |
| regex_compile  | 132 ms                                                 | 153 ms: 1.16x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 96.4 ms: 1.05x faster                                                            |
| xml_etree_parse      | 154 ms                                                 | 150 ms: 1.03x faster                                                             |
| xml_etree_generate   | 86.8 ms                                                | 96.8 ms: 1.12x slower                                                            |
| tomli_loads          | 2.12 sec                                               | 2.45 sec: 1.16x slower                                                           |
| json_loads           | 27.2 us                                                | 31.7 us: 1.17x slower                                                            |
| xml_etree_process    | 60.5 ms                                                | 72.1 ms: 1.19x slower                                                            |
| json_dumps           | 10.1 ms                                                | 12.8 ms: 1.26x slower                                                            |
| pickle_pure_python   | 302 us                                                 | 382 us: 1.26x slower                                                             |
| unpickle_pure_python | 213 us                                                 | 273 us: 1.28x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.15x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.1 ms: 1.19x slower                                                            |
| python_startup_no_site | 7.00 ms                                                | 9.37 ms: 1.34x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 62.8 ms: 1.24x slower                                                            |
| genshi_text     | 22.6 ms                                                | 29.3 ms: 1.30x slower                                                            |
| django_template | 31.7 ms                                                | 41.7 ms: 1.32x slower                                                            |
| mako            | 10.7 ms                                                | 16.5 ms: 1.54x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.35x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 551 ms: 1.56x faster                                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                             |
| create_gc_cycles           | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                            |
| async_tree_io              | 838 ms                                                 | 606 ms: 1.38x faster                                                             |
| async_tree_none_tg         | 319 ms                                                 | 241 ms: 1.33x faster                                                             |
| async_tree_none            | 350 ms                                                 | 292 ms: 1.20x faster                                                             |
| async_tree_memoization     | 437 ms                                                 | 372 ms: 1.18x faster                                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 469 ms: 1.16x faster                                                             |
| regex_effbot               | 3.77 ms                                                | 3.36 ms: 1.12x faster                                                            |
| deepcopy                   | 354 us                                                 | 319 us: 1.11x faster                                                             |
| gc_traversal               | 4.90 ms                                                | 4.44 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 523 ms: 1.10x faster                                                             |
| regex_v8                   | 26.9 ms                                                | 25.0 ms: 1.08x faster                                                            |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                                            |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.05x faster                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 96.4 ms: 1.05x faster                                                            |
| xml_etree_parse            | 154 ms                                                 | 150 ms: 1.03x faster                                                             |
| float                      | 78.7 ms                                                | 78.9 ms: 1.00x slower                                                            |
| deepcopy_reduce            | 3.24 us                                                | 3.26 us: 1.01x slower                                                            |
| async_generators           | 433 ms                                                 | 437 ms: 1.01x slower                                                             |
| pycparser                  | 1.20 sec                                               | 1.21 sec: 1.01x slower                                                           |
| regex_dna                  | 220 ms                                                 | 223 ms: 1.02x slower                                                             |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                                             |
| go                         | 141 ms                                                 | 145 ms: 1.03x slower                                                             |
| k_core                     | 2.37 sec                                               | 2.44 sec: 1.03x slower                                                           |
| deepcopy_memo              | 38.4 us                                                | 39.7 us: 1.03x slower                                                            |
| json                       | 5.32 ms                                                | 5.58 ms: 1.05x slower                                                            |
| spectral_norm              | 113 ms                                                 | 119 ms: 1.05x slower                                                             |
| bpe_tokeniser              | 4.69 sec                                               | 5.04 sec: 1.07x slower                                                           |
| mdp                        | 2.54 sec                                               | 2.73 sec: 1.07x slower                                                           |
| telco                      | 8.40 ms                                                | 9.21 ms: 1.10x slower                                                            |
| generators                 | 28.8 ms                                                | 31.6 ms: 1.10x slower                                                            |
| dulwich_log                | 64.6 ms                                                | 71.3 ms: 1.10x slower                                                            |
| docutils                   | 2.58 sec                                               | 2.87 sec: 1.11x slower                                                           |
| pyflate                    | 470 ms                                                 | 521 ms: 1.11x slower                                                             |
| xml_etree_generate         | 86.8 ms                                                | 96.8 ms: 1.12x slower                                                            |
| sphinx                     | 1.03 sec                                               | 1.15 sec: 1.12x slower                                                           |
| html5lib                   | 63.4 ms                                                | 71.2 ms: 1.12x slower                                                            |
| sqlglot_normalize          | 108 ms                                                 | 122 ms: 1.13x slower                                                             |
| coroutines                 | 22.2 ms                                                | 25.5 ms: 1.15x slower                                                            |
| richards                   | 47.5 ms                                                | 54.9 ms: 1.15x slower                                                            |
| tomli_loads                | 2.12 sec                                               | 2.45 sec: 1.16x slower                                                           |
| regex_compile              | 132 ms                                                 | 153 ms: 1.16x slower                                                             |
| scimark_fft                | 367 ms                                                 | 425 ms: 1.16x slower                                                             |
| scimark_sor                | 122 ms                                                 | 141 ms: 1.16x slower                                                             |
| sqlglot_optimize           | 53.4 ms                                                | 62.0 ms: 1.16x slower                                                            |
| json_loads                 | 27.2 us                                                | 31.7 us: 1.17x slower                                                            |
| shortest_path              | 487 ms                                                 | 573 ms: 1.18x slower                                                             |
| 2to3                       | 266 ms                                                 | 313 ms: 1.18x slower                                                             |
| sympy_str                  | 273 ms                                                 | 323 ms: 1.18x slower                                                             |
| sympy_expand               | 456 ms                                                 | 541 ms: 1.19x slower                                                             |
| connected_components       | 447 ms                                                 | 530 ms: 1.19x slower                                                             |
| python_startup             | 12.7 ms                                                | 15.1 ms: 1.19x slower                                                            |
| richards_super             | 53.7 ms                                                | 64.0 ms: 1.19x slower                                                            |
| logging_silent             | 101 ns                                                 | 120 ns: 1.19x slower                                                             |
| pprint_safe_repr           | 727 ms                                                 | 866 ms: 1.19x slower                                                             |
| xml_etree_process          | 60.5 ms                                                | 72.1 ms: 1.19x slower                                                            |
| sympy_sum                  | 150 ms                                                 | 180 ms: 1.19x slower                                                             |
| thrift                     | 800 us                                                 | 963 us: 1.20x slower                                                             |
| pprint_pformat             | 1.48 sec                                               | 1.79 sec: 1.21x slower                                                           |
| crypto_pyaes               | 74.7 ms                                                | 90.7 ms: 1.21x slower                                                            |
| sympy_integrate            | 19.8 ms                                                | 24.1 ms: 1.22x slower                                                            |
| meteor_contest             | 108 ms                                                 | 132 ms: 1.22x slower                                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.13 ms: 1.22x slower                                                            |
| nqueens                    | 80.9 ms                                                | 99.1 ms: 1.22x slower                                                            |
| scimark_lu                 | 114 ms                                                 | 141 ms: 1.23x slower                                                             |
| sqlalchemy_declarative     | 133 ms                                                 | 164 ms: 1.23x slower                                                             |
| sqlglot_transpile          | 1.57 ms                                                | 1.94 ms: 1.24x slower                                                            |
| logging_simple             | 5.65 us                                                | 7.01 us: 1.24x slower                                                            |
| genshi_xml                 | 50.5 ms                                                | 62.8 ms: 1.24x slower                                                            |
| json_dumps                 | 10.1 ms                                                | 12.8 ms: 1.26x slower                                                            |
| pickle_pure_python         | 302 us                                                 | 382 us: 1.26x slower                                                             |
| sqlglot_parse              | 1.26 ms                                                | 1.60 ms: 1.27x slower                                                            |
| sqlalchemy_imperative      | 16.9 ms                                                | 21.5 ms: 1.27x slower                                                            |
| unpickle_pure_python       | 213 us                                                 | 273 us: 1.28x slower                                                             |
| chaos                      | 58.0 ms                                                | 74.3 ms: 1.28x slower                                                            |
| logging_format             | 6.23 us                                                | 8.02 us: 1.29x slower                                                            |
| comprehensions             | 16.5 us                                                | 21.2 us: 1.29x slower                                                            |
| hexiom                     | 6.08 ms                                                | 7.83 ms: 1.29x slower                                                            |
| many_optionals             | 857 us                                                 | 1.11 ms: 1.29x slower                                                            |
| coverage                   | 82.8 ms                                                | 107 ms: 1.29x slower                                                             |
| genshi_text                | 22.6 ms                                                | 29.3 ms: 1.30x slower                                                            |
| django_template            | 31.7 ms                                                | 41.7 ms: 1.32x slower                                                            |
| scimark_monte_carlo        | 66.8 ms                                                | 88.1 ms: 1.32x slower                                                            |
| fannkuch                   | 394 ms                                                 | 521 ms: 1.32x slower                                                             |
| python_startup_no_site     | 7.00 ms                                                | 9.37 ms: 1.34x slower                                                            |
| typing_runtime_protocols   | 160 us                                                 | 216 us: 1.35x slower                                                             |
| raytrace                   | 262 ms                                                 | 360 ms: 1.38x slower                                                             |
| deltablue                  | 3.19 ms                                                | 4.77 ms: 1.49x slower                                                            |
| mako                       | 10.7 ms                                                | 16.5 ms: 1.54x slower                                                            |
| nbody                      | 87.7 ms                                                | 139 ms: 1.58x slower                                                             |
| subparsers                 | 15.5 ms                                                | 25.0 ms: 1.62x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 89.8 ms: 3.75x slower                                                            |
| bench_thread_pool          | 818 us                                                 | 3.49 ms: 4.27x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.15x slower                                                                     |

Benchmark hidden because not significant (2): asyncio_websockets, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.105x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 1.22x