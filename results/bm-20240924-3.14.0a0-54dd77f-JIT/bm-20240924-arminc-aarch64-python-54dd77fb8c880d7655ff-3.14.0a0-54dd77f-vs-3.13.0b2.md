# Results vs. 3.13.0b2

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: linux-aarch64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 382 ms: 1.25x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.93 sec: 1.27x slower                                                  |
| html5lib       | 66.1 ms                                                      | 71.2 ms: 1.08x slower                                                   |
| tornado_http   | 128 ms                                                       | 146 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                        | 1.18x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|---------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none           | 492 ms                                                       | 440 ms: 1.12x faster                                                    |
| async_tree_memoization    | 645 ms                                                       | 588 ms: 1.10x faster                                                    |
| async_tree_none_tg        | 476 ms                                                       | 435 ms: 1.10x faster                                                    |
| async_tree_io_tg          | 1.27 sec                                                     | 1.17 sec: 1.08x faster                                                  |
| async_tree_memoization_tg | 604 ms                                                       | 561 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed   | 791 ms                                                       | 749 ms: 1.06x faster                                                    |
| async_tree_io             | 1.22 sec                                                     | 1.17 sec: 1.05x faster                                                  |
| Geometric mean            | (ref)                                                        | 1.07x faster                                                            |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 87.4 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.8 ms: 1.01x faster                                                   |
| regex_compile  | 128 ms                                                       | 194 ms: 1.52x slower                                                    |
| Geometric mean | (ref)                                                        | 1.10x slower                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 109 ms: 1.04x faster                                                    |
| unpickle_list        | 6.52 us                                                      | 6.36 us: 1.02x faster                                                   |
| json_loads           | 32.1 us                                                      | 31.4 us: 1.02x faster                                                   |
| unpickle             | 19.8 us                                                      | 19.5 us: 1.02x faster                                                   |
| pickle_list          | 5.27 us                                                      | 5.23 us: 1.01x faster                                                   |
| pickle_dict          | 37.6 us                                                      | 38.3 us: 1.02x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                  |
| pickle               | 13.4 us                                                      | 13.9 us: 1.04x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 265 us: 1.05x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 404 us: 1.13x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.73 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 51.7 ms: 1.22x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 35.1 ms: 1.28x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 80.8 ms: 1.34x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.20x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|---------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo             | 50.8 us                                                      | 39.8 us: 1.27x faster                                                   |
| async_tree_none           | 492 ms                                                       | 440 ms: 1.12x faster                                                    |
| async_tree_memoization    | 645 ms                                                       | 588 ms: 1.10x faster                                                    |
| async_tree_none_tg        | 476 ms                                                       | 435 ms: 1.10x faster                                                    |
| async_tree_io_tg          | 1.27 sec                                                     | 1.17 sec: 1.08x faster                                                  |
| async_tree_memoization_tg | 604 ms                                                       | 561 ms: 1.08x faster                                                    |
| deepcopy                  | 448 us                                                       | 417 us: 1.07x faster                                                    |
| pathlib                   | 22.8 ms                                                      | 21.4 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed   | 791 ms                                                       | 749 ms: 1.06x faster                                                    |
| scimark_sor               | 159 ms                                                       | 152 ms: 1.05x faster                                                    |
| async_tree_io             | 1.22 sec                                                     | 1.17 sec: 1.05x faster                                                  |
| float                     | 91.4 ms                                                      | 87.4 ms: 1.05x faster                                                   |
| xml_etree_generate        | 114 ms                                                       | 109 ms: 1.04x faster                                                    |
| deepcopy_reduce           | 4.04 us                                                      | 3.93 us: 1.03x faster                                                   |
| unpickle_list             | 6.52 us                                                      | 6.36 us: 1.02x faster                                                   |
| sqlite_synth              | 3.90 us                                                      | 3.82 us: 1.02x faster                                                   |
| json_loads                | 32.1 us                                                      | 31.4 us: 1.02x faster                                                   |
| regex_dna                 | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| unpickle                  | 19.8 us                                                      | 19.5 us: 1.02x faster                                                   |
| regex_v8                  | 31.1 ms                                                      | 30.8 ms: 1.01x faster                                                   |
| pickle_list               | 5.27 us                                                      | 5.23 us: 1.01x faster                                                   |
| logging_silent            | 133 ns                                                       | 135 ns: 1.01x slower                                                    |
| python_startup_no_site    | 8.60 ms                                                      | 8.73 ms: 1.01x slower                                                   |
| bpe_tokeniser             | 5.83 sec                                                     | 5.92 sec: 1.02x slower                                                  |
| pickle_dict               | 37.6 us                                                      | 38.3 us: 1.02x slower                                                   |
| asyncio_tcp_ssl           | 2.21 sec                                                     | 2.25 sec: 1.02x slower                                                  |
| json_dumps                | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| tomli_loads               | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                  |
| telco                     | 10.0 ms                                                      | 10.3 ms: 1.02x slower                                                   |
| scimark_fft               | 445 ms                                                       | 458 ms: 1.03x slower                                                    |
| coverage                  | 98.4 ms                                                      | 102 ms: 1.03x slower                                                    |
| spectral_norm             | 141 ms                                                       | 147 ms: 1.04x slower                                                    |
| pickle                    | 13.4 us                                                      | 13.9 us: 1.04x slower                                                   |
| scimark_sparse_mat_mult   | 6.55 ms                                                      | 6.81 ms: 1.04x slower                                                   |
| mdp                       | 3.33 sec                                                     | 3.48 sec: 1.04x slower                                                  |
| async_generators          | 488 ms                                                       | 510 ms: 1.05x slower                                                    |
| logging_simple            | 7.21 us                                                      | 7.53 us: 1.05x slower                                                   |
| logging_format            | 7.82 us                                                      | 8.21 us: 1.05x slower                                                   |
| unpickle_pure_python      | 251 us                                                       | 265 us: 1.05x slower                                                    |
| scimark_lu                | 141 ms                                                       | 149 ms: 1.05x slower                                                    |
| bench_thread_pool         | 1.26 ms                                                      | 1.34 ms: 1.06x slower                                                   |
| bench_mp_pool             | 7.03 ms                                                      | 7.53 ms: 1.07x slower                                                   |
| asyncio_tcp               | 584 ms                                                       | 627 ms: 1.07x slower                                                    |
| html5lib                  | 66.1 ms                                                      | 71.2 ms: 1.08x slower                                                   |
| crypto_pyaes              | 82.0 ms                                                      | 89.4 ms: 1.09x slower                                                   |
| typing_runtime_protocols  | 193 us                                                       | 213 us: 1.10x slower                                                    |
| meteor_contest            | 113 ms                                                       | 125 ms: 1.10x slower                                                    |
| fannkuch                  | 451 ms                                                       | 505 ms: 1.12x slower                                                    |
| pickle_pure_python        | 359 us                                                       | 404 us: 1.13x slower                                                    |
| deltablue                 | 3.88 ms                                                      | 4.40 ms: 1.14x slower                                                   |
| tornado_http              | 128 ms                                                       | 146 ms: 1.14x slower                                                    |
| scimark_monte_carlo       | 82.3 ms                                                      | 95.3 ms: 1.16x slower                                                   |
| sqlglot_normalize         | 129 ms                                                       | 151 ms: 1.17x slower                                                    |
| raytrace                  | 297 ms                                                       | 346 ms: 1.17x slower                                                    |
| go                        | 161 ms                                                       | 189 ms: 1.18x slower                                                    |
| pyflate                   | 557 ms                                                       | 664 ms: 1.19x slower                                                    |
| richards                  | 55.9 ms                                                      | 67.0 ms: 1.20x slower                                                   |
| comprehensions            | 20.5 us                                                      | 24.7 us: 1.20x slower                                                   |
| sqlglot_parse             | 1.42 ms                                                      | 1.73 ms: 1.21x slower                                                   |
| richards_super            | 62.3 ms                                                      | 75.9 ms: 1.22x slower                                                   |
| django_template           | 42.3 ms                                                      | 51.7 ms: 1.22x slower                                                   |
| sqlglot_optimize          | 62.6 ms                                                      | 78.3 ms: 1.25x slower                                                   |
| 2to3                      | 305 ms                                                       | 382 ms: 1.25x slower                                                    |
| docutils                  | 3.10 sec                                                     | 3.93 sec: 1.27x slower                                                  |
| pycparser                 | 1.22 sec                                                     | 1.56 sec: 1.28x slower                                                  |
| genshi_text               | 27.4 ms                                                      | 35.1 ms: 1.28x slower                                                   |
| nqueens                   | 98.9 ms                                                      | 127 ms: 1.28x slower                                                    |
| sqlglot_transpile         | 1.71 ms                                                      | 2.20 ms: 1.29x slower                                                   |
| genshi_xml                | 60.4 ms                                                      | 80.8 ms: 1.34x slower                                                   |
| sympy_expand              | 457 ms                                                       | 613 ms: 1.34x slower                                                    |
| pprint_safe_repr          | 933 ms                                                       | 1.26 sec: 1.35x slower                                                  |
| chaos                     | 68.3 ms                                                      | 92.3 ms: 1.35x slower                                                   |
| sympy_integrate           | 20.9 ms                                                      | 28.5 ms: 1.36x slower                                                   |
| pprint_pformat            | 1.93 sec                                                     | 2.64 sec: 1.37x slower                                                  |
| sympy_str                 | 265 ms                                                       | 366 ms: 1.38x slower                                                    |
| pylint                    | 337 ms                                                       | 477 ms: 1.42x slower                                                    |
| dulwich_log               | 58.5 ms                                                      | 83.2 ms: 1.42x slower                                                   |
| hexiom                    | 7.08 ms                                                      | 10.2 ms: 1.45x slower                                                   |
| sympy_sum                 | 144 ms                                                       | 211 ms: 1.47x slower                                                    |
| regex_compile             | 128 ms                                                       | 194 ms: 1.52x slower                                                    |
| generators                | 37.1 ms                                                      | 57.0 ms: 1.54x slower                                                   |
| Geometric mean            | (ref)                                                        | 1.09x slower                                                            |

Benchmark hidden because not significant (15): async_tree_cpu_io_mixed_tg, create_gc_cycles, coroutines, nbody, xml_etree_parse, regex_effbot, mako, pidigits, python_startup, thrift, xml_etree_process, asyncio_websockets, json, gc_traversal, xml_etree_iterparse
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240924-3.14.0a0-54dd77f-JIT/bm-20240924-arminc-aarch64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.09x