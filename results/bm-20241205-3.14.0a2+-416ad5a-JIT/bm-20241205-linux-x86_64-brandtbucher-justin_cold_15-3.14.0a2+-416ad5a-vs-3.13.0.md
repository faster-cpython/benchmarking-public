# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_cold_15
- machine: linux-x86_64
- commit hash: 416ad5a
- commit date: 2024-12-05
- overall geometric mean: 1.034x faster
- HPT reliability: 98.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                   |
| docutils       | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                 |
| html5lib       | 63.4 ms                                                | 65.3 ms: 1.03x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.05 sec: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 624 ms: 1.34x faster                                                   |
| async_tree_none            | 350 ms                                                 | 274 ms: 1.28x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 345 ms: 1.27x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 500 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                   |
| coroutines                 | 22.2 ms                                                | 22.9 ms: 1.03x slower                                                  |
| async_generators           | 433 ms                                                 | 448 ms: 1.03x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 87.7 ms                                                | 81.4 ms: 1.08x faster                                                  |
| float          | 78.7 ms                                                | 76.0 ms: 1.03x faster                                                  |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.24 ms: 1.16x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                  |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 77.7 ms: 1.12x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 55.0 ms: 1.10x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 1.93 sec: 1.10x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 197 us: 1.08x faster                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 94.9 ms: 1.07x faster                                                  |
| json_loads           | 27.2 us                                                | 26.1 us: 1.04x faster                                                  |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                                   |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.05 ms: 1.01x slower                                                  |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                  |
| django_template | 31.7 ms                                                | 33.2 ms: 1.05x slower                                                  |
| genshi_text     | 22.6 ms                                                | 24.1 ms: 1.07x slower                                                  |
| genshi_xml      | 50.5 ms                                                | 57.5 ms: 1.14x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_15-3.14.0a2+-416ad5a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 316 ms: 1.46x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 618 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 624 ms: 1.34x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 29.4 us: 1.31x faster                                                  |
| deepcopy                   | 354 us                                                 | 272 us: 1.30x faster                                                   |
| async_tree_none            | 350 ms                                                 | 274 ms: 1.28x faster                                                   |
| richards                   | 47.5 ms                                                | 37.5 ms: 1.27x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 345 ms: 1.27x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 255 ms: 1.25x faster                                                   |
| richards_super             | 53.7 ms                                                | 43.4 ms: 1.24x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.70 us: 1.20x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.24 ms: 1.16x faster                                                  |
| scimark_fft                | 367 ms                                                 | 320 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 500 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 481 ms: 1.13x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 77.7 ms: 1.12x faster                                                  |
| telco                      | 8.40 ms                                                | 7.53 ms: 1.12x faster                                                  |
| json                       | 5.32 ms                                                | 4.82 ms: 1.11x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 55.0 ms: 1.10x faster                                                  |
| pylint                     | 312 ms                                                 | 284 ms: 1.10x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.93 sec: 1.10x faster                                                 |
| crypto_pyaes               | 74.7 ms                                                | 68.6 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.64 ms: 1.08x faster                                                  |
| unpickle_pure_python       | 213 us                                                 | 197 us: 1.08x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                  |
| nbody                      | 87.7 ms                                                | 81.4 ms: 1.08x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.36 sec: 1.08x faster                                                 |
| pathlib                    | 17.4 ms                                                | 16.2 ms: 1.07x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 94.9 ms: 1.07x faster                                                  |
| mako                       | 10.7 ms                                                | 10.1 ms: 1.06x faster                                                  |
| go                         | 141 ms                                                 | 134 ms: 1.05x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.78 us: 1.04x faster                                                  |
| json_loads                 | 27.2 us                                                | 26.1 us: 1.04x faster                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 64.3 ms: 1.04x faster                                                  |
| scimark_lu                 | 114 ms                                                 | 110 ms: 1.04x faster                                                   |
| float                      | 78.7 ms                                                | 76.0 ms: 1.03x faster                                                  |
| connected_components       | 447 ms                                                 | 434 ms: 1.03x faster                                                   |
| pyflate                    | 470 ms                                                 | 457 ms: 1.03x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                   |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.02x faster                                                 |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                   |
| thrift                     | 800 us                                                 | 783 us: 1.02x faster                                                   |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.81 ms: 1.02x faster                                                  |
| shortest_path              | 487 ms                                                 | 480 ms: 1.01x faster                                                   |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| fannkuch                   | 394 ms                                                 | 389 ms: 1.01x faster                                                   |
| deltablue                  | 3.19 ms                                                | 3.16 ms: 1.01x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.8 ms: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.46 ms: 1.01x slower                                                  |
| coverage                   | 82.8 ms                                                | 83.3 ms: 1.01x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 7.05 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                  |
| sympy_str                  | 273 ms                                                 | 276 ms: 1.01x slower                                                   |
| pprint_safe_repr           | 727 ms                                                 | 735 ms: 1.01x slower                                                   |
| spectral_norm              | 113 ms                                                 | 115 ms: 1.01x slower                                                   |
| sphinx                     | 1.03 sec                                               | 1.05 sec: 1.01x slower                                                 |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.01x slower                                                   |
| chaos                      | 58.0 ms                                                | 59.2 ms: 1.02x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 154 ms: 1.02x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.66 sec: 1.03x slower                                                 |
| sympy_expand               | 456 ms                                                 | 469 ms: 1.03x slower                                                   |
| coroutines                 | 22.2 ms                                                | 22.9 ms: 1.03x slower                                                  |
| logging_format             | 6.23 us                                                | 6.41 us: 1.03x slower                                                  |
| html5lib                   | 63.4 ms                                                | 65.3 ms: 1.03x slower                                                  |
| logging_silent             | 101 ns                                                 | 104 ns: 1.03x slower                                                   |
| async_generators           | 433 ms                                                 | 448 ms: 1.03x slower                                                   |
| sqlglot_optimize           | 53.4 ms                                                | 55.3 ms: 1.04x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.53 sec: 1.04x slower                                                 |
| sympy_integrate            | 19.8 ms                                                | 20.5 ms: 1.04x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.63 ms: 1.04x slower                                                  |
| logging_simple             | 5.65 us                                                | 5.86 us: 1.04x slower                                                  |
| comprehensions             | 16.5 us                                                | 17.2 us: 1.04x slower                                                  |
| sqlglot_parse              | 1.26 ms                                                | 1.32 ms: 1.05x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 67.6 ms: 1.05x slower                                                  |
| mdp                        | 2.54 sec                                               | 2.67 sec: 1.05x slower                                                 |
| django_template            | 31.7 ms                                                | 33.2 ms: 1.05x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                                   |
| genshi_text                | 22.6 ms                                                | 24.1 ms: 1.07x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 877 us: 1.07x slower                                                   |
| raytrace                   | 262 ms                                                 | 286 ms: 1.09x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                  |
| nqueens                    | 80.9 ms                                                | 90.4 ms: 1.12x slower                                                  |
| many_optionals             | 857 us                                                 | 970 us: 1.13x slower                                                   |
| genshi_xml                 | 50.5 ms                                                | 57.5 ms: 1.14x slower                                                  |
| hexiom                     | 6.08 ms                                                | 7.00 ms: 1.15x slower                                                  |
| generators                 | 28.8 ms                                                | 36.4 ms: 1.27x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.39x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (4): djangocms, pycparser, regex_dna, asyncio_websockets
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 98.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x