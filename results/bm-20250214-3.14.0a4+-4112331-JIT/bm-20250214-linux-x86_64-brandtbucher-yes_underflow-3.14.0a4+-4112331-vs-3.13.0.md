# Results vs. 3.13.0

- fork: brandtbucher
- ref: yes_underflow
- machine: linux-x86_64
- commit hash: 4112331
- commit date: 2025-02-14
- overall geometric mean: 1.010x faster
- HPT reliability: 60.59%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 260 ms: 1.02x faster                                                  |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                |
| html5lib       | 63.4 ms                                                | 69.0 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 609 ms: 1.41x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 329 ms: 1.33x faster                                                  |
| async_tree_io              | 838 ms                                                 | 633 ms: 1.32x faster                                                  |
| async_tree_none            | 350 ms                                                 | 271 ms: 1.29x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                  |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                  |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 66.0 ms: 1.19x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| nbody          | 87.7 ms                                                | 89.3 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.05 ms: 1.23x faster                                                 |
| regex_v8       | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                 |
| regex_dna      | 220 ms                                                 | 202 ms: 1.09x faster                                                  |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 138 ms: 1.12x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 78.8 ms: 1.10x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 55.7 ms: 1.09x faster                                                 |
| tomli_loads          | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                |
| unpickle_pure_python | 213 us                                                 | 202 us: 1.06x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 96.1 ms: 1.05x faster                                                 |
| pickle_pure_python   | 302 us                                                 | 317 us: 1.05x slower                                                  |
| json_loads           | 27.2 us                                                | 28.9 us: 1.07x slower                                                 |
| json_dumps           | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                 |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 9.95 ms: 1.07x faster                                                 |
| genshi_text     | 22.6 ms                                                | 23.0 ms: 1.02x slower                                                 |
| django_template | 31.7 ms                                                | 35.7 ms: 1.13x slower                                                 |
| genshi_xml      | 50.5 ms                                                | 66.7 ms: 1.32x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.09x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250214-linux-x86_64-brandtbucher-yes_underflow-3.14.0a4+-4112331 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 609 ms: 1.41x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 329 ms: 1.33x faster                                                  |
| async_tree_io              | 838 ms                                                 | 633 ms: 1.32x faster                                                  |
| deepcopy                   | 354 us                                                 | 274 us: 1.29x faster                                                  |
| async_tree_none            | 350 ms                                                 | 271 ms: 1.29x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.8 us: 1.29x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.05 ms: 1.23x faster                                                 |
| spectral_norm              | 113 ms                                                 | 93.0 ms: 1.22x faster                                                 |
| float                      | 78.7 ms                                                | 66.0 ms: 1.19x faster                                                 |
| scimark_fft                | 367 ms                                                 | 312 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 492 ms: 1.17x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.79 us: 1.16x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 479 ms: 1.13x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.45 ms: 1.13x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 138 ms: 1.12x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 78.8 ms: 1.10x faster                                                 |
| pathlib                    | 17.4 ms                                                | 15.8 ms: 1.10x faster                                                 |
| telco                      | 8.40 ms                                                | 7.67 ms: 1.09x faster                                                 |
| pylint                     | 312 ms                                                 | 286 ms: 1.09x faster                                                  |
| regex_dna                  | 220 ms                                                 | 202 ms: 1.09x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 55.7 ms: 1.09x faster                                                 |
| mako                       | 10.7 ms                                                | 9.95 ms: 1.07x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.38 sec: 1.07x faster                                                |
| tomli_loads                | 2.12 sec                                               | 1.98 sec: 1.07x faster                                                |
| sqlite_synth               | 2.90 us                                                | 2.73 us: 1.06x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 202 us: 1.06x faster                                                  |
| crypto_pyaes               | 74.7 ms                                                | 70.8 ms: 1.05x faster                                                 |
| gc_traversal               | 4.90 ms                                                | 4.65 ms: 1.05x faster                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 63.4 ms: 1.05x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 96.1 ms: 1.05x faster                                                 |
| async_generators           | 433 ms                                                 | 412 ms: 1.05x faster                                                  |
| thrift                     | 800 us                                                 | 767 us: 1.04x faster                                                  |
| k_core                     | 2.37 sec                                               | 2.31 sec: 1.02x faster                                                |
| 2to3                       | 266 ms                                                 | 260 ms: 1.02x faster                                                  |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.02x faster                                                  |
| json                       | 5.32 ms                                                | 5.22 ms: 1.02x faster                                                 |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                  |
| connected_components       | 447 ms                                                 | 441 ms: 1.01x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.01x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.7 ms: 1.01x faster                                                 |
| shortest_path              | 487 ms                                                 | 482 ms: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                 |
| mdp                        | 2.54 sec                                               | 2.57 sec: 1.01x slower                                                |
| fannkuch                   | 394 ms                                                 | 397 ms: 1.01x slower                                                  |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                 |
| genshi_text                | 22.6 ms                                                | 23.0 ms: 1.02x slower                                                 |
| nbody                      | 87.7 ms                                                | 89.3 ms: 1.02x slower                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                                  |
| pycparser                  | 1.20 sec                                               | 1.23 sec: 1.02x slower                                                |
| sqlglot_optimize           | 53.4 ms                                                | 54.7 ms: 1.03x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                  |
| sympy_str                  | 273 ms                                                 | 281 ms: 1.03x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                |
| sqlglot_parse              | 1.26 ms                                                | 1.31 ms: 1.03x slower                                                 |
| sympy_integrate            | 19.8 ms                                                | 20.5 ms: 1.03x slower                                                 |
| sympy_expand               | 456 ms                                                 | 472 ms: 1.03x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 120 ms: 1.05x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 317 us: 1.05x slower                                                  |
| comprehensions             | 16.5 us                                                | 17.4 us: 1.05x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 770 ms: 1.06x slower                                                  |
| chaos                      | 58.0 ms                                                | 61.5 ms: 1.06x slower                                                 |
| sqlglot_normalize          | 108 ms                                                 | 115 ms: 1.06x slower                                                  |
| json_loads                 | 27.2 us                                                | 28.9 us: 1.07x slower                                                 |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.59 sec: 1.07x slower                                                |
| nqueens                    | 80.9 ms                                                | 87.9 ms: 1.09x slower                                                 |
| html5lib                   | 63.4 ms                                                | 69.0 ms: 1.09x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 890 us: 1.09x slower                                                  |
| coverage                   | 82.8 ms                                                | 90.3 ms: 1.09x slower                                                 |
| dulwich_log                | 64.6 ms                                                | 70.5 ms: 1.09x slower                                                 |
| logging_format             | 6.23 us                                                | 6.83 us: 1.10x slower                                                 |
| raytrace                   | 262 ms                                                 | 289 ms: 1.11x slower                                                  |
| logging_simple             | 5.65 us                                                | 6.27 us: 1.11x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.3 ms: 1.12x slower                                                 |
| many_optionals             | 857 us                                                 | 964 us: 1.13x slower                                                  |
| django_template            | 31.7 ms                                                | 35.7 ms: 1.13x slower                                                 |
| hexiom                     | 6.08 ms                                                | 7.68 ms: 1.26x slower                                                 |
| deltablue                  | 3.19 ms                                                | 4.22 ms: 1.32x slower                                                 |
| genshi_xml                 | 50.5 ms                                                | 66.7 ms: 1.32x slower                                                 |
| logging_silent             | 101 ns                                                 | 134 ns: 1.32x slower                                                  |
| richards                   | 47.5 ms                                                | 64.2 ms: 1.35x slower                                                 |
| subparsers                 | 15.5 ms                                                | 21.1 ms: 1.37x slower                                                 |
| richards_super             | 53.7 ms                                                | 75.9 ms: 1.41x slower                                                 |
| generators                 | 28.8 ms                                                | 49.5 ms: 1.72x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 81.0 ms: 3.38x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (5): meteor_contest, asyncio_websockets, pyflate, go, sphinx
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 60.59% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x