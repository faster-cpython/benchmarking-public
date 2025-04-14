# Results vs. 3.13.0

- fork: brandtbucher
- ref: remove_optimizer_api
- machine: linux-x86_64
- commit hash: 085e172
- commit date: 2025-01-21
- overall geometric mean: 1.044x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                                         |
| html5lib       | 63.4 ms                                                | 60.8 ms: 1.04x faster                                                        |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 591 ms: 1.46x faster                                                         |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                                         |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                         |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                         |
| async_generators           | 433 ms                                                 | 388 ms: 1.12x faster                                                         |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.7 ms: 1.11x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| nbody          | 87.7 ms                                                | 92.9 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.15 ms: 1.20x faster                                                        |
| regex_v8       | 26.9 ms                                                | 25.0 ms: 1.08x faster                                                        |
| regex_dna      | 220 ms                                                 | 208 ms: 1.05x faster                                                         |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                         |
| tomli_loads          | 2.12 sec                                               | 1.99 sec: 1.06x faster                                                       |
| xml_etree_iterparse  | 101 ms                                                 | 97.2 ms: 1.04x faster                                                        |
| xml_etree_generate   | 86.8 ms                                                | 83.8 ms: 1.04x faster                                                        |
| xml_etree_process    | 60.5 ms                                                | 61.4 ms: 1.02x slower                                                        |
| unpickle_pure_python | 213 us                                                 | 226 us: 1.06x slower                                                         |
| json_loads           | 27.2 us                                                | 29.0 us: 1.07x slower                                                        |
| pickle_pure_python   | 302 us                                                 | 331 us: 1.09x slower                                                         |
| json_dumps           | 10.1 ms                                                | 11.9 ms: 1.18x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                        |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.2 ms: 1.02x faster                                                        |
| django_template | 31.7 ms                                                | 31.8 ms: 1.01x slower                                                        |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 310 ms: 1.49x faster                                                         |
| async_tree_io_tg           | 861 ms                                                 | 591 ms: 1.46x faster                                                         |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                                         |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                         |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                                         |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                                         |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                         |
| deepcopy_memo              | 38.4 us                                                | 31.2 us: 1.23x faster                                                        |
| deepcopy_reduce            | 3.24 us                                                | 2.65 us: 1.22x faster                                                        |
| go                         | 141 ms                                                 | 116 ms: 1.21x faster                                                         |
| regex_effbot               | 3.77 ms                                                | 3.15 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 491 ms: 1.17x faster                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 473 ms: 1.15x faster                                                         |
| pylint                     | 312 ms                                                 | 274 ms: 1.14x faster                                                         |
| async_generators           | 433 ms                                                 | 388 ms: 1.12x faster                                                         |
| float                      | 78.7 ms                                                | 70.7 ms: 1.11x faster                                                        |
| spectral_norm              | 113 ms                                                 | 102 ms: 1.11x faster                                                         |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.61 ms: 1.09x faster                                                        |
| richards                   | 47.5 ms                                                | 43.8 ms: 1.09x faster                                                        |
| scimark_fft                | 367 ms                                                 | 340 ms: 1.08x faster                                                         |
| regex_v8                   | 26.9 ms                                                | 25.0 ms: 1.08x faster                                                        |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.07x faster                                                        |
| richards_super             | 53.7 ms                                                | 50.2 ms: 1.07x faster                                                        |
| telco                      | 8.40 ms                                                | 7.86 ms: 1.07x faster                                                        |
| tomli_loads                | 2.12 sec                                               | 1.99 sec: 1.06x faster                                                       |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.05x faster                                                         |
| k_core                     | 2.37 sec                                               | 2.25 sec: 1.05x faster                                                       |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                       |
| html5lib                   | 63.4 ms                                                | 60.8 ms: 1.04x faster                                                        |
| xml_etree_iterparse        | 101 ms                                                 | 97.2 ms: 1.04x faster                                                        |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                                        |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.52 sec: 1.04x faster                                                       |
| xml_etree_generate         | 86.8 ms                                                | 83.8 ms: 1.04x faster                                                        |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                         |
| sqlglot_normalize          | 108 ms                                                 | 105 ms: 1.03x faster                                                         |
| json                       | 5.32 ms                                                | 5.18 ms: 1.03x faster                                                        |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                                         |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                         |
| nqueens                    | 80.9 ms                                                | 78.7 ms: 1.03x faster                                                        |
| shortest_path              | 487 ms                                                 | 474 ms: 1.03x faster                                                         |
| gc_traversal               | 4.90 ms                                                | 4.77 ms: 1.03x faster                                                        |
| connected_components       | 447 ms                                                 | 436 ms: 1.03x faster                                                         |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                         |
| crypto_pyaes               | 74.7 ms                                                | 73.0 ms: 1.02x faster                                                        |
| mdp                        | 2.54 sec                                               | 2.49 sec: 1.02x faster                                                       |
| thrift                     | 800 us                                                 | 784 us: 1.02x faster                                                         |
| genshi_text                | 22.6 ms                                                | 22.2 ms: 1.02x faster                                                        |
| generators                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                                        |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                       |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                         |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                         |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                                        |
| deltablue                  | 3.19 ms                                                | 3.16 ms: 1.01x faster                                                        |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                                        |
| sqlglot_parse              | 1.26 ms                                                | 1.25 ms: 1.01x faster                                                        |
| pyflate                    | 470 ms                                                 | 466 ms: 1.01x faster                                                         |
| sqlglot_transpile          | 1.57 ms                                                | 1.56 ms: 1.01x faster                                                        |
| sympy_expand               | 456 ms                                                 | 453 ms: 1.01x faster                                                         |
| sqlglot_optimize           | 53.4 ms                                                | 53.0 ms: 1.01x faster                                                        |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.00x faster                                                       |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| django_template            | 31.7 ms                                                | 31.8 ms: 1.01x slower                                                        |
| python_startup_no_site     | 7.00 ms                                                | 7.08 ms: 1.01x slower                                                        |
| xml_etree_process          | 60.5 ms                                                | 61.4 ms: 1.02x slower                                                        |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                                         |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                        |
| scimark_monte_carlo        | 66.8 ms                                                | 68.3 ms: 1.02x slower                                                        |
| chaos                      | 58.0 ms                                                | 59.4 ms: 1.02x slower                                                        |
| hexiom                     | 6.08 ms                                                | 6.23 ms: 1.02x slower                                                        |
| fannkuch                   | 394 ms                                                 | 407 ms: 1.03x slower                                                         |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                         |
| bench_thread_pool          | 818 us                                                 | 864 us: 1.06x slower                                                         |
| nbody                      | 87.7 ms                                                | 92.9 ms: 1.06x slower                                                        |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                                        |
| unpickle_pure_python       | 213 us                                                 | 226 us: 1.06x slower                                                         |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                        |
| json_loads                 | 27.2 us                                                | 29.0 us: 1.07x slower                                                        |
| coverage                   | 82.8 ms                                                | 89.8 ms: 1.08x slower                                                        |
| pickle_pure_python         | 302 us                                                 | 331 us: 1.09x slower                                                         |
| many_optionals             | 857 us                                                 | 950 us: 1.11x slower                                                         |
| json_dumps                 | 10.1 ms                                                | 11.9 ms: 1.18x slower                                                        |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.7 ms: 3.41x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (10): logging_silent, genshi_xml, dulwich_log, logging_simple, asyncio_websockets, pprint_safe_repr, create_gc_cycles, docutils, scimark_lu, logging_format
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.044x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x