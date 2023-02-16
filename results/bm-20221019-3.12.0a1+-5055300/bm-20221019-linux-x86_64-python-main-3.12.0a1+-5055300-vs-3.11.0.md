
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 5055300
- commit date: 2022-10-19
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| chameleon      | 6.38 ms                                                | 6.46 ms: 1.01x slower                                  |
| html5lib       | 64.8 ms                                                | 60.2 ms: 1.08x faster                                  |
| tornado_http   | 96.5 ms                                                | 93.0 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 71.1 ms: 1.08x faster                                  |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                   |
| nbody          | 90.0 ms                                                | 94.8 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                   |
| regex_v8       | 22.2 ms                                                | 21.4 ms: 1.04x faster                                  |
| regex_effbot   | 3.46 ms                                                | 3.40 ms: 1.02x faster                                  |
| regex_dna      | 203 ms                                                 | 205 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.42 ms: 1.31x faster                                  |
| unpickle_pure_python | 227 us                                                 | 202 us: 1.12x faster                                   |
| xml_etree_parse      | 160 ms                                                 | 144 ms: 1.11x faster                                   |
| json_loads           | 26.1 us                                                | 24.0 us: 1.09x faster                                  |
| pickle_pure_python   | 308 us                                                 | 285 us: 1.08x faster                                   |
| pickle_list          | 4.14 us                                                | 3.99 us: 1.04x faster                                  |
| xml_etree_process    | 53.7 ms                                                | 53.3 ms: 1.01x faster                                  |
| pickle_dict          | 31.2 us                                                | 31.1 us: 1.00x faster                                  |
| unpickle_list        | 4.99 us                                                | 5.02 us: 1.01x slower                                  |
| xml_etree_generate   | 75.9 ms                                                | 76.9 ms: 1.01x slower                                  |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                   |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.32 ms: 1.03x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.03 ms: 1.00x faster                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 49.3 ms: 1.04x faster                                  |
| genshi_text     | 21.5 ms                                                | 20.9 ms: 1.03x faster                                  |
| mako            | 9.83 ms                                                | 9.79 ms: 1.00x faster                                  |
| django_template | 32.3 ms                                                | 32.7 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.42 ms: 1.31x faster                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.04 ms: 1.13x faster                                  |
| unpickle_pure_python    | 227 us                                                 | 202 us: 1.12x faster                                   |
| xml_etree_parse         | 160 ms                                                 | 144 ms: 1.11x faster                                   |
| scimark_sor             | 115 ms                                                 | 104 ms: 1.11x faster                                   |
| pycparser               | 1.19 sec                                               | 1.08 sec: 1.09x faster                                 |
| deltablue               | 3.66 ms                                                | 3.36 ms: 1.09x faster                                  |
| json_loads              | 26.1 us                                                | 24.0 us: 1.09x faster                                  |
| pickle_pure_python      | 308 us                                                 | 285 us: 1.08x faster                                   |
| float                   | 76.8 ms                                                | 71.1 ms: 1.08x faster                                  |
| html5lib                | 64.8 ms                                                | 60.2 ms: 1.08x faster                                  |
| coroutines              | 26.2 ms                                                | 24.5 ms: 1.07x faster                                  |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                   |
| fannkuch                | 384 ms                                                 | 363 ms: 1.06x faster                                   |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                 |
| pprint_safe_repr        | 706 ms                                                 | 669 ms: 1.06x faster                                   |
| logging_silent          | 98.0 ns                                                | 93.3 ns: 1.05x faster                                  |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                  |
| scimark_fft             | 325 ms                                                 | 311 ms: 1.05x faster                                   |
| dulwich_log             | 64.0 ms                                                | 61.2 ms: 1.04x faster                                  |
| deepcopy_reduce         | 3.02 us                                                | 2.89 us: 1.04x faster                                  |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                   |
| genshi_xml              | 51.4 ms                                                | 49.3 ms: 1.04x faster                                  |
| sympy_str               | 291 ms                                                 | 280 ms: 1.04x faster                                   |
| regex_v8                | 22.2 ms                                                | 21.4 ms: 1.04x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                   |
| deepcopy_memo           | 35.8 us                                                | 34.5 us: 1.04x faster                                  |
| pickle_list             | 4.14 us                                                | 3.99 us: 1.04x faster                                  |
| tornado_http            | 96.5 ms                                                | 93.0 ms: 1.04x faster                                  |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                  |
| hexiom                  | 6.34 ms                                                | 6.11 ms: 1.04x faster                                  |
| nqueens                 | 83.8 ms                                                | 80.9 ms: 1.04x faster                                  |
| sqlglot_optimize        | 52.7 ms                                                | 51.0 ms: 1.03x faster                                  |
| logging_simple          | 6.02 us                                                | 5.83 us: 1.03x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                  |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                   |
| python_startup          | 8.58 ms                                                | 8.32 ms: 1.03x faster                                  |
| generators              | 73.5 ms                                                | 71.4 ms: 1.03x faster                                  |
| pathlib                 | 18.1 ms                                                | 17.6 ms: 1.03x faster                                  |
| genshi_text             | 21.5 ms                                                | 20.9 ms: 1.03x faster                                  |
| spectral_norm           | 98.1 ms                                                | 95.4 ms: 1.03x faster                                  |
| meteor_contest          | 104 ms                                                 | 102 ms: 1.03x faster                                   |
| sqlglot_parse           | 1.36 ms                                                | 1.33 ms: 1.03x faster                                  |
| deepcopy                | 341 us                                                 | 333 us: 1.03x faster                                   |
| pyflate                 | 419 ms                                                 | 409 ms: 1.02x faster                                   |
| thrift                  | 760 us                                                 | 742 us: 1.02x faster                                   |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                   |
| json                    | 4.87 ms                                                | 4.77 ms: 1.02x faster                                  |
| richards                | 46.1 ms                                                | 45.2 ms: 1.02x faster                                  |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                   |
| coverage                | 99.3 ms                                                | 97.7 ms: 1.02x faster                                  |
| regex_effbot            | 3.46 ms                                                | 3.40 ms: 1.02x faster                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.63 ms: 1.01x faster                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 67.0 ms: 1.01x faster                                  |
| chaos                   | 68.7 ms                                                | 67.8 ms: 1.01x faster                                  |
| raytrace                | 291 ms                                                 | 289 ms: 1.01x faster                                   |
| xml_etree_process       | 53.7 ms                                                | 53.3 ms: 1.01x faster                                  |
| crypto_pyaes            | 75.7 ms                                                | 75.4 ms: 1.00x faster                                  |
| mako                    | 9.83 ms                                                | 9.79 ms: 1.00x faster                                  |
| pickle_dict             | 31.2 us                                                | 31.1 us: 1.00x faster                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.03 ms: 1.00x faster                                  |
| unpickle_list           | 4.99 us                                                | 5.02 us: 1.01x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                 |
| regex_dna               | 203 ms                                                 | 205 ms: 1.01x slower                                   |
| chameleon               | 6.38 ms                                                | 6.46 ms: 1.01x slower                                  |
| xml_etree_generate      | 75.9 ms                                                | 76.9 ms: 1.01x slower                                  |
| django_template         | 32.3 ms                                                | 32.7 ms: 1.01x slower                                  |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                   |
| mdp                     | 2.63 sec                                               | 2.69 sec: 1.02x slower                                 |
| unpack_sequence         | 44.5 ns                                                | 45.7 ns: 1.03x slower                                  |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.60 us: 1.05x slower                                  |
| async_tree_memoization  | 624 ms                                                 | 657 ms: 1.05x slower                                   |
| nbody                   | 90.0 ms                                                | 94.8 ms: 1.05x slower                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (7): pylint, async_tree_cpu_io_mixed, scimark_lu, async_tree_none, unpickle, telco, logging_format
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: async_generators, asyncio_tcp, bench_mp_pool, bench_thread_pool, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221019-3.12.0a1+-5055300/bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300.json: mypy
