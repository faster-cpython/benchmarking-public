
# Results vs. 3.11.0

- fork: iritkatriel
- ref: single_op_exit
- machine: linux-x86_64
- commit hash: 4684fa7
- commit date: 2023-01-27
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                  |
| chameleon      | 6.38 ms                                                | 6.53 ms: 1.02x slower                                                 |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                |
| html5lib       | 64.8 ms                                                | 60.1 ms: 1.08x faster                                                 |
| tornado_http   | 96.5 ms                                                | 93.0 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.8 ms: 1.05x faster                                                 |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                  |
| nbody          | 90.0 ms                                                | 95.1 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                                  |
| regex_dna      | 203 ms                                                 | 209 ms: 1.03x slower                                                  |
| regex_effbot   | 3.46 ms                                                | 3.57 ms: 1.03x slower                                                 |
| regex_v8       | 22.2 ms                                                | 25.9 ms: 1.16x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.28 ms: 1.33x faster                                                 |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                                  |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                  |
| pickle_pure_python   | 308 us                                                 | 283 us: 1.09x faster                                                  |
| json_loads           | 26.1 us                                                | 24.1 us: 1.08x faster                                                 |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                  |
| xml_etree_process    | 53.7 ms                                                | 54.1 ms: 1.01x slower                                                 |
| pickle_list          | 4.14 us                                                | 4.21 us: 1.02x slower                                                 |
| xml_etree_generate   | 75.9 ms                                                | 77.6 ms: 1.02x slower                                                 |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (3): unpickle_list, pickle_dict, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.96 ms: 1.05x slower                                                 |
| python_startup_no_site | 6.04 ms                                                | 6.48 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.1 ms: 1.12x faster                                                 |
| genshi_text     | 21.5 ms                                                | 20.4 ms: 1.06x faster                                                 |
| mako            | 9.83 ms                                                | 9.69 ms: 1.01x faster                                                 |
| django_template | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 496 ms: 1.78x faster                                                  |
| json_dumps              | 12.4 ms                                                | 9.28 ms: 1.33x faster                                                 |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.99 ms: 1.15x faster                                                 |
| deltablue               | 3.66 ms                                                | 3.26 ms: 1.12x faster                                                 |
| genshi_xml              | 51.4 ms                                                | 46.1 ms: 1.12x faster                                                 |
| richards                | 46.1 ms                                                | 42.1 ms: 1.10x faster                                                 |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                  |
| nqueens                 | 83.8 ms                                                | 76.8 ms: 1.09x faster                                                 |
| pickle_pure_python      | 308 us                                                 | 283 us: 1.09x faster                                                  |
| sympy_str               | 291 ms                                                 | 268 ms: 1.09x faster                                                  |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.08x faster                                                |
| json_loads              | 26.1 us                                                | 24.1 us: 1.08x faster                                                 |
| scimark_fft             | 325 ms                                                 | 301 ms: 1.08x faster                                                  |
| html5lib                | 64.8 ms                                                | 60.1 ms: 1.08x faster                                                 |
| sympy_sum               | 166 ms                                                 | 154 ms: 1.07x faster                                                  |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                                  |
| hexiom                  | 6.34 ms                                                | 5.94 ms: 1.07x faster                                                 |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                                  |
| logging_silent          | 98.0 ns                                                | 92.0 ns: 1.07x faster                                                 |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                                 |
| bench_thread_pool       | 817 us                                                 | 769 us: 1.06x faster                                                  |
| chaos                   | 68.7 ms                                                | 64.8 ms: 1.06x faster                                                 |
| scimark_monte_carlo     | 68.0 ms                                                | 64.2 ms: 1.06x faster                                                 |
| aiohttp                 | 1.05 ms                                                | 991 us: 1.06x faster                                                  |
| gunicorn                | 1.12 ms                                                | 1.06 ms: 1.06x faster                                                 |
| genshi_text             | 21.5 ms                                                | 20.4 ms: 1.06x faster                                                 |
| json                    | 4.87 ms                                                | 4.61 ms: 1.06x faster                                                 |
| logging_simple          | 6.02 us                                                | 5.70 us: 1.06x faster                                                 |
| float                   | 76.8 ms                                                | 72.8 ms: 1.05x faster                                                 |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                                |
| sympy_expand            | 475 ms                                                 | 452 ms: 1.05x faster                                                  |
| coroutines              | 26.2 ms                                                | 24.8 ms: 1.05x faster                                                 |
| pyflate                 | 419 ms                                                 | 399 ms: 1.05x faster                                                  |
| pprint_safe_repr        | 706 ms                                                 | 674 ms: 1.05x faster                                                  |
| deepcopy                | 341 us                                                 | 327 us: 1.04x faster                                                  |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                  |
| sqlglot_optimize        | 52.7 ms                                                | 50.6 ms: 1.04x faster                                                 |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                |
| unpack_sequence         | 44.5 ns                                                | 42.8 ns: 1.04x faster                                                 |
| raytrace                | 291 ms                                                 | 281 ms: 1.04x faster                                                  |
| tornado_http            | 96.5 ms                                                | 93.0 ms: 1.04x faster                                                 |
| logging_format          | 6.48 us                                                | 6.25 us: 1.04x faster                                                 |
| dulwich_log             | 64.0 ms                                                | 61.8 ms: 1.03x faster                                                 |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                  |
| crypto_pyaes            | 75.7 ms                                                | 73.3 ms: 1.03x faster                                                 |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| deepcopy_memo           | 35.8 us                                                | 34.7 us: 1.03x faster                                                 |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                 |
| deepcopy_reduce         | 3.02 us                                                | 2.93 us: 1.03x faster                                                 |
| go                      | 140 ms                                                 | 137 ms: 1.03x faster                                                  |
| telco                   | 6.43 ms                                                | 6.28 ms: 1.02x faster                                                 |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                  |
| fannkuch                | 384 ms                                                 | 377 ms: 1.02x faster                                                  |
| spectral_norm           | 98.1 ms                                                | 96.5 ms: 1.02x faster                                                 |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.02x faster                                                 |
| coverage                | 99.3 ms                                                | 97.8 ms: 1.02x faster                                                 |
| mako                    | 9.83 ms                                                | 9.69 ms: 1.01x faster                                                 |
| scimark_lu              | 108 ms                                                 | 106 ms: 1.01x faster                                                  |
| thrift                  | 760 us                                                 | 755 us: 1.01x faster                                                  |
| async_generators        | 356 ms                                                 | 354 ms: 1.00x faster                                                  |
| django_template         | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                 |
| xml_etree_process       | 53.7 ms                                                | 54.1 ms: 1.01x slower                                                 |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                                |
| pickle_list             | 4.14 us                                                | 4.21 us: 1.02x slower                                                 |
| generators              | 73.5 ms                                                | 74.9 ms: 1.02x slower                                                 |
| mdp                     | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                |
| xml_etree_generate      | 75.9 ms                                                | 77.6 ms: 1.02x slower                                                 |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                                 |
| chameleon               | 6.38 ms                                                | 6.53 ms: 1.02x slower                                                 |
| regex_dna               | 203 ms                                                 | 209 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 757 ms: 1.03x slower                                                  |
| regex_effbot            | 3.46 ms                                                | 3.57 ms: 1.03x slower                                                 |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                                 |
| sqlite_synth            | 2.48 us                                                | 2.57 us: 1.04x slower                                                 |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                                 |
| python_startup          | 8.58 ms                                                | 8.96 ms: 1.05x slower                                                 |
| nbody                   | 90.0 ms                                                | 95.1 ms: 1.06x slower                                                 |
| python_startup_no_site  | 6.04 ms                                                | 6.48 ms: 1.07x slower                                                 |
| gc_traversal            | 3.82 ms                                                | 4.30 ms: 1.13x slower                                                 |
| regex_v8                | 22.2 ms                                                | 25.9 ms: 1.16x slower                                                 |
| dask                    | 365 ms                                                 | 491 ms: 1.35x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (8): async_tree_none, unpickle_list, pickle_dict, bench_mp_pool, unpickle, djangocms, meteor_contest, async_tree_memoization
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230127-3.12.0a4+-4684fa7/bm-20230127-linux-x86_64-iritkatriel-single_op_exit-3.12.0a4+-4684fa7.json: mypy
