# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: py_likely_unlikely
- machine: linux-x86_64
- commit hash: 2b26797
- commit date: 2025-01-29
- overall geometric mean: 1.045x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 252 ms: 1.05x faster                                                           |
| html5lib       | 63.4 ms                                                | 61.1 ms: 1.04x faster                                                          |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                           |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                           |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                           |
| async_tree_memoization     | 437 ms                                                 | 331 ms: 1.32x faster                                                           |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                           |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                           |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                           |
| async_generators           | 433 ms                                                 | 387 ms: 1.12x faster                                                           |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.07x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.6 ms: 1.11x faster                                                          |
| nbody          | 87.7 ms                                                | 93.0 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.38 ms: 1.11x faster                                                          |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                           |
| regex_v8       | 26.9 ms                                                | 26.0 ms: 1.03x faster                                                          |
| regex_dna      | 220 ms                                                 | 213 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                           |
| tomli_loads          | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 83.9 ms: 1.03x faster                                                          |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                                          |
| xml_etree_process    | 60.5 ms                                                | 59.0 ms: 1.02x faster                                                          |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                           |
| pickle_pure_python   | 302 us                                                 | 314 us: 1.04x slower                                                           |
| json_loads           | 27.2 us                                                | 29.1 us: 1.07x slower                                                          |
| json_dumps           | 10.1 ms                                                | 11.9 ms: 1.18x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                          |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.7 ms: 1.04x faster                                                          |
| genshi_xml      | 50.5 ms                                                | 48.4 ms: 1.04x faster                                                          |
| django_template | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                          |
| mako            | 10.7 ms                                                | 11.4 ms: 1.06x slower                                                          |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-Fidget%2dSpinner-py_likely_unlikely-3.14.0a4+-2b26797 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                           |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                           |
| deepcopy                   | 354 us                                                 | 256 us: 1.38x faster                                                           |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                           |
| async_tree_memoization     | 437 ms                                                 | 331 ms: 1.32x faster                                                           |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                           |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                           |
| deepcopy_memo              | 38.4 us                                                | 30.8 us: 1.25x faster                                                          |
| deepcopy_reduce            | 3.24 us                                                | 2.62 us: 1.24x faster                                                          |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                                           |
| spectral_norm              | 113 ms                                                 | 94.9 ms: 1.19x faster                                                          |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.15x faster                                                           |
| pylint                     | 312 ms                                                 | 274 ms: 1.14x faster                                                           |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                           |
| async_generators           | 433 ms                                                 | 387 ms: 1.12x faster                                                           |
| float                      | 78.7 ms                                                | 70.6 ms: 1.11x faster                                                          |
| regex_effbot               | 3.77 ms                                                | 3.38 ms: 1.11x faster                                                          |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                           |
| richards                   | 47.5 ms                                                | 43.8 ms: 1.08x faster                                                          |
| telco                      | 8.40 ms                                                | 7.80 ms: 1.08x faster                                                          |
| gc_traversal               | 4.90 ms                                                | 4.57 ms: 1.07x faster                                                          |
| richards_super             | 53.7 ms                                                | 50.2 ms: 1.07x faster                                                          |
| tomli_loads                | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                         |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                                          |
| scimark_fft                | 367 ms                                                 | 347 ms: 1.06x faster                                                           |
| 2to3                       | 266 ms                                                 | 252 ms: 1.05x faster                                                           |
| crypto_pyaes               | 74.7 ms                                                | 71.4 ms: 1.05x faster                                                          |
| genshi_text                | 22.6 ms                                                | 21.7 ms: 1.04x faster                                                          |
| genshi_xml                 | 50.5 ms                                                | 48.4 ms: 1.04x faster                                                          |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                         |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                           |
| generators                 | 28.8 ms                                                | 27.7 ms: 1.04x faster                                                          |
| bpe_tokeniser              | 4.69 sec                                               | 4.52 sec: 1.04x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                          |
| thrift                     | 800 us                                                 | 771 us: 1.04x faster                                                           |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.3 ms: 1.04x faster                                                          |
| html5lib                   | 63.4 ms                                                | 61.1 ms: 1.04x faster                                                          |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.04x faster                                                           |
| xml_etree_generate         | 86.8 ms                                                | 83.9 ms: 1.03x faster                                                          |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.86 ms: 1.03x faster                                                          |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                           |
| regex_v8                   | 26.9 ms                                                | 26.0 ms: 1.03x faster                                                          |
| regex_dna                  | 220 ms                                                 | 213 ms: 1.03x faster                                                           |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                                          |
| mdp                        | 2.54 sec                                               | 2.47 sec: 1.03x faster                                                         |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                           |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.03x faster                                                           |
| logging_simple             | 5.65 us                                                | 5.51 us: 1.03x faster                                                          |
| pyflate                    | 470 ms                                                 | 458 ms: 1.03x faster                                                           |
| xml_etree_process          | 60.5 ms                                                | 59.0 ms: 1.02x faster                                                          |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                         |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                         |
| connected_components       | 447 ms                                                 | 437 ms: 1.02x faster                                                           |
| shortest_path              | 487 ms                                                 | 477 ms: 1.02x faster                                                           |
| logging_format             | 6.23 us                                                | 6.13 us: 1.02x faster                                                          |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                                         |
| pprint_safe_repr           | 727 ms                                                 | 717 ms: 1.01x faster                                                           |
| sqlglot_optimize           | 53.4 ms                                                | 52.7 ms: 1.01x faster                                                          |
| json                       | 5.32 ms                                                | 5.26 ms: 1.01x faster                                                          |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                                          |
| sympy_expand               | 456 ms                                                 | 451 ms: 1.01x faster                                                           |
| dulwich_log                | 64.6 ms                                                | 64.0 ms: 1.01x faster                                                          |
| sqlglot_parse              | 1.26 ms                                                | 1.25 ms: 1.01x faster                                                          |
| sqlglot_transpile          | 1.57 ms                                                | 1.56 ms: 1.01x faster                                                          |
| create_gc_cycles           | 2.45 ms                                                | 2.44 ms: 1.00x faster                                                          |
| python_startup_no_site     | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                          |
| chaos                      | 58.0 ms                                                | 58.3 ms: 1.00x slower                                                          |
| deltablue                  | 3.19 ms                                                | 3.22 ms: 1.01x slower                                                          |
| scimark_monte_carlo        | 66.8 ms                                                | 67.4 ms: 1.01x slower                                                          |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                          |
| django_template            | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                          |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                                           |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                           |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                          |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                           |
| hexiom                     | 6.08 ms                                                | 6.19 ms: 1.02x slower                                                          |
| fannkuch                   | 394 ms                                                 | 402 ms: 1.02x slower                                                           |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                           |
| pickle_pure_python         | 302 us                                                 | 314 us: 1.04x slower                                                           |
| logging_silent             | 101 ns                                                 | 105 ns: 1.04x slower                                                           |
| bench_thread_pool          | 818 us                                                 | 863 us: 1.06x slower                                                           |
| nbody                      | 87.7 ms                                                | 93.0 ms: 1.06x slower                                                          |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.06x slower                                                          |
| json_loads                 | 27.2 us                                                | 29.1 us: 1.07x slower                                                          |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.07x slower                                                          |
| many_optionals             | 857 us                                                 | 937 us: 1.09x slower                                                           |
| coverage                   | 82.8 ms                                                | 90.9 ms: 1.10x slower                                                          |
| json_dumps                 | 10.1 ms                                                | 11.9 ms: 1.18x slower                                                          |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.34x slower                                                          |
| bench_mp_pool              | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                   |

Benchmark hidden because not significant (5): docutils, pidigits, asyncio_websockets, nqueens, scimark_sor
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x