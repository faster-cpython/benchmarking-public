# Results vs. 3.13.0

- fork: python
- ref: bac4edad69bb20dd9460
- machine: linux-x86_64
- commit hash: bac4eda
- commit date: 2024-06-16
- overall geometric mean: 1.013x slower
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 266 ms: 1.00x slower                                                  |
| docutils       | 2.58 sec                                               | 2.72 sec: 1.05x slower                                                |
| html5lib       | 63.4 ms                                                | 66.4 ms: 1.05x slower                                                 |
| sphinx         | 1.03 sec                                               | 1.06 sec: 1.02x slower                                                |
| tornado_http   | 91.2 ms                                                | 92.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 431 ms: 1.07x faster                                                  |
| async_generators           | 433 ms                                                 | 436 ms: 1.01x slower                                                  |
| async_tree_none            | 350 ms                                                 | 362 ms: 1.03x slower                                                  |
| async_tree_none_tg         | 319 ms                                                 | 333 ms: 1.04x slower                                                  |
| async_tree_memoization     | 437 ms                                                 | 458 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 603 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 595 ms: 1.10x slower                                                  |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                 |
| async_tree_io_tg           | 861 ms                                                 | 978 ms: 1.14x slower                                                  |
| async_tree_io              | 838 ms                                                 | 952 ms: 1.14x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 77.7 ms: 1.01x faster                                                 |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 23.1 ms: 1.16x faster                                                 |
| regex_effbot   | 3.77 ms                                                | 3.50 ms: 1.07x faster                                                 |
| regex_compile  | 132 ms                                                 | 132 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 86.8 ms                                                | 85.3 ms: 1.02x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 59.4 ms: 1.02x faster                                                 |
| tomli_loads          | 2.12 sec                                               | 2.13 sec: 1.01x slower                                                |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                  |
| json_loads           | 27.2 us                                                | 28.0 us: 1.03x slower                                                 |
| xml_etree_parse      | 154 ms                                                 | 160 ms: 1.04x slower                                                  |
| json_dumps           | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 107 ms: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.01 ms: 1.00x slower                                                 |
| python_startup         | 12.7 ms                                                | 14.4 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 51.2 ms: 1.01x slower                                                 |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                 |
| genshi_text     | 22.6 ms                                                | 23.2 ms: 1.03x slower                                                 |
| mako            | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 354 us                                                 | 260 us: 1.36x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.5 us: 1.30x faster                                                 |
| deepcopy_reduce            | 3.24 us                                                | 2.69 us: 1.20x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 23.1 ms: 1.16x faster                                                 |
| gc_traversal               | 4.90 ms                                                | 4.49 ms: 1.09x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.50 ms: 1.07x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 431 ms: 1.07x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.3 ms: 1.06x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                |
| crypto_pyaes               | 74.7 ms                                                | 72.6 ms: 1.03x faster                                                 |
| nqueens                    | 80.9 ms                                                | 78.7 ms: 1.03x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 85.3 ms: 1.02x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 59.4 ms: 1.02x faster                                                 |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| float                      | 78.7 ms                                                | 77.7 ms: 1.01x faster                                                 |
| scimark_lu                 | 114 ms                                                 | 113 ms: 1.01x faster                                                  |
| mdp                        | 2.54 sec                                               | 2.52 sec: 1.01x faster                                                |
| spectral_norm              | 113 ms                                                 | 112 ms: 1.01x faster                                                  |
| scimark_fft                | 367 ms                                                 | 365 ms: 1.00x faster                                                  |
| thrift                     | 800 us                                                 | 797 us: 1.00x faster                                                  |
| regex_compile              | 132 ms                                                 | 132 ms: 1.00x faster                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.01 ms: 1.00x slower                                                 |
| 2to3                       | 266 ms                                                 | 266 ms: 1.00x slower                                                  |
| generators                 | 28.8 ms                                                | 28.9 ms: 1.00x slower                                                 |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                  |
| raytrace                   | 262 ms                                                 | 263 ms: 1.01x slower                                                  |
| async_generators           | 433 ms                                                 | 436 ms: 1.01x slower                                                  |
| many_optionals             | 857 us                                                 | 862 us: 1.01x slower                                                  |
| tomli_loads                | 2.12 sec                                               | 2.13 sec: 1.01x slower                                                |
| deltablue                  | 3.19 ms                                                | 3.22 ms: 1.01x slower                                                 |
| tornado_http               | 91.2 ms                                                | 92.1 ms: 1.01x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 825 us: 1.01x slower                                                  |
| sympy_str                  | 273 ms                                                 | 276 ms: 1.01x slower                                                  |
| telco                      | 8.40 ms                                                | 8.48 ms: 1.01x slower                                                 |
| dulwich_log                | 64.6 ms                                                | 65.2 ms: 1.01x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.14 ms: 1.01x slower                                                 |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                 |
| sqlite_synth               | 2.90 us                                                | 2.93 us: 1.01x slower                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.09 ms: 1.01x slower                                                 |
| chaos                      | 58.0 ms                                                | 58.7 ms: 1.01x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.01x slower                                                 |
| genshi_xml                 | 50.5 ms                                                | 51.2 ms: 1.01x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 737 ms: 1.01x slower                                                  |
| logging_format             | 6.23 us                                                | 6.33 us: 1.02x slower                                                 |
| go                         | 141 ms                                                 | 143 ms: 1.02x slower                                                  |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 136 ms: 1.02x slower                                                  |
| logging_simple             | 5.65 us                                                | 5.77 us: 1.02x slower                                                 |
| pyflate                    | 470 ms                                                 | 480 ms: 1.02x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.02x slower                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                 |
| sphinx                     | 1.03 sec                                               | 1.06 sec: 1.02x slower                                                |
| pprint_pformat             | 1.48 sec                                               | 1.51 sec: 1.02x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 68.5 ms: 1.03x slower                                                 |
| genshi_text                | 22.6 ms                                                | 23.2 ms: 1.03x slower                                                 |
| sympy_expand               | 456 ms                                                 | 470 ms: 1.03x slower                                                  |
| json_loads                 | 27.2 us                                                | 28.0 us: 1.03x slower                                                 |
| async_tree_none            | 350 ms                                                 | 362 ms: 1.03x slower                                                  |
| xml_etree_parse            | 154 ms                                                 | 160 ms: 1.04x slower                                                  |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                 |
| logging_silent             | 101 ns                                                 | 105 ns: 1.04x slower                                                  |
| async_tree_none_tg         | 319 ms                                                 | 333 ms: 1.04x slower                                                  |
| html5lib                   | 63.4 ms                                                | 66.4 ms: 1.05x slower                                                 |
| richards                   | 47.5 ms                                                | 49.9 ms: 1.05x slower                                                 |
| async_tree_memoization     | 437 ms                                                 | 458 ms: 1.05x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 10.6 ms: 1.05x slower                                                 |
| fannkuch                   | 394 ms                                                 | 414 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 603 ms: 1.05x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.72 sec: 1.05x slower                                                |
| xml_etree_iterparse        | 101 ms                                                 | 107 ms: 1.06x slower                                                  |
| richards_super             | 53.7 ms                                                | 57.0 ms: 1.06x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 5.05 sec: 1.08x slower                                                |
| create_gc_cycles           | 2.45 ms                                                | 2.66 ms: 1.08x slower                                                 |
| scimark_sor                | 122 ms                                                 | 134 ms: 1.09x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 595 ms: 1.10x slower                                                  |
| coroutines                 | 22.2 ms                                                | 24.4 ms: 1.10x slower                                                 |
| coverage                   | 82.8 ms                                                | 91.5 ms: 1.11x slower                                                 |
| async_tree_io_tg           | 861 ms                                                 | 978 ms: 1.14x slower                                                  |
| async_tree_io              | 838 ms                                                 | 952 ms: 1.14x slower                                                  |
| python_startup             | 12.7 ms                                                | 14.4 ms: 1.14x slower                                                 |
| k_core                     | 2.37 sec                                               | 3.52 sec: 1.48x slower                                                |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (12): pylint, nbody, regex_dna, shortest_path, connected_components, json, subparsers, pickle_pure_python, asyncio_websockets, bench_mp_pool, sympy_sum, djangocms
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
Ignored benchmarks (12) of results/bm-20240616-3.14.0a0-bac4eda/bm-20240616-linux-x86_64-python-bac4edad69bb20dd9460-3.14.0a0-bac4eda.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 99.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x