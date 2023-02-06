
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 2e2a861
- commit date: 2023-02-06
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (4): chameleon, docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 72.3 ms                                                                | 73.2 ms: 1.01x slower                                               |
| nbody          | 94.2 ms                                                                | 95.9 ms: 1.02x slower                                               |
| pidigits       | 189 ms                                                                 | 203 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 128 ms: 1.02x faster                                                |
| regex_dna      | 200 ms                                                                 | 207 ms: 1.03x slower                                                |
| regex_effbot   | 3.36 ms                                                                | 3.51 ms: 1.04x slower                                               |
| regex_v8       | 21.1 ms                                                                | 22.4 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse  | 106 ms                                                                 | 103 ms: 1.03x faster                                                |
| json_loads           | 24.3 us                                                                | 23.5 us: 1.03x faster                                               |
| pickle_dict          | 32.2 us                                                                | 31.5 us: 1.02x faster                                               |
| pickle               | 10.3 us                                                                | 10.1 us: 1.02x faster                                               |
| pickle_list          | 4.26 us                                                                | 4.22 us: 1.01x faster                                               |
| unpickle_list        | 5.04 us                                                                | 4.98 us: 1.01x faster                                               |
| unpickle             | 13.2 us                                                                | 13.1 us: 1.01x faster                                               |
| json_dumps           | 9.37 ms                                                                | 9.34 ms: 1.00x faster                                               |
| unpickle_pure_python | 198 us                                                                 | 200 us: 1.01x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_process, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.94 ms                                                                | 8.96 ms: 1.00x slower                                               |
| python_startup_no_site | 6.48 ms                                                                | 6.49 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.77 ms                                                                | 9.46 ms: 1.03x faster                                               |
| django_template | 32.9 ms                                                                | 32.5 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines              | 25.8 ms                                                                | 24.5 ms: 1.05x faster                                               |
| async_tree_memoization  | 651 ms                                                                 | 624 ms: 1.04x faster                                                |
| telco                   | 6.40 ms                                                                | 6.17 ms: 1.04x faster                                               |
| xml_etree_iterparse     | 106 ms                                                                 | 103 ms: 1.03x faster                                                |
| scimark_sparse_mat_mult | 4.09 ms                                                                | 3.96 ms: 1.03x faster                                               |
| mako                    | 9.77 ms                                                                | 9.46 ms: 1.03x faster                                               |
| richards                | 43.9 ms                                                                | 42.6 ms: 1.03x faster                                               |
| json_loads              | 24.3 us                                                                | 23.5 us: 1.03x faster                                               |
| spectral_norm           | 98.3 ms                                                                | 95.5 ms: 1.03x faster                                               |
| json                    | 4.63 ms                                                                | 4.50 ms: 1.03x faster                                               |
| djangocms               | 32.6 us                                                                | 31.7 us: 1.03x faster                                               |
| coverage                | 99.1 ms                                                                | 96.8 ms: 1.02x faster                                               |
| pathlib                 | 17.9 ms                                                                | 17.5 ms: 1.02x faster                                               |
| pickle_dict             | 32.2 us                                                                | 31.5 us: 1.02x faster                                               |
| pprint_safe_repr        | 679 ms                                                                 | 666 ms: 1.02x faster                                                |
| pickle                  | 10.3 us                                                                | 10.1 us: 1.02x faster                                               |
| pprint_pformat          | 1.39 sec                                                               | 1.36 sec: 1.02x faster                                              |
| regex_compile           | 130 ms                                                                 | 128 ms: 1.02x faster                                                |
| dask                    | 501 ms                                                                 | 493 ms: 1.02x faster                                                |
| unpack_sequence         | 43.4 ns                                                                | 42.8 ns: 1.01x faster                                               |
| django_template         | 32.9 ms                                                                | 32.5 ms: 1.01x faster                                               |
| pyflate                 | 400 ms                                                                 | 395 ms: 1.01x faster                                                |
| logging_silent          | 93.3 ns                                                                | 92.2 ns: 1.01x faster                                               |
| gunicorn                | 1.08 ms                                                                | 1.07 ms: 1.01x faster                                               |
| pickle_list             | 4.26 us                                                                | 4.22 us: 1.01x faster                                               |
| unpickle_list           | 5.04 us                                                                | 4.98 us: 1.01x faster                                               |
| aiohttp                 | 1.00 ms                                                                | 994 us: 1.01x faster                                                |
| sqlglot_normalize       | 106 ms                                                                 | 105 ms: 1.01x faster                                                |
| scimark_fft             | 304 ms                                                                 | 302 ms: 1.01x faster                                                |
| scimark_sor             | 107 ms                                                                 | 106 ms: 1.01x faster                                                |
| logging_simple          | 5.73 us                                                                | 5.69 us: 1.01x faster                                               |
| sqlglot_optimize        | 51.3 ms                                                                | 50.9 ms: 1.01x faster                                               |
| sympy_str               | 272 ms                                                                 | 270 ms: 1.01x faster                                                |
| dulwich_log             | 62.8 ms                                                                | 62.4 ms: 1.01x faster                                               |
| sympy_integrate         | 19.8 ms                                                                | 19.7 ms: 1.01x faster                                               |
| unpickle                | 13.2 us                                                                | 13.1 us: 1.01x faster                                               |
| sympy_expand            | 458 ms                                                                 | 456 ms: 1.00x faster                                                |
| json_dumps              | 9.37 ms                                                                | 9.34 ms: 1.00x faster                                               |
| async_generators        | 353 ms                                                                 | 352 ms: 1.00x faster                                                |
| python_startup          | 8.94 ms                                                                | 8.96 ms: 1.00x slower                                               |
| python_startup_no_site  | 6.48 ms                                                                | 6.49 ms: 1.00x slower                                               |
| deepcopy_reduce         | 2.96 us                                                                | 2.97 us: 1.01x slower                                               |
| 2to3                    | 251 ms                                                                 | 252 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed | 751 ms                                                                 | 757 ms: 1.01x slower                                                |
| deltablue               | 3.18 ms                                                                | 3.21 ms: 1.01x slower                                               |
| create_gc_cycles        | 1.45 ms                                                                | 1.47 ms: 1.01x slower                                               |
| hexiom                  | 5.95 ms                                                                | 6.02 ms: 1.01x slower                                               |
| meteor_contest          | 103 ms                                                                 | 105 ms: 1.01x slower                                                |
| unpickle_pure_python    | 198 us                                                                 | 200 us: 1.01x slower                                                |
| float                   | 72.3 ms                                                                | 73.2 ms: 1.01x slower                                               |
| sqlite_synth            | 2.57 us                                                                | 2.61 us: 1.01x slower                                               |
| deepcopy                | 328 us                                                                 | 334 us: 1.02x slower                                                |
| nbody                   | 94.2 ms                                                                | 95.9 ms: 1.02x slower                                               |
| scimark_monte_carlo     | 65.4 ms                                                                | 66.6 ms: 1.02x slower                                               |
| generators              | 77.0 ms                                                                | 78.7 ms: 1.02x slower                                               |
| mdp                     | 2.58 sec                                                               | 2.65 sec: 1.03x slower                                              |
| crypto_pyaes            | 73.3 ms                                                                | 75.7 ms: 1.03x slower                                               |
| deepcopy_memo           | 33.6 us                                                                | 34.7 us: 1.03x slower                                               |
| regex_dna               | 200 ms                                                                 | 207 ms: 1.03x slower                                                |
| nqueens                 | 75.4 ms                                                                | 78.1 ms: 1.04x slower                                               |
| regex_effbot            | 3.36 ms                                                                | 3.51 ms: 1.04x slower                                               |
| pycparser               | 1.08 sec                                                               | 1.14 sec: 1.06x slower                                              |
| regex_v8                | 21.1 ms                                                                | 22.4 ms: 1.06x slower                                               |
| gc_traversal            | 3.64 ms                                                                | 3.87 ms: 1.07x slower                                               |
| pidigits                | 189 ms                                                                 | 203 ms: 1.07x slower                                                |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (26): html5lib, genshi_xml, thrift, pickle_pure_python, raytrace, tornado_http, bench_thread_pool, chameleon, mypy, scimark_lu, bench_mp_pool, sqlglot_parse, docutils, xml_etree_process, go, xml_etree_generate, asyncio_tcp, sqlglot_transpile, chaos, genshi_text, sympy_sum, xml_etree_parse, async_tree_io, logging_format, async_tree_none, fannkuch
