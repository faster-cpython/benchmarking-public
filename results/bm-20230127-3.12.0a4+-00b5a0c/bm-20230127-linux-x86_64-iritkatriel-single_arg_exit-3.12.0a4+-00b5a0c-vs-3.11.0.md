
# Results vs. 3.11.0

- fork: iritkatriel
- ref: single_arg_exit
- machine: linux-x86_64
- commit hash: 00b5a0c
- commit date: 2023-01-27
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 254 ms: 1.02x faster                                                   |
| chameleon      | 6.38 ms                                                | 6.42 ms: 1.01x slower                                                  |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                 |
| html5lib       | 64.8 ms                                                | 60.6 ms: 1.07x faster                                                  |
| tornado_http   | 96.5 ms                                                | 94.7 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.5 ms: 1.06x faster                                                  |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                   |
| nbody          | 90.0 ms                                                | 94.8 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                                   |
| regex_v8       | 22.2 ms                                                | 21.5 ms: 1.04x faster                                                  |
| regex_effbot   | 3.46 ms                                                | 3.37 ms: 1.02x faster                                                  |
| regex_dna      | 203 ms                                                 | 205 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.32 ms: 1.33x faster                                                  |
| unpickle_pure_python | 227 us                                                 | 201 us: 1.13x faster                                                   |
| xml_etree_parse      | 160 ms                                                 | 146 ms: 1.10x faster                                                   |
| pickle_pure_python   | 308 us                                                 | 285 us: 1.08x faster                                                   |
| unpickle             | 13.3 us                                                | 13.0 us: 1.02x faster                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| json_loads           | 26.1 us                                                | 25.7 us: 1.01x faster                                                  |
| unpickle_list        | 4.99 us                                                | 4.95 us: 1.01x faster                                                  |
| xml_etree_process    | 53.7 ms                                                | 53.5 ms: 1.00x faster                                                  |
| pickle_dict          | 31.2 us                                                | 31.3 us: 1.01x slower                                                  |
| xml_etree_generate   | 75.9 ms                                                | 77.8 ms: 1.03x slower                                                  |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.96 ms: 1.05x slower                                                  |
| python_startup_no_site | 6.04 ms                                                | 6.54 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.7 ms: 1.10x faster                                                  |
| genshi_text     | 21.5 ms                                                | 20.4 ms: 1.05x faster                                                  |
| mako            | 9.83 ms                                                | 9.45 ms: 1.04x faster                                                  |
| django_template | 32.3 ms                                                | 33.3 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 498 ms: 1.77x faster                                                   |
| json_dumps              | 12.4 ms                                                | 9.32 ms: 1.33x faster                                                  |
| unpickle_pure_python    | 227 us                                                 | 201 us: 1.13x faster                                                   |
| deltablue               | 3.66 ms                                                | 3.25 ms: 1.13x faster                                                  |
| gc_traversal            | 3.82 ms                                                | 3.41 ms: 1.12x faster                                                  |
| genshi_xml              | 51.4 ms                                                | 46.7 ms: 1.10x faster                                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.17 ms: 1.10x faster                                                  |
| nqueens                 | 83.8 ms                                                | 76.3 ms: 1.10x faster                                                  |
| xml_etree_parse         | 160 ms                                                 | 146 ms: 1.10x faster                                                   |
| richards                | 46.1 ms                                                | 42.4 ms: 1.09x faster                                                  |
| pickle_pure_python      | 308 us                                                 | 285 us: 1.08x faster                                                   |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                                   |
| html5lib                | 64.8 ms                                                | 60.6 ms: 1.07x faster                                                  |
| sympy_str               | 291 ms                                                 | 273 ms: 1.07x faster                                                   |
| logging_silent          | 98.0 ns                                                | 92.0 ns: 1.07x faster                                                  |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                                   |
| mdp                     | 2.63 sec                                               | 2.47 sec: 1.06x faster                                                 |
| pyflate                 | 419 ms                                                 | 394 ms: 1.06x faster                                                   |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                                   |
| hexiom                  | 6.34 ms                                                | 5.98 ms: 1.06x faster                                                  |
| deepcopy_memo           | 35.8 us                                                | 33.8 us: 1.06x faster                                                  |
| float                   | 76.8 ms                                                | 72.5 ms: 1.06x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                 |
| pycparser               | 1.19 sec                                               | 1.12 sec: 1.06x faster                                                 |
| genshi_text             | 21.5 ms                                                | 20.4 ms: 1.05x faster                                                  |
| pprint_safe_repr        | 706 ms                                                 | 671 ms: 1.05x faster                                                   |
| sympy_integrate         | 21.0 ms                                                | 20.0 ms: 1.05x faster                                                  |
| scimark_fft             | 325 ms                                                 | 311 ms: 1.05x faster                                                   |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                   |
| mako                    | 9.83 ms                                                | 9.45 ms: 1.04x faster                                                  |
| coroutines              | 26.2 ms                                                | 25.2 ms: 1.04x faster                                                  |
| regex_v8                | 22.2 ms                                                | 21.5 ms: 1.04x faster                                                  |
| deepcopy                | 341 us                                                 | 330 us: 1.04x faster                                                   |
| crypto_pyaes            | 75.7 ms                                                | 73.1 ms: 1.04x faster                                                  |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                 |
| deepcopy_reduce         | 3.02 us                                                | 2.92 us: 1.03x faster                                                  |
| sympy_expand            | 475 ms                                                 | 461 ms: 1.03x faster                                                   |
| raytrace                | 291 ms                                                 | 283 ms: 1.03x faster                                                   |
| spectral_norm           | 98.1 ms                                                | 95.4 ms: 1.03x faster                                                  |
| aiohttp                 | 1.05 ms                                                | 1.02 ms: 1.03x faster                                                  |
| telco                   | 6.43 ms                                                | 6.25 ms: 1.03x faster                                                  |
| logging_simple          | 6.02 us                                                | 5.87 us: 1.03x faster                                                  |
| regex_effbot            | 3.46 ms                                                | 3.37 ms: 1.02x faster                                                  |
| chaos                   | 68.7 ms                                                | 67.2 ms: 1.02x faster                                                  |
| 2to3                    | 259 ms                                                 | 254 ms: 1.02x faster                                                   |
| unpickle                | 13.3 us                                                | 13.0 us: 1.02x faster                                                  |
| tornado_http            | 96.5 ms                                                | 94.7 ms: 1.02x faster                                                  |
| dulwich_log             | 64.0 ms                                                | 62.7 ms: 1.02x faster                                                  |
| json                    | 4.87 ms                                                | 4.78 ms: 1.02x faster                                                  |
| async_tree_none         | 526 ms                                                 | 517 ms: 1.02x faster                                                   |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| unpack_sequence         | 44.5 ns                                                | 43.8 ns: 1.02x faster                                                  |
| thrift                  | 760 us                                                 | 749 us: 1.01x faster                                                   |
| go                      | 140 ms                                                 | 138 ms: 1.01x faster                                                   |
| gunicorn                | 1.12 ms                                                | 1.10 ms: 1.01x faster                                                  |
| json_loads              | 26.1 us                                                | 25.7 us: 1.01x faster                                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 67.1 ms: 1.01x faster                                                  |
| sqlglot_optimize        | 52.7 ms                                                | 52.1 ms: 1.01x faster                                                  |
| async_generators        | 356 ms                                                 | 352 ms: 1.01x faster                                                   |
| fannkuch                | 384 ms                                                 | 381 ms: 1.01x faster                                                   |
| unpickle_list           | 4.99 us                                                | 4.95 us: 1.01x faster                                                  |
| pathlib                 | 18.1 ms                                                | 18.0 ms: 1.01x faster                                                  |
| xml_etree_process       | 53.7 ms                                                | 53.5 ms: 1.00x faster                                                  |
| pickle_dict             | 31.2 us                                                | 31.3 us: 1.01x slower                                                  |
| chameleon               | 6.38 ms                                                | 6.42 ms: 1.01x slower                                                  |
| regex_dna               | 203 ms                                                 | 205 ms: 1.01x slower                                                   |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                                 |
| async_tree_cpu_io_mixed | 736 ms                                                 | 747 ms: 1.02x slower                                                   |
| xml_etree_generate      | 75.9 ms                                                | 77.8 ms: 1.03x slower                                                  |
| django_template         | 32.3 ms                                                | 33.3 ms: 1.03x slower                                                  |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                  |
| async_tree_memoization  | 624 ms                                                 | 646 ms: 1.03x slower                                                   |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.04x slower                                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                                  |
| scimark_lu              | 108 ms                                                 | 112 ms: 1.04x slower                                                   |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                                  |
| python_startup          | 8.58 ms                                                | 8.96 ms: 1.05x slower                                                  |
| nbody                   | 90.0 ms                                                | 94.8 ms: 1.05x slower                                                  |
| generators              | 73.5 ms                                                | 78.4 ms: 1.07x slower                                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.54 ms: 1.08x slower                                                  |
| create_gc_cycles        | 1.52 ms                                                | 1.66 ms: 1.10x slower                                                  |
| bench_thread_pool       | 817 us                                                 | 963 us: 1.18x slower                                                   |
| bench_mp_pool           | 24.0 ms                                                | 30.6 ms: 1.27x slower                                                  |
| dask                    | 365 ms                                                 | 518 ms: 1.42x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (6): logging_format, pickle_list, sqlglot_normalize, coverage, meteor_contest, djangocms
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230127-3.12.0a4+-00b5a0c/bm-20230127-linux-x86_64-iritkatriel-single_arg_exit-3.12.0a4+-00b5a0c.json: mypy
