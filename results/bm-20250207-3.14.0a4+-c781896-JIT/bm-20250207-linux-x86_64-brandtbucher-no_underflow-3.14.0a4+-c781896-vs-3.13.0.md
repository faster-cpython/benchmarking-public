# Results vs. 3.13.0

- fork: brandtbucher
- ref: no_underflow
- machine: linux-x86_64
- commit hash: c781896
- commit date: 2025-02-07
- overall geometric mean: 1.052x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 259 ms: 1.03x faster                                                 |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.03x slower                                               |
| html5lib       | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 627 ms: 1.37x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 325 ms: 1.34x faster                                                 |
| async_tree_io              | 838 ms                                                 | 626 ms: 1.34x faster                                                 |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 259 ms: 1.23x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                 |
| async_generators           | 433 ms                                                 | 409 ms: 1.06x faster                                                 |
| coroutines                 | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                         |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.5 ms: 1.13x faster                                                |
| nbody          | 87.7 ms                                                | 94.3 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.05 ms: 1.23x faster                                                |
| regex_v8       | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                |
| regex_dna      | 220 ms                                                 | 204 ms: 1.08x faster                                                 |
| regex_compile  | 132 ms                                                 | 125 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.83 sec: 1.16x faster                                               |
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.13x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 78.3 ms: 1.11x faster                                                |
| xml_etree_process    | 60.5 ms                                                | 55.1 ms: 1.10x faster                                                |
| unpickle_pure_python | 213 us                                                 | 198 us: 1.08x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 96.4 ms: 1.05x faster                                                |
| json_loads           | 27.2 us                                                | 28.6 us: 1.05x slower                                                |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                 |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.15x slower                                                |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 9.91 ms: 1.08x faster                                                |
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                |
| genshi_xml      | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                |
| django_template | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                                 |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 627 ms: 1.37x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 325 ms: 1.34x faster                                                 |
| async_tree_io              | 838 ms                                                 | 626 ms: 1.34x faster                                                 |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                 |
| deepcopy_memo              | 38.4 us                                                | 30.7 us: 1.25x faster                                                |
| regex_effbot               | 3.77 ms                                                | 3.05 ms: 1.23x faster                                                |
| async_tree_none_tg         | 319 ms                                                 | 259 ms: 1.23x faster                                                 |
| spectral_norm              | 113 ms                                                 | 92.0 ms: 1.23x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                                |
| go                         | 141 ms                                                 | 118 ms: 1.19x faster                                                 |
| scimark_fft                | 367 ms                                                 | 314 ms: 1.17x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 1.83 sec: 1.16x faster                                               |
| float                      | 78.7 ms                                                | 69.5 ms: 1.13x faster                                                |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.13x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                 |
| pylint                     | 312 ms                                                 | 278 ms: 1.12x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 78.3 ms: 1.11x faster                                                |
| pyflate                    | 470 ms                                                 | 428 ms: 1.10x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 55.1 ms: 1.10x faster                                                |
| telco                      | 8.40 ms                                                | 7.68 ms: 1.09x faster                                                |
| richards                   | 47.5 ms                                                | 43.5 ms: 1.09x faster                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.61 ms: 1.09x faster                                                |
| pathlib                    | 17.4 ms                                                | 16.0 ms: 1.09x faster                                                |
| richards_super             | 53.7 ms                                                | 49.7 ms: 1.08x faster                                                |
| regex_dna                  | 220 ms                                                 | 204 ms: 1.08x faster                                                 |
| mako                       | 10.7 ms                                                | 9.91 ms: 1.08x faster                                                |
| unpickle_pure_python       | 213 us                                                 | 198 us: 1.08x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.36 sec: 1.07x faster                                               |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                                |
| async_generators           | 433 ms                                                 | 409 ms: 1.06x faster                                                 |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                |
| regex_compile              | 132 ms                                                 | 125 ms: 1.05x faster                                                 |
| thrift                     | 800 us                                                 | 759 us: 1.05x faster                                                 |
| crypto_pyaes               | 74.7 ms                                                | 71.1 ms: 1.05x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 96.4 ms: 1.05x faster                                                |
| json                       | 5.32 ms                                                | 5.13 ms: 1.04x faster                                                |
| generators                 | 28.8 ms                                                | 27.8 ms: 1.04x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                               |
| 2to3                       | 266 ms                                                 | 259 ms: 1.03x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                               |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                 |
| html5lib                   | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                               |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                               |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.02x faster                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                 |
| connected_components       | 447 ms                                                 | 441 ms: 1.01x faster                                                 |
| logging_simple             | 5.65 us                                                | 5.59 us: 1.01x faster                                                |
| shortest_path              | 487 ms                                                 | 481 ms: 1.01x faster                                                 |
| fannkuch                   | 394 ms                                                 | 390 ms: 1.01x faster                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 66.2 ms: 1.01x faster                                                |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.01x faster                                               |
| logging_format             | 6.23 us                                                | 6.19 us: 1.01x faster                                                |
| sqlglot_optimize           | 53.4 ms                                                | 53.6 ms: 1.00x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.01x slower                                                |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                |
| gc_traversal               | 4.90 ms                                                | 4.94 ms: 1.01x slower                                                |
| deltablue                  | 3.19 ms                                                | 3.22 ms: 1.01x slower                                                |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                |
| chaos                      | 58.0 ms                                                | 58.6 ms: 1.01x slower                                                |
| django_template            | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                |
| sympy_integrate            | 19.8 ms                                                | 20.0 ms: 1.01x slower                                                |
| coroutines                 | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                |
| dulwich_log                | 64.6 ms                                                | 65.7 ms: 1.02x slower                                                |
| nqueens                    | 80.9 ms                                                | 82.6 ms: 1.02x slower                                                |
| sympy_expand               | 456 ms                                                 | 468 ms: 1.03x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.03x slower                                               |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.35 ms: 1.05x slower                                                |
| logging_silent             | 101 ns                                                 | 106 ns: 1.05x slower                                                 |
| json_loads                 | 27.2 us                                                | 28.6 us: 1.05x slower                                                |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 871 us: 1.07x slower                                                 |
| nbody                      | 87.7 ms                                                | 94.3 ms: 1.08x slower                                                |
| coverage                   | 82.8 ms                                                | 89.9 ms: 1.09x slower                                                |
| many_optionals             | 857 us                                                 | 948 us: 1.11x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.15x slower                                                |
| subparsers                 | 15.5 ms                                                | 20.3 ms: 1.32x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 80.8 ms: 3.37x slower                                                |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                         |

Benchmark hidden because not significant (9): pprint_safe_repr, sqlalchemy_imperative, sympy_sum, typing_runtime_protocols, sympy_str, pidigits, asyncio_websockets, sqlglot_parse, scimark_lu
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x