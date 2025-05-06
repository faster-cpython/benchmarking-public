# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_recursive
- machine: linux-x86_64
- commit hash: fe02176
- commit date: 2025-05-05
- overall geometric mean: 1.047x faster
- HPT reliability: 97.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 261 ms: 1.02x faster                                                  |
| docutils       | 2.58 sec                                               | 2.65 sec: 1.03x slower                                                |
| html5lib       | 63.4 ms                                                | 61.1 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                                  |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                  |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 501 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 496 ms: 1.10x faster                                                  |
| async_generators           | 433 ms                                                 | 423 ms: 1.02x faster                                                  |
| coroutines                 | 22.2 ms                                                | 24.6 ms: 1.11x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.8 ms: 1.21x faster                                                 |
| pidigits       | 186 ms                                                 | 191 ms: 1.03x slower                                                  |
| nbody          | 87.7 ms                                                | 95.6 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 2.95 ms: 1.28x faster                                                 |
| regex_v8       | 26.9 ms                                                | 22.4 ms: 1.20x faster                                                 |
| regex_dna      | 220 ms                                                 | 196 ms: 1.12x faster                                                  |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 1.88 sec: 1.13x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 142 ms: 1.08x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 56.2 ms: 1.08x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 81.2 ms: 1.07x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 208 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 99.3 ms: 1.02x faster                                                 |
| pickle_pure_python   | 302 us                                                 | 323 us: 1.07x slower                                                  |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                 |
| json_dumps           | 10.1 ms                                                | 11.9 ms: 1.17x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 6.92 ms: 1.01x faster                                                 |
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.9 ms: 1.03x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 49.4 ms: 1.02x faster                                                 |
| django_template | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                 |
| mako            | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.23 sec: 2.07x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 314 ms: 1.47x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 612 ms: 1.41x faster                                                  |
| async_tree_io              | 838 ms                                                 | 597 ms: 1.40x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 312 ms: 1.40x faster                                                  |
| deepcopy                   | 354 us                                                 | 258 us: 1.38x faster                                                  |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                  |
| richards                   | 47.5 ms                                                | 35.4 ms: 1.34x faster                                                 |
| richards_super             | 53.7 ms                                                | 40.5 ms: 1.33x faster                                                 |
| deepcopy_memo              | 38.4 us                                                | 29.8 us: 1.29x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 2.95 ms: 1.28x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                  |
| float                      | 78.7 ms                                                | 64.8 ms: 1.21x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 22.4 ms: 1.20x faster                                                 |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                                 |
| go                         | 141 ms                                                 | 121 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 501 ms: 1.14x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 1.88 sec: 1.13x faster                                                |
| regex_dna                  | 220 ms                                                 | 196 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 496 ms: 1.10x faster                                                  |
| pylint                     | 312 ms                                                 | 285 ms: 1.09x faster                                                  |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.09x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 142 ms: 1.08x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.35 sec: 1.08x faster                                                |
| xml_etree_process          | 60.5 ms                                                | 56.2 ms: 1.08x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 81.2 ms: 1.07x faster                                                 |
| pyflate                    | 470 ms                                                 | 440 ms: 1.07x faster                                                  |
| telco                      | 8.40 ms                                                | 7.88 ms: 1.07x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.07x faster                                                |
| dulwich_log                | 64.6 ms                                                | 60.8 ms: 1.06x faster                                                 |
| deltablue                  | 3.19 ms                                                | 3.05 ms: 1.05x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.79 us: 1.04x faster                                                 |
| html5lib                   | 63.4 ms                                                | 61.1 ms: 1.04x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.9 ms: 1.03x faster                                                 |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                  |
| async_generators           | 433 ms                                                 | 423 ms: 1.02x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                 |
| unpickle_pure_python       | 213 us                                                 | 208 us: 1.02x faster                                                  |
| genshi_xml                 | 50.5 ms                                                | 49.4 ms: 1.02x faster                                                 |
| pathlib                    | 17.4 ms                                                | 17.0 ms: 1.02x faster                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 99.3 ms: 1.02x faster                                                 |
| 2to3                       | 266 ms                                                 | 261 ms: 1.02x faster                                                  |
| python_startup_no_site     | 7.00 ms                                                | 6.92 ms: 1.01x faster                                                 |
| sympy_str                  | 273 ms                                                 | 270 ms: 1.01x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.69 us: 1.01x slower                                                 |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 76.2 ms: 1.02x slower                                                 |
| logging_format             | 6.23 us                                                | 6.36 us: 1.02x slower                                                 |
| pidigits                   | 186 ms                                                 | 191 ms: 1.03x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.65 sec: 1.03x slower                                                |
| django_template            | 31.7 ms                                                | 32.6 ms: 1.03x slower                                                 |
| sympy_expand               | 456 ms                                                 | 471 ms: 1.03x slower                                                  |
| nqueens                    | 80.9 ms                                                | 83.6 ms: 1.03x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.53 sec: 1.03x slower                                                |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                 |
| gc_traversal               | 4.90 ms                                                | 5.08 ms: 1.04x slower                                                 |
| fannkuch                   | 394 ms                                                 | 410 ms: 1.04x slower                                                  |
| mako                       | 10.7 ms                                                | 11.2 ms: 1.05x slower                                                 |
| typing_runtime_protocols   | 160 us                                                 | 168 us: 1.05x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.58 ms: 1.05x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 122 ms: 1.06x slower                                                  |
| chaos                      | 58.0 ms                                                | 61.9 ms: 1.07x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 323 us: 1.07x slower                                                  |
| raytrace                   | 262 ms                                                 | 281 ms: 1.08x slower                                                  |
| comprehensions             | 16.5 us                                                | 17.8 us: 1.08x slower                                                 |
| generators                 | 28.8 ms                                                | 31.3 ms: 1.09x slower                                                 |
| nbody                      | 87.7 ms                                                | 95.6 ms: 1.09x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.65 ms: 1.09x slower                                                 |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 903 us: 1.10x slower                                                  |
| coroutines                 | 22.2 ms                                                | 24.6 ms: 1.11x slower                                                 |
| scimark_fft                | 367 ms                                                 | 409 ms: 1.11x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 75.5 ms: 1.13x slower                                                 |
| many_optionals             | 857 us                                                 | 976 us: 1.14x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.9 ms: 1.17x slower                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.06 ms: 1.20x slower                                                 |
| subparsers                 | 15.5 ms                                                | 23.1 ms: 1.50x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 92.3 ms: 3.85x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (7): json, shortest_path, asyncio_websockets, scimark_sor, connected_components, pprint_safe_repr, logging_silent
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, coverage, djangocms, gevent_hub, gunicorn, sphinx, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (10) of results/bm-20250505-3.14.0a7+-fe02176-JIT/bm-20250505-linux-x86_64-brandtbucher-jit_recursive-3.14.0a7+-fe02176.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.047x faster

# HPT report

- Reliability score: 97.76% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x