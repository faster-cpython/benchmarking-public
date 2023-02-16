
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_float_freelist
- machine: linux-x86_64
- commit hash: 42ee27f
- commit date: 2023-02-07
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                      |
| chameleon      | 6.38 ms                                                | 6.31 ms: 1.01x faster                                                     |
| docutils       | 2.60 sec                                               | 2.49 sec: 1.05x faster                                                    |
| html5lib       | 64.8 ms                                                | 60.6 ms: 1.07x faster                                                     |
| tornado_http   | 96.5 ms                                                | 94.0 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.5 ms: 1.06x faster                                                     |
| pidigits       | 197 ms                                                 | 203 ms: 1.03x slower                                                      |
| nbody          | 90.0 ms                                                | 97.7 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                                      |
| regex_v8       | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                     |
| regex_effbot   | 3.46 ms                                                | 3.43 ms: 1.01x faster                                                     |
| regex_dna      | 203 ms                                                 | 213 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.43 ms: 1.31x faster                                                     |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                                      |
| json_loads           | 26.1 us                                                | 23.7 us: 1.10x faster                                                     |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                      |
| pickle_pure_python   | 308 us                                                 | 284 us: 1.09x faster                                                      |
| pickle_list          | 4.14 us                                                | 3.98 us: 1.04x faster                                                     |
| unpickle_list        | 4.99 us                                                | 4.84 us: 1.03x faster                                                     |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                      |
| pickle_dict          | 31.2 us                                                | 30.8 us: 1.01x faster                                                     |
| pickle               | 9.90 us                                                | 9.98 us: 1.01x slower                                                     |
| xml_etree_generate   | 75.9 ms                                                | 77.9 ms: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                              |

