# Results vs. 3.13.0

- fork: python
- ref: 5d66c55c8ad0a0aeff8d
- machine: linux-x86_64
- commit hash: 5d66c55
- commit date: 2025-02-21
- overall geometric mean: 1.050x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 253 ms: 1.05x faster                                                   |
| docutils       | 2.58 sec                                               | 2.56 sec: 1.01x faster                                                 |
| html5lib       | 63.4 ms                                                | 59.8 ms: 1.06x faster                                                  |
| sphinx         | 1.03 sec                                               | 993 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                   |
| async_tree_io              | 838 ms                                                 | 605 ms: 1.39x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 623 ms: 1.38x faster                                                   |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 327 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 484 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                   |
| async_generators           | 433 ms                                                 | 389 ms: 1.11x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.8 ms: 1.13x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| nbody          | 87.7 ms                                                | 93.6 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.06 ms: 1.23x faster                                                  |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                   |
| regex_v8       | 26.9 ms                                                | 25.4 ms: 1.06x faster                                                  |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 97.8 ms: 1.04x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 84.0 ms: 1.03x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 58.6 ms: 1.03x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 315 us: 1.04x slower                                                   |
| json_loads           | 27.2 us                                                | 30.0 us: 1.10x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                  |
| genshi_xml     | 50.5 ms                                                | 48.3 ms: 1.04x faster                                                  |
| mako           | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                   |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 605 ms: 1.39x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 623 ms: 1.38x faster                                                   |
| async_tree_none            | 350 ms                                                 | 259 ms: 1.35x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 327 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 247 ms: 1.29x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 29.8 us: 1.29x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.06 ms: 1.23x faster                                                  |
| go                         | 141 ms                                                 | 115 ms: 1.22x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.65 us: 1.22x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 484 ms: 1.18x faster                                                   |
| spectral_norm              | 113 ms                                                 | 98.0 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                   |
| pylint                     | 312 ms                                                 | 274 ms: 1.14x faster                                                   |
| float                      | 78.7 ms                                                | 69.8 ms: 1.13x faster                                                  |
| async_generators           | 433 ms                                                 | 389 ms: 1.11x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                   |
| richards                   | 47.5 ms                                                | 43.7 ms: 1.09x faster                                                  |
| pyflate                    | 470 ms                                                 | 433 ms: 1.09x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                 |
| telco                      | 8.40 ms                                                | 7.80 ms: 1.08x faster                                                  |
| richards_super             | 53.7 ms                                                | 50.3 ms: 1.07x faster                                                  |
| scimark_fft                | 367 ms                                                 | 343 ms: 1.07x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.41 sec: 1.06x faster                                                 |
| html5lib                   | 63.4 ms                                                | 59.8 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.75 ms: 1.06x faster                                                  |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 25.4 ms: 1.06x faster                                                  |
| thrift                     | 800 us                                                 | 758 us: 1.06x faster                                                   |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                  |
| 2to3                       | 266 ms                                                 | 253 ms: 1.05x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 48.3 ms: 1.04x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                   |
| sphinx                     | 1.03 sec                                               | 993 ms: 1.04x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 97.8 ms: 1.04x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 84.0 ms: 1.03x faster                                                  |
| generators                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 58.6 ms: 1.03x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 72.8 ms: 1.03x faster                                                  |
| sqlglot_normalize          | 108 ms                                                 | 105 ms: 1.02x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.79 ms: 1.02x faster                                                  |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                   |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                                 |
| shortest_path              | 487 ms                                                 | 476 ms: 1.02x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                   |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                   |
| sqlglot_parse              | 1.26 ms                                                | 1.24 ms: 1.02x faster                                                  |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 727 ms                                                 | 714 ms: 1.02x faster                                                   |
| deltablue                  | 3.19 ms                                                | 3.14 ms: 1.02x faster                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 52.6 ms: 1.02x faster                                                  |
| connected_components       | 447 ms                                                 | 440 ms: 1.01x faster                                                   |
| logging_simple             | 5.65 us                                                | 5.58 us: 1.01x faster                                                  |
| logging_format             | 6.23 us                                                | 6.15 us: 1.01x faster                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.55 ms: 1.01x faster                                                  |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.01x faster                                                 |
| docutils                   | 2.58 sec                                               | 2.56 sec: 1.01x faster                                                 |
| typing_runtime_protocols   | 160 us                                                 | 159 us: 1.01x faster                                                   |
| sympy_expand               | 456 ms                                                 | 454 ms: 1.01x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.7 ms: 1.00x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 64.8 ms: 1.00x slower                                                  |
| chaos                      | 58.0 ms                                                | 58.3 ms: 1.00x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 67.1 ms: 1.01x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.15 ms: 1.01x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                   |
| fannkuch                   | 394 ms                                                 | 402 ms: 1.02x slower                                                   |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                  |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                   |
| nqueens                    | 80.9 ms                                                | 83.3 ms: 1.03x slower                                                  |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 315 us: 1.04x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 863 us: 1.05x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                  |
| nbody                      | 87.7 ms                                                | 93.6 ms: 1.07x slower                                                  |
| coverage                   | 82.8 ms                                                | 89.5 ms: 1.08x slower                                                  |
| many_optionals             | 857 us                                                 | 934 us: 1.09x slower                                                   |
| json_loads                 | 27.2 us                                                | 30.0 us: 1.10x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.4 ms: 1.32x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (6): asyncio_websockets, create_gc_cycles, meteor_contest, django_template, logging_silent, json
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.03x