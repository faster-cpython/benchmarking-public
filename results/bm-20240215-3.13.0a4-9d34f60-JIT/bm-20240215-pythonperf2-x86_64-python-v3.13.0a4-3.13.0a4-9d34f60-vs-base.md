# Results vs. base

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| 2to3           | 292 ms                                                                                                     | 300 ms: 1.03x slower                                                                                           |
| chameleon      | 7.42 ms                                                                                                    | 7.14 ms: 1.04x faster                                                                                          |
| docutils       | 2.84 sec                                                                                                   | 2.88 sec: 1.01x slower                                                                                         |
| tornado_http   | 122 ms                                                                                                     | 126 ms: 1.03x slower                                                                                           |
| Geometric mean | (ref)                                                                                                      | 1.01x slower                                                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|--------------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg   | 1.08 sec                                                                                                   | 1.08 sec: 1.00x slower                                                                                         |
| async_tree_none_tg | 434 ms                                                                                                     | 438 ms: 1.01x slower                                                                                           |
| Geometric mean     | (ref)                                                                                                      | 1.00x slower                                                                                                   |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_io, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| float          | 78.8 ms                                                                                                    | 80.7 ms: 1.02x slower                                                                                          |
| nbody          | 84.8 ms                                                                                                    | 106 ms: 1.25x slower                                                                                           |
| Geometric mean | (ref)                                                                                                      | 1.09x slower                                                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                                                                    | 25.0 ms: 1.04x faster                                                                                          |
| regex_dna      | 241 ms                                                                                                     | 244 ms: 1.01x slower                                                                                           |
| regex_effbot   | 3.48 ms                                                                                                    | 3.53 ms: 1.01x slower                                                                                          |
| regex_compile  | 142 ms                                                                                                     | 145 ms: 1.02x slower                                                                                           |
| Geometric mean | (ref)                                                                                                      | 1.00x slower                                                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| pickle_pure_python   | 316 us                                                                                                     | 304 us: 1.04x faster                                                                                           |
| tomli_loads          | 2.38 sec                                                                                                   | 2.31 sec: 1.03x faster                                                                                         |
| xml_etree_generate   | 85.1 ms                                                                                                    | 83.4 ms: 1.02x faster                                                                                          |
| xml_etree_iterparse  | 105 ms                                                                                                     | 103 ms: 1.01x faster                                                                                           |
| pickle               | 10.3 us                                                                                                    | 10.2 us: 1.01x faster                                                                                          |
| json_dumps           | 10.5 ms                                                                                                    | 10.5 ms: 1.00x slower                                                                                          |
| pickle_dict          | 30.3 us                                                                                                    | 30.6 us: 1.01x slower                                                                                          |
| json_loads           | 25.3 us                                                                                                    | 25.6 us: 1.01x slower                                                                                          |
| pickle_list          | 4.33 us                                                                                                    | 4.50 us: 1.04x slower                                                                                          |
| unpickle_pure_python | 217 us                                                                                                     | 230 us: 1.06x slower                                                                                           |
| Geometric mean       | (ref)                                                                                                      | 1.00x slower                                                                                                   |

Benchmark hidden because not significant (4): xml_etree_process, unpickle_list, unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|------------------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                                                                    | 12.7 ms: 1.01x slower                                                                                          |
| python_startup_no_site | 11.0 ms                                                                                                    | 11.1 ms: 1.01x slower                                                                                          |
| Geometric mean         | (ref)                                                                                                      | 1.01x slower                                                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|-----------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| mako      | 10.4 ms                                                                                                    | 11.8 ms: 1.13x slower                                                                                          |

All benchmarks:
===============

