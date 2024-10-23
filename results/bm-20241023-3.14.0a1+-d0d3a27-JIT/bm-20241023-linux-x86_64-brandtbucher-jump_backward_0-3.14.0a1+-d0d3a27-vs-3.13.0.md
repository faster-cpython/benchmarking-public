# Results vs. 3.13.0

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: d0d3a27
- commit date: 2024-10-23
- overall geometric mean: 1.08x slower
- HPT reliability: 99.43%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 288 ms: 1.09x slower                                                    |
| docutils       | 2.58 sec                                               | 3.41 sec: 1.32x slower                                                  |
| html5lib       | 64.5 ms                                                | 70.3 ms: 1.09x slower                                                   |
| tornado_http   | 91.5 ms                                                | 112 ms: 1.22x slower                                                    |
| Geometric mean | (ref)                                                  | 1.17x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 408 ms: 1.14x faster                                                    |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                                    |
| async_tree_none_tg         | 320 ms                                                 | 331 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 596 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 584 ms: 1.07x slower                                                    |
| async_generators           | 433 ms                                                 | 468 ms: 1.08x slower                                                    |
| async_tree_io              | 843 ms                                                 | 940 ms: 1.12x slower                                                    |
| async_tree_io_tg           | 825 ms                                                 | 956 ms: 1.16x slower                                                    |
| coroutines                 | 22.5 ms                                                | 26.6 ms: 1.18x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.05x slower                                                            |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 85.7 ms                                                | 81.2 ms: 1.06x faster                                                   |
| float          | 78.5 ms                                                | 75.5 ms: 1.04x faster                                                   |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 220 ms                                                 | 223 ms: 1.01x slower                                                    |
| regex_effbot   | 3.88 ms                                                | 3.94 ms: 1.01x slower                                                   |
| regex_v8       | 25.3 ms                                                | 26.1 ms: 1.03x slower                                                   |
| regex_compile  | 131 ms                                                 | 147 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                  | 1.04x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                  |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                    |
| xml_etree_generate   | 87.0 ms                                                | 82.8 ms: 1.05x faster                                                   |
| xml_etree_iterparse  | 102 ms                                                 | 99.4 ms: 1.03x faster                                                   |
| pickle_pure_python   | 300 us                                                 | 296 us: 1.02x faster                                                    |
| xml_etree_process    | 60.4 ms                                                | 59.8 ms: 1.01x faster                                                   |
| json_loads           | 27.0 us                                                | 26.7 us: 1.01x faster                                                   |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.05x slower                                                   |
| unpickle_pure_python | 213 us                                                 | 226 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.22 ms: 1.03x slower                                                   |
| python_startup         | 10.6 ms                                                | 11.9 ms: 1.13x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.5 ms: 1.06x faster                                                   |
| genshi_text     | 22.9 ms                                                | 26.6 ms: 1.16x slower                                                   |
| django_template | 34.4 ms                                                | 40.5 ms: 1.18x slower                                                   |
| genshi_xml      | 50.3 ms                                                | 62.8 ms: 1.25x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.13x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 276 us: 1.28x faster                                                    |
| deepcopy_memo              | 38.0 us                                                | 30.1 us: 1.26x faster                                                   |
| scimark_fft                | 369 ms                                                 | 319 ms: 1.15x faster                                                    |
| async_tree_memoization_tg  | 465 ms                                                 | 408 ms: 1.14x faster                                                    |
| telco                      | 8.45 ms                                                | 7.64 ms: 1.11x faster                                                   |
| go                         | 142 ms                                                 | 129 ms: 1.10x faster                                                    |
| deepcopy_reduce            | 3.17 us                                                | 2.91 us: 1.09x faster                                                   |
| tomli_loads                | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.66 ms: 1.08x faster                                                   |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                    |
| crypto_pyaes               | 73.0 ms                                                | 68.3 ms: 1.07x faster                                                   |
| scimark_monte_carlo        | 66.3 ms                                                | 62.3 ms: 1.06x faster                                                   |
| mako                       | 11.1 ms                                                | 10.5 ms: 1.06x faster                                                   |
| nbody                      | 85.7 ms                                                | 81.2 ms: 1.06x faster                                                   |
| xml_etree_generate         | 87.0 ms                                                | 82.8 ms: 1.05x faster                                                   |
| bpe_tokeniser              | 4.69 sec                                               | 4.48 sec: 1.05x faster                                                  |
| json                       | 5.20 ms                                                | 4.97 ms: 1.05x faster                                                   |
| pprint_safe_repr           | 744 ms                                                 | 715 ms: 1.04x faster                                                    |
| pathlib                    | 17.1 ms                                                | 16.4 ms: 1.04x faster                                                   |
| float                      | 78.5 ms                                                | 75.5 ms: 1.04x faster                                                   |
| pprint_pformat             | 1.51 sec                                               | 1.46 sec: 1.03x faster                                                  |
| mdp                        | 2.74 sec                                               | 2.65 sec: 1.03x faster                                                  |
| xml_etree_iterparse        | 102 ms                                                 | 99.4 ms: 1.03x faster                                                   |
| scimark_sor                | 122 ms                                                 | 120 ms: 1.02x faster                                                    |
| pickle_pure_python         | 300 us                                                 | 296 us: 1.02x faster                                                    |
| xml_etree_process          | 60.4 ms                                                | 59.8 ms: 1.01x faster                                                   |
| json_loads                 | 27.0 us                                                | 26.7 us: 1.01x faster                                                   |
| fannkuch                   | 381 ms                                                 | 378 ms: 1.01x faster                                                    |
| asyncio_websockets         | 555 ms                                                 | 558 ms: 1.01x slower                                                    |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                    |
| meteor_contest             | 108 ms                                                 | 108 ms: 1.01x slower                                                    |
| regex_dna                  | 220 ms                                                 | 223 ms: 1.01x slower                                                    |
| regex_effbot               | 3.88 ms                                                | 3.94 ms: 1.01x slower                                                   |
| richards_super             | 54.4 ms                                                | 55.2 ms: 1.01x slower                                                   |
| pyflate                    | 460 ms                                                 | 467 ms: 1.02x slower                                                    |
| chaos                      | 58.4 ms                                                | 59.5 ms: 1.02x slower                                                   |
| regex_v8                   | 25.3 ms                                                | 26.1 ms: 1.03x slower                                                   |
| python_startup_no_site     | 6.99 ms                                                | 7.22 ms: 1.03x slower                                                   |
| async_tree_none_tg         | 320 ms                                                 | 331 ms: 1.04x slower                                                    |
| thrift                     | 796 us                                                 | 826 us: 1.04x slower                                                    |
| richards                   | 48.1 ms                                                | 49.9 ms: 1.04x slower                                                   |
| coverage                   | 83.7 ms                                                | 86.9 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 596 ms: 1.04x slower                                                    |
| typing_runtime_protocols   | 159 us                                                 | 167 us: 1.05x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.05x slower                                                   |
| logging_silent             | 102 ns                                                 | 108 ns: 1.05x slower                                                    |
| unpickle_pure_python       | 213 us                                                 | 226 us: 1.06x slower                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 584 ms: 1.07x slower                                                    |
| async_generators           | 433 ms                                                 | 468 ms: 1.08x slower                                                    |
| nqueens                    | 80.6 ms                                                | 87.3 ms: 1.08x slower                                                   |
| 2to3                       | 265 ms                                                 | 288 ms: 1.09x slower                                                    |
| comprehensions             | 16.4 us                                                | 17.8 us: 1.09x slower                                                   |
| html5lib                   | 64.5 ms                                                | 70.3 ms: 1.09x slower                                                   |
| dulwich_log                | 63.0 ms                                                | 68.6 ms: 1.09x slower                                                   |
| async_tree_io              | 843 ms                                                 | 940 ms: 1.12x slower                                                    |
| regex_compile              | 131 ms                                                 | 147 ms: 1.12x slower                                                    |
| pycparser                  | 1.19 sec                                               | 1.34 sec: 1.12x slower                                                  |
| sqlglot_normalize          | 107 ms                                                 | 121 ms: 1.12x slower                                                    |
| raytrace                   | 262 ms                                                 | 295 ms: 1.13x slower                                                    |
| python_startup             | 10.6 ms                                                | 11.9 ms: 1.13x slower                                                   |
| sqlglot_parse              | 1.27 ms                                                | 1.44 ms: 1.14x slower                                                   |
| async_tree_io_tg           | 825 ms                                                 | 956 ms: 1.16x slower                                                    |
| sympy_expand               | 462 ms                                                 | 536 ms: 1.16x slower                                                    |
| genshi_text                | 22.9 ms                                                | 26.6 ms: 1.16x slower                                                   |
| sqlglot_transpile          | 1.57 ms                                                | 1.85 ms: 1.18x slower                                                   |
| django_template            | 34.4 ms                                                | 40.5 ms: 1.18x slower                                                   |
| bench_thread_pool          | 815 us                                                 | 963 us: 1.18x slower                                                    |
| coroutines                 | 22.5 ms                                                | 26.6 ms: 1.18x slower                                                   |
| logging_format             | 6.25 us                                                | 7.43 us: 1.19x slower                                                   |
| logging_simple             | 5.66 us                                                | 6.90 us: 1.22x slower                                                   |
| sympy_str                  | 274 ms                                                 | 333 ms: 1.22x slower                                                    |
| hexiom                     | 6.13 ms                                                | 7.48 ms: 1.22x slower                                                   |
| tornado_http               | 91.5 ms                                                | 112 ms: 1.22x slower                                                    |
| sqlglot_optimize           | 53.9 ms                                                | 67.2 ms: 1.25x slower                                                   |
| genshi_xml                 | 50.3 ms                                                | 62.8 ms: 1.25x slower                                                   |
| generators                 | 28.8 ms                                                | 36.5 ms: 1.27x slower                                                   |
| gc_traversal               | 3.81 ms                                                | 4.85 ms: 1.27x slower                                                   |
| deltablue                  | 3.15 ms                                                | 4.03 ms: 1.28x slower                                                   |
| docutils                   | 2.58 sec                                               | 3.41 sec: 1.32x slower                                                  |
| sympy_integrate            | 19.9 ms                                                | 27.6 ms: 1.39x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 208 ms: 1.39x slower                                                    |
| pylint                     | 313 ms                                                 | 468 ms: 1.50x slower                                                    |
| create_gc_cycles           | 1.61 ms                                                | 2.69 ms: 1.67x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 89.9 ms: 3.75x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.08x slower                                                            |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_none, scimark_lu, spectral_norm
Ignored benchmarks (16) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241023-3.14.0a1+-d0d3a27-JIT/bm-20241023-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a1+-d0d3a27.json: sphinx

# HPT report

- Reliability score: 99.43% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.23x