
# Results vs. 3.11.0

- fork: python
- ref: e3c3f9fec099fe78d2f9
- machine: linux-x86_64
- commit hash: e3c3f9f
- commit date: 2023-02-27
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 247 ms: 1.05x faster                                                   |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                 |
| html5lib       | 64.8 ms                                                | 61.3 ms: 1.06x faster                                                  |
| tornado_http   | 96.5 ms                                                | 94.2 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.5 ms: 1.06x faster                                                  |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                                   |
| nbody          | 90.0 ms                                                | 96.0 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 131 ms: 1.04x faster                                                   |
| regex_dna      | 203 ms                                                 | 198 ms: 1.03x faster                                                   |
| regex_v8       | 22.2 ms                                                | 21.7 ms: 1.03x faster                                                  |
| regex_effbot   | 3.46 ms                                                | 3.63 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.52 ms: 1.30x faster                                                  |
| unpickle_pure_python | 227 us                                                 | 195 us: 1.16x faster                                                   |
| pickle_pure_python   | 308 us                                                 | 280 us: 1.10x faster                                                   |
| json_loads           | 26.1 us                                                | 23.9 us: 1.09x faster                                                  |
| xml_etree_parse      | 160 ms                                                 | 150 ms: 1.07x faster                                                   |
| xml_etree_iterparse  | 104 ms                                                 | 99.8 ms: 1.04x faster                                                  |
| unpickle_list        | 4.99 us                                                | 5.08 us: 1.02x slower                                                  |
| xml_etree_process    | 53.7 ms                                                | 55.1 ms: 1.03x slower                                                  |
| pickle_dict          | 31.2 us                                                | 32.5 us: 1.04x slower                                                  |
| pickle_list          | 4.14 us                                                | 4.33 us: 1.05x slower                                                  |
| pickle               | 9.90 us                                                | 10.4 us: 1.05x slower                                                  |
| xml_etree_generate   | 75.9 ms                                                | 80.6 ms: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.95 ms: 1.04x slower                                                  |
| python_startup_no_site | 6.04 ms                                                | 6.49 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.0 ms: 1.10x faster                                                  |
| genshi_text     | 21.5 ms                                                | 20.9 ms: 1.03x faster                                                  |
| django_template | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                  |
| mako            | 9.83 ms                                                | 9.99 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.9 ms: 2.45x faster                                                  |
| asyncio_tcp             | 883 ms                                                 | 503 ms: 1.76x faster                                                   |
| json_dumps              | 12.4 ms                                                | 9.52 ms: 1.30x faster                                                  |
| mypy2                   | 420 ms                                                 | 332 ms: 1.27x faster                                                   |
| deltablue               | 3.66 ms                                                | 3.11 ms: 1.18x faster                                                  |
| unpickle_pure_python    | 227 us                                                 | 195 us: 1.16x faster                                                   |
| richards                | 46.1 ms                                                | 41.0 ms: 1.13x faster                                                  |
| coroutines              | 26.2 ms                                                | 23.7 ms: 1.10x faster                                                  |
| scimark_sor             | 115 ms                                                 | 104 ms: 1.10x faster                                                   |
| pickle_pure_python      | 308 us                                                 | 280 us: 1.10x faster                                                   |
| genshi_xml              | 51.4 ms                                                | 47.0 ms: 1.10x faster                                                  |
| fannkuch                | 384 ms                                                 | 352 ms: 1.09x faster                                                   |
| json_loads              | 26.1 us                                                | 23.9 us: 1.09x faster                                                  |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.09x faster                                                 |
| json                    | 4.87 ms                                                | 4.53 ms: 1.07x faster                                                  |
| xml_etree_parse         | 160 ms                                                 | 150 ms: 1.07x faster                                                   |
| nqueens                 | 83.8 ms                                                | 78.4 ms: 1.07x faster                                                  |
| logging_silent          | 98.0 ns                                                | 92.2 ns: 1.06x faster                                                  |
| go                      | 140 ms                                                 | 132 ms: 1.06x faster                                                   |
| float                   | 76.8 ms                                                | 72.5 ms: 1.06x faster                                                  |
| html5lib                | 64.8 ms                                                | 61.3 ms: 1.06x faster                                                  |
| hexiom                  | 6.34 ms                                                | 6.00 ms: 1.06x faster                                                  |
| unpack_sequence         | 44.5 ns                                                | 42.2 ns: 1.05x faster                                                  |
| crypto_pyaes            | 75.7 ms                                                | 72.1 ms: 1.05x faster                                                  |
| 2to3                    | 259 ms                                                 | 247 ms: 1.05x faster                                                   |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                 |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                   |
| spectral_norm           | 98.1 ms                                                | 94.0 ms: 1.04x faster                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 99.8 ms: 1.04x faster                                                  |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                  |
| raytrace                | 291 ms                                                 | 280 ms: 1.04x faster                                                   |
| scimark_fft             | 325 ms                                                 | 313 ms: 1.04x faster                                                   |
| regex_compile           | 136 ms                                                 | 131 ms: 1.04x faster                                                   |
| logging_simple          | 6.02 us                                                | 5.79 us: 1.04x faster                                                  |
| bench_thread_pool       | 817 us                                                 | 786 us: 1.04x faster                                                   |
| pprint_safe_repr        | 706 ms                                                 | 680 ms: 1.04x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| sqlglot_optimize        | 52.7 ms                                                | 50.8 ms: 1.04x faster                                                  |
| sympy_str               | 291 ms                                                 | 281 ms: 1.04x faster                                                   |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                                  |
| deepcopy_memo           | 35.8 us                                                | 34.6 us: 1.04x faster                                                  |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                  |
| pyflate                 | 419 ms                                                 | 405 ms: 1.03x faster                                                   |
| genshi_text             | 21.5 ms                                                | 20.9 ms: 1.03x faster                                                  |
| coverage                | 99.3 ms                                                | 96.5 ms: 1.03x faster                                                  |
| regex_dna               | 203 ms                                                 | 198 ms: 1.03x faster                                                   |
| regex_v8                | 22.2 ms                                                | 21.7 ms: 1.03x faster                                                  |
| deepcopy                | 341 us                                                 | 333 us: 1.03x faster                                                   |
| tornado_http            | 96.5 ms                                                | 94.2 ms: 1.02x faster                                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.48 ms: 1.02x faster                                                  |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                                   |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                 |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                  |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                   |
| pathlib                 | 18.1 ms                                                | 17.8 ms: 1.02x faster                                                  |
| logging_format          | 6.48 us                                                | 6.38 us: 1.02x faster                                                  |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                                   |
| dulwich_log             | 64.0 ms                                                | 63.3 ms: 1.01x faster                                                  |
| sympy_sum               | 166 ms                                                 | 165 ms: 1.01x faster                                                   |
| chaos                   | 68.7 ms                                                | 68.2 ms: 1.01x faster                                                  |
| django_template         | 32.3 ms                                                | 32.5 ms: 1.01x slower                                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 68.3 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 743 ms: 1.01x slower                                                   |
| mako                    | 9.83 ms                                                | 9.99 ms: 1.02x slower                                                  |
| telco                   | 6.43 ms                                                | 6.53 ms: 1.02x slower                                                  |
| unpickle_list           | 4.99 us                                                | 5.08 us: 1.02x slower                                                  |
| mdp                     | 2.63 sec                                               | 2.69 sec: 1.03x slower                                                 |
| xml_etree_process       | 53.7 ms                                                | 55.1 ms: 1.03x slower                                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.03x slower                                                  |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                                  |
| async_tree_memoization  | 624 ms                                                 | 649 ms: 1.04x slower                                                   |
| python_startup          | 8.58 ms                                                | 8.95 ms: 1.04x slower                                                  |
| pickle_dict             | 31.2 us                                                | 32.5 us: 1.04x slower                                                  |
| pickle_list             | 4.14 us                                                | 4.33 us: 1.05x slower                                                  |
| pickle                  | 9.90 us                                                | 10.4 us: 1.05x slower                                                  |
| regex_effbot            | 3.46 ms                                                | 3.63 ms: 1.05x slower                                                  |
| xml_etree_generate      | 75.9 ms                                                | 80.6 ms: 1.06x slower                                                  |
| sqlite_synth            | 2.48 us                                                | 2.64 us: 1.06x slower                                                  |
| nbody                   | 90.0 ms                                                | 96.0 ms: 1.07x slower                                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.49 ms: 1.08x slower                                                  |
| gc_traversal            | 3.82 ms                                                | 4.30 ms: 1.13x slower                                                  |
| async_generators        | 356 ms                                                 | 409 ms: 1.15x slower                                                   |
| dask                    | 365 ms                                                 | 498 ms: 1.36x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (10): djangocms, async_tree_none, sqlalchemy_imperative, chameleon, unpickle, async_tree_io, bench_mp_pool, thrift, deepcopy_reduce, scimark_lu
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
