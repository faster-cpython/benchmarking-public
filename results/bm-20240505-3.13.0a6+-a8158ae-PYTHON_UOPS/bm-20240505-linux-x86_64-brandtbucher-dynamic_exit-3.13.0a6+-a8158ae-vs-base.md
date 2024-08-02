# Results vs. base

- fork: brandtbucher
- ref: dynamic_exit
- machine: linux-x86_64
- commit hash: a8158ae
- commit date: 2024-05-05
- overall geometric mean: 1.02x slower
- HPT reliability: 99.70%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6+-d8d9491 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 355 ms                                                                 | 357 ms: 1.01x slower                                                 |
| chameleon      | 8.72 ms                                                                | 9.02 ms: 1.03x slower                                                |
| html5lib       | 82.4 ms                                                                | 83.5 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6+-d8d9491 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 92.0 ms                                                                | 92.6 ms: 1.01x slower                                                |
| nbody          | 122 ms                                                                 | 123 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6+-d8d9491 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.78 ms                                                                | 3.75 ms: 1.01x faster                                                |
| regex_dna      | 223 ms                                                                 | 223 ms: 1.00x faster                                                 |
| regex_v8       | 27.0 ms                                                                | 27.1 ms: 1.00x slower                                                |
| regex_compile  | 213 ms                                                                 | 220 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6+-d8d9491 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_list        | 5.39 us                                                                | 5.17 us: 1.04x faster                                                |
| xml_etree_process    | 72.3 ms                                                                | 71.4 ms: 1.01x faster                                                |
| pickle_list          | 5.00 us                                                                | 5.03 us: 1.01x slower                                                |
| pickle_dict          | 35.8 us                                                                | 36.0 us: 1.01x slower                                                |
| json_dumps           | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                                |
| unpickle_pure_python | 327 us                                                                 | 331 us: 1.01x slower                                                 |
| tomli_loads          | 2.76 sec                                                               | 2.81 sec: 1.02x slower                                               |
| pickle_pure_python   | 469 us                                                                 | 525 us: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (6): pickle, xml_etree_parse, xml_etree_iterparse, xml_etree_generate, json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6+-d8d9491 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.28 ms                                                                | 7.25 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6+-d8d9491 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 14.0 ms                                                                | 14.2 ms: 1.01x slower                                                |
| genshi_text     | 38.4 ms                                                                | 39.8 ms: 1.04x slower                                                |
| django_template | 47.5 ms                                                                | 49.2 ms: 1.04x slower                                                |
| genshi_xml      | 79.5 ms                                                                | 82.8 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                         |

All benchmarks:
===============

