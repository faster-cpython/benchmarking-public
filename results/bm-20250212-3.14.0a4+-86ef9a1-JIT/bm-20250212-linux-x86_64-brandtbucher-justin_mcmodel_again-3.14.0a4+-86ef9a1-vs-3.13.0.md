# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.053x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                                         |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.03x slower                                                       |
| html5lib       | 63.4 ms                                                | 61.5 ms: 1.03x faster                                                        |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 325 ms: 1.34x faster                                                         |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                                         |
| async_generators           | 433 ms                                                 | 406 ms: 1.07x faster                                                         |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.03x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.1 ms: 1.14x faster                                                        |
| nbody          | 87.7 ms                                                | 84.5 ms: 1.04x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.00 ms: 1.25x faster                                                        |
| regex_v8       | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                        |
| regex_dna      | 220 ms                                                 | 201 ms: 1.10x faster                                                         |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.82 sec: 1.16x faster                                                       |
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                         |
| xml_etree_generate   | 86.8 ms                                                | 78.1 ms: 1.11x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 55.0 ms: 1.10x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 199 us: 1.07x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 95.7 ms: 1.06x faster                                                        |
| pickle_pure_python   | 302 us                                                 | 317 us: 1.05x slower                                                         |
| json_loads           | 27.2 us                                                | 28.9 us: 1.07x slower                                                        |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.05 ms: 1.01x slower                                                        |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 10.7 ms                                                | 9.82 ms: 1.09x faster                                                        |
| genshi_text    | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                        |
| genshi_xml     | 50.5 ms                                                | 48.9 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.45x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                         |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                         |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 325 ms: 1.34x faster                                                         |
| async_tree_none            | 350 ms                                                 | 266 ms: 1.32x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 30.5 us: 1.26x faster                                                        |
| regex_effbot               | 3.77 ms                                                | 3.00 ms: 1.25x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                         |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                        |
| scimark_fft                | 367 ms                                                 | 308 ms: 1.19x faster                                                         |
| spectral_norm              | 113 ms                                                 | 95.3 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 1.82 sec: 1.16x faster                                                       |
| float                      | 78.7 ms                                                | 69.1 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 480 ms: 1.13x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 23.8 ms: 1.13x faster                                                        |
| pylint                     | 312 ms                                                 | 277 ms: 1.13x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 78.1 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.56 ms: 1.10x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 55.0 ms: 1.10x faster                                                        |
| go                         | 141 ms                                                 | 128 ms: 1.10x faster                                                         |
| regex_dna                  | 220 ms                                                 | 201 ms: 1.10x faster                                                         |
| telco                      | 8.40 ms                                                | 7.68 ms: 1.09x faster                                                        |
| mako                       | 10.7 ms                                                | 9.82 ms: 1.09x faster                                                        |
| pyflate                    | 470 ms                                                 | 435 ms: 1.08x faster                                                         |
| richards                   | 47.5 ms                                                | 44.3 ms: 1.07x faster                                                        |
| sqlite_synth               | 2.90 us                                                | 2.71 us: 1.07x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 199 us: 1.07x faster                                                         |
| crypto_pyaes               | 74.7 ms                                                | 69.8 ms: 1.07x faster                                                        |
| richards_super             | 53.7 ms                                                | 50.3 ms: 1.07x faster                                                        |
| async_generators           | 433 ms                                                 | 406 ms: 1.07x faster                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.40 sec: 1.07x faster                                                       |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 95.7 ms: 1.06x faster                                                        |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                         |
| thrift                     | 800 us                                                 | 758 us: 1.06x faster                                                         |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                       |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                                         |
| nbody                      | 87.7 ms                                                | 84.5 ms: 1.04x faster                                                        |
| json                       | 5.32 ms                                                | 5.14 ms: 1.04x faster                                                        |
| logging_format             | 6.23 us                                                | 6.01 us: 1.04x faster                                                        |
| generators                 | 28.8 ms                                                | 27.8 ms: 1.03x faster                                                        |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                       |
| genshi_xml                 | 50.5 ms                                                | 48.9 ms: 1.03x faster                                                        |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                                         |
| html5lib                   | 63.4 ms                                                | 61.5 ms: 1.03x faster                                                        |
| sqlglot_normalize          | 108 ms                                                 | 105 ms: 1.03x faster                                                         |
| logging_simple             | 5.65 us                                                | 5.49 us: 1.03x faster                                                        |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                       |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                         |
| scimark_monte_carlo        | 66.8 ms                                                | 65.5 ms: 1.02x faster                                                        |
| shortest_path              | 487 ms                                                 | 477 ms: 1.02x faster                                                         |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                                         |
| gc_traversal               | 4.90 ms                                                | 4.81 ms: 1.02x faster                                                        |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                                        |
| mdp                        | 2.54 sec                                               | 2.52 sec: 1.01x faster                                                       |
| chaos                      | 58.0 ms                                                | 57.5 ms: 1.01x faster                                                        |
| sqlglot_parse              | 1.26 ms                                                | 1.25 ms: 1.01x faster                                                        |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.00x faster                                                         |
| sqlglot_optimize           | 53.4 ms                                                | 53.2 ms: 1.00x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| python_startup_no_site     | 7.00 ms                                                | 7.05 ms: 1.01x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                                         |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                        |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.02x slower                                                        |
| sympy_expand               | 456 ms                                                 | 466 ms: 1.02x slower                                                         |
| pprint_pformat             | 1.48 sec                                               | 1.51 sec: 1.02x slower                                                       |
| dulwich_log                | 64.6 ms                                                | 66.1 ms: 1.02x slower                                                        |
| logging_silent             | 101 ns                                                 | 104 ns: 1.03x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.03x slower                                                       |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                        |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.03x slower                                                        |
| raytrace                   | 262 ms                                                 | 273 ms: 1.04x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 317 us: 1.05x slower                                                         |
| deltablue                  | 3.19 ms                                                | 3.35 ms: 1.05x slower                                                        |
| json_loads                 | 27.2 us                                                | 28.9 us: 1.07x slower                                                        |
| coverage                   | 82.8 ms                                                | 88.6 ms: 1.07x slower                                                        |
| bench_thread_pool          | 818 us                                                 | 881 us: 1.08x slower                                                         |
| nqueens                    | 80.9 ms                                                | 87.8 ms: 1.09x slower                                                        |
| many_optionals             | 857 us                                                 | 948 us: 1.11x slower                                                         |
| hexiom                     | 6.08 ms                                                | 6.83 ms: 1.12x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.33x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                 |

Benchmark hidden because not significant (8): scimark_lu, pprint_safe_repr, fannkuch, typing_runtime_protocols, sqlglot_transpile, sympy_str, asyncio_websockets, django_template
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x