
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 1134727
- commit date: 2023-02-08
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| chameleon      | 6.41 ms                                                | 6.30 ms: 1.02x faster                                               |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                              |
| html5lib       | 63.2 ms                                                | 61.0 ms: 1.04x faster                                               |
| tornado_http   | 96.6 ms                                                | 94.2 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 71.4 ms: 1.07x faster                                               |
| pidigits       | 199 ms                                                 | 203 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.05x faster                                                |
| regex_v8       | 22.3 ms                                                | 21.7 ms: 1.03x faster                                               |
| regex_effbot   | 3.36 ms                                                | 3.46 ms: 1.03x slower                                               |
| regex_dna      | 203 ms                                                 | 212 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.60 ms: 1.32x faster                                               |
| unpickle_pure_python | 225 us                                                 | 197 us: 1.14x faster                                                |
| json_loads           | 26.2 us                                                | 24.1 us: 1.09x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| pickle_pure_python   | 304 us                                                 | 288 us: 1.06x faster                                                |
| unpickle_list        | 4.95 us                                                | 4.89 us: 1.01x faster                                               |
| xml_etree_iterparse  | 103 ms                                                 | 102 ms: 1.01x faster                                                |
| pickle_list          | 4.17 us                                                | 4.22 us: 1.01x slower                                               |
| pickle_dict          | 31.4 us                                                | 32.0 us: 1.02x slower                                               |
| xml_etree_process    | 53.8 ms                                                | 55.1 ms: 1.03x slower                                               |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 80.4 ms: 1.05x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.92 ms: 1.07x slower                                               |
| python_startup_no_site | 5.96 ms                                                | 6.48 ms: 1.09x slower                                               |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.1 ms: 1.11x faster                                               |
| genshi_text     | 22.1 ms                                                | 20.6 ms: 1.07x faster                                               |
| mako            | 9.85 ms                                                | 9.62 ms: 1.02x faster                                               |
| django_template | 32.5 ms                                                | 32.9 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.60 ms: 1.32x faster                                               |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.81 ms: 1.15x faster                                               |
| unpickle_pure_python    | 225 us                                                 | 197 us: 1.14x faster                                                |
| deltablue               | 3.64 ms                                                | 3.21 ms: 1.14x faster                                               |
| scimark_fft             | 329 ms                                                 | 296 ms: 1.11x faster                                                |
| genshi_xml              | 52.1 ms                                                | 47.1 ms: 1.11x faster                                               |
| richards                | 46.2 ms                                                | 42.4 ms: 1.09x faster                                               |
| json_loads              | 26.2 us                                                | 24.1 us: 1.09x faster                                               |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                |
| nqueens                 | 85.0 ms                                                | 79.1 ms: 1.08x faster                                               |
| logging_silent          | 98.5 ns                                                | 91.8 ns: 1.07x faster                                               |
| genshi_text             | 22.1 ms                                                | 20.6 ms: 1.07x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| float                   | 76.3 ms                                                | 71.4 ms: 1.07x faster                                               |
| json                    | 4.95 ms                                                | 4.63 ms: 1.07x faster                                               |
| hexiom                  | 6.35 ms                                                | 5.96 ms: 1.07x faster                                               |
| sympy_str               | 287 ms                                                 | 270 ms: 1.06x faster                                                |
| go                      | 143 ms                                                 | 135 ms: 1.06x faster                                                |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                                |
| scimark_monte_carlo     | 68.3 ms                                                | 64.6 ms: 1.06x faster                                               |
| pickle_pure_python      | 304 us                                                 | 288 us: 1.06x faster                                                |
| sympy_sum               | 166 ms                                                 | 157 ms: 1.05x faster                                                |
| sympy_integrate         | 20.9 ms                                                | 19.8 ms: 1.05x faster                                               |
| regex_compile           | 136 ms                                                 | 129 ms: 1.05x faster                                                |
| deepcopy_memo           | 36.4 us                                                | 34.7 us: 1.05x faster                                               |
| spectral_norm           | 99.9 ms                                                | 95.2 ms: 1.05x faster                                               |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                               |
| chaos                   | 68.6 ms                                                | 65.7 ms: 1.04x faster                                               |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.04x faster                                               |
| logging_simple          | 6.06 us                                                | 5.82 us: 1.04x faster                                               |
| logging_format          | 6.62 us                                                | 6.35 us: 1.04x faster                                               |
| pyflate                 | 417 ms                                                 | 402 ms: 1.04x faster                                                |
| html5lib                | 63.2 ms                                                | 61.0 ms: 1.04x faster                                               |
| sqlglot_optimize        | 53.0 ms                                                | 51.2 ms: 1.04x faster                                               |
| pprint_pformat          | 1.44 sec                                               | 1.40 sec: 1.03x faster                                              |
| sympy_expand            | 472 ms                                                 | 457 ms: 1.03x faster                                                |
| pycparser               | 1.17 sec                                               | 1.14 sec: 1.03x faster                                              |
| bench_thread_pool       | 810 us                                                 | 785 us: 1.03x faster                                                |
| regex_v8                | 22.3 ms                                                | 21.7 ms: 1.03x faster                                               |
| deepcopy                | 344 us                                                 | 334 us: 1.03x faster                                                |
| unpack_sequence         | 43.4 ns                                                | 42.2 ns: 1.03x faster                                               |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                              |
| dulwich_log             | 63.9 ms                                                | 62.3 ms: 1.03x faster                                               |
| tornado_http            | 96.6 ms                                                | 94.2 ms: 1.03x faster                                               |
| coverage                | 101 ms                                                 | 98.0 ms: 1.03x faster                                               |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                |
| mako                    | 9.85 ms                                                | 9.62 ms: 1.02x faster                                               |
| sqlalchemy_declarative  | 139 ms                                                 | 136 ms: 1.02x faster                                                |
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| telco                   | 6.62 ms                                                | 6.50 ms: 1.02x faster                                               |
| sqlalchemy_imperative   | 18.0 ms                                                | 17.7 ms: 1.02x faster                                               |
| chameleon               | 6.41 ms                                                | 6.30 ms: 1.02x faster                                               |
| raytrace                | 290 ms                                                 | 285 ms: 1.02x faster                                                |
| pprint_safe_repr        | 691 ms                                                 | 680 ms: 1.02x faster                                                |
| unpickle_list           | 4.95 us                                                | 4.89 us: 1.01x faster                                               |
| coroutines              | 26.1 ms                                                | 25.9 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 103 ms                                                 | 102 ms: 1.01x faster                                                |
| mdp                     | 2.62 sec                                               | 2.60 sec: 1.01x faster                                              |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                              |
| pickle_list             | 4.17 us                                                | 4.22 us: 1.01x slower                                               |
| async_tree_cpu_io_mixed | 752 ms                                                 | 761 ms: 1.01x slower                                                |
| django_template         | 32.5 ms                                                | 32.9 ms: 1.01x slower                                               |
| pidigits                | 199 ms                                                 | 203 ms: 1.02x slower                                                |
| pickle_dict             | 31.4 us                                                | 32.0 us: 1.02x slower                                               |
| scimark_lu              | 107 ms                                                 | 110 ms: 1.02x slower                                                |
| xml_etree_process       | 53.8 ms                                                | 55.1 ms: 1.03x slower                                               |
| sqlite_synth            | 2.49 us                                                | 2.56 us: 1.03x slower                                               |
| regex_effbot            | 3.36 ms                                                | 3.46 ms: 1.03x slower                                               |
| meteor_contest          | 105 ms                                                 | 108 ms: 1.03x slower                                                |
| sqlglot_transpile       | 1.66 ms                                                | 1.71 ms: 1.03x slower                                               |
| sqlglot_parse           | 1.37 ms                                                | 1.42 ms: 1.04x slower                                               |
| crypto_pyaes            | 73.9 ms                                                | 76.5 ms: 1.04x slower                                               |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                               |
| regex_dna               | 203 ms                                                 | 212 ms: 1.04x slower                                                |
| xml_etree_generate      | 76.2 ms                                                | 80.4 ms: 1.05x slower                                               |
| async_tree_memoization  | 625 ms                                                 | 662 ms: 1.06x slower                                                |
| python_startup          | 8.36 ms                                                | 8.92 ms: 1.07x slower                                               |
| python_startup_no_site  | 5.96 ms                                                | 6.48 ms: 1.09x slower                                               |
| generators              | 72.2 ms                                                | 79.4 ms: 1.10x slower                                               |
| async_generators        | 359 ms                                                 | 424 ms: 1.18x slower                                                |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                        |

Benchmark hidden because not significant (6): unpickle, deepcopy_reduce, bench_mp_pool, nbody, async_tree_none, thrift
Ignored benchmarks (3) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy, pylint
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230208-3.12.0a5+-1134727/bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal, mypy2
