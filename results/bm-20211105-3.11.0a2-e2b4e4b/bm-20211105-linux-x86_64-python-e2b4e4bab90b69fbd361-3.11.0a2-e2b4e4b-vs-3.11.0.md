
# Results vs. 3.11.0

- fork: python
- ref: e2b4e4bab90b69fbd361
- machine: linux-x86_64
- commit hash: e2b4e4b
- commit date: 2021-11-05
- overall geometric mean: 1.09x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 274 ms: 1.06x slower                                                  |
| chameleon      | 6.38 ms                                                | 7.46 ms: 1.17x slower                                                 |
| docutils       | 2.60 sec                                               | 2.79 sec: 1.07x slower                                                |
| html5lib       | 64.8 ms                                                | 71.5 ms: 1.10x slower                                                 |
| tornado_http   | 96.5 ms                                                | 111 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 188 ms: 1.05x faster                                                  |
| float          | 76.8 ms                                                | 83.3 ms: 1.08x slower                                                 |
| nbody          | 90.0 ms                                                | 112 ms: 1.24x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.26 ms: 1.06x faster                                                 |
| regex_compile  | 136 ms                                                 | 145 ms: 1.06x slower                                                  |
| regex_v8       | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                 |
| regex_dna      | 203 ms                                                 | 219 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_dict          | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| xml_etree_parse      | 160 ms                                                 | 158 ms: 1.01x faster                                                  |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                                 |
| unpickle_list        | 4.99 us                                                | 5.13 us: 1.03x slower                                                 |
| unpickle             | 13.3 us                                                | 13.7 us: 1.03x slower                                                 |
| xml_etree_iterparse  | 104 ms                                                 | 110 ms: 1.06x slower                                                  |
| xml_etree_generate   | 75.9 ms                                                | 81.6 ms: 1.08x slower                                                 |
| xml_etree_process    | 53.7 ms                                                | 59.6 ms: 1.11x slower                                                 |
| pickle_list          | 4.14 us                                                | 4.68 us: 1.13x slower                                                 |
| pickle_pure_python   | 308 us                                                 | 364 us: 1.18x slower                                                  |
| unpickle_pure_python | 227 us                                                 | 271 us: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.04 ms                                                | 5.77 ms: 1.05x faster                                                 |
| python_startup         | 8.58 ms                                                | 14.6 ms: 1.70x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 56.1 ms: 1.09x slower                                                 |
| genshi_text     | 21.5 ms                                                | 24.6 ms: 1.14x slower                                                 |
| django_template | 32.3 ms                                                | 37.9 ms: 1.17x slower                                                 |
| mako            | 9.83 ms                                                | 12.1 ms: 1.23x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.16x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211105-linux-x86_64-python-e2b4e4bab90b69fbd361-3.11.0a2-e2b4e4b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coverage                | 99.3 ms                                                | 75.8 ms: 1.31x faster                                                 |
| generators              | 73.5 ms                                                | 57.4 ms: 1.28x faster                                                 |
| pickle_dict             | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| regex_effbot            | 3.46 ms                                                | 3.26 ms: 1.06x faster                                                 |
| pidigits                | 197 ms                                                 | 188 ms: 1.05x faster                                                  |
| python_startup_no_site  | 6.04 ms                                                | 5.77 ms: 1.05x faster                                                 |
| unpack_sequence         | 44.5 ns                                                | 43.6 ns: 1.02x faster                                                 |
| async_tree_none         | 526 ms                                                 | 518 ms: 1.02x faster                                                  |
| xml_etree_parse         | 160 ms                                                 | 158 ms: 1.01x faster                                                  |
| logging_simple          | 6.02 us                                                | 6.07 us: 1.01x slower                                                 |
| json                    | 4.87 ms                                                | 4.91 ms: 1.01x slower                                                 |
| telco                   | 6.43 ms                                                | 6.50 ms: 1.01x slower                                                 |
| async_generators        | 356 ms                                                 | 361 ms: 1.01x slower                                                  |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                                 |
| meteor_contest          | 104 ms                                                 | 106 ms: 1.02x slower                                                  |
| sympy_sum               | 166 ms                                                 | 170 ms: 1.03x slower                                                  |
| unpickle_list           | 4.99 us                                                | 5.13 us: 1.03x slower                                                 |
| mdp                     | 2.63 sec                                               | 2.71 sec: 1.03x slower                                                |
| gunicorn                | 1.12 ms                                                | 1.15 ms: 1.03x slower                                                 |
| unpickle                | 13.3 us                                                | 13.7 us: 1.03x slower                                                 |
| logging_format          | 6.48 us                                                | 6.71 us: 1.04x slower                                                 |
| sqlalchemy_imperative   | 18.1 ms                                                | 18.8 ms: 1.04x slower                                                 |
| flaskblogging           | 7.11 ms                                                | 7.46 ms: 1.05x slower                                                 |
| sqlalchemy_declarative  | 138 ms                                                 | 145 ms: 1.05x slower                                                  |
| sympy_str               | 291 ms                                                 | 306 ms: 1.05x slower                                                  |
| 2to3                    | 259 ms                                                 | 274 ms: 1.06x slower                                                  |
| pathlib                 | 18.1 ms                                                | 19.1 ms: 1.06x slower                                                 |
| pycparser               | 1.19 sec                                               | 1.26 sec: 1.06x slower                                                |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.86 ms: 1.06x slower                                                 |
| regex_compile           | 136 ms                                                 | 145 ms: 1.06x slower                                                  |
| sympy_integrate         | 21.0 ms                                                | 22.2 ms: 1.06x slower                                                 |
| xml_etree_iterparse     | 104 ms                                                 | 110 ms: 1.06x slower                                                  |
| sympy_expand            | 475 ms                                                 | 505 ms: 1.06x slower                                                  |
| regex_v8                | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                 |
| dulwich_log             | 64.0 ms                                                | 68.3 ms: 1.07x slower                                                 |
| docutils                | 2.60 sec                                               | 2.79 sec: 1.07x slower                                                |
| xml_etree_generate      | 75.9 ms                                                | 81.6 ms: 1.08x slower                                                 |
| regex_dna               | 203 ms                                                 | 219 ms: 1.08x slower                                                  |
| spectral_norm           | 98.1 ms                                                | 106 ms: 1.08x slower                                                  |
| thrift                  | 760 us                                                 | 821 us: 1.08x slower                                                  |
| pprint_safe_repr        | 706 ms                                                 | 763 ms: 1.08x slower                                                  |
| async_tree_io           | 1.30 sec                                               | 1.41 sec: 1.08x slower                                                |
| async_tree_memoization  | 624 ms                                                 | 676 ms: 1.08x slower                                                  |
| float                   | 76.8 ms                                                | 83.3 ms: 1.08x slower                                                 |
| pprint_pformat          | 1.46 sec                                               | 1.58 sec: 1.08x slower                                                |
| deepcopy_reduce         | 3.02 us                                                | 3.27 us: 1.09x slower                                                 |
| genshi_xml              | 51.4 ms                                                | 56.1 ms: 1.09x slower                                                 |
| nqueens                 | 83.8 ms                                                | 91.4 ms: 1.09x slower                                                 |
| scimark_fft             | 325 ms                                                 | 355 ms: 1.09x slower                                                  |
| bench_thread_pool       | 817 us                                                 | 892 us: 1.09x slower                                                  |
| coroutines              | 26.2 ms                                                | 28.8 ms: 1.10x slower                                                 |
| html5lib                | 64.8 ms                                                | 71.5 ms: 1.10x slower                                                 |
| sqlglot_optimize        | 52.7 ms                                                | 58.4 ms: 1.11x slower                                                 |
| sqlglot_normalize       | 108 ms                                                 | 119 ms: 1.11x slower                                                  |
| xml_etree_process       | 53.7 ms                                                | 59.6 ms: 1.11x slower                                                 |
| fannkuch                | 384 ms                                                 | 427 ms: 1.11x slower                                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 818 ms: 1.11x slower                                                  |
| sqlite_synth            | 2.48 us                                                | 2.76 us: 1.11x slower                                                 |
| deepcopy                | 341 us                                                 | 382 us: 1.12x slower                                                  |
| raytrace                | 291 ms                                                 | 326 ms: 1.12x slower                                                  |
| chaos                   | 68.7 ms                                                | 77.1 ms: 1.12x slower                                                 |
| deepcopy_memo           | 35.8 us                                                | 40.4 us: 1.13x slower                                                 |
| pickle_list             | 4.14 us                                                | 4.68 us: 1.13x slower                                                 |
| genshi_text             | 21.5 ms                                                | 24.6 ms: 1.14x slower                                                 |
| tornado_http            | 96.5 ms                                                | 111 ms: 1.15x slower                                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 78.4 ms: 1.15x slower                                                 |
| chameleon               | 6.38 ms                                                | 7.46 ms: 1.17x slower                                                 |
| hexiom                  | 6.34 ms                                                | 7.42 ms: 1.17x slower                                                 |
| django_template         | 32.3 ms                                                | 37.9 ms: 1.17x slower                                                 |
| pickle_pure_python      | 308 us                                                 | 364 us: 1.18x slower                                                  |
| logging_silent          | 98.0 ns                                                | 117 ns: 1.19x slower                                                  |
| crypto_pyaes            | 75.7 ms                                                | 90.2 ms: 1.19x slower                                                 |
| go                      | 140 ms                                                 | 167 ms: 1.19x slower                                                  |
| unpickle_pure_python    | 227 us                                                 | 271 us: 1.19x slower                                                  |
| richards                | 46.1 ms                                                | 55.7 ms: 1.21x slower                                                 |
| mako                    | 9.83 ms                                                | 12.1 ms: 1.23x slower                                                 |
| nbody                   | 90.0 ms                                                | 112 ms: 1.24x slower                                                  |
| scimark_lu              | 108 ms                                                 | 136 ms: 1.26x slower                                                  |
| pyflate                 | 419 ms                                                 | 541 ms: 1.29x slower                                                  |
| deltablue               | 3.66 ms                                                | 4.86 ms: 1.33x slower                                                 |
| scimark_sor             | 115 ms                                                 | 156 ms: 1.36x slower                                                  |
| sqlglot_transpile       | 1.65 ms                                                | 2.37 ms: 1.44x slower                                                 |
| sqlglot_parse           | 1.36 ms                                                | 2.06 ms: 1.51x slower                                                 |
| python_startup          | 8.58 ms                                                | 14.6 ms: 1.70x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.09x slower                                                          |

Benchmark hidden because not significant (4): json_loads, bench_mp_pool, json_dumps, pylint
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal, mypy2
