# Results vs. 3.13.0

- fork: python
- ref: cdcacec79f7a216c3c98
- machine: linux-x86_64
- commit hash: cdcacec
- commit date: 2025-02-05
- overall geometric mean: 1.033x faster
- HPT reliability: 98.54%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                   |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                 |
| html5lib       | 63.4 ms                                                | 64.1 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 627 ms: 1.34x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 329 ms: 1.33x faster                                                   |
| async_tree_none            | 350 ms                                                 | 268 ms: 1.31x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 501 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                   |
| async_generators           | 433 ms                                                 | 411 ms: 1.05x faster                                                   |
| coroutines                 | 22.2 ms                                                | 22.7 ms: 1.02x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 67.1 ms: 1.17x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| nbody          | 87.7 ms                                                | 93.6 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.1 ms: 1.11x faster                                                  |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                   |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                 |
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.11x faster                                                   |
| xml_etree_process    | 60.5 ms                                                | 56.7 ms: 1.07x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 201 us: 1.06x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 95.9 ms: 1.06x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 83.3 ms: 1.04x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 314 us: 1.04x slower                                                   |
| json_loads           | 27.2 us                                                | 29.1 us: 1.07x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.04 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 9.86 ms: 1.08x faster                                                  |
| genshi_text     | 22.6 ms                                                | 23.1 ms: 1.02x slower                                                  |
| django_template | 31.7 ms                                                | 33.0 ms: 1.04x slower                                                  |
| genshi_xml      | 50.5 ms                                                | 57.0 ms: 1.13x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-python-cdcacec79f7a216c3c98-3.14.0a4+-cdcacec |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 627 ms: 1.34x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 329 ms: 1.33x faster                                                   |
| async_tree_none            | 350 ms                                                 | 268 ms: 1.31x faster                                                   |
| deepcopy                   | 354 us                                                 | 272 us: 1.30x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 30.3 us: 1.27x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                   |
| spectral_norm              | 113 ms                                                 | 95.4 ms: 1.19x faster                                                  |
| float                      | 78.7 ms                                                | 67.1 ms: 1.17x faster                                                  |
| scimark_fft                | 367 ms                                                 | 315 ms: 1.16x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.81 us: 1.15x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.84 sec: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 501 ms: 1.14x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                  |
| go                         | 141 ms                                                 | 126 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.51 ms: 1.11x faster                                                  |
| telco                      | 8.40 ms                                                | 7.53 ms: 1.11x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.11x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 24.1 ms: 1.11x faster                                                  |
| richards                   | 47.5 ms                                                | 43.7 ms: 1.09x faster                                                  |
| pylint                     | 312 ms                                                 | 286 ms: 1.09x faster                                                   |
| mako                       | 10.7 ms                                                | 9.86 ms: 1.08x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.37 sec: 1.07x faster                                                 |
| scimark_sor                | 122 ms                                                 | 114 ms: 1.07x faster                                                   |
| richards_super             | 53.7 ms                                                | 50.1 ms: 1.07x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.07x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.71 us: 1.07x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 69.9 ms: 1.07x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 56.7 ms: 1.07x faster                                                  |
| unpickle_pure_python       | 213 us                                                 | 201 us: 1.06x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 95.9 ms: 1.06x faster                                                  |
| async_generators           | 433 ms                                                 | 411 ms: 1.05x faster                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 63.5 ms: 1.05x faster                                                  |
| pyflate                    | 470 ms                                                 | 448 ms: 1.05x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 83.3 ms: 1.04x faster                                                  |
| thrift                     | 800 us                                                 | 773 us: 1.03x faster                                                   |
| json                       | 5.32 ms                                                | 5.15 ms: 1.03x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                 |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                   |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                                   |
| fannkuch                   | 394 ms                                                 | 386 ms: 1.02x faster                                                   |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                   |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.01x faster                                                 |
| connected_components       | 447 ms                                                 | 441 ms: 1.01x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.89 ms: 1.00x faster                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.04 ms: 1.01x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.56 sec: 1.01x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 115 ms: 1.01x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                                   |
| html5lib                   | 63.4 ms                                                | 64.1 ms: 1.01x slower                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.28 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| logging_format             | 6.23 us                                                | 6.32 us: 1.02x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 54.3 ms: 1.02x slower                                                  |
| coroutines                 | 22.2 ms                                                | 22.7 ms: 1.02x slower                                                  |
| logging_simple             | 5.65 us                                                | 5.77 us: 1.02x slower                                                  |
| genshi_text                | 22.6 ms                                                | 23.1 ms: 1.02x slower                                                  |
| sympy_str                  | 273 ms                                                 | 280 ms: 1.02x slower                                                   |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.03x slower                                                  |
| chaos                      | 58.0 ms                                                | 60.0 ms: 1.03x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.04x slower                                                 |
| dulwich_log                | 64.6 ms                                                | 66.9 ms: 1.04x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 314 us: 1.04x slower                                                   |
| django_template            | 31.7 ms                                                | 33.0 ms: 1.04x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 20.7 ms: 1.04x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 763 ms: 1.05x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.56 sec: 1.06x slower                                                 |
| nbody                      | 87.7 ms                                                | 93.6 ms: 1.07x slower                                                  |
| json_loads                 | 27.2 us                                                | 29.1 us: 1.07x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.48 ms: 1.09x slower                                                  |
| coverage                   | 82.8 ms                                                | 90.6 ms: 1.09x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 897 us: 1.10x slower                                                   |
| logging_silent             | 101 ns                                                 | 112 ns: 1.10x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                  |
| raytrace                   | 262 ms                                                 | 292 ms: 1.12x slower                                                   |
| many_optionals             | 857 us                                                 | 958 us: 1.12x slower                                                   |
| nqueens                    | 80.9 ms                                                | 90.5 ms: 1.12x slower                                                  |
| genshi_xml                 | 50.5 ms                                                | 57.0 ms: 1.13x slower                                                  |
| hexiom                     | 6.08 ms                                                | 7.43 ms: 1.22x slower                                                  |
| generators                 | 28.8 ms                                                | 37.5 ms: 1.30x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.7 ms: 1.34x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 80.4 ms: 3.35x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (5): shortest_path, create_gc_cycles, asyncio_websockets, sqlglot_normalize, sphinx
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 98.54% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x