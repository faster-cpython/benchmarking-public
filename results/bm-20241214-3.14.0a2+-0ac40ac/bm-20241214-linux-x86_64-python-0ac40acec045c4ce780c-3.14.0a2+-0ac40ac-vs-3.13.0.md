# Results vs. 3.13.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.032x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 257 ms: 1.04x faster                                                   |
| docutils       | 2.58 sec                                               | 2.59 sec: 1.00x slower                                                 |
| html5lib       | 63.4 ms                                                | 64.1 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 627 ms: 1.34x faster                                                   |
| async_tree_none            | 350 ms                                                 | 271 ms: 1.29x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 339 ms: 1.29x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 500 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                                   |
| async_generators           | 433 ms                                                 | 417 ms: 1.04x faster                                                   |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 77.5 ms: 1.02x faster                                                  |
| nbody          | 87.7 ms                                                | 95.5 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                  |
| regex_v8       | 26.9 ms                                                | 25.0 ms: 1.07x faster                                                  |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 97.3 ms: 1.04x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 2.04 sec: 1.04x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 324 us: 1.07x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (2): xml_etree_generate, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.09 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 22.2 ms: 1.02x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                  |
| django_template | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                  |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 619 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 627 ms: 1.34x faster                                                   |
| deepcopy                   | 354 us                                                 | 268 us: 1.32x faster                                                   |
| async_tree_none            | 350 ms                                                 | 271 ms: 1.29x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 339 ms: 1.29x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 31.0 us: 1.24x faster                                                  |
| go                         | 141 ms                                                 | 120 ms: 1.17x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.81 us: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 500 ms: 1.15x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                  |
| pylint                     | 312 ms                                                 | 277 ms: 1.13x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 25.0 ms: 1.07x faster                                                  |
| telco                      | 8.40 ms                                                | 7.85 ms: 1.07x faster                                                  |
| scimark_fft                | 367 ms                                                 | 347 ms: 1.06x faster                                                   |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.06x faster                                                  |
| json                       | 5.32 ms                                                | 5.05 ms: 1.05x faster                                                  |
| thrift                     | 800 us                                                 | 761 us: 1.05x faster                                                   |
| spectral_norm              | 113 ms                                                 | 108 ms: 1.05x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.04x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 97.3 ms: 1.04x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 2.04 sec: 1.04x faster                                                 |
| async_generators           | 433 ms                                                 | 417 ms: 1.04x faster                                                   |
| richards                   | 47.5 ms                                                | 45.8 ms: 1.04x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                 |
| 2to3                       | 266 ms                                                 | 257 ms: 1.04x faster                                                   |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                   |
| sqlglot_normalize          | 108 ms                                                 | 104 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.87 ms: 1.03x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.54 sec: 1.03x faster                                                 |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 72.8 ms: 1.03x faster                                                  |
| richards_super             | 53.7 ms                                                | 52.4 ms: 1.03x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.83 us: 1.03x faster                                                  |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| djangocms                  | 22.3 us                                                | 21.8 us: 1.02x faster                                                  |
| logging_format             | 6.23 us                                                | 6.11 us: 1.02x faster                                                  |
| generators                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                 |
| genshi_text                | 22.6 ms                                                | 22.2 ms: 1.02x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.56 us: 1.02x faster                                                  |
| float                      | 78.7 ms                                                | 77.5 ms: 1.02x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 49.8 ms: 1.01x faster                                                  |
| shortest_path              | 487 ms                                                 | 480 ms: 1.01x faster                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 52.8 ms: 1.01x faster                                                  |
| sympy_str                  | 273 ms                                                 | 270 ms: 1.01x faster                                                   |
| nqueens                    | 80.9 ms                                                | 80.0 ms: 1.01x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 59.9 ms: 1.01x faster                                                  |
| pyflate                    | 470 ms                                                 | 467 ms: 1.01x faster                                                   |
| docutils                   | 2.58 sec                                               | 2.59 sec: 1.00x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                   |
| coverage                   | 82.8 ms                                                | 83.2 ms: 1.00x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                  |
| gc_traversal               | 4.90 ms                                                | 4.94 ms: 1.01x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 734 ms: 1.01x slower                                                   |
| html5lib                   | 63.4 ms                                                | 64.1 ms: 1.01x slower                                                  |
| django_template            | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.01x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 162 us: 1.01x slower                                                   |
| python_startup_no_site     | 7.00 ms                                                | 7.09 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.25 ms: 1.02x slower                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.29 ms: 1.02x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                  |
| fannkuch                   | 394 ms                                                 | 401 ms: 1.02x slower                                                   |
| scimark_monte_carlo        | 66.8 ms                                                | 68.1 ms: 1.02x slower                                                  |
| scimark_sor                | 122 ms                                                 | 125 ms: 1.02x slower                                                   |
| hexiom                     | 6.08 ms                                                | 6.23 ms: 1.02x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 1.52 sec: 1.03x slower                                                 |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 118 ms: 1.03x slower                                                   |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.2 ms: 1.04x slower                                                  |
| logging_silent             | 101 ns                                                 | 106 ns: 1.05x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 862 us: 1.05x slower                                                   |
| chaos                      | 58.0 ms                                                | 61.4 ms: 1.06x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 324 us: 1.07x slower                                                   |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                  |
| nbody                      | 87.7 ms                                                | 95.5 ms: 1.09x slower                                                  |
| many_optionals             | 857 us                                                 | 956 us: 1.12x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.5 ms: 3.40x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (9): sphinx, connected_components, xml_etree_generate, json_loads, pidigits, mdp, sympy_expand, dulwich_log, regex_dna
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: mypy2

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 99.89% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x