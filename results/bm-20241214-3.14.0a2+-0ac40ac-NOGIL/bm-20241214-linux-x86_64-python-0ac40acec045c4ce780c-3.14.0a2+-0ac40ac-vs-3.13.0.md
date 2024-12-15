# Results vs. 3.13.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-x86_64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.210x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 353 ms: 1.33x slower                                                   |
| docutils       | 2.58 sec                                               | 3.01 sec: 1.16x slower                                                 |
| html5lib       | 63.4 ms                                                | 89.8 ms: 1.42x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.17 sec: 1.14x slower                                                 |
| Geometric mean | (ref)                                                  | 1.26x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 748 ms: 1.15x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 422 ms: 1.10x faster                                                   |
| async_tree_io              | 838 ms                                                 | 782 ms: 1.07x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 330 ms: 1.03x slower                                                   |
| async_tree_none            | 350 ms                                                 | 368 ms: 1.05x slower                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 574 ms: 1.06x slower                                                   |
| async_tree_memoization     | 437 ms                                                 | 464 ms: 1.06x slower                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 619 ms: 1.08x slower                                                   |
| async_generators           | 433 ms                                                 | 501 ms: 1.16x slower                                                   |
| coroutines                 | 22.2 ms                                                | 26.8 ms: 1.21x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 191 ms: 1.02x slower                                                   |
| nbody          | 87.7 ms                                                | 139 ms: 1.59x slower                                                   |
| float          | 78.7 ms                                                | 129 ms: 1.63x slower                                                   |
| Geometric mean | (ref)                                                  | 1.39x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.51 ms: 1.07x faster                                                  |
| regex_v8       | 26.9 ms                                                | 25.7 ms: 1.04x faster                                                  |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                                   |
| regex_compile  | 132 ms                                                 | 170 ms: 1.29x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 96.5 ms: 1.05x faster                                                  |
| xml_etree_parse      | 154 ms                                                 | 148 ms: 1.04x faster                                                   |
| json_loads           | 27.2 us                                                | 30.1 us: 1.11x slower                                                  |
| xml_etree_generate   | 86.8 ms                                                | 96.9 ms: 1.12x slower                                                  |
| tomli_loads          | 2.12 sec                                               | 2.62 sec: 1.24x slower                                                 |
| xml_etree_process    | 60.5 ms                                                | 75.0 ms: 1.24x slower                                                  |
| json_dumps           | 10.1 ms                                                | 13.4 ms: 1.33x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 316 us: 1.48x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 479 us: 1.58x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.21x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 16.1 ms: 1.27x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 9.81 ms: 1.40x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.33x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 64.3 ms: 1.27x slower                                                  |
| genshi_text     | 22.6 ms                                                | 30.5 ms: 1.35x slower                                                  |
| django_template | 31.7 ms                                                | 47.1 ms: 1.49x slower                                                  |
| mako            | 10.7 ms                                                | 18.0 ms: 1.69x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.44x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 3.65 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 748 ms: 1.15x faster                                                   |
| deepcopy                   | 354 us                                                 | 316 us: 1.12x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 422 ms: 1.10x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.51 ms: 1.07x faster                                                  |
| async_tree_io              | 838 ms                                                 | 782 ms: 1.07x faster                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.31 ms: 1.06x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 96.5 ms: 1.05x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 25.7 ms: 1.04x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 148 ms: 1.04x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.84 us: 1.02x faster                                                  |
| pathlib                    | 17.4 ms                                                | 17.5 ms: 1.01x slower                                                  |
| regex_dna                  | 220 ms                                                 | 224 ms: 1.02x slower                                                   |
| json                       | 5.32 ms                                                | 5.44 ms: 1.02x slower                                                  |
| pidigits                   | 186 ms                                                 | 191 ms: 1.02x slower                                                   |
| async_tree_none_tg         | 319 ms                                                 | 330 ms: 1.03x slower                                                   |
| k_core                     | 2.37 sec                                               | 2.48 sec: 1.05x slower                                                 |
| async_tree_none            | 350 ms                                                 | 368 ms: 1.05x slower                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 574 ms: 1.06x slower                                                   |
| deepcopy_memo              | 38.4 us                                                | 40.6 us: 1.06x slower                                                  |
| async_tree_memoization     | 437 ms                                                 | 464 ms: 1.06x slower                                                   |
| deepcopy_reduce            | 3.24 us                                                | 3.46 us: 1.07x slower                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 619 ms: 1.08x slower                                                   |
| spectral_norm              | 113 ms                                                 | 124 ms: 1.09x slower                                                   |
| telco                      | 8.40 ms                                                | 9.21 ms: 1.10x slower                                                  |
| json_loads                 | 27.2 us                                                | 30.1 us: 1.11x slower                                                  |
| xml_etree_generate         | 86.8 ms                                                | 96.9 ms: 1.12x slower                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 5.26 sec: 1.12x slower                                                 |
| pylint                     | 312 ms                                                 | 353 ms: 1.13x slower                                                   |
| scimark_fft                | 367 ms                                                 | 416 ms: 1.13x slower                                                   |
| sphinx                     | 1.03 sec                                               | 1.17 sec: 1.14x slower                                                 |
| async_generators           | 433 ms                                                 | 501 ms: 1.16x slower                                                   |
| docutils                   | 2.58 sec                                               | 3.01 sec: 1.16x slower                                                 |
| shortest_path              | 487 ms                                                 | 579 ms: 1.19x slower                                                   |
| meteor_contest             | 108 ms                                                 | 130 ms: 1.20x slower                                                   |
| connected_components       | 447 ms                                                 | 535 ms: 1.20x slower                                                   |
| mdp                        | 2.54 sec                                               | 3.05 sec: 1.20x slower                                                 |
| sqlglot_normalize          | 108 ms                                                 | 130 ms: 1.20x slower                                                   |
| pycparser                  | 1.20 sec                                               | 1.45 sec: 1.21x slower                                                 |
| coroutines                 | 22.2 ms                                                | 26.8 ms: 1.21x slower                                                  |
| nqueens                    | 80.9 ms                                                | 98.2 ms: 1.21x slower                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.12 ms: 1.22x slower                                                  |
| sqlglot_optimize           | 53.4 ms                                                | 65.5 ms: 1.23x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 79.5 ms: 1.23x slower                                                  |
| tomli_loads                | 2.12 sec                                               | 2.62 sec: 1.24x slower                                                 |
| xml_etree_process          | 60.5 ms                                                | 75.0 ms: 1.24x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 92.9 ms: 1.24x slower                                                  |
| generators                 | 28.8 ms                                                | 36.2 ms: 1.26x slower                                                  |
| python_startup             | 12.7 ms                                                | 16.1 ms: 1.27x slower                                                  |
| genshi_xml                 | 50.5 ms                                                | 64.3 ms: 1.27x slower                                                  |
| regex_compile              | 132 ms                                                 | 170 ms: 1.29x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 209 us: 1.31x slower                                                   |
| coverage                   | 82.8 ms                                                | 109 ms: 1.31x slower                                                   |
| sympy_integrate            | 19.8 ms                                                | 26.2 ms: 1.32x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 13.4 ms: 1.33x slower                                                  |
| 2to3                       | 266 ms                                                 | 353 ms: 1.33x slower                                                   |
| fannkuch                   | 394 ms                                                 | 524 ms: 1.33x slower                                                   |
| many_optionals             | 857 us                                                 | 1.15 ms: 1.34x slower                                                  |
| genshi_text                | 22.6 ms                                                | 30.5 ms: 1.35x slower                                                  |
| thrift                     | 800 us                                                 | 1.09 ms: 1.36x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 1000 ms: 1.38x slower                                                  |
| sympy_str                  | 273 ms                                                 | 376 ms: 1.38x slower                                                   |
| pyflate                    | 470 ms                                                 | 655 ms: 1.39x slower                                                   |
| pprint_pformat             | 1.48 sec                                               | 2.07 sec: 1.40x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 9.81 ms: 1.40x slower                                                  |
| html5lib                   | 63.4 ms                                                | 89.8 ms: 1.42x slower                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 190 ms: 1.43x slower                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 24.5 ms: 1.45x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 316 us: 1.48x slower                                                   |
| django_template            | 31.7 ms                                                | 47.1 ms: 1.49x slower                                                  |
| richards_super             | 53.7 ms                                                | 80.0 ms: 1.49x slower                                                  |
| sympy_expand               | 456 ms                                                 | 682 ms: 1.49x slower                                                   |
| logging_simple             | 5.65 us                                                | 8.55 us: 1.51x slower                                                  |
| logging_format             | 6.23 us                                                | 9.52 us: 1.53x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 176 ms: 1.53x slower                                                   |
| richards                   | 47.5 ms                                                | 74.0 ms: 1.56x slower                                                  |
| comprehensions             | 16.5 us                                                | 25.7 us: 1.56x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 235 ms: 1.56x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 479 us: 1.58x slower                                                   |
| nbody                      | 87.7 ms                                                | 139 ms: 1.59x slower                                                   |
| hexiom                     | 6.08 ms                                                | 9.82 ms: 1.62x slower                                                  |
| float                      | 78.7 ms                                                | 129 ms: 1.63x slower                                                   |
| mako                       | 10.7 ms                                                | 18.0 ms: 1.69x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 113 ms: 1.69x slower                                                   |
| chaos                      | 58.0 ms                                                | 98.7 ms: 1.70x slower                                                  |
| go                         | 141 ms                                                 | 240 ms: 1.71x slower                                                   |
| sqlglot_transpile          | 1.57 ms                                                | 2.76 ms: 1.75x slower                                                  |
| logging_silent             | 101 ns                                                 | 178 ns: 1.76x slower                                                   |
| subparsers                 | 15.5 ms                                                | 27.7 ms: 1.80x slower                                                  |
| scimark_sor                | 122 ms                                                 | 226 ms: 1.85x slower                                                   |
| sqlglot_parse              | 1.26 ms                                                | 2.39 ms: 1.89x slower                                                  |
| raytrace                   | 262 ms                                                 | 502 ms: 1.92x slower                                                   |
| deltablue                  | 3.19 ms                                                | 7.57 ms: 2.37x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 102 ms: 4.24x slower                                                   |
| bench_thread_pool          | 818 us                                                 | 3.57 ms: 4.37x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.30x slower                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-linux-x86_64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: mypy2

- Geometric mean (including insignificant results): 1.210x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.20x
- 95% likely to have a slowdown of 1.19x
- 99% likely to have a slowdown of 1.16x

# Memory
- memory change: 1.21x