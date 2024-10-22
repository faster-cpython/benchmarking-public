# Results vs. 3.13.0

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: linux-aarch64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 382 ms: 1.25x slower                                                    |
| docutils       | 2.91 sec                                                 | 3.93 sec: 1.35x slower                                                  |
| html5lib       | 64.3 ms                                                  | 71.2 ms: 1.11x slower                                                   |
| tornado_http   | 131 ms                                                   | 146 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                    | 1.20x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 561 ms: 1.16x faster                                                    |
| async_tree_none           | 493 ms                                                   | 440 ms: 1.12x faster                                                    |
| async_tree_none_tg        | 467 ms                                                   | 435 ms: 1.08x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 588 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 749 ms: 1.02x faster                                                    |
| asyncio_websockets        | 656 ms                                                   | 663 ms: 1.01x slower                                                    |
| coroutines                | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                                   |
| async_generators          | 496 ms                                                   | 510 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                  |
| async_tree_io             | 1.11 sec                                                 | 1.17 sec: 1.06x slower                                                  |
| async_tree_io_tg          | 1.09 sec                                                 | 1.17 sec: 1.08x slower                                                  |
| asyncio_tcp               | 568 ms                                                   | 627 ms: 1.10x slower                                                    |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 87.4 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.8 ms: 1.02x faster                                                   |
| regex_effbot   | 4.87 ms                                                  | 4.96 ms: 1.02x slower                                                   |
| regex_dna      | 246 ms                                                   | 254 ms: 1.03x slower                                                    |
| regex_compile  | 128 ms                                                   | 194 ms: 1.51x slower                                                    |
| Geometric mean | (ref)                                                    | 1.12x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_list        | 6.65 us                                                  | 6.36 us: 1.04x faster                                                   |
| unpickle             | 20.2 us                                                  | 19.5 us: 1.04x faster                                                   |
| xml_etree_generate   | 113 ms                                                   | 109 ms: 1.04x faster                                                    |
| pickle_list          | 5.34 us                                                  | 5.23 us: 1.02x faster                                                   |
| pickle               | 13.5 us                                                  | 13.9 us: 1.03x slower                                                   |
| tomli_loads          | 2.53 sec                                                 | 2.62 sec: 1.04x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 265 us: 1.04x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 404 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (6): json_dumps, json_loads, pickle_dict, xml_etree_parse, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| django_template | 42.3 ms                                                  | 51.7 ms: 1.22x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 35.1 ms: 1.27x slower                                                   |
| genshi_xml      | 60.2 ms                                                  | 80.8 ms: 1.34x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.20x slower                                                            |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 39.8 us: 1.28x faster                                                   |
| async_tree_memoization_tg | 649 ms                                                   | 561 ms: 1.16x faster                                                    |
| async_tree_none           | 493 ms                                                   | 440 ms: 1.12x faster                                                    |
| deepcopy                  | 451 us                                                   | 417 us: 1.08x faster                                                    |
| float                     | 94.4 ms                                                  | 87.4 ms: 1.08x faster                                                   |
| async_tree_none_tg        | 467 ms                                                   | 435 ms: 1.08x faster                                                    |
| async_tree_memoization    | 626 ms                                                   | 588 ms: 1.06x faster                                                    |
| scimark_sor               | 159 ms                                                   | 152 ms: 1.05x faster                                                    |
| pathlib                   | 22.4 ms                                                  | 21.4 ms: 1.05x faster                                                   |
| unpickle_list             | 6.65 us                                                  | 6.36 us: 1.04x faster                                                   |
| unpickle                  | 20.2 us                                                  | 19.5 us: 1.04x faster                                                   |
| deepcopy_reduce           | 4.07 us                                                  | 3.93 us: 1.04x faster                                                   |
| xml_etree_generate        | 113 ms                                                   | 109 ms: 1.04x faster                                                    |
| regex_v8                  | 31.5 ms                                                  | 30.8 ms: 1.02x faster                                                   |
| python_startup            | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| pickle_list               | 5.34 us                                                  | 5.23 us: 1.02x faster                                                   |
| async_tree_cpu_io_mixed   | 764 ms                                                   | 749 ms: 1.02x faster                                                    |
| mako                      | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| bpe_tokeniser             | 5.90 sec                                                 | 5.92 sec: 1.00x slower                                                  |
| asyncio_websockets        | 656 ms                                                   | 663 ms: 1.01x slower                                                    |
| json                      | 5.61 ms                                                  | 5.71 ms: 1.02x slower                                                   |
| regex_effbot              | 4.87 ms                                                  | 4.96 ms: 1.02x slower                                                   |
| coroutines                | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                                   |
| thrift                    | 946 us                                                   | 966 us: 1.02x slower                                                    |
| scimark_fft               | 447 ms                                                   | 458 ms: 1.02x slower                                                    |
| async_generators          | 496 ms                                                   | 510 ms: 1.03x slower                                                    |
| bench_mp_pool             | 7.30 ms                                                  | 7.53 ms: 1.03x slower                                                   |
| regex_dna                 | 246 ms                                                   | 254 ms: 1.03x slower                                                    |
| coverage                  | 98.5 ms                                                  | 102 ms: 1.03x slower                                                    |
| pickle                    | 13.5 us                                                  | 13.9 us: 1.03x slower                                                   |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                  |
| mdp                       | 3.36 sec                                                 | 3.48 sec: 1.03x slower                                                  |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.81 ms: 1.04x slower                                                   |
| tomli_loads               | 2.53 sec                                                 | 2.62 sec: 1.04x slower                                                  |
| spectral_norm             | 141 ms                                                   | 147 ms: 1.04x slower                                                    |
| unpickle_pure_python      | 254 us                                                   | 265 us: 1.04x slower                                                    |
| bench_thread_pool         | 1.28 ms                                                  | 1.34 ms: 1.05x slower                                                   |
| logging_format            | 7.83 us                                                  | 8.21 us: 1.05x slower                                                   |
| telco                     | 9.73 ms                                                  | 10.3 ms: 1.05x slower                                                   |
| async_tree_io             | 1.11 sec                                                 | 1.17 sec: 1.06x slower                                                  |
| scimark_lu                | 139 ms                                                   | 149 ms: 1.07x slower                                                    |
| logging_simple            | 7.04 us                                                  | 7.53 us: 1.07x slower                                                   |
| async_tree_io_tg          | 1.09 sec                                                 | 1.17 sec: 1.08x slower                                                  |
| crypto_pyaes              | 82.7 ms                                                  | 89.4 ms: 1.08x slower                                                   |
| create_gc_cycles          | 2.12 ms                                                  | 2.30 ms: 1.09x slower                                                   |
| meteor_contest            | 113 ms                                                   | 125 ms: 1.10x slower                                                    |
| asyncio_tcp               | 568 ms                                                   | 627 ms: 1.10x slower                                                    |
| html5lib                  | 64.3 ms                                                  | 71.2 ms: 1.11x slower                                                   |
| typing_runtime_protocols  | 192 us                                                   | 213 us: 1.11x slower                                                    |
| tornado_http              | 131 ms                                                   | 146 ms: 1.11x slower                                                    |
| fannkuch                  | 452 ms                                                   | 505 ms: 1.12x slower                                                    |
| pickle_pure_python        | 359 us                                                   | 404 us: 1.13x slower                                                    |
| scimark_monte_carlo       | 83.8 ms                                                  | 95.3 ms: 1.14x slower                                                   |
| deltablue                 | 3.85 ms                                                  | 4.40 ms: 1.14x slower                                                   |
| gc_traversal              | 4.53 ms                                                  | 5.27 ms: 1.16x slower                                                   |
| go                        | 163 ms                                                   | 189 ms: 1.16x slower                                                    |
| raytrace                  | 298 ms                                                   | 346 ms: 1.16x slower                                                    |
| sqlglot_normalize         | 128 ms                                                   | 151 ms: 1.18x slower                                                    |
| pyflate                   | 556 ms                                                   | 664 ms: 1.19x slower                                                    |
| comprehensions            | 20.4 us                                                  | 24.7 us: 1.21x slower                                                   |
| django_template           | 42.3 ms                                                  | 51.7 ms: 1.22x slower                                                   |
| pycparser                 | 1.26 sec                                                 | 1.56 sec: 1.24x slower                                                  |
| 2to3                      | 306 ms                                                   | 382 ms: 1.25x slower                                                    |
| sqlglot_parse             | 1.38 ms                                                  | 1.73 ms: 1.25x slower                                                   |
| richards                  | 53.5 ms                                                  | 67.0 ms: 1.25x slower                                                   |
| sqlglot_optimize          | 62.4 ms                                                  | 78.3 ms: 1.26x slower                                                   |
| richards_super            | 60.3 ms                                                  | 75.9 ms: 1.26x slower                                                   |
| genshi_text               | 27.7 ms                                                  | 35.1 ms: 1.27x slower                                                   |
| sqlglot_transpile         | 1.73 ms                                                  | 2.20 ms: 1.27x slower                                                   |
| nqueens                   | 98.7 ms                                                  | 127 ms: 1.28x slower                                                    |
| chaos                     | 68.8 ms                                                  | 92.3 ms: 1.34x slower                                                   |
| genshi_xml                | 60.2 ms                                                  | 80.8 ms: 1.34x slower                                                   |
| sympy_expand              | 455 ms                                                   | 613 ms: 1.35x slower                                                    |
| docutils                  | 2.91 sec                                                 | 3.93 sec: 1.35x slower                                                  |
| pprint_safe_repr          | 926 ms                                                   | 1.26 sec: 1.36x slower                                                  |
| sympy_integrate           | 21.0 ms                                                  | 28.5 ms: 1.36x slower                                                   |
| pylint                    | 343 ms                                                   | 477 ms: 1.39x slower                                                    |
| sympy_str                 | 264 ms                                                   | 366 ms: 1.39x slower                                                    |
| pprint_pformat            | 1.90 sec                                                 | 2.64 sec: 1.39x slower                                                  |
| hexiom                    | 7.13 ms                                                  | 10.2 ms: 1.44x slower                                                   |
| sympy_sum                 | 143 ms                                                   | 211 ms: 1.47x slower                                                    |
| generators                | 37.8 ms                                                  | 57.0 ms: 1.51x slower                                                   |
| regex_compile             | 128 ms                                                   | 194 ms: 1.51x slower                                                    |
| unpack_sequence           | 57.2 ns                                                  | 146 ns: 2.55x slower                                                    |
| Geometric mean            | (ref)                                                    | 1.10x slower                                                            |

Benchmark hidden because not significant (12): nbody, sqlite_synth, logging_silent, python_startup_no_site, json_dumps, pidigits, json_loads, pickle_dict, async_tree_cpu_io_mixed_tg, xml_etree_parse, xml_etree_process, xml_etree_iterparse
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240924-3.14.0a0-54dd77f-JIT/bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x