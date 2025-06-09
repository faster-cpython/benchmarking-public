# Results vs. 3.13.0

- fork: gpshead
- ref: traceback_timestamps
- machine: linux-x86_64
- commit hash: e4f54d4
- commit date: 2025-06-08
- overall geometric mean: 1.044x slower
- HPT reliability: 98.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                                   |
| html5lib       | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                   |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                   |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                   |
| coroutines                 | 22.2 ms                                                | 26.4 ms: 1.19x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.9 ms: 1.08x faster                                                  |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| nbody          | 87.7 ms                                                | 102 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                  |
| regex_v8       | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                  |
| regex_dna      | 220 ms                                                 | 211 ms: 1.04x faster                                                   |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 143 ms: 1.08x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 98.8 ms: 1.02x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 86.1 ms: 1.01x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 61.0 ms: 1.01x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 223 us: 1.05x slower                                                   |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 322 us: 1.06x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.1 ms: 1.05x faster                                                  |
| python_startup_no_site | 7.00 ms                                                | 6.89 ms: 1.02x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                  |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                  |
| mako            | 10.7 ms                                                | 11.7 ms: 1.09x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                                 |
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                   |
| async_tree_io              | 838 ms                                                 | 600 ms: 1.40x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 622 ms: 1.38x faster                                                   |
| deepcopy                   | 354 us                                                 | 256 us: 1.38x faster                                                   |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.34x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.31x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                   |
| go                         | 141 ms                                                 | 112 ms: 1.25x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.68 us: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 490 ms: 1.17x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 484 ms: 1.12x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 23.9 ms: 1.12x faster                                                  |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                   |
| richards                   | 47.5 ms                                                | 43.0 ms: 1.11x faster                                                  |
| pyflate                    | 470 ms                                                 | 429 ms: 1.10x faster                                                   |
| richards_super             | 53.7 ms                                                | 49.4 ms: 1.09x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 59.5 ms: 1.09x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 143 ms: 1.08x faster                                                   |
| float                      | 78.7 ms                                                | 72.9 ms: 1.08x faster                                                  |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                   |
| python_startup             | 12.7 ms                                                | 12.1 ms: 1.05x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 2.03 sec: 1.04x faster                                                 |
| pathlib                    | 17.4 ms                                                | 16.7 ms: 1.04x faster                                                  |
| regex_dna                  | 220 ms                                                 | 211 ms: 1.04x faster                                                   |
| telco                      | 8.40 ms                                                | 8.08 ms: 1.04x faster                                                  |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                                   |
| genshi_text                | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                  |
| comprehensions             | 16.5 us                                                | 15.9 us: 1.04x faster                                                  |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.81 us: 1.03x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.55 sec: 1.03x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.03x faster                                                 |
| spectral_norm              | 113 ms                                                 | 110 ms: 1.03x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 98.8 ms: 1.02x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.02x faster                                                 |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                   |
| html5lib                   | 63.4 ms                                                | 62.3 ms: 1.02x faster                                                  |
| python_startup_no_site     | 7.00 ms                                                | 6.89 ms: 1.02x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.01x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.84 ms: 1.01x faster                                                  |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 86.1 ms: 1.01x faster                                                  |
| sympy_expand               | 456 ms                                                 | 453 ms: 1.01x faster                                                   |
| nqueens                    | 80.9 ms                                                | 81.3 ms: 1.01x slower                                                  |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| xml_etree_process          | 60.5 ms                                                | 61.0 ms: 1.01x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 75.5 ms: 1.01x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 68.6 ms: 1.03x slower                                                  |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.20 ms: 1.03x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.55 ms: 1.04x slower                                                  |
| generators                 | 28.8 ms                                                | 30.1 ms: 1.04x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 223 us: 1.05x slower                                                   |
| scimark_fft                | 367 ms                                                 | 384 ms: 1.05x slower                                                   |
| raytrace                   | 262 ms                                                 | 276 ms: 1.05x slower                                                   |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 170 us: 1.06x slower                                                   |
| chaos                      | 58.0 ms                                                | 61.6 ms: 1.06x slower                                                  |
| fannkuch                   | 394 ms                                                 | 418 ms: 1.06x slower                                                   |
| connected_components       | 447 ms                                                 | 475 ms: 1.06x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 322 us: 1.06x slower                                                   |
| shortest_path              | 487 ms                                                 | 521 ms: 1.07x slower                                                   |
| pprint_safe_repr           | 727 ms                                                 | 792 ms: 1.09x slower                                                   |
| mako                       | 10.7 ms                                                | 11.7 ms: 1.09x slower                                                  |
| logging_simple             | 5.65 us                                                | 6.20 us: 1.10x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.62 sec: 1.10x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.53 ms: 1.10x slower                                                  |
| logging_format             | 6.23 us                                                | 6.93 us: 1.11x slower                                                  |
| many_optionals             | 857 us                                                 | 958 us: 1.12x slower                                                   |
| nbody                      | 87.7 ms                                                | 102 ms: 1.16x slower                                                   |
| coroutines                 | 22.2 ms                                                | 26.4 ms: 1.19x slower                                                  |
| subparsers                 | 15.5 ms                                                | 23.4 ms: 1.52x slower                                                  |
| logging_silent             | 101 ns                                                 | 474 ns: 4.69x slower                                                   |
| coverage                   | 82.8 ms                                                | 438 ms: 5.29x slower                                                   |
| thrift                     | 800 us                                                 | 148 ms: 185.25x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                           |

Benchmark hidden because not significant (5): json, docutils, hexiom, asyncio_websockets, scimark_sor
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250608-3.15.0a0-e4f54d4/bm-20250608-linux-x86_64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.044x slower

# HPT report

- Reliability score: 98.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x