# Results vs. 3.13.0

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: dda3d1f
- commit date: 2025-02-06
- overall geometric mean: 1.054x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 251 ms: 1.06x faster                                                       |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.00x faster                                                     |
| html5lib       | 63.4 ms                                                | 60.6 ms: 1.05x faster                                                      |
| sphinx         | 1.03 sec                                               | 995 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                       |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                                       |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.14x faster                                                       |
| async_generators           | 433 ms                                                 | 390 ms: 1.11x faster                                                       |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.3 ms: 1.12x faster                                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| nbody          | 87.7 ms                                                | 91.2 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.32 ms: 1.14x faster                                                      |
| regex_v8       | 26.9 ms                                                | 25.5 ms: 1.05x faster                                                      |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                                       |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                       |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.08x faster                                                     |
| xml_etree_generate   | 86.8 ms                                                | 83.7 ms: 1.04x faster                                                      |
| xml_etree_process    | 60.5 ms                                                | 58.4 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 98.6 ms: 1.03x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                       |
| pickle_pure_python   | 302 us                                                 | 315 us: 1.04x slower                                                       |
| json_loads           | 27.2 us                                                | 29.3 us: 1.08x slower                                                      |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.00 ms: 1.00x slower                                                      |
| python_startup         | 12.7 ms                                                | 12.7 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                      |
| genshi_xml      | 50.5 ms                                                | 47.7 ms: 1.06x faster                                                      |
| django_template | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                      |
| mako            | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                       |
| deepcopy                   | 354 us                                                 | 258 us: 1.38x faster                                                       |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                                       |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                       |
| deepcopy_memo              | 38.4 us                                                | 29.7 us: 1.29x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                       |
| spectral_norm              | 113 ms                                                 | 94.5 ms: 1.20x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.72 us: 1.19x faster                                                      |
| go                         | 141 ms                                                 | 119 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                       |
| pylint                     | 312 ms                                                 | 272 ms: 1.15x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.32 ms: 1.14x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.14x faster                                                       |
| float                      | 78.7 ms                                                | 70.3 ms: 1.12x faster                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.53 ms: 1.11x faster                                                      |
| async_generators           | 433 ms                                                 | 390 ms: 1.11x faster                                                       |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                       |
| pathlib                    | 17.4 ms                                                | 15.9 ms: 1.09x faster                                                      |
| genshi_text                | 22.6 ms                                                | 20.9 ms: 1.08x faster                                                      |
| telco                      | 8.40 ms                                                | 7.78 ms: 1.08x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.08x faster                                                     |
| scimark_fft                | 367 ms                                                 | 341 ms: 1.08x faster                                                       |
| bpe_tokeniser              | 4.69 sec                                               | 4.38 sec: 1.07x faster                                                     |
| crypto_pyaes               | 74.7 ms                                                | 69.9 ms: 1.07x faster                                                      |
| thrift                     | 800 us                                                 | 750 us: 1.07x faster                                                       |
| gc_traversal               | 4.90 ms                                                | 4.60 ms: 1.06x faster                                                      |
| richards                   | 47.5 ms                                                | 44.9 ms: 1.06x faster                                                      |
| richards_super             | 53.7 ms                                                | 50.7 ms: 1.06x faster                                                      |
| genshi_xml                 | 50.5 ms                                                | 47.7 ms: 1.06x faster                                                      |
| 2to3                       | 266 ms                                                 | 251 ms: 1.06x faster                                                       |
| regex_v8                   | 26.9 ms                                                | 25.5 ms: 1.05x faster                                                      |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                                       |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                       |
| sqlglot_normalize          | 108 ms                                                 | 103 ms: 1.05x faster                                                       |
| k_core                     | 2.37 sec                                               | 2.26 sec: 1.05x faster                                                     |
| pyflate                    | 470 ms                                                 | 449 ms: 1.05x faster                                                       |
| html5lib                   | 63.4 ms                                                | 60.6 ms: 1.05x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                                      |
| generators                 | 28.8 ms                                                | 27.6 ms: 1.04x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                       |
| xml_etree_generate         | 86.8 ms                                                | 83.7 ms: 1.04x faster                                                      |
| sphinx                     | 1.03 sec                                               | 995 ms: 1.04x faster                                                       |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.04x faster                                                       |
| xml_etree_process          | 60.5 ms                                                | 58.4 ms: 1.03x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                     |
| logging_simple             | 5.65 us                                                | 5.47 us: 1.03x faster                                                      |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                                       |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                      |
| json                       | 5.32 ms                                                | 5.17 ms: 1.03x faster                                                      |
| sqlglot_optimize           | 53.4 ms                                                | 51.8 ms: 1.03x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                       |
| typing_runtime_protocols   | 160 us                                                 | 156 us: 1.03x faster                                                       |
| logging_format             | 6.23 us                                                | 6.07 us: 1.03x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 98.6 ms: 1.03x faster                                                      |
| pprint_safe_repr           | 727 ms                                                 | 709 ms: 1.02x faster                                                       |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.02x faster                                                     |
| shortest_path              | 487 ms                                                 | 475 ms: 1.02x faster                                                       |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                                       |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                       |
| sympy_expand               | 456 ms                                                 | 448 ms: 1.02x faster                                                       |
| comprehensions             | 16.5 us                                                | 16.2 us: 1.02x faster                                                      |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                                     |
| sympy_integrate            | 19.8 ms                                                | 19.5 ms: 1.02x faster                                                      |
| dulwich_log                | 64.6 ms                                                | 63.9 ms: 1.01x faster                                                      |
| nqueens                    | 80.9 ms                                                | 80.1 ms: 1.01x faster                                                      |
| django_template            | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                      |
| sqlglot_parse              | 1.26 ms                                                | 1.25 ms: 1.01x faster                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.56 ms: 1.01x faster                                                      |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.00x faster                                                     |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| create_gc_cycles           | 2.45 ms                                                | 2.44 ms: 1.00x faster                                                      |
| python_startup_no_site     | 7.00 ms                                                | 7.00 ms: 1.00x slower                                                      |
| fannkuch                   | 394 ms                                                 | 395 ms: 1.00x slower                                                       |
| chaos                      | 58.0 ms                                                | 58.3 ms: 1.00x slower                                                      |
| deltablue                  | 3.19 ms                                                | 3.21 ms: 1.01x slower                                                      |
| python_startup             | 12.7 ms                                                | 12.7 ms: 1.01x slower                                                      |
| hexiom                     | 6.08 ms                                                | 6.16 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                       |
| logging_silent             | 101 ns                                                 | 104 ns: 1.03x slower                                                       |
| raytrace                   | 262 ms                                                 | 269 ms: 1.03x slower                                                       |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                      |
| nbody                      | 87.7 ms                                                | 91.2 ms: 1.04x slower                                                      |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 315 us: 1.04x slower                                                       |
| bench_thread_pool          | 818 us                                                 | 861 us: 1.05x slower                                                       |
| many_optionals             | 857 us                                                 | 924 us: 1.08x slower                                                       |
| json_loads                 | 27.2 us                                                | 29.3 us: 1.08x slower                                                      |
| coverage                   | 82.8 ms                                                | 92.7 ms: 1.12x slower                                                      |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.16x slower                                                      |
| subparsers                 | 15.5 ms                                                | 20.3 ms: 1.32x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 80.6 ms: 3.36x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (3): scimark_lu, scimark_monte_carlo, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.054x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x