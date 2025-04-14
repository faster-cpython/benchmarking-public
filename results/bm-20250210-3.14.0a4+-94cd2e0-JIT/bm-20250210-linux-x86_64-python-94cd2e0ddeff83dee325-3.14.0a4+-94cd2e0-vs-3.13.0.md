# Results vs. 3.13.0

- fork: python
- ref: 94cd2e0ddeff83dee325
- machine: linux-x86_64
- commit hash: 94cd2e0
- commit date: 2025-02-10
- overall geometric mean: 1.040x faster
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                   |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                 |
| html5lib       | 63.4 ms                                                | 62.2 ms: 1.02x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                   |
| async_tree_io              | 838 ms                                                 | 627 ms: 1.34x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                                   |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 260 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                   |
| async_generators           | 433 ms                                                 | 411 ms: 1.05x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.9 ms: 1.12x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| nbody          | 87.7 ms                                                | 96.6 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.09 ms: 1.22x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.1 ms: 1.11x faster                                                  |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                                   |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.85 sec: 1.14x faster                                                 |
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.13x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 79.1 ms: 1.10x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 56.1 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 95.0 ms: 1.07x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 201 us: 1.06x faster                                                   |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                   |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 9.83 ms: 1.09x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                  |
| genshi_text     | 22.6 ms                                                | 22.3 ms: 1.02x faster                                                  |
| django_template | 31.7 ms                                                | 32.1 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                   |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                                   |
| async_tree_io              | 838 ms                                                 | 627 ms: 1.34x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 328 ms: 1.33x faster                                                   |
| async_tree_none            | 350 ms                                                 | 269 ms: 1.30x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 30.7 us: 1.25x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 260 ms: 1.23x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.09 ms: 1.22x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.68 us: 1.21x faster                                                  |
| scimark_fft                | 367 ms                                                 | 315 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                   |
| spectral_norm              | 113 ms                                                 | 98.5 ms: 1.15x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.14x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.13x faster                                                   |
| float                      | 78.7 ms                                                | 69.9 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                   |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 24.1 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.57 ms: 1.10x faster                                                  |
| telco                      | 8.40 ms                                                | 7.63 ms: 1.10x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 79.1 ms: 1.10x faster                                                  |
| mako                       | 10.7 ms                                                | 9.83 ms: 1.09x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 56.1 ms: 1.08x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.36 sec: 1.07x faster                                                 |
| crypto_pyaes               | 74.7 ms                                                | 69.6 ms: 1.07x faster                                                  |
| go                         | 141 ms                                                 | 131 ms: 1.07x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 95.0 ms: 1.07x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                                  |
| unpickle_pure_python       | 213 us                                                 | 201 us: 1.06x faster                                                   |
| pyflate                    | 470 ms                                                 | 444 ms: 1.06x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.63 ms: 1.06x faster                                                  |
| async_generators           | 433 ms                                                 | 411 ms: 1.05x faster                                                   |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                                   |
| richards                   | 47.5 ms                                                | 45.5 ms: 1.05x faster                                                  |
| richards_super             | 53.7 ms                                                | 51.6 ms: 1.04x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                 |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                   |
| thrift                     | 800 us                                                 | 772 us: 1.04x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                 |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                   |
| json                       | 5.32 ms                                                | 5.18 ms: 1.03x faster                                                  |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                   |
| html5lib                   | 63.4 ms                                                | 62.2 ms: 1.02x faster                                                  |
| generators                 | 28.8 ms                                                | 28.3 ms: 1.02x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                   |
| genshi_text                | 22.6 ms                                                | 22.3 ms: 1.02x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                 |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 66.4 ms: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 53.7 ms: 1.01x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 115 ms: 1.01x slower                                                   |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                  |
| sympy_str                  | 273 ms                                                 | 276 ms: 1.01x slower                                                   |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                  |
| chaos                      | 58.0 ms                                                | 58.8 ms: 1.01x slower                                                  |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                                   |
| sympy_integrate            | 19.8 ms                                                | 20.3 ms: 1.02x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 66.2 ms: 1.03x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 748 ms: 1.03x slower                                                   |
| sympy_expand               | 456 ms                                                 | 472 ms: 1.03x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.04x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.54 sec: 1.04x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                 |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.05x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                   |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                                  |
| raytrace                   | 262 ms                                                 | 281 ms: 1.07x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.44 ms: 1.08x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 888 us: 1.09x slower                                                   |
| coverage                   | 82.8 ms                                                | 90.2 ms: 1.09x slower                                                  |
| logging_silent             | 101 ns                                                 | 110 ns: 1.09x slower                                                   |
| nbody                      | 87.7 ms                                                | 96.6 ms: 1.10x slower                                                  |
| nqueens                    | 80.9 ms                                                | 89.4 ms: 1.10x slower                                                  |
| many_optionals             | 857 us                                                 | 960 us: 1.12x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.95 ms: 1.14x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.39x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (12): connected_components, logging_simple, shortest_path, create_gc_cycles, asyncio_websockets, logging_format, sqlalchemy_imperative, meteor_contest, sympy_sum, mdp, sqlglot_parse, fannkuch
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x