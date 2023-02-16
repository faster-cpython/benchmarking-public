
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 5609e30
- commit date: 2023-02-03
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                |
| chameleon      | 6.38 ms                                                | 6.21 ms: 1.03x faster                                               |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                              |
| html5lib       | 64.8 ms                                                | 59.9 ms: 1.08x faster                                               |
| tornado_http   | 96.5 ms                                                | 93.6 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.1 ms: 1.05x faster                                               |
| pidigits       | 197 ms                                                 | 190 ms: 1.03x faster                                                |
| nbody          | 90.0 ms                                                | 96.7 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.00x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                                |
| regex_dna      | 203 ms                                                 | 217 ms: 1.07x slower                                                |
| regex_effbot   | 3.46 ms                                                | 3.77 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x slower                                                        |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.41 ms: 1.31x faster                                               |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                |
| json_loads           | 26.1 us                                                | 23.4 us: 1.12x faster                                               |
| xml_etree_parse      | 160 ms                                                 | 145 ms: 1.10x faster                                                |
| pickle_pure_python   | 308 us                                                 | 284 us: 1.09x faster                                                |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| xml_etree_process    | 53.7 ms                                                | 53.4 ms: 1.00x faster                                               |
| pickle_list          | 4.14 us                                                | 4.22 us: 1.02x slower                                               |
| pickle_dict          | 31.2 us                                                | 31.8 us: 1.02x slower                                               |
| xml_etree_generate   | 75.9 ms                                                | 77.5 ms: 1.02x slower                                               |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                               |
| unpickle_list        | 4.99 us                                                | 5.15 us: 1.03x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.97 ms: 1.05x slower                                               |
| python_startup_no_site | 6.04 ms                                                | 6.50 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.5 ms: 1.08x faster                                               |
| mako            | 9.83 ms                                                | 9.47 ms: 1.04x faster                                               |
| genshi_text     | 21.5 ms                                                | 21.3 ms: 1.01x faster                                               |
| django_template | 32.3 ms                                                | 32.1 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 492 ms: 1.80x faster                                                |
| json_dumps              | 12.4 ms                                                | 9.41 ms: 1.31x faster                                               |
| deltablue               | 3.66 ms                                                | 3.18 ms: 1.15x faster                                               |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.04 ms: 1.13x faster                                               |
| json_loads              | 26.1 us                                                | 23.4 us: 1.12x faster                                               |
| richards                | 46.1 ms                                                | 41.9 ms: 1.10x faster                                               |
| xml_etree_parse         | 160 ms                                                 | 145 ms: 1.10x faster                                                |
| pickle_pure_python      | 308 us                                                 | 284 us: 1.09x faster                                                |
| nqueens                 | 83.8 ms                                                | 77.2 ms: 1.09x faster                                               |
| genshi_xml              | 51.4 ms                                                | 47.5 ms: 1.08x faster                                               |
| coroutines              | 26.2 ms                                                | 24.1 ms: 1.08x faster                                               |
| html5lib                | 64.8 ms                                                | 59.9 ms: 1.08x faster                                               |
| sympy_str               | 291 ms                                                 | 270 ms: 1.08x faster                                                |
| chaos                   | 68.7 ms                                                | 63.7 ms: 1.08x faster                                               |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                                |
| scimark_fft             | 325 ms                                                 | 304 ms: 1.07x faster                                                |
| hexiom                  | 6.34 ms                                                | 5.93 ms: 1.07x faster                                               |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                |
| logging_simple          | 6.02 us                                                | 5.67 us: 1.06x faster                                               |
| json                    | 4.87 ms                                                | 4.59 ms: 1.06x faster                                               |
| go                      | 140 ms                                                 | 132 ms: 1.06x faster                                                |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                               |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                                |
| deepcopy_memo           | 35.8 us                                                | 33.9 us: 1.06x faster                                               |
| logging_silent          | 98.0 ns                                                | 92.8 ns: 1.06x faster                                               |
| aiohttp                 | 1.05 ms                                                | 995 us: 1.05x faster                                                |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                              |
| bench_thread_pool       | 817 us                                                 | 777 us: 1.05x faster                                                |
| float                   | 76.8 ms                                                | 73.1 ms: 1.05x faster                                               |
| deepcopy                | 341 us                                                 | 326 us: 1.05x faster                                                |
| unpack_sequence         | 44.5 ns                                                | 42.5 ns: 1.05x faster                                               |
| coverage                | 99.3 ms                                                | 94.8 ms: 1.05x faster                                               |
| fannkuch                | 384 ms                                                 | 368 ms: 1.05x faster                                                |
| mdp                     | 2.63 sec                                               | 2.51 sec: 1.05x faster                                              |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.05x faster                                                |
| pycparser               | 1.19 sec                                               | 1.14 sec: 1.04x faster                                              |
| pprint_safe_repr        | 706 ms                                                 | 676 ms: 1.04x faster                                                |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                               |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                              |
| mako                    | 9.83 ms                                                | 9.47 ms: 1.04x faster                                               |
| pidigits                | 197 ms                                                 | 190 ms: 1.03x faster                                                |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                |
| logging_format          | 6.48 us                                                | 6.26 us: 1.03x faster                                               |
| deepcopy_reduce         | 3.02 us                                                | 2.92 us: 1.03x faster                                               |
| sqlglot_optimize        | 52.7 ms                                                | 51.1 ms: 1.03x faster                                               |
| tornado_http            | 96.5 ms                                                | 93.6 ms: 1.03x faster                                               |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                               |
| chameleon               | 6.38 ms                                                | 6.21 ms: 1.03x faster                                               |
| thrift                  | 760 us                                                 | 740 us: 1.03x faster                                                |
| raytrace                | 291 ms                                                 | 284 ms: 1.03x faster                                                |
| dulwich_log             | 64.0 ms                                                | 62.4 ms: 1.02x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| pyflate                 | 419 ms                                                 | 410 ms: 1.02x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                               |
| spectral_norm           | 98.1 ms                                                | 96.6 ms: 1.02x faster                                               |
| scimark_monte_carlo     | 68.0 ms                                                | 67.0 ms: 1.01x faster                                               |
| genshi_text             | 21.5 ms                                                | 21.3 ms: 1.01x faster                                               |
| django_template         | 32.3 ms                                                | 32.1 ms: 1.01x faster                                               |
| async_generators        | 356 ms                                                 | 353 ms: 1.01x faster                                                |
| meteor_contest          | 104 ms                                                 | 104 ms: 1.01x faster                                                |
| xml_etree_process       | 53.7 ms                                                | 53.4 ms: 1.00x faster                                               |
| crypto_pyaes            | 75.7 ms                                                | 76.1 ms: 1.00x slower                                               |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                              |
| pickle_list             | 4.14 us                                                | 4.22 us: 1.02x slower                                               |
| pickle_dict             | 31.2 us                                                | 31.8 us: 1.02x slower                                               |
| xml_etree_generate      | 75.9 ms                                                | 77.5 ms: 1.02x slower                                               |
| sqlite_synth            | 2.48 us                                                | 2.54 us: 1.02x slower                                               |
| sqlglot_transpile       | 1.65 ms                                                | 1.69 ms: 1.02x slower                                               |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                               |
| async_tree_cpu_io_mixed | 736 ms                                                 | 754 ms: 1.03x slower                                                |
| gc_traversal            | 3.82 ms                                                | 3.93 ms: 1.03x slower                                               |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                               |
| unpickle_list           | 4.99 us                                                | 5.15 us: 1.03x slower                                               |
| python_startup          | 8.58 ms                                                | 8.97 ms: 1.05x slower                                               |
| async_tree_memoization  | 624 ms                                                 | 660 ms: 1.06x slower                                                |
| generators              | 73.5 ms                                                | 77.7 ms: 1.06x slower                                               |
| regex_dna               | 203 ms                                                 | 217 ms: 1.07x slower                                                |
| nbody                   | 90.0 ms                                                | 96.7 ms: 1.07x slower                                               |
| python_startup_no_site  | 6.04 ms                                                | 6.50 ms: 1.08x slower                                               |
| regex_effbot            | 3.46 ms                                                | 3.77 ms: 1.09x slower                                               |
| dask                    | 365 ms                                                 | 494 ms: 1.35x slower                                                |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (7): unpickle, async_tree_none, regex_v8, scimark_lu, telco, bench_mp_pool, djangocms
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230203-3.12.0a4+-5609e30/bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30.json: mypy
