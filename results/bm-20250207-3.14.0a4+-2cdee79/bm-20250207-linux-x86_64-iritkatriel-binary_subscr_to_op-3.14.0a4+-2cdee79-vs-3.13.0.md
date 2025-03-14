# Results vs. 3.13.0

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: 2cdee79
- commit date: 2025-02-07
- overall geometric mean: 1.050x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 252 ms: 1.06x faster                                                       |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                     |
| html5lib       | 63.4 ms                                                | 61.2 ms: 1.04x faster                                                      |
| sphinx         | 1.03 sec                                               | 993 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.38x faster                                                       |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                                       |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 501 ms: 1.14x faster                                                       |
| async_generators           | 433 ms                                                 | 384 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 493 ms: 1.10x faster                                                       |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.0 ms: 1.12x faster                                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| nbody          | 87.7 ms                                                | 91.9 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.25 ms: 1.16x faster                                                      |
| regex_v8       | 26.9 ms                                                | 24.3 ms: 1.11x faster                                                      |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                       |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 139 ms: 1.11x faster                                                       |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.08x faster                                                     |
| xml_etree_generate   | 86.8 ms                                                | 83.2 ms: 1.04x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 97.1 ms: 1.04x faster                                                      |
| xml_etree_process    | 60.5 ms                                                | 58.1 ms: 1.04x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                       |
| json_loads           | 27.2 us                                                | 28.7 us: 1.06x slower                                                      |
| pickle_pure_python   | 302 us                                                 | 320 us: 1.06x slower                                                       |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                      |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                      |
| genshi_xml      | 50.5 ms                                                | 48.0 ms: 1.05x faster                                                      |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                      |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250207-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-2cdee79 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 321 ms: 1.44x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.38x faster                                                       |
| deepcopy                   | 354 us                                                 | 259 us: 1.37x faster                                                       |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                                       |
| async_tree_none            | 350 ms                                                 | 263 ms: 1.33x faster                                                       |
| deepcopy_memo              | 38.4 us                                                | 30.7 us: 1.25x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                       |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                      |
| go                         | 141 ms                                                 | 118 ms: 1.19x faster                                                       |
| spectral_norm              | 113 ms                                                 | 96.0 ms: 1.18x faster                                                      |
| regex_effbot               | 3.77 ms                                                | 3.25 ms: 1.16x faster                                                      |
| pylint                     | 312 ms                                                 | 272 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 501 ms: 1.14x faster                                                       |
| async_generators           | 433 ms                                                 | 384 ms: 1.13x faster                                                       |
| float                      | 78.7 ms                                                | 70.0 ms: 1.12x faster                                                      |
| pathlib                    | 17.4 ms                                                | 15.6 ms: 1.11x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 139 ms: 1.11x faster                                                       |
| regex_v8                   | 26.9 ms                                                | 24.3 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 493 ms: 1.10x faster                                                       |
| scimark_fft                | 367 ms                                                 | 337 ms: 1.09x faster                                                       |
| telco                      | 8.40 ms                                                | 7.81 ms: 1.08x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.08x faster                                                     |
| genshi_text                | 22.6 ms                                                | 21.1 ms: 1.07x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                     |
| richards                   | 47.5 ms                                                | 44.6 ms: 1.07x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                                     |
| 2to3                       | 266 ms                                                 | 252 ms: 1.06x faster                                                       |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.06x faster                                                      |
| crypto_pyaes               | 74.7 ms                                                | 70.8 ms: 1.05x faster                                                      |
| pyflate                    | 470 ms                                                 | 446 ms: 1.05x faster                                                       |
| genshi_xml                 | 50.5 ms                                                | 48.0 ms: 1.05x faster                                                      |
| k_core                     | 2.37 sec                                               | 2.25 sec: 1.05x faster                                                     |
| richards_super             | 53.7 ms                                                | 51.2 ms: 1.05x faster                                                      |
| thrift                     | 800 us                                                 | 762 us: 1.05x faster                                                       |
| sqlglot_normalize          | 108 ms                                                 | 103 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.81 ms: 1.05x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 83.2 ms: 1.04x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 97.1 ms: 1.04x faster                                                      |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.2 ms: 1.04x faster                                                      |
| generators                 | 28.8 ms                                                | 27.6 ms: 1.04x faster                                                      |
| xml_etree_process          | 60.5 ms                                                | 58.1 ms: 1.04x faster                                                      |
| json                       | 5.32 ms                                                | 5.12 ms: 1.04x faster                                                      |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                       |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                       |
| sphinx                     | 1.03 sec                                               | 993 ms: 1.04x faster                                                       |
| html5lib                   | 63.4 ms                                                | 61.2 ms: 1.04x faster                                                      |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.04x faster                                                       |
| shortest_path              | 487 ms                                                 | 472 ms: 1.03x faster                                                       |
| sqlglot_optimize           | 53.4 ms                                                | 51.8 ms: 1.03x faster                                                      |
| mdp                        | 2.54 sec                                               | 2.47 sec: 1.03x faster                                                     |
| logging_simple             | 5.65 us                                                | 5.50 us: 1.03x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                       |
| connected_components       | 447 ms                                                 | 435 ms: 1.03x faster                                                       |
| logging_format             | 6.23 us                                                | 6.07 us: 1.03x faster                                                      |
| sympy_str                  | 273 ms                                                 | 266 ms: 1.03x faster                                                       |
| typing_runtime_protocols   | 160 us                                                 | 156 us: 1.02x faster                                                       |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                                       |
| gc_traversal               | 4.90 ms                                                | 4.80 ms: 1.02x faster                                                      |
| comprehensions             | 16.5 us                                                | 16.2 us: 1.02x faster                                                      |
| sqlglot_parse              | 1.26 ms                                                | 1.25 ms: 1.01x faster                                                      |
| dulwich_log                | 64.6 ms                                                | 63.8 ms: 1.01x faster                                                      |
| sympy_expand               | 456 ms                                                 | 451 ms: 1.01x faster                                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.55 ms: 1.01x faster                                                      |
| nqueens                    | 80.9 ms                                                | 80.1 ms: 1.01x faster                                                      |
| deltablue                  | 3.19 ms                                                | 3.17 ms: 1.01x faster                                                      |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                       |
| sympy_integrate            | 19.8 ms                                                | 19.7 ms: 1.01x faster                                                      |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                     |
| pprint_safe_repr           | 727 ms                                                 | 722 ms: 1.01x faster                                                       |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.00x slower                                                      |
| python_startup_no_site     | 7.00 ms                                                | 7.02 ms: 1.00x slower                                                      |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                      |
| chaos                      | 58.0 ms                                                | 58.6 ms: 1.01x slower                                                      |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                      |
| scimark_monte_carlo        | 66.8 ms                                                | 67.9 ms: 1.02x slower                                                      |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                       |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                       |
| fannkuch                   | 394 ms                                                 | 405 ms: 1.03x slower                                                       |
| hexiom                     | 6.08 ms                                                | 6.26 ms: 1.03x slower                                                      |
| raytrace                   | 262 ms                                                 | 271 ms: 1.04x slower                                                       |
| coroutines                 | 22.2 ms                                                | 23.1 ms: 1.04x slower                                                      |
| nbody                      | 87.7 ms                                                | 91.9 ms: 1.05x slower                                                      |
| logging_silent             | 101 ns                                                 | 106 ns: 1.05x slower                                                       |
| bench_thread_pool          | 818 us                                                 | 860 us: 1.05x slower                                                       |
| json_loads                 | 27.2 us                                                | 28.7 us: 1.06x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                       |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                      |
| many_optionals             | 857 us                                                 | 930 us: 1.09x slower                                                       |
| coverage                   | 82.8 ms                                                | 92.4 ms: 1.12x slower                                                      |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.17x slower                                                      |
| subparsers                 | 15.5 ms                                                | 20.3 ms: 1.31x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 80.5 ms: 3.36x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (2): asyncio_websockets, pprint_pformat
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x