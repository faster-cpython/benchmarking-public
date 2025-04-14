# Results vs. 3.13.0

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: c05e483
- commit date: 2025-02-05
- overall geometric mean: 1.049x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 252 ms: 1.05x faster                                                       |
| html5lib       | 63.4 ms                                                | 61.6 ms: 1.03x faster                                                      |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                       |
| async_tree_io              | 838 ms                                                 | 614 ms: 1.37x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                                       |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                       |
| async_generators           | 433 ms                                                 | 381 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                       |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.8 ms: 1.14x faster                                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| nbody          | 87.7 ms                                                | 94.7 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.36 ms: 1.12x faster                                                      |
| regex_v8       | 26.9 ms                                                | 25.4 ms: 1.06x faster                                                      |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                       |
| regex_dna      | 220 ms                                                 | 213 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                       |
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                     |
| xml_etree_generate   | 86.8 ms                                                | 83.5 ms: 1.04x faster                                                      |
| xml_etree_process    | 60.5 ms                                                | 58.1 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 97.5 ms: 1.04x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                       |
| pickle_pure_python   | 302 us                                                 | 312 us: 1.03x slower                                                       |
| json_loads           | 27.2 us                                                | 28.9 us: 1.07x slower                                                      |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.10 ms: 1.01x slower                                                      |
| python_startup         | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text    | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                      |
| genshi_xml     | 50.5 ms                                                | 48.1 ms: 1.05x faster                                                      |
| mako           | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                       |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                       |
| async_tree_io              | 838 ms                                                 | 614 ms: 1.37x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                                       |
| async_tree_none            | 350 ms                                                 | 261 ms: 1.34x faster                                                       |
| deepcopy_memo              | 38.4 us                                                | 30.1 us: 1.28x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                       |
| go                         | 141 ms                                                 | 115 ms: 1.22x faster                                                       |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.19x faster                                                      |
| spectral_norm              | 113 ms                                                 | 95.5 ms: 1.19x faster                                                      |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                       |
| float                      | 78.7 ms                                                | 68.8 ms: 1.14x faster                                                      |
| async_generators           | 433 ms                                                 | 381 ms: 1.14x faster                                                       |
| pylint                     | 312 ms                                                 | 275 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.36 ms: 1.12x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                       |
| pathlib                    | 17.4 ms                                                | 15.8 ms: 1.10x faster                                                      |
| richards                   | 47.5 ms                                                | 43.4 ms: 1.10x faster                                                      |
| richards_super             | 53.7 ms                                                | 49.3 ms: 1.09x faster                                                      |
| telco                      | 8.40 ms                                                | 7.76 ms: 1.08x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                     |
| scimark_fft                | 367 ms                                                 | 341 ms: 1.08x faster                                                       |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                      |
| regex_v8                   | 26.9 ms                                                | 25.4 ms: 1.06x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.44 sec: 1.06x faster                                                     |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                       |
| thrift                     | 800 us                                                 | 759 us: 1.05x faster                                                       |
| 2to3                       | 266 ms                                                 | 252 ms: 1.05x faster                                                       |
| sqlglot_normalize          | 108 ms                                                 | 103 ms: 1.05x faster                                                       |
| genshi_xml                 | 50.5 ms                                                | 48.1 ms: 1.05x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                                      |
| crypto_pyaes               | 74.7 ms                                                | 71.1 ms: 1.05x faster                                                      |
| json                       | 5.32 ms                                                | 5.08 ms: 1.05x faster                                                      |
| logging_format             | 6.23 us                                                | 5.98 us: 1.04x faster                                                      |
| logging_simple             | 5.65 us                                                | 5.42 us: 1.04x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 83.5 ms: 1.04x faster                                                      |
| xml_etree_process          | 60.5 ms                                                | 58.1 ms: 1.04x faster                                                      |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 97.5 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.85 ms: 1.04x faster                                                      |
| pprint_safe_repr           | 727 ms                                                 | 703 ms: 1.03x faster                                                       |
| mdp                        | 2.54 sec                                               | 2.46 sec: 1.03x faster                                                     |
| sqlglot_optimize           | 53.4 ms                                                | 51.7 ms: 1.03x faster                                                      |
| regex_dna                  | 220 ms                                                 | 213 ms: 1.03x faster                                                       |
| sqlglot_parse              | 1.26 ms                                                | 1.23 ms: 1.03x faster                                                      |
| html5lib                   | 63.4 ms                                                | 61.6 ms: 1.03x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                     |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.03x faster                                                     |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                       |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                       |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                       |
| generators                 | 28.8 ms                                                | 28.1 ms: 1.02x faster                                                      |
| shortest_path              | 487 ms                                                 | 476 ms: 1.02x faster                                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.54 ms: 1.02x faster                                                      |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                       |
| pyflate                    | 470 ms                                                 | 460 ms: 1.02x faster                                                       |
| pprint_pformat             | 1.48 sec                                               | 1.45 sec: 1.02x faster                                                     |
| connected_components       | 447 ms                                                 | 439 ms: 1.02x faster                                                       |
| comprehensions             | 16.5 us                                                | 16.2 us: 1.02x faster                                                      |
| sympy_expand               | 456 ms                                                 | 450 ms: 1.01x faster                                                       |
| nqueens                    | 80.9 ms                                                | 79.9 ms: 1.01x faster                                                      |
| deltablue                  | 3.19 ms                                                | 3.16 ms: 1.01x faster                                                      |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.00x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 152 ms: 1.01x slower                                                       |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                      |
| mako                       | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                      |
| chaos                      | 58.0 ms                                                | 58.7 ms: 1.01x slower                                                      |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.01x slower                                                       |
| python_startup_no_site     | 7.00 ms                                                | 7.10 ms: 1.01x slower                                                      |
| logging_silent             | 101 ns                                                 | 103 ns: 1.02x slower                                                       |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                      |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                       |
| python_startup             | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                      |
| gc_traversal               | 4.90 ms                                                | 5.03 ms: 1.03x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 312 us: 1.03x slower                                                       |
| fannkuch                   | 394 ms                                                 | 407 ms: 1.03x slower                                                       |
| raytrace                   | 262 ms                                                 | 271 ms: 1.03x slower                                                       |
| dulwich_log                | 64.6 ms                                                | 66.9 ms: 1.04x slower                                                      |
| hexiom                     | 6.08 ms                                                | 6.33 ms: 1.04x slower                                                      |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                      |
| json_loads                 | 27.2 us                                                | 28.9 us: 1.07x slower                                                      |
| bench_thread_pool          | 818 us                                                 | 872 us: 1.07x slower                                                       |
| nbody                      | 87.7 ms                                                | 94.7 ms: 1.08x slower                                                      |
| many_optionals             | 857 us                                                 | 946 us: 1.10x slower                                                       |
| coverage                   | 82.8 ms                                                | 91.8 ms: 1.11x slower                                                      |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                      |
| subparsers                 | 15.5 ms                                                | 20.5 ms: 1.33x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 82.3 ms: 3.43x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (5): django_template, asyncio_websockets, docutils, typing_runtime_protocols, scimark_monte_carlo
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x