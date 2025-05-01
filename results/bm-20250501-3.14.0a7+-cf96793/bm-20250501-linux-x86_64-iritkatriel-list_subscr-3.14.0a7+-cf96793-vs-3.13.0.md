# Results vs. 3.13.0

- fork: iritkatriel
- ref: list_subscr
- machine: linux-x86_64
- commit hash: cf96793
- commit date: 2025-05-01
- overall geometric mean: 1.040x faster
- HPT reliability: 99.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                               |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                             |
| html5lib       | 63.4 ms                                                | 61.0 ms: 1.04x faster                                              |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 307 ms: 1.51x faster                                               |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                               |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                               |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 494 ms: 1.10x faster                                               |
| async_generators           | 433 ms                                                 | 409 ms: 1.06x faster                                               |
| coroutines                 | 22.2 ms                                                | 26.3 ms: 1.18x slower                                              |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.0 ms: 1.09x faster                                              |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                               |
| nbody          | 87.7 ms                                                | 97.7 ms: 1.11x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.34 ms: 1.13x faster                                              |
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.12x faster                                              |
| regex_dna      | 220 ms                                                 | 208 ms: 1.06x faster                                               |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.08x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 85.0 ms: 1.02x faster                                              |
| xml_etree_process    | 60.5 ms                                                | 59.3 ms: 1.02x faster                                              |
| tomli_loads          | 2.12 sec                                               | 2.08 sec: 1.02x faster                                             |
| xml_etree_iterparse  | 101 ms                                                 | 100 ms: 1.01x faster                                               |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                               |
| pickle_pure_python   | 302 us                                                 | 319 us: 1.05x slower                                               |
| json_loads           | 27.2 us                                                | 30.5 us: 1.12x slower                                              |
| json_dumps           | 10.1 ms                                                | 12.0 ms: 1.18x slower                                              |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.94 ms: 1.01x faster                                              |
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                              |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.0 ms: 1.07x faster                                              |
| genshi_xml      | 50.5 ms                                                | 49.2 ms: 1.03x faster                                              |
| django_template | 31.7 ms                                                | 32.5 ms: 1.03x slower                                              |
| mako            | 10.7 ms                                                | 11.7 ms: 1.10x slower                                              |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.24 sec: 2.06x faster                                             |
| async_tree_memoization_tg  | 463 ms                                                 | 307 ms: 1.51x faster                                               |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                               |
| async_tree_io_tg           | 861 ms                                                 | 613 ms: 1.40x faster                                               |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.40x faster                                               |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                               |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                              |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                               |
| go                         | 141 ms                                                 | 113 ms: 1.25x faster                                               |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                              |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 499 ms: 1.15x faster                                               |
| regex_effbot               | 3.77 ms                                                | 3.34 ms: 1.13x faster                                              |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.12x faster                                              |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                               |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 494 ms: 1.10x faster                                               |
| richards                   | 47.5 ms                                                | 43.3 ms: 1.10x faster                                              |
| float                      | 78.7 ms                                                | 72.0 ms: 1.09x faster                                              |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.08x faster                                               |
| richards_super             | 53.7 ms                                                | 49.6 ms: 1.08x faster                                              |
| dulwich_log                | 64.6 ms                                                | 59.8 ms: 1.08x faster                                              |
| logging_silent             | 101 ns                                                 | 93.6 ns: 1.08x faster                                              |
| genshi_text                | 22.6 ms                                                | 21.0 ms: 1.07x faster                                              |
| async_generators           | 433 ms                                                 | 409 ms: 1.06x faster                                               |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.06x faster                                               |
| telco                      | 8.40 ms                                                | 7.96 ms: 1.05x faster                                              |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                             |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                               |
| html5lib                   | 63.4 ms                                                | 61.0 ms: 1.04x faster                                              |
| pyflate                    | 470 ms                                                 | 453 ms: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                             |
| sympy_integrate            | 19.8 ms                                                | 19.1 ms: 1.04x faster                                              |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                               |
| bpe_tokeniser              | 4.69 sec                                               | 4.56 sec: 1.03x faster                                             |
| genshi_xml                 | 50.5 ms                                                | 49.2 ms: 1.03x faster                                              |
| spectral_norm              | 113 ms                                                 | 110 ms: 1.03x faster                                               |
| gc_traversal               | 4.90 ms                                                | 4.79 ms: 1.02x faster                                              |
| xml_etree_generate         | 86.8 ms                                                | 85.0 ms: 1.02x faster                                              |
| xml_etree_process          | 60.5 ms                                                | 59.3 ms: 1.02x faster                                              |
| tomli_loads                | 2.12 sec                                               | 2.08 sec: 1.02x faster                                             |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.01x faster                                             |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.01x faster                                               |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                               |
| xml_etree_iterparse        | 101 ms                                                 | 100 ms: 1.01x faster                                               |
| pathlib                    | 17.4 ms                                                | 17.2 ms: 1.01x faster                                              |
| python_startup_no_site     | 7.00 ms                                                | 6.94 ms: 1.01x faster                                              |
| sqlite_synth               | 2.90 us                                                | 2.88 us: 1.01x faster                                              |
| sympy_sum                  | 150 ms                                                 | 150 ms: 1.01x faster                                               |
| scimark_sor                | 122 ms                                                 | 122 ms: 1.01x faster                                               |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.00x faster                                               |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                               |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                             |
| sympy_expand               | 456 ms                                                 | 459 ms: 1.01x slower                                               |
| scimark_lu                 | 114 ms                                                 | 115 ms: 1.01x slower                                               |
| logging_format             | 6.23 us                                                | 6.28 us: 1.01x slower                                              |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                             |
| nqueens                    | 80.9 ms                                                | 81.8 ms: 1.01x slower                                              |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                              |
| connected_components       | 447 ms                                                 | 454 ms: 1.02x slower                                               |
| shortest_path              | 487 ms                                                 | 496 ms: 1.02x slower                                               |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                               |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                              |
| scimark_monte_carlo        | 66.8 ms                                                | 68.2 ms: 1.02x slower                                              |
| chaos                      | 58.0 ms                                                | 59.3 ms: 1.02x slower                                              |
| json                       | 5.32 ms                                                | 5.45 ms: 1.02x slower                                              |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                               |
| django_template            | 31.7 ms                                                | 32.5 ms: 1.03x slower                                              |
| typing_runtime_protocols   | 160 us                                                 | 165 us: 1.03x slower                                               |
| generators                 | 28.8 ms                                                | 29.7 ms: 1.03x slower                                              |
| scimark_fft                | 367 ms                                                 | 378 ms: 1.03x slower                                               |
| crypto_pyaes               | 74.7 ms                                                | 77.1 ms: 1.03x slower                                              |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                              |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                              |
| hexiom                     | 6.08 ms                                                | 6.37 ms: 1.05x slower                                              |
| deltablue                  | 3.19 ms                                                | 3.36 ms: 1.05x slower                                              |
| pickle_pure_python         | 302 us                                                 | 319 us: 1.05x slower                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.37 ms: 1.07x slower                                              |
| fannkuch                   | 394 ms                                                 | 424 ms: 1.08x slower                                               |
| many_optionals             | 857 us                                                 | 931 us: 1.09x slower                                               |
| bench_thread_pool          | 818 us                                                 | 892 us: 1.09x slower                                               |
| mako                       | 10.7 ms                                                | 11.7 ms: 1.10x slower                                              |
| nbody                      | 87.7 ms                                                | 97.7 ms: 1.11x slower                                              |
| json_loads                 | 27.2 us                                                | 30.5 us: 1.12x slower                                              |
| coverage                   | 82.8 ms                                                | 93.2 ms: 1.13x slower                                              |
| coroutines                 | 22.2 ms                                                | 26.3 ms: 1.18x slower                                              |
| json_dumps                 | 10.1 ms                                                | 12.0 ms: 1.18x slower                                              |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.34x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 82.8 ms: 3.45x slower                                              |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (3): logging_simple, asyncio_websockets, pprint_safe_repr
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250501-3.14.0a7+-cf96793/bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 99.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x