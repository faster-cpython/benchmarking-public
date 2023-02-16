
# Results vs. 3.11.0

- fork: python
- ref: v3.11.1
- machine: linux-x86_64
- commit hash: a7a450f
- commit date: 2022-12-06
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 258 ms: 1.00x faster                                   |
| chameleon      | 6.38 ms                                                | 6.63 ms: 1.04x slower                                  |
| docutils       | 2.60 sec                                               | 2.57 sec: 1.01x faster                                 |
| html5lib       | 64.8 ms                                                | 63.4 ms: 1.02x faster                                  |
| tornado_http   | 96.5 ms                                                | 99.8 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                   |
| float          | 76.8 ms                                                | 76.0 ms: 1.01x faster                                  |
| nbody          | 90.0 ms                                                | 95.4 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.31 ms: 1.04x faster                                  |
| regex_dna      | 203 ms                                                 | 200 ms: 1.02x faster                                   |
| regex_v8       | 22.2 ms                                                | 22.3 ms: 1.00x slower                                  |
| regex_compile  | 136 ms                                                 | 137 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_loads           | 26.1 us                                                | 24.0 us: 1.09x faster                                  |
| pickle               | 9.90 us                                                | 9.72 us: 1.02x faster                                  |
| xml_etree_parse      | 160 ms                                                 | 158 ms: 1.02x faster                                   |
| unpickle_list        | 4.99 us                                                | 4.95 us: 1.01x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| pickle_dict          | 31.2 us                                                | 31.1 us: 1.00x faster                                  |
| pickle_list          | 4.14 us                                                | 4.17 us: 1.01x slower                                  |
| unpickle_pure_python | 227 us                                                 | 229 us: 1.01x slower                                   |
| xml_etree_generate   | 75.9 ms                                                | 76.6 ms: 1.01x slower                                  |
| json_dumps           | 12.4 ms                                                | 12.6 ms: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (3): xml_etree_process, pickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.49 ms: 1.01x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 5.98 ms: 1.01x faster                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.83 ms                                                | 9.92 ms: 1.01x slower                                  |
| genshi_xml      | 51.4 ms                                                | 52.5 ms: 1.02x slower                                  |
| django_template | 32.3 ms                                                | 33.2 ms: 1.03x slower                                  |
| genshi_text     | 21.5 ms                                                | 22.1 ms: 1.03x slower                                  |
| Geometric mean  | (ref)                                                  | 1.02x slower                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_loads              | 26.1 us                                                | 24.0 us: 1.09x faster                                  |
| json                    | 4.87 ms                                                | 4.63 ms: 1.05x faster                                  |
| regex_effbot            | 3.46 ms                                                | 3.31 ms: 1.04x faster                                  |
| crypto_pyaes            | 75.7 ms                                                | 72.6 ms: 1.04x faster                                  |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                   |
| coroutines              | 26.2 ms                                                | 25.3 ms: 1.03x faster                                  |
| html5lib                | 64.8 ms                                                | 63.4 ms: 1.02x faster                                  |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.02x faster                                  |
| pickle                  | 9.90 us                                                | 9.72 us: 1.02x faster                                  |
| pycparser               | 1.19 sec                                               | 1.16 sec: 1.02x faster                                 |
| regex_dna               | 203 ms                                                 | 200 ms: 1.02x faster                                   |
| xml_etree_parse         | 160 ms                                                 | 158 ms: 1.02x faster                                   |
| docutils                | 2.60 sec                                               | 2.57 sec: 1.01x faster                                 |
| pprint_pformat          | 1.46 sec                                               | 1.44 sec: 1.01x faster                                 |
| logging_simple          | 6.02 us                                                | 5.95 us: 1.01x faster                                  |
| float                   | 76.8 ms                                                | 76.0 ms: 1.01x faster                                  |
| python_startup          | 8.58 ms                                                | 8.49 ms: 1.01x faster                                  |
| python_startup_no_site  | 6.04 ms                                                | 5.98 ms: 1.01x faster                                  |
| pprint_safe_repr        | 706 ms                                                 | 700 ms: 1.01x faster                                   |
| pyflate                 | 419 ms                                                 | 415 ms: 1.01x faster                                   |
| unpickle_list           | 4.99 us                                                | 4.95 us: 1.01x faster                                  |
| sympy_str               | 291 ms                                                 | 289 ms: 1.01x faster                                   |
| dulwich_log             | 64.0 ms                                                | 63.5 ms: 1.01x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| sympy_expand            | 475 ms                                                 | 472 ms: 1.01x faster                                   |
| flaskblogging           | 7.11 ms                                                | 7.07 ms: 1.01x faster                                  |
| go                      | 140 ms                                                 | 140 ms: 1.01x faster                                   |
| bench_thread_pool       | 817 us                                                 | 813 us: 1.00x faster                                   |
| sqlite_synth            | 2.48 us                                                | 2.47 us: 1.00x faster                                  |
| 2to3                    | 259 ms                                                 | 258 ms: 1.00x faster                                   |
| generators              | 73.5 ms                                                | 73.3 ms: 1.00x faster                                  |
| pickle_dict             | 31.2 us                                                | 31.1 us: 1.00x faster                                  |
| regex_v8                | 22.2 ms                                                | 22.3 ms: 1.00x slower                                  |
| mdp                     | 2.63 sec                                               | 2.64 sec: 1.00x slower                                 |
| deltablue               | 3.66 ms                                                | 3.67 ms: 1.00x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.00x slower                                 |
| regex_compile           | 136 ms                                                 | 137 ms: 1.01x slower                                   |
| pickle_list             | 4.14 us                                                | 4.17 us: 1.01x slower                                  |
| async_generators        | 356 ms                                                 | 358 ms: 1.01x slower                                   |
| scimark_fft             | 325 ms                                                 | 327 ms: 1.01x slower                                   |
| scimark_monte_carlo     | 68.0 ms                                                | 68.4 ms: 1.01x slower                                  |
| unpickle_pure_python    | 227 us                                                 | 229 us: 1.01x slower                                   |
| asyncio_tcp             | 883 ms                                                 | 889 ms: 1.01x slower                                   |
| sqlglot_normalize       | 108 ms                                                 | 108 ms: 1.01x slower                                   |
| gunicorn                | 1.12 ms                                                | 1.13 ms: 1.01x slower                                  |
| scimark_sor             | 115 ms                                                 | 116 ms: 1.01x slower                                   |
| thrift                  | 760 us                                                 | 765 us: 1.01x slower                                   |
| async_tree_cpu_io_mixed | 736 ms                                                 | 742 ms: 1.01x slower                                   |
| raytrace                | 291 ms                                                 | 294 ms: 1.01x slower                                   |
| mako                    | 9.83 ms                                                | 9.92 ms: 1.01x slower                                  |
| xml_etree_generate      | 75.9 ms                                                | 76.6 ms: 1.01x slower                                  |
| logging_format          | 6.48 us                                                | 6.54 us: 1.01x slower                                  |
| sqlglot_optimize        | 52.7 ms                                                | 53.3 ms: 1.01x slower                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.38 ms: 1.01x slower                                  |
| chaos                   | 68.7 ms                                                | 69.6 ms: 1.01x slower                                  |
| meteor_contest          | 104 ms                                                 | 106 ms: 1.01x slower                                   |
| nqueens                 | 83.8 ms                                                | 85.0 ms: 1.01x slower                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.68 ms: 1.02x slower                                  |
| richards                | 46.1 ms                                                | 46.9 ms: 1.02x slower                                  |
| hexiom                  | 6.34 ms                                                | 6.46 ms: 1.02x slower                                  |
| genshi_xml              | 51.4 ms                                                | 52.5 ms: 1.02x slower                                  |
| json_dumps              | 12.4 ms                                                | 12.6 ms: 1.02x slower                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 141 ms: 1.02x slower                                   |
| deepcopy                | 341 us                                                 | 349 us: 1.02x slower                                   |
| deepcopy_reduce         | 3.02 us                                                | 3.09 us: 1.02x slower                                  |
| django_template         | 32.3 ms                                                | 33.2 ms: 1.03x slower                                  |
| genshi_text             | 21.5 ms                                                | 22.1 ms: 1.03x slower                                  |
| spectral_norm           | 98.1 ms                                                | 101 ms: 1.03x slower                                   |
| tornado_http            | 96.5 ms                                                | 99.8 ms: 1.03x slower                                  |
| telco                   | 6.43 ms                                                | 6.66 ms: 1.04x slower                                  |
| deepcopy_memo           | 35.8 us                                                | 37.2 us: 1.04x slower                                  |
| chameleon               | 6.38 ms                                                | 6.63 ms: 1.04x slower                                  |
| logging_silent          | 98.0 ns                                                | 102 ns: 1.04x slower                                   |
| coverage                | 99.3 ms                                                | 104 ms: 1.05x slower                                   |
| nbody                   | 90.0 ms                                                | 95.4 ms: 1.06x slower                                  |
| gc_traversal            | 3.82 ms                                                | 4.26 ms: 1.11x slower                                  |
| Geometric mean          | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (19): async_tree_none, scimark_lu, sqlalchemy_imperative, pylint, fannkuch, dask, scimark_sparse_mat_mult, aiohttp, bench_mp_pool, sympy_sum, sympy_integrate, xml_etree_process, pathlib, mypy2, unpack_sequence, pickle_pure_python, async_tree_memoization, unpickle, djangocms
