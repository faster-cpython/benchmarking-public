
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 8a6e6a3
- commit date: 2023-01-31
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                              |
| html5lib       | 64.8 ms                                                | 61.6 ms: 1.05x faster                                               |
| tornado_http   | 96.5 ms                                                | 95.3 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.8 ms: 1.04x faster                                               |
| pidigits       | 197 ms                                                 | 192 ms: 1.03x faster                                                |
| nbody          | 90.0 ms                                                | 96.3 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.00x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.08x faster                                                |
| regex_v8       | 22.2 ms                                                | 21.2 ms: 1.05x faster                                               |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.50 ms: 1.30x faster                                               |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.15x faster                                                |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                |
| pickle_pure_python   | 308 us                                                 | 286 us: 1.08x faster                                                |
| json_loads           | 26.1 us                                                | 24.7 us: 1.06x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| unpickle_list        | 4.99 us                                                | 4.93 us: 1.01x faster                                               |
| pickle_dict          | 31.2 us                                                | 31.8 us: 1.02x slower                                               |
| xml_etree_generate   | 75.9 ms                                                | 77.4 ms: 1.02x slower                                               |
| pickle_list          | 4.14 us                                                | 4.23 us: 1.02x slower                                               |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                               |
| unpickle             | 13.3 us                                                | 14.0 us: 1.06x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.97 ms: 1.05x slower                                               |
| python_startup_no_site | 6.04 ms                                                | 6.49 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.4 ms: 1.09x faster                                               |
| genshi_text     | 21.5 ms                                                | 20.6 ms: 1.04x faster                                               |
| mako            | 9.83 ms                                                | 9.80 ms: 1.00x faster                                               |
| django_template | 32.3 ms                                                | 33.1 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 498 ms: 1.77x faster                                                |
| json_dumps              | 12.4 ms                                                | 9.50 ms: 1.30x faster                                               |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.15x faster                                                |
| deltablue               | 3.66 ms                                                | 3.25 ms: 1.13x faster                                               |
| nqueens                 | 83.8 ms                                                | 76.2 ms: 1.10x faster                                               |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                |
| genshi_xml              | 51.4 ms                                                | 47.4 ms: 1.09x faster                                               |
| pickle_pure_python      | 308 us                                                 | 286 us: 1.08x faster                                                |
| regex_compile           | 136 ms                                                 | 127 ms: 1.08x faster                                                |
| sympy_str               | 291 ms                                                 | 271 ms: 1.07x faster                                                |
| fannkuch                | 384 ms                                                 | 360 ms: 1.07x faster                                                |
| richards                | 46.1 ms                                                | 43.2 ms: 1.07x faster                                               |
| chaos                   | 68.7 ms                                                | 64.4 ms: 1.07x faster                                               |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.07x faster                                                |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.07x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                              |
| pycparser               | 1.19 sec                                               | 1.12 sec: 1.06x faster                                              |
| logging_silent          | 98.0 ns                                                | 92.4 ns: 1.06x faster                                               |
| hexiom                  | 6.34 ms                                                | 5.98 ms: 1.06x faster                                               |
| json_loads              | 26.1 us                                                | 24.7 us: 1.06x faster                                               |
| pprint_safe_repr        | 706 ms                                                 | 669 ms: 1.06x faster                                                |
| html5lib                | 64.8 ms                                                | 61.6 ms: 1.05x faster                                               |
| regex_v8                | 22.2 ms                                                | 21.2 ms: 1.05x faster                                               |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.04x faster                                               |
| genshi_text             | 21.5 ms                                                | 20.6 ms: 1.04x faster                                               |
| unpack_sequence         | 44.5 ns                                                | 42.7 ns: 1.04x faster                                               |
| float                   | 76.8 ms                                                | 73.8 ms: 1.04x faster                                               |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                              |
| logging_simple          | 6.02 us                                                | 5.79 us: 1.04x faster                                               |
| json                    | 4.87 ms                                                | 4.69 ms: 1.04x faster                                               |
| sqlglot_optimize        | 52.7 ms                                                | 50.8 ms: 1.04x faster                                               |
| mdp                     | 2.63 sec                                               | 2.53 sec: 1.04x faster                                              |
| sympy_expand            | 475 ms                                                 | 459 ms: 1.04x faster                                                |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                               |
| coroutines              | 26.2 ms                                                | 25.3 ms: 1.03x faster                                               |
| coverage                | 99.3 ms                                                | 96.1 ms: 1.03x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                |
| deepcopy                | 341 us                                                 | 331 us: 1.03x faster                                                |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| pidigits                | 197 ms                                                 | 192 ms: 1.03x faster                                                |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.03x faster                                               |
| deepcopy_memo           | 35.8 us                                                | 34.9 us: 1.03x faster                                               |
| scimark_monte_carlo     | 68.0 ms                                                | 66.4 ms: 1.02x faster                                               |
| logging_format          | 6.48 us                                                | 6.35 us: 1.02x faster                                               |
| bench_thread_pool       | 817 us                                                 | 801 us: 1.02x faster                                                |
| tornado_http            | 96.5 ms                                                | 95.3 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| unpickle_list           | 4.99 us                                                | 4.93 us: 1.01x faster                                               |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                                |
| thrift                  | 760 us                                                 | 751 us: 1.01x faster                                                |
| mako                    | 9.83 ms                                                | 9.80 ms: 1.00x faster                                               |
| gc_traversal            | 3.82 ms                                                | 3.81 ms: 1.00x faster                                               |
| dulwich_log             | 64.0 ms                                                | 64.4 ms: 1.01x slower                                               |
| pickle_dict             | 31.2 us                                                | 31.8 us: 1.02x slower                                               |
| xml_etree_generate      | 75.9 ms                                                | 77.4 ms: 1.02x slower                                               |
| pickle_list             | 4.14 us                                                | 4.23 us: 1.02x slower                                               |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                              |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                                |
| django_template         | 32.3 ms                                                | 33.1 ms: 1.02x slower                                               |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                               |
| async_tree_cpu_io_mixed | 736 ms                                                 | 761 ms: 1.03x slower                                                |
| async_generators        | 356 ms                                                 | 369 ms: 1.04x slower                                                |
| python_startup          | 8.58 ms                                                | 8.97 ms: 1.05x slower                                               |
| pathlib                 | 18.1 ms                                                | 18.9 ms: 1.05x slower                                               |
| async_tree_memoization  | 624 ms                                                 | 659 ms: 1.06x slower                                                |
| unpickle                | 13.3 us                                                | 14.0 us: 1.06x slower                                               |
| scimark_sor             | 115 ms                                                 | 123 ms: 1.07x slower                                                |
| nbody                   | 90.0 ms                                                | 96.3 ms: 1.07x slower                                               |
| python_startup_no_site  | 6.04 ms                                                | 6.49 ms: 1.08x slower                                               |
| sqlglot_transpile       | 1.65 ms                                                | 1.78 ms: 1.08x slower                                               |
| sqlite_synth            | 2.48 us                                                | 2.68 us: 1.08x slower                                               |
| sqlglot_parse           | 1.36 ms                                                | 1.48 ms: 1.09x slower                                               |
| pyflate                 | 419 ms                                                 | 461 ms: 1.10x slower                                                |
| generators              | 73.5 ms                                                | 83.5 ms: 1.14x slower                                               |
| crypto_pyaes            | 75.7 ms                                                | 90.0 ms: 1.19x slower                                               |
| scimark_fft             | 325 ms                                                 | 390 ms: 1.20x slower                                                |
| spectral_norm           | 98.1 ms                                                | 138 ms: 1.41x slower                                                |
| dask                    | 365 ms                                                 | 525 ms: 1.44x slower                                                |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (11): scimark_sparse_mat_mult, meteor_contest, raytrace, chameleon, xml_etree_process, bench_mp_pool, deepcopy_reduce, djangocms, telco, async_tree_none, regex_effbot
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230131-3.12.0a4+-8a6e6a3/bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-8a6e6a3.json: mypy
