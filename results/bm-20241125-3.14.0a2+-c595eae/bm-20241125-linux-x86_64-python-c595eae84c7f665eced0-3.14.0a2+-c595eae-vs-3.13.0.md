# Results vs. 3.13.0

- fork: python
- ref: c595eae84c7f665eced0
- machine: linux-x86_64
- commit hash: c595eae
- commit date: 2024-11-25
- overall geometric mean: 1.001x slower
- HPT reliability: 76.11%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                   |
| docutils       | 2.58 sec                                               | 2.68 sec: 1.03x slower                                                 |
| html5lib       | 63.4 ms                                                | 64.0 ms: 1.01x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.06 sec: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 393 ms: 1.18x faster                                                   |
| async_tree_none            | 350 ms                                                 | 324 ms: 1.08x faster                                                   |
| async_generators           | 433 ms                                                 | 431 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 571 ms: 1.05x slower                                                   |
| async_tree_none_tg         | 319 ms                                                 | 340 ms: 1.07x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                  |
| async_tree_io_tg           | 861 ms                                                 | 928 ms: 1.08x slower                                                   |
| async_tree_io              | 838 ms                                                 | 934 ms: 1.11x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_memoization, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| float          | 78.7 ms                                                | 82.5 ms: 1.05x slower                                                  |
| nbody          | 87.7 ms                                                | 96.4 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.46 ms: 1.09x faster                                                  |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                   |
| regex_dna      | 220 ms                                                 | 226 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_loads           | 27.2 us                                                | 26.0 us: 1.05x faster                                                  |
| xml_etree_parse      | 154 ms                                                 | 150 ms: 1.03x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 2.09 sec: 1.01x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 86.0 ms: 1.01x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.02x slower                                                   |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.03x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 329 us: 1.09x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                  |
| genshi_text     | 22.6 ms                                                | 22.4 ms: 1.01x faster                                                  |
| django_template | 31.7 ms                                                | 31.8 ms: 1.01x slower                                                  |
| mako            | 10.7 ms                                                | 11.6 ms: 1.08x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 354 us                                                 | 264 us: 1.34x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 31.2 us: 1.23x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                                  |
| pylint                     | 312 ms                                                 | 263 ms: 1.19x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 393 ms: 1.18x faster                                                   |
| go                         | 141 ms                                                 | 121 ms: 1.16x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                  |
| json                       | 5.32 ms                                                | 4.84 ms: 1.10x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.46 ms: 1.09x faster                                                  |
| async_tree_none            | 350 ms                                                 | 324 ms: 1.08x faster                                                   |
| pathlib                    | 17.4 ms                                                | 16.1 ms: 1.08x faster                                                  |
| telco                      | 8.40 ms                                                | 7.88 ms: 1.07x faster                                                  |
| generators                 | 28.8 ms                                                | 27.3 ms: 1.05x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                   |
| json_loads                 | 27.2 us                                                | 26.0 us: 1.05x faster                                                  |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                   |
| thrift                     | 800 us                                                 | 777 us: 1.03x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 150 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.91 ms: 1.02x faster                                                  |
| richards                   | 47.5 ms                                                | 46.4 ms: 1.02x faster                                                  |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.80 ms: 1.02x faster                                                  |
| richards_super             | 53.7 ms                                                | 52.7 ms: 1.02x faster                                                  |
| logging_format             | 6.23 us                                                | 6.11 us: 1.02x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.85 us: 1.02x faster                                                  |
| connected_components       | 447 ms                                                 | 439 ms: 1.02x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                  |
| shortest_path              | 487 ms                                                 | 480 ms: 1.01x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 73.7 ms: 1.01x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.01x faster                                                 |
| sympy_str                  | 273 ms                                                 | 270 ms: 1.01x faster                                                   |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| logging_simple             | 5.65 us                                                | 5.59 us: 1.01x faster                                                  |
| mdp                        | 2.54 sec                                               | 2.52 sec: 1.01x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 2.09 sec: 1.01x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 86.0 ms: 1.01x faster                                                  |
| genshi_text                | 22.6 ms                                                | 22.4 ms: 1.01x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 64.1 ms: 1.01x faster                                                  |
| async_generators           | 433 ms                                                 | 431 ms: 1.01x faster                                                   |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| django_template            | 31.7 ms                                                | 31.8 ms: 1.01x slower                                                  |
| pyflate                    | 470 ms                                                 | 472 ms: 1.01x slower                                                   |
| sympy_integrate            | 19.8 ms                                                | 20.0 ms: 1.01x slower                                                  |
| html5lib                   | 63.4 ms                                                | 64.0 ms: 1.01x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 738 ms: 1.02x slower                                                   |
| spectral_norm              | 113 ms                                                 | 115 ms: 1.02x slower                                                   |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 104 ms: 1.02x slower                                                   |
| scimark_fft                | 367 ms                                                 | 376 ms: 1.02x slower                                                   |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.03x slower                                                   |
| sphinx                     | 1.03 sec                                               | 1.06 sec: 1.03x slower                                                 |
| coverage                   | 82.8 ms                                                | 85.1 ms: 1.03x slower                                                  |
| regex_dna                  | 220 ms                                                 | 226 ms: 1.03x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.68 sec: 1.03x slower                                                 |
| deltablue                  | 3.19 ms                                                | 3.31 ms: 1.04x slower                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.87 sec: 1.04x slower                                                 |
| fannkuch                   | 394 ms                                                 | 409 ms: 1.04x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 851 us: 1.04x slower                                                   |
| scimark_sor                | 122 ms                                                 | 128 ms: 1.05x slower                                                   |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                   |
| float                      | 78.7 ms                                                | 82.5 ms: 1.05x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 70.1 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 571 ms: 1.05x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.43 ms: 1.06x slower                                                  |
| chaos                      | 58.0 ms                                                | 61.6 ms: 1.06x slower                                                  |
| async_tree_none_tg         | 319 ms                                                 | 340 ms: 1.07x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                  |
| logging_silent             | 101 ns                                                 | 109 ns: 1.07x slower                                                   |
| async_tree_io_tg           | 861 ms                                                 | 928 ms: 1.08x slower                                                   |
| mako                       | 10.7 ms                                                | 11.6 ms: 1.08x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 329 us: 1.09x slower                                                   |
| many_optionals             | 857 us                                                 | 942 us: 1.10x slower                                                   |
| nbody                      | 87.7 ms                                                | 96.4 ms: 1.10x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.72 ms: 1.11x slower                                                  |
| async_tree_io              | 838 ms                                                 | 934 ms: 1.11x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                  |
| k_core                     | 2.37 sec                                               | 2.91 sec: 1.23x slower                                                 |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 80.6 ms: 3.36x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_memoization, djangocms, sqlalchemy_imperative, sympy_expand, typing_runtime_protocols, nqueens, asyncio_websockets
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20241125-3.14.0a2+-c595eae/bm-20241125-linux-x86_64-python-c595eae84c7f665eced0-3.14.0a2+-c595eae.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, dask, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 76.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x