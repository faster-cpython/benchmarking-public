# Results vs. 3.13.0

- fork: python
- ref: 1b27f36eb0ef146aa60b
- machine: linux-x86_64
- commit hash: 1b27f36
- commit date: 2025-02-13
- overall geometric mean: 1.068x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 253 ms: 1.05x faster                                                   |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                 |
| html5lib       | 63.4 ms                                                | 57.8 ms: 1.10x faster                                                  |
| sphinx         | 1.03 sec                                               | 987 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                                   |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 528 ms: 1.08x faster                                                   |
| async_generators           | 433 ms                                                 | 403 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 517 ms: 1.05x faster                                                   |
| coroutines                 | 22.2 ms                                                | 22.1 ms: 1.00x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.8 ms: 1.19x faster                                                  |
| nbody          | 87.7 ms                                                | 92.7 ms: 1.06x slower                                                  |
| pidigits       | 186 ms                                                 | 212 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.11 ms: 1.21x faster                                                  |
| regex_dna      | 220 ms                                                 | 197 ms: 1.12x faster                                                   |
| regex_v8       | 26.9 ms                                                | 24.6 ms: 1.09x faster                                                  |
| regex_compile  | 132 ms                                                 | 123 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.81 sec: 1.17x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 55.3 ms: 1.09x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 79.7 ms: 1.09x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 208 us: 1.03x faster                                                   |
| xml_etree_parse      | 154 ms                                                 | 155 ms: 1.01x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 309 us: 1.02x slower                                                   |
| json_loads           | 27.2 us                                                | 30.2 us: 1.11x slower                                                  |
| json_dumps           | 10.1 ms                                                | 12.3 ms: 1.21x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.00 ms: 1.00x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.7 ms: 1.00x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 20.8 ms: 1.09x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 48.0 ms: 1.05x faster                                                  |
| django_template | 31.7 ms                                                | 30.6 ms: 1.03x faster                                                  |
| mako            | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-python-1b27f36eb0ef146aa60b-3.14.0a5+-1b27f36 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.47x faster                                                   |
| deepcopy                   | 354 us                                                 | 243 us: 1.46x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                   |
| spectral_norm              | 113 ms                                                 | 81.9 ms: 1.38x faster                                                  |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 28.2 us: 1.36x faster                                                  |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.50 us: 1.30x faster                                                  |
| scimark_fft                | 367 ms                                                 | 284 ms: 1.29x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 3.99 ms: 1.26x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.11 ms: 1.21x faster                                                  |
| float                      | 78.7 ms                                                | 65.8 ms: 1.19x faster                                                  |
| telco                      | 8.40 ms                                                | 7.07 ms: 1.19x faster                                                  |
| richards                   | 47.5 ms                                                | 40.2 ms: 1.18x faster                                                  |
| pathlib                    | 17.4 ms                                                | 14.7 ms: 1.18x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.81 sec: 1.17x faster                                                 |
| pyflate                    | 470 ms                                                 | 403 ms: 1.16x faster                                                   |
| go                         | 141 ms                                                 | 121 ms: 1.16x faster                                                   |
| scimark_sor                | 122 ms                                                 | 106 ms: 1.15x faster                                                   |
| richards_super             | 53.7 ms                                                | 47.1 ms: 1.14x faster                                                  |
| pylint                     | 312 ms                                                 | 274 ms: 1.14x faster                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 58.7 ms: 1.14x faster                                                  |
| regex_dna                  | 220 ms                                                 | 197 ms: 1.12x faster                                                   |
| logging_silent             | 101 ns                                                 | 91.0 ns: 1.11x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.63 us: 1.10x faster                                                  |
| html5lib                   | 63.4 ms                                                | 57.8 ms: 1.10x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 55.3 ms: 1.09x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 24.6 ms: 1.09x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 79.7 ms: 1.09x faster                                                  |
| genshi_text                | 22.6 ms                                                | 20.8 ms: 1.09x faster                                                  |
| scimark_lu                 | 114 ms                                                 | 105 ms: 1.09x faster                                                   |
| thrift                     | 800 us                                                 | 736 us: 1.09x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 528 ms: 1.08x faster                                                   |
| async_generators           | 433 ms                                                 | 403 ms: 1.07x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                 |
| regex_compile              | 132 ms                                                 | 123 ms: 1.07x faster                                                   |
| chaos                      | 58.0 ms                                                | 54.3 ms: 1.07x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.41 sec: 1.06x faster                                                 |
| generators                 | 28.8 ms                                                | 27.3 ms: 1.05x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 48.0 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 517 ms: 1.05x faster                                                   |
| typing_runtime_protocols   | 160 us                                                 | 153 us: 1.05x faster                                                   |
| 2to3                       | 266 ms                                                 | 253 ms: 1.05x faster                                                   |
| nqueens                    | 80.9 ms                                                | 77.1 ms: 1.05x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.39 us: 1.05x faster                                                  |
| logging_format             | 6.23 us                                                | 5.94 us: 1.05x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                   |
| sphinx                     | 1.03 sec                                               | 987 ms: 1.05x faster                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.2 ms: 1.04x faster                                                  |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                   |
| django_template            | 31.7 ms                                                | 30.6 ms: 1.03x faster                                                  |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.3 ms: 1.03x faster                                                  |
| unpickle_pure_python       | 213 us                                                 | 208 us: 1.03x faster                                                   |
| coverage                   | 82.8 ms                                                | 80.8 ms: 1.03x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 73.2 ms: 1.02x faster                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.55 ms: 1.01x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.83 ms: 1.01x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 63.9 ms: 1.01x faster                                                  |
| raytrace                   | 262 ms                                                 | 259 ms: 1.01x faster                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 53.1 ms: 1.01x faster                                                  |
| coroutines                 | 22.2 ms                                                | 22.1 ms: 1.00x faster                                                  |
| sympy_expand               | 456 ms                                                 | 454 ms: 1.00x faster                                                   |
| python_startup_no_site     | 7.00 ms                                                | 7.00 ms: 1.00x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.7 ms: 1.00x slower                                                  |
| xml_etree_parse            | 154 ms                                                 | 155 ms: 1.01x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                 |
| deltablue                  | 3.19 ms                                                | 3.25 ms: 1.02x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 741 ms: 1.02x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 309 us: 1.02x slower                                                   |
| connected_components       | 447 ms                                                 | 457 ms: 1.02x slower                                                   |
| json                       | 5.32 ms                                                | 5.45 ms: 1.02x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 839 us: 1.03x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.53 ms: 1.03x slower                                                  |
| meteor_contest             | 108 ms                                                 | 112 ms: 1.04x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.54 sec: 1.04x slower                                                 |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                  |
| nbody                      | 87.7 ms                                                | 92.7 ms: 1.06x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.51 ms: 1.07x slower                                                  |
| many_optionals             | 857 us                                                 | 930 us: 1.09x slower                                                   |
| json_loads                 | 27.2 us                                                | 30.2 us: 1.11x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.88 sec: 1.13x slower                                                 |
| pidigits                   | 186 ms                                                 | 212 ms: 1.14x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 12.3 ms: 1.21x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.2 ms: 1.30x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 79.5 ms: 3.32x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (6): k_core, xml_etree_iterparse, sqlglot_parse, asyncio_websockets, shortest_path, fannkuch
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.068x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x