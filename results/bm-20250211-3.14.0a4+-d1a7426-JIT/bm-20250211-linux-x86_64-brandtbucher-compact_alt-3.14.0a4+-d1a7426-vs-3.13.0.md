# Results vs. 3.13.0

- fork: brandtbucher
- ref: compact_alt
- machine: linux-x86_64
- commit hash: d1a7426
- commit date: 2025-02-11
- overall geometric mean: 1.018x faster
- HPT reliability: 80.04%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                                |
| docutils       | 2.58 sec                                               | 2.71 sec: 1.05x slower                                              |
| html5lib       | 63.4 ms                                                | 59.8 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 334 ms: 1.39x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 641 ms: 1.34x faster                                                |
| async_tree_io              | 838 ms                                                 | 637 ms: 1.32x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 340 ms: 1.28x faster                                                |
| async_tree_none            | 350 ms                                                 | 275 ms: 1.27x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 268 ms: 1.19x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 511 ms: 1.12x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 504 ms: 1.08x faster                                                |
| async_generators           | 433 ms                                                 | 404 ms: 1.07x faster                                                |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                               |
| Geometric mean             | (ref)                                                  | 1.17x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 75.5 ms: 1.04x faster                                               |
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                                |
| nbody          | 87.7 ms                                                | 93.7 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.11 ms: 1.21x faster                                               |
| regex_v8       | 26.9 ms                                                | 24.2 ms: 1.11x faster                                               |
| regex_compile  | 132 ms                                                 | 125 ms: 1.05x faster                                                |
| regex_dna      | 220 ms                                                 | 210 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.85 sec: 1.15x faster                                              |
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                |
| xml_etree_generate   | 86.8 ms                                                | 81.2 ms: 1.07x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 58.6 ms: 1.03x faster                                               |
| unpickle_pure_python | 213 us                                                 | 223 us: 1.05x slower                                                |
| json_loads           | 27.2 us                                                | 28.6 us: 1.05x slower                                               |
| pickle_pure_python   | 302 us                                                 | 330 us: 1.09x slower                                                |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.14x slower                                               |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.08 ms: 1.01x slower                                               |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                               |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 11.2 ms: 1.05x slower                                               |
| django_template | 31.7 ms                                                | 33.5 ms: 1.06x slower                                               |
| genshi_text     | 22.6 ms                                                | 24.4 ms: 1.08x slower                                               |
| genshi_xml      | 50.5 ms                                                | 56.4 ms: 1.12x slower                                               |
| Geometric mean  | (ref)                                                  | 1.08x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250211-linux-x86_64-brandtbucher-compact_alt-3.14.0a4+-d1a7426 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 334 ms: 1.39x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 641 ms: 1.34x faster                                                |
| async_tree_io              | 838 ms                                                 | 637 ms: 1.32x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 340 ms: 1.28x faster                                                |
| async_tree_none            | 350 ms                                                 | 275 ms: 1.27x faster                                                |
| deepcopy                   | 354 us                                                 | 282 us: 1.26x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.11 ms: 1.21x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 268 ms: 1.19x faster                                                |
| deepcopy_memo              | 38.4 us                                                | 32.5 us: 1.18x faster                                               |
| scimark_fft                | 367 ms                                                 | 315 ms: 1.16x faster                                                |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.15x faster                                              |
| deepcopy_reduce            | 3.24 us                                                | 2.83 us: 1.15x faster                                               |
| go                         | 141 ms                                                 | 124 ms: 1.13x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 511 ms: 1.12x faster                                                |
| regex_v8                   | 26.9 ms                                                | 24.2 ms: 1.11x faster                                               |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                |
| telco                      | 8.40 ms                                                | 7.61 ms: 1.10x faster                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.62 ms: 1.09x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 504 ms: 1.08x faster                                                |
| async_generators           | 433 ms                                                 | 404 ms: 1.07x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 81.2 ms: 1.07x faster                                               |
| spectral_norm              | 113 ms                                                 | 107 ms: 1.06x faster                                                |
| pylint                     | 312 ms                                                 | 294 ms: 1.06x faster                                                |
| html5lib                   | 63.4 ms                                                | 59.8 ms: 1.06x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                              |
| crypto_pyaes               | 74.7 ms                                                | 70.6 ms: 1.06x faster                                               |
| regex_compile              | 132 ms                                                 | 125 ms: 1.05x faster                                                |
| connected_components       | 447 ms                                                 | 426 ms: 1.05x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                               |
| regex_dna                  | 220 ms                                                 | 210 ms: 1.04x faster                                                |
| float                      | 78.7 ms                                                | 75.5 ms: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                              |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                               |
| richards                   | 47.5 ms                                                | 45.7 ms: 1.04x faster                                               |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                                |
| richards_super             | 53.7 ms                                                | 51.8 ms: 1.04x faster                                               |
| shortest_path              | 487 ms                                                 | 470 ms: 1.04x faster                                                |
| xml_etree_process          | 60.5 ms                                                | 58.6 ms: 1.03x faster                                               |
| json                       | 5.32 ms                                                | 5.17 ms: 1.03x faster                                               |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                |
| pyflate                    | 470 ms                                                 | 457 ms: 1.03x faster                                                |
| thrift                     | 800 us                                                 | 780 us: 1.03x faster                                                |
| logging_format             | 6.23 us                                                | 6.14 us: 1.01x faster                                               |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.00x faster                                                |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.0 ms: 1.01x slower                                               |
| mdp                        | 2.54 sec                                               | 2.57 sec: 1.01x slower                                              |
| python_startup_no_site     | 7.00 ms                                                | 7.08 ms: 1.01x slower                                               |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                               |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                               |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                |
| sympy_str                  | 273 ms                                                 | 281 ms: 1.03x slower                                                |
| gc_traversal               | 4.90 ms                                                | 5.05 ms: 1.03x slower                                               |
| sympy_integrate            | 19.8 ms                                                | 20.5 ms: 1.03x slower                                               |
| sqlglot_transpile          | 1.57 ms                                                | 1.63 ms: 1.04x slower                                               |
| sqlglot_parse              | 1.26 ms                                                | 1.31 ms: 1.04x slower                                               |
| sqlglot_optimize           | 53.4 ms                                                | 55.5 ms: 1.04x slower                                               |
| scimark_sor                | 122 ms                                                 | 127 ms: 1.04x slower                                                |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                |
| dulwich_log                | 64.6 ms                                                | 67.5 ms: 1.04x slower                                               |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                               |
| pprint_pformat             | 1.48 sec                                               | 1.55 sec: 1.05x slower                                              |
| docutils                   | 2.58 sec                                               | 2.71 sec: 1.05x slower                                              |
| comprehensions             | 16.5 us                                                | 17.3 us: 1.05x slower                                               |
| unpickle_pure_python       | 213 us                                                 | 223 us: 1.05x slower                                                |
| fannkuch                   | 394 ms                                                 | 413 ms: 1.05x slower                                                |
| json_loads                 | 27.2 us                                                | 28.6 us: 1.05x slower                                               |
| pprint_safe_repr           | 727 ms                                                 | 765 ms: 1.05x slower                                                |
| sqlglot_normalize          | 108 ms                                                 | 114 ms: 1.05x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 70.4 ms: 1.05x slower                                               |
| django_template            | 31.7 ms                                                | 33.5 ms: 1.06x slower                                               |
| sympy_expand               | 456 ms                                                 | 484 ms: 1.06x slower                                                |
| chaos                      | 58.0 ms                                                | 61.9 ms: 1.07x slower                                               |
| nbody                      | 87.7 ms                                                | 93.7 ms: 1.07x slower                                               |
| raytrace                   | 262 ms                                                 | 280 ms: 1.07x slower                                                |
| generators                 | 28.8 ms                                                | 30.9 ms: 1.07x slower                                               |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                               |
| genshi_text                | 22.6 ms                                                | 24.4 ms: 1.08x slower                                               |
| coverage                   | 82.8 ms                                                | 89.6 ms: 1.08x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.61 ms: 1.09x slower                                               |
| nqueens                    | 80.9 ms                                                | 88.0 ms: 1.09x slower                                               |
| pickle_pure_python         | 302 us                                                 | 330 us: 1.09x slower                                                |
| bench_thread_pool          | 818 us                                                 | 898 us: 1.10x slower                                                |
| deltablue                  | 3.19 ms                                                | 3.54 ms: 1.11x slower                                               |
| genshi_xml                 | 50.5 ms                                                | 56.4 ms: 1.12x slower                                               |
| scimark_lu                 | 114 ms                                                 | 129 ms: 1.13x slower                                                |
| many_optionals             | 857 us                                                 | 965 us: 1.13x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.14x slower                                               |
| logging_silent             | 101 ns                                                 | 134 ns: 1.33x slower                                                |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 81.4 ms: 3.39x slower                                               |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (4): xml_etree_iterparse, logging_simple, asyncio_websockets, sphinx
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, pycparser, tornado_http

- Geometric mean (including insignificant results): 1.018x faster

# HPT report

- Reliability score: 80.04% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x