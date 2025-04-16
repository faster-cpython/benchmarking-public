# Results vs. 3.13.0

- fork: brandtbucher
- ref: call_self_or_null
- machine: linux-x86_64
- commit hash: 39daf97
- commit date: 2025-04-15
- overall geometric mean: 1.065x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 248 ms: 1.07x faster                                                      |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                    |
| html5lib       | 63.4 ms                                                | 61.2 ms: 1.04x faster                                                     |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                      |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                                      |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 483 ms: 1.19x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                                      |
| async_generators           | 433 ms                                                 | 389 ms: 1.11x faster                                                      |
| coroutines                 | 22.2 ms                                                | 22.9 ms: 1.03x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.9 ms: 1.08x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| nbody          | 87.7 ms                                                | 88.7 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.0 ms: 1.17x faster                                                     |
| regex_effbot   | 3.77 ms                                                | 3.24 ms: 1.16x faster                                                     |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                      |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.88 sec: 1.13x faster                                                    |
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.09x faster                                                      |
| xml_etree_process    | 60.5 ms                                                | 57.4 ms: 1.05x faster                                                     |
| xml_etree_generate   | 86.8 ms                                                | 82.6 ms: 1.05x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 98.1 ms: 1.03x faster                                                     |
| pickle_pure_python   | 302 us                                                 | 316 us: 1.04x slower                                                      |
| unpickle_pure_python | 213 us                                                 | 226 us: 1.06x slower                                                      |
| json_loads           | 27.2 us                                                | 30.0 us: 1.11x slower                                                     |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                     |
| python_startup_no_site | 7.00 ms                                                | 8.16 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                     |
| genshi_xml      | 50.5 ms                                                | 49.1 ms: 1.03x faster                                                     |
| django_template | 31.7 ms                                                | 31.5 ms: 1.00x faster                                                     |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.19 sec: 2.13x faster                                                    |
| deepcopy                   | 354 us                                                 | 242 us: 1.46x faster                                                      |
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                                      |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                      |
| async_tree_memoization     | 437 ms                                                 | 316 ms: 1.38x faster                                                      |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                                      |
| deepcopy_memo              | 38.4 us                                                | 28.4 us: 1.35x faster                                                     |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                      |
| go                         | 141 ms                                                 | 110 ms: 1.28x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.60 us: 1.25x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 483 ms: 1.19x faster                                                      |
| spectral_norm              | 113 ms                                                 | 95.5 ms: 1.19x faster                                                     |
| regex_v8                   | 26.9 ms                                                | 23.0 ms: 1.17x faster                                                     |
| regex_effbot               | 3.77 ms                                                | 3.24 ms: 1.16x faster                                                     |
| richards                   | 47.5 ms                                                | 41.9 ms: 1.14x faster                                                     |
| pylint                     | 312 ms                                                 | 275 ms: 1.13x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 1.88 sec: 1.13x faster                                                    |
| richards_super             | 53.7 ms                                                | 47.9 ms: 1.12x faster                                                     |
| scimark_fft                | 367 ms                                                 | 328 ms: 1.12x faster                                                      |
| pyflate                    | 470 ms                                                 | 421 ms: 1.11x faster                                                      |
| async_generators           | 433 ms                                                 | 389 ms: 1.11x faster                                                      |
| telco                      | 8.40 ms                                                | 7.55 ms: 1.11x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.57 ms: 1.10x faster                                                     |
| dulwich_log                | 64.6 ms                                                | 59.1 ms: 1.09x faster                                                     |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.09x faster                                                      |
| float                      | 78.7 ms                                                | 72.9 ms: 1.08x faster                                                     |
| 2to3                       | 266 ms                                                 | 248 ms: 1.07x faster                                                      |
| logging_silent             | 101 ns                                                 | 95.2 ns: 1.06x faster                                                     |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                      |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                     |
| scimark_sor                | 122 ms                                                 | 116 ms: 1.06x faster                                                      |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.45 sec: 1.05x faster                                                    |
| xml_etree_process          | 60.5 ms                                                | 57.4 ms: 1.05x faster                                                     |
| xml_etree_generate         | 86.8 ms                                                | 82.6 ms: 1.05x faster                                                     |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                                     |
| crypto_pyaes               | 74.7 ms                                                | 71.6 ms: 1.04x faster                                                     |
| sympy_str                  | 273 ms                                                 | 263 ms: 1.04x faster                                                      |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                    |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                    |
| scimark_monte_carlo        | 66.8 ms                                                | 64.5 ms: 1.04x faster                                                     |
| html5lib                   | 63.4 ms                                                | 61.2 ms: 1.04x faster                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 98.1 ms: 1.03x faster                                                     |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                      |
| genshi_xml                 | 50.5 ms                                                | 49.1 ms: 1.03x faster                                                     |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                    |
| nqueens                    | 80.9 ms                                                | 78.9 ms: 1.03x faster                                                     |
| sympy_expand               | 456 ms                                                 | 445 ms: 1.02x faster                                                      |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                     |
| logging_format             | 6.23 us                                                | 6.10 us: 1.02x faster                                                     |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                     |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                      |
| typing_runtime_protocols   | 160 us                                                 | 157 us: 1.02x faster                                                      |
| gc_traversal               | 4.90 ms                                                | 4.81 ms: 1.02x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                      |
| logging_simple             | 5.65 us                                                | 5.57 us: 1.01x faster                                                     |
| pprint_safe_repr           | 727 ms                                                 | 722 ms: 1.01x faster                                                      |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                    |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| django_template            | 31.7 ms                                                | 31.5 ms: 1.00x faster                                                     |
| hexiom                     | 6.08 ms                                                | 6.06 ms: 1.00x faster                                                     |
| create_gc_cycles           | 2.45 ms                                                | 2.44 ms: 1.00x faster                                                     |
| coverage                   | 82.8 ms                                                | 83.3 ms: 1.01x slower                                                     |
| shortest_path              | 487 ms                                                 | 491 ms: 1.01x slower                                                      |
| chaos                      | 58.0 ms                                                | 58.7 ms: 1.01x slower                                                     |
| nbody                      | 87.7 ms                                                | 88.7 ms: 1.01x slower                                                     |
| generators                 | 28.8 ms                                                | 29.5 ms: 1.02x slower                                                     |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                     |
| json                       | 5.32 ms                                                | 5.47 ms: 1.03x slower                                                     |
| fannkuch                   | 394 ms                                                 | 404 ms: 1.03x slower                                                      |
| coroutines                 | 22.2 ms                                                | 22.9 ms: 1.03x slower                                                     |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                     |
| pickle_pure_python         | 302 us                                                 | 316 us: 1.04x slower                                                      |
| deltablue                  | 3.19 ms                                                | 3.35 ms: 1.05x slower                                                     |
| unpickle_pure_python       | 213 us                                                 | 226 us: 1.06x slower                                                      |
| bench_thread_pool          | 818 us                                                 | 872 us: 1.07x slower                                                      |
| many_optionals             | 857 us                                                 | 920 us: 1.07x slower                                                      |
| raytrace                   | 262 ms                                                 | 282 ms: 1.08x slower                                                      |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.11x slower                                                     |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                     |
| python_startup_no_site     | 7.00 ms                                                | 8.16 ms: 1.17x slower                                                     |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.33x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (5): pprint_pformat, comprehensions, scimark_lu, asyncio_websockets, connected_components
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250415-3.14.0a7+-39daf97/bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.065x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x