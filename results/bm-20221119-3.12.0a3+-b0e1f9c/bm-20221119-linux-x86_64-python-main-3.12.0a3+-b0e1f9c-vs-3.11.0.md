
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: b0e1f9c
- commit date: 2022-11-19
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 245 ms: 1.06x faster                                   |
| chameleon      | 6.38 ms                                                | 6.49 ms: 1.02x slower                                  |
| html5lib       | 64.8 ms                                                | 59.1 ms: 1.10x faster                                  |
| tornado_http   | 96.5 ms                                                | 92.7 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.6 ms: 1.07x faster                                  |
| pidigits       | 197 ms                                                 | 192 ms: 1.03x faster                                   |
| nbody          | 90.0 ms                                                | 94.1 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                   |
| regex_v8       | 22.2 ms                                                | 22.2 ms: 1.00x faster                                  |
| regex_dna      | 203 ms                                                 | 213 ms: 1.05x slower                                   |
| regex_effbot   | 3.46 ms                                                | 3.77 ms: 1.09x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.42 ms: 1.31x faster                                  |
| unpickle_pure_python | 227 us                                                 | 201 us: 1.13x faster                                   |
| pickle_pure_python   | 308 us                                                 | 283 us: 1.09x faster                                   |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                   |
| json_loads           | 26.1 us                                                | 24.2 us: 1.08x faster                                  |
| xml_etree_process    | 53.7 ms                                                | 52.9 ms: 1.01x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| pickle_list          | 4.14 us                                                | 4.11 us: 1.01x faster                                  |
| pickle_dict          | 31.2 us                                                | 31.0 us: 1.01x faster                                  |
| xml_etree_generate   | 75.9 ms                                                | 76.4 ms: 1.01x slower                                  |
| unpickle_list        | 4.99 us                                                | 5.10 us: 1.02x slower                                  |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.51 ms: 1.01x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.25 ms: 1.03x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.2 ms: 1.11x faster                                  |
| genshi_text     | 21.5 ms                                                | 20.4 ms: 1.05x faster                                  |
| django_template | 32.3 ms                                                | 32.6 ms: 1.01x slower                                  |
| mako            | 9.83 ms                                                | 9.94 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.42 ms: 1.31x faster                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.96 ms: 1.16x faster                                  |
| deltablue               | 3.66 ms                                                | 3.23 ms: 1.13x faster                                  |
| unpickle_pure_python    | 227 us                                                 | 201 us: 1.13x faster                                   |
| genshi_xml              | 51.4 ms                                                | 46.2 ms: 1.11x faster                                  |
| richards                | 46.1 ms                                                | 41.6 ms: 1.11x faster                                  |
| scimark_sor             | 115 ms                                                 | 104 ms: 1.10x faster                                   |
| html5lib                | 64.8 ms                                                | 59.1 ms: 1.10x faster                                  |
| pickle_pure_python      | 308 us                                                 | 283 us: 1.09x faster                                   |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                   |
| json_loads              | 26.1 us                                                | 24.2 us: 1.08x faster                                  |
| logging_silent          | 98.0 ns                                                | 91.1 ns: 1.08x faster                                  |
| scimark_fft             | 325 ms                                                 | 303 ms: 1.08x faster                                   |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                   |
| float                   | 76.8 ms                                                | 71.6 ms: 1.07x faster                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 64.0 ms: 1.06x faster                                  |
| pycparser               | 1.19 sec                                               | 1.12 sec: 1.06x faster                                 |
| 2to3                    | 259 ms                                                 | 245 ms: 1.06x faster                                   |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                 |
| dulwich_log             | 64.0 ms                                                | 60.6 ms: 1.06x faster                                  |
| coroutines              | 26.2 ms                                                | 24.8 ms: 1.05x faster                                  |
| genshi_text             | 21.5 ms                                                | 20.4 ms: 1.05x faster                                  |
| aiohttp                 | 1.05 ms                                                | 999 us: 1.05x faster                                   |
| pprint_safe_repr        | 706 ms                                                 | 673 ms: 1.05x faster                                   |
| raytrace                | 291 ms                                                 | 278 ms: 1.05x faster                                   |
| deepcopy_memo           | 35.8 us                                                | 34.2 us: 1.05x faster                                  |
| logging_simple          | 6.02 us                                                | 5.77 us: 1.04x faster                                  |
| json                    | 4.87 ms                                                | 4.67 ms: 1.04x faster                                  |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                   |
| fannkuch                | 384 ms                                                 | 369 ms: 1.04x faster                                   |
| tornado_http            | 96.5 ms                                                | 92.7 ms: 1.04x faster                                  |
| chaos                   | 68.7 ms                                                | 66.0 ms: 1.04x faster                                  |
| pyflate                 | 419 ms                                                 | 403 ms: 1.04x faster                                   |
| sqlglot_optimize        | 52.7 ms                                                | 50.7 ms: 1.04x faster                                  |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                  |
| scimark_lu              | 108 ms                                                 | 104 ms: 1.04x faster                                   |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                   |
| unpack_sequence         | 44.5 ns                                                | 42.9 ns: 1.04x faster                                  |
| deepcopy                | 341 us                                                 | 330 us: 1.04x faster                                   |
| pathlib                 | 18.1 ms                                                | 17.5 ms: 1.03x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                   |
| sympy_str               | 291 ms                                                 | 283 ms: 1.03x faster                                   |
| nqueens                 | 83.8 ms                                                | 81.5 ms: 1.03x faster                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.33 ms: 1.03x faster                                  |
| pidigits                | 197 ms                                                 | 192 ms: 1.03x faster                                   |
| telco                   | 6.43 ms                                                | 6.27 ms: 1.03x faster                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.61 ms: 1.02x faster                                  |
| hexiom                  | 6.34 ms                                                | 6.21 ms: 1.02x faster                                  |
| logging_format          | 6.48 us                                                | 6.35 us: 1.02x faster                                  |
| crypto_pyaes            | 75.7 ms                                                | 74.3 ms: 1.02x faster                                  |
| thrift                  | 760 us                                                 | 746 us: 1.02x faster                                   |
| xml_etree_process       | 53.7 ms                                                | 52.9 ms: 1.01x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| deepcopy_reduce         | 3.02 us                                                | 2.98 us: 1.01x faster                                  |
| coverage                | 99.3 ms                                                | 98.2 ms: 1.01x faster                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 729 ms: 1.01x faster                                   |
| meteor_contest          | 104 ms                                                 | 104 ms: 1.01x faster                                   |
| pickle_list             | 4.14 us                                                | 4.11 us: 1.01x faster                                  |
| python_startup          | 8.58 ms                                                | 8.51 ms: 1.01x faster                                  |
| sympy_sum               | 166 ms                                                 | 165 ms: 1.01x faster                                   |
| pickle_dict             | 31.2 us                                                | 31.0 us: 1.01x faster                                  |
| spectral_norm           | 98.1 ms                                                | 97.6 ms: 1.01x faster                                  |
| regex_v8                | 22.2 ms                                                | 22.2 ms: 1.00x faster                                  |
| xml_etree_generate      | 75.9 ms                                                | 76.4 ms: 1.01x slower                                  |
| mdp                     | 2.63 sec                                               | 2.65 sec: 1.01x slower                                 |
| django_template         | 32.3 ms                                                | 32.6 ms: 1.01x slower                                  |
| mako                    | 9.83 ms                                                | 9.94 ms: 1.01x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                 |
| chameleon               | 6.38 ms                                                | 6.49 ms: 1.02x slower                                  |
| unpickle_list           | 4.99 us                                                | 5.10 us: 1.02x slower                                  |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.25 ms: 1.03x slower                                  |
| nbody                   | 90.0 ms                                                | 94.1 ms: 1.05x slower                                  |
| regex_dna               | 203 ms                                                 | 213 ms: 1.05x slower                                   |
| generators              | 73.5 ms                                                | 78.0 ms: 1.06x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.64 us: 1.06x slower                                  |
| async_tree_memoization  | 624 ms                                                 | 665 ms: 1.07x slower                                   |
| regex_effbot            | 3.46 ms                                                | 3.77 ms: 1.09x slower                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (2): async_tree_none, unpickle
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: async_generators, asyncio_tcp, bench_mp_pool, bench_thread_pool, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221119-3.12.0a3+-b0e1f9c/bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c.json: mypy