| Benchmark              | bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6+-d8d9491 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| scimark_monte_carlo    | 114 ms                                                                 | 99.5 ms: 1.15x faster                                                |
| scimark_sor            | 168 ms                                                                 | 158 ms: 1.06x faster                                                 |
| mdp                    | 3.08 sec                                                               | 2.91 sec: 1.06x faster                                               |
| fannkuch               | 510 ms                                                                 | 483 ms: 1.06x faster                                                 |
| unpickle_list          | 5.39 us                                                                | 5.17 us: 1.04x faster                                                |
| scimark_fft            | 460 ms                                                                 | 445 ms: 1.03x faster                                                 |
| pyflate                | 639 ms                                                                 | 619 ms: 1.03x faster                                                 |
| sqlglot_parse          | 1.85 ms                                                                | 1.81 ms: 1.02x faster                                                |
| json                   | 5.62 ms                                                                | 5.53 ms: 1.02x faster                                                |
| coverage               | 93.9 ms                                                                | 92.4 ms: 1.02x faster                                                |
| sqlglot_transpile      | 2.27 ms                                                                | 2.24 ms: 1.01x faster                                                |
| xml_etree_process      | 72.3 ms                                                                | 71.4 ms: 1.01x faster                                                |
| coroutines             | 25.1 ms                                                                | 24.8 ms: 1.01x faster                                                |
| comprehensions         | 27.4 us                                                                | 27.1 us: 1.01x faster                                                |
| sympy_integrate        | 26.1 ms                                                                | 25.9 ms: 1.01x faster                                                |
| regex_effbot           | 3.78 ms                                                                | 3.75 ms: 1.01x faster                                                |
| meteor_contest         | 130 ms                                                                 | 129 ms: 1.01x faster                                                 |
| create_gc_cycles       | 1.88 ms                                                                | 1.87 ms: 1.00x faster                                                |
| python_startup_no_site | 7.28 ms                                                                | 7.25 ms: 1.00x faster                                                |
| regex_dna              | 223 ms                                                                 | 223 ms: 1.00x faster                                                 |
| asyncio_tcp            | 528 ms                                                                 | 526 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl        | 1.88 sec                                                               | 1.87 sec: 1.00x faster                                               |
| regex_v8               | 27.0 ms                                                                | 27.1 ms: 1.00x slower                                                |
| crypto_pyaes           | 99.6 ms                                                                | 99.9 ms: 1.00x slower                                                |
| dulwich_log            | 77.6 ms                                                                | 77.9 ms: 1.00x slower                                                |
| 2to3                   | 355 ms                                                                 | 357 ms: 1.01x slower                                                 |
| pickle_list            | 5.00 us                                                                | 5.03 us: 1.01x slower                                                |
| float                  | 92.0 ms                                                                | 92.6 ms: 1.01x slower                                                |
| pickle_dict            | 35.8 us                                                                | 36.0 us: 1.01x slower                                                |
| nbody                  | 122 ms                                                                 | 123 ms: 1.01x slower                                                 |
| json_dumps             | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                                |
| pathlib                | 18.9 ms                                                                | 19.0 ms: 1.01x slower                                                |
| mako                   | 14.0 ms                                                                | 14.2 ms: 1.01x slower                                                |
| sympy_sum              | 192 ms                                                                 | 194 ms: 1.01x slower                                                 |
| spectral_norm          | 136 ms                                                                 | 137 ms: 1.01x slower                                                 |
| sympy_expand           | 607 ms                                                                 | 614 ms: 1.01x slower                                                 |
| html5lib               | 82.4 ms                                                                | 83.5 ms: 1.01x slower                                                |
| unpickle_pure_python   | 327 us                                                                 | 331 us: 1.01x slower                                                 |
| pycparser              | 1.58 sec                                                               | 1.60 sec: 1.01x slower                                               |
| telco                  | 10.6 ms                                                                | 10.7 ms: 1.01x slower                                                |
| deepcopy               | 510 us                                                                 | 518 us: 1.02x slower                                                 |
| tomli_loads            | 2.76 sec                                                               | 2.81 sec: 1.02x slower                                               |
| deepcopy_reduce        | 4.36 us                                                                | 4.45 us: 1.02x slower                                                |
| chaos                  | 85.7 ms                                                                | 87.6 ms: 1.02x slower                                                |
| async_generators       | 490 ms                                                                 | 504 ms: 1.03x slower                                                 |
| sqlglot_normalize      | 150 ms                                                                 | 154 ms: 1.03x slower                                                 |
| regex_compile          | 213 ms                                                                 | 220 ms: 1.03x slower                                                 |
| chameleon              | 8.72 ms                                                                | 9.02 ms: 1.03x slower                                                |
| genshi_text            | 38.4 ms                                                                | 39.8 ms: 1.04x slower                                                |
| django_template        | 47.5 ms                                                                | 49.2 ms: 1.04x slower                                                |
| deltablue              | 4.50 ms                                                                | 4.67 ms: 1.04x slower                                                |
| genshi_xml             | 79.5 ms                                                                | 82.8 ms: 1.04x slower                                                |
| logging_format         | 7.52 us                                                                | 7.83 us: 1.04x slower                                                |
| logging_simple         | 6.67 us                                                                | 6.97 us: 1.04x slower                                                |
| deepcopy_memo          | 54.2 us                                                                | 56.6 us: 1.05x slower                                                |
| sqlglot_optimize       | 72.0 ms                                                                | 75.4 ms: 1.05x slower                                                |
| bench_thread_pool      | 947 us                                                                 | 991 us: 1.05x slower                                                 |
| go                     | 197 ms                                                                 | 208 ms: 1.05x slower                                                 |
| logging_silent         | 144 ns                                                                 | 152 ns: 1.06x slower                                                 |
| hexiom                 | 9.84 ms                                                                | 10.7 ms: 1.09x slower                                                |
| richards_super         | 73.1 ms                                                                | 79.4 ms: 1.09x slower                                                |
| richards               | 64.9 ms                                                                | 71.0 ms: 1.10x slower                                                |
| pprint_safe_repr       | 1.10 sec                                                               | 1.21 sec: 1.10x slower                                               |
| pprint_pformat         | 2.31 sec                                                               | 2.55 sec: 1.10x slower                                               |
| nqueens                | 127 ms                                                                 | 141 ms: 1.11x slower                                                 |
| pickle_pure_python     | 469 us                                                                 | 525 us: 1.12x slower                                                 |
| generators             | 30.5 ms                                                                | 65.9 ms: 2.16x slower                                                |
| Geometric mean         | (ref)                                                                  | 1.02x slower                                                         |

Benchmark hidden because not significant (34): djangocms, pickle, dask, bench_mp_pool, async_tree_memoization, async_tree_memoization_tg, scimark_sparse_mat_mult, typing_runtime_protocols, tornado_http, asyncio_websockets, async_tree_cpu_io_mixed, sqlite_synth, python_startup, xml_etree_parse, raytrace, gunicorn, xml_etree_iterparse, pidigits, gc_traversal, xml_etree_generate, json_loads, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_io, thrift, aiohttp, scimark_lu, flaskblogging, mypy2, sympy_str, async_tree_none, async_tree_none_tg, unpickle, pylint

# HPT report

- Reliability score: 99.70% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x