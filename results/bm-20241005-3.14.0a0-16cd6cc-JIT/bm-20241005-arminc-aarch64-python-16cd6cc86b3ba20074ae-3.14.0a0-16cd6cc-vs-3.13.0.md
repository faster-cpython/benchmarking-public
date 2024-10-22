# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-aarch64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 383 ms: 1.25x slower                                                    |
| docutils       | 2.91 sec                                                 | 3.71 sec: 1.28x slower                                                  |
| html5lib       | 64.3 ms                                                  | 71.0 ms: 1.10x slower                                                   |
| tornado_http   | 131 ms                                                   | 147 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                    | 1.19x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 561 ms: 1.16x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 420 ms: 1.11x faster                                                    |
| async_tree_none           | 493 ms                                                   | 445 ms: 1.11x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 591 ms: 1.06x faster                                                    |
| asyncio_websockets        | 656 ms                                                   | 664 ms: 1.01x slower                                                    |
| async_generators          | 496 ms                                                   | 508 ms: 1.02x slower                                                    |
| coroutines                | 28.2 ms                                                  | 29.0 ms: 1.03x slower                                                   |
| async_tree_io             | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.27 sec: 1.04x slower                                                  |
| asyncio_tcp               | 568 ms                                                   | 611 ms: 1.08x slower                                                    |
| async_tree_io_tg          | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 90.0 ms: 1.05x faster                                                   |
| nbody          | 114 ms                                                   | 112 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 31.0 ms: 1.02x faster                                                   |
| regex_effbot   | 4.87 ms                                                  | 5.02 ms: 1.03x slower                                                   |
| regex_dna      | 246 ms                                                   | 262 ms: 1.06x slower                                                    |
| regex_compile  | 128 ms                                                   | 184 ms: 1.43x slower                                                    |
| Geometric mean | (ref)                                                    | 1.11x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 20.2 us                                                  | 19.2 us: 1.05x faster                                                   |
| unpickle_list        | 6.65 us                                                  | 6.37 us: 1.04x faster                                                   |
| pickle_list          | 5.34 us                                                  | 5.21 us: 1.02x faster                                                   |
| json_dumps           | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| json_loads           | 31.4 us                                                  | 31.1 us: 1.01x faster                                                   |
| pickle               | 13.5 us                                                  | 13.8 us: 1.02x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                   | 150 ms: 1.02x slower                                                    |
| tomli_loads          | 2.53 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 268 us: 1.05x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 386 us: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_generate, pickle_dict, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| django_template | 42.3 ms                                                  | 51.8 ms: 1.22x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 34.4 ms: 1.24x slower                                                   |
| genshi_xml      | 60.2 ms                                                  | 83.1 ms: 1.38x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.20x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 37.9 us: 1.35x faster                                                   |
| async_tree_memoization_tg | 649 ms                                                   | 561 ms: 1.16x faster                                                    |
| deepcopy                  | 451 us                                                   | 400 us: 1.13x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 420 ms: 1.11x faster                                                    |
| async_tree_none           | 493 ms                                                   | 445 ms: 1.11x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 591 ms: 1.06x faster                                                    |
| unpickle                  | 20.2 us                                                  | 19.2 us: 1.05x faster                                                   |
| float                     | 94.4 ms                                                  | 90.0 ms: 1.05x faster                                                   |
| unpickle_list             | 6.65 us                                                  | 6.37 us: 1.04x faster                                                   |
| scimark_sor               | 159 ms                                                   | 152 ms: 1.04x faster                                                    |
| deepcopy_reduce           | 4.07 us                                                  | 3.93 us: 1.04x faster                                                   |
| logging_silent            | 135 ns                                                   | 131 ns: 1.03x faster                                                    |
| pathlib                   | 22.4 ms                                                  | 21.8 ms: 1.03x faster                                                   |
| python_startup            | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| pickle_list               | 5.34 us                                                  | 5.21 us: 1.02x faster                                                   |
| nbody                     | 114 ms                                                   | 112 ms: 1.02x faster                                                    |
| mako                      | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| json_dumps                | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| regex_v8                  | 31.5 ms                                                  | 31.0 ms: 1.02x faster                                                   |
| json_loads                | 31.4 us                                                  | 31.1 us: 1.01x faster                                                   |
| asyncio_websockets        | 656 ms                                                   | 664 ms: 1.01x slower                                                    |
| bpe_tokeniser             | 5.90 sec                                                 | 5.97 sec: 1.01x slower                                                  |
| thrift                    | 946 us                                                   | 960 us: 1.02x slower                                                    |
| sqlite_synth              | 3.84 us                                                  | 3.91 us: 1.02x slower                                                   |
| pickle                    | 13.5 us                                                  | 13.8 us: 1.02x slower                                                   |
| xml_etree_iterparse       | 147 ms                                                   | 150 ms: 1.02x slower                                                    |
| async_generators          | 496 ms                                                   | 508 ms: 1.02x slower                                                    |
| spectral_norm             | 141 ms                                                   | 145 ms: 1.03x slower                                                    |
| coroutines                | 28.2 ms                                                  | 29.0 ms: 1.03x slower                                                   |
| regex_effbot              | 4.87 ms                                                  | 5.02 ms: 1.03x slower                                                   |
| mdp                       | 3.36 sec                                                 | 3.48 sec: 1.03x slower                                                  |
| logging_format            | 7.83 us                                                  | 8.11 us: 1.04x slower                                                   |
| async_tree_io             | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.27 sec: 1.04x slower                                                  |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.87 ms: 1.04x slower                                                   |
| tomli_loads               | 2.53 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| unpickle_pure_python      | 254 us                                                   | 268 us: 1.05x slower                                                    |
| regex_dna                 | 246 ms                                                   | 262 ms: 1.06x slower                                                    |
| scimark_monte_carlo       | 83.8 ms                                                  | 89.1 ms: 1.06x slower                                                   |
| logging_simple            | 7.04 us                                                  | 7.54 us: 1.07x slower                                                   |
| pickle_pure_python        | 359 us                                                   | 386 us: 1.08x slower                                                    |
| asyncio_tcp               | 568 ms                                                   | 611 ms: 1.08x slower                                                    |
| scimark_lu                | 139 ms                                                   | 150 ms: 1.08x slower                                                    |
| bench_thread_pool         | 1.28 ms                                                  | 1.37 ms: 1.08x slower                                                   |
| async_tree_io_tg          | 1.09 sec                                                 | 1.18 sec: 1.08x slower                                                  |
| create_gc_cycles          | 2.12 ms                                                  | 2.29 ms: 1.08x slower                                                   |
| crypto_pyaes              | 82.7 ms                                                  | 89.9 ms: 1.09x slower                                                   |
| meteor_contest            | 113 ms                                                   | 124 ms: 1.09x slower                                                    |
| html5lib                  | 64.3 ms                                                  | 71.0 ms: 1.10x slower                                                   |
| typing_runtime_protocols  | 192 us                                                   | 213 us: 1.11x slower                                                    |
| gc_traversal              | 4.53 ms                                                  | 5.05 ms: 1.11x slower                                                   |
| fannkuch                  | 452 ms                                                   | 503 ms: 1.11x slower                                                    |
| tornado_http              | 131 ms                                                   | 147 ms: 1.12x slower                                                    |
| deltablue                 | 3.85 ms                                                  | 4.35 ms: 1.13x slower                                                   |
| go                        | 163 ms                                                   | 185 ms: 1.14x slower                                                    |
| pyflate                   | 556 ms                                                   | 640 ms: 1.15x slower                                                    |
| pycparser                 | 1.26 sec                                                 | 1.48 sec: 1.17x slower                                                  |
| raytrace                  | 298 ms                                                   | 350 ms: 1.18x slower                                                    |
| richards                  | 53.5 ms                                                  | 63.8 ms: 1.19x slower                                                   |
| richards_super            | 60.3 ms                                                  | 72.0 ms: 1.19x slower                                                   |
| sqlglot_normalize         | 128 ms                                                   | 156 ms: 1.22x slower                                                    |
| comprehensions            | 20.4 us                                                  | 24.9 us: 1.22x slower                                                   |
| django_template           | 42.3 ms                                                  | 51.8 ms: 1.22x slower                                                   |
| genshi_text               | 27.7 ms                                                  | 34.4 ms: 1.24x slower                                                   |
| 2to3                      | 306 ms                                                   | 383 ms: 1.25x slower                                                    |
| nqueens                   | 98.7 ms                                                  | 124 ms: 1.26x slower                                                    |
| sqlglot_parse             | 1.38 ms                                                  | 1.74 ms: 1.26x slower                                                   |
| docutils                  | 2.91 sec                                                 | 3.71 sec: 1.28x slower                                                  |
| sqlglot_transpile         | 1.73 ms                                                  | 2.21 ms: 1.28x slower                                                   |
| sympy_expand              | 455 ms                                                   | 598 ms: 1.32x slower                                                    |
| chaos                     | 68.8 ms                                                  | 90.5 ms: 1.32x slower                                                   |
| sqlglot_optimize          | 62.4 ms                                                  | 82.2 ms: 1.32x slower                                                   |
| pprint_safe_repr          | 926 ms                                                   | 1.23 sec: 1.33x slower                                                  |
| pprint_pformat            | 1.90 sec                                                 | 2.61 sec: 1.37x slower                                                  |
| genshi_xml                | 60.2 ms                                                  | 83.1 ms: 1.38x slower                                                   |
| sympy_str                 | 264 ms                                                   | 366 ms: 1.39x slower                                                    |
| sympy_integrate           | 21.0 ms                                                  | 29.6 ms: 1.41x slower                                                   |
| pylint                    | 343 ms                                                   | 486 ms: 1.42x slower                                                    |
| hexiom                    | 7.13 ms                                                  | 10.1 ms: 1.42x slower                                                   |
| regex_compile             | 128 ms                                                   | 184 ms: 1.43x slower                                                    |
| sympy_sum                 | 143 ms                                                   | 218 ms: 1.52x slower                                                    |
| generators                | 37.8 ms                                                  | 59.2 ms: 1.56x slower                                                   |
| unpack_sequence           | 57.2 ns                                                  | 144 ns: 2.53x slower                                                    |
| bench_mp_pool             | 7.30 ms                                                  | 2.07 sec: 283.20x slower                                                |
| Geometric mean            | (ref)                                                    | 1.16x slower                                                            |

Benchmark hidden because not significant (12): async_tree_cpu_io_mixed, xml_etree_generate, pickle_dict, json, scimark_fft, python_startup_no_site, pidigits, xml_etree_parse, telco, async_tree_cpu_io_mixed_tg, xml_etree_process, coverage
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.06x