# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: 7773cea
- commit date: 2025-02-13
- overall geometric mean: 1.044x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-7773cea |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                         |
| docutils       | 2.58 sec                                               | 2.63 sec: 1.02x slower                                                       |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                        |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-7773cea |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 323 ms: 1.35x faster                                                         |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                         |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                         |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                         |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-7773cea |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.3 ms: 1.10x faster                                                        |
| nbody          | 87.7 ms                                                | 85.8 ms: 1.02x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-7773cea |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.26 ms: 1.16x faster                                                        |
| regex_v8       | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                        |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                                         |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-7773cea |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 137 ms: 1.13x faster                                                         |
| tomli_loads          | 2.12 sec                                               | 1.89 sec: 1.12x faster                                                       |
| xml_etree_generate   | 86.8 ms                                                | 78.0 ms: 1.11x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 55.5 ms: 1.09x faster                                                        |
| unpickle_pure_python | 213 us                                                 | 204 us: 1.04x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 97.0 ms: 1.04x faster                                                        |
| json_loads           | 27.2 us                                                | 28.5 us: 1.05x slower                                                        |
| pickle_pure_python   | 302 us                                                 | 326 us: 1.08x slower                                                         |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-7773cea |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                        |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-7773cea |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 9.99 ms: 1.07x faster                                                        |
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                        |
| genshi_xml      | 50.5 ms                                                | 48.8 ms: 1.03x faster                                                        |
| django_template | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250213-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a5+-7773cea |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 323 ms: 1.35x faster                                                         |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                         |
| deepcopy                   | 354 us                                                 | 263 us: 1.35x faster                                                         |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 30.9 us: 1.24x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                        |
| scimark_fft                | 367 ms                                                 | 310 ms: 1.18x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.26 ms: 1.16x faster                                                        |
| regex_v8                   | 26.9 ms                                                | 23.5 ms: 1.14x faster                                                        |
| spectral_norm              | 113 ms                                                 | 100 ms: 1.13x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 137 ms: 1.13x faster                                                         |
| go                         | 141 ms                                                 | 125 ms: 1.13x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 1.89 sec: 1.12x faster                                                       |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 487 ms: 1.12x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 78.0 ms: 1.11x faster                                                        |
| telco                      | 8.40 ms                                                | 7.57 ms: 1.11x faster                                                        |
| float                      | 78.7 ms                                                | 71.3 ms: 1.10x faster                                                        |
| xml_etree_process          | 60.5 ms                                                | 55.5 ms: 1.09x faster                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.68 ms: 1.08x faster                                                        |
| sqlite_synth               | 2.90 us                                                | 2.71 us: 1.07x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                       |
| mako                       | 10.7 ms                                                | 9.99 ms: 1.07x faster                                                        |
| pathlib                    | 17.4 ms                                                | 16.3 ms: 1.07x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                                       |
| richards                   | 47.5 ms                                                | 44.9 ms: 1.06x faster                                                        |
| richards_super             | 53.7 ms                                                | 50.9 ms: 1.06x faster                                                        |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                                         |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                        |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                         |
| unpickle_pure_python       | 213 us                                                 | 204 us: 1.04x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 97.0 ms: 1.04x faster                                                        |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                         |
| thrift                     | 800 us                                                 | 770 us: 1.04x faster                                                         |
| genshi_xml                 | 50.5 ms                                                | 48.8 ms: 1.03x faster                                                        |
| json                       | 5.32 ms                                                | 5.15 ms: 1.03x faster                                                        |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                       |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                         |
| crypto_pyaes               | 74.7 ms                                                | 72.6 ms: 1.03x faster                                                        |
| logging_simple             | 5.65 us                                                | 5.51 us: 1.03x faster                                                        |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                       |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                        |
| nbody                      | 87.7 ms                                                | 85.8 ms: 1.02x faster                                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                         |
| shortest_path              | 487 ms                                                 | 477 ms: 1.02x faster                                                         |
| connected_components       | 447 ms                                                 | 438 ms: 1.02x faster                                                         |
| gc_traversal               | 4.90 ms                                                | 4.80 ms: 1.02x faster                                                        |
| logging_format             | 6.23 us                                                | 6.12 us: 1.02x faster                                                        |
| generators                 | 28.8 ms                                                | 28.3 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 727 ms                                                 | 715 ms: 1.02x faster                                                         |
| mdp                        | 2.54 sec                                               | 2.51 sec: 1.01x faster                                                       |
| pyflate                    | 470 ms                                                 | 465 ms: 1.01x faster                                                         |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                         |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.00x faster                                                         |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| sqlglot_optimize           | 53.4 ms                                                | 53.7 ms: 1.01x slower                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                        |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                        |
| scimark_sor                | 122 ms                                                 | 123 ms: 1.01x slower                                                         |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| nqueens                    | 80.9 ms                                                | 82.0 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.26 ms                                                | 1.29 ms: 1.02x slower                                                        |
| sympy_integrate            | 19.8 ms                                                | 20.2 ms: 1.02x slower                                                        |
| fannkuch                   | 394 ms                                                 | 401 ms: 1.02x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.63 sec: 1.02x slower                                                       |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                         |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.02x slower                                                         |
| sympy_expand               | 456 ms                                                 | 466 ms: 1.02x slower                                                         |
| dulwich_log                | 64.6 ms                                                | 66.3 ms: 1.03x slower                                                        |
| django_template            | 31.7 ms                                                | 32.5 ms: 1.03x slower                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 68.8 ms: 1.03x slower                                                        |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                        |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                        |
| chaos                      | 58.0 ms                                                | 60.4 ms: 1.04x slower                                                        |
| json_loads                 | 27.2 us                                                | 28.5 us: 1.05x slower                                                        |
| raytrace                   | 262 ms                                                 | 277 ms: 1.06x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 872 us: 1.07x slower                                                         |
| pickle_pure_python         | 302 us                                                 | 326 us: 1.08x slower                                                         |
| deltablue                  | 3.19 ms                                                | 3.44 ms: 1.08x slower                                                        |
| hexiom                     | 6.08 ms                                                | 6.59 ms: 1.08x slower                                                        |
| coverage                   | 82.8 ms                                                | 90.1 ms: 1.09x slower                                                        |
| logging_silent             | 101 ns                                                 | 110 ns: 1.09x slower                                                         |
| many_optionals             | 857 us                                                 | 954 us: 1.11x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (5): sqlalchemy_imperative, sympy_sum, asyncio_websockets, sympy_str, pprint_pformat
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x