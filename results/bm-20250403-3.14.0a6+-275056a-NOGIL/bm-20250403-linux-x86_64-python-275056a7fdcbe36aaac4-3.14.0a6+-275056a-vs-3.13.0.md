# Results vs. 3.13.0

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: linux-x86_64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.030x slower
- HPT reliability: 99.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 287 ms: 1.08x slower                                                   |
| docutils       | 2.58 sec                                               | 2.78 sec: 1.08x slower                                                 |
| html5lib       | 63.4 ms                                                | 67.2 ms: 1.06x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.11 sec: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 508 ms: 1.69x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 295 ms: 1.57x faster                                                   |
| async_tree_io              | 838 ms                                                 | 547 ms: 1.53x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 223 ms: 1.43x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 331 ms: 1.32x faster                                                   |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 449 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                   |
| async_generators           | 433 ms                                                 | 423 ms: 1.03x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.27x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.4 ms: 1.15x faster                                                  |
| pidigits       | 186 ms                                                 | 184 ms: 1.01x faster                                                   |
| nbody          | 87.7 ms                                                | 119 ms: 1.36x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.23 ms: 1.17x faster                                                  |
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                  |
| regex_compile  | 132 ms                                                 | 145 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 94.0 ms: 1.08x faster                                                  |
| xml_etree_parse      | 154 ms                                                 | 147 ms: 1.05x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 2.17 sec: 1.02x slower                                                 |
| xml_etree_generate   | 86.8 ms                                                | 93.5 ms: 1.08x slower                                                  |
| xml_etree_process    | 60.5 ms                                                | 65.5 ms: 1.08x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 240 us: 1.13x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 345 us: 1.14x slower                                                   |
| json_loads           | 27.2 us                                                | 32.0 us: 1.18x slower                                                  |
| json_dumps           | 10.1 ms                                                | 12.8 ms: 1.27x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.6 ms: 1.23x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 10.9 ms: 1.56x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.39x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 57.5 ms: 1.14x slower                                                  |
| genshi_text     | 22.6 ms                                                | 26.7 ms: 1.18x slower                                                  |
| django_template | 31.7 ms                                                | 38.5 ms: 1.22x slower                                                  |
| mako            | 10.7 ms                                                | 15.6 ms: 1.46x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.24x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 2.03 ms: 2.41x faster                                                  |
| mdp                        | 2.54 sec                                               | 1.38 sec: 1.84x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 508 ms: 1.69x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 295 ms: 1.57x faster                                                   |
| async_tree_io              | 838 ms                                                 | 547 ms: 1.53x faster                                                   |
| create_gc_cycles           | 2.45 ms                                                | 1.68 ms: 1.46x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 223 ms: 1.43x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 331 ms: 1.32x faster                                                   |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                   |
| deepcopy                   | 354 us                                                 | 290 us: 1.22x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 449 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.23 ms: 1.17x faster                                                  |
| float                      | 78.7 ms                                                | 68.4 ms: 1.15x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                  |
| go                         | 141 ms                                                 | 130 ms: 1.08x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 94.0 ms: 1.08x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.08x faster                                                 |
| deepcopy_reduce            | 3.24 us                                                | 3.02 us: 1.07x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 35.8 us: 1.07x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.05x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 147 ms: 1.05x faster                                                   |
| spectral_norm              | 113 ms                                                 | 109 ms: 1.04x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 62.6 ms: 1.03x faster                                                  |
| async_generators           | 433 ms                                                 | 423 ms: 1.03x faster                                                   |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                                  |
| pidigits                   | 186 ms                                                 | 184 ms: 1.01x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.40 sec: 1.01x slower                                                 |
| scimark_fft                | 367 ms                                                 | 374 ms: 1.02x slower                                                   |
| tomli_loads                | 2.12 sec                                               | 2.17 sec: 1.02x slower                                                 |
| generators                 | 28.8 ms                                                | 29.5 ms: 1.03x slower                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.85 sec: 1.04x slower                                                 |
| json                       | 5.32 ms                                                | 5.52 ms: 1.04x slower                                                  |
| scimark_sor                | 122 ms                                                 | 128 ms: 1.05x slower                                                   |
| html5lib                   | 63.4 ms                                                | 67.2 ms: 1.06x slower                                                  |
| logging_silent             | 101 ns                                                 | 108 ns: 1.06x slower                                                   |
| pyflate                    | 470 ms                                                 | 501 ms: 1.07x slower                                                   |
| richards                   | 47.5 ms                                                | 50.7 ms: 1.07x slower                                                  |
| telco                      | 8.40 ms                                                | 8.99 ms: 1.07x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.11 sec: 1.07x slower                                                 |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.78 sec: 1.08x slower                                                 |
| xml_etree_generate         | 86.8 ms                                                | 93.5 ms: 1.08x slower                                                  |
| 2to3                       | 266 ms                                                 | 287 ms: 1.08x slower                                                   |
| xml_etree_process          | 60.5 ms                                                | 65.5 ms: 1.08x slower                                                  |
| richards_super             | 53.7 ms                                                | 59.0 ms: 1.10x slower                                                  |
| regex_compile              | 132 ms                                                 | 145 ms: 1.10x slower                                                   |
| nqueens                    | 80.9 ms                                                | 89.8 ms: 1.11x slower                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.60 ms: 1.11x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 240 us: 1.13x slower                                                   |
| chaos                      | 58.0 ms                                                | 65.3 ms: 1.13x slower                                                  |
| sympy_str                  | 273 ms                                                 | 308 ms: 1.13x slower                                                   |
| sympy_integrate            | 19.8 ms                                                | 22.4 ms: 1.13x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 826 ms: 1.14x slower                                                   |
| genshi_xml                 | 50.5 ms                                                | 57.5 ms: 1.14x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 345 us: 1.14x slower                                                   |
| sympy_expand               | 456 ms                                                 | 520 ms: 1.14x slower                                                   |
| shortest_path              | 487 ms                                                 | 560 ms: 1.15x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.70 sec: 1.15x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 174 ms: 1.15x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.69 ms: 1.15x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 86.5 ms: 1.16x slower                                                  |
| logging_simple             | 5.65 us                                                | 6.57 us: 1.16x slower                                                  |
| connected_components       | 447 ms                                                 | 523 ms: 1.17x slower                                                   |
| comprehensions             | 16.5 us                                                | 19.4 us: 1.18x slower                                                  |
| json_loads                 | 27.2 us                                                | 32.0 us: 1.18x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 135 ms: 1.18x slower                                                   |
| genshi_text                | 22.6 ms                                                | 26.7 ms: 1.18x slower                                                  |
| logging_format             | 6.23 us                                                | 7.36 us: 1.18x slower                                                  |
| hexiom                     | 6.08 ms                                                | 7.20 ms: 1.19x slower                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 158 ms: 1.19x slower                                                   |
| raytrace                   | 262 ms                                                 | 312 ms: 1.19x slower                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 79.8 ms: 1.19x slower                                                  |
| meteor_contest             | 108 ms                                                 | 130 ms: 1.20x slower                                                   |
| many_optionals             | 857 us                                                 | 1.04 ms: 1.22x slower                                                  |
| django_template            | 31.7 ms                                                | 38.5 ms: 1.22x slower                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 20.6 ms: 1.22x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 197 us: 1.23x slower                                                   |
| python_startup             | 12.7 ms                                                | 15.6 ms: 1.23x slower                                                  |
| fannkuch                   | 394 ms                                                 | 487 ms: 1.24x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 12.8 ms: 1.27x slower                                                  |
| nbody                      | 87.7 ms                                                | 119 ms: 1.36x slower                                                   |
| coverage                   | 82.8 ms                                                | 119 ms: 1.44x slower                                                   |
| mako                       | 10.7 ms                                                | 15.6 ms: 1.46x slower                                                  |
| subparsers                 | 15.5 ms                                                | 23.3 ms: 1.51x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 10.9 ms: 1.56x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 90.3 ms: 3.76x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 3.25 ms: 3.98x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                           |

Benchmark hidden because not significant (3): pylint, regex_dna, asyncio_websockets
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250403-3.14.0a6+-275056a-NOGIL/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.030x slower

# HPT report

- Reliability score: 99.50% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.23x