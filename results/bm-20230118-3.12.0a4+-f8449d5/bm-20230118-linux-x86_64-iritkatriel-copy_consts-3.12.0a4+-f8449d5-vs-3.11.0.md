
# Results vs. 3.11.0

- fork: iritkatriel
- ref: copy_consts
- machine: linux-x86_64
- commit hash: f8449d5
- commit date: 2023-01-18
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| chameleon      | 6.41 ms                                                | 6.53 ms: 1.02x slower                                              |
| html5lib       | 63.2 ms                                                | 61.5 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 73.5 ms: 1.04x faster                                              |
| nbody          | 95.0 ms                                                | 93.4 ms: 1.02x faster                                              |
| pidigits       | 199 ms                                                 | 190 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 132 ms: 1.03x faster                                               |
| regex_dna      | 203 ms                                                 | 201 ms: 1.01x faster                                               |
| regex_effbot   | 3.36 ms                                                | 3.41 ms: 1.02x slower                                              |
| regex_v8       | 22.3 ms                                                | 21.3 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.65 ms: 1.31x faster                                              |
| json_loads           | 26.2 us                                                | 24.1 us: 1.09x faster                                              |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                              |
| pickle_dict          | 31.4 us                                                | 30.6 us: 1.03x faster                                              |
| pickle_list          | 4.17 us                                                | 4.03 us: 1.04x faster                                              |
| pickle_pure_python   | 304 us                                                 | 293 us: 1.04x faster                                               |
| unpickle_list        | 4.95 us                                                | 4.97 us: 1.00x slower                                              |
| unpickle_pure_python | 225 us                                                 | 201 us: 1.12x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 150 ms: 1.06x faster                                               |
| xml_etree_generate   | 76.2 ms                                                | 78.6 ms: 1.03x slower                                              |
| xml_etree_process    | 53.8 ms                                                | 54.6 ms: 1.02x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.56 ms: 1.03x slower                                              |
| python_startup_no_site | 5.96 ms                                                | 6.10 ms: 1.02x slower                                              |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 32.5 ms                                                | 33.8 ms: 1.04x slower                                              |
| genshi_text     | 22.1 ms                                                | 20.8 ms: 1.06x faster                                              |
| genshi_xml      | 52.1 ms                                                | 48.1 ms: 1.08x faster                                              |
| mako            | 9.85 ms                                                | 9.67 ms: 1.02x faster                                              |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_generators        | 359 ms                                                 | 358 ms: 1.00x faster                                               |
| async_tree_cpu_io_mixed | 752 ms                                                 | 757 ms: 1.01x slower                                               |
| async_tree_io           | 1.31 sec                                               | 1.34 sec: 1.02x slower                                             |
| async_tree_memoization  | 625 ms                                                 | 674 ms: 1.08x slower                                               |
| chameleon               | 6.41 ms                                                | 6.53 ms: 1.02x slower                                              |
| bench_thread_pool       | 810 us                                                 | 797 us: 1.02x faster                                               |
| coroutines              | 26.1 ms                                                | 25.6 ms: 1.02x faster                                              |
| coverage                | 101 ms                                                 | 98.3 ms: 1.02x faster                                              |
| crypto_pyaes            | 73.9 ms                                                | 74.7 ms: 1.01x slower                                              |
| deepcopy                | 344 us                                                 | 341 us: 1.01x faster                                               |
| deepcopy_reduce         | 2.97 us                                                | 3.00 us: 1.01x slower                                              |
| deepcopy_memo           | 36.4 us                                                | 35.1 us: 1.04x faster                                              |
| deltablue               | 3.64 ms                                                | 3.38 ms: 1.08x faster                                              |
| django_template         | 32.5 ms                                                | 33.8 ms: 1.04x slower                                              |
| dulwich_log             | 63.9 ms                                                | 63.4 ms: 1.01x faster                                              |
| fannkuch                | 388 ms                                                 | 367 ms: 1.06x faster                                               |
| float                   | 76.3 ms                                                | 73.5 ms: 1.04x faster                                              |
| generators              | 72.2 ms                                                | 79.0 ms: 1.09x slower                                              |
| genshi_text             | 22.1 ms                                                | 20.8 ms: 1.06x faster                                              |
| genshi_xml              | 52.1 ms                                                | 48.1 ms: 1.08x faster                                              |
| go                      | 143 ms                                                 | 139 ms: 1.03x faster                                               |
| hexiom                  | 6.35 ms                                                | 6.18 ms: 1.03x faster                                              |
| html5lib                | 63.2 ms                                                | 61.5 ms: 1.03x faster                                              |
| json                    | 4.95 ms                                                | 4.70 ms: 1.05x faster                                              |
| json_dumps              | 12.7 ms                                                | 9.65 ms: 1.31x faster                                              |
| json_loads              | 26.2 us                                                | 24.1 us: 1.09x faster                                              |
| logging_format          | 6.62 us                                                | 6.66 us: 1.01x slower                                              |
| logging_silent          | 98.5 ns                                                | 95.0 ns: 1.04x faster                                              |
| mako                    | 9.85 ms                                                | 9.67 ms: 1.02x faster                                              |
| mdp                     | 2.62 sec                                               | 2.53 sec: 1.04x faster                                             |
| mypy                    | 669 ms                                                 | 855 ms: 1.28x slower                                               |
| nbody                   | 95.0 ms                                                | 93.4 ms: 1.02x faster                                              |
| nqueens                 | 85.0 ms                                                | 81.8 ms: 1.04x faster                                              |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                              |
| pickle_dict             | 31.4 us                                                | 30.6 us: 1.03x faster                                              |
| pickle_list             | 4.17 us                                                | 4.03 us: 1.04x faster                                              |
| pickle_pure_python      | 304 us                                                 | 293 us: 1.04x faster                                               |
| pidigits                | 199 ms                                                 | 190 ms: 1.05x faster                                               |
| pprint_safe_repr        | 691 ms                                                 | 700 ms: 1.01x slower                                               |
| pprint_pformat          | 1.44 sec                                               | 1.42 sec: 1.02x faster                                             |
| pycparser               | 1.17 sec                                               | 1.11 sec: 1.06x faster                                             |
| pyflate                 | 417 ms                                                 | 406 ms: 1.03x faster                                               |
| python_startup          | 8.36 ms                                                | 8.56 ms: 1.03x slower                                              |
| python_startup_no_site  | 5.96 ms                                                | 6.10 ms: 1.02x slower                                              |
| raytrace                | 290 ms                                                 | 293 ms: 1.01x slower                                               |
| regex_compile           | 136 ms                                                 | 132 ms: 1.03x faster                                               |
| regex_dna               | 203 ms                                                 | 201 ms: 1.01x faster                                               |
| regex_effbot            | 3.36 ms                                                | 3.41 ms: 1.02x slower                                              |
| regex_v8                | 22.3 ms                                                | 21.3 ms: 1.05x faster                                              |
| richards                | 46.2 ms                                                | 43.8 ms: 1.05x faster                                              |
| scimark_fft             | 329 ms                                                 | 314 ms: 1.05x faster                                               |
| scimark_lu              | 107 ms                                                 | 111 ms: 1.04x slower                                               |
| scimark_monte_carlo     | 68.3 ms                                                | 67.4 ms: 1.01x faster                                              |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.07x faster                                               |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.03 ms: 1.09x faster                                              |
| sqlglot_parse           | 1.37 ms                                                | 1.45 ms: 1.06x slower                                              |
| sqlglot_transpile       | 1.66 ms                                                | 1.75 ms: 1.06x slower                                              |
| sqlglot_optimize        | 53.0 ms                                                | 52.5 ms: 1.01x faster                                              |
| sqlglot_normalize       | 108 ms                                                 | 108 ms: 1.00x slower                                               |
| sqlite_synth            | 2.49 us                                                | 2.56 us: 1.03x slower                                              |
| sympy_expand            | 472 ms                                                 | 469 ms: 1.01x faster                                               |
| sympy_integrate         | 20.9 ms                                                | 21.9 ms: 1.05x slower                                              |
| sympy_sum               | 166 ms                                                 | 167 ms: 1.01x slower                                               |
| telco                   | 6.62 ms                                                | 6.31 ms: 1.05x faster                                              |
| unpack_sequence         | 43.4 ns                                                | 41.6 ns: 1.04x faster                                              |
| unpickle_list           | 4.95 us                                                | 4.97 us: 1.00x slower                                              |
| unpickle_pure_python    | 225 us                                                 | 201 us: 1.12x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 150 ms: 1.06x faster                                               |
| xml_etree_generate      | 76.2 ms                                                | 78.6 ms: 1.03x slower                                              |
| xml_etree_process       | 53.8 ms                                                | 54.6 ms: 1.02x slower                                              |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (13): 2to3, async_tree_none, chaos, bench_mp_pool, docutils, logging_simple, meteor_contest, pathlib, spectral_norm, sympy_str, thrift, unpickle, xml_etree_iterparse
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-f8449d5/bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
