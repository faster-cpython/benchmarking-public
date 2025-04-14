# Results vs. 3.13.0

- fork: brandtbucher
- ref: trace_generators
- machine: linux-x86_64
- commit hash: d740bda
- commit date: 2025-02-13
- overall geometric mean: 1.040x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 262 ms: 1.01x faster                                                     |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                   |
| html5lib       | 63.4 ms                                                | 61.2 ms: 1.03x faster                                                    |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 325 ms: 1.34x faster                                                     |
| async_tree_io              | 838 ms                                                 | 624 ms: 1.34x faster                                                     |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 319 ms                                                 | 258 ms: 1.24x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                     |
| async_generators           | 433 ms                                                 | 416 ms: 1.04x faster                                                     |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.4 ms: 1.13x faster                                                    |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                     |
| nbody          | 87.7 ms                                                | 90.6 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.09 ms: 1.22x faster                                                    |
| regex_v8       | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                    |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                     |
| regex_dna      | 220 ms                                                 | 210 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                  | 1.11x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                   |
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.12x faster                                                     |
| xml_etree_generate   | 86.8 ms                                                | 78.7 ms: 1.10x faster                                                    |
| xml_etree_process    | 60.5 ms                                                | 56.1 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 101 ms                                                 | 96.9 ms: 1.05x faster                                                    |
| unpickle_pure_python | 213 us                                                 | 207 us: 1.03x faster                                                     |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                                    |
| pickle_pure_python   | 302 us                                                 | 324 us: 1.07x slower                                                     |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                    |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 10.7 ms                                                | 10.2 ms: 1.05x faster                                                    |
| genshi_text    | 22.6 ms                                                | 23.1 ms: 1.02x slower                                                    |
| genshi_xml     | 50.5 ms                                                | 52.6 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.00x slower                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-brandtbucher-trace_generators-3.14.0a5+-d740bda |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 315 ms: 1.47x faster                                                     |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                     |
| deepcopy                   | 354 us                                                 | 262 us: 1.35x faster                                                     |
| async_tree_memoization     | 437 ms                                                 | 325 ms: 1.34x faster                                                     |
| async_tree_io              | 838 ms                                                 | 624 ms: 1.34x faster                                                     |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                     |
| deepcopy_memo              | 38.4 us                                                | 30.5 us: 1.26x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 258 ms: 1.24x faster                                                     |
| regex_effbot               | 3.77 ms                                                | 3.09 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                    |
| scimark_fft                | 367 ms                                                 | 312 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                     |
| spectral_norm              | 113 ms                                                 | 96.7 ms: 1.17x faster                                                    |
| tomli_loads                | 2.12 sec                                               | 1.86 sec: 1.14x faster                                                   |
| float                      | 78.7 ms                                                | 69.4 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                     |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.12x faster                                                     |
| go                         | 141 ms                                                 | 125 ms: 1.12x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.49 ms: 1.12x faster                                                    |
| regex_v8                   | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                    |
| pylint                     | 312 ms                                                 | 282 ms: 1.11x faster                                                     |
| xml_etree_generate         | 86.8 ms                                                | 78.7 ms: 1.10x faster                                                    |
| telco                      | 8.40 ms                                                | 7.79 ms: 1.08x faster                                                    |
| xml_etree_process          | 60.5 ms                                                | 56.1 ms: 1.08x faster                                                    |
| richards                   | 47.5 ms                                                | 44.2 ms: 1.08x faster                                                    |
| sqlite_synth               | 2.90 us                                                | 2.72 us: 1.07x faster                                                    |
| richards_super             | 53.7 ms                                                | 50.7 ms: 1.06x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                                   |
| pyflate                    | 470 ms                                                 | 444 ms: 1.06x faster                                                     |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.06x faster                                                    |
| thrift                     | 800 us                                                 | 760 us: 1.05x faster                                                     |
| mako                       | 10.7 ms                                                | 10.2 ms: 1.05x faster                                                    |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                     |
| regex_dna                  | 220 ms                                                 | 210 ms: 1.05x faster                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 96.9 ms: 1.05x faster                                                    |
| async_generators           | 433 ms                                                 | 416 ms: 1.04x faster                                                     |
| crypto_pyaes               | 74.7 ms                                                | 71.8 ms: 1.04x faster                                                    |
| html5lib                   | 63.4 ms                                                | 61.2 ms: 1.03x faster                                                    |
| logging_simple             | 5.65 us                                                | 5.47 us: 1.03x faster                                                    |
| json                       | 5.32 ms                                                | 5.15 ms: 1.03x faster                                                    |
| unpickle_pure_python       | 213 us                                                 | 207 us: 1.03x faster                                                     |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                   |
| logging_format             | 6.23 us                                                | 6.08 us: 1.03x faster                                                    |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.02x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                     |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                     |
| connected_components       | 447 ms                                                 | 440 ms: 1.02x faster                                                     |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                   |
| 2to3                       | 266 ms                                                 | 262 ms: 1.01x faster                                                     |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                     |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                     |
| shortest_path              | 487 ms                                                 | 482 ms: 1.01x faster                                                     |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                    |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                     |
| sqlglot_optimize           | 53.4 ms                                                | 53.6 ms: 1.00x slower                                                    |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                    |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                    |
| scimark_monte_carlo        | 66.8 ms                                                | 67.4 ms: 1.01x slower                                                    |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.01x slower                                                    |
| gc_traversal               | 4.90 ms                                                | 4.96 ms: 1.01x slower                                                    |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                    |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                     |
| chaos                      | 58.0 ms                                                | 59.0 ms: 1.02x slower                                                    |
| pprint_safe_repr           | 727 ms                                                 | 740 ms: 1.02x slower                                                     |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                                     |
| sympy_expand               | 456 ms                                                 | 466 ms: 1.02x slower                                                     |
| genshi_text                | 22.6 ms                                                | 23.1 ms: 1.02x slower                                                    |
| sqlglot_transpile          | 1.57 ms                                                | 1.61 ms: 1.02x slower                                                    |
| fannkuch                   | 394 ms                                                 | 404 ms: 1.03x slower                                                     |
| sqlglot_parse              | 1.26 ms                                                | 1.30 ms: 1.03x slower                                                    |
| pprint_pformat             | 1.48 sec                                               | 1.52 sec: 1.03x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                   |
| logging_silent             | 101 ns                                                 | 104 ns: 1.03x slower                                                     |
| nbody                      | 87.7 ms                                                | 90.6 ms: 1.03x slower                                                    |
| genshi_xml                 | 50.5 ms                                                | 52.6 ms: 1.04x slower                                                    |
| deltablue                  | 3.19 ms                                                | 3.34 ms: 1.05x slower                                                    |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                     |
| dulwich_log                | 64.6 ms                                                | 67.8 ms: 1.05x slower                                                    |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                    |
| comprehensions             | 16.5 us                                                | 17.4 us: 1.05x slower                                                    |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                                    |
| pickle_pure_python         | 302 us                                                 | 324 us: 1.07x slower                                                     |
| bench_thread_pool          | 818 us                                                 | 882 us: 1.08x slower                                                     |
| coverage                   | 82.8 ms                                                | 90.1 ms: 1.09x slower                                                    |
| hexiom                     | 6.08 ms                                                | 6.64 ms: 1.09x slower                                                    |
| many_optionals             | 857 us                                                 | 954 us: 1.11x slower                                                     |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                    |
| generators                 | 28.8 ms                                                | 34.9 ms: 1.21x slower                                                    |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.36x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                             |

Benchmark hidden because not significant (5): nqueens, meteor_contest, sympy_str, asyncio_websockets, django_template
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x