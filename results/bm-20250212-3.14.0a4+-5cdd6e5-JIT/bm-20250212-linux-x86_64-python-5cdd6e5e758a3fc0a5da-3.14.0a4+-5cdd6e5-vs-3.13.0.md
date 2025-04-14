# Results vs. 3.13.0

- fork: python
- ref: 5cdd6e5e758a3fc0a5da
- machine: linux-x86_64
- commit hash: 5cdd6e5
- commit date: 2025-02-12
- overall geometric mean: 1.043x faster
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                   |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                 |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 625 ms: 1.34x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                                   |
| async_tree_none            | 350 ms                                                 | 268 ms: 1.31x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 261 ms: 1.22x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                                   |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.5 ms: 1.12x faster                                                  |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| nbody          | 87.7 ms                                                | 93.5 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.16 ms: 1.19x faster                                                  |
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                  |
| regex_dna      | 220 ms                                                 | 207 ms: 1.06x faster                                                   |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                 |
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 78.3 ms: 1.11x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 55.5 ms: 1.09x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 199 us: 1.07x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 96.2 ms: 1.05x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.06x slower                                                   |
| json_loads           | 27.2 us                                                | 29.0 us: 1.07x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.9 ms: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                  |
| genshi_text    | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                  |
| genshi_xml     | 50.5 ms                                                | 49.4 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                   |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                                   |
| async_tree_io              | 838 ms                                                 | 625 ms: 1.34x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                                   |
| async_tree_none            | 350 ms                                                 | 268 ms: 1.31x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 30.7 us: 1.25x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 261 ms: 1.22x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.68 us: 1.21x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.16 ms: 1.19x faster                                                  |
| spectral_norm              | 113 ms                                                 | 95.7 ms: 1.18x faster                                                  |
| scimark_fft                | 367 ms                                                 | 312 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 493 ms: 1.16x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.48 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                   |
| float                      | 78.7 ms                                                | 70.5 ms: 1.12x faster                                                  |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 78.3 ms: 1.11x faster                                                  |
| telco                      | 8.40 ms                                                | 7.59 ms: 1.11x faster                                                  |
| richards                   | 47.5 ms                                                | 43.4 ms: 1.10x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 55.5 ms: 1.09x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.10 sec: 1.09x faster                                                 |
| richards_super             | 53.7 ms                                                | 49.8 ms: 1.08x faster                                                  |
| go                         | 141 ms                                                 | 131 ms: 1.08x faster                                                   |
| unpickle_pure_python       | 213 us                                                 | 199 us: 1.07x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.39 sec: 1.07x faster                                                 |
| regex_dna                  | 220 ms                                                 | 207 ms: 1.06x faster                                                   |
| mako                       | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 70.7 ms: 1.06x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.06x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 96.2 ms: 1.05x faster                                                  |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                   |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                   |
| thrift                     | 800 us                                                 | 763 us: 1.05x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                                  |
| generators                 | 28.8 ms                                                | 27.7 ms: 1.04x faster                                                  |
| genshi_text                | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                  |
| json                       | 5.32 ms                                                | 5.14 ms: 1.03x faster                                                  |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                   |
| pyflate                    | 470 ms                                                 | 457 ms: 1.03x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                 |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 49.4 ms: 1.02x faster                                                  |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| logging_format             | 6.23 us                                                | 6.12 us: 1.02x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.56 us: 1.02x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 65.8 ms: 1.02x faster                                                  |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.01x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                   |
| connected_components       | 447 ms                                                 | 442 ms: 1.01x faster                                                   |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| shortest_path              | 487 ms                                                 | 483 ms: 1.01x faster                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                  |
| fannkuch                   | 394 ms                                                 | 395 ms: 1.00x slower                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 53.6 ms: 1.00x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                                   |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| chaos                      | 58.0 ms                                                | 58.4 ms: 1.01x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.57 sec: 1.01x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 4.95 ms: 1.01x slower                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.28 ms: 1.01x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.02x slower                                                 |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 20.2 ms: 1.02x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                   |
| dulwich_log                | 64.6 ms                                                | 66.1 ms: 1.02x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.02x slower                                                   |
| sympy_expand               | 456 ms                                                 | 470 ms: 1.03x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 751 ms: 1.03x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                  |
| logging_silent             | 101 ns                                                 | 106 ns: 1.05x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                  |
| raytrace                   | 262 ms                                                 | 275 ms: 1.05x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.37 ms: 1.06x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.06x slower                                                   |
| nbody                      | 87.7 ms                                                | 93.5 ms: 1.07x slower                                                  |
| json_loads                 | 27.2 us                                                | 29.0 us: 1.07x slower                                                  |
| coverage                   | 82.8 ms                                                | 89.8 ms: 1.08x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 889 us: 1.09x slower                                                   |
| nqueens                    | 80.9 ms                                                | 89.3 ms: 1.10x slower                                                  |
| many_optionals             | 857 us                                                 | 958 us: 1.12x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.93 ms: 1.14x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.9 ms: 1.18x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, django_template, sympy_str
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x