# Results vs. 3.13.0

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: 0474adc
- commit date: 2025-02-03
- overall geometric mean: 1.051x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 252 ms: 1.06x faster                                                       |
| docutils       | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                     |
| html5lib       | 63.4 ms                                                | 61.2 ms: 1.03x faster                                                      |
| sphinx         | 1.03 sec                                               | 999 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 320 ms: 1.45x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                       |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 321 ms: 1.36x faster                                                       |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                       |
| async_generators           | 433 ms                                                 | 382 ms: 1.13x faster                                                       |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 70.1 ms: 1.12x faster                                                      |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                       |
| nbody          | 87.7 ms                                                | 93.7 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.27 ms: 1.15x faster                                                      |
| regex_v8       | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                      |
| regex_compile  | 132 ms                                                 | 125 ms: 1.06x faster                                                       |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                       |
| tomli_loads          | 2.12 sec                                               | 1.92 sec: 1.10x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 97.1 ms: 1.04x faster                                                      |
| xml_etree_generate   | 86.8 ms                                                | 83.5 ms: 1.04x faster                                                      |
| xml_etree_process    | 60.5 ms                                                | 58.7 ms: 1.03x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                       |
| pickle_pure_python   | 302 us                                                 | 318 us: 1.05x slower                                                       |
| json_loads           | 27.2 us                                                | 28.9 us: 1.06x slower                                                      |
| json_dumps           | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                      |
| python_startup         | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                      |
| genshi_xml      | 50.5 ms                                                | 48.6 ms: 1.04x faster                                                      |
| django_template | 31.7 ms                                                | 31.8 ms: 1.01x slower                                                      |
| mako            | 10.7 ms                                                | 10.9 ms: 1.02x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250203-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-0474adc |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 320 ms: 1.45x faster                                                       |
| deepcopy                   | 354 us                                                 | 253 us: 1.40x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                       |
| async_tree_io              | 838 ms                                                 | 616 ms: 1.36x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 321 ms: 1.36x faster                                                       |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                       |
| deepcopy_memo              | 38.4 us                                                | 30.1 us: 1.28x faster                                                      |
| async_tree_none_tg         | 319 ms                                                 | 254 ms: 1.26x faster                                                       |
| deepcopy_reduce            | 3.24 us                                                | 2.68 us: 1.21x faster                                                      |
| spectral_norm              | 113 ms                                                 | 94.6 ms: 1.20x faster                                                      |
| go                         | 141 ms                                                 | 118 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 487 ms: 1.18x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.27 ms: 1.15x faster                                                      |
| pylint                     | 312 ms                                                 | 271 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 478 ms: 1.14x faster                                                       |
| async_generators           | 433 ms                                                 | 382 ms: 1.13x faster                                                       |
| float                      | 78.7 ms                                                | 70.1 ms: 1.12x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                       |
| pathlib                    | 17.4 ms                                                | 15.7 ms: 1.10x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 1.92 sec: 1.10x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.59 ms: 1.10x faster                                                      |
| scimark_fft                | 367 ms                                                 | 340 ms: 1.08x faster                                                       |
| regex_v8                   | 26.9 ms                                                | 24.9 ms: 1.08x faster                                                      |
| richards                   | 47.5 ms                                                | 44.4 ms: 1.07x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.38 sec: 1.07x faster                                                     |
| telco                      | 8.40 ms                                                | 7.86 ms: 1.07x faster                                                      |
| crypto_pyaes               | 74.7 ms                                                | 70.0 ms: 1.07x faster                                                      |
| richards_super             | 53.7 ms                                                | 50.6 ms: 1.06x faster                                                      |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                      |
| k_core                     | 2.37 sec                                               | 2.24 sec: 1.06x faster                                                     |
| 2to3                       | 266 ms                                                 | 252 ms: 1.06x faster                                                       |
| regex_compile              | 132 ms                                                 | 125 ms: 1.06x faster                                                       |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                                       |
| sqlite_synth               | 2.90 us                                                | 2.76 us: 1.05x faster                                                      |
| sqlglot_normalize          | 108 ms                                                 | 103 ms: 1.05x faster                                                       |
| thrift                     | 800 us                                                 | 762 us: 1.05x faster                                                       |
| xml_etree_iterparse        | 101 ms                                                 | 97.1 ms: 1.04x faster                                                      |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                       |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.04x faster                                                     |
| xml_etree_generate         | 86.8 ms                                                | 83.5 ms: 1.04x faster                                                      |
| genshi_xml                 | 50.5 ms                                                | 48.6 ms: 1.04x faster                                                      |
| mdp                        | 2.54 sec                                               | 2.45 sec: 1.04x faster                                                     |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.3 ms: 1.04x faster                                                      |
| html5lib                   | 63.4 ms                                                | 61.2 ms: 1.03x faster                                                      |
| json                       | 5.32 ms                                                | 5.15 ms: 1.03x faster                                                      |
| shortest_path              | 487 ms                                                 | 471 ms: 1.03x faster                                                       |
| sqlglot_optimize           | 53.4 ms                                                | 51.7 ms: 1.03x faster                                                      |
| sphinx                     | 1.03 sec                                               | 999 ms: 1.03x faster                                                       |
| logging_simple             | 5.65 us                                                | 5.47 us: 1.03x faster                                                      |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                       |
| generators                 | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                      |
| sympy_str                  | 273 ms                                                 | 265 ms: 1.03x faster                                                       |
| xml_etree_process          | 60.5 ms                                                | 58.7 ms: 1.03x faster                                                      |
| connected_components       | 447 ms                                                 | 435 ms: 1.03x faster                                                       |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                       |
| logging_format             | 6.23 us                                                | 6.10 us: 1.02x faster                                                      |
| sympy_expand               | 456 ms                                                 | 449 ms: 1.02x faster                                                       |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                                      |
| nqueens                    | 80.9 ms                                                | 79.9 ms: 1.01x faster                                                      |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                                      |
| typing_runtime_protocols   | 160 us                                                 | 158 us: 1.01x faster                                                       |
| pprint_safe_repr           | 727 ms                                                 | 719 ms: 1.01x faster                                                       |
| dulwich_log                | 64.6 ms                                                | 64.1 ms: 1.01x faster                                                      |
| pyflate                    | 470 ms                                                 | 467 ms: 1.01x faster                                                       |
| docutils                   | 2.58 sec                                               | 2.57 sec: 1.01x faster                                                     |
| scimark_sor                | 122 ms                                                 | 122 ms: 1.00x faster                                                       |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                       |
| chaos                      | 58.0 ms                                                | 58.3 ms: 1.00x slower                                                      |
| django_template            | 31.7 ms                                                | 31.8 ms: 1.01x slower                                                      |
| scimark_lu                 | 114 ms                                                 | 115 ms: 1.01x slower                                                       |
| python_startup_no_site     | 7.00 ms                                                | 7.06 ms: 1.01x slower                                                      |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                       |
| python_startup             | 12.7 ms                                                | 12.9 ms: 1.02x slower                                                      |
| scimark_monte_carlo        | 66.8 ms                                                | 68.3 ms: 1.02x slower                                                      |
| mako                       | 10.7 ms                                                | 10.9 ms: 1.02x slower                                                      |
| hexiom                     | 6.08 ms                                                | 6.24 ms: 1.03x slower                                                      |
| deltablue                  | 3.19 ms                                                | 3.28 ms: 1.03x slower                                                      |
| gc_traversal               | 4.90 ms                                                | 5.03 ms: 1.03x slower                                                      |
| fannkuch                   | 394 ms                                                 | 408 ms: 1.04x slower                                                       |
| raytrace                   | 262 ms                                                 | 272 ms: 1.04x slower                                                       |
| bench_thread_pool          | 818 us                                                 | 860 us: 1.05x slower                                                       |
| pickle_pure_python         | 302 us                                                 | 318 us: 1.05x slower                                                       |
| logging_silent             | 101 ns                                                 | 107 ns: 1.06x slower                                                       |
| coroutines                 | 22.2 ms                                                | 23.6 ms: 1.06x slower                                                      |
| json_loads                 | 27.2 us                                                | 28.9 us: 1.06x slower                                                      |
| nbody                      | 87.7 ms                                                | 93.7 ms: 1.07x slower                                                      |
| coverage                   | 82.8 ms                                                | 89.9 ms: 1.09x slower                                                      |
| many_optionals             | 857 us                                                 | 932 us: 1.09x slower                                                       |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.14x slower                                                      |
| subparsers                 | 15.5 ms                                                | 20.4 ms: 1.32x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 81.0 ms: 3.38x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (4): sqlglot_parse, sqlglot_transpile, asyncio_websockets, pprint_pformat
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.051x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x