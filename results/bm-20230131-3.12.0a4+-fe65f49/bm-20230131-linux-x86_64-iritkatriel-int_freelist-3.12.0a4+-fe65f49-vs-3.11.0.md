
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
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| chameleon      | 6.41 ms                                                | 6.36 ms: 1.01x faster                                               |
| docutils       | 2.60 sec                                               | 2.52 sec: 1.03x faster                                              |
| html5lib       | 63.2 ms                                                | 61.1 ms: 1.03x faster                                               |
| tornado_http   | 96.6 ms                                                | 94.6 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 192 ms: 1.04x faster                                                |
| float          | 76.3 ms                                                | 73.8 ms: 1.03x faster                                               |
| nbody          | 95.0 ms                                                | 98.3 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                |
| regex_v8       | 22.3 ms                                                | 22.5 ms: 1.01x slower                                               |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                                |
| regex_effbot   | 3.36 ms                                                | 3.54 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.47 ms: 1.34x faster                                               |
| unpickle_pure_python | 225 us                                                 | 198 us: 1.14x faster                                                |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| pickle_pure_python   | 304 us                                                 | 287 us: 1.06x faster                                                |
| json_loads           | 26.2 us                                                | 25.1 us: 1.05x faster                                               |
| xml_etree_process    | 53.8 ms                                                | 53.5 ms: 1.01x faster                                               |
| xml_etree_iterparse  | 103 ms                                                 | 103 ms: 1.00x slower                                                |
| pickle_dict          | 31.4 us                                                | 31.6 us: 1.01x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 77.4 ms: 1.02x slower                                               |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (3): unpickle_list, unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.96 ms: 1.07x slower                                               |
| python_startup_no_site | 5.96 ms                                                | 6.47 ms: 1.09x slower                                               |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 52.1 ms                                                | 47.2 ms: 1.10x faster                                               |
| genshi_text    | 22.1 ms                                                | 20.5 ms: 1.08x faster                                               |
| mako           | 9.85 ms                                                | 9.78 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.47 ms: 1.34x faster                                               |
| unpickle_pure_python    | 225 us                                                 | 198 us: 1.14x faster                                                |
| deltablue               | 3.64 ms                                                | 3.25 ms: 1.12x faster                                               |
| genshi_xml              | 52.1 ms                                                | 47.2 ms: 1.10x faster                                               |
| nqueens                 | 85.0 ms                                                | 77.9 ms: 1.09x faster                                               |
| genshi_text             | 22.1 ms                                                | 20.5 ms: 1.08x faster                                               |
| richards                | 46.2 ms                                                | 42.9 ms: 1.08x faster                                               |
| sympy_sum               | 166 ms                                                 | 154 ms: 1.08x faster                                                |
| logging_silent          | 98.5 ns                                                | 91.8 ns: 1.07x faster                                               |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                                |
| logging_simple          | 6.06 us                                                | 5.67 us: 1.07x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| sympy_str               | 287 ms                                                 | 270 ms: 1.06x faster                                                |
| logging_format          | 6.62 us                                                | 6.23 us: 1.06x faster                                               |
| sympy_integrate         | 20.9 ms                                                | 19.6 ms: 1.06x faster                                               |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                |
| pickle_pure_python      | 304 us                                                 | 287 us: 1.06x faster                                                |
| deepcopy                | 344 us                                                 | 325 us: 1.06x faster                                                |
| hexiom                  | 6.35 ms                                                | 6.03 ms: 1.05x faster                                               |
| deepcopy_memo           | 36.4 us                                                | 34.6 us: 1.05x faster                                               |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                               |
| json                    | 4.95 ms                                                | 4.73 ms: 1.05x faster                                               |
| sqlglot_optimize        | 53.0 ms                                                | 50.6 ms: 1.05x faster                                               |
| aiohttp                 | 1.05 ms                                                | 1000 us: 1.05x faster                                               |
| json_loads              | 26.2 us                                                | 25.1 us: 1.05x faster                                               |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.04x faster                                              |
| pidigits                | 199 ms                                                 | 192 ms: 1.04x faster                                                |
| sympy_expand            | 472 ms                                                 | 454 ms: 1.04x faster                                                |
| coroutines              | 26.1 ms                                                | 25.1 ms: 1.04x faster                                               |
| telco                   | 6.62 ms                                                | 6.37 ms: 1.04x faster                                               |
| float                   | 76.3 ms                                                | 73.8 ms: 1.03x faster                                               |
| html5lib                | 63.2 ms                                                | 61.1 ms: 1.03x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                |
| docutils                | 2.60 sec                                               | 2.52 sec: 1.03x faster                                              |
| thrift                  | 752 us                                                 | 731 us: 1.03x faster                                                |
| chaos                   | 68.6 ms                                                | 66.9 ms: 1.03x faster                                               |
| pprint_safe_repr        | 691 ms                                                 | 674 ms: 1.02x faster                                                |
| coverage                | 101 ms                                                 | 98.2 ms: 1.02x faster                                               |
| tornado_http            | 96.6 ms                                                | 94.6 ms: 1.02x faster                                               |
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| unpack_sequence         | 43.4 ns                                                | 42.6 ns: 1.02x faster                                               |
| mdp                     | 2.62 sec                                               | 2.57 sec: 1.02x faster                                              |
| go                      | 143 ms                                                 | 141 ms: 1.02x faster                                                |
| bench_thread_pool       | 810 us                                                 | 800 us: 1.01x faster                                                |
| async_tree_none         | 529 ms                                                 | 524 ms: 1.01x faster                                                |
| meteor_contest          | 105 ms                                                 | 104 ms: 1.01x faster                                                |
| raytrace                | 290 ms                                                 | 288 ms: 1.01x faster                                                |
| chameleon               | 6.41 ms                                                | 6.36 ms: 1.01x faster                                               |
| deepcopy_reduce         | 2.97 us                                                | 2.95 us: 1.01x faster                                               |
| mako                    | 9.85 ms                                                | 9.78 ms: 1.01x faster                                               |
| xml_etree_process       | 53.8 ms                                                | 53.5 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 103 ms                                                 | 103 ms: 1.00x slower                                                |
| async_tree_cpu_io_mixed | 752 ms                                                 | 757 ms: 1.01x slower                                                |
| pickle_dict             | 31.4 us                                                | 31.6 us: 1.01x slower                                               |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                              |
| regex_v8                | 22.3 ms                                                | 22.5 ms: 1.01x slower                                               |
| dulwich_log             | 63.9 ms                                                | 64.6 ms: 1.01x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 77.4 ms: 1.02x slower                                               |
| scimark_lu              | 107 ms                                                 | 109 ms: 1.02x slower                                                |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                               |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                                |
| nbody                   | 95.0 ms                                                | 98.3 ms: 1.03x slower                                               |
| async_generators        | 359 ms                                                 | 373 ms: 1.04x slower                                                |
| pathlib                 | 18.2 ms                                                | 19.1 ms: 1.05x slower                                               |
| regex_effbot            | 3.36 ms                                                | 3.54 ms: 1.05x slower                                               |
| sqlglot_transpile       | 1.66 ms                                                | 1.76 ms: 1.06x slower                                               |
| sqlglot_parse           | 1.37 ms                                                | 1.46 ms: 1.07x slower                                               |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.71 ms: 1.07x slower                                               |
| python_startup          | 8.36 ms                                                | 8.96 ms: 1.07x slower                                               |
| sqlite_synth            | 2.49 us                                                | 2.68 us: 1.07x slower                                               |
| scimark_sor             | 115 ms                                                 | 125 ms: 1.09x slower                                                |
| python_startup_no_site  | 5.96 ms                                                | 6.47 ms: 1.09x slower                                               |
| generators              | 72.2 ms                                                | 79.5 ms: 1.10x slower                                               |
| pyflate                 | 417 ms                                                 | 463 ms: 1.11x slower                                                |
| mypy                    | 669 ms                                                 | 804 ms: 1.20x slower                                                |
| crypto_pyaes            | 73.9 ms                                                | 89.3 ms: 1.21x slower                                               |
| scimark_fft             | 329 ms                                                 | 399 ms: 1.21x slower                                                |
| spectral_norm           | 99.9 ms                                                | 138 ms: 1.38x slower                                                |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (8): pycparser, unpickle_list, django_template, bench_mp_pool, unpickle, scimark_monte_carlo, pickle_list, async_tree_memoization
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230131-3.12.0a4+-fe65f49/bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
