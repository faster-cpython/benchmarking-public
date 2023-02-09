
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 6b312e0
- commit date: 2023-02-03
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| chameleon      | 6.41 ms                                                | 6.28 ms: 1.02x faster                                               |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                              |
| html5lib       | 63.2 ms                                                | 59.5 ms: 1.06x faster                                               |
| tornado_http   | 96.6 ms                                                | 94.0 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.5 ms: 1.05x faster                                               |
| pidigits       | 199 ms                                                 | 191 ms: 1.05x faster                                                |
| nbody          | 95.0 ms                                                | 96.7 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                                |
| regex_v8       | 22.3 ms                                                | 22.6 ms: 1.01x slower                                               |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                                |
| regex_effbot   | 3.36 ms                                                | 3.44 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.00x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.52 ms: 1.33x faster                                               |
| unpickle_pure_python | 225 us                                                 | 200 us: 1.13x faster                                                |
| json_loads           | 26.2 us                                                | 23.8 us: 1.10x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| pickle_list          | 4.17 us                                                | 3.92 us: 1.07x faster                                               |
| pickle_pure_python   | 304 us                                                 | 287 us: 1.06x faster                                                |
| pickle_dict          | 31.4 us                                                | 29.8 us: 1.05x faster                                               |
| xml_etree_process    | 53.8 ms                                                | 53.4 ms: 1.01x faster                                               |
| xml_etree_iterparse  | 103 ms                                                 | 102 ms: 1.01x faster                                                |
| unpickle_list        | 4.95 us                                                | 5.02 us: 1.01x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 77.6 ms: 1.02x slower                                               |
| pickle               | 9.79 us                                                | 10.0 us: 1.02x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.96 ms: 1.07x slower                                               |
| python_startup_no_site | 5.96 ms                                                | 6.48 ms: 1.09x slower                                               |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 47.9 ms: 1.09x faster                                               |
| genshi_text     | 22.1 ms                                                | 20.8 ms: 1.06x faster                                               |
| mako            | 9.85 ms                                                | 9.58 ms: 1.03x faster                                               |
| django_template | 32.5 ms                                                | 32.3 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.52 ms: 1.33x faster                                               |
| deltablue               | 3.64 ms                                                | 3.18 ms: 1.15x faster                                               |
| unpickle_pure_python    | 225 us                                                 | 200 us: 1.13x faster                                                |
| nqueens                 | 85.0 ms                                                | 75.8 ms: 1.12x faster                                               |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.98 ms: 1.11x faster                                               |
| richards                | 46.2 ms                                                | 41.8 ms: 1.10x faster                                               |
| json_loads              | 26.2 us                                                | 23.8 us: 1.10x faster                                               |
| go                      | 143 ms                                                 | 132 ms: 1.09x faster                                                |
| genshi_xml              | 52.1 ms                                                | 47.9 ms: 1.09x faster                                               |
| chaos                   | 68.6 ms                                                | 63.5 ms: 1.08x faster                                               |
| mdp                     | 2.62 sec                                               | 2.45 sec: 1.07x faster                                              |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| hexiom                  | 6.35 ms                                                | 5.94 ms: 1.07x faster                                               |
| scimark_fft             | 329 ms                                                 | 308 ms: 1.07x faster                                                |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                |
| deepcopy_memo           | 36.4 us                                                | 34.2 us: 1.07x faster                                               |
| json                    | 4.95 ms                                                | 4.64 ms: 1.07x faster                                               |
| pickle_list             | 4.17 us                                                | 3.92 us: 1.07x faster                                               |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                                |
| genshi_text             | 22.1 ms                                                | 20.8 ms: 1.06x faster                                               |
| logging_simple          | 6.06 us                                                | 5.70 us: 1.06x faster                                               |
| sympy_str               | 287 ms                                                 | 270 ms: 1.06x faster                                                |
| logging_silent          | 98.5 ns                                                | 92.7 ns: 1.06x faster                                               |
| html5lib                | 63.2 ms                                                | 59.5 ms: 1.06x faster                                               |
| deepcopy                | 344 us                                                 | 324 us: 1.06x faster                                                |
| pickle_pure_python      | 304 us                                                 | 287 us: 1.06x faster                                                |
| scimark_sor             | 115 ms                                                 | 109 ms: 1.06x faster                                                |
| sympy_integrate         | 20.9 ms                                                | 19.7 ms: 1.06x faster                                               |
| logging_format          | 6.62 us                                                | 6.28 us: 1.05x faster                                               |
| pickle_dict             | 31.4 us                                                | 29.8 us: 1.05x faster                                               |
| float                   | 76.3 ms                                                | 72.5 ms: 1.05x faster                                               |
| aiohttp                 | 1.05 ms                                                | 995 us: 1.05x faster                                                |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.05x faster                                              |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                               |
| pidigits                | 199 ms                                                 | 191 ms: 1.05x faster                                                |
| async_generators        | 359 ms                                                 | 346 ms: 1.04x faster                                                |
| sqlglot_optimize        | 53.0 ms                                                | 51.0 ms: 1.04x faster                                               |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                              |
| fannkuch                | 388 ms                                                 | 375 ms: 1.03x faster                                                |
| sympy_expand            | 472 ms                                                 | 457 ms: 1.03x faster                                                |
| pycparser               | 1.17 sec                                               | 1.13 sec: 1.03x faster                                              |
| bench_thread_pool       | 810 us                                                 | 784 us: 1.03x faster                                                |
| deepcopy_reduce         | 2.97 us                                                | 2.88 us: 1.03x faster                                               |
| mako                    | 9.85 ms                                                | 9.58 ms: 1.03x faster                                               |
| tornado_http            | 96.6 ms                                                | 94.0 ms: 1.03x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                |
| scimark_monte_carlo     | 68.3 ms                                                | 66.5 ms: 1.03x faster                                               |
| dulwich_log             | 63.9 ms                                                | 62.3 ms: 1.03x faster                                               |
| telco                   | 6.62 ms                                                | 6.46 ms: 1.03x faster                                               |
| pprint_safe_repr        | 691 ms                                                 | 676 ms: 1.02x faster                                                |
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                                |
| raytrace                | 290 ms                                                 | 285 ms: 1.02x faster                                                |
| chameleon               | 6.41 ms                                                | 6.28 ms: 1.02x faster                                               |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                               |
| pyflate                 | 417 ms                                                 | 414 ms: 1.01x faster                                                |
| xml_etree_process       | 53.8 ms                                                | 53.4 ms: 1.01x faster                                               |
| thrift                  | 752 us                                                 | 747 us: 1.01x faster                                                |
| django_template         | 32.5 ms                                                | 32.3 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 103 ms                                                 | 102 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed | 752 ms                                                 | 760 ms: 1.01x slower                                                |
| unpickle_list           | 4.95 us                                                | 5.02 us: 1.01x slower                                               |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                              |
| regex_v8                | 22.3 ms                                                | 22.6 ms: 1.01x slower                                               |
| sqlite_synth            | 2.49 us                                                | 2.53 us: 1.01x slower                                               |
| nbody                   | 95.0 ms                                                | 96.7 ms: 1.02x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 77.6 ms: 1.02x slower                                               |
| sqlglot_transpile       | 1.66 ms                                                | 1.69 ms: 1.02x slower                                               |
| sqlglot_parse           | 1.37 ms                                                | 1.40 ms: 1.02x slower                                               |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                                |
| pickle                  | 9.79 us                                                | 10.0 us: 1.02x slower                                               |
| regex_effbot            | 3.36 ms                                                | 3.44 ms: 1.03x slower                                               |
| spectral_norm           | 99.9 ms                                                | 103 ms: 1.03x slower                                                |
| generators              | 72.2 ms                                                | 74.5 ms: 1.03x slower                                               |
| crypto_pyaes            | 73.9 ms                                                | 76.4 ms: 1.03x slower                                               |
| async_tree_memoization  | 625 ms                                                 | 652 ms: 1.04x slower                                                |
| python_startup          | 8.36 ms                                                | 8.96 ms: 1.07x slower                                               |
| unpack_sequence         | 43.4 ns                                                | 46.9 ns: 1.08x slower                                               |
| python_startup_no_site  | 5.96 ms                                                | 6.48 ms: 1.09x slower                                               |
| mypy                    | 669 ms                                                 | 802 ms: 1.20x slower                                                |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (7): unpickle, coverage, coroutines, async_tree_none, meteor_contest, bench_mp_pool, scimark_lu
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230203-3.12.0a4+-6b312e0/bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-6b312e0.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
