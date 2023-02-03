
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 906fc0d
- commit date: 2023-01-30
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 253 ms: 1.01x slower                                                |
| chameleon      | 6.35 ms                                                                | 6.31 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 94.2 ms                                                                | 95.5 ms: 1.01x slower                                               |
| pidigits       | 189 ms                                                                 | 199 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 128 ms: 1.01x faster                                                |
| regex_v8       | 21.1 ms                                                                | 21.7 ms: 1.03x slower                                               |
| regex_dna      | 200 ms                                                                 | 209 ms: 1.04x slower                                                |
| regex_effbot   | 3.36 ms                                                                | 3.63 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse  | 106 ms                                                                 | 103 ms: 1.03x faster                                                |
| pickle_dict          | 32.2 us                                                                | 31.2 us: 1.03x faster                                               |
| unpickle_list        | 5.04 us                                                                | 4.89 us: 1.03x faster                                               |
| pickle               | 10.3 us                                                                | 10.2 us: 1.01x faster                                               |
| pickle_list          | 4.26 us                                                                | 4.24 us: 1.01x faster                                               |
| unpickle_pure_python | 198 us                                                                 | 197 us: 1.00x faster                                                |
| xml_etree_generate   | 77.3 ms                                                                | 77.6 ms: 1.00x slower                                               |
| xml_etree_parse      | 147 ms                                                                 | 149 ms: 1.01x slower                                                |
| json_dumps           | 9.37 ms                                                                | 9.58 ms: 1.02x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (4): json_loads, unpickle, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.48 ms                                                                | 6.49 ms: 1.00x slower                                               |
| python_startup         | 8.94 ms                                                                | 8.98 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 32.9 ms                                                                | 33.1 ms: 1.01x slower                                               |
| mako            | 9.77 ms                                                                | 9.87 ms: 1.01x slower                                               |
| genshi_text     | 20.7 ms                                                                | 21.0 ms: 1.01x slower                                               |
| genshi_xml      | 46.7 ms                                                                | 47.6 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                        |

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| richards                | 43.9 ms                                                                | 41.6 ms: 1.05x faster                                               |
| xml_etree_iterparse     | 106 ms                                                                 | 103 ms: 1.03x faster                                                |
| pickle_dict             | 32.2 us                                                                | 31.2 us: 1.03x faster                                               |
| coverage                | 99.1 ms                                                                | 96.0 ms: 1.03x faster                                               |
| unpickle_list           | 5.04 us                                                                | 4.89 us: 1.03x faster                                               |
| coroutines              | 25.8 ms                                                                | 25.1 ms: 1.03x faster                                               |
| scimark_sparse_mat_mult | 4.09 ms                                                                | 4.02 ms: 1.02x faster                                               |
| pprint_safe_repr        | 679 ms                                                                 | 669 ms: 1.02x faster                                                |
| chaos                   | 64.7 ms                                                                | 63.9 ms: 1.01x faster                                               |
| regex_compile           | 130 ms                                                                 | 128 ms: 1.01x faster                                                |
| pickle                  | 10.3 us                                                                | 10.2 us: 1.01x faster                                               |
| logging_silent          | 93.3 ns                                                                | 92.2 ns: 1.01x faster                                               |
| pyflate                 | 400 ms                                                                 | 396 ms: 1.01x faster                                                |
| sympy_expand            | 458 ms                                                                 | 453 ms: 1.01x faster                                                |
| gunicorn                | 1.08 ms                                                                | 1.07 ms: 1.01x faster                                               |
| logging_simple          | 5.73 us                                                                | 5.68 us: 1.01x faster                                               |
| fannkuch                | 361 ms                                                                 | 358 ms: 1.01x faster                                                |
| pprint_pformat          | 1.39 sec                                                               | 1.38 sec: 1.01x faster                                              |
| aiohttp                 | 1.00 ms                                                                | 997 us: 1.01x faster                                                |
| chameleon               | 6.35 ms                                                                | 6.31 ms: 1.01x faster                                               |
| deepcopy_reduce         | 2.96 us                                                                | 2.94 us: 1.01x faster                                               |
| sympy_str               | 272 ms                                                                 | 270 ms: 1.01x faster                                                |
| go                      | 135 ms                                                                 | 134 ms: 1.01x faster                                                |
| pickle_list             | 4.26 us                                                                | 4.24 us: 1.01x faster                                               |
| unpickle_pure_python    | 198 us                                                                 | 197 us: 1.00x faster                                                |
| sympy_integrate         | 19.8 ms                                                                | 19.8 ms: 1.00x faster                                               |
| sqlglot_optimize        | 51.3 ms                                                                | 51.2 ms: 1.00x faster                                               |
| python_startup_no_site  | 6.48 ms                                                                | 6.49 ms: 1.00x slower                                               |
| xml_etree_generate      | 77.3 ms                                                                | 77.6 ms: 1.00x slower                                               |
| python_startup          | 8.94 ms                                                                | 8.98 ms: 1.00x slower                                               |
| deepcopy                | 328 us                                                                 | 330 us: 1.01x slower                                                |
| sqlglot_transpile       | 1.70 ms                                                                | 1.71 ms: 1.01x slower                                               |
| create_gc_cycles        | 1.45 ms                                                                | 1.46 ms: 1.01x slower                                               |
| django_template         | 32.9 ms                                                                | 33.1 ms: 1.01x slower                                               |
| mako                    | 9.77 ms                                                                | 9.87 ms: 1.01x slower                                               |
| 2to3                    | 251 ms                                                                 | 253 ms: 1.01x slower                                                |
| sqlite_synth            | 2.57 us                                                                | 2.60 us: 1.01x slower                                               |
| bench_thread_pool       | 780 us                                                                 | 790 us: 1.01x slower                                                |
| generators              | 77.0 ms                                                                | 78.0 ms: 1.01x slower                                               |
| nbody                   | 94.2 ms                                                                | 95.5 ms: 1.01x slower                                               |
| genshi_text             | 20.7 ms                                                                | 21.0 ms: 1.01x slower                                               |
| xml_etree_parse         | 147 ms                                                                 | 149 ms: 1.01x slower                                                |
| raytrace                | 284 ms                                                                 | 289 ms: 1.02x slower                                                |
| mdp                     | 2.58 sec                                                               | 2.62 sec: 1.02x slower                                              |
| genshi_xml              | 46.7 ms                                                                | 47.6 ms: 1.02x slower                                               |
| scimark_monte_carlo     | 65.4 ms                                                                | 66.7 ms: 1.02x slower                                               |
| scimark_fft             | 304 ms                                                                 | 311 ms: 1.02x slower                                                |
| json_dumps              | 9.37 ms                                                                | 9.58 ms: 1.02x slower                                               |
| deepcopy_memo           | 33.6 us                                                                | 34.6 us: 1.03x slower                                               |
| pycparser               | 1.08 sec                                                               | 1.12 sec: 1.03x slower                                              |
| regex_v8                | 21.1 ms                                                                | 21.7 ms: 1.03x slower                                               |
| scimark_sor             | 107 ms                                                                 | 111 ms: 1.04x slower                                                |
| crypto_pyaes            | 73.3 ms                                                                | 76.0 ms: 1.04x slower                                               |
| meteor_contest          | 103 ms                                                                 | 107 ms: 1.04x slower                                                |
| regex_dna               | 200 ms                                                                 | 209 ms: 1.04x slower                                                |
| pidigits                | 189 ms                                                                 | 199 ms: 1.05x slower                                                |
| gc_traversal            | 3.64 ms                                                                | 3.82 ms: 1.05x slower                                               |
| nqueens                 | 75.4 ms                                                                | 79.5 ms: 1.06x slower                                               |
| spectral_norm           | 98.3 ms                                                                | 105 ms: 1.06x slower                                                |
| regex_effbot            | 3.36 ms                                                                | 3.63 ms: 1.08x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (31): djangocms, html5lib, dask, json_loads, unpickle, telco, float, unpack_sequence, sympy_sum, tornado_http, sqlglot_normalize, pathlib, docutils, scimark_lu, dulwich_log, async_generators, thrift, mypy, bench_mp_pool, logging_format, async_tree_cpu_io_mixed, asyncio_tcp, async_tree_io, hexiom, xml_etree_process, sqlglot_parse, pickle_pure_python, deltablue, async_tree_none, json, async_tree_memoization