| Benchmark               | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|-------------------------|:----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| gc_traversal            | 3.76 ms                                                                                                    | 3.47 ms: 1.08x faster                                                                                          |
| richards_super          | 60.8 ms                                                                                                    | 57.6 ms: 1.05x faster                                                                                          |
| richards                | 54.4 ms                                                                                                    | 51.7 ms: 1.05x faster                                                                                          |
| regex_v8                | 26.0 ms                                                                                                    | 25.0 ms: 1.04x faster                                                                                          |
| chameleon               | 7.42 ms                                                                                                    | 7.14 ms: 1.04x faster                                                                                          |
| create_gc_cycles        | 1.61 ms                                                                                                    | 1.55 ms: 1.04x faster                                                                                          |
| pickle_pure_python      | 316 us                                                                                                     | 304 us: 1.04x faster                                                                                           |
| tomli_loads             | 2.38 sec                                                                                                   | 2.31 sec: 1.03x faster                                                                                         |
| deepcopy_reduce         | 3.41 us                                                                                                    | 3.33 us: 1.02x faster                                                                                          |
| scimark_sor             | 146 ms                                                                                                     | 143 ms: 1.02x faster                                                                                           |
| xml_etree_generate      | 85.1 ms                                                                                                    | 83.4 ms: 1.02x faster                                                                                          |
| go                      | 170 ms                                                                                                     | 167 ms: 1.02x faster                                                                                           |
| logging_simple          | 6.63 us                                                                                                    | 6.51 us: 1.02x faster                                                                                          |
| xml_etree_iterparse     | 105 ms                                                                                                     | 103 ms: 1.01x faster                                                                                           |
| pickle                  | 10.3 us                                                                                                    | 10.2 us: 1.01x faster                                                                                          |
| generators              | 34.1 ms                                                                                                    | 34.0 ms: 1.00x faster                                                                                          |
| async_tree_io_tg        | 1.08 sec                                                                                                   | 1.08 sec: 1.00x slower                                                                                         |
| json_dumps              | 10.5 ms                                                                                                    | 10.5 ms: 1.00x slower                                                                                          |
| pathlib                 | 19.0 ms                                                                                                    | 19.1 ms: 1.01x slower                                                                                          |
| python_startup          | 12.6 ms                                                                                                    | 12.7 ms: 1.01x slower                                                                                          |
| json                    | 5.30 ms                                                                                                    | 5.35 ms: 1.01x slower                                                                                          |
| sqlglot_transpile       | 1.80 ms                                                                                                    | 1.82 ms: 1.01x slower                                                                                          |
| pickle_dict             | 30.3 us                                                                                                    | 30.6 us: 1.01x slower                                                                                          |
| python_startup_no_site  | 11.0 ms                                                                                                    | 11.1 ms: 1.01x slower                                                                                          |
| async_tree_none_tg      | 434 ms                                                                                                     | 438 ms: 1.01x slower                                                                                           |
| json_loads              | 25.3 us                                                                                                    | 25.6 us: 1.01x slower                                                                                          |
| docutils                | 2.84 sec                                                                                                   | 2.88 sec: 1.01x slower                                                                                         |
| regex_dna               | 241 ms                                                                                                     | 244 ms: 1.01x slower                                                                                           |
| sympy_expand            | 496 ms                                                                                                     | 502 ms: 1.01x slower                                                                                           |
| regex_effbot            | 3.48 ms                                                                                                    | 3.53 ms: 1.01x slower                                                                                          |
| mdp                     | 2.50 sec                                                                                                   | 2.53 sec: 1.01x slower                                                                                         |
| sqlite_synth            | 2.73 us                                                                                                    | 2.77 us: 1.01x slower                                                                                          |
| coverage                | 82.9 ms                                                                                                    | 84.4 ms: 1.02x slower                                                                                          |
| sqlglot_normalize       | 115 ms                                                                                                     | 117 ms: 1.02x slower                                                                                           |
| sympy_str               | 291 ms                                                                                                     | 298 ms: 1.02x slower                                                                                           |
| regex_compile           | 142 ms                                                                                                     | 145 ms: 1.02x slower                                                                                           |
| float                   | 78.8 ms                                                                                                    | 80.7 ms: 1.02x slower                                                                                          |
| deltablue               | 3.59 ms                                                                                                    | 3.69 ms: 1.03x slower                                                                                          |
| 2to3                    | 292 ms                                                                                                     | 300 ms: 1.03x slower                                                                                           |
| tornado_http            | 122 ms                                                                                                     | 126 ms: 1.03x slower                                                                                           |
| sympy_integrate         | 23.2 ms                                                                                                    | 23.9 ms: 1.03x slower                                                                                          |
| sqlglot_optimize        | 58.6 ms                                                                                                    | 60.4 ms: 1.03x slower                                                                                          |
| async_generators        | 359 ms                                                                                                     | 371 ms: 1.03x slower                                                                                           |
| sympy_sum               | 153 ms                                                                                                     | 158 ms: 1.03x slower                                                                                           |
| pycparser               | 1.28 sec                                                                                                   | 1.33 sec: 1.04x slower                                                                                         |
| meteor_contest          | 126 ms                                                                                                     | 130 ms: 1.04x slower                                                                                           |
| pickle_list             | 4.33 us                                                                                                    | 4.50 us: 1.04x slower                                                                                          |
| fannkuch                | 393 ms                                                                                                     | 409 ms: 1.04x slower                                                                                           |
| logging_silent          | 93.6 ns                                                                                                    | 97.7 ns: 1.04x slower                                                                                          |
| pyflate                 | 506 ms                                                                                                     | 529 ms: 1.04x slower                                                                                           |
| pprint_safe_repr        | 791 ms                                                                                                     | 826 ms: 1.04x slower                                                                                           |
| raytrace                | 262 ms                                                                                                     | 274 ms: 1.04x slower                                                                                           |
| scimark_lu              | 94.4 ms                                                                                                    | 99.3 ms: 1.05x slower                                                                                          |
| unpickle_pure_python    | 217 us                                                                                                     | 230 us: 1.06x slower                                                                                           |
| pprint_pformat          | 1.62 sec                                                                                                   | 1.72 sec: 1.06x slower                                                                                         |
| bench_mp_pool           | 4.58 ms                                                                                                    | 4.90 ms: 1.07x slower                                                                                          |
| nqueens                 | 88.8 ms                                                                                                    | 95.4 ms: 1.07x slower                                                                                          |
| crypto_pyaes            | 71.3 ms                                                                                                    | 79.3 ms: 1.11x slower                                                                                          |
| mako                    | 10.4 ms                                                                                                    | 11.8 ms: 1.13x slower                                                                                          |
| chaos                   | 61.0 ms                                                                                                    | 69.4 ms: 1.14x slower                                                                                          |
| scimark_monte_carlo     | 67.0 ms                                                                                                    | 78.5 ms: 1.17x slower                                                                                          |
| comprehensions          | 16.5 us                                                                                                    | 19.3 us: 1.17x slower                                                                                          |
| hexiom                  | 6.44 ms                                                                                                    | 7.63 ms: 1.19x slower                                                                                          |
| scimark_fft             | 301 ms                                                                                                     | 357 ms: 1.19x slower                                                                                           |
| spectral_norm           | 92.5 ms                                                                                                    | 115 ms: 1.24x slower                                                                                           |
| nbody                   | 84.8 ms                                                                                                    | 106 ms: 1.25x slower                                                                                           |
| scimark_sparse_mat_mult | 4.12 ms                                                                                                    | 5.23 ms: 1.27x slower                                                                                          |
| Geometric mean          | (ref)                                                                                                      | 1.03x slower                                                                                                   |

Benchmark hidden because not significant (24): deepcopy_memo, telco, async_tree_memoization_tg, xml_etree_process, unpickle_list, logging_format, async_tree_io, pidigits, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, unpickle, xml_etree_parse, async_tree_cpu_io_mixed_tg, typing_runtime_protocols, dulwich_log, sqlglot_parse, coroutines, async_tree_memoization, async_tree_cpu_io_mixed, deepcopy, asyncio_websockets, bench_thread_pool, mypy2
Ignored benchmarks (9) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x