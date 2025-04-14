# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a5
- machine: linux-x86_64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.041x faster
- HPT reliability: 99.47%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.03x faster                                       |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                     |
| html5lib       | 63.4 ms                                                | 60.6 ms: 1.05x faster                                      |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                       |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                       |
| async_tree_io              | 838 ms                                                 | 623 ms: 1.35x faster                                       |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                       |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                       |
| async_tree_none_tg         | 319 ms                                                 | 262 ms: 1.22x faster                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 503 ms: 1.14x faster                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 493 ms: 1.10x faster                                       |
| async_generators           | 433 ms                                                 | 408 ms: 1.06x faster                                       |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.04x slower                                      |
| Geometric mean             | (ref)                                                  | 1.20x faster                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.1 ms: 1.14x faster                                      |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| nbody          | 87.7 ms                                                | 97.7 ms: 1.11x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.20 ms: 1.18x faster                                      |
| regex_v8       | 26.9 ms                                                | 23.5 ms: 1.14x faster                                      |
| regex_dna      | 220 ms                                                 | 206 ms: 1.07x faster                                       |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                     |
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                       |
| xml_etree_generate   | 86.8 ms                                                | 78.7 ms: 1.10x faster                                      |
| xml_etree_process    | 60.5 ms                                                | 55.6 ms: 1.09x faster                                      |
| unpickle_pure_python | 213 us                                                 | 199 us: 1.07x faster                                       |
| xml_etree_iterparse  | 101 ms                                                 | 96.0 ms: 1.05x faster                                      |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                      |
| pickle_pure_python   | 302 us                                                 | 324 us: 1.07x slower                                       |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.05 ms: 1.01x slower                                      |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                      |
| Geometric mean         | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.9 ms: 1.03x faster                                      |
| mako            | 10.7 ms                                                | 10.5 ms: 1.02x faster                                      |
| django_template | 31.7 ms                                                | 31.5 ms: 1.00x faster                                      |
| Geometric mean  | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                       |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                       |
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                       |
| async_tree_io              | 838 ms                                                 | 623 ms: 1.35x faster                                       |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                       |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                       |
| deepcopy_memo              | 38.4 us                                                | 30.5 us: 1.26x faster                                      |
| async_tree_none_tg         | 319 ms                                                 | 262 ms: 1.22x faster                                       |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                      |
| regex_effbot               | 3.77 ms                                                | 3.20 ms: 1.18x faster                                      |
| spectral_norm              | 113 ms                                                 | 96.7 ms: 1.17x faster                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.34 ms: 1.16x faster                                      |
| scimark_fft                | 367 ms                                                 | 317 ms: 1.16x faster                                       |
| regex_v8                   | 26.9 ms                                                | 23.5 ms: 1.14x faster                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 503 ms: 1.14x faster                                       |
| float                      | 78.7 ms                                                | 69.1 ms: 1.14x faster                                      |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                     |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                       |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                       |
| xml_etree_generate         | 86.8 ms                                                | 78.7 ms: 1.10x faster                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 493 ms: 1.10x faster                                       |
| telco                      | 8.40 ms                                                | 7.67 ms: 1.10x faster                                      |
| xml_etree_process          | 60.5 ms                                                | 55.6 ms: 1.09x faster                                      |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                       |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.36 sec: 1.07x faster                                     |
| crypto_pyaes               | 74.7 ms                                                | 69.5 ms: 1.07x faster                                      |
| unpickle_pure_python       | 213 us                                                 | 199 us: 1.07x faster                                       |
| regex_dna                  | 220 ms                                                 | 206 ms: 1.07x faster                                       |
| pyflate                    | 470 ms                                                 | 441 ms: 1.06x faster                                       |
| async_generators           | 433 ms                                                 | 408 ms: 1.06x faster                                       |
| sqlite_synth               | 2.90 us                                                | 2.74 us: 1.06x faster                                      |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                       |
| richards                   | 47.5 ms                                                | 45.0 ms: 1.06x faster                                      |
| thrift                     | 800 us                                                 | 759 us: 1.05x faster                                       |
| xml_etree_iterparse        | 101 ms                                                 | 96.0 ms: 1.05x faster                                      |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                      |
| richards_super             | 53.7 ms                                                | 51.3 ms: 1.05x faster                                      |
| html5lib                   | 63.4 ms                                                | 60.6 ms: 1.05x faster                                      |
| json                       | 5.32 ms                                                | 5.13 ms: 1.04x faster                                      |
| genshi_text                | 22.6 ms                                                | 21.9 ms: 1.03x faster                                      |
| 2to3                       | 266 ms                                                 | 257 ms: 1.03x faster                                       |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                     |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                     |
| logging_simple             | 5.65 us                                                | 5.50 us: 1.03x faster                                      |
| logging_format             | 6.23 us                                                | 6.08 us: 1.02x faster                                      |
| mako                       | 10.7 ms                                                | 10.5 ms: 1.02x faster                                      |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.02x faster                                       |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                       |
| connected_components       | 447 ms                                                 | 441 ms: 1.01x faster                                       |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                      |
| shortest_path              | 487 ms                                                 | 483 ms: 1.01x faster                                       |
| gc_traversal               | 4.90 ms                                                | 4.87 ms: 1.01x faster                                      |
| django_template            | 31.7 ms                                                | 31.5 ms: 1.00x faster                                      |
| generators                 | 28.8 ms                                                | 28.9 ms: 1.00x slower                                      |
| sqlglot_optimize           | 53.4 ms                                                | 53.7 ms: 1.01x slower                                      |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.01x slower                                      |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                      |
| sympy_str                  | 273 ms                                                 | 275 ms: 1.01x slower                                       |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| python_startup_no_site     | 7.00 ms                                                | 7.05 ms: 1.01x slower                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                      |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                       |
| chaos                      | 58.0 ms                                                | 58.7 ms: 1.01x slower                                      |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                       |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                      |
| sympy_integrate            | 19.8 ms                                                | 20.2 ms: 1.02x slower                                      |
| logging_silent             | 101 ns                                                 | 103 ns: 1.02x slower                                       |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                       |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                       |
| dulwich_log                | 64.6 ms                                                | 66.4 ms: 1.03x slower                                      |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                     |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                      |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.04x slower                                      |
| pprint_safe_repr           | 727 ms                                                 | 764 ms: 1.05x slower                                       |
| pprint_pformat             | 1.48 sec                                               | 1.56 sec: 1.05x slower                                     |
| deltablue                  | 3.19 ms                                                | 3.38 ms: 1.06x slower                                      |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                      |
| raytrace                   | 262 ms                                                 | 279 ms: 1.07x slower                                       |
| pickle_pure_python         | 302 us                                                 | 324 us: 1.07x slower                                       |
| bench_thread_pool          | 818 us                                                 | 888 us: 1.09x slower                                       |
| nqueens                    | 80.9 ms                                                | 88.5 ms: 1.09x slower                                      |
| many_optionals             | 857 us                                                 | 948 us: 1.11x slower                                       |
| nbody                      | 87.7 ms                                                | 97.7 ms: 1.11x slower                                      |
| hexiom                     | 6.08 ms                                                | 6.96 ms: 1.15x slower                                      |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                      |
| coverage                   | 82.8 ms                                                | 96.8 ms: 1.17x slower                                      |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.33x slower                                      |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                      |
| Geometric mean             | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (7): scimark_monte_carlo, mdp, genshi_xml, scimark_sor, asyncio_websockets, meteor_contest, fannkuch
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 99.47% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x