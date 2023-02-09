
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
| 2to3           | 257 ms                                                 | 251 ms: 1.03x faster                                                |
| chameleon      | 6.41 ms                                                | 6.21 ms: 1.03x faster                                               |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                              |
| html5lib       | 63.2 ms                                                | 59.9 ms: 1.05x faster                                               |
| tornado_http   | 96.6 ms                                                | 93.6 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 190 ms: 1.05x faster                                                |
| float          | 76.3 ms                                                | 73.1 ms: 1.04x faster                                               |
| nbody          | 95.0 ms                                                | 96.7 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.05x faster                                                |
| regex_v8       | 22.3 ms                                                | 22.2 ms: 1.01x faster                                               |
| regex_dna      | 203 ms                                                 | 217 ms: 1.07x slower                                                |
| regex_effbot   | 3.36 ms                                                | 3.77 ms: 1.12x slower                                               |
| Geometric mean | (ref)                                                  | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.41 ms: 1.35x faster                                               |
| unpickle_pure_python | 225 us                                                 | 198 us: 1.14x faster                                                |
| json_loads           | 26.2 us                                                | 23.4 us: 1.12x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 145 ms: 1.09x faster                                                |
| pickle_pure_python   | 304 us                                                 | 284 us: 1.07x faster                                                |
| xml_etree_iterparse  | 103 ms                                                 | 102 ms: 1.01x faster                                                |
| xml_etree_process    | 53.8 ms                                                | 53.4 ms: 1.01x faster                                               |
| pickle_list          | 4.17 us                                                | 4.22 us: 1.01x slower                                               |
| pickle_dict          | 31.4 us                                                | 31.8 us: 1.01x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 77.5 ms: 1.02x slower                                               |
| pickle               | 9.79 us                                                | 10.1 us: 1.04x slower                                               |
| unpickle_list        | 4.95 us                                                | 5.15 us: 1.04x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.97 ms: 1.07x slower                                               |
| python_startup_no_site | 5.96 ms                                                | 6.50 ms: 1.09x slower                                               |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.5 ms: 1.10x faster                                               |
| mako            | 9.85 ms                                                | 9.47 ms: 1.04x faster                                               |
| genshi_text     | 22.1 ms                                                | 21.3 ms: 1.04x faster                                               |
| django_template | 32.5 ms                                                | 32.1 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.41 ms: 1.35x faster                                               |
| deltablue               | 3.64 ms                                                | 3.18 ms: 1.15x faster                                               |
| unpickle_pure_python    | 225 us                                                 | 198 us: 1.14x faster                                                |
| json_loads              | 26.2 us                                                | 23.4 us: 1.12x faster                                               |
| richards                | 46.2 ms                                                | 41.9 ms: 1.10x faster                                               |
| nqueens                 | 85.0 ms                                                | 77.2 ms: 1.10x faster                                               |
| genshi_xml              | 52.1 ms                                                | 47.5 ms: 1.10x faster                                               |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.04 ms: 1.09x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 145 ms: 1.09x faster                                                |
| go                      | 143 ms                                                 | 132 ms: 1.08x faster                                                |
| scimark_fft             | 329 ms                                                 | 304 ms: 1.08x faster                                                |
| coroutines              | 26.1 ms                                                | 24.1 ms: 1.08x faster                                               |
| json                    | 4.95 ms                                                | 4.59 ms: 1.08x faster                                               |
| chaos                   | 68.6 ms                                                | 63.7 ms: 1.08x faster                                               |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                |
| deepcopy_memo           | 36.4 us                                                | 33.9 us: 1.08x faster                                               |
| pickle_pure_python      | 304 us                                                 | 284 us: 1.07x faster                                                |
| hexiom                  | 6.35 ms                                                | 5.93 ms: 1.07x faster                                               |
| logging_simple          | 6.06 us                                                | 5.67 us: 1.07x faster                                               |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                |
| sympy_str               | 287 ms                                                 | 270 ms: 1.06x faster                                                |
| logging_silent          | 98.5 ns                                                | 92.8 ns: 1.06x faster                                               |
| coverage                | 101 ms                                                 | 94.8 ms: 1.06x faster                                               |
| logging_format          | 6.62 us                                                | 6.26 us: 1.06x faster                                               |
| fannkuch                | 388 ms                                                 | 368 ms: 1.06x faster                                                |
| sympy_integrate         | 20.9 ms                                                | 19.8 ms: 1.06x faster                                               |
| html5lib                | 63.2 ms                                                | 59.9 ms: 1.05x faster                                               |
| regex_compile           | 136 ms                                                 | 129 ms: 1.05x faster                                                |
| deepcopy                | 344 us                                                 | 326 us: 1.05x faster                                                |
| aiohttp                 | 1.05 ms                                                | 995 us: 1.05x faster                                                |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                               |
| pidigits                | 199 ms                                                 | 190 ms: 1.05x faster                                                |
| float                   | 76.3 ms                                                | 73.1 ms: 1.04x faster                                               |
| mdp                     | 2.62 sec                                               | 2.51 sec: 1.04x faster                                              |
| bench_thread_pool       | 810 us                                                 | 777 us: 1.04x faster                                                |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.04x faster                                              |
| mako                    | 9.85 ms                                                | 9.47 ms: 1.04x faster                                               |
| sympy_expand            | 472 ms                                                 | 455 ms: 1.04x faster                                                |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                              |
| sqlglot_optimize        | 53.0 ms                                                | 51.1 ms: 1.04x faster                                               |
| genshi_text             | 22.1 ms                                                | 21.3 ms: 1.04x faster                                               |
| spectral_norm           | 99.9 ms                                                | 96.6 ms: 1.03x faster                                               |
| pycparser               | 1.17 sec                                               | 1.14 sec: 1.03x faster                                              |
| tornado_http            | 96.6 ms                                                | 93.6 ms: 1.03x faster                                               |
| chameleon               | 6.41 ms                                                | 6.21 ms: 1.03x faster                                               |
| telco                   | 6.62 ms                                                | 6.42 ms: 1.03x faster                                               |
| 2to3                    | 257 ms                                                 | 251 ms: 1.03x faster                                                |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.02x faster                                               |
| dulwich_log             | 63.9 ms                                                | 62.4 ms: 1.02x faster                                               |
| raytrace                | 290 ms                                                 | 284 ms: 1.02x faster                                                |
| pprint_safe_repr        | 691 ms                                                 | 676 ms: 1.02x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                |
| unpack_sequence         | 43.4 ns                                                | 42.5 ns: 1.02x faster                                               |
| scimark_monte_carlo     | 68.3 ms                                                | 67.0 ms: 1.02x faster                                               |
| pyflate                 | 417 ms                                                 | 410 ms: 1.02x faster                                                |
| async_generators        | 359 ms                                                 | 353 ms: 1.02x faster                                                |
| thrift                  | 752 us                                                 | 740 us: 1.02x faster                                                |
| deepcopy_reduce         | 2.97 us                                                | 2.92 us: 1.01x faster                                               |
| django_template         | 32.5 ms                                                | 32.1 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 103 ms                                                 | 102 ms: 1.01x faster                                                |
| meteor_contest          | 105 ms                                                 | 104 ms: 1.01x faster                                                |
| async_tree_none         | 529 ms                                                 | 524 ms: 1.01x faster                                                |
| xml_etree_process       | 53.8 ms                                                | 53.4 ms: 1.01x faster                                               |
| regex_v8                | 22.3 ms                                                | 22.2 ms: 1.01x faster                                               |
| pickle_list             | 4.17 us                                                | 4.22 us: 1.01x slower                                               |
| pickle_dict             | 31.4 us                                                | 31.8 us: 1.01x slower                                               |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                              |
| sqlglot_transpile       | 1.66 ms                                                | 1.69 ms: 1.02x slower                                               |
| nbody                   | 95.0 ms                                                | 96.7 ms: 1.02x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 77.5 ms: 1.02x slower                                               |
| sqlite_synth            | 2.49 us                                                | 2.54 us: 1.02x slower                                               |
| sqlglot_parse           | 1.37 ms                                                | 1.40 ms: 1.02x slower                                               |
| crypto_pyaes            | 73.9 ms                                                | 76.1 ms: 1.03x slower                                               |
| pickle                  | 9.79 us                                                | 10.1 us: 1.04x slower                                               |
| unpickle_list           | 4.95 us                                                | 5.15 us: 1.04x slower                                               |
| async_tree_memoization  | 625 ms                                                 | 660 ms: 1.06x slower                                                |
| regex_dna               | 203 ms                                                 | 217 ms: 1.07x slower                                                |
| python_startup          | 8.36 ms                                                | 8.97 ms: 1.07x slower                                               |
| generators              | 72.2 ms                                                | 77.7 ms: 1.08x slower                                               |
| python_startup_no_site  | 5.96 ms                                                | 6.50 ms: 1.09x slower                                               |
| regex_effbot            | 3.36 ms                                                | 3.77 ms: 1.12x slower                                               |
| mypy                    | 669 ms                                                 | 803 ms: 1.20x slower                                                |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (4): unpickle, bench_mp_pool, async_tree_cpu_io_mixed, scimark_lu
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230203-3.12.0a4+-5609e30/bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
