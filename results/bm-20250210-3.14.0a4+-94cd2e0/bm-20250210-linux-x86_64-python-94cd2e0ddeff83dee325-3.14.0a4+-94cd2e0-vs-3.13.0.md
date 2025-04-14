# Results vs. 3.13.0

- fork: python
- ref: 94cd2e0ddeff83dee325
- machine: linux-x86_64
- commit hash: 94cd2e0
- commit date: 2025-02-10
- overall geometric mean: 1.050x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 251 ms: 1.06x faster                                                   |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.00x slower                                                 |
| html5lib       | 63.4 ms                                                | 61.6 ms: 1.03x faster                                                  |
| sphinx         | 1.03 sec                                               | 999 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 323 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 257 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.17x faster                                                   |
| async_generators           | 433 ms                                                 | 376 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.4 ms: 1.13x faster                                                  |
| nbody          | 87.7 ms                                                | 92.6 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.40 ms: 1.11x faster                                                  |
| regex_v8       | 26.9 ms                                                | 25.1 ms: 1.07x faster                                                  |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                   |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 96.6 ms: 1.05x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 83.1 ms: 1.04x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 58.0 ms: 1.04x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                   |
| json_loads           | 27.2 us                                                | 28.6 us: 1.05x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.05 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 47.9 ms: 1.05x faster                                                  |
| django_template | 31.7 ms                                                | 32.1 ms: 1.01x slower                                                  |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-linux-x86_64-python-94cd2e0ddeff83dee325-3.14.0a4+-94cd2e0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.40x faster                                                   |
| deepcopy                   | 354 us                                                 | 258 us: 1.37x faster                                                   |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 323 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 30.6 us: 1.26x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 257 ms: 1.24x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.21x faster                                                  |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.17x faster                                                   |
| spectral_norm              | 113 ms                                                 | 97.8 ms: 1.16x faster                                                  |
| async_generators           | 433 ms                                                 | 376 ms: 1.15x faster                                                   |
| pylint                     | 312 ms                                                 | 272 ms: 1.14x faster                                                   |
| float                      | 78.7 ms                                                | 69.4 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 482 ms: 1.13x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.40 ms: 1.11x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                 |
| scimark_fft                | 367 ms                                                 | 340 ms: 1.08x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.35 sec: 1.08x faster                                                 |
| richards                   | 47.5 ms                                                | 44.1 ms: 1.08x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 25.1 ms: 1.07x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.3 ms: 1.07x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 70.0 ms: 1.07x faster                                                  |
| richards_super             | 53.7 ms                                                | 50.4 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.74 ms: 1.06x faster                                                  |
| 2to3                       | 266 ms                                                 | 251 ms: 1.06x faster                                                   |
| telco                      | 8.40 ms                                                | 7.94 ms: 1.06x faster                                                  |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 47.9 ms: 1.05x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.26 sec: 1.05x faster                                                 |
| sqlglot_normalize          | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 96.6 ms: 1.05x faster                                                  |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 83.1 ms: 1.04x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 58.0 ms: 1.04x faster                                                  |
| thrift                     | 800 us                                                 | 767 us: 1.04x faster                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.2 ms: 1.04x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 145 ms: 1.04x faster                                                   |
| sympy_str                  | 273 ms                                                 | 264 ms: 1.03x faster                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 51.7 ms: 1.03x faster                                                  |
| sphinx                     | 1.03 sec                                               | 999 ms: 1.03x faster                                                   |
| logging_simple             | 5.65 us                                                | 5.48 us: 1.03x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                 |
| html5lib                   | 63.4 ms                                                | 61.6 ms: 1.03x faster                                                  |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| json                       | 5.32 ms                                                | 5.17 ms: 1.03x faster                                                  |
| connected_components       | 447 ms                                                 | 435 ms: 1.03x faster                                                   |
| shortest_path              | 487 ms                                                 | 474 ms: 1.03x faster                                                   |
| typing_runtime_protocols   | 160 us                                                 | 156 us: 1.03x faster                                                   |
| generators                 | 28.8 ms                                                | 28.1 ms: 1.02x faster                                                  |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                                   |
| sqlglot_parse              | 1.26 ms                                                | 1.24 ms: 1.02x faster                                                  |
| logging_format             | 6.23 us                                                | 6.11 us: 1.02x faster                                                  |
| nqueens                    | 80.9 ms                                                | 79.3 ms: 1.02x faster                                                  |
| pyflate                    | 470 ms                                                 | 461 ms: 1.02x faster                                                   |
| sqlglot_transpile          | 1.57 ms                                                | 1.54 ms: 1.02x faster                                                  |
| mdp                        | 2.54 sec                                               | 2.50 sec: 1.02x faster                                                 |
| pprint_safe_repr           | 727 ms                                                 | 716 ms: 1.01x faster                                                   |
| sympy_expand               | 456 ms                                                 | 450 ms: 1.01x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                                 |
| dulwich_log                | 64.6 ms                                                | 64.0 ms: 1.01x faster                                                  |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                                  |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                   |
| chaos                      | 58.0 ms                                                | 57.7 ms: 1.01x faster                                                  |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.00x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.11 ms: 1.01x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 67.2 ms: 1.01x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.05 ms: 1.01x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 4.95 ms: 1.01x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| django_template            | 31.7 ms                                                | 32.1 ms: 1.01x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                   |
| fannkuch                   | 394 ms                                                 | 403 ms: 1.02x slower                                                   |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                  |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.3 ms: 1.05x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 860 us: 1.05x slower                                                   |
| json_loads                 | 27.2 us                                                | 28.6 us: 1.05x slower                                                  |
| logging_silent             | 101 ns                                                 | 107 ns: 1.06x slower                                                   |
| nbody                      | 87.7 ms                                                | 92.6 ms: 1.06x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                                   |
| many_optionals             | 857 us                                                 | 927 us: 1.08x slower                                                   |
| coverage                   | 82.8 ms                                                | 90.9 ms: 1.10x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.15x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.5 ms: 1.33x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 80.7 ms: 3.37x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (4): deltablue, pidigits, asyncio_websockets, scimark_lu
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.03x