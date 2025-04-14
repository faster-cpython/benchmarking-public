# Results vs. 3.13.0

- fork: python
- ref: bff4bfeae1f428a815dc
- machine: linux-x86_64
- commit hash: bff4bfe
- commit date: 2025-02-10
- overall geometric mean: 1.061x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.87 sec: 1.02x slower                                                       |
| html5lib       | 73.5 ms                                                      | 67.5 ms: 1.09x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 342 ms: 1.36x faster                                                         |
| async_tree_io              | 843 ms                                                       | 657 ms: 1.28x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 651 ms: 1.28x faster                                                         |
| async_tree_none            | 376 ms                                                       | 295 ms: 1.27x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 357 ms: 1.27x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 285 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 526 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 515 ms: 1.13x faster                                                         |
| async_generators           | 457 ms                                                       | 411 ms: 1.11x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 69.7 ms: 1.17x faster                                                        |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| nbody          | 89.3 ms                                                      | 101 ms: 1.13x slower                                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.12 ms: 1.18x faster                                                        |
| regex_compile  | 143 ms                                                       | 134 ms: 1.06x faster                                                         |
| regex_dna      | 247 ms                                                       | 237 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.06 sec: 1.20x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 134 ms: 1.12x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 95.4 ms: 1.08x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 207 us: 1.05x faster                                                         |
| xml_etree_generate   | 86.5 ms                                                      | 84.3 ms: 1.03x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 59.6 ms: 1.03x faster                                                        |
| pickle_pure_python   | 323 us                                                       | 327 us: 1.01x slower                                                         |
| json_dumps           | 11.1 ms                                                      | 11.5 ms: 1.04x slower                                                        |
| json_loads           | 24.7 us                                                      | 26.7 us: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.00 ms: 1.00x slower                                                        |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.4 ms: 1.12x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 52.2 ms: 1.09x faster                                                        |
| django_template | 36.4 ms                                                      | 35.2 ms: 1.03x faster                                                        |
| mako            | 10.4 ms                                                      | 10.6 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250210-pythonperf2-x86_64-python-bff4bfeae1f428a815dc-3.14.0a4+-bff4bfe |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 392 us                                                       | 281 us: 1.40x faster                                                         |
| async_tree_memoization_tg  | 466 ms                                                       | 342 ms: 1.36x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 29.5 us: 1.31x faster                                                        |
| async_tree_io              | 843 ms                                                       | 657 ms: 1.28x faster                                                         |
| go                         | 162 ms                                                       | 127 ms: 1.28x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 651 ms: 1.28x faster                                                         |
| async_tree_none            | 376 ms                                                       | 295 ms: 1.27x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 357 ms: 1.27x faster                                                         |
| deepcopy_reduce            | 3.54 us                                                      | 2.89 us: 1.23x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 285 ms: 1.21x faster                                                         |
| generators                 | 33.6 ms                                                      | 28.0 ms: 1.20x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.06 sec: 1.20x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.12 ms: 1.18x faster                                                        |
| float                      | 81.3 ms                                                      | 69.7 ms: 1.17x faster                                                        |
| richards                   | 52.9 ms                                                      | 45.8 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 526 ms: 1.15x faster                                                         |
| richards_super             | 59.6 ms                                                      | 52.1 ms: 1.14x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 85.1 ms: 1.14x faster                                                        |
| pyflate                    | 503 ms                                                       | 445 ms: 1.13x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 515 ms: 1.13x faster                                                         |
| xml_etree_parse            | 150 ms                                                       | 134 ms: 1.12x faster                                                         |
| genshi_text                | 26.2 ms                                                      | 23.4 ms: 1.12x faster                                                        |
| scimark_sor                | 123 ms                                                       | 110 ms: 1.12x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.56 sec: 1.12x faster                                                       |
| async_generators           | 457 ms                                                       | 411 ms: 1.11x faster                                                         |
| telco                      | 8.79 ms                                                      | 7.95 ms: 1.11x faster                                                        |
| pylint                     | 347 ms                                                       | 316 ms: 1.10x faster                                                         |
| genshi_xml                 | 57.1 ms                                                      | 52.2 ms: 1.09x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 67.5 ms: 1.09x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 60.8 ms: 1.09x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 6.07 ms: 1.08x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 95.4 ms: 1.08x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 783 ms: 1.08x faster                                                         |
| pathlib                    | 17.5 ms                                                      | 16.3 ms: 1.08x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.61 sec: 1.07x faster                                                       |
| regex_compile              | 143 ms                                                       | 134 ms: 1.06x faster                                                         |
| sqlglot_parse              | 1.40 ms                                                      | 1.33 ms: 1.05x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 207 us: 1.05x faster                                                         |
| json                       | 5.69 ms                                                      | 5.42 ms: 1.05x faster                                                        |
| thrift                     | 901 us                                                       | 858 us: 1.05x faster                                                         |
| scimark_fft                | 328 ms                                                       | 313 ms: 1.05x faster                                                         |
| connected_components       | 432 ms                                                       | 414 ms: 1.04x faster                                                         |
| sympy_expand               | 509 ms                                                       | 488 ms: 1.04x faster                                                         |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 56.8 ms: 1.04x faster                                                        |
| regex_dna                  | 247 ms                                                       | 237 ms: 1.04x faster                                                         |
| nqueens                    | 90.7 ms                                                      | 87.1 ms: 1.04x faster                                                        |
| sqlglot_normalize          | 119 ms                                                       | 115 ms: 1.04x faster                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 1.72 ms: 1.04x faster                                                        |
| meteor_contest             | 130 ms                                                       | 125 ms: 1.04x faster                                                         |
| shortest_path              | 460 ms                                                       | 443 ms: 1.04x faster                                                         |
| sympy_str                  | 298 ms                                                       | 287 ms: 1.04x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.80 us: 1.04x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 143 ms: 1.04x faster                                                         |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                                       |
| logging_simple             | 6.39 us                                                      | 6.19 us: 1.03x faster                                                        |
| django_template            | 36.4 ms                                                      | 35.2 ms: 1.03x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 95.7 ms: 1.03x faster                                                        |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.8 ms: 1.03x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 84.3 ms: 1.03x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 59.6 ms: 1.03x faster                                                        |
| coverage                   | 80.0 ms                                                      | 78.0 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.02x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.78 us: 1.02x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 66.6 ms: 1.02x faster                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 71.7 ms: 1.02x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.35 ms: 1.02x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 152 ms: 1.02x faster                                                         |
| sympy_integrate            | 23.6 ms                                                      | 23.1 ms: 1.02x faster                                                        |
| mdp                        | 2.54 sec                                                     | 2.50 sec: 1.02x faster                                                       |
| typing_runtime_protocols   | 169 us                                                       | 167 us: 1.01x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                         |
| python_startup_no_site     | 8.96 ms                                                      | 9.00 ms: 1.00x slower                                                        |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                         |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| raytrace                   | 273 ms                                                       | 276 ms: 1.01x slower                                                         |
| pickle_pure_python         | 323 us                                                       | 327 us: 1.01x slower                                                         |
| docutils                   | 2.83 sec                                                     | 2.87 sec: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.86 ms: 1.02x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.73 ms: 1.02x slower                                                        |
| mako                       | 10.4 ms                                                      | 10.6 ms: 1.02x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.04x slower                                                        |
| many_optionals             | 930 us                                                       | 995 us: 1.07x slower                                                         |
| json_loads                 | 24.7 us                                                      | 26.7 us: 1.08x slower                                                        |
| nbody                      | 89.3 ms                                                      | 101 ms: 1.13x slower                                                         |
| subparsers                 | 17.5 ms                                                      | 22.6 ms: 1.29x slower                                                        |
| gc_traversal               | 4.74 ms                                                      | 6.37 ms: 1.34x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.24 sec: 242.41x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (7): regex_v8, bench_thread_pool, fannkuch, logging_silent, comprehensions, chaos, pycparser
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.061x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.02x