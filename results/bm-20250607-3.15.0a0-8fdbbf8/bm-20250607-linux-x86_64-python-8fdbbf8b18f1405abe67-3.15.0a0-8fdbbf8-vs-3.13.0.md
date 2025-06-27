# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.044x faster
- HPT reliability: 99.81%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                  |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.00x faster                                                |
| html5lib       | 63.4 ms                                                | 61.8 ms: 1.03x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                  |
| async_tree_io              | 838 ms                                                 | 595 ms: 1.41x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.40x faster                                                  |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 494 ms: 1.10x faster                                                  |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                  |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.1 ms: 1.11x faster                                                 |
| pidigits       | 186 ms                                                 | 192 ms: 1.03x slower                                                  |
| nbody          | 87.7 ms                                                | 98.2 ms: 1.12x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.06 ms: 1.23x faster                                                 |
| regex_v8       | 26.9 ms                                                | 22.4 ms: 1.20x faster                                                 |
| regex_dna      | 220 ms                                                 | 188 ms: 1.17x faster                                                  |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 144 ms: 1.07x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 2.02 sec: 1.05x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 99.3 ms: 1.02x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 85.9 ms: 1.01x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                  |
| json_loads           | 27.2 us                                                | 28.4 us: 1.05x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                  |
| json_dumps           | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.1 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.90 ms: 1.02x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                 |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                 |
| mako            | 10.7 ms                                                | 11.7 ms: 1.09x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                  |
| async_tree_io              | 838 ms                                                 | 595 ms: 1.41x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.40x faster                                                  |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                                  |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 28.9 us: 1.33x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                  |
| go                         | 141 ms                                                 | 111 ms: 1.27x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.06 ms: 1.23x faster                                                 |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 22.4 ms: 1.20x faster                                                 |
| regex_dna                  | 220 ms                                                 | 188 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 505 ms: 1.13x faster                                                  |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                  |
| richards                   | 47.5 ms                                                | 42.9 ms: 1.11x faster                                                 |
| float                      | 78.7 ms                                                | 71.1 ms: 1.11x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 494 ms: 1.10x faster                                                  |
| richards_super             | 53.7 ms                                                | 49.0 ms: 1.10x faster                                                 |
| pyflate                    | 470 ms                                                 | 430 ms: 1.09x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 59.2 ms: 1.09x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 144 ms: 1.07x faster                                                  |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                 |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 18.9 ms: 1.05x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 2.02 sec: 1.05x faster                                                |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                  |
| thrift                     | 800 us                                                 | 767 us: 1.04x faster                                                  |
| python_startup             | 12.7 ms                                                | 12.1 ms: 1.04x faster                                                 |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.52 sec: 1.04x faster                                                |
| comprehensions             | 16.5 us                                                | 15.9 us: 1.04x faster                                                 |
| telco                      | 8.40 ms                                                | 8.12 ms: 1.03x faster                                                 |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.03x faster                                                  |
| html5lib                   | 63.4 ms                                                | 61.8 ms: 1.03x faster                                                 |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.91 ms: 1.02x faster                                                 |
| spectral_norm              | 113 ms                                                 | 111 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 99.3 ms: 1.02x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.85 us: 1.02x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.90 ms: 1.02x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 85.9 ms: 1.01x faster                                                 |
| sympy_expand               | 456 ms                                                 | 451 ms: 1.01x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.84 ms: 1.01x faster                                                 |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                  |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.00x faster                                                |
| nqueens                    | 80.9 ms                                                | 81.4 ms: 1.01x slower                                                 |
| crypto_pyaes               | 74.7 ms                                                | 75.3 ms: 1.01x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 67.9 ms: 1.02x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                  |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.03x slower                                                  |
| raytrace                   | 262 ms                                                 | 269 ms: 1.03x slower                                                  |
| pidigits                   | 186 ms                                                 | 192 ms: 1.03x slower                                                  |
| shortest_path              | 487 ms                                                 | 503 ms: 1.03x slower                                                  |
| scimark_fft                | 367 ms                                                 | 380 ms: 1.03x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                  |
| chaos                      | 58.0 ms                                                | 60.6 ms: 1.04x slower                                                 |
| json_loads                 | 27.2 us                                                | 28.4 us: 1.05x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.57 ms: 1.05x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                  |
| coverage                   | 82.8 ms                                                | 87.4 ms: 1.06x slower                                                 |
| connected_components       | 447 ms                                                 | 478 ms: 1.07x slower                                                  |
| logging_simple             | 5.65 us                                                | 6.08 us: 1.07x slower                                                 |
| generators                 | 28.8 ms                                                | 31.0 ms: 1.08x slower                                                 |
| logging_format             | 6.23 us                                                | 6.72 us: 1.08x slower                                                 |
| fannkuch                   | 394 ms                                                 | 425 ms: 1.08x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.61 sec: 1.09x slower                                                |
| deltablue                  | 3.19 ms                                                | 3.48 ms: 1.09x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 794 ms: 1.09x slower                                                  |
| mako                       | 10.7 ms                                                | 11.7 ms: 1.09x slower                                                 |
| many_optionals             | 857 us                                                 | 957 us: 1.12x slower                                                  |
| nbody                      | 87.7 ms                                                | 98.2 ms: 1.12x slower                                                 |
| coroutines                 | 22.2 ms                                                | 25.1 ms: 1.13x slower                                                 |
| subparsers                 | 15.5 ms                                                | 23.3 ms: 1.51x slower                                                 |
| logging_silent             | 101 ns                                                 | 473 ns: 4.68x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (5): djangocms, hexiom, json, asyncio_websockets, xml_etree_process
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 99.81% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x