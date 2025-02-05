# Results vs. 3.13.0

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: 875bc77
- commit date: 2025-02-04
- overall geometric mean: 1.054x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 250 ms: 1.06x faster                                                       |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.00x faster                                                     |
| html5lib       | 63.4 ms                                                | 61.3 ms: 1.03x faster                                                      |
| sphinx         | 1.03 sec                                               | 999 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 624 ms: 1.38x faster                                                       |
| async_tree_io              | 838 ms                                                 | 624 ms: 1.34x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 327 ms: 1.34x faster                                                       |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 258 ms: 1.24x faster                                                       |
| async_generators           | 433 ms                                                 | 380 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 492 ms: 1.10x faster                                                       |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 68.5 ms: 1.15x faster                                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| nbody          | 87.7 ms                                                | 92.1 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.27 ms: 1.15x faster                                                      |
| regex_compile  | 132 ms                                                 | 124 ms: 1.06x faster                                                       |
| regex_v8       | 26.9 ms                                                | 25.6 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                       |
| tomli_loads          | 2.12 sec                                               | 1.93 sec: 1.10x faster                                                     |
| xml_etree_generate   | 86.8 ms                                                | 82.6 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 96.9 ms: 1.04x faster                                                      |
| xml_etree_process    | 60.5 ms                                                | 58.1 ms: 1.04x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 214 us: 1.00x slower                                                       |
| pickle_pure_python   | 302 us                                                 | 312 us: 1.03x slower                                                       |
| json_loads           | 27.2 us                                                | 28.7 us: 1.06x slower                                                      |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.03 ms: 1.00x slower                                                      |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                      |
| genshi_xml      | 50.5 ms                                                | 47.7 ms: 1.06x faster                                                      |
| django_template | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                      |
| mako            | 10.7 ms                                                | 11.3 ms: 1.05x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                       |
| deepcopy                   | 354 us                                                 | 250 us: 1.42x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 624 ms: 1.38x faster                                                       |
| async_tree_io              | 838 ms                                                 | 624 ms: 1.34x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 327 ms: 1.34x faster                                                       |
| async_tree_none            | 350 ms                                                 | 267 ms: 1.31x faster                                                       |
| deepcopy_memo              | 38.4 us                                                | 29.3 us: 1.31x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 258 ms: 1.24x faster                                                       |
| go                         | 141 ms                                                 | 115 ms: 1.22x faster                                                       |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                      |
| spectral_norm              | 113 ms                                                 | 97.0 ms: 1.17x faster                                                      |
| pylint                     | 312 ms                                                 | 270 ms: 1.15x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.27 ms: 1.15x faster                                                      |
| float                      | 78.7 ms                                                | 68.5 ms: 1.15x faster                                                      |
| async_generators           | 433 ms                                                 | 380 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 502 ms: 1.14x faster                                                       |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                       |
| pathlib                    | 17.4 ms                                                | 15.7 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 492 ms: 1.10x faster                                                       |
| tomli_loads                | 2.12 sec                                               | 1.93 sec: 1.10x faster                                                     |
| scimark_fft                | 367 ms                                                 | 340 ms: 1.08x faster                                                       |
| richards                   | 47.5 ms                                                | 44.1 ms: 1.08x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.11 sec: 1.08x faster                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.38 sec: 1.07x faster                                                     |
| crypto_pyaes               | 74.7 ms                                                | 69.9 ms: 1.07x faster                                                      |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                      |
| richards_super             | 53.7 ms                                                | 50.5 ms: 1.06x faster                                                      |
| regex_compile              | 132 ms                                                 | 124 ms: 1.06x faster                                                       |
| 2to3                       | 266 ms                                                 | 250 ms: 1.06x faster                                                       |
| genshi_xml                 | 50.5 ms                                                | 47.7 ms: 1.06x faster                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.76 ms: 1.06x faster                                                      |
| sqlglot_normalize          | 108 ms                                                 | 103 ms: 1.05x faster                                                       |
| telco                      | 8.40 ms                                                | 7.98 ms: 1.05x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 82.6 ms: 1.05x faster                                                      |
| regex_v8                   | 26.9 ms                                                | 25.6 ms: 1.05x faster                                                      |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                                      |
| k_core                     | 2.37 sec                                               | 2.26 sec: 1.05x faster                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 96.9 ms: 1.04x faster                                                      |
| thrift                     | 800 us                                                 | 767 us: 1.04x faster                                                       |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.2 ms: 1.04x faster                                                      |
| xml_etree_process          | 60.5 ms                                                | 58.1 ms: 1.04x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                       |
| sqlglot_optimize           | 53.4 ms                                                | 51.4 ms: 1.04x faster                                                      |
| json                       | 5.32 ms                                                | 5.13 ms: 1.04x faster                                                      |
| mdp                        | 2.54 sec                                               | 2.45 sec: 1.04x faster                                                     |
| sympy_str                  | 273 ms                                                 | 264 ms: 1.04x faster                                                       |
| generators                 | 28.8 ms                                                | 27.8 ms: 1.03x faster                                                      |
| html5lib                   | 63.4 ms                                                | 61.3 ms: 1.03x faster                                                      |
| sphinx                     | 1.03 sec                                               | 999 ms: 1.03x faster                                                       |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                       |
| pprint_safe_repr           | 727 ms                                                 | 707 ms: 1.03x faster                                                       |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.03x faster                                                       |
| logging_simple             | 5.65 us                                                | 5.51 us: 1.03x faster                                                      |
| nqueens                    | 80.9 ms                                                | 78.9 ms: 1.02x faster                                                      |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                       |
| connected_components       | 447 ms                                                 | 436 ms: 1.02x faster                                                       |
| sqlglot_parse              | 1.26 ms                                                | 1.24 ms: 1.02x faster                                                      |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                      |
| pyflate                    | 470 ms                                                 | 460 ms: 1.02x faster                                                       |
| sympy_expand               | 456 ms                                                 | 447 ms: 1.02x faster                                                       |
| typing_runtime_protocols   | 160 us                                                 | 157 us: 1.02x faster                                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.54 ms: 1.02x faster                                                      |
| shortest_path              | 487 ms                                                 | 478 ms: 1.02x faster                                                       |
| comprehensions             | 16.5 us                                                | 16.2 us: 1.02x faster                                                      |
| logging_format             | 6.23 us                                                | 6.14 us: 1.02x faster                                                      |
| deltablue                  | 3.19 ms                                                | 3.15 ms: 1.01x faster                                                      |
| pprint_pformat             | 1.48 sec                                               | 1.46 sec: 1.01x faster                                                     |
| dulwich_log                | 64.6 ms                                                | 63.8 ms: 1.01x faster                                                      |
| scimark_monte_carlo        | 66.8 ms                                                | 66.2 ms: 1.01x faster                                                      |
| django_template            | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                      |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.00x faster                                                     |
| hexiom                     | 6.08 ms                                                | 6.05 ms: 1.00x faster                                                      |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| chaos                      | 58.0 ms                                                | 57.9 ms: 1.00x faster                                                      |
| unpickle_pure_python       | 213 us                                                 | 214 us: 1.00x slower                                                       |
| python_startup_no_site     | 7.00 ms                                                | 7.03 ms: 1.00x slower                                                      |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                      |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                      |
| raytrace                   | 262 ms                                                 | 268 ms: 1.02x slower                                                       |
| gc_traversal               | 4.90 ms                                                | 5.03 ms: 1.03x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 312 us: 1.03x slower                                                       |
| bench_thread_pool          | 818 us                                                 | 855 us: 1.05x slower                                                       |
| nbody                      | 87.7 ms                                                | 92.1 ms: 1.05x slower                                                      |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.05x slower                                                      |
| json_loads                 | 27.2 us                                                | 28.7 us: 1.06x slower                                                      |
| coroutines                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                      |
| many_optionals             | 857 us                                                 | 927 us: 1.08x slower                                                       |
| coverage                   | 82.8 ms                                                | 89.7 ms: 1.08x slower                                                      |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.16x slower                                                      |
| subparsers                 | 15.5 ms                                                | 20.6 ms: 1.33x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 80.5 ms: 3.36x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (5): regex_dna, scimark_lu, fannkuch, asyncio_websockets, logging_silent
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.054x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x