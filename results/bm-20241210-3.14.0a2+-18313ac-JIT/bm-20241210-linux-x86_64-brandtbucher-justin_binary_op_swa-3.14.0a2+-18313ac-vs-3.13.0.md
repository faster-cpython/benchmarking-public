# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_binary_op_swa
- machine: linux-x86_64
- commit hash: 18313ac
- commit date: 2024-12-10
- overall geometric mean: 1.031x faster
- HPT reliability: 98.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.03x faster                                                         |
| docutils       | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                       |
| html5lib       | 63.4 ms                                                | 64.5 ms: 1.02x slower                                                        |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.48x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 618 ms: 1.36x faster                                                         |
| async_tree_none            | 350 ms                                                 | 268 ms: 1.31x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 337 ms: 1.30x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                                         |
| async_generators           | 433 ms                                                 | 446 ms: 1.03x slower                                                         |
| coroutines                 | 22.2 ms                                                | 22.9 ms: 1.03x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 76.7 ms: 1.03x faster                                                        |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                         |
| nbody          | 87.7 ms                                                | 93.2 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.25 ms: 1.16x faster                                                        |
| regex_v8       | 26.9 ms                                                | 25.0 ms: 1.08x faster                                                        |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                         |
| unpickle_pure_python | 213 us                                                 | 194 us: 1.10x faster                                                         |
| xml_etree_process    | 60.5 ms                                                | 55.0 ms: 1.10x faster                                                        |
| tomli_loads          | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                       |
| xml_etree_generate   | 86.8 ms                                                | 81.1 ms: 1.07x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 95.8 ms: 1.06x faster                                                        |
| json_loads           | 27.2 us                                                | 26.1 us: 1.04x faster                                                        |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                         |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                        |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                        |
| django_template | 31.7 ms                                                | 33.3 ms: 1.05x slower                                                        |
| genshi_text     | 22.6 ms                                                | 24.1 ms: 1.06x slower                                                        |
| genshi_xml      | 50.5 ms                                                | 58.6 ms: 1.16x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.48x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 617 ms: 1.39x faster                                                         |
| async_tree_io              | 838 ms                                                 | 618 ms: 1.36x faster                                                         |
| deepcopy                   | 354 us                                                 | 270 us: 1.31x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.31x faster                                                        |
| async_tree_none            | 350 ms                                                 | 268 ms: 1.31x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 337 ms: 1.30x faster                                                         |
| richards                   | 47.5 ms                                                | 36.9 ms: 1.29x faster                                                        |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                         |
| richards_super             | 53.7 ms                                                | 43.6 ms: 1.23x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.74 us: 1.18x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.16x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.25 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                         |
| json                       | 5.32 ms                                                | 4.79 ms: 1.11x faster                                                        |
| telco                      | 8.40 ms                                                | 7.59 ms: 1.11x faster                                                        |
| unpickle_pure_python       | 213 us                                                 | 194 us: 1.10x faster                                                         |
| xml_etree_process          | 60.5 ms                                                | 55.0 ms: 1.10x faster                                                        |
| scimark_fft                | 367 ms                                                 | 336 ms: 1.09x faster                                                         |
| tomli_loads                | 2.12 sec                                               | 1.94 sec: 1.09x faster                                                       |
| crypto_pyaes               | 74.7 ms                                                | 69.3 ms: 1.08x faster                                                        |
| pathlib                    | 17.4 ms                                                | 16.1 ms: 1.08x faster                                                        |
| regex_v8                   | 26.9 ms                                                | 25.0 ms: 1.08x faster                                                        |
| pylint                     | 312 ms                                                 | 290 ms: 1.08x faster                                                         |
| xml_etree_generate         | 86.8 ms                                                | 81.1 ms: 1.07x faster                                                        |
| gc_traversal               | 4.90 ms                                                | 4.60 ms: 1.06x faster                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.41 sec: 1.06x faster                                                       |
| xml_etree_iterparse        | 101 ms                                                 | 95.8 ms: 1.06x faster                                                        |
| mako                       | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                        |
| go                         | 141 ms                                                 | 135 ms: 1.04x faster                                                         |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                                        |
| json_loads                 | 27.2 us                                                | 26.1 us: 1.04x faster                                                        |
| 2to3                       | 266 ms                                                 | 257 ms: 1.03x faster                                                         |
| thrift                     | 800 us                                                 | 775 us: 1.03x faster                                                         |
| pyflate                    | 470 ms                                                 | 455 ms: 1.03x faster                                                         |
| connected_components       | 447 ms                                                 | 434 ms: 1.03x faster                                                         |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                         |
| float                      | 78.7 ms                                                | 76.7 ms: 1.03x faster                                                        |
| pprint_safe_repr           | 727 ms                                                 | 709 ms: 1.02x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.02x faster                                                       |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                                       |
| logging_silent             | 101 ns                                                 | 99.1 ns: 1.02x faster                                                        |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                         |
| shortest_path              | 487 ms                                                 | 478 ms: 1.02x faster                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 65.8 ms: 1.01x faster                                                        |
| fannkuch                   | 394 ms                                                 | 388 ms: 1.01x faster                                                         |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.01x faster                                                         |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.01x faster                                                         |
| deltablue                  | 3.19 ms                                                | 3.16 ms: 1.01x faster                                                        |
| create_gc_cycles           | 2.45 ms                                                | 2.44 ms: 1.00x faster                                                        |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                         |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.09 ms: 1.01x slower                                                        |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                        |
| mdp                        | 2.54 sec                                               | 2.58 sec: 1.02x slower                                                       |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                       |
| html5lib                   | 63.4 ms                                                | 64.5 ms: 1.02x slower                                                        |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                                         |
| sympy_str                  | 273 ms                                                 | 281 ms: 1.03x slower                                                         |
| async_generators           | 433 ms                                                 | 446 ms: 1.03x slower                                                         |
| coroutines                 | 22.2 ms                                                | 22.9 ms: 1.03x slower                                                        |
| coverage                   | 82.8 ms                                                | 85.7 ms: 1.04x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.63 ms: 1.04x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                                         |
| sqlglot_parse              | 1.26 ms                                                | 1.31 ms: 1.04x slower                                                        |
| sqlglot_optimize           | 53.4 ms                                                | 55.4 ms: 1.04x slower                                                        |
| dulwich_log                | 64.6 ms                                                | 67.1 ms: 1.04x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.69 sec: 1.04x slower                                                       |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                         |
| spectral_norm              | 113 ms                                                 | 118 ms: 1.04x slower                                                         |
| sympy_expand               | 456 ms                                                 | 476 ms: 1.04x slower                                                         |
| sympy_integrate            | 19.8 ms                                                | 20.7 ms: 1.04x slower                                                        |
| comprehensions             | 16.5 us                                                | 17.3 us: 1.05x slower                                                        |
| django_template            | 31.7 ms                                                | 33.3 ms: 1.05x slower                                                        |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                         |
| nbody                      | 87.7 ms                                                | 93.2 ms: 1.06x slower                                                        |
| genshi_text                | 22.6 ms                                                | 24.1 ms: 1.06x slower                                                        |
| bench_thread_pool          | 818 us                                                 | 873 us: 1.07x slower                                                         |
| chaos                      | 58.0 ms                                                | 62.3 ms: 1.07x slower                                                        |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.11x slower                                                        |
| raytrace                   | 262 ms                                                 | 294 ms: 1.12x slower                                                         |
| nqueens                    | 80.9 ms                                                | 91.1 ms: 1.13x slower                                                        |
| many_optionals             | 857 us                                                 | 978 us: 1.14x slower                                                         |
| hexiom                     | 6.08 ms                                                | 7.00 ms: 1.15x slower                                                        |
| genshi_xml                 | 50.5 ms                                                | 58.6 ms: 1.16x slower                                                        |
| generators                 | 28.8 ms                                                | 36.2 ms: 1.26x slower                                                        |
| subparsers                 | 15.5 ms                                                | 21.1 ms: 1.36x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (6): djangocms, pycparser, logging_format, logging_simple, asyncio_websockets, meteor_contest
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241210-3.14.0a2+-18313ac-JIT/bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac.json: mypy2

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 98.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x