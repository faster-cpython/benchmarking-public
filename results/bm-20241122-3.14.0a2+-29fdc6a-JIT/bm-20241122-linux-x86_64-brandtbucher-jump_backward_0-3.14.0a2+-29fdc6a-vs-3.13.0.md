# Results vs. 3.13.0

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: 29fdc6a
- commit date: 2024-11-22
- overall geometric mean: 1.020x slower
- HPT reliability: 97.05%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 268 ms: 1.00x slower                                                    |
| docutils       | 2.59 sec                                               | 3.02 sec: 1.17x slower                                                  |
| html5lib       | 64.2 ms                                                | 67.2 ms: 1.05x slower                                                   |
| sphinx         | 1.03 sec                                               | 1.15 sec: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 412 ms: 1.12x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 423 ms: 1.04x faster                                                    |
| async_tree_none            | 351 ms                                                 | 338 ms: 1.04x faster                                                    |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 586 ms: 1.07x slower                                                    |
| async_tree_io_tg           | 857 ms                                                 | 927 ms: 1.08x slower                                                    |
| async_tree_io              | 842 ms                                                 | 939 ms: 1.12x slower                                                    |
| coroutines                 | 22.7 ms                                                | 27.1 ms: 1.19x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                            |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 82.8 ms: 1.05x faster                                                   |
| float          | 79.2 ms                                                | 77.4 ms: 1.02x faster                                                   |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.45 ms: 1.08x faster                                                   |
| regex_v8       | 26.2 ms                                                | 25.7 ms: 1.02x faster                                                   |
| regex_dna      | 218 ms                                                 | 225 ms: 1.03x slower                                                    |
| regex_compile  | 132 ms                                                 | 137 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|--------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads        | 2.14 sec                                               | 1.97 sec: 1.09x faster                                                  |
| json_loads         | 27.2 us                                                | 26.0 us: 1.05x faster                                                   |
| xml_etree_parse    | 156 ms                                                 | 149 ms: 1.05x faster                                                    |
| xml_etree_generate | 86.7 ms                                                | 83.8 ms: 1.03x faster                                                   |
| xml_etree_process  | 60.6 ms                                                | 59.6 ms: 1.02x faster                                                   |
| pickle_pure_python | 310 us                                                 | 324 us: 1.04x slower                                                    |
| json_dumps         | 10.6 ms                                                | 11.3 ms: 1.07x slower                                                   |
| Geometric mean     | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                   |
| python_startup         | 12.5 ms                                                | 12.9 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.6 ms: 1.05x faster                                                   |
| django_template | 35.2 ms                                                | 36.2 ms: 1.03x slower                                                   |
| genshi_text     | 23.5 ms                                                | 24.3 ms: 1.03x slower                                                   |
| genshi_xml      | 50.9 ms                                                | 58.2 ms: 1.14x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 29.6 us: 1.32x faster                                                   |
| deepcopy                   | 358 us                                                 | 277 us: 1.29x faster                                                    |
| scimark_fft                | 364 ms                                                 | 316 ms: 1.15x faster                                                    |
| telco                      | 8.54 ms                                                | 7.46 ms: 1.14x faster                                                   |
| async_tree_memoization_tg  | 464 ms                                                 | 412 ms: 1.12x faster                                                    |
| go                         | 144 ms                                                 | 129 ms: 1.11x faster                                                    |
| json                       | 5.36 ms                                                | 4.84 ms: 1.11x faster                                                   |
| crypto_pyaes               | 75.3 ms                                                | 68.1 ms: 1.11x faster                                                   |
| deepcopy_reduce            | 3.20 us                                                | 2.90 us: 1.10x faster                                                   |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.58 ms: 1.10x faster                                                   |
| tomli_loads                | 2.14 sec                                               | 1.97 sec: 1.09x faster                                                  |
| regex_effbot               | 3.73 ms                                                | 3.45 ms: 1.08x faster                                                   |
| scimark_monte_carlo        | 67.4 ms                                                | 62.4 ms: 1.08x faster                                                   |
| pathlib                    | 17.5 ms                                                | 16.4 ms: 1.07x faster                                                   |
| nbody                      | 87.0 ms                                                | 82.8 ms: 1.05x faster                                                   |
| json_loads                 | 27.2 us                                                | 26.0 us: 1.05x faster                                                   |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.05x faster                                                    |
| mako                       | 11.1 ms                                                | 10.6 ms: 1.05x faster                                                   |
| async_tree_memoization     | 442 ms                                                 | 423 ms: 1.04x faster                                                    |
| richards                   | 48.7 ms                                                | 46.7 ms: 1.04x faster                                                   |
| richards_super             | 54.9 ms                                                | 52.7 ms: 1.04x faster                                                   |
| fannkuch                   | 404 ms                                                 | 389 ms: 1.04x faster                                                    |
| bpe_tokeniser              | 4.75 sec                                               | 4.57 sec: 1.04x faster                                                  |
| async_tree_none            | 351 ms                                                 | 338 ms: 1.04x faster                                                    |
| xml_etree_generate         | 86.7 ms                                                | 83.8 ms: 1.03x faster                                                   |
| mdp                        | 2.72 sec                                               | 2.64 sec: 1.03x faster                                                  |
| float                      | 79.2 ms                                                | 77.4 ms: 1.02x faster                                                   |
| regex_v8                   | 26.2 ms                                                | 25.7 ms: 1.02x faster                                                   |
| xml_etree_process          | 60.6 ms                                                | 59.6 ms: 1.02x faster                                                   |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.01x faster                                                    |
| connected_components       | 444 ms                                                 | 440 ms: 1.01x faster                                                    |
| scimark_sor                | 124 ms                                                 | 123 ms: 1.01x faster                                                    |
| pyflate                    | 471 ms                                                 | 468 ms: 1.01x faster                                                    |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| 2to3                       | 267 ms                                                 | 268 ms: 1.00x slower                                                    |
| shortest_path              | 481 ms                                                 | 483 ms: 1.01x slower                                                    |
| scimark_lu                 | 113 ms                                                 | 114 ms: 1.01x slower                                                    |
| pprint_pformat             | 1.49 sec                                               | 1.52 sec: 1.01x slower                                                  |
| python_startup_no_site     | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                   |
| thrift                     | 809 us                                                 | 825 us: 1.02x slower                                                    |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.02x slower                                                    |
| pprint_safe_repr           | 728 ms                                                 | 744 ms: 1.02x slower                                                    |
| regex_dna                  | 218 ms                                                 | 225 ms: 1.03x slower                                                    |
| django_template            | 35.2 ms                                                | 36.2 ms: 1.03x slower                                                   |
| genshi_text                | 23.5 ms                                                | 24.3 ms: 1.03x slower                                                   |
| python_startup             | 12.5 ms                                                | 12.9 ms: 1.03x slower                                                   |
| regex_compile              | 132 ms                                                 | 137 ms: 1.03x slower                                                    |
| gc_traversal               | 4.37 ms                                                | 4.52 ms: 1.03x slower                                                   |
| typing_runtime_protocols   | 165 us                                                 | 171 us: 1.04x slower                                                    |
| pickle_pure_python         | 310 us                                                 | 324 us: 1.04x slower                                                    |
| coverage                   | 84.0 ms                                                | 87.9 ms: 1.05x slower                                                   |
| html5lib                   | 64.2 ms                                                | 67.2 ms: 1.05x slower                                                   |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                    |
| chaos                      | 58.1 ms                                                | 61.8 ms: 1.06x slower                                                   |
| json_dumps                 | 10.6 ms                                                | 11.3 ms: 1.07x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.7 us: 1.07x slower                                                   |
| dulwich_log                | 64.3 ms                                                | 69.0 ms: 1.07x slower                                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 586 ms: 1.07x slower                                                    |
| sympy_expand               | 463 ms                                                 | 501 ms: 1.08x slower                                                    |
| sympy_str                  | 275 ms                                                 | 297 ms: 1.08x slower                                                    |
| async_tree_io_tg           | 857 ms                                                 | 927 ms: 1.08x slower                                                    |
| sqlglot_normalize          | 108 ms                                                 | 117 ms: 1.09x slower                                                    |
| raytrace                   | 267 ms                                                 | 294 ms: 1.10x slower                                                    |
| create_gc_cycles           | 2.41 ms                                                | 2.66 ms: 1.10x slower                                                   |
| sqlglot_optimize           | 53.7 ms                                                | 59.4 ms: 1.10x slower                                                   |
| sphinx                     | 1.03 sec                                               | 1.15 sec: 1.11x slower                                                  |
| async_tree_io              | 842 ms                                                 | 939 ms: 1.12x slower                                                    |
| bench_thread_pool          | 822 us                                                 | 923 us: 1.12x slower                                                    |
| sympy_integrate            | 19.9 ms                                                | 22.4 ms: 1.13x slower                                                   |
| sqlglot_parse              | 1.27 ms                                                | 1.43 ms: 1.13x slower                                                   |
| sqlglot_transpile          | 1.58 ms                                                | 1.80 ms: 1.14x slower                                                   |
| genshi_xml                 | 50.9 ms                                                | 58.2 ms: 1.14x slower                                                   |
| nqueens                    | 78.4 ms                                                | 90.8 ms: 1.16x slower                                                   |
| docutils                   | 2.59 sec                                               | 3.02 sec: 1.17x slower                                                  |
| logging_format             | 6.40 us                                                | 7.46 us: 1.17x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 178 ms: 1.18x slower                                                    |
| sqlalchemy_imperative      | 17.1 ms                                                | 20.2 ms: 1.19x slower                                                   |
| coroutines                 | 22.7 ms                                                | 27.1 ms: 1.19x slower                                                   |
| logging_simple             | 5.72 us                                                | 6.84 us: 1.20x slower                                                   |
| hexiom                     | 6.16 ms                                                | 7.40 ms: 1.20x slower                                                   |
| deltablue                  | 3.23 ms                                                | 3.93 ms: 1.22x slower                                                   |
| k_core                     | 2.35 sec                                               | 2.92 sec: 1.24x slower                                                  |
| generators                 | 29.0 ms                                                | 36.9 ms: 1.27x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 79.4 ms: 3.31x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                            |

Benchmark hidden because not significant (9): pylint, pycparser, sqlalchemy_declarative, unpickle_pure_python, logging_silent, asyncio_websockets, xml_etree_iterparse, async_tree_cpu_io_mixed, async_tree_none_tg
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241122-3.14.0a2+-29fdc6a-JIT/bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.020x slower
# HPT report

- Reliability score: 97.05% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x