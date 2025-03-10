# Results vs. 3.13.0

- fork: brandtbucher
- ref: chain_depth_5
- machine: linux-x86_64
- commit hash: dc27e14
- commit date: 2024-12-12
- overall geometric mean: 1.032x faster
- HPT reliability: 99.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 258 ms: 1.03x faster                                                  |
| docutils       | 2.58 sec                                               | 2.71 sec: 1.05x slower                                                |
| html5lib       | 63.4 ms                                                | 65.2 ms: 1.03x slower                                                 |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 602 ms: 1.43x faster                                                  |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                  |
| async_tree_none            | 350 ms                                                 | 271 ms: 1.29x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 340 ms: 1.28x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.14x faster                                                  |
| coroutines                 | 22.2 ms                                                | 22.7 ms: 1.02x slower                                                 |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 87.7 ms                                                | 80.5 ms: 1.09x faster                                                 |
| float          | 78.7 ms                                                | 76.0 ms: 1.04x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.39 ms: 1.11x faster                                                 |
| regex_v8       | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                 |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                  |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 78.0 ms: 1.11x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 195 us: 1.09x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 55.4 ms: 1.09x faster                                                 |
| tomli_loads          | 2.12 sec                                               | 1.95 sec: 1.08x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 95.2 ms: 1.06x faster                                                 |
| json_loads           | 27.2 us                                                | 26.1 us: 1.04x faster                                                 |
| pickle_pure_python   | 302 us                                                 | 315 us: 1.04x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.2 ms: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.03 ms: 1.00x slower                                                 |
| python_startup         | 12.7 ms                                                | 12.7 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.3 ms: 1.04x faster                                                 |
| django_template | 31.7 ms                                                | 33.9 ms: 1.07x slower                                                 |
| genshi_text     | 22.6 ms                                                | 24.7 ms: 1.09x slower                                                 |
| genshi_xml      | 50.5 ms                                                | 57.7 ms: 1.14x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 602 ms: 1.43x faster                                                  |
| async_tree_io              | 838 ms                                                 | 617 ms: 1.36x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.1 us: 1.32x faster                                                 |
| deepcopy                   | 354 us                                                 | 272 us: 1.30x faster                                                  |
| async_tree_none            | 350 ms                                                 | 271 ms: 1.29x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 340 ms: 1.28x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                  |
| richards                   | 47.5 ms                                                | 37.6 ms: 1.27x faster                                                 |
| richards_super             | 53.7 ms                                                | 43.1 ms: 1.25x faster                                                 |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.14x faster                                                  |
| scimark_fft                | 367 ms                                                 | 325 ms: 1.13x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 78.0 ms: 1.11x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.39 ms: 1.11x faster                                                 |
| json                       | 5.32 ms                                                | 4.80 ms: 1.11x faster                                                 |
| telco                      | 8.40 ms                                                | 7.64 ms: 1.10x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 195 us: 1.09x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 55.4 ms: 1.09x faster                                                 |
| crypto_pyaes               | 74.7 ms                                                | 68.5 ms: 1.09x faster                                                 |
| nbody                      | 87.7 ms                                                | 80.5 ms: 1.09x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 1.95 sec: 1.08x faster                                                |
| regex_v8                   | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                 |
| pylint                     | 312 ms                                                 | 290 ms: 1.07x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.07x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.41 sec: 1.06x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 95.2 ms: 1.06x faster                                                 |
| go                         | 141 ms                                                 | 133 ms: 1.05x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                |
| json_loads                 | 27.2 us                                                | 26.1 us: 1.04x faster                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 64.3 ms: 1.04x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.85 ms: 1.04x faster                                                 |
| mako                       | 10.7 ms                                                | 10.3 ms: 1.04x faster                                                 |
| float                      | 78.7 ms                                                | 76.0 ms: 1.04x faster                                                 |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.03x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                 |
| 2to3                       | 266 ms                                                 | 258 ms: 1.03x faster                                                  |
| connected_components       | 447 ms                                                 | 435 ms: 1.03x faster                                                  |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                  |
| scimark_lu                 | 114 ms                                                 | 112 ms: 1.02x faster                                                  |
| thrift                     | 800 us                                                 | 783 us: 1.02x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.80 ms: 1.02x faster                                                 |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                  |
| pyflate                    | 470 ms                                                 | 460 ms: 1.02x faster                                                  |
| fannkuch                   | 394 ms                                                 | 388 ms: 1.02x faster                                                  |
| shortest_path              | 487 ms                                                 | 479 ms: 1.02x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                 |
| spectral_norm              | 113 ms                                                 | 112 ms: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 7.03 ms: 1.00x slower                                                 |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.7 ms: 1.01x slower                                                 |
| logging_simple             | 5.65 us                                                | 5.74 us: 1.01x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.02x slower                                                |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.02x slower                                                |
| coroutines                 | 22.2 ms                                                | 22.7 ms: 1.02x slower                                                 |
| sqlglot_normalize          | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| html5lib                   | 63.4 ms                                                | 65.2 ms: 1.03x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                  |
| sympy_str                  | 273 ms                                                 | 283 ms: 1.04x slower                                                  |
| chaos                      | 58.0 ms                                                | 60.2 ms: 1.04x slower                                                 |
| sqlglot_optimize           | 53.4 ms                                                | 55.5 ms: 1.04x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 315 us: 1.04x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.64 ms: 1.04x slower                                                 |
| coverage                   | 82.8 ms                                                | 86.5 ms: 1.04x slower                                                 |
| sympy_expand               | 456 ms                                                 | 478 ms: 1.05x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 20.8 ms: 1.05x slower                                                 |
| dulwich_log                | 64.6 ms                                                | 67.7 ms: 1.05x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.71 sec: 1.05x slower                                                |
| sqlglot_parse              | 1.26 ms                                                | 1.33 ms: 1.05x slower                                                 |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                  |
| comprehensions             | 16.5 us                                                | 17.4 us: 1.06x slower                                                 |
| django_template            | 31.7 ms                                                | 33.9 ms: 1.07x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 878 us: 1.07x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.76 sec: 1.08x slower                                                |
| raytrace                   | 262 ms                                                 | 284 ms: 1.09x slower                                                  |
| genshi_text                | 22.6 ms                                                | 24.7 ms: 1.09x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.2 ms: 1.10x slower                                                 |
| nqueens                    | 80.9 ms                                                | 90.3 ms: 1.12x slower                                                 |
| genshi_xml                 | 50.5 ms                                                | 57.7 ms: 1.14x slower                                                 |
| many_optionals             | 857 us                                                 | 984 us: 1.15x slower                                                  |
| hexiom                     | 6.08 ms                                                | 7.10 ms: 1.17x slower                                                 |
| generators                 | 28.8 ms                                                | 36.3 ms: 1.26x slower                                                 |
| subparsers                 | 15.5 ms                                                | 20.8 ms: 1.35x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 80.8 ms: 3.37x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (6): pprint_safe_repr, deltablue, djangocms, logging_format, asyncio_websockets, logging_silent
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241212-3.14.0a2+-dc27e14-JIT/bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14.json: mypy2

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 99.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x