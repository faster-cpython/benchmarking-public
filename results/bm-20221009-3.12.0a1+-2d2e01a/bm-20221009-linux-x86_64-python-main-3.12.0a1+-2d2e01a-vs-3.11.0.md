
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2d2e01a
- commit date: 2022-10-09
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.05x faster                                   |
| chameleon      | 6.38 ms                                                | 6.61 ms: 1.04x slower                                  |
| html5lib       | 64.8 ms                                                | 59.7 ms: 1.08x faster                                  |
| tornado_http   | 96.5 ms                                                | 93.4 ms: 1.03x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.3 ms: 1.06x faster                                  |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                   |
| nbody          | 90.0 ms                                                | 94.6 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                   |
| regex_v8       | 22.2 ms                                                | 22.1 ms: 1.01x faster                                  |
| regex_effbot   | 3.46 ms                                                | 3.60 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.44 ms: 1.31x faster                                  |
| unpickle_pure_python | 227 us                                                 | 204 us: 1.11x faster                                   |
| xml_etree_parse      | 160 ms                                                 | 146 ms: 1.10x faster                                   |
| json_loads           | 26.1 us                                                | 23.8 us: 1.10x faster                                  |
| pickle_pure_python   | 308 us                                                 | 293 us: 1.05x faster                                   |
| xml_etree_iterparse  | 104 ms                                                 | 101 ms: 1.03x faster                                   |
| pickle_list          | 4.14 us                                                | 4.06 us: 1.02x faster                                  |
| unpickle             | 13.3 us                                                | 13.0 us: 1.02x faster                                  |
| unpickle_list        | 4.99 us                                                | 5.02 us: 1.01x slower                                  |
| xml_etree_generate   | 75.9 ms                                                | 76.6 ms: 1.01x slower                                  |
| pickle_dict          | 31.2 us                                                | 31.9 us: 1.02x slower                                  |
| pickle               | 9.90 us                                                | 10.3 us: 1.04x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.38 ms: 1.02x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.06 ms: 1.00x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 49.1 ms: 1.05x faster                                  |
| genshi_text     | 21.5 ms                                                | 21.8 ms: 1.01x slower                                  |
| django_template | 32.3 ms                                                | 33.3 ms: 1.03x slower                                  |
| Geometric mean  | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.44 ms: 1.31x faster                                  |
| unpickle_pure_python    | 227 us                                                 | 204 us: 1.11x faster                                   |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.10x faster                                   |
| xml_etree_parse         | 160 ms                                                 | 146 ms: 1.10x faster                                   |
| json_loads              | 26.1 us                                                | 23.8 us: 1.10x faster                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.20 ms: 1.09x faster                                  |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.09x faster                                 |
| html5lib                | 64.8 ms                                                | 59.7 ms: 1.08x faster                                  |
| deltablue               | 3.66 ms                                                | 3.40 ms: 1.07x faster                                  |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                   |
| fannkuch                | 384 ms                                                 | 362 ms: 1.06x faster                                   |
| float                   | 76.8 ms                                                | 72.3 ms: 1.06x faster                                  |
| nqueens                 | 83.8 ms                                                | 79.2 ms: 1.06x faster                                  |
| logging_silent          | 98.0 ns                                                | 92.7 ns: 1.06x faster                                  |
| hexiom                  | 6.34 ms                                                | 6.02 ms: 1.05x faster                                  |
| pickle_pure_python      | 308 us                                                 | 293 us: 1.05x faster                                   |
| logging_simple          | 6.02 us                                                | 5.74 us: 1.05x faster                                  |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                  |
| chaos                   | 68.7 ms                                                | 65.5 ms: 1.05x faster                                  |
| coroutines              | 26.2 ms                                                | 25.0 ms: 1.05x faster                                  |
| genshi_xml              | 51.4 ms                                                | 49.1 ms: 1.05x faster                                  |
| 2to3                    | 259 ms                                                 | 248 ms: 1.05x faster                                   |
| dulwich_log             | 64.0 ms                                                | 61.1 ms: 1.05x faster                                  |
| deepcopy_memo           | 35.8 us                                                | 34.3 us: 1.04x faster                                  |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                   |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                   |
| deepcopy_reduce         | 3.02 us                                                | 2.90 us: 1.04x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                 |
| sympy_str               | 291 ms                                                 | 280 ms: 1.04x faster                                   |
| richards                | 46.1 ms                                                | 44.4 ms: 1.04x faster                                  |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                  |
| pprint_safe_repr        | 706 ms                                                 | 682 ms: 1.03x faster                                   |
| tornado_http            | 96.5 ms                                                | 93.4 ms: 1.03x faster                                  |
| deepcopy                | 341 us                                                 | 331 us: 1.03x faster                                   |
| thrift                  | 760 us                                                 | 737 us: 1.03x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                   |
| json                    | 4.87 ms                                                | 4.72 ms: 1.03x faster                                  |
| pyflate                 | 419 ms                                                 | 407 ms: 1.03x faster                                   |
| xml_etree_iterparse     | 104 ms                                                 | 101 ms: 1.03x faster                                   |
| scimark_fft             | 325 ms                                                 | 316 ms: 1.03x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                  |
| raytrace                | 291 ms                                                 | 284 ms: 1.03x faster                                   |
| sqlglot_optimize        | 52.7 ms                                                | 51.4 ms: 1.03x faster                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 66.3 ms: 1.03x faster                                  |
| python_startup          | 8.58 ms                                                | 8.38 ms: 1.02x faster                                  |
| pickle_list             | 4.14 us                                                | 4.06 us: 1.02x faster                                  |
| unpickle                | 13.3 us                                                | 13.0 us: 1.02x faster                                  |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                   |
| spectral_norm           | 98.1 ms                                                | 96.4 ms: 1.02x faster                                  |
| telco                   | 6.43 ms                                                | 6.32 ms: 1.02x faster                                  |
| mdp                     | 2.63 sec                                               | 2.59 sec: 1.01x faster                                 |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| sqlglot_parse           | 1.36 ms                                                | 1.34 ms: 1.01x faster                                  |
| sympy_sum               | 166 ms                                                 | 164 ms: 1.01x faster                                   |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                  |
| logging_format          | 6.48 us                                                | 6.43 us: 1.01x faster                                  |
| regex_v8                | 22.2 ms                                                | 22.1 ms: 1.01x faster                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 731 ms: 1.01x faster                                   |
| sqlglot_transpile       | 1.65 ms                                                | 1.64 ms: 1.01x faster                                  |
| crypto_pyaes            | 75.7 ms                                                | 75.3 ms: 1.00x faster                                  |
| python_startup_no_site  | 6.04 ms                                                | 6.06 ms: 1.00x slower                                  |
| generators              | 73.5 ms                                                | 73.8 ms: 1.00x slower                                  |
| unpickle_list           | 4.99 us                                                | 5.02 us: 1.01x slower                                  |
| xml_etree_generate      | 75.9 ms                                                | 76.6 ms: 1.01x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                 |
| genshi_text             | 21.5 ms                                                | 21.8 ms: 1.01x slower                                  |
| pickle_dict             | 31.2 us                                                | 31.9 us: 1.02x slower                                  |
| django_template         | 32.3 ms                                                | 33.3 ms: 1.03x slower                                  |
| async_tree_memoization  | 624 ms                                                 | 646 ms: 1.03x slower                                   |
| chameleon               | 6.38 ms                                                | 6.61 ms: 1.04x slower                                  |
| pickle                  | 9.90 us                                                | 10.3 us: 1.04x slower                                  |
| regex_effbot            | 3.46 ms                                                | 3.60 ms: 1.04x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.60 us: 1.05x slower                                  |
| nbody                   | 90.0 ms                                                | 94.6 ms: 1.05x slower                                  |
| unpack_sequence         | 44.5 ns                                                | 50.2 ns: 1.13x slower                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (7): pylint, coverage, regex_dna, scimark_lu, xml_etree_process, mako, async_tree_none
Ignored benchmarks (13) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: async_generators, asyncio_tcp, bench_mp_pool, bench_thread_pool, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221009-3.12.0a1+-2d2e01a/bm-20221009-linux-x86_64-python-main-3.12.0a1+-2d2e01a.json: mypy
