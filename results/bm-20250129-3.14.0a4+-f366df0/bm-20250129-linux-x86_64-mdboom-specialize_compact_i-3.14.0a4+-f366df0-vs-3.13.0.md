# Results vs. 3.13.0

- fork: mdboom
- ref: specialize_compact_i
- machine: linux-x86_64
- commit hash: f366df0
- commit date: 2025-01-29
- overall geometric mean: 1.048x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 253 ms: 1.05x faster                                                   |
| html5lib       | 63.4 ms                                                | 60.7 ms: 1.04x faster                                                  |
| sphinx         | 1.03 sec                                               | 996 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 609 ms: 1.41x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 321 ms: 1.36x faster                                                   |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                                   |
| async_generators           | 433 ms                                                 | 384 ms: 1.13x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.9 ms: 1.11x faster                                                  |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| nbody          | 87.7 ms                                                | 93.2 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.34 ms: 1.13x faster                                                  |
| regex_v8       | 26.9 ms                                                | 25.5 ms: 1.05x faster                                                  |
| regex_compile  | 132 ms                                                 | 125 ms: 1.05x faster                                                   |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 97.4 ms: 1.04x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 58.4 ms: 1.04x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 83.9 ms: 1.03x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                   |
| json_loads           | 27.2 us                                                | 28.8 us: 1.06x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.05 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 49.1 ms: 1.03x faster                                                  |
| django_template | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                  |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 609 ms: 1.41x faster                                                   |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 321 ms: 1.36x faster                                                   |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 253 ms: 1.26x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 30.8 us: 1.25x faster                                                  |
| go                         | 141 ms                                                 | 117 ms: 1.20x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.20x faster                                                  |
| spectral_norm              | 113 ms                                                 | 95.9 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                   |
| pylint                     | 312 ms                                                 | 272 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.34 ms: 1.13x faster                                                  |
| async_generators           | 433 ms                                                 | 384 ms: 1.13x faster                                                   |
| float                      | 78.7 ms                                                | 70.9 ms: 1.11x faster                                                  |
| pathlib                    | 17.4 ms                                                | 15.8 ms: 1.10x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                   |
| scimark_fft                | 367 ms                                                 | 335 ms: 1.09x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.62 ms: 1.09x faster                                                  |
| telco                      | 8.40 ms                                                | 7.78 ms: 1.08x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                 |
| richards                   | 47.5 ms                                                | 44.2 ms: 1.08x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 69.9 ms: 1.07x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.41 sec: 1.06x faster                                                 |
| richards_super             | 53.7 ms                                                | 50.8 ms: 1.06x faster                                                  |
| thrift                     | 800 us                                                 | 759 us: 1.05x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.05x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 25.5 ms: 1.05x faster                                                  |
| regex_compile              | 132 ms                                                 | 125 ms: 1.05x faster                                                   |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                  |
| 2to3                       | 266 ms                                                 | 253 ms: 1.05x faster                                                   |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                                   |
| sqlglot_normalize          | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| html5lib                   | 63.4 ms                                                | 60.7 ms: 1.04x faster                                                  |
| pyflate                    | 470 ms                                                 | 450 ms: 1.04x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 97.4 ms: 1.04x faster                                                  |
| mdp                        | 2.54 sec                                               | 2.45 sec: 1.04x faster                                                 |
| logging_simple             | 5.65 us                                                | 5.45 us: 1.04x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                   |
| sphinx                     | 1.03 sec                                               | 996 ms: 1.04x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 58.4 ms: 1.04x faster                                                  |
| json                       | 5.32 ms                                                | 5.14 ms: 1.03x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 83.9 ms: 1.03x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                   |
| logging_format             | 6.23 us                                                | 6.04 us: 1.03x faster                                                  |
| connected_components       | 447 ms                                                 | 434 ms: 1.03x faster                                                   |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                 |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 49.1 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 52.0 ms: 1.03x faster                                                  |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.03x faster                                                   |
| typing_runtime_protocols   | 160 us                                                 | 156 us: 1.02x faster                                                   |
| shortest_path              | 487 ms                                                 | 477 ms: 1.02x faster                                                   |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                   |
| generators                 | 28.8 ms                                                | 28.3 ms: 1.02x faster                                                  |
| sympy_expand               | 456 ms                                                 | 449 ms: 1.02x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 63.9 ms: 1.01x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 66.3 ms: 1.01x faster                                                  |
| nqueens                    | 80.9 ms                                                | 80.5 ms: 1.00x faster                                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| pprint_safe_repr           | 727 ms                                                 | 731 ms: 1.01x slower                                                   |
| sqlglot_transpile          | 1.57 ms                                                | 1.58 ms: 1.01x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.05 ms: 1.01x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                  |
| django_template            | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.01x slower                                                 |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                   |
| chaos                      | 58.0 ms                                                | 59.0 ms: 1.02x slower                                                  |
| fannkuch                   | 394 ms                                                 | 401 ms: 1.02x slower                                                   |
| deltablue                  | 3.19 ms                                                | 3.28 ms: 1.03x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 5.03 ms: 1.03x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.29 ms: 1.04x slower                                                  |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 858 us: 1.05x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                   |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                                  |
| nbody                      | 87.7 ms                                                | 93.2 ms: 1.06x slower                                                  |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                                  |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                  |
| many_optionals             | 857 us                                                 | 933 us: 1.09x slower                                                   |
| coverage                   | 82.8 ms                                                | 90.7 ms: 1.10x slower                                                  |
| logging_silent             | 101 ns                                                 | 113 ns: 1.12x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.16x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.4 ms: 1.32x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (4): docutils, comprehensions, asyncio_websockets, sqlglot_parse
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x