Benchmark hidden because not significant (2): unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.97 ms: 1.05x slower                                                     |
| python_startup_no_site | 6.04 ms                                                | 6.49 ms: 1.08x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.5 ms: 1.08x faster                                                     |
| genshi_text     | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                     |
| mako            | 9.83 ms                                                | 9.63 ms: 1.02x faster                                                     |
| django_template | 32.3 ms                                                | 32.2 ms: 1.00x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 493 ms: 1.79x faster                                                      |
| json_dumps              | 12.4 ms                                                | 9.43 ms: 1.31x faster                                                     |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                                      |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.99 ms: 1.15x faster                                                     |
| deltablue               | 3.66 ms                                                | 3.21 ms: 1.14x faster                                                     |
| richards                | 46.1 ms                                                | 41.4 ms: 1.11x faster                                                     |
| json_loads              | 26.1 us                                                | 23.7 us: 1.10x faster                                                     |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                      |
| pickle_pure_python      | 308 us                                                 | 284 us: 1.09x faster                                                      |
| genshi_xml              | 51.4 ms                                                | 47.5 ms: 1.08x faster                                                     |
| logging_silent          | 98.0 ns                                                | 90.7 ns: 1.08x faster                                                     |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                      |
| pycparser               | 1.19 sec                                               | 1.10 sec: 1.08x faster                                                    |
| chaos                   | 68.7 ms                                                | 63.9 ms: 1.08x faster                                                     |
| mdp                     | 2.63 sec                                               | 2.45 sec: 1.07x faster                                                    |
| sympy_str               | 291 ms                                                 | 272 ms: 1.07x faster                                                      |
| html5lib                | 64.8 ms                                                | 60.6 ms: 1.07x faster                                                     |
| json                    | 4.87 ms                                                | 4.56 ms: 1.07x faster                                                     |
| logging_simple          | 6.02 us                                                | 5.64 us: 1.07x faster                                                     |
| nqueens                 | 83.8 ms                                                | 78.6 ms: 1.07x faster                                                     |
| gc_traversal            | 3.82 ms                                                | 3.59 ms: 1.06x faster                                                     |
| hexiom                  | 6.34 ms                                                | 5.96 ms: 1.06x faster                                                     |
| coroutines              | 26.2 ms                                                | 24.6 ms: 1.06x faster                                                     |
| pyflate                 | 419 ms                                                 | 394 ms: 1.06x faster                                                      |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                                      |
| float                   | 76.8 ms                                                | 72.5 ms: 1.06x faster                                                     |
| unpack_sequence         | 44.5 ns                                                | 42.1 ns: 1.06x faster                                                     |
| sympy_sum               | 166 ms                                                 | 157 ms: 1.06x faster                                                      |
| scimark_fft             | 325 ms                                                 | 308 ms: 1.06x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                                     |
| aiohttp                 | 1.05 ms                                                | 995 us: 1.05x faster                                                      |
| genshi_text             | 21.5 ms                                                | 20.5 ms: 1.05x faster                                                     |
| bench_thread_pool       | 817 us                                                 | 780 us: 1.05x faster                                                      |
| docutils                | 2.60 sec                                               | 2.49 sec: 1.05x faster                                                    |
| deepcopy_memo           | 35.8 us                                                | 34.2 us: 1.05x faster                                                     |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                                     |
| pickle_list             | 4.14 us                                                | 3.98 us: 1.04x faster                                                     |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                      |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                    |
| spectral_norm           | 98.1 ms                                                | 94.4 ms: 1.04x faster                                                     |
| pprint_safe_repr        | 706 ms                                                 | 680 ms: 1.04x faster                                                      |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                      |
| deepcopy_reduce         | 3.02 us                                                | 2.91 us: 1.04x faster                                                     |
| logging_format          | 6.48 us                                                | 6.26 us: 1.03x faster                                                     |
| sqlglot_optimize        | 52.7 ms                                                | 51.0 ms: 1.03x faster                                                     |
| deepcopy                | 341 us                                                 | 331 us: 1.03x faster                                                      |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                      |
| unpickle_list           | 4.99 us                                                | 4.84 us: 1.03x faster                                                     |
| dulwich_log             | 64.0 ms                                                | 62.1 ms: 1.03x faster                                                     |
| tornado_http            | 96.5 ms                                                | 94.0 ms: 1.03x faster                                                     |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.03x faster                                                     |
| thrift                  | 760 us                                                 | 740 us: 1.03x faster                                                      |
| raytrace                | 291 ms                                                 | 284 ms: 1.03x faster                                                      |
| pathlib                 | 18.1 ms                                                | 17.6 ms: 1.03x faster                                                     |
| coverage                | 99.3 ms                                                | 97.1 ms: 1.02x faster                                                     |
| mako                    | 9.83 ms                                                | 9.63 ms: 1.02x faster                                                     |
| fannkuch                | 384 ms                                                 | 377 ms: 1.02x faster                                                      |
| regex_v8                | 22.2 ms                                                | 21.8 ms: 1.02x faster                                                     |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                                      |
| pickle_dict             | 31.2 us                                                | 30.8 us: 1.01x faster                                                     |
| chameleon               | 6.38 ms                                                | 6.31 ms: 1.01x faster                                                     |
| async_generators        | 356 ms                                                 | 353 ms: 1.01x faster                                                      |
| regex_effbot            | 3.46 ms                                                | 3.43 ms: 1.01x faster                                                     |
| django_template         | 32.3 ms                                                | 32.2 ms: 1.00x faster                                                     |
| pickle                  | 9.90 us                                                | 9.98 us: 1.01x slower                                                     |
| meteor_contest          | 104 ms                                                 | 106 ms: 1.01x slower                                                      |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                                    |
| xml_etree_generate      | 75.9 ms                                                | 77.9 ms: 1.03x slower                                                     |
| pidigits                | 197 ms                                                 | 203 ms: 1.03x slower                                                      |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                                     |
| async_tree_cpu_io_mixed | 736 ms                                                 | 761 ms: 1.03x slower                                                      |
| sqlite_synth            | 2.48 us                                                | 2.57 us: 1.04x slower                                                     |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                                     |
| python_startup          | 8.58 ms                                                | 8.97 ms: 1.05x slower                                                     |
| regex_dna               | 203 ms                                                 | 213 ms: 1.05x slower                                                      |
| generators              | 73.5 ms                                                | 77.0 ms: 1.05x slower                                                     |
| async_tree_memoization  | 624 ms                                                 | 660 ms: 1.06x slower                                                      |
| python_startup_no_site  | 6.04 ms                                                | 6.49 ms: 1.08x slower                                                     |
| nbody                   | 90.0 ms                                                | 97.7 ms: 1.09x slower                                                     |
| dask                    | 365 ms                                                 | 495 ms: 1.35x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (9): unpickle, djangocms, scimark_monte_carlo, scimark_lu, telco, xml_etree_process, bench_mp_pool, async_tree_none, crypto_pyaes
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230207-3.12.0a4+-42ee27f/bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f.json: mypy
