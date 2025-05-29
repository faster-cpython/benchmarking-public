# Results vs. 3.13.0

- fork: faster-cpython
- ref: tos_caching_1
- machine: linux-x86_64
- commit hash: 5bbc96e
- commit date: 2025-04-08
- overall geometric mean: 1.081x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 245 ms: 1.08x faster                                                      |
| html5lib       | 63.4 ms                                                | 58.5 ms: 1.08x faster                                                     |
| sphinx         | 1.03 sec                                               | 992 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 309 ms: 1.41x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                      |
| async_tree_io              | 838 ms                                                 | 605 ms: 1.39x faster                                                      |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                      |
| async_generators           | 433 ms                                                 | 386 ms: 1.12x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                      |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.04x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.9 ms: 1.18x faster                                                     |
| nbody          | 87.7 ms                                                | 82.1 ms: 1.07x faster                                                     |
| pidigits       | 186 ms                                                 | 202 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.06 ms: 1.23x faster                                                     |
| regex_v8       | 26.9 ms                                                | 22.3 ms: 1.20x faster                                                     |
| regex_dna      | 220 ms                                                 | 191 ms: 1.15x faster                                                      |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                  | 1.16x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                    |
| xml_etree_generate   | 86.8 ms                                                | 87.9 ms: 1.01x slower                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 103 ms: 1.02x slower                                                      |
| pickle_pure_python   | 302 us                                                 | 309 us: 1.02x slower                                                      |
| unpickle_pure_python | 213 us                                                 | 220 us: 1.03x slower                                                      |
| json_loads           | 27.2 us                                                | 28.3 us: 1.04x slower                                                     |
| xml_etree_parse      | 154 ms                                                 | 162 ms: 1.05x slower                                                      |
| json_dumps           | 10.1 ms                                                | 12.3 ms: 1.22x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                     |
| python_startup_no_site | 7.00 ms                                                | 8.12 ms: 1.16x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.0 ms: 1.08x faster                                                     |
| genshi_xml      | 50.5 ms                                                | 47.4 ms: 1.06x faster                                                     |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                     |
| mako            | 10.7 ms                                                | 11.6 ms: 1.09x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.21 sec: 2.10x faster                                                    |
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                      |
| deepcopy                   | 354 us                                                 | 247 us: 1.44x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 309 ms: 1.41x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                      |
| async_tree_io              | 838 ms                                                 | 605 ms: 1.39x faster                                                      |
| async_tree_none            | 350 ms                                                 | 257 ms: 1.36x faster                                                      |
| deepcopy_memo              | 38.4 us                                                | 29.1 us: 1.32x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 3.81 ms: 1.32x faster                                                     |
| go                         | 141 ms                                                 | 108 ms: 1.30x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.57 us: 1.26x faster                                                     |
| regex_effbot               | 3.77 ms                                                | 3.06 ms: 1.23x faster                                                     |
| spectral_norm              | 113 ms                                                 | 93.5 ms: 1.21x faster                                                     |
| scimark_fft                | 367 ms                                                 | 303 ms: 1.21x faster                                                      |
| regex_v8                   | 26.9 ms                                                | 22.3 ms: 1.20x faster                                                     |
| float                      | 78.7 ms                                                | 66.9 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                      |
| richards                   | 47.5 ms                                                | 41.1 ms: 1.16x faster                                                     |
| pyflate                    | 470 ms                                                 | 407 ms: 1.15x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                    |
| pathlib                    | 17.4 ms                                                | 15.1 ms: 1.15x faster                                                     |
| regex_dna                  | 220 ms                                                 | 191 ms: 1.15x faster                                                      |
| richards_super             | 53.7 ms                                                | 47.0 ms: 1.14x faster                                                     |
| scimark_monte_carlo        | 66.8 ms                                                | 58.6 ms: 1.14x faster                                                     |
| logging_silent             | 101 ns                                                 | 88.7 ns: 1.14x faster                                                     |
| telco                      | 8.40 ms                                                | 7.38 ms: 1.14x faster                                                     |
| pylint                     | 312 ms                                                 | 274 ms: 1.14x faster                                                      |
| async_generators           | 433 ms                                                 | 386 ms: 1.12x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                      |
| scimark_sor                | 122 ms                                                 | 109 ms: 1.12x faster                                                      |
| dulwich_log                | 64.6 ms                                                | 58.2 ms: 1.11x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.09 sec: 1.10x faster                                                    |
| sqlite_synth               | 2.90 us                                                | 2.66 us: 1.09x faster                                                     |
| 2to3                       | 266 ms                                                 | 245 ms: 1.08x faster                                                      |
| html5lib                   | 63.4 ms                                                | 58.5 ms: 1.08x faster                                                     |
| genshi_text                | 22.6 ms                                                | 21.0 ms: 1.08x faster                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.35 sec: 1.08x faster                                                    |
| sympy_integrate            | 19.8 ms                                                | 18.6 ms: 1.07x faster                                                     |
| nbody                      | 87.7 ms                                                | 82.1 ms: 1.07x faster                                                     |
| genshi_xml                 | 50.5 ms                                                | 47.4 ms: 1.06x faster                                                     |
| chaos                      | 58.0 ms                                                | 54.6 ms: 1.06x faster                                                     |
| deltablue                  | 3.19 ms                                                | 3.01 ms: 1.06x faster                                                     |
| comprehensions             | 16.5 us                                                | 15.6 us: 1.06x faster                                                     |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                      |
| crypto_pyaes               | 74.7 ms                                                | 71.7 ms: 1.04x faster                                                     |
| sphinx                     | 1.03 sec                                               | 992 ms: 1.04x faster                                                      |
| raytrace                   | 262 ms                                                 | 252 ms: 1.04x faster                                                      |
| hexiom                     | 6.08 ms                                                | 5.86 ms: 1.04x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                      |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                    |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                      |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                                      |
| generators                 | 28.8 ms                                                | 28.0 ms: 1.03x faster                                                     |
| nqueens                    | 80.9 ms                                                | 78.8 ms: 1.03x faster                                                     |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.5 ms: 1.02x faster                                                     |
| typing_runtime_protocols   | 160 us                                                 | 157 us: 1.02x faster                                                      |
| logging_simple             | 5.65 us                                                | 5.53 us: 1.02x faster                                                     |
| logging_format             | 6.23 us                                                | 6.11 us: 1.02x faster                                                     |
| json                       | 5.32 ms                                                | 5.24 ms: 1.02x faster                                                     |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.01x faster                                                      |
| coverage                   | 82.8 ms                                                | 82.1 ms: 1.01x faster                                                     |
| sympy_expand               | 456 ms                                                 | 455 ms: 1.00x faster                                                      |
| fannkuch                   | 394 ms                                                 | 396 ms: 1.01x slower                                                      |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                     |
| gc_traversal               | 4.90 ms                                                | 4.94 ms: 1.01x slower                                                     |
| xml_etree_generate         | 86.8 ms                                                | 87.9 ms: 1.01x slower                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 103 ms: 1.02x slower                                                      |
| shortest_path              | 487 ms                                                 | 496 ms: 1.02x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 309 us: 1.02x slower                                                      |
| create_gc_cycles           | 2.45 ms                                                | 2.51 ms: 1.02x slower                                                     |
| python_startup             | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                     |
| unpickle_pure_python       | 213 us                                                 | 220 us: 1.03x slower                                                      |
| connected_components       | 447 ms                                                 | 463 ms: 1.04x slower                                                      |
| bench_thread_pool          | 818 us                                                 | 848 us: 1.04x slower                                                      |
| json_loads                 | 27.2 us                                                | 28.3 us: 1.04x slower                                                     |
| pprint_safe_repr           | 727 ms                                                 | 758 ms: 1.04x slower                                                      |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.04x slower                                                     |
| pprint_pformat             | 1.48 sec                                               | 1.56 sec: 1.05x slower                                                    |
| xml_etree_parse            | 154 ms                                                 | 162 ms: 1.05x slower                                                      |
| many_optionals             | 857 us                                                 | 921 us: 1.07x slower                                                      |
| pidigits                   | 186 ms                                                 | 202 ms: 1.08x slower                                                      |
| mako                       | 10.7 ms                                                | 11.6 ms: 1.09x slower                                                     |
| python_startup_no_site     | 7.00 ms                                                | 8.12 ms: 1.16x slower                                                     |
| json_dumps                 | 10.1 ms                                                | 12.3 ms: 1.22x slower                                                     |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.33x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 80.9 ms: 3.38x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (4): meteor_contest, docutils, asyncio_websockets, xml_etree_process
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250408-3.14.0a6+-5bbc96e-CLANG/bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.081x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x