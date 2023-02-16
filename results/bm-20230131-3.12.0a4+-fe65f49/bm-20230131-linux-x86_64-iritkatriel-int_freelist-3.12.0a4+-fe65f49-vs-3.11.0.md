
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: fe65f49
- commit date: 2023-01-31
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.03x faster                                                |
| chameleon      | 6.38 ms                                                | 6.29 ms: 1.01x faster                                               |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.04x faster                                              |
| html5lib       | 64.8 ms                                                | 61.9 ms: 1.05x faster                                               |
| tornado_http   | 96.5 ms                                                | 95.0 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.8 ms: 1.06x faster                                               |
| pidigits       | 197 ms                                                 | 192 ms: 1.03x faster                                                |
| nbody          | 90.0 ms                                                | 97.9 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.00x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                |
| regex_v8       | 22.2 ms                                                | 21.7 ms: 1.02x faster                                               |
| regex_effbot   | 3.46 ms                                                | 3.50 ms: 1.01x slower                                               |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.35 ms: 1.32x faster                                               |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                                |
| pickle_pure_python   | 308 us                                                 | 285 us: 1.08x faster                                                |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                |
| json_loads           | 26.1 us                                                | 24.6 us: 1.06x faster                                               |
| pickle_dict          | 31.2 us                                                | 30.5 us: 1.02x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| unpickle_list        | 4.99 us                                                | 4.90 us: 1.02x faster                                               |
| pickle_list          | 4.14 us                                                | 4.09 us: 1.01x faster                                               |
| xml_etree_process    | 53.7 ms                                                | 53.2 ms: 1.01x faster                                               |
| unpickle             | 13.3 us                                                | 13.6 us: 1.02x slower                                               |
| xml_etree_generate   | 75.9 ms                                                | 77.7 ms: 1.02x slower                                               |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.94 ms: 1.04x slower                                               |
| python_startup_no_site | 6.04 ms                                                | 6.47 ms: 1.07x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.0 ms: 1.10x faster                                               |
| genshi_text     | 21.5 ms                                                | 20.2 ms: 1.07x faster                                               |
| django_template | 32.3 ms                                                | 32.6 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 496 ms: 1.78x faster                                                |
| json_dumps              | 12.4 ms                                                | 9.35 ms: 1.32x faster                                               |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                                |
| deltablue               | 3.66 ms                                                | 3.24 ms: 1.13x faster                                               |
| genshi_xml              | 51.4 ms                                                | 47.0 ms: 1.10x faster                                               |
| pickle_pure_python      | 308 us                                                 | 285 us: 1.08x faster                                                |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                |
| sympy_str               | 291 ms                                                 | 270 ms: 1.08x faster                                                |
| logging_silent          | 98.0 ns                                                | 91.3 ns: 1.07x faster                                               |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                |
| genshi_text             | 21.5 ms                                                | 20.2 ms: 1.07x faster                                               |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                |
| pycparser               | 1.19 sec                                               | 1.12 sec: 1.06x faster                                              |
| json_loads              | 26.1 us                                                | 24.6 us: 1.06x faster                                               |
| hexiom                  | 6.34 ms                                                | 5.99 ms: 1.06x faster                                               |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                               |
| nqueens                 | 83.8 ms                                                | 79.3 ms: 1.06x faster                                               |
| float                   | 76.8 ms                                                | 72.8 ms: 1.06x faster                                               |
| logging_simple          | 6.02 us                                                | 5.72 us: 1.05x faster                                               |
| richards                | 46.1 ms                                                | 43.8 ms: 1.05x faster                                               |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                                |
| html5lib                | 64.8 ms                                                | 61.9 ms: 1.05x faster                                               |
| create_gc_cycles        | 1.52 ms                                                | 1.45 ms: 1.05x faster                                               |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                               |
| coverage                | 99.3 ms                                                | 95.1 ms: 1.04x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.04x faster                                              |
| fannkuch                | 384 ms                                                 | 369 ms: 1.04x faster                                                |
| json                    | 4.87 ms                                                | 4.67 ms: 1.04x faster                                               |
| pprint_safe_repr        | 706 ms                                                 | 678 ms: 1.04x faster                                                |
| sqlglot_optimize        | 52.7 ms                                                | 50.7 ms: 1.04x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                               |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.04x faster                                              |
| deepcopy                | 341 us                                                 | 330 us: 1.04x faster                                                |
| unpack_sequence         | 44.5 ns                                                | 43.0 ns: 1.04x faster                                               |
| chaos                   | 68.7 ms                                                | 66.4 ms: 1.03x faster                                               |
| thrift                  | 760 us                                                 | 735 us: 1.03x faster                                                |
| deepcopy_memo           | 35.8 us                                                | 34.7 us: 1.03x faster                                               |
| logging_format          | 6.48 us                                                | 6.29 us: 1.03x faster                                               |
| pidigits                | 197 ms                                                 | 192 ms: 1.03x faster                                                |
| 2to3                    | 259 ms                                                 | 253 ms: 1.03x faster                                                |
| coroutines              | 26.2 ms                                                | 25.5 ms: 1.03x faster                                               |
| regex_v8                | 22.2 ms                                                | 21.7 ms: 1.02x faster                                               |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.48 ms: 1.02x faster                                               |
| pickle_dict             | 31.2 us                                                | 30.5 us: 1.02x faster                                               |
| bench_thread_pool       | 817 us                                                 | 800 us: 1.02x faster                                                |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| deepcopy_reduce         | 3.02 us                                                | 2.96 us: 1.02x faster                                               |
| unpickle_list           | 4.99 us                                                | 4.90 us: 1.02x faster                                               |
| tornado_http            | 96.5 ms                                                | 95.0 ms: 1.02x faster                                               |
| go                      | 140 ms                                                 | 138 ms: 1.01x faster                                                |
| chameleon               | 6.38 ms                                                | 6.29 ms: 1.01x faster                                               |
| pickle_list             | 4.14 us                                                | 4.09 us: 1.01x faster                                               |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                                |
| xml_etree_process       | 53.7 ms                                                | 53.2 ms: 1.01x faster                                               |
| gc_traversal            | 3.82 ms                                                | 3.82 ms: 1.00x slower                                               |
| dulwich_log             | 64.0 ms                                                | 64.3 ms: 1.00x slower                                               |
| meteor_contest          | 104 ms                                                 | 105 ms: 1.01x slower                                                |
| django_template         | 32.3 ms                                                | 32.6 ms: 1.01x slower                                               |
| regex_effbot            | 3.46 ms                                                | 3.50 ms: 1.01x slower                                               |
| async_tree_memoization  | 624 ms                                                 | 635 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed | 736 ms                                                 | 752 ms: 1.02x slower                                                |
| unpickle                | 13.3 us                                                | 13.6 us: 1.02x slower                                               |
| xml_etree_generate      | 75.9 ms                                                | 77.7 ms: 1.02x slower                                               |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                |
| mdp                     | 2.63 sec                                               | 2.72 sec: 1.03x slower                                              |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                               |
| python_startup          | 8.58 ms                                                | 8.94 ms: 1.04x slower                                               |
| async_generators        | 356 ms                                                 | 372 ms: 1.05x slower                                                |
| pathlib                 | 18.1 ms                                                | 19.0 ms: 1.05x slower                                               |
| python_startup_no_site  | 6.04 ms                                                | 6.47 ms: 1.07x slower                                               |
| sqlglot_transpile       | 1.65 ms                                                | 1.78 ms: 1.08x slower                                               |
| sqlglot_parse           | 1.36 ms                                                | 1.48 ms: 1.08x slower                                               |
| nbody                   | 90.0 ms                                                | 97.9 ms: 1.09x slower                                               |
| scimark_sor             | 115 ms                                                 | 125 ms: 1.09x slower                                                |
| sqlite_synth            | 2.48 us                                                | 2.70 us: 1.09x slower                                               |
| generators              | 73.5 ms                                                | 81.0 ms: 1.10x slower                                               |
| pyflate                 | 419 ms                                                 | 467 ms: 1.12x slower                                                |
| crypto_pyaes            | 75.7 ms                                                | 89.5 ms: 1.18x slower                                               |
| scimark_fft             | 325 ms                                                 | 397 ms: 1.22x slower                                                |
| spectral_norm           | 98.1 ms                                                | 141 ms: 1.44x slower                                                |
| dask                    | 365 ms                                                 | 526 ms: 1.44x slower                                                |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (8): telco, async_tree_none, scimark_monte_carlo, mako, bench_mp_pool, raytrace, async_tree_io, djangocms
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230131-3.12.0a4+-fe65f49/bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49.json: mypy
