# Results vs. 3.13.0

- fork: iritkatriel
- ref: gh_100239
- machine: linux-x86_64
- commit hash: 7264e37
- commit date: 2025-01-10
- overall geometric mean: 1.046x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                             |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.01x slower                                           |
| html5lib       | 63.4 ms                                                | 61.3 ms: 1.03x faster                                            |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                             |
| async_tree_io_tg           | 861 ms                                                 | 587 ms: 1.47x faster                                             |
| async_tree_io              | 838 ms                                                 | 604 ms: 1.39x faster                                             |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                             |
| async_tree_memoization     | 437 ms                                                 | 325 ms: 1.34x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                             |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 483 ms: 1.19x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 461 ms: 1.18x faster                                             |
| async_generators           | 433 ms                                                 | 421 ms: 1.03x faster                                             |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                            |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                     |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.9 ms: 1.09x faster                                            |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                             |
| nbody          | 87.7 ms                                                | 94.2 ms: 1.07x slower                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.48 ms: 1.08x faster                                            |
| regex_v8       | 26.9 ms                                                | 25.5 ms: 1.05x faster                                            |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                             |
| tomli_loads          | 2.12 sec                                               | 1.91 sec: 1.11x faster                                           |
| xml_etree_iterparse  | 101 ms                                                 | 97.5 ms: 1.04x faster                                            |
| json_loads           | 27.2 us                                                | 26.5 us: 1.03x faster                                            |
| xml_etree_generate   | 86.8 ms                                                | 85.3 ms: 1.02x faster                                            |
| xml_etree_process    | 60.5 ms                                                | 59.5 ms: 1.02x faster                                            |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                             |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.06x slower                                             |
| json_dumps           | 10.1 ms                                                | 11.4 ms: 1.13x slower                                            |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.04 ms: 1.01x slower                                            |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                            |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 49.2 ms: 1.03x faster                                            |
| genshi_text     | 22.6 ms                                                | 22.2 ms: 1.02x faster                                            |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                            |
| mako            | 10.7 ms                                                | 11.5 ms: 1.08x slower                                            |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 308 ms: 1.50x faster                                             |
| async_tree_io_tg           | 861 ms                                                 | 587 ms: 1.47x faster                                             |
| async_tree_io              | 838 ms                                                 | 604 ms: 1.39x faster                                             |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                             |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                             |
| async_tree_memoization     | 437 ms                                                 | 325 ms: 1.34x faster                                             |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                             |
| deepcopy_memo              | 38.4 us                                                | 31.2 us: 1.23x faster                                            |
| go                         | 141 ms                                                 | 115 ms: 1.22x faster                                             |
| deepcopy_reduce            | 3.24 us                                                | 2.68 us: 1.21x faster                                            |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 483 ms: 1.19x faster                                             |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 461 ms: 1.18x faster                                             |
| spectral_norm              | 113 ms                                                 | 96.3 ms: 1.18x faster                                            |
| pylint                     | 312 ms                                                 | 277 ms: 1.13x faster                                             |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                             |
| tomli_loads                | 2.12 sec                                               | 1.91 sec: 1.11x faster                                           |
| float                      | 78.7 ms                                                | 71.9 ms: 1.09x faster                                            |
| json                       | 5.32 ms                                                | 4.91 ms: 1.08x faster                                            |
| regex_effbot               | 3.77 ms                                                | 3.48 ms: 1.08x faster                                            |
| telco                      | 8.40 ms                                                | 7.77 ms: 1.08x faster                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.66 ms: 1.08x faster                                            |
| richards                   | 47.5 ms                                                | 44.2 ms: 1.08x faster                                            |
| pyflate                    | 470 ms                                                 | 437 ms: 1.07x faster                                             |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.07x faster                                            |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                           |
| richards_super             | 53.7 ms                                                | 50.8 ms: 1.06x faster                                            |
| regex_v8                   | 26.9 ms                                                | 25.5 ms: 1.05x faster                                            |
| scimark_fft                | 367 ms                                                 | 349 ms: 1.05x faster                                             |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                             |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.04x faster                                             |
| thrift                     | 800 us                                                 | 769 us: 1.04x faster                                             |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                           |
| xml_etree_iterparse        | 101 ms                                                 | 97.5 ms: 1.04x faster                                            |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                            |
| crypto_pyaes               | 74.7 ms                                                | 72.0 ms: 1.04x faster                                            |
| html5lib                   | 63.4 ms                                                | 61.3 ms: 1.03x faster                                            |
| generators                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                            |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                             |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                             |
| async_generators           | 433 ms                                                 | 421 ms: 1.03x faster                                             |
| genshi_xml                 | 50.5 ms                                                | 49.2 ms: 1.03x faster                                            |
| json_loads                 | 27.2 us                                                | 26.5 us: 1.03x faster                                            |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.5 ms: 1.03x faster                                            |
| bpe_tokeniser              | 4.69 sec                                               | 4.58 sec: 1.02x faster                                           |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                             |
| nqueens                    | 80.9 ms                                                | 79.4 ms: 1.02x faster                                            |
| xml_etree_generate         | 86.8 ms                                                | 85.3 ms: 1.02x faster                                            |
| genshi_text                | 22.6 ms                                                | 22.2 ms: 1.02x faster                                            |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.02x faster                                             |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                           |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                             |
| dulwich_log                | 64.6 ms                                                | 63.5 ms: 1.02x faster                                            |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.02x faster                                             |
| xml_etree_process          | 60.5 ms                                                | 59.5 ms: 1.02x faster                                            |
| mdp                        | 2.54 sec                                               | 2.51 sec: 1.01x faster                                           |
| sqlglot_optimize           | 53.4 ms                                                | 52.7 ms: 1.01x faster                                            |
| shortest_path              | 487 ms                                                 | 480 ms: 1.01x faster                                             |
| gc_traversal               | 4.90 ms                                                | 4.85 ms: 1.01x faster                                            |
| pprint_safe_repr           | 727 ms                                                 | 722 ms: 1.01x faster                                             |
| logging_format             | 6.23 us                                                | 6.20 us: 1.01x faster                                            |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                             |
| chaos                      | 58.0 ms                                                | 57.9 ms: 1.00x faster                                            |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.01x slower                                            |
| python_startup_no_site     | 7.00 ms                                                | 7.04 ms: 1.01x slower                                            |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                           |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.01x slower                                            |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.01x slower                                           |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.01x slower                                            |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.01x slower                                             |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                            |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                            |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                             |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                            |
| deltablue                  | 3.19 ms                                                | 3.23 ms: 1.01x slower                                            |
| fannkuch                   | 394 ms                                                 | 399 ms: 1.01x slower                                             |
| scimark_monte_carlo        | 66.8 ms                                                | 67.7 ms: 1.01x slower                                            |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                             |
| coverage                   | 82.8 ms                                                | 84.5 ms: 1.02x slower                                            |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                            |
| hexiom                     | 6.08 ms                                                | 6.23 ms: 1.03x slower                                            |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                             |
| bench_thread_pool          | 818 us                                                 | 861 us: 1.05x slower                                             |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                            |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.06x slower                                             |
| nbody                      | 87.7 ms                                                | 94.2 ms: 1.07x slower                                            |
| logging_silent             | 101 ns                                                 | 109 ns: 1.08x slower                                             |
| mako                       | 10.7 ms                                                | 11.5 ms: 1.08x slower                                            |
| many_optionals             | 857 us                                                 | 941 us: 1.10x slower                                             |
| json_dumps                 | 10.1 ms                                                | 11.4 ms: 1.13x slower                                            |
| subparsers                 | 15.5 ms                                                | 20.3 ms: 1.32x slower                                            |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                     |

Benchmark hidden because not significant (5): regex_dna, logging_simple, typing_runtime_protocols, sympy_expand, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x