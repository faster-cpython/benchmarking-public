
# Results vs. 3.11.0

- fork: python
- ref: v3.11.2
- machine: linux-x86_64
- commit hash: 878ead1
- commit date: 2023-02-07
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 257 ms: 1.01x faster                                   |
| chameleon      | 6.38 ms                                                | 6.49 ms: 1.02x slower                                  |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                   |
| nbody          | 90.0 ms                                                | 93.0 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 203 ms                                                 | 192 ms: 1.06x faster                                   |
| regex_v8       | 22.2 ms                                                | 21.3 ms: 1.04x faster                                  |
| regex_effbot   | 3.46 ms                                                | 3.39 ms: 1.02x faster                                  |
| regex_compile  | 136 ms                                                 | 138 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 308 us                                                 | 305 us: 1.01x faster                                   |
| unpickle_list        | 4.99 us                                                | 4.94 us: 1.01x faster                                  |
| xml_etree_process    | 53.7 ms                                                | 53.8 ms: 1.00x slower                                  |
| json_loads           | 26.1 us                                                | 26.2 us: 1.00x slower                                  |
| unpickle_pure_python | 227 us                                                 | 228 us: 1.00x slower                                   |
| json_dumps           | 12.4 ms                                                | 12.5 ms: 1.01x slower                                  |
| xml_etree_generate   | 75.9 ms                                                | 76.5 ms: 1.01x slower                                  |
| pickle_dict          | 31.2 us                                                | 31.4 us: 1.01x slower                                  |
| pickle               | 9.90 us                                                | 10.00 us: 1.01x slower                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_iterparse, unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.47 ms: 1.01x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 5.97 ms: 1.01x faster                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 21.5 ms                                                | 21.7 ms: 1.01x slower                                  |
| django_template | 32.3 ms                                                | 32.7 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pycparser               | 1.19 sec                                               | 1.11 sec: 1.07x faster                                 |
| regex_dna               | 203 ms                                                 | 192 ms: 1.06x faster                                   |
| regex_v8                | 22.2 ms                                                | 21.3 ms: 1.04x faster                                  |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                   |
| crypto_pyaes            | 75.7 ms                                                | 73.8 ms: 1.03x faster                                  |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                 |
| coroutines              | 26.2 ms                                                | 25.6 ms: 1.02x faster                                  |
| regex_effbot            | 3.46 ms                                                | 3.39 ms: 1.02x faster                                  |
| create_gc_cycles        | 1.52 ms                                                | 1.49 ms: 1.02x faster                                  |
| sympy_expand            | 475 ms                                                 | 468 ms: 1.02x faster                                   |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.01x faster                                  |
| pprint_safe_repr        | 706 ms                                                 | 697 ms: 1.01x faster                                   |
| flaskblogging           | 7.11 ms                                                | 7.02 ms: 1.01x faster                                  |
| python_startup          | 8.58 ms                                                | 8.47 ms: 1.01x faster                                  |
| richards                | 46.1 ms                                                | 45.6 ms: 1.01x faster                                  |
| sympy_str               | 291 ms                                                 | 288 ms: 1.01x faster                                   |
| python_startup_no_site  | 6.04 ms                                                | 5.97 ms: 1.01x faster                                  |
| pickle_pure_python      | 308 us                                                 | 305 us: 1.01x faster                                   |
| unpickle_list           | 4.99 us                                                | 4.94 us: 1.01x faster                                  |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                   |
| logging_simple          | 6.02 us                                                | 5.97 us: 1.01x faster                                  |
| 2to3                    | 259 ms                                                 | 257 ms: 1.01x faster                                   |
| nqueens                 | 83.8 ms                                                | 83.1 ms: 1.01x faster                                  |
| chaos                   | 68.7 ms                                                | 68.2 ms: 1.01x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.45 sec: 1.01x faster                                 |
| sqlite_synth            | 2.48 us                                                | 2.46 us: 1.01x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.8 ms: 1.01x faster                                  |
| bench_thread_pool       | 817 us                                                 | 812 us: 1.01x faster                                   |
| pyflate                 | 419 ms                                                 | 417 ms: 1.00x faster                                   |
| dulwich_log             | 64.0 ms                                                | 63.7 ms: 1.00x faster                                  |
| spectral_norm           | 98.1 ms                                                | 98.4 ms: 1.00x slower                                  |
| xml_etree_process       | 53.7 ms                                                | 53.8 ms: 1.00x slower                                  |
| json_loads              | 26.1 us                                                | 26.2 us: 1.00x slower                                  |
| hexiom                  | 6.34 ms                                                | 6.36 ms: 1.00x slower                                  |
| unpickle_pure_python    | 227 us                                                 | 228 us: 1.00x slower                                   |
| deltablue               | 3.66 ms                                                | 3.68 ms: 1.01x slower                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 740 ms: 1.01x slower                                   |
| go                      | 140 ms                                                 | 141 ms: 1.01x slower                                   |
| deepcopy_reduce         | 3.02 us                                                | 3.04 us: 1.01x slower                                  |
| genshi_text             | 21.5 ms                                                | 21.7 ms: 1.01x slower                                  |
| json_dumps              | 12.4 ms                                                | 12.5 ms: 1.01x slower                                  |
| generators              | 73.5 ms                                                | 74.1 ms: 1.01x slower                                  |
| xml_etree_generate      | 75.9 ms                                                | 76.5 ms: 1.01x slower                                  |
| pickle_dict             | 31.2 us                                                | 31.4 us: 1.01x slower                                  |
| sqlglot_normalize       | 108 ms                                                 | 109 ms: 1.01x slower                                   |
| pickle                  | 9.90 us                                                | 10.00 us: 1.01x slower                                 |
| sqlglot_transpile       | 1.65 ms                                                | 1.67 ms: 1.01x slower                                  |
| gunicorn                | 1.12 ms                                                | 1.13 ms: 1.01x slower                                  |
| sqlglot_optimize        | 52.7 ms                                                | 53.3 ms: 1.01x slower                                  |
| json                    | 4.87 ms                                                | 4.92 ms: 1.01x slower                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.38 ms: 1.01x slower                                  |
| regex_compile           | 136 ms                                                 | 138 ms: 1.01x slower                                   |
| django_template         | 32.3 ms                                                | 32.7 ms: 1.01x slower                                  |
| thrift                  | 760 us                                                 | 770 us: 1.01x slower                                   |
| chameleon               | 6.38 ms                                                | 6.49 ms: 1.02x slower                                  |
| logging_silent          | 98.0 ns                                                | 99.8 ns: 1.02x slower                                  |
| deepcopy                | 341 us                                                 | 348 us: 1.02x slower                                   |
| fannkuch                | 384 ms                                                 | 392 ms: 1.02x slower                                   |
| sqlalchemy_declarative  | 138 ms                                                 | 141 ms: 1.02x slower                                   |
| telco                   | 6.43 ms                                                | 6.59 ms: 1.03x slower                                  |
| deepcopy_memo           | 35.8 us                                                | 36.8 us: 1.03x slower                                  |
| pylint                  | 462 ms                                                 | 475 ms: 1.03x slower                                   |
| nbody                   | 90.0 ms                                                | 93.0 ms: 1.03x slower                                  |
| coverage                | 99.3 ms                                                | 103 ms: 1.04x slower                                   |
| mdp                     | 2.63 sec                                               | 2.77 sec: 1.05x slower                                 |
| gc_traversal            | 3.82 ms                                                | 4.15 ms: 1.09x slower                                  |
| unpack_sequence         | 44.5 ns                                                | 48.8 ns: 1.10x slower                                  |
| Geometric mean          | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (28): html5lib, djangocms, xml_etree_parse, async_tree_none, tornado_http, scimark_monte_carlo, async_tree_io, scimark_sor, float, xml_etree_iterparse, raytrace, dask, unpickle, aiohttp, mako, sympy_sum, bench_mp_pool, asyncio_tcp, meteor_contest, mypy2, genshi_xml, async_generators, logging_format, pickle_list, async_tree_memoization, scimark_fft, sqlalchemy_imperative, scimark_sparse_mat_mult
