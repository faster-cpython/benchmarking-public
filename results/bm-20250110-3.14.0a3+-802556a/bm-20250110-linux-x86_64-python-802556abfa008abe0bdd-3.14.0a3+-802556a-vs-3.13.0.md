# Results vs. 3.13.0

- fork: python
- ref: 802556abfa008abe0bdd
- machine: linux-x86_64
- commit hash: 802556a
- commit date: 2025-01-10
- overall geometric mean: 1.040x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 254 ms: 1.05x faster                                                   |
| docutils       | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                 |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 307 ms: 1.51x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 588 ms: 1.46x faster                                                   |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 485 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 461 ms: 1.18x faster                                                   |
| async_generators           | 433 ms                                                 | 418 ms: 1.04x faster                                                   |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.10x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.7 ms: 1.08x faster                                                  |
| pidigits       | 186 ms                                                 | 190 ms: 1.02x slower                                                   |
| nbody          | 87.7 ms                                                | 93.8 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.43 ms: 1.10x faster                                                  |
| regex_v8       | 26.9 ms                                                | 25.8 ms: 1.04x faster                                                  |
| regex_dna      | 220 ms                                                 | 213 ms: 1.03x faster                                                   |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 2.01 sec: 1.05x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 96.9 ms: 1.05x faster                                                  |
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 86.0 ms: 1.01x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 324 us: 1.07x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.04 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 50.5 ms                                                | 49.4 ms: 1.02x faster                                                  |
| genshi_text    | 22.6 ms                                                | 22.2 ms: 1.02x faster                                                  |
| mako           | 10.7 ms                                                | 11.5 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 307 ms: 1.51x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 588 ms: 1.46x faster                                                   |
| async_tree_io              | 838 ms                                                 | 602 ms: 1.39x faster                                                   |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 248 ms: 1.28x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 31.0 us: 1.24x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.65 us: 1.22x faster                                                  |
| go                         | 141 ms                                                 | 118 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 485 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 461 ms: 1.18x faster                                                   |
| pylint                     | 312 ms                                                 | 277 ms: 1.12x faster                                                   |
| pathlib                    | 17.4 ms                                                | 15.6 ms: 1.11x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.43 ms: 1.10x faster                                                  |
| telco                      | 8.40 ms                                                | 7.74 ms: 1.08x faster                                                  |
| float                      | 78.7 ms                                                | 72.7 ms: 1.08x faster                                                  |
| json                       | 5.32 ms                                                | 4.93 ms: 1.08x faster                                                  |
| spectral_norm              | 113 ms                                                 | 107 ms: 1.06x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.24 sec: 1.06x faster                                                 |
| richards                   | 47.5 ms                                                | 45.2 ms: 1.05x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 2.01 sec: 1.05x faster                                                 |
| richards_super             | 53.7 ms                                                | 51.2 ms: 1.05x faster                                                  |
| scimark_fft                | 367 ms                                                 | 349 ms: 1.05x faster                                                   |
| generators                 | 28.8 ms                                                | 27.4 ms: 1.05x faster                                                  |
| thrift                     | 800 us                                                 | 763 us: 1.05x faster                                                   |
| 2to3                       | 266 ms                                                 | 254 ms: 1.05x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 96.9 ms: 1.05x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 25.8 ms: 1.04x faster                                                  |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                  |
| async_generators           | 433 ms                                                 | 418 ms: 1.04x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 72.1 ms: 1.04x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.87 ms: 1.03x faster                                                  |
| regex_dna                  | 220 ms                                                 | 213 ms: 1.03x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.55 sec: 1.03x faster                                                 |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                   |
| connected_components       | 447 ms                                                 | 435 ms: 1.03x faster                                                   |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                  |
| shortest_path              | 487 ms                                                 | 475 ms: 1.02x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 49.4 ms: 1.02x faster                                                  |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                  |
| genshi_text                | 22.6 ms                                                | 22.2 ms: 1.02x faster                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 52.5 ms: 1.02x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                 |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                                  |
| nqueens                    | 80.9 ms                                                | 79.7 ms: 1.01x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.01x faster                                                   |
| logging_format             | 6.23 us                                                | 6.15 us: 1.01x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.59 us: 1.01x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 63.9 ms: 1.01x faster                                                  |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 86.0 ms: 1.01x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.01x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.04 ms: 1.01x slower                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.01x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 732 ms: 1.01x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.49 sec: 1.01x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.61 sec: 1.01x slower                                                 |
| coverage                   | 82.8 ms                                                | 83.6 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 67.5 ms: 1.01x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 4.95 ms: 1.01x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                                   |
| pidigits                   | 186 ms                                                 | 190 ms: 1.02x slower                                                   |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                  |
| scimark_sor                | 122 ms                                                 | 125 ms: 1.02x slower                                                   |
| pyflate                    | 470 ms                                                 | 480 ms: 1.02x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.27 ms: 1.02x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.61 sec: 1.03x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                   |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.35 ms: 1.05x slower                                                  |
| logging_silent             | 101 ns                                                 | 106 ns: 1.05x slower                                                   |
| fannkuch                   | 394 ms                                                 | 412 ms: 1.05x slower                                                   |
| chaos                      | 58.0 ms                                                | 61.1 ms: 1.05x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 863 us: 1.06x slower                                                   |
| nbody                      | 87.7 ms                                                | 93.8 ms: 1.07x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 324 us: 1.07x slower                                                   |
| mako                       | 10.7 ms                                                | 11.5 ms: 1.07x slower                                                  |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.10x slower                                                  |
| many_optionals             | 857 us                                                 | 944 us: 1.10x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.34x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.5 ms: 3.40x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (5): xml_etree_process, sympy_expand, asyncio_websockets, django_template, scimark_lu
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x