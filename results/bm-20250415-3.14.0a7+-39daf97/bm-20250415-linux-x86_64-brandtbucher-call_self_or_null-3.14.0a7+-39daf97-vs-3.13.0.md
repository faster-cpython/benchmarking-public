# Results vs. 3.13.0

- fork: brandtbucher
- ref: call_self_or_null
- machine: linux-x86_64
- commit hash: 39daf97
- commit date: 2025-04-15
- overall geometric mean: 1.062x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 249 ms: 1.07x faster                                                      |
| docutils       | 2.58 sec                                               | 2.56 sec: 1.01x faster                                                    |
| html5lib       | 63.4 ms                                                | 59.9 ms: 1.06x faster                                                     |
| sphinx         | 1.03 sec                                               | 1000 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                      |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                      |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 485 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                      |
| async_generators           | 433 ms                                                 | 400 ms: 1.08x faster                                                      |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.7 ms: 1.08x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| nbody          | 87.7 ms                                                | 88.4 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.19 ms: 1.18x faster                                                     |
| regex_v8       | 26.9 ms                                                | 23.1 ms: 1.16x faster                                                     |
| regex_dna      | 220 ms                                                 | 207 ms: 1.06x faster                                                      |
| regex_compile  | 132 ms                                                 | 125 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                                      |
| tomli_loads          | 2.12 sec                                               | 1.95 sec: 1.09x faster                                                    |
| xml_etree_generate   | 86.8 ms                                                | 82.9 ms: 1.05x faster                                                     |
| xml_etree_process    | 60.5 ms                                                | 57.8 ms: 1.05x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 98.1 ms: 1.03x faster                                                     |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                      |
| unpickle_pure_python | 213 us                                                 | 230 us: 1.08x slower                                                      |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                     |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                     |
| python_startup_no_site | 7.00 ms                                                | 8.18 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                     |
| genshi_xml      | 50.5 ms                                                | 48.9 ms: 1.03x faster                                                     |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                     |
| mako            | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.21 sec: 2.11x faster                                                    |
| deepcopy                   | 354 us                                                 | 244 us: 1.45x faster                                                      |
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                      |
| deepcopy_memo              | 38.4 us                                                | 28.1 us: 1.36x faster                                                     |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                      |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                      |
| go                         | 141 ms                                                 | 111 ms: 1.27x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.59 us: 1.25x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 485 ms: 1.18x faster                                                      |
| regex_effbot               | 3.77 ms                                                | 3.19 ms: 1.18x faster                                                     |
| regex_v8                   | 26.9 ms                                                | 23.1 ms: 1.16x faster                                                     |
| spectral_norm              | 113 ms                                                 | 97.8 ms: 1.16x faster                                                     |
| richards                   | 47.5 ms                                                | 41.7 ms: 1.14x faster                                                     |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                      |
| richards_super             | 53.7 ms                                                | 47.8 ms: 1.13x faster                                                     |
| scimark_fft                | 367 ms                                                 | 335 ms: 1.09x faster                                                      |
| telco                      | 8.40 ms                                                | 7.71 ms: 1.09x faster                                                     |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 1.95 sec: 1.09x faster                                                    |
| dulwich_log                | 64.6 ms                                                | 59.7 ms: 1.08x faster                                                     |
| async_generators           | 433 ms                                                 | 400 ms: 1.08x faster                                                      |
| float                      | 78.7 ms                                                | 72.7 ms: 1.08x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                    |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                     |
| 2to3                       | 266 ms                                                 | 249 ms: 1.07x faster                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.71 ms: 1.07x faster                                                     |
| regex_dna                  | 220 ms                                                 | 207 ms: 1.06x faster                                                      |
| pyflate                    | 470 ms                                                 | 442 ms: 1.06x faster                                                      |
| html5lib                   | 63.4 ms                                                | 59.9 ms: 1.06x faster                                                     |
| logging_silent             | 101 ns                                                 | 95.8 ns: 1.06x faster                                                     |
| regex_compile              | 132 ms                                                 | 125 ms: 1.05x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                                     |
| xml_etree_generate         | 86.8 ms                                                | 82.9 ms: 1.05x faster                                                     |
| xml_etree_process          | 60.5 ms                                                | 57.8 ms: 1.05x faster                                                     |
| k_core                     | 2.37 sec                                               | 2.27 sec: 1.04x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.52 sec: 1.04x faster                                                    |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                                      |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.04x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 98.1 ms: 1.03x faster                                                     |
| sphinx                     | 1.03 sec                                               | 1000 ms: 1.03x faster                                                     |
| genshi_xml                 | 50.5 ms                                                | 48.9 ms: 1.03x faster                                                     |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                                      |
| logging_format             | 6.23 us                                                | 6.05 us: 1.03x faster                                                     |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                     |
| crypto_pyaes               | 74.7 ms                                                | 72.6 ms: 1.03x faster                                                     |
| scimark_monte_carlo        | 66.8 ms                                                | 64.9 ms: 1.03x faster                                                     |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.03x faster                                                     |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                      |
| logging_simple             | 5.65 us                                                | 5.54 us: 1.02x faster                                                     |
| nqueens                    | 80.9 ms                                                | 79.3 ms: 1.02x faster                                                     |
| sympy_expand               | 456 ms                                                 | 449 ms: 1.02x faster                                                      |
| gc_traversal               | 4.90 ms                                                | 4.82 ms: 1.02x faster                                                     |
| generators                 | 28.8 ms                                                | 28.5 ms: 1.01x faster                                                     |
| docutils                   | 2.58 sec                                               | 2.56 sec: 1.01x faster                                                    |
| sqlalchemy_declarative     | 133 ms                                                 | 132 ms: 1.01x faster                                                      |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                     |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.00x faster                                                    |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| comprehensions             | 16.5 us                                                | 16.4 us: 1.00x faster                                                     |
| create_gc_cycles           | 2.45 ms                                                | 2.45 ms: 1.00x slower                                                     |
| chaos                      | 58.0 ms                                                | 58.3 ms: 1.00x slower                                                     |
| coverage                   | 82.8 ms                                                | 83.5 ms: 1.01x slower                                                     |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                     |
| nbody                      | 87.7 ms                                                | 88.4 ms: 1.01x slower                                                     |
| mako                       | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                     |
| json                       | 5.32 ms                                                | 5.40 ms: 1.01x slower                                                     |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                                      |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.04x slower                                                     |
| fannkuch                   | 394 ms                                                 | 410 ms: 1.04x slower                                                      |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                     |
| deltablue                  | 3.19 ms                                                | 3.35 ms: 1.05x slower                                                     |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                      |
| bench_thread_pool          | 818 us                                                 | 873 us: 1.07x slower                                                      |
| many_optionals             | 857 us                                                 | 921 us: 1.08x slower                                                      |
| unpickle_pure_python       | 213 us                                                 | 230 us: 1.08x slower                                                      |
| raytrace                   | 262 ms                                                 | 283 ms: 1.08x slower                                                      |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                     |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                                     |
| python_startup_no_site     | 7.00 ms                                                | 8.18 ms: 1.17x slower                                                     |
| subparsers                 | 15.5 ms                                                | 20.5 ms: 1.33x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 82.1 ms: 3.43x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (6): scimark_lu, pprint_safe_repr, connected_components, hexiom, asyncio_websockets, shortest_path
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250415-3.14.0a7+-39daf97/bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.062x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x