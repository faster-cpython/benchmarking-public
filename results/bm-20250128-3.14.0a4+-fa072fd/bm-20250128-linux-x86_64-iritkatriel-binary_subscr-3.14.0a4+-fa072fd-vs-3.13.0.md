# Results vs. 3.13.0

- fork: iritkatriel
- ref: binary_subscr
- machine: linux-x86_64
- commit hash: fa072fd
- commit date: 2025-01-28
- overall geometric mean: 1.037x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.03x faster                                                 |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.01x slower                                               |
| html5lib       | 63.4 ms                                                | 62.2 ms: 1.02x faster                                                |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                 |
| async_tree_io              | 838 ms                                                 | 623 ms: 1.35x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 327 ms: 1.34x faster                                                 |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                 |
| async_generators           | 433 ms                                                 | 387 ms: 1.12x faster                                                 |
| coroutines                 | 22.2 ms                                                | 22.9 ms: 1.03x slower                                                |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                         |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.1 ms: 1.09x faster                                                |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| nbody          | 87.7 ms                                                | 97.9 ms: 1.12x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.18 ms: 1.18x faster                                                |
| regex_v8       | 26.9 ms                                                | 25.7 ms: 1.04x faster                                                |
| regex_dna      | 220 ms                                                 | 214 ms: 1.03x faster                                                 |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 97.4 ms: 1.04x faster                                                |
| tomli_loads          | 2.12 sec                                               | 2.05 sec: 1.03x faster                                               |
| xml_etree_generate   | 86.8 ms                                                | 84.8 ms: 1.02x faster                                                |
| xml_etree_process    | 60.5 ms                                                | 59.5 ms: 1.02x faster                                                |
| unpickle_pure_python | 213 us                                                 | 221 us: 1.04x slower                                                 |
| json_loads           | 27.2 us                                                | 29.0 us: 1.07x slower                                                |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.07x slower                                                 |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.0 ms: 1.03x faster                                                |
| genshi_xml      | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250128-linux-x86_64-iritkatriel-binary_subscr-3.14.0a4+-fa072fd |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                 |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                 |
| async_tree_io              | 838 ms                                                 | 623 ms: 1.35x faster                                                 |
| async_tree_memoization     | 437 ms                                                 | 327 ms: 1.34x faster                                                 |
| async_tree_none            | 350 ms                                                 | 265 ms: 1.32x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                 |
| deepcopy_memo              | 38.4 us                                                | 31.1 us: 1.24x faster                                                |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                |
| go                         | 141 ms                                                 | 119 ms: 1.19x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.18 ms: 1.18x faster                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                 |
| spectral_norm              | 113 ms                                                 | 97.9 ms: 1.16x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                 |
| pylint                     | 312 ms                                                 | 276 ms: 1.13x faster                                                 |
| async_generators           | 433 ms                                                 | 387 ms: 1.12x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                 |
| float                      | 78.7 ms                                                | 72.1 ms: 1.09x faster                                                |
| telco                      | 8.40 ms                                                | 7.85 ms: 1.07x faster                                                |
| richards                   | 47.5 ms                                                | 44.6 ms: 1.07x faster                                                |
| scimark_fft                | 367 ms                                                 | 346 ms: 1.06x faster                                                 |
| thrift                     | 800 us                                                 | 757 us: 1.06x faster                                                 |
| pathlib                    | 17.4 ms                                                | 16.4 ms: 1.06x faster                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.77 ms: 1.05x faster                                                |
| richards_super             | 53.7 ms                                                | 51.1 ms: 1.05x faster                                                |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                               |
| regex_v8                   | 26.9 ms                                                | 25.7 ms: 1.04x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                                |
| xml_etree_iterparse        | 101 ms                                                 | 97.4 ms: 1.04x faster                                                |
| json                       | 5.32 ms                                                | 5.13 ms: 1.04x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.53 sec: 1.04x faster                                               |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.04x faster                                               |
| 2to3                       | 266 ms                                                 | 257 ms: 1.03x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 2.05 sec: 1.03x faster                                               |
| sqlglot_normalize          | 108 ms                                                 | 105 ms: 1.03x faster                                                 |
| regex_dna                  | 220 ms                                                 | 214 ms: 1.03x faster                                                 |
| genshi_text                | 22.6 ms                                                | 22.0 ms: 1.03x faster                                                |
| shortest_path              | 487 ms                                                 | 475 ms: 1.02x faster                                                 |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.02x faster                                               |
| generators                 | 28.8 ms                                                | 28.1 ms: 1.02x faster                                                |
| xml_etree_generate         | 86.8 ms                                                | 84.8 ms: 1.02x faster                                                |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.5 ms: 1.02x faster                                                |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                               |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                 |
| html5lib                   | 63.4 ms                                                | 62.2 ms: 1.02x faster                                                |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                 |
| sympy_str                  | 273 ms                                                 | 268 ms: 1.02x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 49.6 ms: 1.02x faster                                                |
| gc_traversal               | 4.90 ms                                                | 4.81 ms: 1.02x faster                                                |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                 |
| connected_components       | 447 ms                                                 | 439 ms: 1.02x faster                                                 |
| logging_format             | 6.23 us                                                | 6.13 us: 1.02x faster                                                |
| xml_etree_process          | 60.5 ms                                                | 59.5 ms: 1.02x faster                                                |
| sqlglot_optimize           | 53.4 ms                                                | 52.6 ms: 1.01x faster                                                |
| logging_simple             | 5.65 us                                                | 5.58 us: 1.01x faster                                                |
| sympy_expand               | 456 ms                                                 | 450 ms: 1.01x faster                                                 |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                 |
| typing_runtime_protocols   | 160 us                                                 | 159 us: 1.01x faster                                                 |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.45 ms: 1.00x slower                                                |
| sympy_integrate            | 19.8 ms                                                | 19.9 ms: 1.00x slower                                                |
| crypto_pyaes               | 74.7 ms                                                | 74.9 ms: 1.00x slower                                                |
| dulwich_log                | 64.6 ms                                                | 64.8 ms: 1.00x slower                                                |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.00x slower                                                |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                |
| scimark_monte_carlo        | 66.8 ms                                                | 67.2 ms: 1.01x slower                                                |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.01x slower                                               |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 736 ms: 1.01x slower                                                 |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.01x slower                                                 |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                |
| pprint_pformat             | 1.48 sec                                               | 1.51 sec: 1.02x slower                                               |
| deltablue                  | 3.19 ms                                                | 3.27 ms: 1.02x slower                                                |
| pyflate                    | 470 ms                                                 | 482 ms: 1.03x slower                                                 |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                |
| coroutines                 | 22.2 ms                                                | 22.9 ms: 1.03x slower                                                |
| chaos                      | 58.0 ms                                                | 60.1 ms: 1.04x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 221 us: 1.04x slower                                                 |
| nqueens                    | 80.9 ms                                                | 83.8 ms: 1.04x slower                                                |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.40 ms: 1.05x slower                                                |
| raytrace                   | 262 ms                                                 | 277 ms: 1.06x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 867 us: 1.06x slower                                                 |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                |
| json_loads                 | 27.2 us                                                | 29.0 us: 1.07x slower                                                |
| fannkuch                   | 394 ms                                                 | 423 ms: 1.07x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.07x slower                                                 |
| coverage                   | 82.8 ms                                                | 89.8 ms: 1.08x slower                                                |
| logging_silent             | 101 ns                                                 | 110 ns: 1.09x slower                                                 |
| many_optionals             | 857 us                                                 | 946 us: 1.10x slower                                                 |
| nbody                      | 87.7 ms                                                | 97.9 ms: 1.12x slower                                                |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x