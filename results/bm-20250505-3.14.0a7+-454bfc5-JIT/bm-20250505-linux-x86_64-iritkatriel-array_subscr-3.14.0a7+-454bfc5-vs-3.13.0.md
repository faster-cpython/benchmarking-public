# Results vs. 3.13.0

- fork: iritkatriel
- ref: array_subscr
- machine: linux-x86_64
- commit hash: 454bfc5
- commit date: 2025-05-05
- overall geometric mean: 1.042x faster
- HPT reliability: 98.12%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                              |
| html5lib       | 63.4 ms                                                | 60.6 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 601 ms: 1.43x faster                                                |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 503 ms: 1.14x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 493 ms: 1.10x faster                                                |
| async_generators           | 433 ms                                                 | 431 ms: 1.00x faster                                                |
| coroutines                 | 22.2 ms                                                | 25.7 ms: 1.16x slower                                               |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.9 ms: 1.19x faster                                               |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                |
| nbody          | 87.7 ms                                                | 98.1 ms: 1.12x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.35 ms: 1.12x faster                                               |
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.12x faster                                               |
| regex_dna      | 220 ms                                                 | 208 ms: 1.06x faster                                                |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.90 sec: 1.11x faster                                              |
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.10x faster                                                |
| xml_etree_generate   | 86.8 ms                                                | 80.7 ms: 1.08x faster                                               |
| xml_etree_process    | 60.5 ms                                                | 56.2 ms: 1.08x faster                                               |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                               |
| unpickle_pure_python | 213 us                                                 | 207 us: 1.03x faster                                                |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                                |
| json_loads           | 27.2 us                                                | 30.2 us: 1.11x slower                                               |
| json_dumps           | 10.1 ms                                                | 12.0 ms: 1.18x slower                                               |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.94 ms: 1.01x faster                                               |
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                               |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                               |
| genshi_xml      | 50.5 ms                                                | 49.1 ms: 1.03x faster                                               |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                               |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                               |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                              |
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 601 ms: 1.43x faster                                                |
| async_tree_io              | 838 ms                                                 | 599 ms: 1.40x faster                                                |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                                |
| richards                   | 47.5 ms                                                | 35.2 ms: 1.35x faster                                               |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                |
| richards_super             | 53.7 ms                                                | 40.6 ms: 1.32x faster                                               |
| deepcopy_memo              | 38.4 us                                                | 29.1 us: 1.32x faster                                               |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                               |
| float                      | 78.7 ms                                                | 65.9 ms: 1.19x faster                                               |
| go                         | 141 ms                                                 | 123 ms: 1.15x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 503 ms: 1.14x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.35 ms: 1.12x faster                                               |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.12x faster                                               |
| tomli_loads                | 2.12 sec                                               | 1.90 sec: 1.11x faster                                              |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 493 ms: 1.10x faster                                                |
| pylint                     | 312 ms                                                 | 283 ms: 1.10x faster                                                |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.10x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 80.7 ms: 1.08x faster                                               |
| xml_etree_process          | 60.5 ms                                                | 56.2 ms: 1.08x faster                                               |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                               |
| pyflate                    | 470 ms                                                 | 438 ms: 1.07x faster                                                |
| spectral_norm              | 113 ms                                                 | 106 ms: 1.07x faster                                                |
| dulwich_log                | 64.6 ms                                                | 60.6 ms: 1.07x faster                                               |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.06x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                              |
| bpe_tokeniser              | 4.69 sec                                               | 4.48 sec: 1.05x faster                                              |
| html5lib                   | 63.4 ms                                                | 60.6 ms: 1.05x faster                                               |
| telco                      | 8.40 ms                                                | 8.03 ms: 1.05x faster                                               |
| deltablue                  | 3.19 ms                                                | 3.07 ms: 1.04x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                               |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                               |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.03x faster                                               |
| genshi_xml                 | 50.5 ms                                                | 49.1 ms: 1.03x faster                                               |
| unpickle_pure_python       | 213 us                                                 | 207 us: 1.03x faster                                                |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                              |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                               |
| logging_silent             | 101 ns                                                 | 99.8 ns: 1.01x faster                                               |
| sympy_str                  | 273 ms                                                 | 270 ms: 1.01x faster                                                |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                |
| python_startup_no_site     | 7.00 ms                                                | 6.94 ms: 1.01x faster                                               |
| async_generators           | 433 ms                                                 | 431 ms: 1.00x faster                                                |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.01x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 735 ms: 1.01x slower                                                |
| json                       | 5.32 ms                                                | 5.39 ms: 1.01x slower                                               |
| logging_simple             | 5.65 us                                                | 5.72 us: 1.01x slower                                               |
| nqueens                    | 80.9 ms                                                | 82.1 ms: 1.01x slower                                               |
| create_gc_cycles           | 2.45 ms                                                | 2.49 ms: 1.02x slower                                               |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                               |
| gc_traversal               | 4.90 ms                                                | 4.99 ms: 1.02x slower                                               |
| logging_format             | 6.23 us                                                | 6.36 us: 1.02x slower                                               |
| scimark_sor                | 122 ms                                                 | 126 ms: 1.03x slower                                                |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                                |
| pprint_pformat             | 1.48 sec                                               | 1.53 sec: 1.03x slower                                              |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                              |
| generators                 | 28.8 ms                                                | 29.8 ms: 1.03x slower                                               |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                               |
| crypto_pyaes               | 74.7 ms                                                | 77.9 ms: 1.04x slower                                               |
| fannkuch                   | 394 ms                                                 | 411 ms: 1.05x slower                                                |
| chaos                      | 58.0 ms                                                | 61.6 ms: 1.06x slower                                               |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                               |
| typing_runtime_protocols   | 160 us                                                 | 171 us: 1.07x slower                                                |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                                |
| raytrace                   | 262 ms                                                 | 282 ms: 1.08x slower                                                |
| scimark_lu                 | 114 ms                                                 | 124 ms: 1.09x slower                                                |
| comprehensions             | 16.5 us                                                | 18.1 us: 1.09x slower                                               |
| hexiom                     | 6.08 ms                                                | 6.70 ms: 1.10x slower                                               |
| bench_thread_pool          | 818 us                                                 | 908 us: 1.11x slower                                                |
| json_loads                 | 27.2 us                                                | 30.2 us: 1.11x slower                                               |
| nbody                      | 87.7 ms                                                | 98.1 ms: 1.12x slower                                               |
| many_optionals             | 857 us                                                 | 964 us: 1.13x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 76.3 ms: 1.14x slower                                               |
| scimark_fft                | 367 ms                                                 | 419 ms: 1.14x slower                                                |
| coroutines                 | 22.2 ms                                                | 25.7 ms: 1.16x slower                                               |
| json_dumps                 | 10.1 ms                                                | 12.0 ms: 1.18x slower                                               |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.29 ms: 1.25x slower                                               |
| subparsers                 | 15.5 ms                                                | 22.8 ms: 1.48x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.8 ms: 3.45x slower                                               |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (4): sphinx, connected_components, asyncio_websockets, shortest_path
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, coverage, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250505-3.14.0a7+-454bfc5-JIT/bm-20250505-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-454bfc5.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 98.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x