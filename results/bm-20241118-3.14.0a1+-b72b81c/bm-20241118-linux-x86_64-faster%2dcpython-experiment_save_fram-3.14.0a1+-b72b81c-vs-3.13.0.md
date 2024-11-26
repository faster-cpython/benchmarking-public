# Results vs. 3.13.0

- fork: faster-cpython
- ref: experiment_save_fram
- machine: linux-x86_64
- commit hash: b72b81c
- commit date: 2024-11-18
- overall geometric mean: 1.004x faster
- HPT reliability: 54.32%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 256 ms: 1.04x faster                                                             |
| docutils       | 2.59 sec                                               | 2.70 sec: 1.04x slower                                                           |
| html5lib       | 64.2 ms                                                | 65.4 ms: 1.02x slower                                                            |
| sphinx         | 1.03 sec                                               | 1.06 sec: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 383 ms: 1.21x faster                                                             |
| async_tree_memoization     | 442 ms                                                 | 416 ms: 1.06x faster                                                             |
| async_tree_none            | 351 ms                                                 | 331 ms: 1.06x faster                                                             |
| async_generators           | 436 ms                                                 | 434 ms: 1.00x faster                                                             |
| coroutines                 | 22.7 ms                                                | 23.4 ms: 1.03x slower                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 575 ms: 1.05x slower                                                             |
| async_tree_io_tg           | 857 ms                                                 | 967 ms: 1.13x slower                                                             |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_cpu_io_mixed, async_tree_io, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                             |
| float          | 79.2 ms                                                | 80.0 ms: 1.01x slower                                                            |
| nbody          | 87.0 ms                                                | 96.7 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.2 ms: 1.08x faster                                                            |
| regex_effbot   | 3.73 ms                                                | 3.58 ms: 1.04x faster                                                            |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 2.10 sec: 1.02x faster                                                           |
| xml_etree_process    | 60.6 ms                                                | 60.1 ms: 1.01x faster                                                            |
| json_loads           | 27.2 us                                                | 27.1 us: 1.01x faster                                                            |
| unpickle_pure_python | 216 us                                                 | 218 us: 1.01x slower                                                             |
| xml_etree_parse      | 156 ms                                                 | 158 ms: 1.02x slower                                                             |
| xml_etree_iterparse  | 101 ms                                                 | 106 ms: 1.05x slower                                                             |
| pickle_pure_python   | 310 us                                                 | 326 us: 1.05x slower                                                             |
| json_dumps           | 10.6 ms                                                | 11.5 ms: 1.09x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                            |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 32.2 ms: 1.09x faster                                                            |
| genshi_text     | 23.5 ms                                                | 23.2 ms: 1.01x faster                                                            |
| genshi_xml      | 50.9 ms                                                | 51.3 ms: 1.01x slower                                                            |
| mako            | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 266 us: 1.35x faster                                                             |
| deepcopy_memo              | 39.1 us                                                | 30.2 us: 1.30x faster                                                            |
| async_tree_memoization_tg  | 464 ms                                                 | 383 ms: 1.21x faster                                                             |
| go                         | 144 ms                                                 | 119 ms: 1.21x faster                                                             |
| deepcopy_reduce            | 3.20 us                                                | 2.72 us: 1.17x faster                                                            |
| pathlib                    | 17.5 ms                                                | 16.0 ms: 1.10x faster                                                            |
| django_template            | 35.2 ms                                                | 32.2 ms: 1.09x faster                                                            |
| telco                      | 8.54 ms                                                | 7.82 ms: 1.09x faster                                                            |
| regex_v8                   | 26.2 ms                                                | 24.2 ms: 1.08x faster                                                            |
| json                       | 5.36 ms                                                | 5.03 ms: 1.07x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 416 ms: 1.06x faster                                                             |
| async_tree_none            | 351 ms                                                 | 331 ms: 1.06x faster                                                             |
| richards                   | 48.7 ms                                                | 46.4 ms: 1.05x faster                                                            |
| crypto_pyaes               | 75.3 ms                                                | 71.9 ms: 1.05x faster                                                            |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.05x faster                                                             |
| logging_format             | 6.40 us                                                | 6.14 us: 1.04x faster                                                            |
| generators                 | 29.0 ms                                                | 27.8 ms: 1.04x faster                                                            |
| regex_effbot               | 3.73 ms                                                | 3.58 ms: 1.04x faster                                                            |
| 2to3                       | 267 ms                                                 | 256 ms: 1.04x faster                                                             |
| richards_super             | 54.9 ms                                                | 52.8 ms: 1.04x faster                                                            |
| thrift                     | 809 us                                                 | 778 us: 1.04x faster                                                             |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                           |
| logging_simple             | 5.72 us                                                | 5.59 us: 1.02x faster                                                            |
| connected_components       | 444 ms                                                 | 434 ms: 1.02x faster                                                             |
| sympy_str                  | 275 ms                                                 | 269 ms: 1.02x faster                                                             |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                             |
| shortest_path              | 481 ms                                                 | 472 ms: 1.02x faster                                                             |
| mdp                        | 2.72 sec                                               | 2.67 sec: 1.02x faster                                                           |
| tomli_loads                | 2.14 sec                                               | 2.10 sec: 1.02x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                             |
| sympy_expand               | 463 ms                                                 | 457 ms: 1.02x faster                                                             |
| genshi_text                | 23.5 ms                                                | 23.2 ms: 1.01x faster                                                            |
| sqlalchemy_imperative      | 17.1 ms                                                | 16.9 ms: 1.01x faster                                                            |
| xml_etree_process          | 60.6 ms                                                | 60.1 ms: 1.01x faster                                                            |
| pprint_pformat             | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                           |
| pprint_safe_repr           | 728 ms                                                 | 724 ms: 1.01x faster                                                             |
| json_loads                 | 27.2 us                                                | 27.1 us: 1.01x faster                                                            |
| async_generators           | 436 ms                                                 | 434 ms: 1.00x faster                                                             |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                             |
| genshi_xml                 | 50.9 ms                                                | 51.3 ms: 1.01x slower                                                            |
| float                      | 79.2 ms                                                | 80.0 ms: 1.01x slower                                                            |
| sqlglot_transpile          | 1.58 ms                                                | 1.60 ms: 1.01x slower                                                            |
| python_startup_no_site     | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                            |
| deltablue                  | 3.23 ms                                                | 3.26 ms: 1.01x slower                                                            |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.01x slower                                                             |
| unpickle_pure_python       | 216 us                                                 | 218 us: 1.01x slower                                                             |
| meteor_contest             | 109 ms                                                 | 110 ms: 1.01x slower                                                             |
| dulwich_log                | 64.3 ms                                                | 65.3 ms: 1.01x slower                                                            |
| bpe_tokeniser              | 4.75 sec                                               | 4.82 sec: 1.02x slower                                                           |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.13 ms: 1.02x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.02x slower                                                            |
| xml_etree_parse            | 156 ms                                                 | 158 ms: 1.02x slower                                                             |
| html5lib                   | 64.2 ms                                                | 65.4 ms: 1.02x slower                                                            |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                            |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                             |
| sphinx                     | 1.03 sec                                               | 1.06 sec: 1.02x slower                                                           |
| raytrace                   | 267 ms                                                 | 274 ms: 1.03x slower                                                             |
| hexiom                     | 6.16 ms                                                | 6.33 ms: 1.03x slower                                                            |
| coroutines                 | 22.7 ms                                                | 23.4 ms: 1.03x slower                                                            |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                            |
| bench_thread_pool          | 822 us                                                 | 852 us: 1.04x slower                                                             |
| scimark_fft                | 364 ms                                                 | 379 ms: 1.04x slower                                                             |
| mako                       | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                            |
| nqueens                    | 78.4 ms                                                | 81.6 ms: 1.04x slower                                                            |
| docutils                   | 2.59 sec                                               | 2.70 sec: 1.04x slower                                                           |
| scimark_monte_carlo        | 67.4 ms                                                | 70.3 ms: 1.04x slower                                                            |
| scimark_lu                 | 113 ms                                                 | 118 ms: 1.04x slower                                                             |
| xml_etree_iterparse        | 101 ms                                                 | 106 ms: 1.05x slower                                                             |
| pickle_pure_python         | 310 us                                                 | 326 us: 1.05x slower                                                             |
| scimark_sor                | 124 ms                                                 | 130 ms: 1.05x slower                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 575 ms: 1.05x slower                                                             |
| chaos                      | 58.1 ms                                                | 61.6 ms: 1.06x slower                                                            |
| gc_traversal               | 4.37 ms                                                | 4.72 ms: 1.08x slower                                                            |
| json_dumps                 | 10.6 ms                                                | 11.5 ms: 1.09x slower                                                            |
| nbody                      | 87.0 ms                                                | 96.7 ms: 1.11x slower                                                            |
| create_gc_cycles           | 2.41 ms                                                | 2.70 ms: 1.12x slower                                                            |
| async_tree_io_tg           | 857 ms                                                 | 967 ms: 1.13x slower                                                             |
| k_core                     | 2.35 sec                                               | 3.60 sec: 1.53x slower                                                           |
| bench_mp_pool              | 24.0 ms                                                | 78.7 ms: 3.28x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (14): sqlglot_normalize, typing_runtime_protocols, pyflate, sqlglot_optimize, fannkuch, xml_etree_generate, coverage, sympy_integrate, regex_dna, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_io, async_tree_none_tg, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241118-3.14.0a1+-b72b81c/bm-20241118-linux-x86_64-faster%2dcpython-experiment_save_fram-3.14.0a1+-b72b81c.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.004x faster
# HPT report

- Reliability score: 54.32% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x