
# Results vs. 3.11.0

- fork: iritkatriel
- ref: copy_consts
- machine: linux-x86_64
- commit hash: f8449d5
- commit date: 2023-01-18
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 257 ms: 1.01x faster                                               |
| chameleon      | 6.38 ms                                                | 6.53 ms: 1.02x slower                                              |
| html5lib       | 64.8 ms                                                | 61.5 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.5 ms: 1.04x faster                                              |
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                               |
| nbody          | 90.0 ms                                                | 93.4 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.3 ms: 1.04x faster                                              |
| regex_compile  | 136 ms                                                 | 132 ms: 1.03x faster                                               |
| regex_effbot   | 3.46 ms                                                | 3.41 ms: 1.01x faster                                              |
| regex_dna      | 203 ms                                                 | 201 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.65 ms: 1.28x faster                                              |
| unpickle_pure_python | 227 us                                                 | 201 us: 1.13x faster                                               |
| json_loads           | 26.1 us                                                | 24.1 us: 1.08x faster                                              |
| xml_etree_parse      | 160 ms                                                 | 150 ms: 1.07x faster                                               |
| pickle_pure_python   | 308 us                                                 | 293 us: 1.05x faster                                               |
| pickle_list          | 4.14 us                                                | 4.03 us: 1.03x faster                                              |
| pickle_dict          | 31.2 us                                                | 30.6 us: 1.02x faster                                              |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                               |
| xml_etree_process    | 53.7 ms                                                | 54.6 ms: 1.02x slower                                              |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                              |
| xml_etree_generate   | 75.9 ms                                                | 78.6 ms: 1.04x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.56 ms: 1.00x faster                                              |
| python_startup_no_site | 6.04 ms                                                | 6.10 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.1 ms: 1.07x faster                                              |
| genshi_text     | 21.5 ms                                                | 20.8 ms: 1.03x faster                                              |
| mako            | 9.83 ms                                                | 9.67 ms: 1.02x faster                                              |
| django_template | 32.3 ms                                                | 33.8 ms: 1.05x slower                                              |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 511 ms: 1.73x faster                                               |
| json_dumps              | 12.4 ms                                                | 9.65 ms: 1.28x faster                                              |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.03 ms: 1.14x faster                                              |
| unpickle_pure_python    | 227 us                                                 | 201 us: 1.13x faster                                               |
| json_loads              | 26.1 us                                                | 24.1 us: 1.08x faster                                              |
| deltablue               | 3.66 ms                                                | 3.38 ms: 1.08x faster                                              |
| xml_etree_parse         | 160 ms                                                 | 150 ms: 1.07x faster                                               |
| genshi_xml              | 51.4 ms                                                | 48.1 ms: 1.07x faster                                              |
| pycparser               | 1.19 sec                                               | 1.11 sec: 1.07x faster                                             |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.07x faster                                               |
| unpack_sequence         | 44.5 ns                                                | 41.6 ns: 1.07x faster                                              |
| richards                | 46.1 ms                                                | 43.8 ms: 1.05x faster                                              |
| html5lib                | 64.8 ms                                                | 61.5 ms: 1.05x faster                                              |
| pickle_pure_python      | 308 us                                                 | 293 us: 1.05x faster                                               |
| fannkuch                | 384 ms                                                 | 367 ms: 1.05x faster                                               |
| float                   | 76.8 ms                                                | 73.5 ms: 1.04x faster                                              |
| regex_v8                | 22.2 ms                                                | 21.3 ms: 1.04x faster                                              |
| mdp                     | 2.63 sec                                               | 2.53 sec: 1.04x faster                                             |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                               |
| create_gc_cycles        | 1.52 ms                                                | 1.46 ms: 1.04x faster                                              |
| scimark_fft             | 325 ms                                                 | 314 ms: 1.04x faster                                               |
| json                    | 4.87 ms                                                | 4.70 ms: 1.03x faster                                              |
| genshi_text             | 21.5 ms                                                | 20.8 ms: 1.03x faster                                              |
| pyflate                 | 419 ms                                                 | 406 ms: 1.03x faster                                               |
| logging_silent          | 98.0 ns                                                | 95.0 ns: 1.03x faster                                              |
| regex_compile           | 136 ms                                                 | 132 ms: 1.03x faster                                               |
| pickle_list             | 4.14 us                                                | 4.03 us: 1.03x faster                                              |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.03x faster                                             |
| hexiom                  | 6.34 ms                                                | 6.18 ms: 1.03x faster                                              |
| bench_thread_pool       | 817 us                                                 | 797 us: 1.02x faster                                               |
| nqueens                 | 83.8 ms                                                | 81.8 ms: 1.02x faster                                              |
| coroutines              | 26.2 ms                                                | 25.6 ms: 1.02x faster                                              |
| deepcopy_memo           | 35.8 us                                                | 35.1 us: 1.02x faster                                              |
| telco                   | 6.43 ms                                                | 6.31 ms: 1.02x faster                                              |
| pickle_dict             | 31.2 us                                                | 30.6 us: 1.02x faster                                              |
| mako                    | 9.83 ms                                                | 9.67 ms: 1.02x faster                                              |
| thrift                  | 760 us                                                 | 749 us: 1.01x faster                                               |
| sympy_expand            | 475 ms                                                 | 469 ms: 1.01x faster                                               |
| regex_effbot            | 3.46 ms                                                | 3.41 ms: 1.01x faster                                              |
| crypto_pyaes            | 75.7 ms                                                | 74.7 ms: 1.01x faster                                              |
| regex_dna               | 203 ms                                                 | 201 ms: 1.01x faster                                               |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                               |
| sympy_str               | 291 ms                                                 | 288 ms: 1.01x faster                                               |
| coverage                | 99.3 ms                                                | 98.3 ms: 1.01x faster                                              |
| pprint_safe_repr        | 706 ms                                                 | 700 ms: 1.01x faster                                               |
| dulwich_log             | 64.0 ms                                                | 63.4 ms: 1.01x faster                                              |
| 2to3                    | 259 ms                                                 | 257 ms: 1.01x faster                                               |
| sqlglot_optimize        | 52.7 ms                                                | 52.5 ms: 1.00x faster                                              |
| python_startup          | 8.58 ms                                                | 8.56 ms: 1.00x faster                                              |
| sqlglot_normalize       | 108 ms                                                 | 108 ms: 1.01x slower                                               |
| async_generators        | 356 ms                                                 | 358 ms: 1.01x slower                                               |
| pathlib                 | 18.1 ms                                                | 18.2 ms: 1.01x slower                                              |
| sympy_sum               | 166 ms                                                 | 167 ms: 1.01x slower                                               |
| spectral_norm           | 98.1 ms                                                | 99.0 ms: 1.01x slower                                              |
| python_startup_no_site  | 6.04 ms                                                | 6.10 ms: 1.01x slower                                              |
| xml_etree_process       | 53.7 ms                                                | 54.6 ms: 1.02x slower                                              |
| chameleon               | 6.38 ms                                                | 6.53 ms: 1.02x slower                                              |
| async_tree_io           | 1.30 sec                                               | 1.34 sec: 1.03x slower                                             |
| logging_format          | 6.48 us                                                | 6.66 us: 1.03x slower                                              |
| async_tree_cpu_io_mixed | 736 ms                                                 | 757 ms: 1.03x slower                                               |
| scimark_lu              | 108 ms                                                 | 111 ms: 1.03x slower                                               |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                              |
| sqlite_synth            | 2.48 us                                                | 2.56 us: 1.03x slower                                              |
| xml_etree_generate      | 75.9 ms                                                | 78.6 ms: 1.04x slower                                              |
| nbody                   | 90.0 ms                                                | 93.4 ms: 1.04x slower                                              |
| sympy_integrate         | 21.0 ms                                                | 21.9 ms: 1.05x slower                                              |
| django_template         | 32.3 ms                                                | 33.8 ms: 1.05x slower                                              |
| sqlglot_transpile       | 1.65 ms                                                | 1.75 ms: 1.06x slower                                              |
| sqlglot_parse           | 1.36 ms                                                | 1.45 ms: 1.06x slower                                              |
| generators              | 73.5 ms                                                | 79.0 ms: 1.07x slower                                              |
| async_tree_memoization  | 624 ms                                                 | 674 ms: 1.08x slower                                               |
| gc_traversal            | 3.82 ms                                                | 4.30 ms: 1.12x slower                                              |
| dask                    | 365 ms                                                 | 516 ms: 1.41x slower                                               |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                       |

Benchmark hidden because not significant (13): scimark_monte_carlo, deepcopy_reduce, unpickle_list, docutils, deepcopy, chaos, meteor_contest, bench_mp_pool, unpickle, raytrace, logging_simple, async_tree_none, djangocms
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-f8449d5/bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5.json: mypy
