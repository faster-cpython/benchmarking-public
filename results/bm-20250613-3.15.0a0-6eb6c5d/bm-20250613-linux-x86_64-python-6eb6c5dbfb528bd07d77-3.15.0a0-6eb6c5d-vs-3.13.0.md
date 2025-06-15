# Results vs. 3.13.0

- fork: python
- ref: 6eb6c5dbfb528bd07d77
- machine: linux-x86_64
- commit hash: 6eb6c5d
- commit date: 2025-06-13
- overall geometric mean: 1.032x slower
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                  |
| docutils       | 2.58 sec                                               | 2.58 sec: 1.00x faster                                                |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 307 ms: 1.51x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                                  |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 631 ms: 1.36x faster                                                  |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.30x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                                  |
| async_generators           | 433 ms                                                 | 411 ms: 1.05x faster                                                  |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                  |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.12x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.4 ms: 1.09x faster                                                 |
| pidigits       | 186 ms                                                 | 192 ms: 1.03x slower                                                  |
| nbody          | 87.7 ms                                                | 97.3 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.10 ms: 1.21x faster                                                 |
| regex_v8       | 26.9 ms                                                | 22.1 ms: 1.21x faster                                                 |
| regex_dna      | 220 ms                                                 | 184 ms: 1.20x faster                                                  |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.08x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 2.04 sec: 1.04x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 98.7 ms: 1.03x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 85.3 ms: 1.02x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 59.6 ms: 1.01x faster                                                 |
| json_loads           | 27.2 us                                                | 27.4 us: 1.01x slower                                                 |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.07x slower                                                  |
| json_dumps           | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.91 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.0 ms: 1.08x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                 |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                 |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 307 ms: 1.51x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 310 ms: 1.41x faster                                                  |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                                  |
| deepcopy                   | 354 us                                                 | 254 us: 1.40x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 631 ms: 1.36x faster                                                  |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 28.8 us: 1.33x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 245 ms: 1.30x faster                                                  |
| go                         | 141 ms                                                 | 110 ms: 1.28x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.10 ms: 1.21x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 22.1 ms: 1.21x faster                                                 |
| regex_dna                  | 220 ms                                                 | 184 ms: 1.20x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.19x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                  |
| richards                   | 47.5 ms                                                | 42.4 ms: 1.12x faster                                                 |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 490 ms: 1.11x faster                                                  |
| richards_super             | 53.7 ms                                                | 48.6 ms: 1.11x faster                                                 |
| pyflate                    | 470 ms                                                 | 427 ms: 1.10x faster                                                  |
| float                      | 78.7 ms                                                | 72.4 ms: 1.09x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.08x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 59.7 ms: 1.08x faster                                                 |
| genshi_text                | 22.6 ms                                                | 21.0 ms: 1.08x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.08x faster                                                |
| async_generators           | 433 ms                                                 | 411 ms: 1.05x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 18.9 ms: 1.05x faster                                                 |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                                |
| telco                      | 8.40 ms                                                | 8.06 ms: 1.04x faster                                                 |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| spectral_norm              | 113 ms                                                 | 109 ms: 1.04x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 2.04 sec: 1.04x faster                                                |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                                |
| comprehensions             | 16.5 us                                                | 16.0 us: 1.03x faster                                                 |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 98.7 ms: 1.03x faster                                                 |
| gc_traversal               | 4.90 ms                                                | 4.78 ms: 1.02x faster                                                 |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.02x faster                                                  |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                 |
| json                       | 5.32 ms                                                | 5.20 ms: 1.02x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 85.3 ms: 1.02x faster                                                 |
| hexiom                     | 6.08 ms                                                | 5.97 ms: 1.02x faster                                                 |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 59.6 ms: 1.01x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.91 ms: 1.01x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                 |
| sympy_expand               | 456 ms                                                 | 451 ms: 1.01x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.87 us: 1.01x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.98 ms: 1.01x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                  |
| nqueens                    | 80.9 ms                                                | 80.6 ms: 1.00x faster                                                 |
| docutils                   | 2.58 sec                                               | 2.58 sec: 1.00x faster                                                |
| crypto_pyaes               | 74.7 ms                                                | 74.5 ms: 1.00x faster                                                 |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                  |
| json_loads                 | 27.2 us                                                | 27.4 us: 1.01x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 67.6 ms: 1.01x slower                                                 |
| scimark_fft                | 367 ms                                                 | 372 ms: 1.02x slower                                                  |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                  |
| shortest_path              | 487 ms                                                 | 497 ms: 1.02x slower                                                  |
| pidigits                   | 186 ms                                                 | 192 ms: 1.03x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                  |
| fannkuch                   | 394 ms                                                 | 408 ms: 1.04x slower                                                  |
| chaos                      | 58.0 ms                                                | 60.3 ms: 1.04x slower                                                 |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                  |
| generators                 | 28.8 ms                                                | 30.0 ms: 1.04x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.59 ms: 1.06x slower                                                 |
| connected_components       | 447 ms                                                 | 474 ms: 1.06x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.07x slower                                                  |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 10.9 ms: 1.08x slower                                                 |
| deltablue                  | 3.19 ms                                                | 3.47 ms: 1.09x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 799 ms: 1.10x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.63 sec: 1.10x slower                                                |
| nbody                      | 87.7 ms                                                | 97.3 ms: 1.11x slower                                                 |
| logging_simple             | 5.65 us                                                | 6.32 us: 1.12x slower                                                 |
| many_optionals             | 857 us                                                 | 958 us: 1.12x slower                                                  |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.12x slower                                                 |
| logging_format             | 6.23 us                                                | 7.00 us: 1.12x slower                                                 |
| subparsers                 | 15.5 ms                                                | 23.4 ms: 1.51x slower                                                 |
| logging_silent             | 101 ns                                                 | 468 ns: 4.63x slower                                                  |
| coverage                   | 82.8 ms                                                | 433 ms: 5.22x slower                                                  |
| thrift                     | 800 us                                                 | 148 ms: 185.14x slower                                                |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250613-3.15.0a0-6eb6c5d/bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.032x slower

# HPT report

- Reliability score: 99.85% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x