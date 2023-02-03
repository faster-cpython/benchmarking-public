
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 6b312e0
- commit date: 2023-02-03
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.01x slower                                                |
| chameleon      | 6.35 ms                                                                | 6.28 ms: 1.01x faster                                               |
| html5lib       | 60.8 ms                                                                | 59.5 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                 | 191 ms: 1.01x slower                                                |
| nbody          | 94.2 ms                                                                | 96.7 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 128 ms: 1.02x faster                                                |
| regex_effbot   | 3.36 ms                                                                | 3.44 ms: 1.03x slower                                               |
| regex_dna      | 200 ms                                                                 | 208 ms: 1.04x slower                                                |
| regex_v8       | 21.1 ms                                                                | 22.6 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_list          | 4.26 us                                                                | 3.92 us: 1.09x faster                                               |
| pickle_dict          | 32.2 us                                                                | 29.8 us: 1.08x faster                                               |
| xml_etree_iterparse  | 106 ms                                                                 | 102 ms: 1.04x faster                                                |
| pickle               | 10.3 us                                                                | 10.0 us: 1.03x faster                                               |
| json_loads           | 24.3 us                                                                | 23.8 us: 1.02x faster                                               |
| unpickle             | 13.2 us                                                                | 13.1 us: 1.01x faster                                               |
| unpickle_list        | 5.04 us                                                                | 5.02 us: 1.00x faster                                               |
| xml_etree_generate   | 77.3 ms                                                                | 77.6 ms: 1.00x slower                                               |
| xml_etree_parse      | 147 ms                                                                 | 148 ms: 1.01x slower                                                |
| unpickle_pure_python | 198 us                                                                 | 200 us: 1.01x slower                                                |
| json_dumps           | 9.37 ms                                                                | 9.52 ms: 1.02x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (2): xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.48 ms                                                                | 6.48 ms: 1.00x slower                                               |
| python_startup         | 8.94 ms                                                                | 8.96 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.77 ms                                                                | 9.58 ms: 1.02x faster                                               |
| django_template | 32.9 ms                                                                | 32.3 ms: 1.02x faster                                               |
| genshi_text     | 20.7 ms                                                                | 20.8 ms: 1.01x slower                                               |
| genshi_xml      | 46.7 ms                                                                | 47.9 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_list             | 4.26 us                                                                | 3.92 us: 1.09x faster                                               |
| pickle_dict             | 32.2 us                                                                | 29.8 us: 1.08x faster                                               |
| mdp                     | 2.58 sec                                                               | 2.45 sec: 1.05x faster                                              |
| richards                | 43.9 ms                                                                | 41.8 ms: 1.05x faster                                               |
| xml_etree_iterparse     | 106 ms                                                                 | 102 ms: 1.04x faster                                                |
| generators              | 77.0 ms                                                                | 74.5 ms: 1.03x faster                                               |
| gc_traversal            | 3.64 ms                                                                | 3.52 ms: 1.03x faster                                               |
| pickle                  | 10.3 us                                                                | 10.0 us: 1.03x faster                                               |
| scimark_sparse_mat_mult | 4.09 ms                                                                | 3.98 ms: 1.03x faster                                               |
| go                      | 135 ms                                                                 | 132 ms: 1.03x faster                                                |
| deepcopy_reduce         | 2.96 us                                                                | 2.88 us: 1.03x faster                                               |
| html5lib                | 60.8 ms                                                                | 59.5 ms: 1.02x faster                                               |
| async_generators        | 353 ms                                                                 | 346 ms: 1.02x faster                                                |
| mako                    | 9.77 ms                                                                | 9.58 ms: 1.02x faster                                               |
| django_template         | 32.9 ms                                                                | 32.3 ms: 1.02x faster                                               |
| chaos                   | 64.7 ms                                                                | 63.5 ms: 1.02x faster                                               |
| sqlite_synth            | 2.57 us                                                                | 2.53 us: 1.02x faster                                               |
| json_loads              | 24.3 us                                                                | 23.8 us: 1.02x faster                                               |
| regex_compile           | 130 ms                                                                 | 128 ms: 1.02x faster                                                |
| deepcopy                | 328 us                                                                 | 324 us: 1.01x faster                                                |
| pprint_pformat          | 1.39 sec                                                               | 1.38 sec: 1.01x faster                                              |
| chameleon               | 6.35 ms                                                                | 6.28 ms: 1.01x faster                                               |
| unpickle                | 13.2 us                                                                | 13.1 us: 1.01x faster                                               |
| aiohttp                 | 1.00 ms                                                                | 995 us: 1.01x faster                                                |
| dulwich_log             | 62.8 ms                                                                | 62.3 ms: 1.01x faster                                               |
| gunicorn                | 1.08 ms                                                                | 1.07 ms: 1.01x faster                                               |
| sqlglot_normalize       | 106 ms                                                                 | 105 ms: 1.01x faster                                                |
| sqlglot_optimize        | 51.3 ms                                                                | 51.0 ms: 1.01x faster                                               |
| pprint_safe_repr        | 679 ms                                                                 | 676 ms: 1.01x faster                                                |
| sympy_str               | 272 ms                                                                 | 270 ms: 1.00x faster                                                |
| sympy_integrate         | 19.8 ms                                                                | 19.7 ms: 1.00x faster                                               |
| sympy_sum               | 156 ms                                                                 | 155 ms: 1.00x faster                                                |
| sqlglot_parse           | 1.40 ms                                                                | 1.40 ms: 1.00x faster                                               |
| unpickle_list           | 5.04 us                                                                | 5.02 us: 1.00x faster                                               |
| python_startup_no_site  | 6.48 ms                                                                | 6.48 ms: 1.00x slower                                               |
| python_startup          | 8.94 ms                                                                | 8.96 ms: 1.00x slower                                               |
| xml_etree_generate      | 77.3 ms                                                                | 77.6 ms: 1.00x slower                                               |
| 2to3                    | 251 ms                                                                 | 252 ms: 1.01x slower                                                |
| bench_thread_pool       | 780 us                                                                 | 784 us: 1.01x slower                                                |
| genshi_text             | 20.7 ms                                                                | 20.8 ms: 1.01x slower                                               |
| thrift                  | 742 us                                                                 | 747 us: 1.01x slower                                                |
| pidigits                | 189 ms                                                                 | 191 ms: 1.01x slower                                                |
| xml_etree_parse         | 147 ms                                                                 | 148 ms: 1.01x slower                                                |
| asyncio_tcp             | 493 ms                                                                 | 496 ms: 1.01x slower                                                |
| create_gc_cycles        | 1.45 ms                                                                | 1.46 ms: 1.01x slower                                               |
| coroutines              | 25.8 ms                                                                | 26.0 ms: 1.01x slower                                               |
| unpickle_pure_python    | 198 us                                                                 | 200 us: 1.01x slower                                                |
| telco                   | 6.40 ms                                                                | 6.46 ms: 1.01x slower                                               |
| async_tree_io           | 1.31 sec                                                               | 1.32 sec: 1.01x slower                                              |
| async_tree_cpu_io_mixed | 751 ms                                                                 | 760 ms: 1.01x slower                                                |
| scimark_fft             | 304 ms                                                                 | 308 ms: 1.01x slower                                                |
| async_tree_none         | 522 ms                                                                 | 528 ms: 1.01x slower                                                |
| meteor_contest          | 103 ms                                                                 | 105 ms: 1.01x slower                                                |
| json_dumps              | 9.37 ms                                                                | 9.52 ms: 1.02x slower                                               |
| scimark_sor             | 107 ms                                                                 | 109 ms: 1.02x slower                                                |
| deepcopy_memo           | 33.6 us                                                                | 34.2 us: 1.02x slower                                               |
| scimark_monte_carlo     | 65.4 ms                                                                | 66.5 ms: 1.02x slower                                               |
| scimark_lu              | 106 ms                                                                 | 108 ms: 1.02x slower                                                |
| regex_effbot            | 3.36 ms                                                                | 3.44 ms: 1.03x slower                                               |
| genshi_xml              | 46.7 ms                                                                | 47.9 ms: 1.03x slower                                               |
| nbody                   | 94.2 ms                                                                | 96.7 ms: 1.03x slower                                               |
| pyflate                 | 400 ms                                                                 | 414 ms: 1.03x slower                                                |
| regex_dna               | 200 ms                                                                 | 208 ms: 1.04x slower                                                |
| fannkuch                | 361 ms                                                                 | 375 ms: 1.04x slower                                                |
| crypto_pyaes            | 73.3 ms                                                                | 76.4 ms: 1.04x slower                                               |
| spectral_norm           | 98.3 ms                                                                | 103 ms: 1.05x slower                                                |
| pycparser               | 1.08 sec                                                               | 1.13 sec: 1.05x slower                                              |
| regex_v8                | 21.1 ms                                                                | 22.6 ms: 1.07x slower                                               |
| unpack_sequence         | 43.4 ns                                                                | 46.9 ns: 1.08x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (22): djangocms, logging_silent, mypy, logging_simple, dask, sqlglot_transpile, sympy_expand, logging_format, hexiom, tornado_http, pathlib, xml_etree_process, deltablue, bench_mp_pool, raytrace, async_tree_memoization, pickle_pure_python, docutils, json, float, nqueens, coverage
