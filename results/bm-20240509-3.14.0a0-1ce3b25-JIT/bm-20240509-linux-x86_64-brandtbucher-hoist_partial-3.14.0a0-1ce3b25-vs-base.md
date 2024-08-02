# Results vs. base

- fork: brandtbucher
- ref: hoist_partial
- machine: linux-x86_64
- commit hash: 1ce3b25
- commit date: 2024-05-09
- overall geometric mean: 1.00x faster
- HPT reliability: 91.06%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                              | 2.98 sec: 1.01x slower                                               |
| html5lib       | 70.7 ms                                                               | 69.1 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (3): 2to3, chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 632 ms                                                                | 618 ms: 1.02x faster                                                 |
| async_tree_none         | 370 ms                                                                | 363 ms: 1.02x faster                                                 |
| Geometric mean          | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 71.1 ms                                                               | 70.6 ms: 1.01x faster                                                |
| nbody          | 84.0 ms                                                               | 86.1 ms: 1.02x slower                                                |
| pidigits       | 188 ms                                                                | 197 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.68 ms                                                               | 3.58 ms: 1.03x faster                                                |
| regex_v8       | 25.3 ms                                                               | 25.1 ms: 1.01x faster                                                |
| regex_dna      | 228 ms                                                                | 226 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_list          | 5.56 us                                                               | 5.29 us: 1.05x faster                                                |
| pickle_dict          | 34.7 us                                                               | 33.1 us: 1.05x faster                                                |
| pickle_pure_python   | 310 us                                                                | 304 us: 1.02x faster                                                 |
| tomli_loads          | 1.98 sec                                                              | 1.96 sec: 1.01x faster                                               |
| xml_etree_process    | 58.9 ms                                                               | 58.2 ms: 1.01x faster                                                |
| pickle               | 12.1 us                                                               | 12.0 us: 1.01x faster                                                |
| unpickle_pure_python | 223 us                                                                | 222 us: 1.01x faster                                                 |
| json_loads           | 28.9 us                                                               | 28.7 us: 1.00x faster                                                |
| xml_etree_generate   | 83.2 ms                                                               | 83.6 ms: 1.00x slower                                                |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                |
| unpickle_list        | 5.21 us                                                               | 5.27 us: 1.01x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.67 ms                                                               | 7.70 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 59.9 ms                                                               | 58.7 ms: 1.02x faster                                                |
| django_template | 37.1 ms                                                               | 36.5 ms: 1.02x faster                                                |
| mako            | 9.67 ms                                                               | 9.62 ms: 1.00x faster                                                |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_list             | 5.56 us                                                               | 5.29 us: 1.05x faster                                                |
| pickle_dict             | 34.7 us                                                               | 33.1 us: 1.05x faster                                                |
| regex_effbot            | 3.68 ms                                                               | 3.58 ms: 1.03x faster                                                |
| spectral_norm           | 104 ms                                                                | 101 ms: 1.03x faster                                                 |
| pycparser               | 1.20 sec                                                              | 1.16 sec: 1.03x faster                                               |
| pyflate                 | 460 ms                                                                | 449 ms: 1.03x faster                                                 |
| coroutines              | 23.3 ms                                                               | 22.8 ms: 1.02x faster                                                |
| scimark_sparse_mat_mult | 4.58 ms                                                               | 4.47 ms: 1.02x faster                                                |
| html5lib                | 70.7 ms                                                               | 69.1 ms: 1.02x faster                                                |
| async_tree_cpu_io_mixed | 632 ms                                                                | 618 ms: 1.02x faster                                                 |
| logging_format          | 6.53 us                                                               | 6.40 us: 1.02x faster                                                |
| richards                | 43.6 ms                                                               | 42.7 ms: 1.02x faster                                                |
| genshi_xml              | 59.9 ms                                                               | 58.7 ms: 1.02x faster                                                |
| comprehensions          | 16.8 us                                                               | 16.4 us: 1.02x faster                                                |
| pprint_safe_repr        | 739 ms                                                                | 724 ms: 1.02x faster                                                 |
| pickle_pure_python      | 310 us                                                                | 304 us: 1.02x faster                                                 |
| deltablue               | 3.82 ms                                                               | 3.75 ms: 1.02x faster                                                |
| async_tree_none         | 370 ms                                                                | 363 ms: 1.02x faster                                                 |
| sqlglot_optimize        | 58.0 ms                                                               | 57.1 ms: 1.02x faster                                                |
| logging_silent          | 109 ns                                                                | 107 ns: 1.02x faster                                                 |
| django_template         | 37.1 ms                                                               | 36.5 ms: 1.02x faster                                                |
| logging_simple          | 5.85 us                                                               | 5.77 us: 1.01x faster                                                |
| tomli_loads             | 1.98 sec                                                              | 1.96 sec: 1.01x faster                                               |
| sqlglot_normalize       | 116 ms                                                                | 114 ms: 1.01x faster                                                 |
| xml_etree_process       | 58.9 ms                                                               | 58.2 ms: 1.01x faster                                                |
| scimark_monte_carlo     | 64.6 ms                                                               | 64.1 ms: 1.01x faster                                                |
| richards_super          | 49.5 ms                                                               | 49.1 ms: 1.01x faster                                                |
| float                   | 71.1 ms                                                               | 70.6 ms: 1.01x faster                                                |
| pickle                  | 12.1 us                                                               | 12.0 us: 1.01x faster                                                |
| regex_v8                | 25.3 ms                                                               | 25.1 ms: 1.01x faster                                                |
| async_generators        | 471 ms                                                                | 468 ms: 1.01x faster                                                 |
| regex_dna               | 228 ms                                                                | 226 ms: 1.01x faster                                                 |
| unpickle_pure_python    | 223 us                                                                | 222 us: 1.01x faster                                                 |
| mako                    | 9.67 ms                                                               | 9.62 ms: 1.00x faster                                                |
| json_loads              | 28.9 us                                                               | 28.7 us: 1.00x faster                                                |
| dulwich_log             | 70.7 ms                                                               | 70.4 ms: 1.00x faster                                                |
| bench_thread_pool       | 874 us                                                                | 871 us: 1.00x faster                                                 |
| xml_etree_generate      | 83.2 ms                                                               | 83.6 ms: 1.00x slower                                                |
| sympy_sum               | 173 ms                                                                | 174 ms: 1.00x slower                                                 |
| create_gc_cycles        | 1.83 ms                                                               | 1.84 ms: 1.00x slower                                                |
| python_startup_no_site  | 7.67 ms                                                               | 7.70 ms: 1.00x slower                                                |
| sqlglot_transpile       | 1.64 ms                                                               | 1.65 ms: 1.01x slower                                                |
| sympy_integrate         | 22.7 ms                                                               | 22.8 ms: 1.01x slower                                                |
| json_dumps              | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                |
| aiohttp                 | 1.25 ms                                                               | 1.26 ms: 1.01x slower                                                |
| generators              | 30.0 ms                                                               | 30.2 ms: 1.01x slower                                                |
| docutils                | 2.96 sec                                                              | 2.98 sec: 1.01x slower                                               |
| go                      | 146 ms                                                                | 148 ms: 1.01x slower                                                 |
| crypto_pyaes            | 68.9 ms                                                               | 69.6 ms: 1.01x slower                                                |
| unpickle_list           | 5.21 us                                                               | 5.27 us: 1.01x slower                                                |
| scimark_lu              | 123 ms                                                                | 125 ms: 1.01x slower                                                 |
| scimark_sor             | 130 ms                                                                | 132 ms: 1.01x slower                                                 |
| scimark_fft             | 317 ms                                                                | 321 ms: 1.01x slower                                                 |
| nqueens                 | 86.6 ms                                                               | 87.7 ms: 1.01x slower                                                |
| fannkuch                | 362 ms                                                                | 368 ms: 1.01x slower                                                 |
| hexiom                  | 6.56 ms                                                               | 6.69 ms: 1.02x slower                                                |
| raytrace                | 278 ms                                                                | 284 ms: 1.02x slower                                                 |
| nbody                   | 84.0 ms                                                               | 86.1 ms: 1.02x slower                                                |
| asyncio_tcp             | 505 ms                                                                | 519 ms: 1.03x slower                                                 |
| deepcopy                | 371 us                                                                | 383 us: 1.03x slower                                                 |
| gc_traversal            | 3.94 ms                                                               | 4.11 ms: 1.04x slower                                                |
| pidigits                | 188 ms                                                                | 197 ms: 1.05x slower                                                 |
| mdp                     | 2.60 sec                                                              | 2.73 sec: 1.05x slower                                               |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (37): async_tree_cpu_io_mixed_tg, async_tree_memoization, chaos, pprint_pformat, typing_runtime_protocols, chameleon, tornado_http, gunicorn, sympy_expand, deepcopy_reduce, pylint, sqlite_synth, dask, meteor_contest, regex_compile, coverage, telco, asyncio_tcp_ssl, asyncio_websockets, sympy_str, 2to3, deepcopy_memo, async_tree_io, bench_mp_pool, json, async_tree_io_tg, python_startup, xml_etree_iterparse, sqlglot_parse, thrift, async_tree_none_tg, async_tree_memoization_tg, pathlib, xml_etree_parse, genshi_text, flaskblogging, unpickle

# HPT report

- Reliability score: 91.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x