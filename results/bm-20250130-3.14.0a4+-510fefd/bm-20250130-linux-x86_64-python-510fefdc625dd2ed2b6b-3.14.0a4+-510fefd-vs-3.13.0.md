# Results vs. 3.13.0

- fork: python
- ref: 510fefdc625dd2ed2b6b
- machine: linux-x86_64
- commit hash: 510fefd
- commit date: 2025-01-30
- overall geometric mean: 1.052x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 251 ms: 1.06x faster                                                   |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                 |
| html5lib       | 63.4 ms                                                | 61.1 ms: 1.04x faster                                                  |
| sphinx         | 1.03 sec                                               | 995 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 605 ms: 1.42x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                                   |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                   |
| async_generators           | 433 ms                                                 | 385 ms: 1.13x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.1 ms: 1.12x faster                                                  |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| nbody          | 87.7 ms                                                | 91.6 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.21 ms: 1.17x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.8 ms: 1.08x faster                                                  |
| regex_compile  | 132 ms                                                 | 125 ms: 1.05x faster                                                   |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 83.6 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 98.3 ms: 1.03x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 59.2 ms: 1.02x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                   |
| json_loads           | 27.2 us                                                | 28.5 us: 1.05x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.8 ms: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.00 ms: 1.00x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.7 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 47.9 ms: 1.05x faster                                                  |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                  |
| mako            | 10.7 ms                                                | 11.3 ms: 1.05x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 313 ms: 1.48x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 605 ms: 1.42x faster                                                   |
| deepcopy                   | 354 us                                                 | 257 us: 1.38x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 322 ms: 1.36x faster                                                   |
| async_tree_io              | 838 ms                                                 | 619 ms: 1.35x faster                                                   |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 30.2 us: 1.27x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.68 us: 1.21x faster                                                  |
| go                         | 141 ms                                                 | 117 ms: 1.21x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.21 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 494 ms: 1.16x faster                                                   |
| spectral_norm              | 113 ms                                                 | 98.0 ms: 1.16x faster                                                  |
| pylint                     | 312 ms                                                 | 272 ms: 1.15x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.41 ms: 1.14x faster                                                  |
| async_generators           | 433 ms                                                 | 385 ms: 1.13x faster                                                   |
| float                      | 78.7 ms                                                | 70.1 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                                   |
| pathlib                    | 17.4 ms                                                | 15.7 ms: 1.11x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                   |
| scimark_fft                | 367 ms                                                 | 337 ms: 1.09x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 24.8 ms: 1.08x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.96 sec: 1.08x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.39 sec: 1.07x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.07x faster                                                 |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                  |
| telco                      | 8.40 ms                                                | 7.89 ms: 1.06x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.61 ms: 1.06x faster                                                  |
| 2to3                       | 266 ms                                                 | 251 ms: 1.06x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 70.8 ms: 1.05x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 47.9 ms: 1.05x faster                                                  |
| richards                   | 47.5 ms                                                | 45.1 ms: 1.05x faster                                                  |
| thrift                     | 800 us                                                 | 760 us: 1.05x faster                                                   |
| regex_compile              | 132 ms                                                 | 125 ms: 1.05x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                                  |
| sqlglot_normalize          | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| json                       | 5.32 ms                                                | 5.09 ms: 1.05x faster                                                  |
| richards_super             | 53.7 ms                                                | 51.5 ms: 1.04x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                 |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 145 ms: 1.04x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 83.6 ms: 1.04x faster                                                  |
| html5lib                   | 63.4 ms                                                | 61.1 ms: 1.04x faster                                                  |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                                   |
| sphinx                     | 1.03 sec                                               | 995 ms: 1.04x faster                                                   |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                  |
| mdp                        | 2.54 sec                                               | 2.47 sec: 1.03x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 98.3 ms: 1.03x faster                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 51.9 ms: 1.03x faster                                                  |
| shortest_path              | 487 ms                                                 | 473 ms: 1.03x faster                                                   |
| logging_simple             | 5.65 us                                                | 5.50 us: 1.03x faster                                                  |
| connected_components       | 447 ms                                                 | 435 ms: 1.03x faster                                                   |
| logging_format             | 6.23 us                                                | 6.07 us: 1.03x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 59.2 ms: 1.02x faster                                                  |
| generators                 | 28.8 ms                                                | 28.3 ms: 1.02x faster                                                  |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                   |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                                  |
| typing_runtime_protocols   | 160 us                                                 | 158 us: 1.01x faster                                                   |
| sympy_expand               | 456 ms                                                 | 450 ms: 1.01x faster                                                   |
| pyflate                    | 470 ms                                                 | 464 ms: 1.01x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                                  |
| pprint_safe_repr           | 727 ms                                                 | 721 ms: 1.01x faster                                                   |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.56 ms: 1.00x faster                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.26 ms: 1.00x faster                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.44 ms: 1.00x faster                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.00 ms: 1.00x slower                                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| python_startup             | 12.7 ms                                                | 12.7 ms: 1.01x slower                                                  |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.13 ms: 1.01x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 67.4 ms: 1.01x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.23 ms: 1.01x slower                                                  |
| nqueens                    | 80.9 ms                                                | 82.0 ms: 1.01x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                   |
| fannkuch                   | 394 ms                                                 | 405 ms: 1.03x slower                                                   |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.0 ms: 1.04x slower                                                  |
| nbody                      | 87.7 ms                                                | 91.6 ms: 1.04x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 857 us: 1.05x slower                                                   |
| json_loads                 | 27.2 us                                                | 28.5 us: 1.05x slower                                                  |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.05x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                                   |
| logging_silent             | 101 ns                                                 | 108 ns: 1.07x slower                                                   |
| many_optionals             | 857 us                                                 | 927 us: 1.08x slower                                                   |
| coverage                   | 82.8 ms                                                | 90.2 ms: 1.09x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.8 ms: 1.16x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.3 ms: 1.31x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 80.5 ms: 3.36x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (4): dulwich_log, chaos, pprint_pformat, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x