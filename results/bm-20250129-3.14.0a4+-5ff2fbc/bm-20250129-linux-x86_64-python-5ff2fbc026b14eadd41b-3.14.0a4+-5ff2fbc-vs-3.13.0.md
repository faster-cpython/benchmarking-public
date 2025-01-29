# Results vs. 3.13.0

- fork: python
- ref: 5ff2fbc026b14eadd41b
- machine: linux-x86_64
- commit hash: 5ff2fbc
- commit date: 2025-01-29
- overall geometric mean: 1.046x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 253 ms: 1.05x faster                                                   |
| html5lib       | 63.4 ms                                                | 61.8 ms: 1.02x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 624 ms: 1.38x faster                                                   |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                   |
| async_generators           | 433 ms                                                 | 380 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                   |
| coroutines                 | 22.2 ms                                                | 24.0 ms: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 72.3 ms: 1.09x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| nbody          | 87.7 ms                                                | 94.3 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.27 ms: 1.15x faster                                                  |
| regex_v8       | 26.9 ms                                                | 25.4 ms: 1.06x faster                                                  |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                   |
| regex_dna      | 220 ms                                                 | 218 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.97 sec: 1.08x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 96.4 ms: 1.05x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 83.6 ms: 1.04x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 58.4 ms: 1.04x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                   |
| json_loads           | 27.2 us                                                | 28.6 us: 1.05x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.9 ms: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 48.2 ms: 1.05x faster                                                  |
| django_template | 31.7 ms                                                | 31.3 ms: 1.01x faster                                                  |
| mako            | 10.7 ms                                                | 11.6 ms: 1.09x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250129-linux-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 319 ms: 1.45x faster                                                   |
| deepcopy                   | 354 us                                                 | 255 us: 1.39x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 624 ms: 1.38x faster                                                   |
| async_tree_io              | 838 ms                                                 | 620 ms: 1.35x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 30.3 us: 1.27x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.67 us: 1.21x faster                                                  |
| go                         | 141 ms                                                 | 119 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 488 ms: 1.17x faster                                                   |
| spectral_norm              | 113 ms                                                 | 96.6 ms: 1.17x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.27 ms: 1.15x faster                                                  |
| pylint                     | 312 ms                                                 | 272 ms: 1.15x faster                                                   |
| async_generators           | 433 ms                                                 | 380 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 477 ms: 1.14x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                   |
| float                      | 78.7 ms                                                | 72.3 ms: 1.09x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.0 ms: 1.09x faster                                                  |
| telco                      | 8.40 ms                                                | 7.78 ms: 1.08x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.97 sec: 1.08x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.68 ms: 1.07x faster                                                  |
| scimark_fft                | 367 ms                                                 | 344 ms: 1.07x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.40 sec: 1.07x faster                                                 |
| richards_super             | 53.7 ms                                                | 50.8 ms: 1.06x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                 |
| richards                   | 47.5 ms                                                | 44.9 ms: 1.06x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.06x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 25.4 ms: 1.06x faster                                                  |
| sqlglot_normalize          | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| 2to3                       | 266 ms                                                 | 253 ms: 1.05x faster                                                   |
| genshi_text                | 22.6 ms                                                | 21.5 ms: 1.05x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 96.4 ms: 1.05x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 48.2 ms: 1.05x faster                                                  |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                   |
| thrift                     | 800 us                                                 | 767 us: 1.04x faster                                                   |
| pyflate                    | 470 ms                                                 | 450 ms: 1.04x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 71.7 ms: 1.04x faster                                                  |
| xml_etree_generate         | 86.8 ms                                                | 83.6 ms: 1.04x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.44 us: 1.04x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 51.5 ms: 1.04x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 58.4 ms: 1.04x faster                                                  |
| json                       | 5.32 ms                                                | 5.14 ms: 1.04x faster                                                  |
| mdp                        | 2.54 sec                                               | 2.46 sec: 1.03x faster                                                 |
| sympy_str                  | 273 ms                                                 | 264 ms: 1.03x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                 |
| html5lib                   | 63.4 ms                                                | 61.8 ms: 1.02x faster                                                  |
| typing_runtime_protocols   | 160 us                                                 | 156 us: 1.02x faster                                                   |
| sympy_expand               | 456 ms                                                 | 447 ms: 1.02x faster                                                   |
| logging_format             | 6.23 us                                                | 6.11 us: 1.02x faster                                                  |
| pprint_safe_repr           | 727 ms                                                 | 712 ms: 1.02x faster                                                   |
| shortest_path              | 487 ms                                                 | 480 ms: 1.01x faster                                                   |
| connected_components       | 447 ms                                                 | 441 ms: 1.01x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 63.7 ms: 1.01x faster                                                  |
| regex_dna                  | 220 ms                                                 | 218 ms: 1.01x faster                                                   |
| django_template            | 31.7 ms                                                | 31.3 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.47 sec: 1.01x faster                                                 |
| generators                 | 28.8 ms                                                | 28.5 ms: 1.01x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.7 ms: 1.01x faster                                                  |
| nqueens                    | 80.9 ms                                                | 80.3 ms: 1.01x faster                                                  |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x faster                                                   |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| sqlglot_parse              | 1.26 ms                                                | 1.27 ms: 1.00x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.22 ms: 1.01x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 4.94 ms: 1.01x slower                                                  |
| chaos                      | 58.0 ms                                                | 58.7 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                   |
| fannkuch                   | 394 ms                                                 | 404 ms: 1.03x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 69.3 ms: 1.04x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.32 ms: 1.04x slower                                                  |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 860 us: 1.05x slower                                                   |
| json_loads                 | 27.2 us                                                | 28.6 us: 1.05x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                                   |
| nbody                      | 87.7 ms                                                | 94.3 ms: 1.08x slower                                                  |
| coroutines                 | 22.2 ms                                                | 24.0 ms: 1.08x slower                                                  |
| logging_silent             | 101 ns                                                 | 110 ns: 1.09x slower                                                   |
| mako                       | 10.7 ms                                                | 11.6 ms: 1.09x slower                                                  |
| many_optionals             | 857 us                                                 | 937 us: 1.09x slower                                                   |
| coverage                   | 82.8 ms                                                | 92.0 ms: 1.11x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.9 ms: 1.18x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.1 ms: 1.30x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (5): comprehensions, scimark_sor, docutils, asyncio_websockets, sqlglot_transpile
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.046x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x