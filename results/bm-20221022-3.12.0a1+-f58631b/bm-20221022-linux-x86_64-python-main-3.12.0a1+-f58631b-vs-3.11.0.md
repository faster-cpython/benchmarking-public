
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: f58631b
- commit date: 2022-10-22
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                   |
| chameleon      | 6.38 ms                                                | 6.60 ms: 1.04x slower                                  |
| html5lib       | 64.8 ms                                                | 59.1 ms: 1.10x faster                                  |
| tornado_http   | 96.5 ms                                                | 93.1 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.5 ms: 1.06x faster                                  |
| pidigits       | 197 ms                                                 | 199 ms: 1.01x slower                                   |
| nbody          | 90.0 ms                                                | 93.9 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.05x faster                                   |
| regex_v8       | 22.2 ms                                                | 22.7 ms: 1.02x slower                                  |
| regex_dna      | 203 ms                                                 | 209 ms: 1.03x slower                                   |
| regex_effbot   | 3.46 ms                                                | 3.66 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.49 ms: 1.30x faster                                  |
| unpickle_pure_python | 227 us                                                 | 203 us: 1.12x faster                                   |
| json_loads           | 26.1 us                                                | 23.5 us: 1.11x faster                                  |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                   |
| pickle_pure_python   | 308 us                                                 | 289 us: 1.07x faster                                   |
| pickle_list          | 4.14 us                                                | 3.96 us: 1.05x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| xml_etree_process    | 53.7 ms                                                | 53.1 ms: 1.01x faster                                  |
| pickle_dict          | 31.2 us                                                | 31.0 us: 1.01x faster                                  |
| xml_etree_generate   | 75.9 ms                                                | 75.5 ms: 1.00x faster                                  |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.37 ms: 1.02x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.06 ms: 1.00x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 49.7 ms: 1.03x faster                                  |
| genshi_text     | 21.5 ms                                                | 21.0 ms: 1.03x faster                                  |
| mako            | 9.83 ms                                                | 9.75 ms: 1.01x faster                                  |
| django_template | 32.3 ms                                                | 32.6 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.49 ms: 1.30x faster                                  |
| unpickle_pure_python    | 227 us                                                 | 203 us: 1.12x faster                                   |
| json_loads              | 26.1 us                                                | 23.5 us: 1.11x faster                                  |
| deltablue               | 3.66 ms                                                | 3.30 ms: 1.11x faster                                  |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.10x faster                                   |
| html5lib                | 64.8 ms                                                | 59.1 ms: 1.10x faster                                  |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.09x faster                                 |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                   |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.22 ms: 1.09x faster                                  |
| logging_silent          | 98.0 ns                                                | 90.5 ns: 1.08x faster                                  |
| coroutines              | 26.2 ms                                                | 24.4 ms: 1.07x faster                                  |
| pickle_pure_python      | 308 us                                                 | 289 us: 1.07x faster                                   |
| json                    | 4.87 ms                                                | 4.58 ms: 1.06x faster                                  |
| richards                | 46.1 ms                                                | 43.5 ms: 1.06x faster                                  |
| mdp                     | 2.63 sec                                               | 2.48 sec: 1.06x faster                                 |
| float                   | 76.8 ms                                                | 72.5 ms: 1.06x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                 |
| deepcopy_memo           | 35.8 us                                                | 34.1 us: 1.05x faster                                  |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                   |
| pickle_list             | 4.14 us                                                | 3.96 us: 1.05x faster                                  |
| regex_compile           | 136 ms                                                 | 130 ms: 1.05x faster                                   |
| pyflate                 | 419 ms                                                 | 400 ms: 1.05x faster                                   |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                   |
| deepcopy_reduce         | 3.02 us                                                | 2.89 us: 1.05x faster                                  |
| hexiom                  | 6.34 ms                                                | 6.07 ms: 1.04x faster                                  |
| dulwich_log             | 64.0 ms                                                | 61.3 ms: 1.04x faster                                  |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                  |
| nqueens                 | 83.8 ms                                                | 80.3 ms: 1.04x faster                                  |
| pprint_safe_repr        | 706 ms                                                 | 678 ms: 1.04x faster                                   |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                  |
| generators              | 73.5 ms                                                | 70.6 ms: 1.04x faster                                  |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                   |
| tornado_http            | 96.5 ms                                                | 93.1 ms: 1.04x faster                                  |
| fannkuch                | 384 ms                                                 | 371 ms: 1.04x faster                                   |
| genshi_xml              | 51.4 ms                                                | 49.7 ms: 1.03x faster                                  |
| sympy_str               | 291 ms                                                 | 282 ms: 1.03x faster                                   |
| spectral_norm           | 98.1 ms                                                | 95.1 ms: 1.03x faster                                  |
| deepcopy                | 341 us                                                 | 331 us: 1.03x faster                                   |
| logging_simple          | 6.02 us                                                | 5.84 us: 1.03x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                  |
| scimark_fft             | 325 ms                                                 | 317 ms: 1.03x faster                                   |
| thrift                  | 760 us                                                 | 739 us: 1.03x faster                                   |
| genshi_text             | 21.5 ms                                                | 21.0 ms: 1.03x faster                                  |
| python_startup          | 8.58 ms                                                | 8.37 ms: 1.02x faster                                  |
| sqlglot_optimize        | 52.7 ms                                                | 51.6 ms: 1.02x faster                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.33 ms: 1.02x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                   |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                   |
| scimark_monte_carlo     | 68.0 ms                                                | 66.6 ms: 1.02x faster                                  |
| raytrace                | 291 ms                                                 | 287 ms: 1.02x faster                                   |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.02x faster                                  |
| coverage                | 99.3 ms                                                | 97.8 ms: 1.01x faster                                  |
| sympy_sum               | 166 ms                                                 | 164 ms: 1.01x faster                                   |
| sqlglot_transpile       | 1.65 ms                                                | 1.63 ms: 1.01x faster                                  |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| xml_etree_process       | 53.7 ms                                                | 53.1 ms: 1.01x faster                                  |
| mako                    | 9.83 ms                                                | 9.75 ms: 1.01x faster                                  |
| pickle_dict             | 31.2 us                                                | 31.0 us: 1.01x faster                                  |
| xml_etree_generate      | 75.9 ms                                                | 75.5 ms: 1.00x faster                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.06 ms: 1.00x slower                                  |
| django_template         | 32.3 ms                                                | 32.6 ms: 1.01x slower                                  |
| crypto_pyaes            | 75.7 ms                                                | 76.4 ms: 1.01x slower                                  |
| pidigits                | 197 ms                                                 | 199 ms: 1.01x slower                                   |
| chaos                   | 68.7 ms                                                | 69.7 ms: 1.01x slower                                  |
| telco                   | 6.43 ms                                                | 6.54 ms: 1.02x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                 |
| regex_v8                | 22.2 ms                                                | 22.7 ms: 1.02x slower                                  |
| regex_dna               | 203 ms                                                 | 209 ms: 1.03x slower                                   |
| chameleon               | 6.38 ms                                                | 6.60 ms: 1.04x slower                                  |
| nbody                   | 90.0 ms                                                | 93.9 ms: 1.04x slower                                  |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.61 us: 1.05x slower                                  |
| regex_effbot            | 3.46 ms                                                | 3.66 ms: 1.06x slower                                  |
| async_tree_memoization  | 624 ms                                                 | 670 ms: 1.07x slower                                   |
| unpack_sequence         | 44.5 ns                                                | 48.7 ns: 1.10x slower                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (7): pylint, async_tree_cpu_io_mixed, logging_format, unpickle_list, unpickle, scimark_lu, async_tree_none
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: async_generators, asyncio_tcp, bench_mp_pool, bench_thread_pool, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221022-3.12.0a1+-f58631b/bm-20221022-linux-x86_64-python-main-3.12.0a1+-f58631b.json: mypy
